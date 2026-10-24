#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extend the established 4,050-article theme map to corpus v2.

Old articles reuse the audited concept map. New articles receive conservative
candidate concepts from first-pass evidence and text cues, then a stratified
sample is emitted for human audit. This is a routing layer, not a claim that
keyword matches are final interpretation.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
OLD_MAP = ROOT / "research/data/article_system_concept_map.csv"
OUT = ROOT / "research-rebuild/reports"
DS = ROOT / "research-rebuild/out"
MANUAL = ROOT / "research-rebuild/data/manual-theme-decisions-v2.csv"

CONCEPTS = [
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
]

# Conservative cues: a concept is assigned only when a cue appears in the
# question, first-pass claim/keyword fields, or body. More than one concept is
# expected; primary is the highest weighted concept, not an exclusive label.
CUES = {
    "照料与家庭": ["家庭", "父母", "子女", "亲属", "兄弟", "亲戚", "婚姻", "夫妻", "孩子"],
    "爱与回应": ["恋爱", "感情", "伴侣", "分手", "暧昧", "网友", "友谊", "约会", "爱", "关心", "尊重", "回应", "帮助", "关系"],
    "能力与学习": ["学习", "教育", "能力", "知识", "读书", "学校", "训练", "经验"],
    "劳动与组织": ["工作", "职场", "同事", "公司", "组织", "管理", "团队", "招聘"],
    "财富与市场": ["钱", "财富", "收入", "借贷", "投资", "消费", "市场", "买", "卖"],
    "法律与秩序": ["法律", "犯罪", "诈骗", "刑罚", "警察", "司法", "违法", "安全"],
    "权力与异议": ["权力", "政府", "政治", "官员", "制度", "阶层", "统治", "异议"],
    "技术与工程": ["技术", "工程", "软件", "互联网", "平台", "算法", "设备"],
    # “模型”在一般论证中极常见（解释模型、历史模型等），不能单独触发 AI。
    # 只有明确的 AI/机器学习/机器人语境才进入该主题。
    "人工智能与机器": ["人工智能", "AI", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶"],
    # Avoid the single-character cue 性: it matches unrelated words such as 属性 and 性能.
    "性别与身体": ["女性", "男性", "性别", "身体", "生育", "性关系", "怀孕", "同意"],
    "心理与主体": ["心理", "情绪", "焦虑", "抑郁", "孤独", "性格", "自我", "精神"],
    "生态与自然": ["自然", "生态", "气候", "环境", "能源", "动物", "植物", "天气"],
    "文明与历史": ["历史", "文明", "社会", "文化", "民族", "国家", "古代", "传统"],
    "事实与证据": ["事实", "证据", "数据", "研究", "统计", "为什么", "原因", "证明"],
    "定义与达意": ["意思", "定义", "概念", "区别", "如何理解", "所谓"],
    "选择与自由": ["选择", "自由", "决定", "要不要", "是否应该", "怎么办"],
    "责任与后果": ["责任", "后果", "风险", "代价", "承担", "应该"],
    "成本与总账": ["成本", "收益", "代价", "投入", "回报", "效率"],
    "信用与信任": ["信任", "信用", "可靠", "欺骗", "诚实", "背叛"],
    "边界与许可": ["边界", "拒绝", "隐私", "许可", "限制", "规则", "安全"],
    "净输出与不掠夺": ["掠夺", "剥削", "伤害", "占用", "公平", "互惠"],
    "宗教与自然法": ["宗教", "信仰", "道德", "正义", "自然法", "神"],
}


def jsonl(path: Path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


def load_old():
    result = {}
    with OLD_MAP.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            result[row["id"]] = row["concepts"].split(";") if row["concepts"] else []
    return result


def load_ds():
    result = {}
    for path in sorted(DS.glob("*.out.jsonl")):
        for rec in jsonl(path):
            result[rec.get("article_id")] = rec
    return result


def load_manual():
    result = {}
    if not MANUAL.exists():
        return result
    with MANUAL.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("id"):
                result[row["id"]] = row
    return result


def _selected_strings(value, key: str = "") -> list[str]:
    """Extract evidence-bearing prose without stringifying whole analysis objects."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(_selected_strings(item, key))
        return out
    if not isinstance(value, dict):
        return []
    allowed = {
        "statement", "summary", "meaning", "evidence", "question_context",
        "working_keywords", "domain_candidates", "issue_candidates",
        "object_candidates", "examples_and_targets", "conditions",
        "argument_steps", "unresolved_questions", "text",
    }
    out: list[str] = []
    for child_key, child in value.items():
        if child_key in allowed:
            out.extend(_selected_strings(child, child_key))
    return out


def text_for(rec: dict) -> str:
    meta = rec.get("metadata") or {}
    analysis = rec.get("analysis") or {}
    provisional = analysis.get("provisional_tags") or {}
    parts = [meta.get("title", "")]
    parts += _selected_strings(analysis)
    parts += _selected_strings(provisional)
    for p in (rec.get("structure") or {}).get("paragraphs") or []:
        parts.append(p.get("text", ""))
    return " ".join(map(str, parts))


def classify(rec: dict) -> tuple[list[str], dict[str, int], dict[str, list[str]]]:
    text = text_for(rec)
    scores = {concept: 0 for concept in CONCEPTS}
    matched: dict[str, list[str]] = {}
    for concept, cues in CUES.items():
        for cue in cues:
            hits = min(len(re.findall(re.escape(cue), text, flags=re.I)), 3)
            if hits:
                scores[concept] += hits
                matched.setdefault(concept, []).append(cue)
    ranked = [c for c, score in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])) if score > 0]
    return ranked[:6], scores, matched


def candidate_status(rec: dict, concepts: list[str], scores: dict[str, int]) -> str:
    if not rec:
        return "missing_first_pass"
    if not concepts:
        return "cue_unmatched"
    top = max(scores.values())
    ties = sum(value == top for value in scores.values())
    return "needs_human_classification" if top <= 1 or ties > 1 else "review_required"


def main():
    old = load_old()
    ds = load_ds()
    manual = load_manual()
    v2 = list(jsonl(V2))
    rows = []
    new_rows = []
    for ordinal, article in enumerate(v2, 1):
        aid = article.get("id")
        if aid in manual:
            decision = manual[aid]
            concepts = [x for x in decision.get("concepts", "").split(";") if x]
            source = "manual_decision"
            confidence = decision.get("audit_status") or "manual_confirmed"
            scores = {}; matched = {}
            if aid not in old:
                new_rows.append((ordinal, article, ds.get(aid, {}), concepts, scores, matched, confidence))
        elif aid in old:
            concepts = old[aid]
            source = "reused_audited_map"
            confidence = "audited"
            scores = {}; matched = {}
        else:
            rec = ds.get(aid, {})
            concepts, scores, matched = classify(rec)
            source = "new_first_pass_candidate"
            confidence = candidate_status(rec, concepts, scores)
            new_rows.append((ordinal, article, rec, concepts, scores, matched, confidence))
        top_score = max(scores.values()) if scores else ""
        tie_count = sum(value == top_score for value in scores.values()) if scores else ""
        rows.append({"ordinal": ordinal, "id": aid, "title": article.get("title", ""), "date": article.get("publishedAt", ""), "concepts": ";".join(concepts), "primary": concepts[0] if concepts else "", "source": source, "confidence": confidence, "audit_status": confidence, "first_pass_status": "covered" if ds.get(aid) else "missing", "top_score": top_score, "tie_count": tie_count, "matched_cues": ";".join(cue for values in matched.values() for cue in values)})

    OUT.mkdir(parents=True, exist_ok=True)
    map_path = OUT / "article-theme-map-v2.csv"
    with map_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    # Stratified sample: every populated new primary concept gets up to 3;
    # additionally include all unassigned and all image-bearing new articles.
    groups = defaultdict(list)
    for item in new_rows:
        ordinal, article, rec, concepts, scores, matched, status = item
        key = concepts[0] if concepts else "UNASSIGNED"
        groups[key].append(item)
    sample = []
    for key, items in sorted(groups.items()):
        sample.extend(sorted(items, key=lambda x: x[0])[:3])
    for item in new_rows:
        if (item[2].get("structure") or {}).get("images") and item not in sample:
            sample.append(item)
    sample_path = OUT / "new-theme-stratified-sample.csv"
    with sample_path.open("w", encoding="utf-8-sig", newline="") as fh:
        fields = ["sample_id", "ordinal", "id", "title", "primary", "concepts", "image_count", "question_context", "audit_status", "first_pass_status", "top_score", "tie_count", "matched_cues"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader()
        for i, (ordinal, article, rec, concepts, scores, matched, status) in enumerate(sample, 1):
            top_score = max(scores.values()) if scores else ""
            tie_count = sum(value == top_score for value in scores.values()) if scores else ""
            audited_statuses = {"manual_provisional", "reviewed_agree", "reviewed_needs_revision"}
            writer.writerow({"sample_id": i, "ordinal": ordinal, "id": article.get("id"), "title": article.get("title", ""), "primary": concepts[0] if concepts else "UNASSIGNED", "concepts": ";".join(concepts), "image_count": len((rec.get("structure") or {}).get("images") or []), "question_context": (rec.get("analysis") or {}).get("question_context", ""), "audit_status": status if status in audited_statuses else "pending", "first_pass_status": "covered" if rec else "missing", "top_score": top_score, "tie_count": tie_count, "matched_cues": ";".join(cue for values in matched.values() for cue in values)})

    counts = Counter(row["primary"] for row in rows)
    status_counts = Counter(item[6] for item in new_rows)
    source_counts = Counter(row["source"] for row in rows)
    manual_old = sum(1 for row in rows if row["source"] == "manual_decision" and row["id"] in old)
    manual_status_counts = Counter(row["audit_status"] for row in rows if row["source"] == "manual_decision")
    deepseek_covered_new = sum(bool(item[2]) for item in new_rows)
    deepseek_missing_new = sum(not bool(item[2]) for item in new_rows)
    manual_decision_records = source_counts["manual_decision"]
    summary = {"v2_records": len(rows), "reused_old_records": source_counts["reused_audited_map"] + manual_old, "manual_decisions_old": manual_old, "new_records": len(new_rows), "deepseek_covered_new": deepseek_covered_new, "deepseek_missing_new": deepseek_missing_new, "missing_first_pass": deepseek_missing_new, "cue_unmatched": status_counts["cue_unmatched"], "needs_human_classification": status_counts["needs_human_classification"], "manual_decision_records": manual_decision_records, "manual_provisional": manual_status_counts["manual_provisional"], "reviewed_agree": manual_status_counts["reviewed_agree"], "reviewed_needs_revision": manual_status_counts["reviewed_needs_revision"], "new_status_counts": dict(status_counts), "manual_status_counts": dict(manual_status_counts), "new_sample_records": len(sample), "theme_counts": dict(counts), "outputs": [str(map_path), str(sample_path)], "method": "旧映射仅复用已有审计记录；新增记录中 DeepSeek 覆盖与缺失分别统计，人工决定按 provisional/agreement/revision 分层；抽样审计完成前不视为最终分类。"}
    (OUT / "v2-theme-classification-progress.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
