#!/usr/bin/env python3
"""Apply Round128 full-text reread and independent-review adjudication."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round128-selection.csv"
FULLTEXT = REPORTS / "round128-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
FIRST = REPORTS / "round128-firsthalf-decisions.tsv"
SECOND = REPORTS / "round128-secondhalf-decisions.tsv"
DECISIONS = REPORTS / "round128-decisions.tsv"
AUDIT = REPORTS / "round128-text-audit.tsv"
BLIND = REPORTS / "round128-independent-audit.tsv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields, rows, delimiter: str = "\t") -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    _, batch = read_csv(BATCH)
    fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
    _, first = read_csv(FIRST, "\t")
    _, second = read_csv(SECOND, "\t")
    _, blind = read_csv(BLIND, "\t")
    decisions_in = first + second
    assert len(batch) == len(fulltext) == len(decisions_in) == 14
    assert [row["id"] for row in batch] == [row["id"] for row in fulltext] == [row["id"] for row in decisions_in]
    assert sum(len(row.get("text") or "") for row in fulltext) == 29992
    assert len({row["id"] for row in decisions_in}) == 14

    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_fields, manual = read_csv(MANUAL)
    manual_by_id = {row["id"]: row for row in manual}
    assert len(manual_by_id) == len(manual) == 4305
    blind_by_id = {row["id"]: row for row in blind}
    assert len(blind_by_id) == 8

    # These are adjudicated from the article body.  Blind suggestions remain
    # traceable in round128-independent-audit.tsv and do not automatically
    # replace the main-thread decision.
    overrides = {
        "自由意志": {
            "primary": "A03", "secondary": "A14;A01", "status": "manual_provisional",
            "basis": "正文围绕意志和意识主体的定义展开，以不可预测性、观察对状态的影响、自我认识的不可靠性和意识边界为核心论证，并延伸讨论心理学作为科学的限度及人工智能是否可能具有意志；认识论事实与论证为中心，人工智能机器与心理主体为副轴。文章明确标注待续，后续论证可能改变范围，因此保留暂定。",
            "risk": "关于自由意志、意识不可预测性、量子认知、心理学科学地位及人工智能意识的判断均未独立核验；属于作者哲学论证，不构成心理学、神经科学、AI安全或法律结论。",
        },
        "芯片": {"primary": "A13", "secondary": "A07;A20"},
        "动物的恐惧": {"primary": "A18", "secondary": "A03;A20"},
        "最强耐力": {"primary": "A18", "secondary": "A20;A03"},
        "为中华之崛起而读书": {
            "primary": "A04", "secondary": "A08;A20",
            "basis": "正文把读书解释为面向国家复兴需求进行知识构建、技能学习和事业规划，重点讨论国家投资、产业需求、个人职业回报与具体能力标准；教育学习与能力形成为中心，财富劳动回报和历史文明经验为副轴。未把战争外交或族群身份作为正文主线。",
            "risk": "关于国家制度、公共投资规模、产业需求、个人回报及历史案例均未独立核验；国家需求导向不等于个人必须服从单一职业路径，不构成教育、就业、投资或国家政策建议。",
        },
        "天命人": {"primary": "A01", "secondary": "A04;A05"},
        "人来": {"primary": "A06", "secondary": "A05;A07"},
        "锚链": {"primary": "A01", "secondary": "A03"},
        "完美这事": {"primary": "A01", "secondary": "A03"},
        "远小人": {
            "primary": "A06", "secondary": "A01",
            "basis": "正文围绕如何防止在人际交往中被算计，提出立威、信用、边界和冲突威慑的行为策略；关系冲突与社会防卫为主，主体姿态与恐惧处理为副轴。A00不再保留，A10不足以代表全文的法律/司法中心。",
            "risk": "鼓吹狠辣诡谲、同归于尽和以恐惧建立威慑，可能升级现实冲突；信用、威慑效果和心理判断未经验证，不是法律、安全、报复或武力行动建议。",
        },
        "0-1-2-3": {
            "primary": "A03", "secondary": "A13",
            "basis": "正文借手机照片整理说明分类算法、标签化、分层筛选和渐进复访，核心是如何降低判断复杂度并形成可复用的分类方法；认识论、分类论证和决策流程为主，技术/信息处理为副轴。",
            "risk": "高维向量计算、算法可靠性、分层比例和复访机制均是解释性类比而非测量结果；方法未讨论备份、隐私、误删和跨设备恢复，不构成数据安全或机器学习工程规范。",
        },
        "清静无为": {"primary": "A20", "secondary": "A10;A11"},
        "困兽": {"primary": "A06", "secondary": "A01;A05"},
        "冠军病": {"primary": "A01", "secondary": "A09;A03"},
    }

    decisions, audits, updates = [], [], []
    for batch_row, article, source in zip(batch, fulltext, decisions_in):
        title = batch_row["title"]
        current = manual_by_id[batch_row["id"]]
        assert current["title"] == title
        override = overrides[title]
        primary = override["primary"]
        secondary = override["secondary"]
        status = override.get("status", source["status"])
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and all(code in codes and code != primary for code in secondary_codes)
        assert len(secondary_codes) <= 3 and len(secondary_codes) == len(set(secondary_codes))
        assert len(article.get("text") or "") == int(batch_row["body_char_count"])
        basis = override.get("basis", source["basis"])
        risk = override.get("risk", source["risk_boundary"])
        decisions.append({
            "id": batch_row["id"], "title": title,
            "old_primary": current["primary_print_topic_code"], "old_secondary": current["secondary_print_topic_codes"],
            "new_primary": primary, "new_secondary": secondary, "status": status,
            "decision": "adjudicated_reread", "basis": basis, "risk_boundary": risk,
        })
        audits.append({
            "id": batch_row["id"], "title": title, "text_chars": batch_row["body_char_count"],
            "current_primary": current["primary_print_topic_code"], "current_secondary": current["secondary_print_topic_codes"],
            "recommended_primary": primary, "recommended_secondary": secondary, "recommended_status": status,
            "decision_basis": basis, "fact_risk": risk,
        })
        desired = {"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary,
                   "classification_status": status, "decision_basis": basis}
        if all(current.get(key, "") == value for key, value in desired.items()):
            continue
        assert current["classification_status"] == "manual_provisional"
        current.update(desired)
        current["review_note"] = f"Round128 full-text reread with independent-review adjudication; body_chars={batch_row['body_char_count']}; Fact-risk boundary: {risk}"
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round128-text-reread+round128-adjudication").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    atomic_write(DECISIONS, fields, decisions)
    atomic_write(AUDIT, ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"], audits)
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual, delimiter=",")
    print(json.dumps({"round": 128, "records": 14, "body_chars": 29992, "updated": len(updates),
                      "confirmed": sum(row["status"] == "manual_confirmed" for row in decisions),
                      "provisional": sum(row["status"] == "manual_provisional" for row in decisions),
                      "dry_run": args.dry_run}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
