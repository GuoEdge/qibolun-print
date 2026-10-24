#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""岐伯论独立重建项目共享库。

提供：
- 语料/批次读取
- lexical（Zhihu RichText）结构解析为可供阅读的节点序列
- 正文段落切分与字符偏移计算
- DeepSeek 初读输出（JSONL）的机械验收

本文件不改写任何语料内容，只做只读解析与校验。
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta, timezone

CST = timezone(timedelta(hours=8))

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REBUILD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CORPUS_PATH = os.path.join(REPO_ROOT, "sooon-q9adg-articles-v2.jsonl")
BATCH_DIR = os.path.join(REBUILD_ROOT, "deepseek-batches")
OUT_DIR = os.path.join(REBUILD_ROOT, "out")
RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")

CORPUS_SHA256 = "E8617186FB3A82FD117C790499191B0E7B14D7A0C06E084C6D91CB5C5BF6AAA4"
SCHEMA_VERSION = "0.2.0"
RECORD_TYPE = "article_reading"

# lexical 节点类型 -> 输出 paragraph 的 field 取值
FIELD_BY_NODE = {
    "paragraph": "body",
    "heading": "heading",
    "list": "list",
    "listitem": "list",
    "quote": "quote",
    "code": "body",
    "code-highlight": "body",
}
IMAGE_NODE_TYPES = {"image", "image-placeholder", "img", "figure"}


# --------------------------------------------------------------------------
# 读取
# --------------------------------------------------------------------------
def read_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                raise ValueError(f"{path}:{lineno} 空行")
            rows.append(json.loads(line))
    return rows


def load_batch(batch_file):
    """读取一个批次文件（batch_id 以文件名或内容为准）。"""
    if not os.path.isabs(batch_file):
        batch_file = os.path.join(BATCH_DIR, batch_file)
    return read_jsonl(batch_file)


def load_manifest():
    with open(os.path.join(BATCH_DIR, "manifest.json"), "r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# lexical 结构解析
# --------------------------------------------------------------------------
def iter_lexical_nodes(lexical):
    """把 lexical JSON 深度优先展开为 (node_type, text, img_src) 序列。

    只处理结构节点；text 节点作为父节点的文本内容收集。
    """
    if not lexical:
        return []
    if isinstance(lexical, str):
        try:
            lexical = json.loads(lexical)
        except json.JSONDecodeError:
            return []
    root = lexical.get("root") if isinstance(lexical, dict) else None
    if root is None:
        return []
    out = []

    def walk(node):
        if not isinstance(node, dict):
            return
        ntype = str(node.get("type") or "")
        if ntype in ("text", "linebreak", "link"):
            return
        if ntype in IMAGE_NODE_TYPES:
            out.append(("image", "", node.get("src") or ""))
            return
        if ntype in FIELD_BY_NODE or ntype == "root":
            text = collect_text(node)
            if ntype != "root":
                out.append((ntype, text, ""))
            for child in node.get("children") or []:
                walk(child)
            return
        for child in node.get("children") or []:
            walk(child)

    walk(root)
    return out


def collect_text(node):
    """收集节点下所有 text/linebreak 叶子文本。"""
    parts = []

    def walk(n):
        if not isinstance(n, dict):
            return
        ntype = str(n.get("type") or "")
        if ntype == "text":
            parts.append(str(n.get("text") or ""))
            return
        if ntype == "linebreak":
            parts.append("\n")
            return
        for child in n.get("children") or []:
            walk(child)

    walk(node)
    return "".join(parts)


def image_srcs(lexical):
    if not lexical:
        return []
    if isinstance(lexical, str):
        try:
            lexical = json.loads(lexical)
        except json.JSONDecodeError:
            return []
    srcs = []

    def walk(n):
        if not isinstance(n, dict):
            return
        if str(n.get("type") or "") in IMAGE_NODE_TYPES:
            srcs.append(n.get("src") or "")
        for child in n.get("children") or []:
            walk(child)

    walk(lexical.get("root") or {})
    return srcs


_COMPACT_CACHE = {}


def _compact(body_text):
    """返回 (hay, index_map)：去掉空白后的正文与其原始下标映射（带缓存）。"""
    key = id(body_text)
    hit = _COMPACT_CACHE.get(key)
    if hit is not None and hit[0] is body_text:
        return hit[1], hit[2]
    hay_chars = []
    index_map = []
    for i, ch in enumerate(body_text):
        if not ch.isspace():
            hay_chars.append(ch)
            index_map.append(i)
    entry = (body_text, "".join(hay_chars), index_map)
    if len(_COMPACT_CACHE) > 8:
        _COMPACT_CACHE.clear()
    _COMPACT_CACHE[key] = entry
    return entry[1], entry[2]


def _span_in(body_text, cursor, needle):
    """在 body_text[cursor:] 中定位 needle，返回 (start, end, kind)。

    kind: exact=逐字匹配; loose=忽略空白匹配; missing=定位失败。
    """
    if not needle:
        return cursor, cursor, "empty"
    start = body_text.find(needle, cursor)
    if start >= 0:
        return start, start + len(needle), "exact"
    hay, index_map = _compact(body_text)
    target = "".join(ch for ch in needle if not ch.isspace())
    if not target:
        return cursor, cursor, "empty"
    pos = hay.find(target)
    if pos < 0:
        return None, None, "missing"
    return index_map[pos], index_map[pos + len(target) - 1] + 1, "loose"


def _lcs_length(a, b, cap=20000):
    """有界最长公共子序列长度（滚动数组，超出 cap 时截断）。"""
    if not a or not b:
        return 0
    a = a[:cap]
    b = b[:cap]
    if len(b) > len(a):
        a, b = b, a
    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0] * (len(b) + 1)
        for j, ch2 in enumerate(b, 1):
            if ch == ch2:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = cur[j - 1] if cur[j - 1] >= prev[j] else prev[j]
        prev = cur
    return prev[len(b)]


