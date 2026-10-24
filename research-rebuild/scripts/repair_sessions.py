#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自愈：扫描 records/<batch>.sessions.py 的结构缺陷并最小修复。

修复项（只改结构，不动任何已填 ANALYSIS 内容）：
1. 缺 `def main(` / `if __name__` 收尾（并发写入被中断导致的截断）→ 补回标准收尾；
2. 缺 `sys.path.insert(..., '..', 'scripts')` → 补为模板写法；
3. 仍以内联 JSON 骨架（`SKELETON = [` + false/true）→ 走 migrate_sessions_v1；
4. 缺 `BATCH = "..."` → 从文件名补。

用法：
    python3 scripts/repair_sessions.py --scan          # 只报告
    python3 scripts/repair_sessions.py --fix           # 修复
    python3 scripts/repair_sessions.py --fix r001-b0081
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import REBUILD_ROOT  # noqa: E402
import migrate_sessions_v1 as M  # noqa: E402

RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")

MAIN_TAIL = '''

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')
    args = ap.parse_args()
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row['article']
        uid = UID_BY_ID[art['id']]
        if uid not in ANALYSIS:
            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))
        p = ANALYSIS[uid]
        records.append(build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', '')))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
'''

HEAD_FIX = (
    "_HERE = os.path.dirname(os.path.abspath(__file__))\n"
    "sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))\n"
    "from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402"
)


def inspect(batch):
    path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    if not os.path.exists(path):
        return ["缺少文件"]
    src = open(path, encoding="utf-8").read()
    issues = []
    try:
        tree = ast.parse(src)
        names = {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}
        if "main" not in names:
            issues.append("缺 main()")
    except SyntaxError as exc:
        issues.append("语法错误: %s" % exc)
        return issues
    if "..', 'scripts'" not in src and '"..", "scripts"' not in src:
        issues.append("sys.path 未指向 ../scripts")
    if not re.search(r"^_HERE\s*=", src, re.M):
        issues.append("缺 _HERE 定义")
    if not re.search(r"^BATCH\s*=", src, re.M):
        issues.append("缺 BATCH")
    if re.search(r"SKELETON\s*=\s*(json\.loads\(r)?['\"]", src):
        issues.append("内联骨架字符串（需迁移）")
    if "UID_BY_ID" not in src:
        issues.append("缺 UID_BY_ID")
    if "SKELETON = [" in src:
        issues.append("内联 JSON 骨架（需迁移）")
    if "ANALYSIS = {" not in src:
        issues.append("缺 ANALYSIS")
    return issues


