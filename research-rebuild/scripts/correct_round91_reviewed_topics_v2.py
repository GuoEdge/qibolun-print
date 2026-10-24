#!/usr/bin/env python3
"""Apply the independently reviewed Round 91 topic-boundary corrections."""
import argparse
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-budget-batch-v2-round91-90k.csv"
DECISIONS = REPORTS / "round91-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

EXPECTED_OLD = {
    "小联盟": ("A05", ""),
    "稳定收入": ("A06", "A08"),
    "天妒": ("A02", "A01;A06"),
    "多了一道五花肉": ("A07", "A02"),
    "madness": ("A21", ""),
    "牙关紧咬": ("A05", "A01"),
    "吵架": ("A06", "A05"),
    "不好骗": ("A03", ""),
    "及格主义": ("A01", ""),
}

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


_, batch = read_csv(BATCH)
_, decisions = read_csv(DECISIONS, "\t")
fields, manual = read_csv(MANUAL)
assert len(batch) == len(decisions) == 48
assert [row["title"] for row in batch] == [row["title"] for row in decisions]

batch_by_title = {row["title"]: row for row in batch}
manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual), "duplicate ID in manual decision table"
assert len(batch_by_title) == len(batch)

changed = []
for decision in decisions:
    title = decision["title"]
    aid = batch_by_title[title]["id"]
    assert aid in manual_by_id, f"Round 91 article missing from manual table: {title}"
    row = manual_by_id[aid]
    assert row["title"] == title
    new_primary = decision["primary"]
    new_secondary = ";".join(value for value in decision["secondary"].split(";") if value)
    old_pair = (row["primary_print_topic_code"], row["secondary_print_topic_codes"])
    new_pair = (new_primary, new_secondary)
    if old_pair != new_pair:
        changed.append(title)
        assert title in EXPECTED_OLD, f"unexpected Round 91 difference: {title} {old_pair} -> {new_pair}"
        assert old_pair == EXPECTED_OLD[title], f"manual row changed since audit: {title} {old_pair}"
        row["primary_print_topic_code"] = new_primary
        row["secondary_print_topic_codes"] = new_secondary
        row["classification_status"] = decision["status"]
        row["decision_basis"] = decision["basis"]
        row["review_note"] += "; Round 91 independent topic-boundary review applied"
        row["reviewed_at"] = date.today().isoformat()

assert set(changed) == set(EXPECTED_OLD), f"correction set mismatch: {changed}"

if not args.dry_run:
    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
    temporary.replace(MANUAL)

print("\n".join(changed))
print(f"corrected={len(changed)} dry_run={args.dry_run} manual_records={len(manual)}")
