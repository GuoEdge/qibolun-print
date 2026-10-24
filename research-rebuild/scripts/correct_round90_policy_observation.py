#!/usr/bin/env python3
"""Apply the independent audit's Round 90 topic-boundary correction."""
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
DECISIONS = REPORTS / "round90-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

with DECISIONS.open(encoding="utf-8-sig", newline="") as fh:
    round90 = [row for row in csv.DictReader(fh, delimiter="\t") if row["title"] == "政策观察"]
assert len(round90) == 1
decision = round90[0]
assert decision["primary"] == "A08" and decision["secondary"] == "A10"

with MANUAL.open(encoding="utf-8-sig", newline="") as fh:
    reader = csv.DictReader(fh)
    fields = list(reader.fieldnames or [])
    rows = list(reader)

targets = [row for row in rows if row["title"] == "政策观察"]
assert len(targets) == 1
target = targets[0]
assert target["primary_print_topic_code"] == "A10"
assert target["secondary_print_topic_codes"] == "A08"

target["primary_print_topic_code"] = decision["primary"]
target["secondary_print_topic_codes"] = decision["secondary"]
target["decision_basis"] = decision["basis"]
target["review_note"] += "; independent topic-boundary audit revised primary/secondary to A08/A10"
target["reviewed_at"] = date.today().isoformat()

temporary = MANUAL.with_suffix(".csv.tmp")
with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
temporary.replace(MANUAL)

print(json.dumps({"id": target["id"], "title": target["title"],
                  "primary": target["primary_print_topic_code"],
                  "secondary": target["secondary_print_topic_codes"],
                  "status": target["classification_status"]}, ensure_ascii=False, indent=2))
