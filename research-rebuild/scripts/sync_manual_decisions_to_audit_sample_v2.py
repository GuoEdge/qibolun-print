#!/usr/bin/env python3
"""Refresh only manual-decision projections in the existing audit sample."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
SAMPLE_CSV = REPORTS / "print-topic-audit-sample-v2.csv"
SAMPLE_JSONL = REPORTS / "print-topic-audit-sample-v2.jsonl"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)


fields, sample = read_csv(SAMPLE_CSV)
_, manual_rows = read_csv(MANUAL)
manual = {row["id"]: row for row in manual_rows}
updated = []

for row in sample:
    decision = manual.get(row.get("id", ""))
    if not decision:
        continue
    status = decision.get("classification_status", "")
    if status == "manual_confirmed":
        audit_decision = "confirmed"
    elif status == "manual_provisional":
        note = f"{decision.get('review_note', '')} {decision.get('decision_basis', '')}"
        audit_decision = (
            "needs_image_review"
            if "图" in note or row.get("image_review_required") == "true"
            else "uncertain"
        )
    else:
        audit_decision = "uncertain"
    projection = {
        "audit_decision": audit_decision,
        "reviewer": decision.get("reviewer", ""),
        "reviewed_at": decision.get("reviewed_at", ""),
        "decision_primary_print_topic": decision.get("primary_print_topic_code", ""),
        "decision_secondary_print_topics": decision.get("secondary_print_topic_codes", ""),
        "decision_note": "; ".join(
            value for value in (
                decision.get("decision_basis", ""),
                decision.get("review_note", ""),
            ) if value
        ),
    }
    if any(row.get(key, "") != value for key, value in projection.items()):
        row.update(projection)
        updated.append(row["id"])

with SAMPLE_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(sample)
with SAMPLE_JSONL.open("w", encoding="utf-8") as fh:
    for row in sample:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")

print(json.dumps({"sample_records": len(sample), "manual_projection_updates": len(updated)}, ensure_ascii=False, indent=2))
