#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""追踪在飞子代理（跨父回合持久化），并给出下一个可派发的批次。

子代理在共享会话里无法被父代理主动"续命"；父代理只能按波次派发。
本工具把"已派发给哪个 agent、什么时候派的"落盘，父代理据此判断是否要补派。

用法：
    python3 scripts/dispatch_track.py --next-wave --slots 6 --max-articles 8
    python3 scripts/dispatch_track.py --reap        # 回收超时未产出的在飞记录
    python3 scripts/dispatch_track.py --status
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dispatch_wave import todo_batches  # noqa: E402
from lib_rebuild import REBUILD_ROOT, load_manifest  # noqa: E402
import schedule_batches as S  # noqa: E402

INFLIGHT_DIR = os.path.join(REBUILD_ROOT, "prompts", "inflight")
TRACK_PATH = os.path.join(REBUILD_ROOT, "reports", "inflight.json")
STALE_SEC = 25 * 60


def load_track():
    if os.path.exists(TRACK_PATH):
        with open(TRACK_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return {"inflight": {}}


def save_track(t):
    with open(TRACK_PATH, "w", encoding="utf-8") as fh:
        json.dump(t, fh, ensure_ascii=False, indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next-wave", action="store_true")
    ap.add_argument("--slots", type=int, default=6)
    ap.add_argument("--max-articles", type=int, default=8)
    ap.add_argument("--reap", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--tag", default="g")
    args = ap.parse_args()

    track = load_track()
    todo, passed = todo_batches()
    done = set()
    man = load_manifest()
    for b in man["batches"]:
        if os.path.exists(os.path.join(REBUILD_ROOT, "out", b["batch_id"] + ".out.jsonl")):
            done.add(b["batch_id"])

    inflight = {k: v for k, v in track["inflight"].items() if k not in done}
    now = time.time()
    if args.reap:
        stale = [k for k, v in inflight.items() if now - v.get("ts", 0) > STALE_SEC]
        for k in stale:
            del inflight[k]
        track["inflight"] = inflight
        save_track(track)
        print(json.dumps({"reaped": stale}, ensure_ascii=False))

    if args.status or (not args.next_wave and not args.reap):
        print(
            json.dumps(
                {
                    "passed": passed,
                    "todo": len(todo),
                    "inflight": len(inflight),
                    "inflight_batches": sorted(inflight)[:24],
                },
                ensure_ascii=False,
            )
        )
        return 0

    budget = max(0, args.slots - len(inflight))
    todo = [b for b in todo if b not in inflight]
    cnt = {b["batch_id"]: b["article_count"] for b in man["batches"]}
    todo.sort(key=lambda b: (cnt[b], b))
    picked = [b for b in todo if cnt[b] <= args.max_articles][:budget]
    os.makedirs(INFLIGHT_DIR, exist_ok=True)
    rows = []
    for i, b in enumerate(picked, 1):
        agent = "%s%02d" % (args.tag, i)
        path = os.path.join(INFLIGHT_DIR, agent + ".md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(S.PROMPT_TEMPLATE.format(batches=b))
        inflight[b] = {"agent": agent, "ts": now, "prompt_file": path}
        rows.append({"agent": agent, "batch": b, "articles": cnt[b]})
    track["inflight"] = inflight
    save_track(track)
    print(json.dumps({"slots_free": budget, "dispatched": len(rows), "rows": rows}, ensure_ascii=False))
    for r in rows:
        print(r["agent"], r["batch"], "articles=%d" % r["articles"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
