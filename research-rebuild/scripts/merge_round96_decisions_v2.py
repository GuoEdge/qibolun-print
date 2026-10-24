#!/usr/bin/env python3
"""Merge independent Round 96 reads into one batch-ordered decision file."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
BATCH = REPORTS / "live-manual-budget-batch-v2-round96-90k.csv"
FULLTEXT = REPORTS / "round96-fulltext.json"
FIRST = REPORTS / "round96-firsthalf-decisions.tsv"
SECOND = REPORTS / "round96-secondhalf-decisions.tsv"
OUT = REPORTS / "round96-decisions.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
first = read_tsv(FIRST)
second = read_tsv(SECOND)
assert len(batch) == len(fulltext) == 50
assert [r["id"] for r in batch] == [r["id"] for r in fulltext]
assert [r["title"] for r in batch] == [r["title"] for r in fulltext]

decisions: dict[str, dict[str, str]] = {}
for source in (first, second):
    for row in source:
        assert row["id"] not in decisions, f"duplicate reviewer coverage: {row['id']}"
        decisions[row["id"]] = row

expected_ids = [row["id"] for row in batch]
assert set(decisions) == set(expected_ids), (
    f"decision coverage mismatch: missing={set(expected_ids)-set(decisions)}, "
    f"extra={set(decisions)-set(expected_ids)}"
)

codes = {row["code"] for row in csv.DictReader(
    (ROOT / "research-rebuild/data/print-topic-registry-v2.csv").open(encoding="utf-8-sig", newline="")
)}
fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
for article, batch_row in zip(fulltext, batch):
    decision = decisions[batch_row["id"]]
    assert decision["id"] == article["id"]
    assert decision["title"] == article["title"]
    assert decision["primary"] in codes
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip()
    assert len(article["text"]) == int(batch_row["body_char_count"])

with OUT.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(decisions[aid] for aid in expected_ids)

print(json.dumps({
    "records": len(expected_ids),
    "confirmed": sum(decisions[aid]["status"] == "manual_confirmed" for aid in expected_ids),
    "provisional": sum(decisions[aid]["status"] == "manual_provisional" for aid in expected_ids),
    "reviewer_overlap_resolved": 0,
    "output": str(OUT),
}, ensure_ascii=False, indent=2))
