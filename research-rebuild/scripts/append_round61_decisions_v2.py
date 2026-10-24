#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the validated Round 61 decisions to the manual print-topic table."""
from __future__ import annotations
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-short-batch-v2-round61-short50.csv"
FULLTEXT = REPORTS / "round61-fulltext.json"
DECISIONS = REPORTS / "round61-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)

batch_fields, batch = read_csv(BATCH)
fields, rows = read_csv(MANUAL)
with DECISIONS.open(encoding="utf-8-sig", newline="") as f:
    decisions = list(csv.DictReader(f, delimiter="\t"))
with FULLTEXT.open(encoding="utf-8") as f:
    fulltext = __import__("json").load(f)
assert len(batch) == len(decisions) == len(fulltext) == 50
assert [r["id"] for r in batch] == [r["id"] for r in fulltext]
assert len({r["id"] for r in batch}) == 50
assert not ({r["id"] for r in batch} & {r["id"] for r in rows}), "batch already exists"
by_title = {r["title"]: r for r in decisions}
assert {r["title"] for r in batch} == set(by_title)
new = []
for b in batch:
    d = by_title[b["title"]]
    secondary = [x for x in d["secondary"].split(";") if x]
    assert d["primary"] not in secondary and len(secondary) <= 3
    new.append({
        "id": b["id"], "title": b["title"],
        "primary_print_topic_code": d["primary"],
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": d["status"],
        "decision_basis": d["basis"],
        "review_note": f"Round 61 full text; batch={BATCH.name}",
        "reviewer": "main-thread", "reviewed_at": date.today().isoformat(),
    })
with MANUAL.open("a", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writerows(new)
print(f"appended={len(new)} total={len(rows)+len(new)}")