def lexical_only_chars(article, lcs_cap=6000):
    """估算 lexical 中存在、但 text 中找不到的正文规模。

    返回 (only_lexical_chars, common_chars, lex_chars, body_chars)，单位为字符
    （已忽略空白）。用于标记 text 与 lexical 存在版本性差异的文章。
    """
    body_text = article.get("text") or ""
    lex_nodes, _div = walk_body(article)
    lex_c = "".join(
        ch
        for ch in "".join(n["text"] for n in lex_nodes if n["field"] != "image")
        if not ch.isspace()
    )
    body_c = "".join(ch for ch in body_text if not ch.isspace())
    if not lex_c:
        return 0, 0, 0, len(body_c)
    if len(lex_c) <= lcs_cap and len(body_c) <= lcs_cap:
        common = _lcs_length(lex_c, body_c, cap=lcs_cap)
        return len(lex_c) - common, common, len(lex_c), len(body_c)
    # 超长文本：用顺序贪心匹配做保守下界估计（只可能高估差异）
    i = 0
    matched = 0
    n = len(body_c)
    for ch in lex_c:
        pos = body_c.find(ch, i)
        if pos < 0:
            continue
        matched += 1
        i = pos + 1
        if i >= n:
            i = n
    return len(lex_c) - matched, matched, len(lex_c), len(body_c)


_WALK_CACHE = {}


def walk_body(article):
    """以 text 为权威、以 lexical 为结构锚，产出正文片段序列。

    返回 (nodes, divergences)。nodes 元素为
    {"field","text","char_start","char_end","anchor"}；
    未被 lexical 覆盖的正文一律以 field="unmodeled" 原样保留，
    并在 divergences 中登记，避免任何正文内容被结构解析吞掉。
    """
    ck = article.get("id")
    if ck:
        hit = _WALK_CACHE.get(ck, (None, None))
        if hit[0] is article:
            return hit[1], hit[2]
    _nodes, _div = _walk_body_uncached(article)
    if ck:
        if len(_WALK_CACHE) > 64:
            _WALK_CACHE.clear()
        _WALK_CACHE[ck] = (article, _nodes, _div)
    return _nodes, _div


