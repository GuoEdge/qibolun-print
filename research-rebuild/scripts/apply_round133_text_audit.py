#!/usr/bin/env python3
"""Apply Round133 body-first reread decisions with idempotent validation."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"


def read(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    _, batch = read(REPORTS / "round133-selection.csv")
    fulltext = json.loads((REPORTS / "round133-fulltext.json").read_text(encoding="utf-8"))
    _, decisions = read(REPORTS / "round133-decisions.tsv", "\t")
    assert len(batch) == len(fulltext) == len(decisions) == 19
    ids = [row["id"] for row in batch]
    assert ids == [row["id"] for row in fulltext] == [row["id"] for row in decisions]
    assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
    assert sum(len(row.get("text") or "") for row in fulltext) == 29938

    _, registry = read(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_fields, manual = read(DATA / "print-topic-manual-decisions-v2.csv")
    by_id = {row["id"]: row for row in manual}
    assert len(manual) == len(by_id) == 4305

    output_decisions: list[dict[str, str]] = []
    audits: list[dict[str, str]] = []
    for batch_row, article, decision in zip(batch, fulltext, decisions):
        current = by_id[batch_row["id"]]
        assert current["title"] == batch_row["title"] == decision["title"] == article["title"]
        primary = decision["new_primary"]
        secondary = decision["new_secondary"]
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and len(secondary_codes) <= 3
        assert len(secondary_codes) == len(set(secondary_codes))
        assert all(code in codes and code != primary for code in secondary_codes)
        status = decision["status"]
        assert status in {"manual_confirmed", "manual_provisional"}
        already_applied = (
            current["primary_print_topic_code"] == primary
            and current["secondary_print_topic_codes"] == secondary
            and current["classification_status"] == status
        )
        # Allow safe reruns after another worker has already applied this batch,
        # while still rejecting an unexpected conflicting manual decision.
        assert current["classification_status"] == "manual_provisional" or already_applied
        basis = decision["basis"]
        risk = decision["risk_boundary"]
        assert "\t" not in basis and "\t" not in risk
        output_decisions.append({
            "id": batch_row["id"], "title": batch_row["title"],
            "old_primary": current["primary_print_topic_code"],
            "old_secondary": current["secondary_print_topic_codes"],
            "new_primary": primary, "new_secondary": secondary,
            "status": status, "decision": "round133_body_reread",
            "basis": basis, "risk_boundary": risk,
        })
        audits.append({
            "id": batch_row["id"], "title": batch_row["title"],
            "text_chars": batch_row["body_char_count"],
            "current_primary": current["primary_print_topic_code"],
            "current_secondary": current["secondary_print_topic_codes"],
            "recommended_primary": primary, "recommended_secondary": secondary,
            "recommended_status": status, "decision_basis": basis, "fact_risk": risk,
        })
        current.update({
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": secondary,
            "classification_status": status,
            "decision_basis": basis,
            "review_note": f"Round133 full-text reread; body_chars={batch_row['body_char_count']}; Fact-risk boundary: {risk}",
            "reviewer": f"{current.get('reviewer', 'main-thread')}+round133-text-reread".strip("+"),
            "reviewed_at": date.today().isoformat(),
        })

    fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    audit_fields = ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"]
    write(REPORTS / "round133-decisions.tsv", fields, output_decisions, "\t")
    write(REPORTS / "round133-text-audit.tsv", audit_fields, audits, "\t")
    if not args.dry_run:
        write(DATA / "print-topic-manual-decisions-v2.csv", manual_fields, manual, ",")
    print(json.dumps({
        "round": 133, "records": len(output_decisions),
        "body_chars": sum(len(row.get("text") or "") for row in fulltext),
        "confirmed": sum(row["status"] == "manual_confirmed" for row in output_decisions),
        "provisional": sum(row["status"] == "manual_provisional" for row in output_decisions),
        "dry_run": args.dry_run,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
