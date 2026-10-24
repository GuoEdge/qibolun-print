#!/usr/bin/env python3
"""Merge two independent full-text reading halves in selected batch order."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
parser = argparse.ArgumentParser()
parser.add_argument("--round", type=int, default=97)
round_no = parser.parse_args().round
BATCH = REPORTS / f"live-manual-budget-batch-v2-round{round_no}-90k.csv"
FULLTEXT = REPORTS / f"round{round_no}-fulltext.json"
FIRST = REPORTS / f"round{round_no}-firsthalf-decisions.tsv"
SECOND = REPORTS / f"round{round_no}-secondhalf-decisions.tsv"
OUT = REPORTS / f"round{round_no}-decisions.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
first, second = read_tsv(FIRST), read_tsv(SECOND)
assert 0 < len(batch) <= 50 and len(batch) == len(fulltext)
assert [row["id"] for row in batch] == [row["id"] for row in fulltext]
assert [row["title"] for row in batch] == [row["title"] for row in fulltext]
decisions = first + second
assert decisions, "no decisions supplied"
assert [row["id"] for row in decisions] == [row["id"] for row in batch], (
    "decision halves must be contiguous and concatenate to the selected batch in order"
)
# Normalize the newer self-describing audit schema at the merge boundary.
# Legacy compact tables already expose primary/secondary directly.
for row in decisions:
    if "primary" not in row:
        row["primary"] = row.get("new_primary", "")
        row["secondary"] = row.get("new_secondary", "")
    if "risk_note" not in row:
        row["risk_note"] = row.get("risk_boundary", "")
codes = {row["code"] for row in csv.DictReader(
    (ROOT / "research-rebuild/data/print-topic-registry-v2.csv").open(encoding="utf-8-sig", newline="")
)}
fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
for article, batch_row, decision in zip(fulltext, batch, decisions):
    assert decision["id"] == article["id"] == batch_row["id"]
    assert decision["title"] == article["title"] == batch_row["title"]
    assert len(article["text"]) == int(batch_row["body_char_count"])
    assert decision["primary"] in codes
    secondary = [code for code in decision["secondary"].split(";") if code and code != "-"]
    assert len(secondary) <= 3 and all(code in codes for code in secondary)
    assert decision["primary"] not in secondary
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip()

with OUT.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows({key: row.get(key, "") for key in fields} for row in decisions)

print(json.dumps({
    "records": len(decisions),
    "confirmed": sum(row["status"] == "manual_confirmed" for row in decisions),
    "provisional": sum(row["status"] == "manual_provisional" for row in decisions),
    "body_chars": sum(len(row["text"]) for row in fulltext),
    "round": round_no,
    "output": str(OUT),
}, ensure_ascii=False, indent=2))
