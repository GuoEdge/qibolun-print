#!/usr/bin/env python3
"""Apply the explicit Round124 blind-review boundary corrections."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round124-decisions.tsv"
AUDIT = REPORTS / "round124-text-audit.tsv"

CORRECTIONS = {
    "964d3312-f52b-5cdf-a3cb-ee6085fb0dd0": {
        "title": "同性恋",
        "old": ("A02", "A11", "manual_confirmed"),
        "new": ("A11", "A02", "manual_confirmed"),
        "basis": "盲审修正：题目明确问基督教中的罪与爱，宗教规范是正文中心；性取向/性伦理为副轴。",
        "risk": "基督教教义及“爱即非罪”的规范判断未独立核验。",
    },
    "5316551a-199f-5363-8436-1c4d4a72bbc2": {
        "title": "酒神与天神",
        "old": ("A11", "A01", "manual_provisional"),
        "new": ("A11", "A03", "manual_provisional"),
        "basis": "盲审修正：宗教/神话入口仍是主轴，但以麻醉剂替代兴奋剂的回答属于概念论证，不足以推出心理主体副轴。",
        "risk": "没有回答神话谱系；药物与人类终极方案的判断未独立核验。",
    },
    "85aecfc3-f160-531a-8404-42441717edd4": {
        "title": "行为艺术",
        "old": ("A15", "", "manual_confirmed"),
        "new": ("A15", "A10", "manual_provisional"),
        "basis": "盲审修正：行为艺术仍是正文场景中心，但“追着打”及录像回应涉及人身、财产和证据边界，保留司法/安全副轴并暂定。",
        "risk": "追打、破坏和录像建议是反讽表达，可能涉及伤害、财产损毁和取证合法性，未核验且不构成行动建议。",
    },
}


def read_rows(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_rows(path: Path, fields, rows, delimiter: str = ","):
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    manual_fields, manual = read_rows(MANUAL)
    decision_fields, decisions = read_rows(DECISIONS, "\t")
    audit_fields, audits = read_rows(AUDIT, "\t")
    manual_by_id = {row["id"]: row for row in manual}
    decision_by_id = {row["id"]: row for row in decisions}
    audit_by_id = {row["id"]: row for row in audits}
    assert len(manual_by_id) == 4305 and len(decision_by_id) == len(audit_by_id) == 50

    for aid, spec in CORRECTIONS.items():
        row = manual_by_id[aid]
        assert row["title"] == spec["title"]
        old_primary, old_secondary, old_status = spec["old"]
        new_primary, new_secondary, new_status = spec["new"]
        if (row["primary_print_topic_code"], row["secondary_print_topic_codes"], row["classification_status"]) == spec["old"]:
            row["primary_print_topic_code"] = new_primary
            row["secondary_print_topic_codes"] = new_secondary
            row["classification_status"] = new_status
        else:
            assert (row["primary_print_topic_code"], row["secondary_print_topic_codes"], row["classification_status"]) == spec["new"]
        row["decision_basis"] = spec["basis"]
        row["review_note"] = f"Round124 blind-review correction; {spec['risk']}"
        row["reviewer"] = (row.get("reviewer", "main-thread") + "+round124-blind-review").strip("+")
        row["reviewed_at"] = date.today().isoformat()

        d = decision_by_id[aid]
        d["new_primary"] = new_primary
        d["new_secondary"] = new_secondary
        d["status"] = new_status
        d["decision"] = "blind_review_correction"
        d["basis"] = spec["basis"]
        d["risk_boundary"] = spec["risk"]
        a = audit_by_id[aid]
        a["recommended_primary"] = new_primary
        a["recommended_secondary"] = new_secondary
        a["recommended_status"] = new_status
        a["decision_basis"] = spec["basis"]
        a["fact_risk"] = spec["risk"]

    write_rows(MANUAL, manual_fields, manual)
    write_rows(DECISIONS, decision_fields, decisions, "\t")
    write_rows(AUDIT, audit_fields, audits, "\t")
    print({"round": 124, "corrections": len(CORRECTIONS), "provisional_delta": 1, "ids": list(CORRECTIONS)})


if __name__ == "__main__":
    main()
