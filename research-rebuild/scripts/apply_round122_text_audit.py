#!/usr/bin/env python3
"""Apply Round122 text audit rows only after strict structural checks."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
AUDIT = REPORTS / "round122-text-audit.tsv"


def read(path: Path, delimiter: str):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    fields, audit = read(AUDIT, "\t")
    assert audit and len(audit) <= 50
    required = {"id", "title", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "boundary_adjustment", "fact_risk"}
    assert required.issubset(fields), sorted(required - set(fields))
    assert len({row["id"] for row in audit}) == len(audit)
    assert all(row["recommended_status"] in {"manual_confirmed", "manual_provisional"} for row in audit)

    manual_fields, manual = read(MANUAL, ",")
    by_id = {row["id"]: row for row in manual}
    assert len(by_id) == len(manual)
    changed = []
    for item in audit:
        row = by_id[item["id"]]
        assert row["title"] == item["title"]
        assert row["classification_status"] == "manual_provisional"
        assert item.get("primary_agreement", "agree") == "agree"
        assert item["recommended_primary"] in {f"A{i:02d}" for i in range(22)}
        secondary = [code for code in item["recommended_secondary"].split(";") if code]
        assert len(secondary) <= 3 and item["recommended_primary"] not in secondary
        assert all(code in {f"A{i:02d}" for i in range(22)} for code in secondary)
        row["primary_print_topic_code"] = item["recommended_primary"]
        row["secondary_print_topic_codes"] = ";".join(secondary)
        row["classification_status"] = item["recommended_status"]
        row["decision_basis"] = item["decision_basis"]
        row["review_note"] = (
            f"Round122 independent full-text reread; body_chars={item.get('text_chars', '')}; "
            f"{item['boundary_adjustment']} Fact-risk boundary: {item['fact_risk']}"
        )
        row["reviewer"] = (row.get("reviewer", "main-thread") + "+round122-reread").strip("+")
        row["reviewed_at"] = date.today().isoformat()
        changed.append(item["title"])

    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=manual_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
    temporary.replace(MANUAL)
    print({"updated": len(changed), "titles": changed})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
