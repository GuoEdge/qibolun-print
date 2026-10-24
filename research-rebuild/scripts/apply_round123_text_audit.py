#!/usr/bin/env python3
"""Apply the audited Round123 full-text reread to the manual topic table."""
from __future__ import annotations

import csv
import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
CANDIDATES = REPORTS / "round123-text-candidates.csv"
AUDIT = REPORTS / "round123-text-audit.tsv"
DECISIONS = REPORTS / "round123-text-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_rows(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def main() -> None:
    _, candidates = read_rows(CANDIDATES)
    audit_fields, audits = read_rows(AUDIT, "\t")
    decision_fields, decisions = read_rows(DECISIONS, "\t")
    manual_fields, manual = read_rows(MANUAL)

    assert len(candidates) == len(audits) == len(decisions) == 10
    ids = [row["id"] for row in candidates]
    assert len(set(ids)) == len(ids)
    audit_ids = [row["id"] for row in audits]
    decision_ids = [row["id"] for row in decisions]
    assert len(set(audit_ids)) == len(audit_ids) and set(ids) == set(audit_ids)
    assert len(set(decision_ids)) == len(decision_ids) and set(ids) == set(decision_ids)
    assert len({row["id"] for row in manual}) == len(manual) == 4305

    by_candidate = {row["id"]: row for row in candidates}
    by_audit = {row["id"]: row for row in audits}
    by_decision = {row["id"]: row for row in decisions}
    manual_by_id = {row["id"]: row for row in manual}
    codes = {f"A{i:02d}" for i in range(22)}
    corpus_by_id = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                article = json.loads(line)
                corpus_by_id[str(article["id"])] = article
    assert len(corpus_by_id) == 4305

    updates = []
    already_applied = 0
    for aid in ids:
        candidate = by_candidate[aid]
        audit = by_audit[aid]
        decision = by_decision[aid]
        current = manual_by_id[aid]
        article = corpus_by_id[aid]

        assert candidate["classification_status"] == "manual_provisional"
        assert candidate["title"] == audit["title"] == decision["title"] == current["title"] == article["title"]
        assert int(candidate["body_char_count"]) == int(audit["text_chars"]) == len(article.get("text") or "")
        assert int(candidate["image_count"]) == int(audit["image_count"])
        assert candidate["primary_print_topic_code"] == audit["current_primary"] == decision["old_primary"]
        assert candidate["secondary_print_topic_codes"] == audit["current_secondary"] == decision["old_secondary"]

        primary = decision["new_primary"]
        secondary = [code for code in decision["new_secondary"].split(";") if code]
        status = decision["status"]
        assert primary == audit["recommended_primary"]
        assert ";".join(secondary) == audit["recommended_secondary"]
        assert status == audit["recommended_status"]
        assert decision["decision"] in {"promote", "retain"}
        assert status in {"manual_confirmed", "manual_provisional"}
        assert primary in codes and len(secondary) <= 3
        assert len(secondary) == len(set(secondary))
        assert all(code in codes and code != primary for code in secondary)
        assert decision["reason"].strip() and decision["risk_boundary"].strip()
        assert audit["decision_basis"].strip() and audit["fact_risk"].strip()

        desired = {
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": ";".join(secondary),
            "classification_status": status,
            "decision_basis": audit["decision_basis"],
        }
        if current["classification_status"] != "manual_provisional":
            assert all(current.get(key, "") == value for key, value in desired.items()), (
                f"partially applied or mismatched Round123 decision: {aid}"
            )
            already_applied += 1
            continue

        assert current["primary_print_topic_code"] == candidate["primary_print_topic_code"]
        assert current["secondary_print_topic_codes"] == candidate["secondary_print_topic_codes"]
        current.update(desired)
        current["review_note"] = (
            f"Round123 independent full-text reread; body_chars={audit['text_chars']}; "
            f"{audit['boundary_adjustment']} Fact-risk boundary: {audit['fact_risk']}"
        )
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round123-text-reread").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    assert already_applied in {0, len(ids)}, "partial Round123 application detected"
    if updates and not args.dry_run:
        assert not already_applied
        temp = MANUAL.with_suffix(".csv.tmp")
        with temp.open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=manual_fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(manual)
        temp.replace(MANUAL)

    print(json.dumps({
        "round": 123,
        "records": len(ids),
        "operation": "append" if updates else "already_applied_verified",
        "updated": len(updates),
        "confirmed": sum(row["classification_status"] == "manual_confirmed" for row in updates),
        "provisional": sum(row["classification_status"] == "manual_provisional" for row in updates),
        "manual_total": len(manual),
        "secondary_limit": 3,
        "dry_run": args.dry_run,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
