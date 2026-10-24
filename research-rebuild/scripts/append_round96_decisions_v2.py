#!/usr/bin/env python3
"""Validate and append independently reviewed Round 96 decisions."""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-budget-batch-v2-round96-90k.csv"
FULLTEXT = REPORTS / "round96-fulltext.json"
DECISIONS = REPORTS / "round96-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


_, batch = read_csv(BATCH)
_, decisions = read_csv(DECISIONS, "\t")
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
fields, manual = read_csv(MANUAL)
_, registry_rows = read_csv(DATA / "print-topic-registry-v2.csv")
codes = {row["code"] for row in registry_rows}

assert 0 < len(batch) <= 50
assert len(batch) == len(decisions) == len(fulltext)
batch_ids = [row["id"] for row in batch]
assert len(batch_ids) == len(set(batch_ids)), "duplicate ID in selected batch"
assert batch_ids == [row["id"] for row in fulltext] == [row["id"] for row in decisions]
assert [row["title"] for row in batch] == [row["title"] for row in fulltext] == [row["title"] for row in decisions]
assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
body_chars = sum(len(row.get("text") or "") for row in fulltext)
assert body_chars <= 90000
assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)

manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual), "duplicate ID in manual decision table"
existing_ids = set(batch_ids).intersection(manual_by_id)
assert not existing_ids or existing_ids == set(batch_ids), (
    "partial Round 96 presence in manual table; inspect IDs before proceeding"
)

new_rows = []
for batch_row, article, decision in zip(batch, fulltext, decisions):
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert decision["primary"] in codes
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip()
    review_note = (
        f"Round 96 full text; body_chars={batch_row['body_char_count']}; "
        f"batch={BATCH.name}; independent reads=round96 first 1-25 and second 26-50; "
        "risk notes separated from topic status"
    )
    risk = decision.get("risk_note", "").strip()
    if risk:
        review_note += f"; claim/safety note: {risk}"
    new_rows.append({
        "id": batch_row["id"],
        "title": batch_row["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": decision["status"],
        "decision_basis": decision["basis"],
        "review_note": review_note,
        "reviewer": "main-thread+independent-review",
        "reviewed_at": date.today().isoformat(),
    })

already_appended = bool(existing_ids)
if already_appended:
    for row in new_rows:
        current = manual_by_id[row["id"]]
        for key in (
            "title",
            "primary_print_topic_code",
            "secondary_print_topic_codes",
            "classification_status",
            "decision_basis",
        ):
            assert current.get(key, "") == row[key], f"existing Round 96 mismatch for {row['id']}: {key}"
elif not args.dry_run:
    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
        writer.writerows(new_rows)
    temporary.replace(MANUAL)

print(json.dumps({
    "operation": "already_present_verified" if already_appended else "append",
    "round96_records": len(new_rows),
    "confirmed": sum(row["classification_status"] == "manual_confirmed" for row in new_rows),
    "provisional": sum(row["classification_status"] == "manual_provisional" for row in new_rows),
    "body_chars": body_chars,
    "manual_total_after": len(manual) if already_appended else len(manual) + len(new_rows),
    "dry_run": args.dry_run,
}, ensure_ascii=False, indent=2))
