#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""迁移：把旧格式 records/<batch>.sessions.py 中已填的 ANALYSIS 提取出来，
按新模板重建 .sessions.py，并生成 .skeleton.json 边车文件。

旧格式（build_sessions.py v1）把 SKELETON 以 JSON 字面量写进 .py，导致
`false/true` 触发 NameError；本脚本用 AST 静态提取 SKELETON 与 ANALYSIS，
不改动、不重写任何分析内容。

用法：
    python3 scripts/migrate_sessions_v1.py r001-b0002 r001-b0003 ...
    python3 scripts/migrate_sessions_v1.py --auto     # 自动处理所有解析失败的批次
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import REBUILD_ROOT  # noqa: E402

RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")


def _clean(node):
    """AST 字面量 → Python 对象；容忍 Name/Attribute（旧骨架里的 false/true）。"""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in ("false", "False"):
            return False
        if node.id in ("true", "True"):
            return True
        if node.id in ("null", "None"):
            return None
        raise ValueError("无法解析名字 %s" % node.id)
    if isinstance(node, ast.List):
        return [_clean(e) for e in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(_clean(e) for e in node.elts)
    if isinstance(node, ast.Dict):
        return {_clean(k): _clean(v) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_clean(node.operand)
    raise ValueError("无法解析节点 %s" % type(node).__name__)


def extract(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id in ("SKELETON", "ANALYSIS", "BATCH"):
                found[tgt.id] = _clean(node.value)
    return found


def _analysis_literal(analysis):
    """analysis 字典 → 合法的 Python 字面量（True/False/None，非 JSON 的 true/false/null）。"""
    txt = json.dumps(analysis, ensure_ascii=False, indent=1)
    return (
        txt.replace(": true", ": True")
        .replace(": false", ": False")
        .replace(": null", ": None")
    )


def _extract_inline_json(src):
    """处理 `SKELETON = json.loads(r'''...''')` 形式（部分代理的自定义修复写法）。"""
    marker = "json.loads("
    i = src.find(marker)
    if i < 0:
        return None
    j = src.find("'''", i)
    if j < 0:
        return None
    k = src.find("'''", j + 3)
    if k < 0:
        return None
    try:
        return json.loads(src[j + 3 : k])
    except json.JSONDecodeError:
        return None


def migrate(batch):
    path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    backup = path + ".v1.bak"
    if os.path.exists(path):
        head = open(path, encoding="utf-8").read()
        if (
            "json.load(_fh)" in head
            and "sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))" in head
        ):
            return None  # 已是新格式
        inline = _extract_inline_json(head)
        if inline:
            skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
            if not os.path.exists(skel_path):
                with open(skel_path, "w", encoding="utf-8") as fh:
                    json.dump(inline, fh, ensure_ascii=False, indent=1)
    if not os.path.exists(path):
        if not os.path.exists(backup):
            return None
        path = backup  # 上次迁移中途失败，直接用备份重做
    try:
        found = extract(path)
    except Exception as exc:  # noqa: BLE001
        return "解析失败 %s: %s" % (batch, exc)
    if "ANALYSIS" not in found:
        return "缺少 ANALYSIS: %s" % batch
    analysis = found["ANALYSIS"]
    skeleton = found.get("SKELETON")
    if not os.path.exists(backup) and path == os.path.join(RECORDS_DIR, batch + ".sessions.py"):
        os.replace(path, backup)
    # 生成骨架 JSON（优先用旧 SKELETON；否则从语料重算）
    import build_sessions as bs  # noqa: E402

    skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
    if skeleton and not os.path.exists(skel_path):
        with open(skel_path, "w", encoding="utf-8") as fh:
            json.dump(skeleton, fh, ensure_ascii=False, indent=1)
    bs.build(batch)  # 写 skeleton.json；.sessions.py 不存在时按新模板生成
    template_path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    src = open(template_path, encoding="utf-8").read()
    start = src.index("ANALYSIS = {")
    marker = "\ndef main("
    end = src.index(marker, start) if marker in src[start:] else len(src)
    body = "ANALYSIS = " + _analysis_literal(analysis) + "\n\n"
    src = src[:start] + body + src[end:]
    with open(template_path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="*")
    ap.add_argument("--auto", action="store_true")
    args = ap.parse_args()
    targets = list(args.batches)
    if args.auto:
        for name in sorted(os.listdir(RECORDS_DIR)):
            if not name.endswith(".sessions.py"):
                continue
            b = name[: -len(".sessions.py")]
            if b not in targets:
                targets.append(b)
    ok = 0
    for b in targets:
        err = migrate(b)
        if err:
            print("SKIP %s" % err)
        else:
            print("migrated %s" % b)
            ok += 1
    print("done: %d migrated" % ok)


if __name__ == "__main__":
    main()
