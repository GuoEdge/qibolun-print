#!/usr/bin/env python3
"""Apply the Round126 full-text reread after independent review adjudication."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round126-selection.csv"
FULLTEXT = REPORTS / "round126-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round126-decisions.tsv"
AUDIT = REPORTS / "round126-text-audit.tsv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

# The independent review was not blind: it had already seen the first-half
# table. Its disagreements were adjudicated against the complete article text.
DECISIONS_BY_TITLE = {
    "军训": ("A12", "A04;A09", "manual_confirmed", "全文以高中和大学军训作为义务兵役制、地方动员体系和总体军事准备的年度检验为中心，军事动员与国家安全是正文主轴，教育训练和训练伤亡为边界副轴。", "军训事故率、强制体检、操场军事用途、动员规模、三个月训练能力、卫星可见性和战争推演均未独立核验；不构成军事动员或医疗建议。"),
    "非洲、非洲": ("A12", "A16;A10", "manual_confirmed", "全文比较欧美与非洲/第三世界的援助依赖，提出中国应把外交、产能和援助重点放在第三世界并以长期示范建立友好关系；国际战略外交为主，舆论传播和国家稳定为副。", "疫情传播、欧美政治危机、人口产能、援助时效、国家政治选择和中国外交计划均未独立核验；不构成现实外交建议。"),
    "七岁": ("A04", "A05;A01;A21", "manual_confirmed", "全文以六至七岁语言/纪律与长期记忆的所谓分界为起点，主张学龄前优先通过游戏、运动和互动形成身体、情绪及社交基础；教育学习与能力形成为主，家庭教养、情绪和运动为副。", "儿童记忆、语言临界年龄、心肺与情绪关系、学习迁移、入学年龄及七岁前活动建议均未作发展心理学或教育实证核验。"),
    "强国的度": ("A12", "A08;A20", "manual_confirmed", "全文借不可妥协的财产与继承假设论证国家交往的根本利益红线，以沙伊复交解释强权越线后影响力归零，并归结于文化禀赋和大国治理上限；国际秩序与战略外交为主。", "沙伊外交、美国中东政策、国家民意机制、文化禀赋与国运因果均未独立核验；不构成外交或国家安全决策建议。"),
    "乱伦": ("A10", "A05;A02;A20", "manual_confirmed", "全文把“伦”界定为人际关系社会规范，区分直接受害与隐蔽破坏，解释公共干预、执法成本和近亲性行为标签，并以社会危机感说明规范宽严变化；法律/公共秩序为主。", "乱伦词源与范围、近亲行为后果、执法成本、危机感与自由度关系及法律历史均未独立核验；不构成法律、伦理或性健康建议。"),
    "聪明族": ("A20", "A17;A03", "manual_confirmed", "全文反对把中国人和犹太人简单称为最聪明/最勤劳民族，以民族概念边界、跨地域文明经验和历史自觉解释差异；历史文明为主，族群身份和概念论证为副。", "关于民族概念史、中国与犹太人历史角色及族群概括均未独立核验，含本质化风险。"),
    "生而平等": ("A03", "A10;A11", "manual_confirmed", "正文中心是平等概念定义、法律程序平等与结果平等的分歧，并比较制度模型及自然法意义上的平等；认识论/概念论证为主，法律制度和自然法为副。", "关于资本主义、再分配、代际优势和历史制度的概括属于作者政治哲学论证，未作外部事实或规范共识核验。"),
    "海外团结": ("A17", "A10;A20", "manual_confirmed", "正文围绕海外华人身份保持、组织团结与所在国忠诚审查之间的张力展开，族群身份秩序为中心，政治参与/安全空间及历史例证为副。", "关于政治审查、代理人判断、移民融合和历史后果的断言未经逐项核验，不能推断现实群体统一动机。"),
    "财富观": ("A11", "A08;A18;A05", "manual_provisional", "正文以财富本质、财富管理、节俭、投资、慈善和财富传承为连续主线，但其规范核心是“神赐财富”的自然法与神学责任；宗教自然法为主，财富市场、生态可持续性和代际责任为副。正文以“未完，待续”结束，暂不确认。", "财富由上帝赐予、自然法惩罚、可持续性、投资和医疗支出等均为作者神学/经济规范性主张，未作金融、生态、医疗或事实核验；未完部分可能改变重心。"),
    "内务班底": ("A05", "A07", "manual_confirmed", "全文最终围绕“家族成员不等于家庭成员”区分保姆、私人管家、内务班子和继承人培养，家庭亲属与代际秩序为主，组织雇佣与合作规则为副；虽有组织管理材料，但不能据职权词汇倒置正文中心。", "关于终身雇佣、退休而非解雇、历史联姻后果及家族治理的概括未经法律、历史或劳动关系核验；不替代劳动合同或家庭教育意见。"),
    "忠与叛": ("A17", "A20", "manual_provisional", "正文从东亚外交语境进入，但主体篇幅实际把日本人整体的忠诚/叛意张力解释为日本文化和身份存在的核心；族群身份秩序为主，历史文明解释为副。因题干与正文错位且族群泛化密集，保留暂定。", "把日本人整体归为忠诚与叛意并存并解释现实外交，是未经证实的民族性格和因果概括；会晤信号、国家战略和历史判断均需外部资料核验。"),
    "对待讨厌的人": ("A01", "A06", "manual_provisional", "正文是处理厌恶与伤害后的内在步骤清单：理解、宽恕、反省、补偿、学习、怜悯与接受道歉的准备；情绪/主体自我调节为主，人际关系边界为副。因仅135字且没有具体情境，保留暂定。", "宽恕、怜悯、断联和接受道歉并非适用于所有伤害情形；未说明持续威胁、虐待或违法情境，不能替代安全计划、心理支持或法律建议。"),
}


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields, rows, delimiter: str = ",") -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    _, batch = read_csv(BATCH)
    fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
    manual_fields, manual = read_csv(MANUAL)
    assert len(batch) == len(fulltext) == 12
    assert [row["id"] for row in batch] == [row["id"] for row in fulltext]
    assert [row["title"] for row in batch] == [row["title"] for row in fulltext]
    assert sum(len(row.get("text") or "") for row in fulltext) == 29954
    assert {row["title"] for row in batch} == set(DECISIONS_BY_TITLE)
    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_by_id = {row["id"]: row for row in manual}
    assert len(manual_by_id) == len(manual) == 4305

    decision_fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    audit_fields = ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"]
    decisions, audits, updates = [], [], []
    for row, article in zip(batch, fulltext):
        title = row["title"]
        primary, secondary, status, basis, risk = DECISIONS_BY_TITLE[title]
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and all(code in codes and code != primary for code in secondary_codes)
        assert len(secondary_codes) <= 3 and len(secondary_codes) == len(set(secondary_codes))
        assert len(article.get("text") or "") == int(row["body_char_count"])
        current = manual_by_id[row["id"]]
        assert current["title"] == title
        assert current["classification_status"] in {"manual_confirmed", "manual_provisional"}
        decisions.append({
            "id": row["id"], "title": title,
            "old_primary": current["primary_print_topic_code"], "old_secondary": current["secondary_print_topic_codes"],
            "new_primary": primary, "new_secondary": secondary, "status": status,
            "decision": "retain" if (primary == current["primary_print_topic_code"] and secondary == current["secondary_print_topic_codes"] and status == current["classification_status"]) else "adjudicated_reread",
            "basis": basis, "risk_boundary": risk,
        })
        audits.append({
            "id": row["id"], "title": title, "text_chars": row["body_char_count"],
            "current_primary": current["primary_print_topic_code"], "current_secondary": current["secondary_print_topic_codes"],
            "recommended_primary": primary, "recommended_secondary": secondary, "recommended_status": status,
            "decision_basis": basis, "fact_risk": risk,
        })
        desired = {"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary, "classification_status": status, "decision_basis": basis}
        if all(current.get(key, "") == value for key, value in desired.items()):
            continue
        assert current["classification_status"] == "manual_provisional"
        assert current["primary_print_topic_code"] == row.get("candidate_primary", "")
        assert current["secondary_print_topic_codes"] == row.get("candidate_secondary", "")
        current.update(desired)
        current["review_note"] = f"Round126 full-text reread with independent-review adjudication; body_chars={row['body_char_count']}; Fact-risk boundary: {risk}"
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round126-text-reread+round126-adjudication").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(AUDIT, audit_fields, audits, "\t")
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual)
    print(json.dumps({"round": 126, "records": len(batch), "body_chars": 29954, "updated": len(updates), "confirmed": sum(row["status"] == "manual_confirmed" for row in decisions), "provisional": sum(row["status"] == "manual_provisional" for row in decisions), "dry_run": args.dry_run}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
