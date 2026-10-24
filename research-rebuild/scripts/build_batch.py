#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一个批次走完全流程：渲染阅读包 → 生成记录 → 机械验收。

用法：
    python3 scripts/build_batch.py r001-b0001            # 生成 + Python 验收
    python3 scripts/build_batch.py r001-b0001 --render    # 额外写出 out/r001-b0001.packet.md
    python3 scripts/build_batch.py r001-b0001 --check     # 只验收，不重新生成

退出码：0 = PASS；1 = FAIL（失败清单打印到 stdout，可直接用于修复）。
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys

# Windows PowerShell consoles may expose a legacy GBK stream; batch diagnostics
# contain article titles/notes with characters outside that code page.
# Reconfigure output so a valid batch is not reported as failed by printing.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, validate_batch  # noqa: E402

OUT_DIR = os.path.join(REBUILD_ROOT, "out")
RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")
GEN_NAME = "gen_%s.py"


def gen_path(batch):
    """生成器查找顺序：records/<batch>.sessions.py > scripts/gen_<batch>.py。"""
    sessions = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    if os.path.exists(sessions):
        return sessions
    return os.path.join(HERE, GEN_NAME % batch.replace("-", "_"))


def run_generator(batch):
    path = gen_path(batch)
    if not os.path.exists(path):
        return False, "缺少生成器 %s" % path
    proc = subprocess.run(
        [sys.executable, path], capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if proc.returncode != 0:
        return False, (proc.stdout or "") + (proc.stderr or "")
    return True, (proc.stdout or "").strip()


def render_packet(batch):
    out = os.path.join(OUT_DIR, batch + ".packet.md")
    os.makedirs(OUT_DIR, exist_ok=True)
    proc = subprocess.run(
        [sys.executable, os.path.join(HERE, "render_batch.py"), batch, "--out", out],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")


def cmd_analyze(batch):
    """生成前自检：列出空条目、paragraph_refs/证据引用/图片状态的确定性提示。

    全部为机械检查（不判断内容质量），目的是让执行代理在写文件时就知道哪里会 FAIL。
    """
    skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
    sess_path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    if not os.path.exists(skel_path):
        print("FAIL 缺骨架 %s（先跑 build_sessions.py %s）" % (skel_path, batch))
        return 1
    with open(skel_path, encoding="utf-8") as fh:
        skeleton = json.load(fh)
    if not os.path.exists(sess_path):
        print("FAIL 缺构造器 %s" % sess_path)
        return 1
    spec = importlib.util.spec_from_file_location("sessions_" + batch, sess_path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:  # noqa: BLE001
        print("FAIL 构造器无法导入：%s: %s" % (type(exc).__name__, exc))
        print("     → 先跑 python3 scripts/repair_sessions.py --fix %s" % batch)
        return 1
    analysis = getattr(mod, "ANALYSIS", {})
    print("批次 %s：骨架 %d 篇" % (batch, len(skeleton)))
    incomplete = 0
    for s in skeleton:
        uid = s["uid"]
        item = analysis.get(uid)
        problems = []
        if item is None:
            problems.append("ANALYSIS 缺少该 uid")
        else:
            a = item.get("analysis") or {}
            if not str(a.get("question_context") or "").strip():
                problems.append("question_context 空")
            if not (a.get("content_units") or []):
                problems.append("content_units 空")
            if not (a.get("main_claims") or []):
                problems.append("main_claims 空（若确无主张可忽略，但需确认）")
            ev = a.get("evidence") or []
            if not ev:
                problems.append("evidence 空（author 类主张必须有证据）")
            pids = set(s["paragraph_ids"])
            for e in ev:
                pid = str(e.get("paragraph_id") or "")
                if pid not in pids:
                    problems.append("证据段落 %s 不存在" % pid)
            for u in a.get("content_units") or []:
                for r in u.get("paragraph_refs") or []:
                    if str(r) not in pids:
                        problems.append("%s 引用不存在的 %s" % (u.get("unit_id"), r))
            if s["images"]:
                if item.get("status") != "needs_reread":
                    problems.append("含 %d 图但 status 不是 needs_reread" % len(s["images"]))
                if item.get("image_checked"):
                    problems.append("含图却标 image_checked=True（无读图能力）")
                if not str(item.get("notes") or "").strip():
                    problems.append("含图但 notes 未说明需图像核验")
            elif not str(item.get("notes") or "").strip():
                pass
        if problems:
            incomplete += 1
            print("  %s %-22s %s" % (uid, str(s.get("title"))[:20], "; ".join(problems)))
    if not incomplete:
        print("  全部条目结构完整 → 可直接 build_batch.py %s" % batch)
    else:
        print("  待补/待修 %d 篇" % incomplete)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--analyze", action="store_true", help="生成前自检：列出会导致 FAIL 的结构问题")
    args = ap.parse_args()
    batch = args.batch[:-6] if args.batch.endswith(".jsonl") else args.batch

    input_path = os.path.join(BATCH_DIR, batch + ".jsonl")
    output_path = os.path.join(OUT_DIR, batch + ".out.jsonl")
    if not os.path.exists(input_path):
        print("FAIL 批次不存在: %s" % input_path)
        return 1

    if args.analyze:
        return cmd_analyze(batch)

    if args.render:
        ok, msg = render_packet(batch)
        if not ok:
            print("FAIL 渲染失败: %s" % msg)
            return 1
        print("rendered out/%s.packet.md" % batch)

    if not args.check:
        ok, msg = run_generator(batch)
        print(msg)
        if not ok:
            print("FAIL 生成器报错")
            return 1

    if not os.path.exists(output_path):
        print("FAIL 缺少输出 %s" % output_path)
        return 1

    if args.check:
        dependencies = [gen_path(batch), os.path.join(RECORDS_DIR, batch + ".skeleton.json")]
        stale = [
            path
            for path in dependencies
            if os.path.exists(path) and os.path.getmtime(path) > os.path.getmtime(output_path)
        ]
        if stale:
            print("FAIL 输出已过期：以下源文件比输出更新")
            for path in stale:
                print("  %s" % os.path.relpath(path, REBUILD_ROOT))
            print("  -> 运行 python3 scripts/build_batch.py %s 重建并验收" % batch)
            return 1

    ok, result = validate_batch(input_path, output_path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
