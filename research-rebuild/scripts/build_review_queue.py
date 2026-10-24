#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从已验收初读结果生成独立复核队列。

该工具只读取 out/*.out.jsonl，不改写原始语料或初读结果。队列把
needs_reread、图片待核验、证据不足和正文/结构缺口集中起来，便于下一阶段
按风险优先逐篇复核；它不是分类器，也不把初读结果升级为最终结论。
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "out"
REPORTS = ROOT / "reports"


def _priority(rec: dict) -> tuple[int, list[str]]:
    reading = rec.get("reading") or {}
    analysis = rec.get("analysis") or {}
    structure = rec.get("structure") or {}
    reasons: list[str] = []
    score = 0
    if reading.get("status") == "needs_reread":
        score += 100
        reasons.append("needs_reread")
    if structure.get("images"):
        score += 60
        reasons.append("image_review")
    if not analysis.get("evidence_locations"):
        score += 25
        reasons.append("no_evidence_locations")
    if not analysis.get("main_claims"):
        score += 20
        reasons.append("no_main_claims")
    if not (reading.get("full_text_checked") is True):
        score += 15
        reasons.append("full_text_unconfirmed")
    if len(analysis.get("unresolved_questions") or []) >= 3:
        score += 5
        reasons.append("many_open_questions")
    return score, reasons


def main() -> int:
    rows: list[dict] = []
    files = sorted(OUT.glob("*.out.jsonl"))
    for path in files:
        with path.open(encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                rec = json.loads(line)
                score, reasons = _priority(rec)
                article_id = rec.get("article_id")
                metadata = rec.get("metadata") or {}
                reading = rec.get("reading") or {}
                rows.append(
                    {
                        "priority": score,
                        "reasons": reasons,
                        "batch_id": reading.get("batch_id"),
                        "record_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                        "line": line_no,
                        "id": article_id,
                        "title": metadata.get("title", ""),
                        "status": reading.get("status"),
                        "image_count": len((rec.get("structure") or {}).get("images") or []),
                    }
                )
    rows.sort(key=lambda x: (-x["priority"], x.get("batch_id") or "", x.get("id") or ""))
    REPORTS.mkdir(parents=True, exist_ok=True)
    jsonl = REPORTS / "independent-review-queue.jsonl"
    with jsonl.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    summary = {
        "records": len(rows),
        "source_files": len(files),
        "needs_reread": sum(r["status"] == "needs_reread" for r in rows),
        "image_review": sum("image_review" in r["reasons"] for r in rows),
        "priority_ge_100": sum(r["priority"] >= 100 for r in rows),
        "priority_ge_60": sum(r["priority"] >= 60 for r in rows),
        "next_batch": rows[:20],
        "note": "机械排序队列；复核者必须回到原文、图片与初读证据，不得把排序分数当作研究结论。",
    }
    (REPORTS / "independent-review-queue.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
