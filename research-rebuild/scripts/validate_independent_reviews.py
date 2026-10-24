#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate independent review records without touching first-pass outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "reports" / "independent-reviews.jsonl"
VALID_CONCLUSIONS = {"reviewed_agree", "reviewed_needs_revision"}


def load() -> list[dict]:
    if not OUT.exists():
        return []
    rows = []
    for n, line in enumerate(OUT.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        row["_line"] = n
        rows.append(row)
    return rows


def validate(rows: list[dict]) -> list[str]:
    errors = []
    seen = set()
    for row in rows:
        line = row["_line"]
        aid = str(row.get("article_id") or "")
        if not aid:
            errors.append(f"line {line}: missing article_id")
        if aid in seen:
            errors.append(f"line {line}: duplicate article_id {aid}")
        seen.add(aid)
        if row.get("conclusion") not in VALID_CONCLUSIONS:
            errors.append(f"line {line}: conclusion must be reviewed_agree or reviewed_needs_revision")
        for key in ("reviewer", "reviewed_at", "coverage", "attribution", "evidence", "images", "independent_judgment"):
            if not str(row.get(key) or "").strip():
                errors.append(f"line {line}: missing {key}")
        if row.get("images") == "pending" and not str(row.get("image_note") or "").strip():
            errors.append(f"line {line}: pending images require image_note")
    return errors


def valid_unique_rows(rows: list[dict]) -> list[dict]:
    """Return rows that satisfy the full validator and have a unique article_id."""
    errors = validate(rows)
    error_lines = {int(error.split(":", 1)[0].split()[1]) for error in errors}
    counts: dict[str, int] = {}
    for row in rows:
        aid = str(row.get("article_id") or "")
        if aid:
            counts[aid] = counts.get(aid, 0) + 1
    return [
        row
        for row in rows
        if row.get("_line") not in error_lines
        and str(row.get("article_id") or "")
        and counts.get(str(row["article_id"]), 0) == 1
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    rows = load()
    errors = validate(rows)
    result = {"records": len(rows), "valid": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
