#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次 r001-bXXXX 初读记录生成器（模板）。

用法：
  1. 复制到 scripts/gen_<batch>.py（或直接改写本文件内的 BATCH 变量）；
  2. 只填写 ANALYSIS 字典中每篇文章的 analysis / provisional_tags / notes；
  3. 运行： python3 scripts/build_batch.py r001-bXXXX

禁止修改本文件中 BATCH 与 ANALYSIS 之间的注释所界定的机制部分：
段落、字符位置、图片节点、元数据、哈希、证据编号都由语料机械生成，
手写定位会被 build_batch.py 的验收脚本直接判定为不合格。
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-bXXXX"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

# ---------------------------------------------------------------------------
# ANALYSIS：每篇文章一条，key = 语料原始 article id
# 每条包含 analysis / provisional_tags / notes 三段，字段约束见 prompt 与 brief。
# 所有 evidence 的 quote 必须是该段落原文的连续片段（不得改写、不得拼接）。
# ---------------------------------------------------------------------------
ANALYSIS = {
    "ARTICLE-ID-1": {
        "analysis": {
            "question_context": "",
            "content_units": [],
            "main_claims": [],
            "argument_steps": [],
            "concept_usage": [],
            "examples_and_targets": [],
            "conditions": [],
            "rhetoric_and_tone": "",
            "unresolved_questions": [],
            "evidence": [],
        },
        "provisional_tags": {
            "domain_candidates": [],
            "issue_candidates": [],
            "text_function_candidates": [],
            "object_candidates": [],
            "working_keywords": [],
        },
        "notes": "",
    },
}


def main():
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row["article"]
        aid = art["id"]
        if aid not in ANALYSIS:
            raise SystemExit("ANALYSIS 缺少文章 %s（%s）" % (aid, art.get("title")))
        payload = ANALYSIS[aid]
        records.append(
            build_record(
                row,
                row["batch_id"],
                row["corpus_sha256"],
                payload["analysis"],
                payload["provisional_tags"],
                STARTED,
                COMPLETED,
                status=payload.get("status", "read"),
                full_text_checked=payload.get("full_text_checked", True),
                image_checked=payload.get("image_checked", False),
                notes=payload.get("notes", ""),
            )
        )
    extra = set(ANALYSIS) - {r["article"]["id"] for r in rows}
    if extra:
        raise SystemExit("ANALYSIS 含不属于本批次的 id: %s" % ", ".join(sorted(extra)))
    write_jsonl(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out", BATCH + ".out.jsonl"),
        records,
    )
    print("ok %s -> out/%s.out.jsonl (%d records)" % (BATCH, BATCH, len(records)))


if __name__ == "__main__":
    main()
