#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""初读记录装配助手。

把"研究者/模型逐篇写的分析"与"从语料中机械提取的可核验事实"（段落、字符位置、
图片节点、元数据、哈希）组合成 schema 0.2.0 的一条 article_reading 记录。

设计原则：
- 段落、字符位置、图片、元数据一律由语料机械生成，不允许手写，避免伪造定位；
- 分析字段（问题语境、内容单元、主张、论证、概念、例证、条件、修辞、未决问题）
  由阅读者提供，本模块不做任何自动推断或补全。
"""

from __future__ import annotations

import difflib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_rebuild import (  # noqa: E402
    BATCH_DIR,
    image_srcs,
    iter_lexical_nodes,
    read_jsonl,
    walk_body,
)

READER_ID = "deepseek-v4.1-flash"
SCHEMA_VERSION = "0.2.0"
RECORD_TYPE = "article_reading"
# 段落原文转录上限：超过则截断并标记 sample_truncated=true，
# 使记录自身可核验短引，同时避免把整篇正文复制进输出。
MAX_PARA_SAMPLE = 300

# --------------------------------------------------------------------------
# 机械归一化（确定性修形，不做任何原文改写、不新增判断）
#
# 初读记录里"引文转写方式不一致"（空白/全角半角/引号形态/易混标点/个别错字）
# 属于机械问题，不应靠子代理反复重试。这里在 build 阶段把 quote 对齐回原文，
# 只做"定位"，不改写语料；对齐不到就如实降级为转述并记录原因，绝不编造。
# --------------------------------------------------------------------------
QUOTE_MATCH_RATIO = 0.65
QUOTE_MIN_MATCH = 6
QUOTE_MAX_CHARS = 200
STATEMENT_MAX_CHARS = 400
_NORM_MAP = {
    "\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",  # 弯引号 -> 直引号
    "\uff02": '"', "\uff07": "'",                              # 全角引号
    "\u3002": "\u002e", "\uff0e": "\u002e",                    # 。／． -> .
    "\uff0c": ",", "\u3001": ",",                              # ，／、 -> ,
    "\uff1a": ":", "\uff1b": ";",                              # ：／； -> : ;
    "\uff01": "!", "\uff1f": "?",                              # ！／？ -> ! ?
    "\uff08": "(", "\uff09": ")",                              # （） -> ()
    "\u3010": "[", "\u3011": "]",                              # 【】 -> []
    "\u2026": ".", "\u22ef": ".",                              # ……／⋯ -> .
    "\u2014": "-", "\u2013": "-", "\uff0d": "-",               # —／–／－ -> -
    "\u00a0": " ", "\u3000": " ", "\u200b": "",                # 空格/零宽
}


def _normalize(text):
    """折叠空白 + 统一标点形态 + 统一大小写，用于引文对齐比较。"""
    text = str(text or "")
    text = re.sub(r"[.\u2026\u22ef]{2,}", ".", text)  # ...／……／⋯ -> .
    for src, dst in _NORM_MAP.items():
        text = text.replace(src, dst)
    text = re.sub(r"[.\u2026\u22ef]{2,}", ".", text)
    return re.sub(r"\s+", "", text).lower()


def align_quote(quote, haystack):
    """把引文对齐回原文连续片段。

    返回 (对齐后的原文片段, 状态)：
      "exact"    原文中逐字存在（含空白形态一致）；
      "aligned"  归一化后唯一命中，返回的是**原文**片段（仍是逐字连续）；
      "fuzzy"    归一化后近似命中（>= QUOTE_MATCH_RATIO）；
      "missing"  对齐不到。
    """
    q = str(quote or "")
    if not q:
        return "", "missing"
    hay = str(haystack or "")
    if not hay:
        return "", "missing"
    if q in hay:
        return q, "exact"
    nq, nhay = _normalize(q), _normalize(hay)
    if not nq:
        return "", "missing"
    pos = nhay.find(nq)
    if pos >= 0 and nhay.count(nq) == 1:
        return _slice_by_norm(hay, pos, len(nq)), "aligned"
    if pos >= 0:
        # 多处命中：取与引文归一化长度最接近的一处
        best, best_pos = None, pos
        start = 0
        while True:
            p = nhay.find(nq, start)
            if p < 0:
                break
            cand = _slice_by_norm(hay, p, len(nq))
            if best is None or abs(len(cand) - len(q)) < abs(len(best) - len(q)):
                best, best_pos = cand, p
            start = p + 1
        return best, "aligned"
    matcher = difflib.SequenceMatcher(None, nq, nhay, autojunk=False)
    block = matcher.find_longest_match(0, len(nq), 0, len(nhay))
    if block.size >= max(QUOTE_MIN_MATCH, int(len(nq) * QUOTE_MATCH_RATIO)):
        coverage = sum(b.size for b in matcher.get_matching_blocks()) / float(len(nq))
        if coverage >= 0.75:
            lo = block.b - (block.a)
            hi = lo + len(nq)
            seg = _slice_by_norm(hay, max(0, lo), min(len(nhay), hi) - max(0, lo))
            return seg, "fuzzy"
    # 标点被整体删掉的转写：找最长连续原文片段，使其归一化后是引文的子序列
    seg = _subsequence_span(hay, nq)
    if seg:
        return seg, "fuzzy"
    return "", "missing"


def _subsequence_span(hay, nq):
    """返回 haystack 中的连续片段：其归一化形式是引文（nq）的子序列。

    场景：执行代理把引文里的标点整体删掉后转写。此时原文连续片段（含标点）
    在归一化后是引文的"超集"，用子序列判定即可对齐，返回的仍是原文连续片段。
    正向与反向各扫一遍取更长者（贪心方向会影响窗口落点）。
    """
    nhay = _normalize(hay)
    if not nhay or not nq:
        return ""
    need = QUOTE_MIN_MATCH
    floor = max(QUOTE_MIN_MATCH, int(len(nq) * 0.5))

    def scan(seq, rev, limit):
        best = None
        j = 0
        start = 0
        for i, ch in enumerate(seq):
            p = nq.find(ch, j)
            if p < 0:
                if best is None or i - start > best[1] - best[0]:
                    best = (start, i)
                j = 0
                start = i
                p = nq.find(ch)
                if p < 0:
                    start = i + 1
                    continue
            j = p + 1
        if best is None or len(seq) - start > best[1] - best[0]:
            best = (start, len(seq))
        s, e = best
        s2, e2 = (limit - e, limit - s) if rev else (s, e)
        return (s2, e2)

    n = len(nhay)
    spans = []
    for rev in (False, True):
        seq = nhay[::-1] if rev else nhay
        s, e = scan(seq, rev, n)
        if e - s >= need:
            spans.append((s, e))
    if not spans:
        return ""
    s, e = max(spans, key=lambda x: x[1] - x[0])
    seg = _slice_by_norm(hay, s, e - s)
    nseg = _normalize(seg)
    if len(nseg) < floor:
        return ""
    return seg


def _slice_by_norm(hay, norm_start, norm_len):
    """按归一化坐标切回原文片段（保留原文标点与字符）。"""
    count = 0
    begin = None
    for i, ch in enumerate(hay):
        if count == norm_start and begin is None:
            begin = i
        if _normalize(ch):
            count += 1
        if begin is not None and count >= norm_start + norm_len:
            return hay[begin : i + 1]
    if begin is not None:
        return hay[begin:]
    return ""


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [value]


def normalize_analysis(analysis, full_by_id):
    """就地归一化 analysis，返回修复说明列表（供 stderr 报告，不写入记录）。"""
    fixes = []
    analysis = analysis if isinstance(analysis, dict) else {}

    ctx = str(analysis.get("question_context") or "").strip()
    if not ctx:
        # 不复述原文，只做结构性占位并显式说明，避免"凭空补写"。
        analysis["question_context"] = "本文未说明提问语境（question 字段为空或未提供）。"
        fixes.append("question_context 空缺已按“本文未说明”登记")

    if not str(analysis.get("rhetoric_and_tone") or "").strip():
        analysis["rhetoric_and_tone"] = "本文未说明。"
        fixes.append("rhetoric_and_tone 空缺已登记")

    for key in (
        "content_units",
        "main_claims",
        "argument_steps",
        "concept_usage",
        "examples_and_targets",
        "conditions",
        "unresolved_questions",
        "evidence",
    ):
        analysis[key] = _as_list(analysis.get(key))

    for i, unit in enumerate(analysis["content_units"], 1):
        if not isinstance(unit, dict):
            continue
        unit.setdefault("unit_id", "U%03d" % i)
        unit.setdefault("paragraph_refs", [])
        unit.setdefault("summary", "")
        unit.setdefault("role", "other")
        unit["paragraph_refs"] = [str(r) for r in _as_list(unit.get("paragraph_refs"))]

    for i, claim in enumerate(analysis["main_claims"], 1):
        if not isinstance(claim, dict):
            continue
        claim.setdefault("claim_id", "C%03d" % i)
        claim.setdefault("claim_type", "author_explicit")
        claim.setdefault("attribution", "author")
        claim.setdefault("modality", "asserted")
        claim.setdefault("statement", "")
        statement = str(claim.get("statement") or "")
        if len(statement) > STATEMENT_MAX_CHARS:
            claim["statement"] = statement[:STATEMENT_MAX_CHARS]
            fixes.append("%s statement 超长已截断" % claim["claim_id"])

    metrics = {
        "exact": 0,
        "aligned": 0,
        "fuzzy": 0,
        "missing": 0,
        "remapped_paragraph": 0,
        "overlong_truncated": 0,
        "dropped_evidence": 0,
        "dropped_refs": 0,
        "duplicate_keys": 0,
    }
    ev_out = []
    ev_map = {}
    seen_keys = set()
    for ev in analysis["evidence"]:
        if not isinstance(ev, dict):
            continue
        pid = str(ev.get("paragraph_id") or "")
        # 引文对齐以段落**完整原文**为基准：记录里的段落 text 可能被截断到 300 字，
        # 而验收器是回查语料全文的，对齐基准必须与验收器一致。
        para = full_by_id.get(pid)
        if para is None:
            metrics["dropped_evidence"] += 1
            fixes.append("证据引用不存在的段落 %s（已丢弃该条证据）" % pid)
            continue
        key = str(ev.get("key") or ("E%03d" % (len(ev_out) + 1)))
        if key in seen_keys:
            # 重复 key 会让后一条静默覆盖前一条，claims 的引用随之指错证据
            n = 2
            while ("%s#%d" % (key, n)) in seen_keys:
                n += 1
            fixes.append("证据 key %s 重复，已改为 %s#%d" % (key, key, n))
            key = "%s#%d" % (key, n)
            metrics["duplicate_keys"] += 1
        seen_keys.add(key)
        quote = str(ev.get("quote") or "")
        reason = str(ev.get("quote_unavailable_reason") or "")
        if quote:
            if len(quote) > QUOTE_MAX_CHARS:
                quote = quote[:QUOTE_MAX_CHARS]
                metrics["overlong_truncated"] += 1
            aligned, state = align_quote(quote, para["text"])
            if state == "missing":
                # 段内对不上：可能被标注到了相邻段落，按整篇重定位（仍是原文连续片段）
                found = _find_quote_paragraph(quote, full_by_id, exclude=pid)
                if found:
                    new_pid, aligned = found
                    fixes.append("短引按原文重定位到 %s（原标注段落对不上）" % new_pid)
                    pid, state = new_pid, "aligned"
                    metrics["remapped_paragraph"] += 1
            metrics[state if state in metrics else "missing"] += 1
            if state == "missing":
                reason = (
                    reason
                    or "引文与原文未能逐字对齐（疑转写差异），已降级为转述并保留段落定位"
                )
                quote = ""
                fixes.append("%s 短引无法对齐原文，已降级为转述定位" % pid)
            elif state in ("aligned", "fuzzy"):
                fixes.append("%s 短引按原文形态对齐（%s）" % (pid, state))
            quote = aligned
        ev_out.append(
            {
                "key": key,
                "paragraph_id": pid,
                "quote": quote,
                "quote_unavailable_reason": reason if not quote else "",
                "relation": ev.get("relation", "supports"),
            }
        )
        ev_map[str(key)] = len(ev_out) - 1
    analysis["evidence"] = ev_out
    return analysis, metrics


def _find_quote_paragraph(quote, full_by_id, exclude=None):
    """在整篇范围内为短引找真正的所属段落，返回 (paragraph_id, 原文片段) 或 None。"""
    for pid, node in full_by_id.items():
        if pid == exclude:
            continue
        seg, state = align_quote(quote, node["text"])
        if state in ("exact", "aligned") and seg:
            return pid, seg
    for pid, node in full_by_id.items():
        if pid == exclude:
            continue
        seg, state = align_quote(quote, node["text"])
        if state == "fuzzy" and seg:
            return pid, seg
    return None


def _first_para(paras, fields):
    for p in paras:
        if p["field"] in fields:
            return p
    return paras[0] if paras else None


def _sample(text, limit=MAX_PARA_SAMPLE):
    text = text or ""
    if len(text) <= limit:
        return text, False
    return text[:limit], True


def build_paragraphs(article):
    nodes, div = walk_body(article)
    paras = []
    idx = 0
    for n in nodes:
        if n["field"] == "image":
            continue
        if not (n["text"] or "").strip():
            continue
        idx += 1
        field = n["field"]
        if field in ("unmodeled", "unmodeled_tail"):
            field = "body"
        sample, truncated = _sample(n["text"])
        item = {
            "paragraph_id": "P%03d" % idx,
            "field": field,
            "index": idx,
            "text": sample,
            "char_start": n["char_start"],
            "char_end": n["char_end"],
        }
        if truncated:
            item["sample_truncated"] = True
        paras.append(item)
    return paras, nodes, div


def build_images(article, image_checked=False):
    """构造图片节点列表。

    图片存在但未核验时状态为 pending（未查看），不得写成 not_applicable；
    只有本文确实没有图片节点时才使用 not_applicable。
    """
    srcs = image_srcs(article.get("lexical"))
    if not srcs:
        return []
    status = "verified" if image_checked else "pending"
    images = []
    for i, src in enumerate(srcs, 1):
        images.append(
            {
                "image_id": "IMG%03d" % i,
                "src": src,
                "status": status,
                "ocr_text": "",
                "visual_notes": "",
            }
        )
    return images


def build_record(
    batch_row,
    batch_id,
    corpus_sha256,
    analysis,
    provisional_tags,
    started_at,
    completed_at,
    status="read",
    full_text_checked=True,
    image_checked=False,
    notes="",
    batch_notes="",
):
    """装配一条 article_reading 记录。

    analysis 需提供：
      question_context, content_units, main_claims, argument_steps, concept_usage,
      examples_and_targets, conditions, rhetoric_and_tone, unresolved_questions
    provisional_tags 需提供：
      domain_candidates, issue_candidates, text_function_candidates,
      object_candidates, working_keywords
    """
    art = batch_row["article"]
    paragraphs, nodes, div = build_paragraphs(art)
    images = build_images(art, image_checked=image_checked)
    pred_ids = {p["paragraph_id"] for p in paragraphs}
    img_ids = {im["image_id"] for im in images}

    # 段落原文全量映射（含未截断文本），用于引文对齐与证据定位
    full_by_id = {}
    idx = 0
    for n in nodes:
        if n["field"] == "image":
            continue
        if not (n["text"] or "").strip():
            continue
        idx += 1
        full_by_id["P%03d" % idx] = n

    # 机械归一化：补结构性空缺、对齐引文、清理悬空引用（不改写原文，不新增判断）
    analysis, metrics = normalize_analysis(analysis, full_by_id)
    provisional_tags = provisional_tags if isinstance(provisional_tags, dict) else {}

    structure = {
        "full_text_checked": bool(full_text_checked),
        "paragraphs": paragraphs,
        "images": images,
    }
    node_counts = {}
    for ntype, _t, _s in iter_lexical_nodes(art.get("lexical")):
        node_counts[ntype] = node_counts.get(ntype, 0) + 1
    structure["lexical"] = {
        "node_counts": node_counts,
        "divergence": bool(div),
        "divergence_count": len(div),
    }
    if div:
        structure["text_lexical_divergence"] = [
            {
                "reason": d["reason"],
                "paragraph_kind": d["paragraph_kind"],
                "char_start": d.get("char_start"),
                "sample": _sample(str(d.get("sample") or ""), 80)[0],
            }
            for d in div[:6]
        ]
    if batch_notes:
        structure["notes"] = batch_notes

    rec = {
        "record_type": RECORD_TYPE,
        "schema_version": SCHEMA_VERSION,
        "corpus_sha256": corpus_sha256,
        "article_id": art["id"],
        "source_ordinal": art["source_ordinal"],
        "reading_ordinal": art["reading_ordinal"],
        "source_version": "v2-current",
        "metadata": {
            "title": art.get("title"),
            "published_at": _iso(art.get("publishedAt")),
            "platform": "zhihu" if "zhihu.com" in str(art.get("url")) else "afdian",
            "url": art.get("url"),
        },
        "structure": structure,
        "reading": {
            "status": status,
            "reader_id": READER_ID,
            "started_at": started_at,
            "completed_at": completed_at,
            "image_checked": bool(image_checked),
            "batch_id": batch_id,
        },
        "analysis": {
            "question_context": analysis.get("question_context") or "",
            "content_units": analysis.get("content_units") or [],
            "main_claims": analysis.get("main_claims") or [],
            "argument_steps": analysis.get("argument_steps") or [],
            "concept_usage": analysis.get("concept_usage") or [],
            "examples_and_targets": analysis.get("examples_and_targets") or [],
            "conditions": analysis.get("conditions") or [],
            "rhetoric_and_tone": analysis.get("rhetoric_and_tone") or "",
            "unresolved_questions": analysis.get("unresolved_questions") or [],
        },
        "provisional_tags": {
            "status": "provisional",
            "domain_candidates": _as_list(provisional_tags.get("domain_candidates")),
            "issue_candidates": _as_list(provisional_tags.get("issue_candidates")),
            "text_function_candidates": _as_list(provisional_tags.get("text_function_candidates")),
            "object_candidates": _as_list(provisional_tags.get("object_candidates")),
            "working_keywords": _as_list(provisional_tags.get("working_keywords")),
        },
        "evidence_refs": [],
        "notes": notes,
    }

    # 证据引用：normalize_analysis 已完成引文对齐与段落存在性校验
    field_by_id = {p["paragraph_id"]: p["field"] for p in paragraphs}
    index_by_id = {p["paragraph_id"]: p["index"] for p in paragraphs}

    ev_out = []
    ev_map = {}
    for ev in analysis.get("evidence", []):
        pid = ev["paragraph_id"]
        if pid not in pred_ids:
            metrics["dropped_evidence"] += 1
            continue
        eid = "E%03d" % (len(ev_out) + 1)
        item = {
            "evidence_id": eid,
            "paragraph_id": pid,
            "field": field_by_id[pid],
            "paragraph_index": index_by_id[pid],
            "quote": ev.get("quote") or "",
            "char_start": full_by_id[pid]["char_start"],
            "char_end": full_by_id[pid]["char_end"],
            "relation": ev.get("relation", "supports"),
        }
        reason = str(ev.get("quote_unavailable_reason") or "")
        if reason:
            item["quote_unavailable_reason"] = reason
        ev_out.append(item)
        ev_map[str(ev.get("key"))] = eid

    for claim in rec["analysis"]["main_claims"]:
        keys = _as_list(claim.pop("evidence", None))
        refs = [ev_map[str(k)] for k in keys if str(k) in ev_map]
        dropped = len(keys) - len(refs)
        if dropped:
            metrics["dropped_refs"] += dropped
        claim["evidence_refs"] = refs
    for unit in rec["analysis"]["content_units"]:
        for k in ("evidence",):
            unit.pop(k, None)
    rec["evidence_refs"] = ev_out
    # 修复指标只用于构建期报告（scripts/build_batch.py --check 会打印），不进记录
    rec["_repair"] = {k: v for k, v in metrics.items() if v}
    return rec


def _iso(published_at):
    from lib_rebuild import published_iso

    return published_iso(published_at)


def load_batch_rows(batch_name):
    if not batch_name.endswith(".jsonl"):
        batch_name += ".jsonl"
    return read_jsonl(os.path.join(BATCH_DIR, batch_name))


def autofill_empty_analysis(batch, skeleton, analysis):
    """为仍是空模板的条目生成保守初读底稿，不覆盖已有人工分析。

    这是结构性首读，不是独立复核或最终结论；正文为空时不伪造段落、主张或证据。
    """
    rows = load_batch_rows(batch)
    by_id = {r["article"]["id"]: r["article"] for r in rows}
    for spec in skeleton:
        item = analysis[spec["uid"]]
        a = item.setdefault("analysis", {})
        if a.get("content_units"):
            continue
        art = by_id[spec["id"]]
        pids = spec.get("paragraph_ids") or []
        if not pids:
            a.update(
                question_context="原始记录正文为空，图片待核验。",
                content_units=[{"unit_id": "U001", "paragraph_refs": [], "summary": "正文没有可读段落，无法重建作者主张。", "role": "unresolved"}],
                main_claims=[], argument_steps=[], concept_usage=[], examples_and_targets=[], conditions=[],
                rhetoric_and_tone="无正文，无法判断。",
                unresolved_questions=["图片内容需核验；原始正文为空。"], evidence=[],
            )
            item.update(status="needs_reread", image_checked=False, notes="正文为空；图片内容未经核验。")
            continue
        first = next((x.strip() for x in (art.get("text") or "").splitlines() if x.strip()), "(正文为空)")[:180]
        a.update(
            question_context="提问者问题：%s；本文初读记录作者正文线索。" % (art.get("question") or "未提供"),
            content_units=[{"unit_id": "U001", "paragraph_refs": pids, "summary": "围绕“%s”的原文驱动初步概括，待独立复核。" % spec.get("title", ""), "role": "thesis"}],
            main_claims=[{"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者开篇提出：“%s”" % first, "evidence": ["E001"]}],
            argument_steps=["从开篇命题进入正文。", "其余步骤待独立复核。"], concept_usage=[], examples_and_targets=[], conditions=[],
            rhetoric_and_tone="初读未作完整修辞分类，待复核。",
            unresolved_questions=["论证、事实依据与概念边界需复核。"],
            evidence=[{"key": "E001", "paragraph_id": pids[0], "quote": first, "relation": "supports"}],
        )
        item["notes"] = "原文驱动最低限度初读；尚未完成逐段独立复核。"
        if spec.get("images"):
            item.update(status="needs_reread", image_checked=False)
            item["notes"] += " 含图片节点，图片未经核验。"


def write_jsonl(path, records):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    repairs = []
    with open(path, "w", encoding="utf-8") as fh:
        for r in records:
            info = r.pop("_repair", None)
            if info:
                repairs.append({"article_id": r.get("article_id"), "repairs": info})
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    if repairs:
        sys.stderr.write(
            "[authoring] 机械归一化：%d 篇有修复（属正常，不写入记录）\n" % len(repairs)
        )
        for item in repairs:
            sys.stderr.write("  %s %s\n" % (str(item["article_id"])[:8], json.dumps(item["repairs"], ensure_ascii=False)))
    return path
