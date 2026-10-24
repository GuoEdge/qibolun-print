#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为独立复核队列生成可逐篇填写的复核包，不改变初读结果。"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
PACKETS = ROOT / "packets" / "independent-review"
BATCHES = ROOT / "deepseek-batches"


def load_queue(path: Path, limit: int) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
                if len(rows) >= limit:
                    break
    return rows


def load_record(item: dict) -> dict:
    path = ROOT / item["record_path"]
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line_no == item["line"]:
                rec = json.loads(line)
                if rec.get("article_id") != item["id"]:
                    raise ValueError(f"queue mismatch: {path}:{line_no}")
                return rec
    raise ValueError(f"missing line: {path}:{item['line']}")


def load_source_question(item: dict) -> str:
    path = BATCHES / f"{item['batch_id']}.jsonl"
    if not path.exists():
        return "本文未提供原始 question 字段。"
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            article = row.get("article") or {}
            if article.get("id") == item["id"]:
                return str(article.get("question") or "[空]")
    return "未在对应批次找到原始 question 字段。"


def render(item: dict, rec: dict, question: str) -> str:
    meta = rec.get("metadata") or {}
    structure = rec.get("structure") or {}
    reading = rec.get("reading") or {}
    analysis = rec.get("analysis") or {}
    lines = [
        f"# 独立复核包｜{meta.get('title', '')}",
        "",
        f"- article_id: `{rec.get('article_id')}`",
        f"- batch_id: `{reading.get('batch_id')}`",
        f"- priority: `{item['priority']}`",
        f"- reasons: {', '.join(item['reasons'])}",
        f"- source_url: {meta.get('url', '')}",
        "",
        "> 本包只提供原文与初读对照。请逐项回到原文/图片复核；填写完成前不要修改初读输出，也不要把初读标签当作最终分类。",
        "",
        "## 提问字段",
        "",
        question,
        "",
        "## 正文段落",
        "",
    ]
    for p in structure.get("paragraphs") or []:
        lines += [f"### {p.get('paragraph_id')} ({p.get('field')})", "", p.get("text", ""), ""]
    lines += ["## 图片索引（待人工/多模态核验）", ""]
    images = structure.get("images") or []
    if images:
        for im in images:
            lines += [
                f"- {im.get('image_id')}: `{im.get('src', '')}`; position={im.get('position', '')}; status={im.get('status', '')}",
            ]
    else:
        lines += ["- 无图片节点", ""]
    lines += [
        "",
        "## 初读对照（仅供核验）",
        "",
        f"- status: `{reading.get('status')}`; full_text_checked: `{structure.get('full_text_checked')}`; image_checked: `{reading.get('image_checked')}`",
        f"- question_context: {analysis.get('question_context', '')}",
        f"- provisional claims: {json.dumps(analysis.get('main_claims') or [], ensure_ascii=False)}",
        f"- provisional evidence: {json.dumps(rec.get('evidence_refs') or [], ensure_ascii=False)}",
        "",
        "## 独立复核记录（待填写）",
        "",
        "### 1. 原文覆盖与遗漏",
        "<!-- 是否完整覆盖 question、正文、lexical 结构、图片；列出遗漏段落/节点及原文依据。 -->",
        "",
        "### 2. 作者主张与归属修正",
        "<!-- 区分作者、提问者、被引/被反驳观点；给出段落号和连续短引。 -->",
        "",
        "### 3. 证据与引文核验",
        "<!-- 逐项核对 evidence quote 是否为原文连续片段、位置是否准确、是否足以支持主张。 -->",
        "",
        "### 4. 图片核验",
        "<!-- 每张图片填写 visible_content / relation_to_text / uncertainty；无法核验则明确写 pending。 -->",
        "",
        "### 5. 独立判断与分歧",
        "<!-- 写遗漏、归属问题、模态问题、术语问题和与初读的分歧；不要做价值评判。 -->",
        "",
        "### 6. 复核结论",
        "<!-- not_started | in_review | reviewed_needs_revision | reviewed_agree；填写日期与复核者。 -->",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1, help="队列中的 1-based 起始位置")
    ap.add_argument("--limit", type=int, default=12)
    ap.add_argument("--new-only", action="store_true", help="只从新增内容队列生成包")
    args = ap.parse_args()
    if args.start < 1 or args.limit < 1:
        ap.error("--start and --limit must be positive")
    queue_path = REPORTS / ("new-independent-review-queue.jsonl" if args.new_only else "independent-review-queue.jsonl")
    packets_dir = PACKETS / ("new-content" if args.new_only else "")
    packets_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    # Load through the requested end so queue order remains authoritative.
    queue = load_queue(queue_path, args.start + args.limit - 1)
    for index, item in enumerate(queue[args.start - 1 : args.start - 1 + args.limit], args.start):
        rec = load_record(item)
        slug = f"{index:03d}-{item['id'][:8]}"
        path = packets_dir / f"{slug}.md"
        if path.exists():
            raise FileExistsError(f"refusing to overwrite existing packet: {path}")
        path.write_text(render(item, rec, load_source_question(item)), encoding="utf-8")
        manifest.append({"index": index, "path": str(path.relative_to(ROOT)).replace("\\", "/"), **item})
    manifest_path = packets_dir / "manifest.json"
    existing = []
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_index = {int(row["index"]): row for row in existing}
    by_index.update({int(row["index"]): row for row in manifest})
    manifest_path.write_text(json.dumps([by_index[k] for k in sorted(by_index)], ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"packets": len(manifest), "directory": str(packets_dir), "manifest": str(manifest_path), "queue": str(queue_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
