#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把导出批次渲染成可阅读、可定位的阅读包（Markdown）。

用法:
    python3 scripts/render_batch.py r001-b0001            # 打印到 stdout
    python3 scripts/render_batch.py r001-b0001 --out X.md # 写文件
    python3 scripts/render_batch.py --list 1 20           # 列出批次清单

渲染内容包含每篇的元数据、提问字段、正文分段（带 [Pnnn] 标记与字符起止）、
结构节点统计、图片节点清单。语料只读，本脚本不修改任何语料。
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_rebuild import (  # noqa: E402
    BATCH_DIR,
    image_srcs,
    iter_lexical_nodes,
    lexical_only_chars,
    load_manifest,
    paragraphs_of,
    published_iso,
    read_jsonl,
    walk_body,
)


def render_article(art, batch_row, index):
    out = []
    out.append("=" * 78)
    out.append(
        "### 文章 %d/%d｜reading_ordinal=%s｜source_ordinal=%s"
        % (
            index,
            batch_row.get("_count", "?"),
            art.get("reading_ordinal"),
            art.get("source_ordinal"),
        )
    )
    out.append("")
    out.append("- id: `%s`" % art.get("id"))
    out.append("- title: %s" % art.get("title"))
    out.append("- url: %s" % art.get("url"))
    out.append("- published_at: %s" % published_iso(art.get("publishedAt")))
    out.append("- updated_at: %s" % published_iso(art.get("updatedAt")))
    out.append("- platform: %s" % ("zhihu" if "zhihu.com" in str(art.get("url")) else "afdian"))
    out.append("- body_chars(UTF-16): %s" % batch_row.get("body_chars"))
    out.append("- oversize: %s" % batch_row.get("oversize"))
    out.append("- provenance: %s" % json.dumps(art.get("provenance"), ensure_ascii=False))
    out.append("- superseded: %s" % json.dumps(art.get("superseded"), ensure_ascii=False))
    out.append("")

    q = (art.get("question") or "").strip()
    out.append("#### 提问字段 (question, Q001) — 属于提问者，不得自动归给作者")
    out.append("")
    out.append("[Q001] " + (q if q else "（本文无提问字段）"))
    out.append("")

    out.append("#### brief（仅作导航，不得单独支持作者主张）")
    out.append("")
    out.append((art.get("brief") or "（无）").strip())
    out.append("")

    out.append("#### 正文分段（text 与 lexical 结构对齐，[Pnnn] 为定位标记）")
    out.append("")
    paras = paragraphs_of(art)
    for p in paras:
        flag = ""
        if p.get("anchor") == "lexical_only":
            flag = " ⚠lexical-only(字符位置不可靠)"
        elif p.get("anchor") in ("unmodeled", "unmodeled_tail"):
            flag = " ⚠lexical未覆盖片段"
        out.append(
            "[%s|%s|idx=%d|chars=%s-%s] %s%s"
            % (
                p["paragraph_id"],
                p["field"] if p["field"] != "unmodeled" else "body",
                p["index"],
                p["char_start"],
                p["char_end"],
                p["text"],
                flag,
            )
        )
        out.append("")

    nodes = iter_lexical_nodes(art.get("lexical"))
    counts = {}
    for ntype, _t, _s in nodes:
        counts[ntype] = counts.get(ntype, 0) + 1
    out.append("#### 结构节点统计（lexical）")
    out.append("")
    out.append("`%s`" % json.dumps(counts, ensure_ascii=False))
    out.append("")

    _nodes, div = walk_body(art)
    only, _c, _l, _b = lexical_only_chars(art)
    if div and (only > 0 or any(n.get("anchor") == "lexical_only" for n in _nodes)):
        out.append("#### ⚠ 文本/结构差异（%d 处，lexical 独有约 %d 字）" % (len(div), only))
        out.append("")
        out.append(
            "说明：以 `text` 为阅读正文；下列位置 lexical 结构与 text 不一致，"
            "必须在 unresolved_questions 或 notes 中登记，差量较大时标记 needs_reread。"
        )
        out.append("")
        for d in div[:12]:
            out.append(
                "- %s @ %s：`%s`"
                % (d["reason"], d.get("char_start"), str(d.get("sample"))[:80])
            )
        out.append("")

    srcs = image_srcs(art.get("lexical"))
    out.append("#### 图片节点 (%d)" % len(srcs))
    out.append("")
    if not srcs:
        out.append("（无图片节点）")
    else:
        for i, src in enumerate(srcs, 1):
            out.append("- IMG%03d src=%s" % (i, src))
    out.append("")
    return "\n".join(out)


def render_batch(batch_name):
    if not batch_name.endswith(".jsonl"):
        batch_name = batch_name + ".jsonl"
    path = os.path.join(BATCH_DIR, batch_name)
    rows = read_jsonl(path)
    for r in rows:
        r["_count"] = len(rows)
    out = []
    out.append("# 阅读包 %s" % batch_name)
    out.append("")
    out.append("- corpus_sha256: `%s`" % rows[0]["corpus_sha256"])
    out.append("- batch_id: `%s`" % rows[0]["batch_id"])
    out.append("- 文章数: %d" % len(rows))
    out.append(
        "- body_chars 合计: %s" % sum(int(r["body_chars"]) for r in rows)
    )
    out.append("")
    for i, r in enumerate(rows, 1):
        out.append(render_article(r["article"], r, i))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--list", nargs=2, type=int, metavar=("START", "END"))
    args = ap.parse_args()

    if args.list:
        man = load_manifest()
        for b in man["batches"][args.list[0] - 1 : args.list[1]]:
            print(
                "%s\t%d篇\t%s字\treading %d-%d\t%s"
                % (
                    b["batch_id"],
                    b["article_count"],
                    b["body_chars"],
                    b["first_reading_ordinal"],
                    b["last_reading_ordinal"],
                    ",".join(b["ids"])[:60],
                )
            )
        return

    text = render_batch(args.batch)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("written %s (%d chars)" % (args.out, len(text)), file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
