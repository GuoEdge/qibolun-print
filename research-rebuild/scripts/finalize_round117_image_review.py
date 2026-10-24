#!/usr/bin/env python3
"""Synchronize completed Round117 visual review without changing topics."""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-image-review-batch-v2-round117.csv"
MANIFEST = REPORTS / "round117-image-manifest.csv"
REVIEW = REPORTS / "round117-image-review.tsv"
INVENTORY = DATA / "image-inventory.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields, rows, delimiter: str = ",") -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def validate():
    _, batch = read_csv(BATCH)
    _, manifest = read_csv(MANIFEST)
    _, review = read_csv(REVIEW, "\t")
    _, inventory = read_csv(INVENTORY)
    ids = {row["id"] for row in batch}
    assert len(batch) == len(ids) == 18
    expected = {(row["id"], row["image_index"], row["src"]) for row in inventory if row["id"] in ids}
    assert len(manifest) == len(review) == 47
    assert {(r["id"], r["image_index"], r["src"]) for r in manifest} == expected
    assert {(r["id"], r["image_index"]) for r in review} == {(r["id"], r["image_index"]) for r in manifest}
    assert all(r["download_status"] == "success" for r in manifest)
    assert all(r["review_status"] == "reviewed" for r in review)
    assert all(r["changes_topic_judgment"] == "no" for r in review)
    groups = defaultdict(list)
    for row in review:
        groups[row["id"]].append(row)
    assert set(groups) == ids
    return groups


def sync_tables(groups):
    review_by_key = {(r["id"], r["image_index"]): r for rows in groups.values() for r in rows}
    _, inventory = read_csv(INVENTORY)
    for row in inventory:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key not in review_by_key:
            continue
        r = review_by_key[key]
        row["status"] = "reviewed"
        row["notes"] = f"{r['visible_content']}；{r['relation_to_text']}；专题改变={r['changes_topic_judgment']}；限制：{r['limitations']}；视觉复核完成，OCR未核验。"
    assert sum(row.get("status") == "reviewed" for row in inventory if row.get("id") in groups) == 47
    write_csv(INVENTORY, list(inventory[0]), inventory)

    fields, manifest = read_csv(MANIFEST)
    for row in manifest:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key in review_by_key:
            r = review_by_key[key]
            row["status"] = "reviewed"
            row["notes"] = f"{r['visible_content']}；图文关系：{r['relation_to_text']}；限制：{r['limitations']}"
    write_csv(MANIFEST, fields, manifest)

    fields, manual = read_csv(MANUAL)
    statuses = {}
    for row in manual:
        aid = row.get("id", "")
        if aid not in groups:
            continue
        statuses[aid] = row.get("classification_status", "")
        old = row.get("review_note", "")
        marker = "Round117 visual review=reports/round117-image-review.tsv"
        if marker not in old:
            row["review_note"] = old.rstrip("; ") + f"; {marker} ({len(groups[aid])}/{len(groups[aid])} images; no topic change); image limitations recorded per image; OCR and factual claims remain unverified."
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    assert set(statuses) == set(groups)
    write_csv(MANUAL, fields, manual)

    by_id = {r["id"]: r for r in manual}
    decisions = []
    for aid, rows in groups.items():
        row = by_id[aid]
        visible = "；".join(dict.fromkeys(r["visible_content"] for r in rows if r["visible_content"]))
        relation = "；".join(dict.fromkeys(r["relation_to_text"] for r in rows if r["relation_to_text"]))
        limitations = "；".join(dict.fromkeys(r["limitations"] for r in rows if r["limitations"]))
        decisions.append({"id": aid, "title": row["title"], "primary": row["primary_print_topic_code"], "secondary": row["secondary_print_topic_codes"], "status": statuses[aid], "basis": row["decision_basis"], "risk_note": f"Round117 image review {len(rows)}/{len(rows)}; changes_topic_judgment=no; visible={visible}; relation={relation}; limitations={limitations}; 图片仅记录可见内容，不替代OCR或外部事实核验。"})
    write_csv(REPORTS / "round117-decisions.tsv", ["id", "title", "primary", "secondary", "status", "basis", "risk_note"], decisions, "\t")
    return statuses


def main():
    groups = validate()
    statuses = sync_tables(groups)
    print(json.dumps({"round": 117, "articles": len(groups), "images": sum(map(len, groups.values())), "status_counts": {s: sum(v == s for v in statuses.values()) for s in sorted(set(statuses.values()))}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
