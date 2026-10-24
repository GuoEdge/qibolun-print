#!/usr/bin/env python3
"""Apply Round127 full-text reread and independent-review adjudication."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round127-selection.csv"
FULLTEXT = REPORTS / "round127-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round127-decisions.tsv"
AUDIT = REPORTS / "round127-text-audit.tsv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

# Independent review read the article text before consulting these decisions.
# Only two material secondary-axis additions survived adjudication.
OVERRIDES = {
    "民主专制": {
        "secondary": "A03;A07;A11",
        "basis": "全文讨论名义制度与实际权力、国家及组织的合作机制，论证“民主/专制”二分与现实运转的差异，并以军队、企业和国家治理比较有效性；国家制度与公共治理为主轴，概念论证、组织协作和自然法/人权为副轴。",
        "risk": "关于制度史、组织效率、军队与企业治理及“实质精英共和”命题均未独立核验；“尽可能排除民主”是作者规范性判断，不构成政治制度、组织管理或人权建议。",
    },
    "完美传染病": {
        "secondary": "A10;A13;A14",
        "basis": "全文以高密度城市面对高传染性疾病的系统性脆弱性为中心，提出医学进步、社会感知与干预能力两类应对，并延伸到检测、消毒、防护装备、远程办公和无人化；医疗疾病与照料为主轴，公共管理、技术工程和机器/自动化未来秩序为副轴。",
        "risk": "病毒特征、超级城市风险、武汉封城效果、各国治理能力及检测/消毒/防护产品前景均未独立核验；“绝对感知和掌控”涉及重大权利与治理风险，不构成防疫、投资或公共管理建议。",
    },
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
    decision_fields_in, decisions_in = read_csv(DECISIONS, "\t")
    assert len(batch) == len(fulltext) == len(decisions_in) == 10
    assert [row["id"] for row in batch] == [row["id"] for row in fulltext] == [row["id"] for row in decisions_in]
    assert [row["title"] for row in batch] == [row["title"] for row in fulltext] == [row["title"] for row in decisions_in]
    assert sum(len(row.get("text") or "") for row in fulltext) == 29974
    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_by_id = {row["id"]: row for row in manual}
    assert len(manual_by_id) == len(manual) == 4305

    decisions, audits, updates = [], [], []
    for batch_row, article, source_decision in zip(batch, fulltext, decisions_in):
        title = batch_row["title"]
        primary = source_decision.get("new_primary", source_decision.get("primary", ""))
        source_secondary = source_decision.get("new_secondary", source_decision.get("secondary", ""))
        secondary = OVERRIDES.get(title, {}).get("secondary", source_secondary)
        status = source_decision["status"]
        source_basis = source_decision.get("basis", "")
        source_risk = source_decision.get("risk_boundary", source_decision.get("risk_note", ""))
        basis = OVERRIDES.get(title, {}).get("basis", source_basis)
        risk = OVERRIDES.get(title, {}).get("risk", source_risk)
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and all(code in codes and code != primary for code in secondary_codes)
        assert len(secondary_codes) <= 3 and len(secondary_codes) == len(set(secondary_codes))
        assert len(article.get("text") or "") == int(batch_row["body_char_count"])
        current = manual_by_id[batch_row["id"]]
        assert current["title"] == title
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
        desired = {"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary, "classification_status": status, "decision_basis": basis}
        if all(current.get(key, "") == value for key, value in desired.items()):
            continue
        assert current["classification_status"] == "manual_provisional"
        assert current["primary_print_topic_code"] == batch_row.get("candidate_primary", "")
        assert current["secondary_print_topic_codes"] == batch_row.get("candidate_secondary", "")
        current.update(desired)
        current["review_note"] = f"Round127 full-text reread with independent-review adjudication; body_chars={batch_row['body_char_count']}; Fact-risk boundary: {risk}"
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round127-text-reread+round127-adjudication").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    decision_fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    audit_fields = ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"]
    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(AUDIT, audit_fields, audits, "\t")
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual)
    print(json.dumps({"round": 127, "records": len(batch), "body_chars": 29974, "updated": len(updates), "confirmed": sum(row["status"] == "manual_confirmed" for row in decisions), "provisional": sum(row["status"] == "manual_provisional" for row in decisions), "secondary_adjudications": len(OVERRIDES), "dry_run": args.dry_run}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
