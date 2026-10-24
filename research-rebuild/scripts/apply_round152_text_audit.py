#!/usr/bin/env python3
"""Apply an independently reviewed full-text reread batch to existing rows."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("--batch", type=Path)
parser.add_argument("--round", type=int, default=152)
parser.add_argument(
    "--allow-images",
    action="store_true",
    help="允许批次包含图片；图片处置仍须由独立 image-review 记录决定。",
)
args = parser.parse_args()

ROUND = args.round
BATCH = args.batch or (REPORTS / f"live-manual-batch-selection-v2-round{ROUND}.csv")
FULLTEXT = REPORTS / f"round{ROUND}-fulltext.json"
DECISIONS = REPORTS / f"round{ROUND}-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
LOG = REPORTS / f"round{ROUND}-revision-log.csv"
REGISTRY = DATA / "print-topic-registry-v2.csv"


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
assert [row["id"] for row in batch] == [row["id"] for row in fulltext] == [row["id"] for row in decisions]
assert [row["title"] for row in batch] == [row["title"] for row in fulltext] == [row["title"] for row in decisions]
assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
if not args.allow_images:
    assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)

manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual), "manual table has duplicate IDs"
missing = [row["id"] for row in decisions if row["id"] not in manual_by_id]
assert not missing, f"Round{ROUND} IDs missing from manual table: {missing}"

revision_rows: list[dict[str, str]] = []
today = date.today().isoformat()
for batch_row, article, decision in zip(batch, fulltext, decisions):
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert decision["primary"] in codes
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip() and decision["risk_note"].strip()

    current = manual_by_id[decision["id"]]
    old_primary = current.get("primary_print_topic_code", "")
    old_secondary = current.get("secondary_print_topic_codes", "")
    old_status = current.get("classification_status", "")
    note = current.get("review_note", "").rstrip("; ")
    marker = f"Round{ROUND} independent full-text reread"
    addition = (
        f"{marker}; body_chars={batch_row['body_char_count']}; batch={BATCH.name}; "
        f"old_primary={old_primary}; old_secondary={old_secondary}; old_status={old_status}; "
        f"new_primary={decision['primary']}; new_secondary={decision['secondary']}; "
        f"new_status={decision['status']}; claim/risk note: {decision['risk_note']}"
    )
    if marker not in note:
        note = f"{note}; {addition}" if note else addition

    current.update(
        {
            "title": decision["title"],
            "primary_print_topic_code": decision["primary"],
            "secondary_print_topic_codes": ";".join(secondary),
            "classification_status": decision["status"],
            "decision_basis": decision["basis"],
            "review_note": note,
            "reviewer": (
                current.get("reviewer", "") + f"+round{ROUND}-reread"
                if f"round{ROUND}-reread" not in current.get("reviewer", "")
                else current.get("reviewer", "")
            ).strip("+"),
            "reviewed_at": today,
        }
    )
    revision_rows.append(
        {
            "id": decision["id"],
            "title": decision["title"],
            "old_primary": old_primary,
            "old_secondary": old_secondary,
            "old_status": old_status,
            "new_primary": decision["primary"],
            "new_secondary": ";".join(secondary),
            "new_status": decision["status"],
            "basis": decision["basis"],
            "risk_note": decision["risk_note"],
            "revision_source": f"round{ROUND}-decisions.tsv + independent full-text reread",
            "revised_at": today,
        }
    )

if not args.dry_run:
    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manual_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
    temporary.replace(MANUAL)

    log_fields = list(revision_rows[0])
    with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=log_fields)
        writer.writeheader()
        writer.writerows(revision_rows)

print(
    json.dumps(
        {
            "operation": "dry_run" if args.dry_run else "updated_existing_rows",
            "round": ROUND,
            "records": len(revision_rows),
            "confirmed": sum(row["new_status"] == "manual_confirmed" for row in revision_rows),
            "provisional": sum(row["new_status"] == "manual_provisional" for row in revision_rows),
            "body_chars": sum(len(row.get("text") or "") for row in fulltext),
            "manual_total": len(manual),
            "revision_log": str(LOG),
        },
        ensure_ascii=False,
        indent=2,
    )
)