def _walk_body_uncached(article):
    """以 text 为权威、以 lexical 为结构锚，产出正文片段序列。

    返回 (nodes, divergences)。nodes 元素为
    {"field","text","char_start","char_end","anchor"}；
    未被 lexical 覆盖的正文一律以 field="unmodeled" 原样保留，
    并在 divergences 中登记，避免任何正文内容被结构解析吞掉。
    """
    body_text = article.get("text") or ""
    nodes = []
    divergences = []
    cursor = 0

    def walk(node, inherited=None):
        nonlocal cursor
        if not isinstance(node, dict):
            return
        ntype = str(node.get("type") or "")
        if ntype in IMAGE_NODE_TYPES:
            src = node.get("src") or ""
            nodes.append(
                {
                    "field": "image",
                    "text": "",
                    "char_start": cursor,
                    "char_end": cursor,
                    "anchor": "image",
                    "image_src": src,
                }
            )
            return
        if ntype in FIELD_BY_NODE:
            field = FIELD_BY_NODE[ntype]
            text = collect_text(node)
            leading = body_text[cursor:]
            lead_ns = len(leading) - len(leading.lstrip())
            if text.strip():
                start, end, kind = _span_in(body_text, cursor, text)
                if kind in {"exact", "loose"}:
                    if start > cursor:
                        gap = body_text[cursor:start]
                        if gap.strip():
                            nodes.append(
                                {
                                    "field": "unmodeled",
                                    "text": gap.strip(),
                                    "char_start": cursor
                                    + (len(gap) - len(gap.lstrip())),
                                    "char_end": cursor + len(gap.rstrip()),
                                    "anchor": "unmodeled",
                                }
                            )
                            divergences.append(
                                {
                                    "paragraph_kind": field,
                                    "reason": "text_has_content_not_in_lexical",
                                    "sample": gap.strip()[:120],
                                    "char_start": cursor + (len(gap) - len(gap.lstrip())),
                                }
                            )
                    nodes.append(
                        {
                            "field": field,
                            "text": body_text[start:end],
                            "char_start": start,
                            "char_end": end,
                            "anchor": ntype,
                        }
                    )
                    cursor = end
                    for child in node.get("children") or []:
                        walk(child, field)
                    return
                # lexical 有内容但 text 中找不到：保留 lexical 文本并标记
                nodes.append(
                    {
                        "field": field,
                        "text": text,
                        "char_start": None,
                        "char_end": None,
                        "anchor": "lexical_only",
                    }
                )
                divergences.append(
                    {
                        "paragraph_kind": field,
                        "reason": "lexical_content_not_found_in_text",
                        "sample": text.strip()[:120],
                        "char_start": None,
                    }
                )
                return
            # 空文本节点：其子节点仍可能承载内容
            for child in node.get("children") or []:
                walk(child, field)
            return
        for child in node.get("children") or []:
            walk(child, inherited)

    root = None
    lex = article.get("lexical")
    if lex:
        if isinstance(lex, str):
            try:
                lex = json.loads(lex)
            except json.JSONDecodeError:
                lex = None
        if isinstance(lex, dict):
            root = lex.get("root")
    if root:
        walk(root)
    if not nodes:
        # 无 lexical：按 text 换行切分
        idx = 0
        for chunk in body_text.split("\n"):
            if chunk.strip():
                lead = len(chunk) - len(chunk.lstrip())
                nodes.append(
                    {
                        "field": "body",
                        "text": chunk.strip(),
                        "char_start": idx + lead,
                        "char_end": idx + len(chunk.rstrip()),
                        "anchor": "text_only",
                    }
                )
            idx += len(chunk) + 1
        return nodes, divergences

    if cursor < len(body_text):
        tail = body_text[cursor:]
        if tail.strip():
            lead = len(tail) - len(tail.lstrip())
            nodes.append(
                {
                    "field": "unmodeled",
                    "text": tail.strip(),
                    "char_start": cursor + lead,
                    "char_end": cursor + len(tail.rstrip()),
                    "anchor": "unmodeled_tail",
                }
            )
            divergences.append(
                {
                    "paragraph_kind": "tail",
                    "reason": "text_tail_not_in_lexical",
                    "sample": tail.strip()[:120],
                    "char_start": cursor + lead,
                }
            )
    return nodes, divergences


