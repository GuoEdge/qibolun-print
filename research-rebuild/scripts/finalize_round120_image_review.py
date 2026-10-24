#!/usr/bin/env python3
"""Synchronize Round120 visual evidence for already-confirmed articles."""
from __future__ import annotations
import csv, json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-image-review-batch-v2-round120.csv"
MANIFEST = REPORTS / "round120-image-manifest.csv"
REVIEW = REPORTS / "round120-image-review.tsv"
INVENTORY = DATA / "image-inventory.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

def read(path: Path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh, delimiter=delimiter)
        return list(r.fieldnames or []), list(r)

def write(path: Path, fields, rows, delimiter=","):
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    temp.replace(path)

def main():
    _, batch = read(BATCH); _, manifest = read(MANIFEST); _, review = read(REVIEW, "\t"); _, inventory = read(INVENTORY)
    ids = {r["id"] for r in batch}
    assert len(batch) == len(ids) == 2 and len(manifest) == len(review) == 44
    assert {(r["id"], r["image_index"], r["src"]) for r in manifest} == {(r["id"], r["image_index"], r["src"]) for r in inventory if r["id"] in ids}
    assert {(r["id"], r["image_index"]) for r in manifest} == {(r["id"], r["image_index"]) for r in review}
    assert all(r["download_status"] == "success" for r in manifest)
    assert all(r["review_status"] == "reviewed" and r["changes_topic_judgment"] == "no" for r in review)
    groups = defaultdict(list)
    for r in review: groups[r["id"]].append(r)
    assert set(groups) == ids
    by_key = {(r["id"], r["image_index"]): r for r in review}
    _, inventory = read(INVENTORY)
    for row in inventory:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key in by_key:
            r = by_key[key]; row["status"] = "reviewed"
            row["notes"] = f"{r['visible_content']}；{r['relation_to_text']}；专题改变={r['changes_topic_judgment']}；限制：{r['limitations']}；视觉复核完成，OCR未核验。"
    assert sum(r.get("status") == "reviewed" for r in inventory if r.get("id") in ids) == 44
    write(INVENTORY, list(inventory[0]), inventory)
    fields, current = read(MANIFEST)
    for row in current:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key in by_key:
            r = by_key[key]; row["status"] = "reviewed"; row["notes"] = f"{r['visible_content']}；图文关系：{r['relation_to_text']}；限制：{r['limitations']}"
    write(MANIFEST, fields, current)
    fields, manual = read(MANUAL); statuses = {}
    for row in manual:
        aid = row.get("id", "")
        if aid not in ids: continue
        statuses[aid] = row.get("classification_status", "")
        marker = "Round120 visual review=reports/round120-image-review.tsv"
        if marker not in row.get("review_note", ""):
            row["review_note"] = row.get("review_note", "").rstrip("; ") + f"; {marker} ({len(groups[aid])}/{len(groups[aid])} images; no topic change); image limitations recorded per image; OCR and factual claims remain unverified."
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    assert set(statuses) == ids
    write(MANUAL, fields, manual)
    by_id = {r["id"]: r for r in manual}; decisions = []
    for aid, rows in groups.items():
        row = by_id[aid]; visible="；".join(dict.fromkeys(r["visible_content"] for r in rows)); relation="；".join(dict.fromkeys(r["relation_to_text"] for r in rows)); limits="；".join(dict.fromkeys(r["limitations"] for r in rows))
        decisions.append({"id":aid,"title":row["title"],"primary":row["primary_print_topic_code"],"secondary":row["secondary_print_topic_codes"],"status":statuses[aid],"basis":row["decision_basis"],"risk_note":f"Round120 image review {len(rows)}/{len(rows)}; changes_topic_judgment=no; visible={visible}; relation={relation}; limitations={limits}; 图片仅记录可见内容，不替代OCR或外部事实核验。"})
    write(REPORTS / "round120-decisions.tsv", ["id","title","primary","secondary","status","basis","risk_note"], decisions, "\t")
    print(json.dumps({"round":120,"articles":len(groups),"images":sum(map(len,groups.values())),"status_counts":{s:sum(v==s for v in statuses.values()) for s in sorted(set(statuses.values()))}},ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
