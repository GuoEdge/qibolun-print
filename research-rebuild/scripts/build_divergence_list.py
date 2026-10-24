#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 text 与 lexical 存在版本性差异的文章清单。

输出：data/lexical-divergence.csv
列：id, reading_ordinal, source_ordinal, title, lexical_extra_chars, lexical_chars, text_chars, note

用途：初读时若命中此清单，必须在 unresolved_questions/notes 中登记
"lexical 结构中存在 text 未包含的内容，需要结构核验"，并按需标记 needs_reread。
"""

from __future__ import annotations

import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_rebuild import (  # noqa: E402
    BATCH_DIR,
    REBUILD_ROOT,
    lexical_only_chars,
    load_manifest,
    read_jsonl,
)


def main():
    man = load_manifest()
    rows = []
    for b in man["batches"]:
        for r in read_jsonl(os.path.join(BATCH_DIR, b["file"])):
            a = r["article"]
            only, common, lexn, bodyn = lexical_only_chars(a)
            if only <= 0:
                continue
            rows.append(
                {
                    "id": a["id"],
                    "reading_ordinal": a["reading_ordinal"],
                    "source_ordinal": a["source_ordinal"],
                    "title": a["title"],
                    "lexical_extra_chars": only,
                    "lexical_chars": lexn,
                    "text_chars": bodyn,
                    "note": (
                        "lexical 结构含 text 未包含的正文，需结构核验"
                        if only > 100
                        else "轻微结构差异（多为平台标签/换行），登记备查"
                    ),
                }
            )
    rows.sort(key=lambda x: -x["lexical_extra_chars"])
    out = os.path.join(REBUILD_ROOT, "data", "lexical-divergence.csv")
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote %s (%d rows)" % (out, len(rows)))
    for r in rows[:10]:
        print("  %6d  %s  %s" % (r["lexical_extra_chars"], r["id"][:8], r["title"]))


if __name__ == "__main__":
    main()
