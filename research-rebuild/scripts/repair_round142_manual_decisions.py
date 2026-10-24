#!/usr/bin/env python3
"""Apply the independently audited Round142 revisions to existing rows."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round142-decisions.tsv"
LOG = REPORTS / "round142-manual-revision-log.csv"

def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)

manual_fields, manual_rows = read_csv(MANUAL)
decision_fields, decision_rows = read_csv(DECISIONS, "\t")
assert manual_fields
assert len(decision_rows) == 20
assert len({row["id"] for row in decision_rows}) == len(decision_rows)

by_id = {row["id"]: row for row in manual_rows}
assert len(by_id) == len(manual_rows), "manual table has duplicate IDs"
missing = [row["id"] for row in decision_rows if row["id"] not in by_id]
assert not missing, f"Round142 IDs missing from manual table: {missing}"

revision_rows = []
for decision in decision_rows:
    current = by_id[decision["id"]]
    old_primary = current.get("primary_print_topic_code", "")
    old_secondary = current.get("secondary_print_topic_codes", "")
    old_status = current.get("classification_status", "")
    basis = decision["basis"]
    risk = decision["risk_note"]
    marker = "Round142 independent blind reread"
    note = current.get("review_note", "").rstrip("; ")
    addition = (
        f"{marker}; body_chars verified from round142-fulltext.json; "
        f"old_primary={old_primary}; old_secondary={old_secondary}; "
        f"old_status={old_status}; new_primary={decision['primary']}; "
        f"new_secondary={decision['secondary']}; {risk}"
    )
    if marker not in note:
        note = f"{note}; {addition}" if note else addition
    current.update({
        "title": decision["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": decision["secondary"],
        "classification_status": decision["status"],
        "decision_basis": basis,
        "review_note": note,
        "reviewer": (current.get("reviewer", "") + "+round142-blind-review").strip("+") if "round142-blind-review" not in current.get("reviewer", "") else current.get("reviewer", ""),
        "reviewed_at": date.today().isoformat(),
    })
    revision_rows.append({
        "id": decision["id"],
        "title": decision["title"],
        "old_primary": old_primary,
        "old_secondary": old_secondary,
        "old_status": old_status,
        "new_primary": decision["primary"],
        "new_secondary": decision["secondary"],
        "new_status": decision["status"],
        "basis": basis,
        "risk_note": risk,
        "revision_source": "round142-decisions.tsv + independent blind reread",
        "revised_at": date.today().isoformat(),
    })

temporary = MANUAL.with_suffix(".csv.tmp")
with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=manual_fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(manual_rows)
temporary.replace(MANUAL)

log_fields = list(revision_rows[0])
with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=log_fields)
    writer.writeheader()
    writer.writerows(revision_rows)

print({"updated": len(revision_rows), "manual_total": len(manual_rows), "revision_log": str(LOG)})
