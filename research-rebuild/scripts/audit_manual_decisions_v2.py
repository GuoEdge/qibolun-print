#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the human A-topic decision table independently of the generators."""
from __future__ import annotations
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
with (DATA / "print-topic-registry-v2.csv").open(encoding="utf-8-sig", newline="") as fh:
    registry = {row["code"]: row for row in csv.DictReader(fh)}
with (DATA / "print-topic-manual-decisions-v2.csv").open(encoding="utf-8-sig", newline="") as fh:
    rows = list(csv.DictReader(fh))

errors = []
seen = set()
status_counts = Counter()
topic_counts = Counter()
topic_status = defaultdict(Counter)
for row in rows:
    aid = row.get("id", "")
    if not aid:
        errors.append("empty id")
    if aid in seen:
        errors.append(f"duplicate id: {aid}")
    seen.add(aid)
    primary = row.get("primary_print_topic_code", "")
    if primary not in registry:
        errors.append(f"invalid primary {aid}: {primary}")
    secondary = [x for x in (row.get("secondary_print_topic_codes", "") or "").split(";") if x]
    if len(secondary) > 3:
        errors.append(f"too many secondary {aid}")
    if primary in secondary:
        errors.append(f"primary duplicated in secondary {aid}")
    for code in secondary:
        if code not in registry:
            errors.append(f"invalid secondary {aid}: {code}")
    status = row.get("classification_status", "")
    if status not in {"manual_confirmed", "manual_provisional"}:
        errors.append(f"invalid status {aid}: {status}")
    if not row.get("decision_basis", "").strip():
        errors.append(f"missing basis {aid}")
    status_counts[status] += 1
    topic_counts[primary] += 1
    topic_status[primary][status] += 1

report = {
    "records": len(rows),
    "unique_ids": len(seen),
    "status_counts": dict(status_counts),
    "topic_counts": dict(sorted(topic_counts.items())),
    "topic_status_counts": {k: dict(v) for k, v in sorted(topic_status.items())},
    "errors": errors,
    "pass": not errors,
}
out = REPORTS / "manual-decisions-audit-v2.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)
