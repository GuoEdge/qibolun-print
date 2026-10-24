#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""进度与状态统计：reports/progress.json 的权威生成器。

统计口径（与 README 一致，必须分开解释）：
- text_coverage_complete：原始提问、正文、结构已覆盖的篇数（机械验收通过的批次内计数）；
- understanding_complete：已形成有证据定位的精读记录（status=read 且至少 1 条证据）；
- needs_review：status = needs_reread（图片未核验、结构差异待复核等）；
- blocked：status = blocked（无正文、纯图等无法完成初读）；
- independent_review_complete / image_review_complete：独立复核、图像核验（本流水线不产生，恒为 0）。

用法：python3 scripts/update_progress.py
"""

from __future__ import annotations

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, load_manifest, validate_batch  # noqa: E402
from validate_independent_reviews import load as load_independent_reviews, valid_unique_rows  # noqa: E402

OUT_DIR = os.path.join(REBUILD_ROOT, "out")
REPORTS_DIR = os.path.join(REBUILD_ROOT, "reports")


def independent_review_count():
    return len(valid_unique_rows(load_independent_reviews()))


def main():
    man = load_manifest()
    total = len(man["batches"])
    done_batches = []
    failed_batches = []
    missing_batches = []
    recs = []
    for b in man["batches"]:
        path = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
        if not os.path.exists(path):
            missing_batches.append(b["batch_id"])
            continue
        ok, _result = validate_batch(os.path.join(BATCH_DIR, b["file"]), path)
        if not ok:
            failed_batches.append(b["batch_id"])
            continue
        done_batches.append(b["batch_id"])
        for line in open(path, encoding="utf-8"):
            if line.strip():
                recs.append(json.loads(line))

    by_status = {}
    image_articles = 0
    image_needing = 0
    claims = 0
    evidences = 0
    unresolved = 0
    for r in recs:
        st = str((r.get("reading") or {}).get("status"))
        by_status[st] = by_status.get(st, 0) + 1
        imgs = (r.get("structure") or {}).get("images") or []
        if imgs:
            image_articles += 1
            if any(str(i.get("status")) in ("pending", "unreadable", "missing") for i in imgs):
                image_needing += 1
        claims += len((r.get("analysis") or {}).get("main_claims") or [])
        evidences += len(r.get("evidence_refs") or [])
        unresolved += len((r.get("analysis") or {}).get("unresolved_questions") or [])

    progress = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "corpus_records": 4296,
        "corpus_sha256": man["corpus_sha256"],
        "batch_total": total,
        "batch_reading_complete": len(done_batches),
        "batch_failed_existing": len(failed_batches),
        "batch_missing": len(missing_batches),
        "batch_pending": len(failed_batches) + len(missing_batches),
        "text_coverage_complete": len(recs),
        "understanding_complete": by_status.get("read", 0),
        "needs_review": by_status.get("needs_reread", 0),
        "blocked": by_status.get("blocked", 0),
        "reading_status_counts": by_status,
        "image_articles_read": image_articles,
        "image_articles_needing_verification": image_needing,
        "claims_total": claims,
        "evidence_refs_total": evidences,
        "unresolved_questions_total": unresolved,
        "independent_review_complete": independent_review_count(),
        "image_review_complete": 0,
        "formal_classification_started": False,
        "notes": (
            "初读（deepseek-v4.1-flash）按批推进：每批输出 out/<batch_id>.out.jsonl 并通过 "
            "scripts/validate_all.py 机械验收后才计入 text_coverage_complete。"
            "已有输出但验收失败的批次仍计入 batch_pending，不计入任何完成篇数。"
            "understanding_complete 只统计 status=read 的记录；含图片文章在图像核验前一律 needs_reread。"
            "独立复核计数来自 reports/independent-reviews.jsonl 中通过完整严格字段校验且 article_id 唯一的逐篇记录；图像核验仍单独统计。"
        ),
    }
    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(os.path.join(REPORTS_DIR, "progress.json"), "w", encoding="utf-8") as fh:
        json.dump(progress, fh, ensure_ascii=False, indent=2)
    print(json.dumps(progress, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
