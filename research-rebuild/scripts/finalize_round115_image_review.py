#!/usr/bin/env python3
"""Synchronize the completed Round115 visual review into source indexes.

The original corpus remains read-only.  This migration validates the 56
per-image records, marks only those image rows as visually reviewed, and
records conservative article-level status decisions.  External factual
verification is deliberately outside this operation.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-image-review-batch-v2-round115.csv"
MANIFEST = REPORTS / "round115-image-manifest.csv"
REVIEW = REPORTS / "round115-image-review.tsv"
INVENTORY = DATA / "image-inventory.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

# These four rows were provisional specifically because their image evidence
# had not been read. The remaining two provisional rows have independent
# boundary/high-risk reasons and therefore stay provisional.
UPGRADE = {
    "1fc9f77c-b92d-55f8-9966-095b782fd87f",
    "df41ffb6-6f13-5218-8142-041b703e7720",
    "8a59e0ff-b610-5f32-967d-a163a4877c5a",
    "78f5b862-b74f-5290-9f25-0106f1807a11",
}
KEEP_PROVISIONAL = {
    "8b35202b-98f5-56ef-b715-e232938a1c89",
    "d4b1d6e0-69f2-551c-bf92-32cad6755776",
}


def read_csv(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = ",") -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def validate_and_group() -> tuple[list[dict[str, str]], dict[str, list[dict[str, str]]]]:
    _, batch = read_csv(BATCH)
    _, manifest = read_csv(MANIFEST)
    _, review = read_csv(REVIEW, "\t")
    _, inventory = read_csv(INVENTORY)
    batch_ids = [row["id"] for row in batch]
    assert len(batch_ids) == 20 and len(set(batch_ids)) == 20
    expected = {(row["id"], row["image_index"], row["src"]) for row in inventory if row["id"] in set(batch_ids)}
    manifest_keys = {(row["id"], row["image_index"], row["src"]) for row in manifest}
    review_keys = {(row["id"], row["image_index"]) for row in review}
    assert len(manifest) == len(review) == 56
    assert len(expected) == len(manifest) == 56
    assert manifest_keys == expected
    assert review_keys == {(row["id"], row["image_index"]) for row in manifest}
    assert len(review_keys) == 56
    assert all(row["download_status"] == "success" for row in review)
    assert all(row["review_status"] == "reviewed" for row in review)
    assert all(row["changes_topic_judgment"] == "no" for row in review)
    assert all(row["image_text_consistency"] in {"consistent", "limited", "unclear"} for row in review)
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in review:
        groups[row["id"]].append(row)
    assert set(groups) == set(batch_ids)
    assert set(groups) & UPGRADE == UPGRADE
    assert set(groups) & KEEP_PROVISIONAL == KEEP_PROVISIONAL
    return manifest, groups


def image_note(rows: list[dict[str, str]]) -> str:
    limitations = "；".join(dict.fromkeys(row["limitations"] for row in rows if row["limitations"]))
    relation = "；".join(dict.fromkeys(row["relation_to_text"] for row in rows if row["relation_to_text"]))
    visible = "；".join(dict.fromkeys(row["visible_content"] for row in rows if row["visible_content"]))
    return (
        f"Round115 image review {len(rows)}/{len(rows)}; changes_topic_judgment=no; "
        f"visible={visible}; relation={relation}; limitations={limitations}; "
        "图片仅记录可见内容，不替代OCR或外部事实核验。"
    )


def update_image_tables(manifest: list[dict[str, str]], groups: dict[str, list[dict[str, str]]]) -> None:
    _, inventory = read_csv(INVENTORY)
    review_by_key = {(row["id"], row["image_index"]): row for rows in groups.values() for row in rows}
    for row in inventory:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key not in review_by_key:
            continue
        review = review_by_key[key]
        row["status"] = "reviewed"
        row["notes"] = (
            f"{review['visible_content']}；{review['relation_to_text']}；"
            f"专题改变={review['changes_topic_judgment']}；限制：{review['limitations']}；"
            "视觉复核完成，OCR未核验。"
        )
    assert sum(row.get("status") == "reviewed" for row in inventory if row.get("id") in groups) == 56
    write_csv(INVENTORY, list(inventory[0]), inventory)

    fields, current_manifest = read_csv(MANIFEST)
    for row in current_manifest:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key in review_by_key:
            review = review_by_key[key]
            row["status"] = "reviewed"
            row["notes"] = f"{review['visible_content']}；图文关系：{review['relation_to_text']}；限制：{review['limitations']}"
    write_csv(MANIFEST, fields, current_manifest)


def update_manual(groups: dict[str, list[dict[str, str]]]) -> dict[str, str]:
    fields, rows = read_csv(MANUAL)
    changed: dict[str, str] = {}
    for row in rows:
        aid = row.get("id", "")
        if aid not in groups:
            continue
        before = row.get("classification_status", "")
        if aid in UPGRADE:
            assert before == "manual_provisional"
            row["classification_status"] = "manual_confirmed"
            changed[aid] = "manual_confirmed"
        elif aid in KEEP_PROVISIONAL:
            assert before == "manual_provisional"
            changed[aid] = "manual_provisional"
        else:
            changed[aid] = before
        row["review_note"] = (
            f"{row.get('review_note', '').split('; image evidence', 1)[0].rstrip('; ')}; "
            f"Round115 visual review=reports/round115-image-review.tsv ({len(groups[aid])}/{len(groups[aid])} images; no topic change); "
            f"image limitations recorded per image; OCR and factual claims remain unverified."
        )
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    assert set(changed) == set(groups)
    write_csv(MANUAL, fields, rows)
    return changed


def write_decisions(groups: dict[str, list[dict[str, str]]], statuses: dict[str, str]) -> None:
    _, manual = read_csv(MANUAL)
    by_id = {row["id"]: row for row in manual}
    fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
    rows = []
    for aid in sorted(groups, key=lambda x: int(by_id[x].get("source_ordinal", "0") or 0)):
        row = by_id[aid]
        rows.append({
            "id": aid,
            "title": row["title"],
            "primary": row["primary_print_topic_code"],
            "secondary": row["secondary_print_topic_codes"],
            "status": statuses[aid],
            "basis": row["decision_basis"],
            "risk_note": image_note(groups[aid]),
        })
    # Stable ordinal order is useful for later audit; manual table is keyed by id.
    rows.sort(key=lambda row: next((int(r.get("source_ordinal", "0") or 0) for r in manual if r["id"] == row["id"]), 10**9))
    write_csv(REPORTS / "round115-decisions.tsv", fields, rows, "\t")


def main() -> None:
    _, groups = validate_and_group()
    manifest, _ = read_csv(MANIFEST)
    update_image_tables(manifest, groups)
    statuses = update_manual(groups)
    write_decisions(groups, statuses)
    print(json.dumps({
        "round": 115,
        "articles": len(groups),
        "images": sum(len(rows) for rows in groups.values()),
        "upgraded": sorted(aid for aid in statuses if aid in UPGRADE),
        "kept_provisional": sorted(aid for aid in statuses if aid in KEEP_PROVISIONAL),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