def _fix_inline(batch):
    """把 `SKELETON = [...]`（JSON 字面量）改为边车 + json.load 形式。"""
    path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    src = open(path, encoding="utf-8").read()
    start = src.find("SKELETON = [")
    if start < 0:
        return None
    i = src.index("[", start)
    depth = 0
    end = None
    for j in range(i, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    if end is None:
        return None
    raw = src[i:end]
    skel = None
    try:
        skel = json.loads(
            raw.replace(": true", ": True").replace(": false", ": False").replace(": null", ": None")
        )
    except json.JSONDecodeError:
        try:
            skel = ast.literal_eval(raw)
        except (ValueError, SyntaxError):
            return None
    skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
    with open(skel_path, "w", encoding="utf-8") as fh:
        json.dump(skel, fh, ensure_ascii=False, indent=1)
    replacement = (
        "with open(os.path.join(_HERE, '%s.skeleton.json'), encoding='utf-8') as _fh:\n"
        "    SKELETON = json.load(_fh)\n"
        "UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}" % batch
    )
    src = src[:start] + replacement + src[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return skel


def _fix_raw_string(batch):
    """处理 `SKELETON = json.loads(r'''...''')` 形式。"""
    path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    src = open(path, encoding="utf-8").read()
    m = re.search(r"SKELETON\s*=\s*json\.loads\(\s*r?('''|\"\"\")(.*?)\1\s*\)", src, re.S)
    if not m:
        return None
    try:
        skel = json.loads(m.group(2))
    except json.JSONDecodeError:
        return None
    skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
    with open(skel_path, "w", encoding="utf-8") as fh:
        json.dump(skel, fh, ensure_ascii=False, indent=1)
    replacement = (
        "with open(os.path.join(_HERE, '%s.skeleton.json'), encoding='utf-8') as _fh:\n"
        "    SKELETON = json.load(_fh)\n"
        "UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}" % batch
    )
    src = src[: m.start()] + replacement + src[m.end() :]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return skel


def fix(batch):
    issues = inspect(batch)
    if not issues:
        return []
    if "内联骨架字符串（需迁移）" in issues:
        if _fix_raw_string(batch) is None:
            return ["内联骨架字符串无法解析"]
        return ["已改为骨架边车"] + fix(batch)
    if "内联 JSON 骨架（需迁移）" in issues:
        if _fix_inline(batch) is None:
            err = M.migrate(batch)
            if err:
                return ["迁移失败: %s" % err]
        after_inline = inspect(batch)
        if "内联 JSON 骨架（需迁移）" in after_inline:
            return ["内联骨架无法解析"]
        rest = [i for i in after_inline if i != "内联 JSON 骨架（需迁移）"]
        return ["已改为骨架边车"] + (fix(batch) if rest else [])

    path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    src = open(path, encoding="utf-8").read()
    changed = []

    if "缺 main()" in issues:
        # 去掉尾部可能残留的半个 main
        cut = src.find("\ndef main(")
        if cut >= 0:
            src = src[:cut]
        src = src.rstrip() + "\n" + MAIN_TAIL
        changed.append("补 main()")
    if "sys.path 未指向 ../scripts" in issues:
        src = src.replace(
            "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))",
            HEAD_FIX,
        )
        changed.append("修 sys.path")
    if "缺 _HERE 定义" in issues:
        # 在 import sys 之后补 _HERE（若 HEAD_FIX 已带入则不重复）
        if not re.search(r"^_HERE\s*=", src, re.M):
            src = re.sub(
                r"^(import sys\s*)$",
                "\\1\n\n_HERE = os.path.dirname(os.path.abspath(__file__))",
                src,
                count=1,
                flags=re.M,
            )
            changed.append("补 _HERE")
        if "..', 'scripts'" not in src and '"..", "scripts"' not in src:
            src = src.replace(
                "_HERE = os.path.dirname(os.path.abspath(__file__))",
                "_HERE = os.path.dirname(os.path.abspath(__file__))\n"
                "sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))",
                1,
            )
            changed.append("补 sys.path")
    if "缺 BATCH" in issues:
        src = src.replace(
            "from authoring import",
            'BATCH = "%s"\nfrom authoring import' % batch,
            1,
        )
        changed.append("补 BATCH")
    if "缺 UID_BY_ID" in issues:
        marker = "SKELETON = json.load(_fh)"
        if marker in src:
            src = src.replace(
                marker,
                marker + "\nUID_BY_ID = {s['id']: s['uid'] for s in SKELETON}",
                1,
            )
            changed.append("补 UID_BY_ID")
    if "缺 ANALYSIS" in issues:
        src = src.rstrip() + "\n\nANALYSIS = {}\n"
        changed.append("补空 ANALYSIS")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    after = inspect(batch)
    if after:
        changed.append("仍存在: " + "; ".join(after))
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="*")
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    targets = args.batches or sorted(
        f[: -len(".sessions.py")]
        for f in os.listdir(RECORDS_DIR)
        if f.endswith(".sessions.py")
    )
    bad = 0
    for b in targets:
        issues = inspect(b)
        if not issues:
            continue
        bad += 1
        print("%-14s %s" % (b, "; ".join(issues)))
        if args.fix:
            done = fix(b)
            after = inspect(b)
            print("    -> %s%s" % ("; ".join(done), "" if not after else "  ⚠ 仍存在: " + "; ".join(after)))
    print("扫描 %d 个，问题 %d 个%s" % (len(targets), bad, "" if not args.fix else "（已尝试修复）"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
