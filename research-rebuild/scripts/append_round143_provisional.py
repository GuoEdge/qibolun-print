#!/usr/bin/env python3
"""Append the explicitly provisional Round143 full-text decisions.

This is intentionally separate from the two-reader batch appender: Round143
contains unfinished articles and has only one completed reading pass so far.
"""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-batch-v2-round143-30k.csv"
FULLTEXT = REPORTS / "round143-fulltext.json"
DECISIONS = REPORTS / "round143-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
REGISTRY = DATA / "print-topic-registry-v2.csv"


def rows(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


_, batch = rows(BATCH)
_, fulltext = rows(FULLTEXT) if False else ([], json.loads(FULLTEXT.read_text(encoding="utf-8")))
_, decisions = rows(DECISIONS, "\t")
manual_fields, manual = rows(MANUAL)
_, registry = rows(REGISTRY)
codes = {row["code"] for row in registry}

assert 0 < len(batch) == len(fulltext) == len(decisions) == 7
assert [row["id"] for row in batch] == [row["id"] for row in fulltext] == [row["id"] for row in decisions]
assert [row["title"] for row in batch] == [row["title"] for row in fulltext] == [row["title"] for row in decisions]
assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
assert sum(len(row.get("text") or "") for row in fulltext) == 29752
assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)

manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual)
existing_ids = set(manual_by_id).intersection(row["id"] for row in batch)
assert not existing_ids or existing_ids == {row["id"] for row in batch}

new_rows = []
for batch_row, decision in zip(batch, decisions):
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert decision["primary"] in codes
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] == "manual_provisional"
    assert decision["basis"].strip() and decision["risk_note"].strip()
    note = (
        f"Round 143 full text; body_chars={batch_row['body_char_count']}; "
        f"batch={BATCH.name}; single-thread reading pass; unfinished article or "
        "boundary status remains provisional; independent blind reread pending; "
        f"claim/risk note: {decision['risk_note']}"
    )
    new_rows.append({
        "id": batch_row["id"],
        "title": batch_row["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": "manual_provisional",
        "decision_basis": decision["basis"],
        "review_note": note,
        "reviewer": "main-thread+round143-single-pass",
        "reviewed_at": date.today().isoformat(),
    })

if existing_ids:
    replacement = {row["id"]: row for row in new_rows}
    manual_output = []
    for row in manual:
        update = replacement.get(row["id"])
        if update:
            prior_note = row.get("review_note", "").rstrip("; ")
            update["review_note"] = (prior_note + "; " if prior_note else "") + update["review_note"]
            manual_output.append(update)
        else:
            manual_output.append(row)
    operation = "updated_existing_provisional"
else:
    manual_output = manual + new_rows
    operation = "appended_new"

tmp = MANUAL.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=manual_fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(manual_output)
tmp.replace(MANUAL)

print(json.dumps({
    "round": 143,
    "updated_or_appended": len(new_rows),
    "operation": operation,
    "provisional": len(new_rows),
    "body_chars": 29752,
    "manual_total_after": len(manual_output),
    "independent_blind_reread_pending": True,
}, ensure_ascii=False, indent=2))
