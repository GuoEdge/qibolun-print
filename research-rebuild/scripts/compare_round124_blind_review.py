#!/usr/bin/env python3
"""Append the existing Round124 decisions to the independent blind sample."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
BLIND = REPORTS / "round124-blind-review.tsv"
DECISIONS = REPORTS / "round124-decisions.tsv"

def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

def main() -> int:
    blind = read(BLIND)
    decisions = {row["id"]: row for row in read(DECISIONS)}
    comparison_fields = [
        "decided_primary", "decided_secondary", "decided_status",
        "primary_match", "secondary_match", "status_match", "disagreement_note",
    ]
    base_fields = [field for field in blind[0] if field not in comparison_fields]
    fields = base_fields + comparison_fields
    out: list[dict[str, str]] = []
    for row in blind:
        decision = decisions.get(row["id"])
        if decision is None:
            raise ValueError(f"missing decision for {row['id']}")
        primary_match = row["blind_primary"] == decision["new_primary"]
        secondary_match = row["blind_secondary"] == decision["new_secondary"]
        status_match = row["blind_status"] == decision["status"]
        disagreements: list[str] = []
        if not primary_match:
            disagreements.append(f"主码盲审{row['blind_primary']} vs决定{decision['new_primary']}")
        if not secondary_match:
            disagreements.append(f"副码盲审{row['blind_secondary'] or '空'} vs决定{decision['new_secondary'] or '空'}")
        if not status_match:
            disagreements.append(f"状态盲审{row['blind_status']} vs决定{decision['status']}")
        merged = {field: row.get(field, "") for field in base_fields}
        merged.update({
            "decided_primary": decision["new_primary"],
            "decided_secondary": decision["new_secondary"],
            "decided_status": decision["status"],
            "primary_match": "yes" if primary_match else "no",
            "secondary_match": "yes" if secondary_match else "no",
            "status_match": "yes" if status_match else "no",
            "disagreement_note": "; ".join(disagreements) or "一致",
        })
        out.append(merged)
    tmp = BLIND.with_suffix(".tmp.tsv")
    with tmp.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(out)
    tmp.replace(BLIND)
    print({
        "records": len(out),
        "primary_disagreements": sum(row["primary_match"] == "no" for row in out),
        "secondary_disagreements": sum(row["secondary_match"] == "no" for row in out),
        "status_disagreements": sum(row["status_match"] == "no" for row in out),
        "output": str(BLIND),
    })
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
