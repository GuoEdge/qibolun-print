#!/usr/bin/env python3
"""Apply the independently reviewed, image-free Round121 text audit."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
AUDIT = REPORTS / "round121-text-audit.tsv"


def read(path: Path, delimiter: str):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    audit_fields, audit_rows = read(AUDIT, "\t")
    assert audit_fields and len(audit_rows) == 10
    assert all(row["recommended_status"] == "manual_confirmed" for row in audit_rows)
    audit_by_id = {row["id"]: row for row in audit_rows}
    assert len(audit_by_id) == len(audit_rows)

    fields, manual_rows = read(MANUAL, ",")
    manual_by_id = {row["id"]: row for row in manual_rows}
    assert len(manual_by_id) == len(manual_rows)
    changed = []
    for aid, audit in audit_by_id.items():
        row = manual_by_id[aid]
        assert row["title"] == audit["title"]
        assert row["classification_status"] == "manual_provisional"
        assert audit["primary_agreement"] == "agree"
        assert audit["current_primary"] == audit["recommended_primary"]
        row["primary_print_topic_code"] = audit["recommended_primary"]
        row["secondary_print_topic_codes"] = audit["recommended_secondary"]
        row["classification_status"] = "manual_confirmed"
        row["decision_basis"] = audit["decision_basis"]
        row["review_note"] = (
            f"Round121 independent full-text reread; body_chars={audit['text_chars']}; "
            "image_count=0; primary topic agrees with prior decision; "
            f"secondary boundary audit: {audit['boundary_adjustment']} "
            "Topic status does not verify historical, political, psychological, "
            "legal, military, or other factual claims."
        )
        row["reviewer"] = (row.get("reviewer", "main-thread") + "+round121-reread").strip("+")
        row["reviewed_at"] = date.today().isoformat()
        changed.append(audit["title"])

    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual_rows)
    temporary.replace(MANUAL)
    print({"updated": len(changed), "titles": changed})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
