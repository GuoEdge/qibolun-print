#!/usr/bin/env python3
"""Apply Round129 full-text reread and adjudication."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round129-selection.csv"
FULLTEXT = REPORTS / "round129-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
FIRST = REPORTS / "round129-firsthalf-decisions.tsv"
SECOND = REPORTS / "round129-secondhalf-decisions.tsv"
DECISIONS = REPORTS / "round129-decisions.tsv"
AUDIT = REPORTS / "round129-text-audit.tsv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields, rows, delimiter: str) -> None:
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
    source_decisions = first + second
    assert len(batch) == len(fulltext) == len(source_decisions) == 20
    assert [r["id"] for r in batch] == [r["id"] for r in fulltext] == [r["id"] for r in source_decisions]
    assert sum(len(r.get("text") or "") for r in fulltext) == 29993
    assert len({r["id"] for r in source_decisions}) == 20

    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {r["code"] for r in registry}
    manual_fields, manual = read_csv(MANUAL)
    manual_by_id = {r["id"]: r for r in manual}
    assert len(manual_by_id) == len(manual) == 4305

    # Body-first adjudications.  These deliberately remove unsupported axes
    # instead of inheriting a machine candidate or a rhetorical association.
    overrides = {
        "烂不透": {
            "primary": "A01", "secondary": "A08;A11",
            "basis": "正文围绕人生陷入困境时如何在高风险谋生与自取灭亡之间保留翻身余地，随后讨论温饱尚在者用小快乐、小努力和稳定收入拖住生活；主体处境与生存选择为中心，财富劳动和自然法/道德边界为副轴。",
            "risk": "海外高风险工作、保险、赌毒、自杀风险及债务和生活成本判断未经核验；文本可能被绝望者误读为冒险鼓励，不构成危机干预、医疗、保险、债务或职业安全建议。",
        },
        "拼命解决": {
            "primary": "A10", "secondary": "A05", "status": "manual_provisional",
            "basis": "正文仅147字，围绕岳父可能以暴力替子女解决问题，指出法律、道德和公众舆论未必能在事后阻止生命行动；刑事暴力与现实安全风险为主轴，家庭亲属关系为副轴。原回答已搬迁，不能补入未提供的法律分析，因此保留暂定。",
            "risk": "案件事实、判决、刑法适用和暴力风险均未核验；不构成刑事法律意见、家庭冲突处置、报复或人身安全行动建议。",
        },
    }

    decisions, audits, updates = [], [], []
    for batch_row, article, source in zip(batch, fulltext, source_decisions):
        title = batch_row["title"]
        current = manual_by_id[batch_row["id"]]
        assert current["title"] == title
        override = overrides.get(title, {})
        primary = override.get("primary", source["new_primary"])
        secondary = override.get("secondary", source["new_secondary"])
        status = override.get("status", source["status"])
        secondary_codes = [c for c in secondary.split(";") if c]
        assert primary in codes and all(c in codes and c != primary for c in secondary_codes)
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
            "recommended_primary": primary, "recommended_secondary": secondary,
            "recommended_status": status, "decision_basis": basis, "fact_risk": risk,
        })
        desired = {"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary,
                   "classification_status": status, "decision_basis": basis}
        if all(current.get(k, "") == v for k, v in desired.items()):
            continue
        assert current["classification_status"] == "manual_provisional"
        current.update(desired)
        current["review_note"] = f"Round129 full-text reread with independent-review adjudication; body_chars={batch_row['body_char_count']}; Fact-risk boundary: {risk}"
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round129-text-reread+round129-adjudication").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    decision_fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    audit_fields = ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"]
    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(AUDIT, audit_fields, audits, "\t")
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual, ",")
    print(json.dumps({
        "round": 129, "records": 20, "body_chars": 29993, "updated": len(updates),
        "confirmed": sum(r["status"] == "manual_confirmed" for r in decisions),
        "provisional": sum(r["status"] == "manual_provisional" for r in decisions),
        "dry_run": args.dry_run,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
