#!/usr/bin/env python3
"""Prepare Round122 text-audit and fresh-image candidate CSVs.

This is a selection-only step. It never edits the corpus, image inventory, or
manual decisions. Text candidates remain provisional; image candidates are
complete unreviewed groups whose article/image keys do not occur in a prior
manifest.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
INDEX = REPORTS / "article-classification-v2.csv"
INVENTORY = DATA / "image-inventory.csv"
TEXT_OUT = REPORTS / "round122-text-candidates.csv"
IMAGE_OUT = REPORTS / "round122-image-candidates.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def prior_manifest_ids_and_keys() -> tuple[set[str], set[tuple[str, str, str]]]:
    ids: set[str] = set()
    keys: set[tuple[str, str, str]] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        for row in read_csv(path):
            aid = row.get("id", "")
            if aid:
                ids.add(aid)
                keys.add((aid, row.get("image_index", ""), row.get("src", "")))
    return ids, keys


def as_int(value: str | int | None, default: int = 0) -> int:
    try:
        return int(value or default)
    except (TypeError, ValueError):
        return default


def main() -> None:
    corpus: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                corpus[str(row["id"])] = row
    manual = {r["id"]: r for r in read_csv(MANUAL)}
    index = {r["id"]: r for r in read_csv(INDEX)}
    inventory = read_csv(INVENTORY)
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventory:
        groups[row["id"]].append(row)
    prior_ids, prior_keys = prior_manifest_ids_and_keys()

    # Text audit: provisional, text-bearing articles with no image dependency,
    # or with every image already reviewed. Rank reread/boundary and weak-route
    # risks first, with stable source order as the final tie-breaker.
    text_pool: list[dict[str, str]] = []
    for aid, decision in manual.items():
        if decision.get("classification_status") != "manual_provisional":
            continue
        article = corpus.get(aid, {})
        text = str(article.get("text") or "")
        if not text.strip():
            continue
        image_rows = groups.get(aid, [])
        if image_rows and not all(r.get("status") == "reviewed" for r in image_rows):
            continue
        ix = index.get(aid, {})
        reasons: list[str] = []
        score = 0
        if ix.get("reading_status") in {"needs_reread", "missing", ""}:
            score += 40
            reasons.append("needs_reread_or_missing")
        if as_int(ix.get("deepseek_image_count")) == 0:
            score += 15
            reasons.append("no_image_dependency")
        if as_int(ix.get("primary_topic_candidate_score"), 100) < 70:
            score += 25
            reasons.append("low_candidate_score")
        if as_int(ix.get("primary_topic_tie_count")) > 1:
            score += 25
            reasons.append("candidate_tie")
        if "unassigned" in (ix.get("native_assignment_status", "").lower()):
            score += 15
            reasons.append("official_unassigned")
        if len(text) < 700:
            score += 10
            reasons.append("short_text")
        text_pool.append({
            "ordinal": str(ix.get("ordinal", "")),
            "id": aid,
            "title": article.get("title", decision.get("title", "")),
            "body_char_count": str(len(text)),
            "image_count": str(len(image_rows)),
            "image_status": "none" if not image_rows else "all_reviewed",
            "primary_print_topic_code": decision.get("primary_print_topic_code", ""),
            "secondary_print_topic_codes": decision.get("secondary_print_topic_codes", ""),
            "classification_status": decision.get("classification_status", ""),
            "candidate_score": ix.get("primary_topic_candidate_score", ""),
            "selection_score": str(score),
            "selection_reasons": ";".join(reasons),
            "selection_basis": "Round122 provisional text audit; complete text; no pending image dependency; ranked for reread/boundary risk.",
        })
    text_pool.sort(key=lambda r: (-as_int(r["selection_score"]), as_int(r["ordinal"], 10**9), r["id"]))
    text_rows = text_pool[:10]
    assert 8 <= len(text_rows) <= 12
    assert len({r["id"] for r in text_rows}) == len(text_rows)
    write_csv(TEXT_OUT, text_rows, list(text_rows[0]))

    # Image audit: only fresh complete groups are eligible. Prefer larger
    # complete groups to reach the requested 40-50 image budget with few
    # article-level batches; ordinal/id keeps ties deterministic.
    fresh: list[tuple[int, int, str, str]] = []
    for aid, image_rows in groups.items():
        if not image_rows or aid in prior_ids:
            continue
        if not all(r.get("status") == "unreviewed" for r in image_rows):
            continue
        keys = {(r.get("id", ""), r.get("image_index", ""), r.get("src", "")) for r in image_rows}
        if keys & prior_keys:
            continue
        indices = sorted(as_int(r.get("image_index")) for r in image_rows)
        if indices != list(range(1, len(indices) + 1)):
            continue
        fresh.append((len(image_rows), as_int(image_rows[0].get("ordinal"), 10**9), aid, image_rows[0].get("title", "")))
    fresh.sort(key=lambda x: (-x[0], x[1], x[2]))
    selected: list[tuple[int, int, str, str]] = []
    total = 0
    for row in fresh:
        if total + row[0] <= 50:
            selected.append(row)
            total += row[0]
        if total >= 40:
            break
    assert 40 <= total <= 50, total
    image_rows = []
    for count, ordinal, aid, title in selected:
        image_rows.append({
            "ordinal": str(ordinal),
            "id": aid,
            "title": title,
            "image_count": str(count),
            "classification_status": manual.get(aid, {}).get("classification_status", ""),
            "primary_print_topic_code": manual.get(aid, {}).get("primary_print_topic_code", ""),
            "selection_basis": "Round122 fresh complete unreviewed image group; article/image-key overlap with prior manifests excluded; dynamic 40-50 image budget.",
        })
    assert len({r["id"] for r in image_rows}) == len(image_rows)
    assert sum(as_int(r["image_count"]) for r in image_rows) == total
    write_csv(IMAGE_OUT, image_rows, list(image_rows[0]))
    print(json.dumps({
        "text_pool": len(text_pool), "text_selected": len(text_rows),
        "text_chars": sum(as_int(r["body_char_count"]) for r in text_rows),
        "fresh_image_groups": len(fresh), "image_selected": len(image_rows),
        "image_total": total, "fresh_provisional_groups": sum(1 for r in fresh if manual.get(r[2], {}).get("classification_status") == "manual_provisional"),
        "text_output": str(TEXT_OUT), "image_output": str(IMAGE_OUT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
