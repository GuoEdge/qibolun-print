#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按"批次体量"排序派发：小批次优先，避免大批次长期占用并卡住吞吐。

用法：
    python3 scripts/dispatch_fast.py --agents 8 --max-articles 5 --prefer small --tag e
    python3 scripts/dispatch_fast.py --status

只影响派发顺序，不改变任何批次内容与编号。
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dispatch_wave import todo_batches  # noqa: E402
from lib_rebuild import REBUILD_ROOT, load_manifest  # noqa: E402
import schedule_batches as S  # noqa: E402

INFLIGHT_DIR = os.path.join(REBUILD_ROOT, "prompts", "inflight")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agents", type=int, default=8)
    ap.add_argument("--per", type=int, default=2)
    ap.add_argument("--max-articles", type=int, default=5)
    ap.add_argument("--tag", default="e")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    todo, passed = todo_batches()
    man = load_manifest()
    count = {b["batch_id"]: b["article_count"] for b in man["batches"]}
    if args.status:
        small = [b for b in todo if count[b] <= args.max_articles]
        print(
            json.dumps(
                {
                    "passed": passed,
                    "todo": len(todo),
                    "todo_small(<=%d)" % args.max_articles: len(small),
                    "small_head": small[:16],
                },
                ensure_ascii=False,
            )
        )
        return 0

    small = [b for b in todo if count[b] <= args.max_articles]
    n = args.agents * args.per
    picked = small[:n]
    groups = [picked[i * args.per : (i + 1) * args.per] for i in range(args.agents)]
    os.makedirs(INFLIGHT_DIR, exist_ok=True)
    rows = []
    for i, g in enumerate(groups, 1):
        if not g:
            break
        agent = "%s%02d" % (args.tag, i)
        path = os.path.join(INFLIGHT_DIR, agent + ".md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(S.PROMPT_TEMPLATE.format(batches="、".join(g)))
        rows.append({"agent": agent, "batches": g, "prompt_file": path})
    with open(os.path.join(REBUILD_ROOT, "reports", "wave-manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)
    print(json.dumps({"todo": len(todo), "small": len(small), "dispatched": len(picked)}, ensure_ascii=False))
    for m in rows:
        print(m["agent"], " ".join(x[-4:] for x in m["batches"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