def paragraphs_of(article):
    """产出结构化段落列表（text 权威 + lexical 锚定）。

    返回 [{"paragraph_id","field","index","text","char_start","char_end","anchor"}]
    paragraph_id 以正文顺序连续编号，覆盖提问之外的全文文本。
    """
    nodes, _div = walk_body(article)
    paragraphs = []
    pid = 0
    for n in nodes:
        if n["field"] == "image":
            continue
        if not n["text"].strip():
            continue
        pid += 1
        paragraphs.append(
            {
                "paragraph_id": "P%03d" % pid,
                "field": n["field"],
                "index": pid,
                "text": n["text"],
                "char_start": n["char_start"],
                "char_end": n["char_end"],
                "anchor": n["anchor"],
            }
        )
    return paragraphs


def published_iso(published_at):
    if published_at in (None, ""):
        return ""
    try:
        return datetime.fromtimestamp(int(published_at) / 1000, CST).isoformat()
    except (ValueError, OSError, TypeError):
        return ""


# --------------------------------------------------------------------------
# 机械验收
# --------------------------------------------------------------------------
CLAIM_TYPES = {
    "author_explicit",
    "author_qualified",
    "author_reported",
    "quoted_or_cited",
    "opponent_view",
    "research_reconstruction",
    "open_question",
}
ATTRIBUTIONS = {"author", "questioner", "cited_source", "opponent", "unknown"}
MODALITIES = {"asserted", "qualified", "hypothetical", "questioned", "negated", "predicted"}
EVIDENCE_RELATIONS = {"supports", "qualifies", "contradicts", "context"}
UNITS_ROLES = {
    "claim",
    "reason",
    "example",
    "rebuttal",
    "qualification",
    "action_advice",
    "transition",
    "conclusion",
    "definition",
    "context",
    "other",
}
IMAGE_STATUSES = {
    "not_applicable",
    "pending",
    "assisted",
    "verified",
    "unreadable",
    "missing",
}
READING_STATUSES = {"read", "blocked", "needs_reread"}


_CORPUS_TEXT_CACHE = {}


