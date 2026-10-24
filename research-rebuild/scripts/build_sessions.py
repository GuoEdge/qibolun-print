#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为一个批次生成"会话记录"格式的记录构造器。

与 gen_template.py 的区别：本脚本把该批全部文章的 id、标题、段落（含字符范围）
机械写入 records/<batch>.sessions.py 的 SKELETON 中，执行代理只需填写
ANALYSIS（按 uid 索引）即可，避免手抄 id / paragraph_id 造成错位。

生成的文件结构：
    SKELETON = [ {...article, paragraphs, images...}, ... ]   # 只读，勿手改
    ANALYSIS = { "<uid>": {analysis, provisional_tags, notes}, ... }
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from authoring import build_paragraphs  # noqa: E402
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, image_srcs, load_manifest, read_jsonl  # noqa: E402

RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")


def build(batch: str):
    man = load_manifest()
    entry = next((b for b in man["batches"] if b["batch_id"] == batch), None)
    if entry is None:
        raise SystemExit("批次不存在: %s" % batch)
    rows = read_jsonl(os.path.join(BATCH_DIR, entry["file"]))
    skeleton = []
    for row in rows:
        art = row["article"]
        paras, _nodes, div = build_paragraphs(art)
        skeleton.append(
            {
                "uid": art["id"][:8],
                "id": art["id"],
                "title": art.get("title"),
                "body_chars": row.get("body_chars"),
                "oversize": row.get("oversize"),
                "images": image_srcs(art.get("lexical")),
                "paragraph_ids": [p["paragraph_id"] for p in paras],
                "paragraph_chars": {
                    p["paragraph_id"]: [p["char_start"], p["char_end"]] for p in paras
                },
                "divergence": bool(div),
                "has_question": bool((art.get("question") or "").strip()),
                "has_text": bool((art.get("text") or "").strip()),
            }
        )

    out_path = os.path.join(RECORDS_DIR, batch + ".sessions.py")
    skel_path = os.path.join(RECORDS_DIR, batch + ".skeleton.json")
    os.makedirs(RECORDS_DIR, exist_ok=True)
    # SKELETON 走 JSON 边车文件：避免把 JSON 字面量（false/true）写进 .py，
    # 也保证重新生成骨架不会覆盖已填写的 ANALYSIS。
    with open(skel_path, "w", encoding="utf-8") as fh:
        json.dump(skeleton, fh, ensure_ascii=False, indent=1)
    if os.path.exists(out_path):
        return out_path, len(skeleton), True

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("# -*- coding: utf-8 -*-\n")
        fh.write('"""批次 %s 的记录构造器（骨架由 build_sessions.py 机械生成）。\n\n' % batch)
        fh.write("只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。\n")
        fh.write("字段要求见 prompts/initial-reading-brief.md。\n")
        fh.write("\n命令行：\n")
        fh.write("  python3 records/%s.sessions.py            # 写 out/%s.out.jsonl\n" % (batch, batch))
        fh.write("  python3 records/%s.sessions.py --out /tmp/x.jsonl\n" % batch)
        fh.write('"""\n\n')
        fh.write("from __future__ import annotations\n\n")
        fh.write("import argparse\nimport json\nimport os\nimport sys\n\n")
        fh.write("_HERE = os.path.dirname(os.path.abspath(__file__))\n")
        fh.write("sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))\n")
        fh.write("from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402\n\n")
        fh.write('BATCH = "%s"\n' % batch)
        fh.write('STARTED = "%s"\n' % "2026-09-20T00:00:00+08:00")
        fh.write('COMPLETED = "%s"\n\n' % "2026-09-20T00:00:00+08:00")
        fh.write("with open(os.path.join(_HERE, '%s.skeleton.json'), encoding='utf-8') as _fh:\n" % batch)
        fh.write("    SKELETON = json.load(_fh)\n")
        fh.write("UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}\n\n\n")
        fh.write("ANALYSIS = {\n")
        for s in skeleton:
            fh.write('    "%s": {  # %s\n' % (s["uid"], s["title"]))
            fh.write('        "analysis": {\n')
            fh.write('            "question_context": "",\n')
            fh.write('            "content_units": [],\n')
            fh.write('            "main_claims": [],\n')
            fh.write('            "argument_steps": [],\n')
            fh.write('            "concept_usage": [],\n')
            fh.write('            "examples_and_targets": [],\n')
            fh.write('            "conditions": [],\n')
            fh.write('            "rhetoric_and_tone": "",\n')
            fh.write('            "unresolved_questions": [],\n')
            fh.write('            "evidence": [],\n')
            fh.write('        },\n')
            fh.write('        "provisional_tags": {\n')
            fh.write('            "domain_candidates": [],\n')
            fh.write('            "issue_candidates": [],\n')
            fh.write('            "text_function_candidates": [],\n')
            fh.write('            "object_candidates": [],\n')
            fh.write('            "working_keywords": [],\n')
            fh.write('        },\n')
            fh.write('        "notes": "",\n')
            fh.write('    },\n')
        fh.write("}\n\n\n")
        fh.write("def main():\n")
        fh.write("    ap = argparse.ArgumentParser()\n")
        fh.write("    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')\n")
        fh.write("    args = ap.parse_args()\n")
        fh.write("    rows = load_batch_rows(BATCH)\n")
        fh.write("    records = []\n")
        fh.write("    for row in rows:\n")
        fh.write("        art = row['article']\n")
        fh.write("        uid = UID_BY_ID[art['id']]\n")
        fh.write("        if uid not in ANALYSIS:\n")
        fh.write("            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))\n")
        fh.write("        p = ANALYSIS[uid]\n")
        fh.write("        records.append(build_record(\n")
        fh.write("            row, row['batch_id'], row['corpus_sha256'],\n")
        fh.write("            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,\n")
        fh.write("            status=p.get('status', 'read'),\n")
        fh.write("            full_text_checked=p.get('full_text_checked', True),\n")
        fh.write("            image_checked=p.get('image_checked', False),\n")
        fh.write("            notes=p.get('notes', '')))\n")
        fh.write("    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')\n")
        fh.write("    write_jsonl(out, records)\n")
        fh.write("    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))\n\n\n")
        fh.write("if __name__ == '__main__':\n    main()\n")
    return out_path, len(skeleton), False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="+")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的 .sessions.py（会丢失已填 ANALYSIS）")
    args = ap.parse_args()
    for b in args.batches:
        path, n, skipped = build(b)
        print(
            "wrote %s.skeleton.json (%d articles)%s"
            % (b, n, "  [skipped existing .sessions.py]" if skipped else "")
        )


if __name__ == "__main__":
    main()
