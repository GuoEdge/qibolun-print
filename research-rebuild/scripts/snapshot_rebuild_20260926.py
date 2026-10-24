#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate the read-only evidence snapshot after the 2026-09-26 rebuild.

Writes ``evidence-snapshot-post-rebuild-20260926.json``.  It records the corpus
hash, the before/after hashes of every file the rebuild touched, the new status
and topic distributions, the round inventory, the image-tail state and the
resolution of each handoff contradiction.  It reads only; the single write is
the snapshot itself.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "reports/rebuild-20260926"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
OLD_CORPUS = ROOT / "sooon-q9adg-articles.jsonl"
CST = timezone(timedelta(hours=8))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path):
    return list(csv.DictReader(path.open(encoding="utf-8-sig")))


def main() -> int:
    man = read_csv(R / "data/print-topic-manual-decisions-v2.csv")
    idx = read_csv(R / "reports/print-index/print-research-index.csv")
    queue = read_csv(R / "reports/live-manual-classification-queue-v2.csv")
    before = json.loads((OUT / "apply-before-hashes.json").read_text(encoding="utf-8"))
    applied = json.loads((OUT / "apply-result.json").read_text(encoding="utf-8"))

    watched = [
        CORPUS,
        OLD_CORPUS,
        R / "data/print-topic-manual-decisions-v2.csv",
        R / "reports/article-classification-v2.csv",
        R / "reports/print-index/print-research-index.csv",
        R / "reports/live-manual-classification-queue-v2.csv",
        R / "data/print-topic-registry-v2.csv",
        R / "reports/native-article-category-edges.csv",
        R / "reports/native-article-category-summary.csv",
        R / "reports/independent-reviews.jsonl",
        R / "reports/image-article-audit-v1.csv",
    ]
    hashes = {}
    for p in watched:
        rel = str(p.relative_to(ROOT))
        hashes[rel] = {
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
            "modified_at": datetime.fromtimestamp(p.stat().st_mtime, CST).isoformat(),
        }

    rounds = {}
    for rnd in (165, 166, 167, 168, 169, 170, 171, 172, 180, 181):
        d = OUT / f"round{rnd}"
        files = sorted(p.name for p in d.iterdir()) if d.exists() else []
        rounds[f"round{rnd}"] = {"dir": str(d.relative_to(ROOT)), "files": files,
                                 "file_count": len(files)}

    body_chars = Counter()
    for row in idx:
        body_chars[row["primary_print_topic"]] += int(row["body_char_count"] or 0)

    snap = {
        "generated_at": datetime.now(CST).isoformat(),
        "scope": "Post-rebuild read-only evidence snapshot; the rebuild wrote new round files, "
                 "one updated live decision table, its derived indexes, and the round180 image assets.",
        "corpus": {
            "path": str(CORPUS.relative_to(ROOT)),
            "records": sum(1 for _ in CORPUS.open(encoding="utf-8")),
            "sha256": hashes[str(CORPUS.relative_to(ROOT))]["sha256"],
            "sha256_expected_handoff": "cdc9c271309e1d71d9708889a3a31f4777e0c339ea54c3753521894afdb8357d",
            "unchanged": hashes[str(CORPUS.relative_to(ROOT))]["sha256"]
                         == "cdc9c271309e1d71d9708889a3a31f4777e0c339ea54c3753521894afdb8357d",
        },
        "file_hashes": hashes,
        "hashes_before_apply": before.get("files", {}),
        "hashes_after_apply": {
            "research-rebuild/data/print-topic-manual-decisions-v2.csv": applied["manual_sha256_after"],
        },
        "manual_rows": len(man),
        "status_counts": dict(Counter(r["classification_status"] for r in man)),
        "status_counts_before": applied["status_before"],
        "rows_updated_this_rebuild": applied["rows_updated"],
        "primary_changed_this_rebuild": applied["primary_changed"],
        "secondary_changed_this_rebuild": applied["secondary_changed"],
        "topic_counts": dict(sorted(Counter(r["primary_print_topic"] for r in idx).items())),
        "topic_body_chars": dict(sorted(body_chars.items())),
        "provisional_records": [
            {"id": r["id"], "title": r["title"], "primary": r["primary_print_topic"],
             "status": r["classification_status"]}
            for r in idx if r["classification_status"] == "manual_provisional"
        ],
        "a00_records": [
            {"id": r["id"], "title": r["title"], "status": r["classification_status"]}
            for r in idx if r["primary_print_topic"] == "A00"
        ],
        "queue_records": len(queue),
        "rounds": rounds,
        "image_tail": json.loads((R / "image-review/round180/round180-summary.json").read_text(encoding="utf-8")),
        "sampling_audit": json.loads((OUT / "round181/round181-audit-summary.json").read_text(encoding="utf-8")),
        "contradictions_resolved": {
            "a00_status_conflict": {
                "status": "resolved",
                "before": "A00 = 28 records, 25 of them manual_confirmed (registry requires pending status)",
                "after": f"A00 = {sum(1 for r in idx if r['primary_print_topic'] == 'A00')} records, "
                         f"all manual_provisional",
                "method": "round172 per-article body adjudication + rule revision R4 (A11 covers secular "
                          "normative argument; A00 is not the default bucket for life-value essays)",
            },
            "official_multi_category_237_238": {
                "status": "resolved",
                "finding": "242 distinct articles have >=2 official edges; 4 of them are officialOnly records "
                           "absent from the local corpus, leaving 238 in-corpus articles; the stored "
                           "official_category_count counts distinct category NAMES, which is >=2 for 237 rows. "
                           "The single difference is a439c81a-95a1-5407-bf12-79a58c908f6b 《可谓之仁》 "
                           "(5 edges to the same practice node 相处, so category_count=1, leaf_count=5).",
                "method": "edge-table recount restricted to local corpus IDs vs stored column count",
            },
            "officialOnly_9_vs_deepseek_missing_9": {
                "status": "resolved",
                "finding": "The two sets are disjoint. officialOnlyArticles=9 are 9 records present in the "
                           "official edge table but absent from the local v2 corpus; all 9 carry the native "
                           "title '此内容不存在'. The 9 DeepSeek-missing records are 9 different IDs that ARE "
                           "in the local corpus (published 2026-09-19..21) with existing topic fields.",
                "intersection_size": 0,
            },
            "round161_164_missing_decision_tsv": {
                "status": "resolved",
                "finding": "round157-160 decision TSVs exist (12/21/13/7 rows); round161-164 decision TSVs do "
                           "not exist and were NOT fabricated. Their selection and fulltext batches exist, and "
                           "all 27 articles (6+7+7+1) are covered by this rebuild's round165-171 full-text "
                           "reviews, so their decisions now exist as supplementary records inside those rounds.",
            },
            "independent_reviews_35": {
                "status": "confirmed",
                "finding": "independent-reviews.jsonl holds 35 records with 35 unique article_ids; all 35 "
                           "conclusions are reviewed_needs_revision. This is NOT a pass and the full corpus is "
                           "NOT independently reviewed.",
            },
        },
        "not_claimed": [
            "all 4,305 articles semantically re-read",
            "the 255 new articles independently full-text reviewed",
            "all images audited (the round180 tail is done; 6 exclusion candidates and other earlier image "
            "decisions are unchanged)",
            "official classification coverage of all 4,305 articles (616 remain unassigned and were NOT "
            "given fabricated official paths)",
            "the 35 independent reviews passed",
        ],
    }
    path = OUT / "evidence-snapshot-post-rebuild-20260926.json"
    path.write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "output": str(path.relative_to(ROOT)),
        "corpus_unchanged": snap["corpus"]["unchanged"],
        "status_counts": snap["status_counts"],
        "a00": len(snap["a00_records"]),
        "provisional": len(snap["provisional_records"]),
        "queue_records": snap["queue_records"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
