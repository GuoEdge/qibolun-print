#!/usr/bin/env python3
"""Apply the Round144 text-only reread to existing provisional rows.

Round144 is a single main-thread reread of unfinished articles, so it may
revise a provisional topic decision but cannot promote a row to confirmed.
The source corpus remains untouched and each prior note is retained.
"""
from __future__ import annotations

import csv
import json
import argparse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
REGISTRY = DATA / "print-topic-registry-v2.csv"

parser = argparse.ArgumentParser()
parser.add_argument("--round", type=int, default=144)
parser.add_argument("--batch", type=Path)
args = parser.parse_args()
ROUND = args.round
BATCH = args.batch or REPORTS / f"live-manual-batch-v2-round{ROUND}-3k.csv"
FULLTEXT = REPORTS / f"round{ROUND}-fulltext.json"
DECISIONS = REPORTS / f"round{ROUND}-decisions.tsv"
LOG = REPORTS / f"round{ROUND}-revision-log.csv"


def read_csv(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


_, batch = read_csv(BATCH)
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
_, decisions = read_csv(DECISIONS, "\t")
manual_fields, manual = read_csv(MANUAL)
_, registry = read_csv(REGISTRY)
codes = {row["code"] for row in registry}

assert 0 < len(batch) <= 50
assert len(batch) == len(fulltext) == len(decisions)
batch_ids = [row["id"] for row in batch]
assert len(batch_ids) == len(set(batch_ids)), f"duplicate ID in Round {ROUND} batch"
assert batch_ids == [row["id"] for row in fulltext] == [row["id"] for row in decisions]
assert [row["title"] for row in batch] == [row["title"] for row in fulltext] == [row["title"] for row in decisions]
assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
assert sum(len(row.get("text") or "") for row in fulltext) <= 90000
assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)

manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual), "duplicate ID in manual table"
assert set(batch_ids) <= set(manual_by_id), f"Round {ROUND} must update existing provisional rows"

updates: dict[str, dict[str, str]] = {}
log_rows: list[dict[str, str]] = []
for batch_row, full_row, decision in zip(batch, fulltext, decisions):
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert decision["primary"] in codes
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] == "manual_provisional"
    assert decision["basis"].strip() and decision["risk_note"].strip()

    prior = manual_by_id[batch_row["id"]]
    note = (
        f"Round {ROUND} full text; body_chars={batch_row['body_char_count']}; "
        f"batch={BATCH.name}; single-thread reread; unfinished article or "
        "boundary status remains provisional; independent blind reread pending; "
        f"claim/risk note: {decision['risk_note']}"
    )
    merged_note = prior.get("review_note", "").rstrip("; ")
    if merged_note:
        merged_note += "; "
    merged_note += note
    updated = dict(prior)
    updated.update({
        "title": batch_row["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": "manual_provisional",
        "decision_basis": decision["basis"],
        "review_note": merged_note,
        "reviewer": f"main-thread+round{ROUND}-single-pass",
        "reviewed_at": date.today().isoformat(),
    })
    updates[batch_row["id"]] = updated
    log_rows.append({
        "id": batch_row["id"],
        "title": batch_row["title"],
        "old_primary": prior.get("primary_print_topic_code", ""),
        "new_primary": decision["primary"],
        "old_secondary": prior.get("secondary_print_topic_codes", ""),
        "new_secondary": ";".join(secondary),
        "old_status": prior.get("classification_status", ""),
        "new_status": "manual_provisional",
        "body_chars": batch_row["body_char_count"],
        "decision_basis": decision["basis"],
    })

output_rows = [updates.get(row["id"], row) for row in manual]
temporary = MANUAL.with_suffix(".csv.tmp")
with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=manual_fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(output_rows)
temporary.replace(MANUAL)

with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
    fields = list(log_rows[0])
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(log_rows)

print(json.dumps({
    "round": ROUND,
    "updated_records": len(updates),
    "changed_primary": sum(row["old_primary"] != row["new_primary"] for row in log_rows),
    "changed_secondary": sum(row["old_secondary"] != row["new_secondary"] for row in log_rows),
    "provisional": len(updates),
    "body_chars": sum(len(row.get("text") or "") for row in fulltext),
    "manual_total_after": len(output_rows),
    "log": str(LOG),
}, ensure_ascii=False, indent=2))
