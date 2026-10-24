#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append validated Round 60 full-text decisions without replacing prior work."""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-short-batch-v2-round60-short50.csv"
FULLTEXT = REPORTS / "round60-fulltext.json"
DECISIONS = REPORTS / "round60-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


batch_fields, batch = read_csv(BATCH)
batch_ids = [r["id"] for r in batch]
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
manual_fields, manual_rows = read_csv(MANUAL)
with DECISIONS.open(encoding="utf-8-sig", newline="") as f:
    decisions = list(csv.DictReader(f, delimiter="\t"))

assert len(batch) == 50, f"expected 50 batch rows, got {len(batch)}"
assert len(fulltext) == 50, f"expected 50 fulltexts, got {len(fulltext)}"
assert [r["id"] for r in fulltext] == batch_ids, "fulltext order/IDs differ from selected batch"
assert len(decisions) == 50, f"expected 50 decisions, got {len(decisions)}"
assert {r["title"] for r in decisions} == {r["title"] for r in batch}, "decision titles do not match batch"
assert len({r["title"] for r in decisions}) == 50, "duplicate decision title"
assert not ({r["id"] for r in manual_rows} & set(batch_ids)), "batch already exists in manual table"

registry_fields, registry_rows = read_csv(DATA / "print-topic-registry-v2.csv")
registry = {r["code"] for r in registry_rows}
decision_by_title = {r["title"]: r for r in decisions}
batch_by_title = {r["title"]: r for r in batch}
new_rows = []
for article in fulltext:
    d = decision_by_title[article["title"]]
    b = batch_by_title[article["title"]]
    assert b["id"] == article["id"]
    # Queue lengths include the appended question; the extracted `text` is body-only.
    assert int(b["body_char_count"]) >= len(article["text"]), f"body length mismatch: {article['title']}"
    primary = d["primary"]
    secondary = [x for x in d["secondary"].split(";") if x]
    assert primary in registry, f"invalid primary: {article['title']} {primary}"
    assert len(secondary) <= 3 and primary not in secondary
    assert len(set(secondary)) == len(secondary)
    assert all(x in registry for x in secondary)
    new_rows.append({
        "id": article["id"],
        "title": article["title"],
        "primary_print_topic_code": primary,
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": d["status"],
        "decision_basis": d["basis"],
        "review_note": f"Round 60 full text; {len(article['text'])} chars; batch={BATCH.name}",
        "reviewer": "main-thread",
        "reviewed_at": date.today().isoformat(),
    })

assert len({r["id"] for r in new_rows}) == 50
with MANUAL.open("a", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=manual_fields, extrasaction="ignore")
    writer.writerows(new_rows)
print(json.dumps({"appended": len(new_rows), "total": len(manual_rows) + len(new_rows), "text_chars": sum(len(x["text"]) for x in fulltext)}, ensure_ascii=False))
