#!/usr/bin/env python3
"""Synchronize the completed Round116 visual review into derived tables.

The raw corpus is never modified.  This migration validates the canonical
Round116 batch and records only visual-review evidence and the two article
status upgrades whose sole remaining provisional reason was unread images.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-image-review-batch-v2-round116.csv"
MANIFEST = REPORTS / "round116-image-manifest.csv"
REVIEW = REPORTS / "round116-image-review.tsv"
INVENTORY = DATA / "image-inventory.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

UPGRADE = {
    "e7cddc02-f86d-5271-a815-cd603d3c4335",  # 地塔
    "ba725db6-a4a3-5d63-a45d-33eabd849398",  # 世交
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


def validate() -> tuple[list[dict[str, str]], dict[str, list[dict[str, str]]]]:
    _, batch = read_csv(BATCH)
    _, manifest = read_csv(MANIFEST)
    _, review = read_csv(REVIEW, "\t")
    _, inventory = read_csv(INVENTORY)
    batch_ids = [row["id"] for row in batch]
    assert len(batch) == 18 and len(set(batch_ids)) == 18
    expected = {(row["id"], row["image_index"], row["src"]) for row in inventory if row["id"] in set(batch_ids)}
    manifest_keys = {(row["id"], row["image_index"], row["src"]) for row in manifest}
    review_keys = {(row["id"], row["image_index"]) for row in review}
    assert len(manifest) == len(review) == 50
    assert expected == manifest_keys and len(expected) == 50
    assert review_keys == {(row["id"], row["image_index"]) for row in manifest}
    assert all(row["download_status"] == "success" for row in manifest)
    assert all(row["review_status"] == "reviewed" for row in review)
    assert all(row["changes_topic_judgment"] == "no" for row in review)
    assert all(row["image_text_consistency"] in {"consistent", "limited", "unclear"} for row in review)
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in review:
        groups[row["id"]].append(row)
    assert set(groups) == set(batch_ids)
    assert UPGRADE.issubset(groups)
    return manifest, groups


def update_image_tables(groups: dict[str, list[dict[str, str]]]) -> None:
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
    assert sum(row.get("status") == "reviewed" for row in inventory if row.get("id") in groups) == 50
    write_csv(INVENTORY, list(inventory[0]), inventory)

    fields, manifest = read_csv(MANIFEST)
    for row in manifest:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key in review_by_key:
            review = review_by_key[key]
            row["status"] = "reviewed"
            row["notes"] = f"{review['visible_content']}；图文关系：{review['relation_to_text']}；限制：{review['limitations']}"
    write_csv(MANIFEST, fields, manifest)


def update_manual(groups: dict[str, list[dict[str, str]]]) -> dict[str, str]:
    fields, rows = read_csv(MANUAL)
    statuses: dict[str, str] = {}
    for row in rows:
        aid = row.get("id", "")
        if aid not in groups:
            continue
        before = row.get("classification_status", "")
        if aid in UPGRADE:
            assert before == "manual_provisional"
            row["classification_status"] = "manual_confirmed"
        statuses[aid] = row.get("classification_status", before)
        old_note = row.get("review_note", "").split("; image evidence", 1)[0].rstrip("; ")
        row["review_note"] = (
            f"{old_note}; Round116 visual review=reports/round116-image-review.tsv "
            f"({len(groups[aid])}/{len(groups[aid])} images; no topic change); "
            "image limitations recorded per image; OCR and factual claims remain unverified."
        )
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    assert set(statuses) == set(groups)
    write_csv(MANUAL, fields, rows)
    return statuses


def write_decisions(groups: dict[str, list[dict[str, str]]], statuses: dict[str, str]) -> None:
    _, manual = read_csv(MANUAL)
    by_id = {row["id"]: row for row in manual}
    rows = []
    for aid in groups:
        row = by_id[aid]
        limitations = "；".join(dict.fromkeys(r["limitations"] for r in groups[aid] if r["limitations"]))
        visible = "；".join(dict.fromkeys(r["visible_content"] for r in groups[aid] if r["visible_content"]))
        relation = "；".join(dict.fromkeys(r["relation_to_text"] for r in groups[aid] if r["relation_to_text"]))
        rows.append({
            "id": aid,
            "title": row["title"],
            "primary": row["primary_print_topic_code"],
            "secondary": row["secondary_print_topic_codes"],
            "status": statuses[aid],
            "basis": row["decision_basis"],
            "risk_note": f"Round116 image review {len(groups[aid])}/{len(groups[aid])}; changes_topic_judgment=no; visible={visible}; relation={relation}; limitations={limitations}; 图片仅记录可见内容，不替代OCR或外部事实核验。",
        })
    write_csv(REPORTS / "round116-decisions.tsv", ["id", "title", "primary", "secondary", "status", "basis", "risk_note"], rows, "\t")


def main() -> None:
    _, groups = validate()
    update_image_tables(groups)
    statuses = update_manual(groups)
    write_decisions(groups, statuses)
    print(json.dumps({
        "round": 116,
        "articles": len(groups),
        "images": sum(len(rows) for rows in groups.values()),
        "upgraded": sorted(aid for aid in statuses if aid in UPGRADE),
        "status_counts": {status: sum(value == status for value in statuses.values()) for status in sorted(set(statuses.values()))},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