def corpus_text_map(corpus_path=CORPUS_PATH):
    """按文章 id 返回语料原始 text/question（惰性加载并缓存）。"""
    key = os.path.abspath(corpus_path)
    hit = _CORPUS_TEXT_CACHE.get(key)
    if hit is not None:
        return hit
    m = {}
    with open(key, "r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            o = json.loads(line)
            m[str(o["id"])] = {
                "text": o.get("text") or "",
                "question": o.get("question") or "",
            }
    _CORPUS_TEXT_CACHE[key] = m
    return m


def validate_batch(input_path, output_path, corpus_sha256=CORPUS_SHA256, corpus_path=CORPUS_PATH):
    """对单批输出做机械验收，返回 (ok, result_dict)。"""
    fails = []
    warns = []

    def fail(msg):
        fails.append(msg)

    def warn(msg):
        warns.append(msg)

    inputs = read_jsonl(input_path)
    in_by_id = {}
    order = []
    for row in inputs:
        art = row["article"]
        aid = str(art["id"])
        if aid in in_by_id:
            fail(f"输入重复 id {aid}")
        in_by_id[aid] = row
        order.append(aid)

    outputs = []
    if not os.path.exists(output_path):
        return False, {
            "status": "FAIL",
            "input_batch": os.path.basename(str(input_path)),
            "output_file": os.path.basename(str(output_path)),
            "input_records": len(inputs),
            "output_records": 0,
            "failures": [f"输出文件不存在: {output_path}"],
            "warnings": [],
        }
    with open(output_path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                fail(f"输出第 {lineno} 行为空行")
                continue
            try:
                outputs.append(json.loads(line))
            except json.JSONDecodeError as exc:
                fail(f"输出第 {lineno} 行 JSON 解析失败: {exc}")

    if len(outputs) != len(inputs):
        fail(f"行数不匹配 输出={len(outputs)} 输入={len(inputs)}")

    seen = set()
    for rec in outputs:
        aid = str(rec.get("article_id") or "")
        if not aid:
            fail("缺少 article_id")
            continue
        tag = aid[:8]
        if aid in seen:
            fail(f"输出重复 article_id {aid}")
        seen.add(aid)
        if aid not in in_by_id:
            fail(f"输出 article_id 不在输入中 {aid}")
            continue
        src = in_by_id[aid]
        art = src["article"]

        if str(rec.get("record_type")) != RECORD_TYPE:
            fail(f"{tag} record_type 必须为 {RECORD_TYPE}")
        if str(rec.get("schema_version")) != SCHEMA_VERSION:
            fail(f"{tag} schema_version 应为 {SCHEMA_VERSION}")
        if str(rec.get("corpus_sha256")).upper() != corpus_sha256.upper():
            fail(f"{tag} corpus_sha256 与批次不一致")
        if int(rec.get("source_ordinal", -1)) != int(art["source_ordinal"]):
            fail(f"{tag} source_ordinal 不一致")
        if int(rec.get("reading_ordinal", -1)) != int(art["reading_ordinal"]):
            fail(f"{tag} reading_ordinal 不一致")
        meta = rec.get("metadata") or {}
        if str(meta.get("title", "")) != str(art.get("title", "")):
            fail(f"{tag} title 未原样回填")
        if str(meta.get("url", "")) != str(art.get("url", "")):
            fail(f"{tag} url 未原样回填")

        st = rec.get("structure") or {}
        rd = rec.get("reading") or {}
        status = str(rd.get("status"))
        if status not in READING_STATUSES:
            fail(f"{tag} reading.status 非法: {status}")
        full = bool(st.get("full_text_checked"))
        img_checked = bool(rd.get("image_checked"))
        paras = st.get("paragraphs") or []
        images = st.get("images") or []
        # 图片-only article may legitimately have no text paragraphs. It must
        # remain needs_reread until the images are inspected; do not fabricate
        # a P001 paragraph or evidence quote for absent source text.
        image_only_unread = (not paras) and bool(images) and status == "needs_reread"
        if not paras and not image_only_unread:
            fail(f"{tag} paragraphs 为空")

        pids = {}
        for p in paras:
            pid = str(p.get("paragraph_id") or "")
            if not pid:
                fail(f"{tag} 存在空 paragraph_id")
                continue
            if pid in pids:
                fail(f"{tag} paragraph_id 重复 {pid}")
            pids[pid] = p
            if str(p.get("field")) not in {
                "question",
                "body",
                "heading",
                "list",
                "quote",
                "image",
            }:
                fail(f"{tag}/{pid} field 非法: {p.get('field')}")
        iids = {}
        for im in images:
            iid = str(im.get("image_id") or "")
            if not iid:
                fail(f"{tag} 存在空 image_id")
                continue
            if iid in iids:
                fail(f"{tag} image_id 重复 {iid}")
            iids[iid] = im
            if str(im.get("status")) not in IMAGE_STATUSES:
                fail(f"{tag}/{iid} image status 非法: {im.get('status')}")

        if status == "read" and not full:
            fail(f"{tag} status=read 但 full_text_checked=false")
        if images and status == "read" and not img_checked:
            fail(f"{tag} 图片文章 status=read 但 image_checked=false")
        if images and status == "read":
            for iid, im in iids.items():
                if str(im.get("status")) == "pending":
                    fail(f"{tag}/{iid} 图片仍为 pending，不得标记 read")
        for iid, im in iids.items():
            ist = str(im.get("status"))
            if ist == "not_applicable" and str(im.get("src") or "").strip():
                fail(f"{tag}/{iid} 图片存在却标为 not_applicable（应为 pending/assisted/verified/unreadable/missing）")
            if ist == "verified" and not img_checked:
                fail(f"{tag}/{iid} 图片标为 verified 但 image_checked=false")
        if status in {"blocked", "needs_reread"}:
            notes = str(rec.get("notes") or "")
            uq = (rec.get("analysis") or {}).get("unresolved_questions") or []
            if not notes.strip() and not uq:
                fail(f"{tag} status={status} 但未在 notes/unresolved_questions 说明原因")

        ev_ids = {}
        for ev in rec.get("evidence_refs") or []:
            eid = str(ev.get("evidence_id") or "")
            if not eid:
                fail(f"{tag} evidence_ref 缺少 evidence_id")
                continue
            if eid in ev_ids:
                fail(f"{tag} evidence_id 重复 {eid}")
            ev_ids[eid] = ev
            pid = ev.get("paragraph_id")
            iid = ev.get("image_id")
            if pid and str(pid) not in pids:
                fail(f"{tag} evidence {eid} 引用不存在的 paragraph_id {pid}")
            if iid and str(iid) not in iids:
                fail(f"{tag} evidence {eid} 引用不存在的 image_id {iid}")
            if not pid and not iid:
                fail(f"{tag} evidence {eid} 既无 paragraph_id 也无 image_id")
            rel = str(ev.get("relation") or "")
            if rel and rel not in EVIDENCE_RELATIONS:
                fail(f"{tag} evidence {eid} relation 非法: {rel}")
            # 短引必须来自原文（先核对本记录转录，再回查语料原文）
            quote = ev.get("quote")
            if quote:
                hay = ""
                if pid and str(pid) in pids:
                    hay = str(pids[str(pid)].get("text") or "")
                if hay and str(quote) in hay:
                    pass
                else:
                    src_text = corpus_text_map(corpus_path).get(aid, {}).get("text", "")
                    if str(quote) not in src_text:
                        fail(f"{tag} evidence {eid} 短引不在原文中（段落 {pid}）")
            elif not str(ev.get("quote_unavailable_reason") or "").strip():
                warn(f"{tag} evidence {eid} 无短引且未说明 quote_unavailable_reason")

        analysis = rec.get("analysis") or {}
        if not str(analysis.get("question_context") or "").strip():
            fail(f"{tag} analysis.question_context 为空")
        if not str(analysis.get("rhetoric_and_tone") or "").strip():
            warn(f"{tag} analysis.rhetoric_and_tone 为空")
        units = analysis.get("content_units") or []
        uids = set()
        for u in units:
            uid = str(u.get("unit_id") or "")
            if not uid:
                fail(f"{tag} content_unit 缺少 unit_id")
                continue
            if uid in uids:
                fail(f"{tag} content_unit unit_id 重复 {uid}")
            uids.add(uid)
            refs = u.get("paragraph_refs") or []
            if not refs and not image_only_unread:
                fail(f"{tag}/{uid} content_unit 缺少 paragraph_refs")
            for r in refs:
                if str(r) not in pids:
                    fail(f"{tag}/{uid} paragraph_refs 引用不存在的 {r}")

        # 完整性红线：四类语义内容全空说明该篇并未真正精读（构造器会用"本文未说明"占位，
        # 不能因此被当成已读）。真实完成的记录至少有 content_units 或主张/论证/证据之一。
        if (
            not units
            and not (analysis.get("main_claims") or [])
            and not (analysis.get("argument_steps") or [])
            and not (rec.get("evidence_refs") or [])
        ):
            fail(
                f"{tag} 分析内容为空（无 content_units/main_claims/argument_steps/evidence_refs）："
                "该篇未完成精读，不得计入 PASS"
            )

        cids = set()
        for claim in analysis.get("main_claims") or []:
            cid = str(claim.get("claim_id") or "")
            if not cid:
                fail(f"{tag} main_claim 缺少 claim_id")
                continue
            if cid in cids:
                fail(f"{tag} claim_id 重复 {cid}")
            cids.add(cid)
            ctype = str(claim.get("claim_type") or "")
            if ctype not in CLAIM_TYPES:
                fail(f"{tag}/{cid} claim_type 非法: {ctype}")
            attr = str(claim.get("attribution") or "")
            if attr not in ATTRIBUTIONS:
                fail(f"{tag}/{cid} attribution 非法: {attr}")
            modal = str(claim.get("modality") or "")
            if modal not in MODALITIES:
                fail(f"{tag}/{cid} modality 非法: {modal}")
            if not str(claim.get("statement") or "").strip():
                fail(f"{tag}/{cid} 主张缺少 statement")
            if ctype == "research_reconstruction":
                warn(f"{tag}/{cid} 初读阶段出现 research_reconstruction，跨文章归纳应留给后续研究")
            refs = claim.get("evidence_refs") or []
            if ctype in {"author_explicit", "author_qualified", "author_reported"} and not refs:
                fail(f"{tag}/{cid} {ctype} 主张缺少证据引用")
            for r in refs:
                if str(r) not in ev_ids:
                    fail(f"{tag}/{cid} 证据引用不存在 {r}")
            if ctype == "research_reconstruction" and attr == "author":
                warn(f"{tag}/{cid} research_reconstruction 归属为 author，注意不得写成作者说法")
            quote_len = len(str(claim.get("statement") or ""))
            if quote_len > 400:
                warn(f"{tag}/{cid} statement 过长（{quote_len} 字），宜为中性转述")

        for ev in rec.get("evidence_refs") or []:
            if len(str(ev.get("quote") or "")) > 200:
                warn(f"{tag}/{ev.get('evidence_id')} 短引超过 200 字，建议只保留承担主张的最短片段")

        # 单篇"作者侧内容"体量上限：只计 reading/analysis/provisional_tags/evidence_refs/notes，
        # 不计机械生成的 structure（超长文章 300+ 段落的结构脚手架本身就很大，不应因此判定失败）。
        authored = {
            "reading": rec.get("reading"),
            "analysis": rec.get("analysis"),
            "provisional_tags": rec.get("provisional_tags"),
            "evidence_refs": rec.get("evidence_refs"),
            "notes": rec.get("notes"),
        }
        rec_size = len(json.dumps(authored, ensure_ascii=False).encode("utf-8"))
        if rec_size > 40000:
            fail(
                f"{tag} 单篇作者侧内容 {rec_size} 字节，超过 40000 上限：请压缩内容后重做"
                "（短引只留承担主张的最短片段、合并高度重复的主张与内容单元、"
                "精简 summary/argument_steps/conditions 的文字量），不要删减证据定位和未决问题"
            )

        if not str(rd.get("reader_id") or "").strip():
            fail(f"{tag} reading.reader_id 为空")
        if not str(rd.get("batch_id") or "").strip():
            fail(f"{tag} reading.batch_id 为空")
        if str(rd.get("batch_id")) != str(src.get("batch_id")):
            fail(f"{tag} reading.batch_id 与输入批次不一致")

        tags = rec.get("provisional_tags") or {}
        if str(tags.get("status")) != "provisional":
            fail(f"{tag} provisional_tags.status 应为 provisional")

        # 空正文文章
        if not str(art.get("text") or "").strip():
            if status == "read":
                fail(f"{tag} 空正文文章不得标记 read")

    for aid in order:
        if aid not in seen:
            fail(f"缺少输出: {aid}")

    result = {
        "status": "PASS" if not fails else "FAIL",
        "input_batch": os.path.basename(str(input_path)),
        "output_file": os.path.basename(str(output_path)),
        "input_records": len(inputs),
        "output_records": len(outputs),
        "failures": fails,
        "warnings": warns,
    }
    return (not fails), result


def main():
    import argparse

    ap = argparse.ArgumentParser(description="岐伯论初读 JSONL 机械验收")
    ap.add_argument("input_batch")
    ap.add_argument("output_jsonl")
    ap.add_argument("--json", action="store_true", help="输出 JSON 结果")
    args = ap.parse_args()
    ok, result = validate_batch(args.input_batch, args.output_jsonl)
    if "input_records" not in result:
        result.setdefault("input_batch", os.path.basename(str(args.input_batch)))
        result.setdefault("output_file", os.path.basename(str(args.output_jsonl)))
        result.setdefault("input_records", 0)
        result.setdefault("output_records", 0)
        result.setdefault("warnings", [])
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"[{result['status']}] {result['input_batch']} -> {result['output_file']}")
        print(f"  输入 {result['input_records']} 条 / 输出 {result['output_records']} 条")
        for f in result["failures"]:
            print(f"  FAIL {f}")
        for w in result["warnings"]:
            print(f"  WARN {w}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
