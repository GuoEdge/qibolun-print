#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Derive auditable A00-A21 print-topic candidates.

This script is deliberately a routing layer.  It never changes the corpus or
the existing 23-theme map.  Official paths and first-version paper routes are
stronger evidence than cross-domain concepts; conflicts are retained as
needs_human_classification instead of being silently resolved by dictionary
order.  The candidate route status is kept separate from the formal
classification status so that a machine route can never be mistaken for a
completed human classification.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
DEFAULT_REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_DATA = ROOT / "research-rebuild/data"
DEFAULT_OUT = DEFAULT_REPORTS / "print-topic-candidates-v2.csv"

# Used only to choose a stable representative when several first-version
# paper routes are tied.  The tie remains visible in the output and changes
# the status to review_required; this order is not a semantic conclusion.
ROUTE_PRIORITY = [
    "A09", "A10", "A12", "A14", "A21", "A02", "A05", "A06", "A07", "A08",
    "A04", "A11", "A13", "A15", "A16", "A17", "A18", "A19", "A20",
    "A01", "A03", "A00",
]

# Article-level domain signals are a recall layer, not a final judgement.  The
# title/question is treated as the strongest text evidence, followed by the
# first few body paragraphs.  A matched signal always carries review_required
# so a reviewer can distinguish a clear candidate from a confirmed topic.
TEXT_SIGNAL_RULES = [
    # Keep A19's lead signal specific to death-care, burial and remembrance.
    # Bare "去世/死亡" mentions are often examples in medical, legal,
    # employment or biology articles and must not create an A19 primary.
    ("T-A19-01", "A19", r"奠仪|葬礼|丧葬|丧事|殡仪|骨灰|墓地|墓葬|坟墓|祭祀|家祭|祭祖|悼亡|悼念|哀悼|追悼|遗体|尸体|弥留|临终关怀|烧七|烧百天|烧周年|遗愿|纪念逝者", 90),
    ("T-A01-01", "A01", r"死亡焦虑|害怕死亡|恐惧死亡|怕死|面对死亡|预备死亡|死亡恐惧|活着的意义", 96),
    ("T-A12-01", "A12", r"战争|军事|军队|国防|军备|交战|战役|战略|外交|敌我|国际秩序|大国博弈|大国竞争|俄乌|北约|军事同盟|战争动员", 86),
    ("T-A10-01", "A10", r"战争罪|战犯|刑事责任|刑罚|审判|法院|司法|犯罪|违法|判决|警察|死刑|监管执法", 98),
    ("T-A14-01", "A14", r"人工智能|AI|机器学习|大语言模型|生成式AI|机器人|自动驾驶|智能体|OpenAI", 96),
    ("T-A09-01", "A09", r"医疗|医学|疾病|医生|医院|治疗|药物|诊断|病人|病痛|看病|探病|病情|护理|健康|手术", 88),
    ("T-A02-01", "A02", r"女性|男性|性别|生育|怀孕|月经|痛经|性关系|性行为|同意|身体自主|性骚扰", 88),
    ("T-A20-01", "A20", r"历史|文明|古代|先秦|秦汉|唐代|宋代|明代|清代|传统|时代变迁|演变|历史经验|社会史|文化史", 82),
    ("T-A21-01", "A21", r"群众体育|竞技体育|职业体育|体育伦理|运动伦理|体育运动体系|体育生态|体育大国|体育强国|体育产业|体育赛事|体育治理|体育训练|运动员健康|运动员伤病|竞技训练|中国足球|足球发展|群众足球|赛事运营|赛事组织|赛事执行|开幕式运营|训练备战|奥运会运动员", 91),
    ("T-A18-01", "A18", r"生态|环境|气候|污染|自然资源|动物|植物|生灵|物种|进化|猫|狗|自然科学", 84),
    ("T-A17-01", "A17", r"民族|族群|种族|国籍|移民|华人|身份政治|文化归属|同化|殖民", 84),
    ("T-A16-01", "A16", r"媒体|舆论|新闻|宣传|传播|舆情|公众认知|评论区|信息环境|公共关系", 84),
    ("T-A15-01", "A15", r"艺术|审美|绘画|素描|电影|音乐|诗歌|小说|创作|美学|设计|文化生产|演员|表演|戏剧", 84),
    ("T-A13-01", "A13", r"技术|工程|软件|程序|互联网|平台|芯片|制造|基础设施|设备|能源技术|供应链", 80),
    ("T-A08-01", "A08", r"财富|赚钱|收入|投资|消费|市场|生意|经济|借贷|财务|价格|买卖|利润|成本收益", 80),
    ("T-A07-01", "A07", r"职场|公司|同事|团队|组织|管理者|员工|招聘|老板|共事|合作|合同|服务", 80),
    ("T-A05-01", "A05", r"家庭|父母|子女|孩子|兄弟|姐妹|亲属|抚养|养老|代际|家委会|家长|亲戚", 80),
    ("T-A06-01", "A06", r"恋爱|婚姻|配偶|伴侣|分手|朋友|友情|亲密|邻居|同学|约会|交往|情侣", 80),
    ("T-A04-01", "A04", r"教育|学习|学校|大学|老师|学生|训练|读书|考试|课堂|教师|作业|课程|宿舍|毕业", 80),
    ("T-A11-01", "A11", r"宗教|信仰|上帝|神|祈祷|自然法|神学|圣经|道德正义", 86),
]


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def unique(values):
    out = []
    seen = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def text_signal_candidates(article: dict) -> list[dict[str, str]]:
    """Return explicit domain signals from the article's lead, not full-text noise.

    A title/question hit is deliberately stronger than a hit in the opening
    body excerpt.  The output is still a candidate rule and is always marked
    for review; it is never treated as a completed reading decision.
    """
    title_question = " ".join(str(article.get(key) or "") for key in ("title", "question", "brief"))
    # Sports and event-operation cues may emerge after the opening; scan a
    # larger bounded excerpt for this one domain without broad full-text routing.
    body = str(article.get("text") or "")[:6000]
    out: list[dict[str, str]] = []
    for rule_id, code, pattern, priority in TEXT_SIGNAL_RULES:
        if re.search(pattern, title_question, flags=re.I):
            out.append({
                "rule_id": rule_id + "-lead",
                "topic_codes": code,
                "priority": str(priority),
                "review_required": "true",
                "source": "text_signal_lead",
                "matched_pattern": pattern,
            })
        elif re.search(pattern, body, flags=re.I):
            out.append({
                "rule_id": rule_id + "-body",
                "topic_codes": code,
                "priority": str(max(40, priority - 20)),
                "review_required": "true",
                "source": "text_signal_body_head",
                "matched_pattern": pattern,
            })

    # Generic death words are useful only when the same lead explicitly
    # frames a death-care/remembrance situation.  This catches concise
    # questions such as "去世前说什么" without routing "去世后公司赔偿"
    # or "动物为何害怕死亡" to A19.
    death_words = r"去世|死亡|身亡|亡者|死后|死前"
    death_context = r"葬|墓|祭|悼|临终|弥留|遗体|尸体|骨灰|遗言|遗愿|告别|纪念|追思|清明|丧葬|葬礼"
    if re.search(death_words, title_question, flags=re.I) and re.search(death_context, title_question + " " + body, flags=re.I):
        out.append({
            "rule_id": "T-A19-02-contextual-death",
            "topic_codes": "A19",
            "priority": "76",
            "review_required": "true",
            "source": "text_signal_lead",
            "matched_pattern": f"({death_words})+({death_context})",
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v2", type=Path, default=DEFAULT_V2)
    ap.add_argument("--reports", type=Path, default=DEFAULT_REPORTS)
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    registry = {r["code"]: r for r in read_csv(args.data / "print-topic-registry-v2.csv") if r.get("code")}
    rules = read_csv(args.data / "print-topic-crosswalk-v2.csv")
    rule_by_id = {r["rule_id"]: r for r in rules if r.get("rule_id")}
    concept_rules: dict[str, list[dict[str, str]]] = defaultdict(list)
    native_rules: list[dict[str, str]] = []
    route_rules: dict[str, list[dict[str, str]]] = defaultdict(list)
    for rule in rules:
        if rule.get("source_type") == "concept":
            concept_rules[rule.get("source_value", "")].append(rule)
        elif rule.get("source_type") == "native_path_prefix":
            native_rules.append(rule)
        elif rule.get("source_type") == "legacy_paper_route":
            route = rule.get("source_value", "")
            route_rules[route.zfill(3)].append(rule)

    theme_rows = {r.get("id"): r for r in read_csv(args.reports / "article-theme-map-v2.csv") if r.get("id")}
    # This file contains explicit A00-A21 decisions.  The similarly named
    # manual-theme-decisions-v2.csv is an older 23-concept review layer and
    # must not be used as a print-topic decision source.
    manual_rows = {r.get("id"): r for r in read_csv(args.data / "print-topic-manual-decisions-v2.csv") if r.get("id")}
    native_rows = {r.get("article_id"): r for r in read_csv(args.reports / "native-article-category-summary.csv") if r.get("article_id")}
    edges: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_csv(args.reports / "native-article-category-edges.csv"):
        if row.get("article_id"):
            edges[row["article_id"]].append(row)
    routes = {r.get("id"): r for r in read_csv(args.data.parent / "data" / "article_paper_route_map.csv") if r.get("id")}
    # The caller normally points --data at research-rebuild/data; the first
    # version route map lives in the top-level research/data directory.
    route_path = ROOT / "research/data/article_paper_route_map.csv"
    routes = {r.get("id"): r for r in read_csv(route_path) if r.get("id")}
    image_rows = read_csv(args.data / "image-inventory.csv")
    image_counts: dict[str, int] = defaultdict(int)
    image_statuses: dict[str, list[str]] = defaultdict(list)
    for image in image_rows:
        aid = image.get("id", "")
        if aid:
            image_counts[aid] += 1
            image_statuses[aid].append(image.get("status", ""))

    rows = []
    for ordinal, article in enumerate(read_jsonl(args.v2), 1):
        aid = article.get("id", "")
        theme = theme_rows.get(aid, {})
        manual = manual_rows.get(aid, {})
        native = native_rows.get(aid, {})
        candidates: dict[str, dict] = defaultdict(lambda: {"score": 0, "level": 0, "rules": [], "sources": [], "review": False})
        secondary_native_rules: list[str] = []
        secondary_native_evidence: list[str] = []
        secondary_native_codes: list[str] = []

        def add(rule: dict[str, str], source: str):
            for code in (rule.get("topic_codes", "").split(";")):
                if code not in registry:
                    continue
                item = candidates[code]
                # A second route or concept supporting the same code should
                # not overpower a different specialist route merely by count.
                item["score"] = max(item["score"], int(rule.get("priority") or 0))
                native_level = 2 if source == "native_path_prefix" and rule.get("review_required", "").lower() == "true" else None
                item["level"] = max(item["level"], native_level if native_level is not None else {
                    "native_path_prefix": 3,
                    # A direct lead signal is comparable to a specific
                    # official path and outranks a reused legacy route; the
                    # body-head signal remains a weaker recall hint.
                    "text_signal_lead": 3,
                    "legacy_paper_route": 2,
                    "text_signal_body_head": 1,
                    "concept": 1,
                }.get(source, 0))
                item["rules"].append(rule.get("rule_id", ""))
                item["sources"].append(source)
                item["review"] = item["review"] or rule.get("review_required", "").lower() == "true"

        # Preserve each exact official path as evidence. Prefix matching is
        # explicit in the rule table and never replaces the official edge.
        native_paths = unique(e.get("native_parent_path_names", "") for e in edges.get(aid, []))
        for path in native_paths:
            for rule in native_rules:
                # Broad official paths can remain in the native evidence
                # layer without deciding the mutually exclusive print spine.
                # In particular, generic body/desire/service paths must be
                # confirmed by article text or an audited paper route before
                # they can become A02/A09 primaries.
                if rule.get("decision_role") != "primary_candidate":
                    rule_id = rule.get("rule_id", "")
                    if rule_id:
                        secondary_native_rules.append(rule_id)
                    for code in unique((rule.get("topic_codes", "") or "").split(";")):
                        if code in registry:
                            secondary_native_codes.append(code)
                            secondary_native_evidence.append(f"{code}:native_path_prefix_secondary:{rule_id}")
                    continue
                if path == rule.get("source_value") or path.startswith(rule.get("source_value", "") + " / "):
                    add(rule, "native_path_prefix")

        route_values = (routes.get(aid, {}).get("paperRoutes") or "").split(";")
        for route in unique(x.zfill(3) for x in route_values):
            for rule in route_rules.get(route, []):
                add(rule, "legacy_paper_route")

        concepts = unique((theme.get("concepts") or "").split(";"))
        for concept in concepts:
            for rule in concept_rules.get(concept, []):
                add(rule, "concept")

        # Explicit article-domain signals are independent from the legacy
        # concept map.  They improve recall for topics that the official tree
        # does not expose (notably death/ritual and war/diplomacy), while the
        # review flag prevents them from being mistaken for human decisions.
        text_signal_rules = text_signal_candidates(article)
        for rule in text_signal_rules:
            add(rule, rule.get("source", "text_signal"))

        # Keep a deterministic candidate list for review, but never hide ties.
        route_rank = {code: index for index, code in enumerate(ROUTE_PRIORITY)}
        ranked = sorted(candidates.items(), key=lambda pair: (-pair[1]["level"], -pair[1]["score"], route_rank.get(pair[0], len(route_rank)), pair[0]))
        top_key = (ranked[0][1]["level"], ranked[0][1]["score"]) if ranked else (0, 0)
        max_score = top_key[1]
        raw_top = [code for code, item in ranked if (item["level"], item["score"]) == top_key]
        # Keep the raw tie count for audit, but select a reproducible route for
        # the one-row print index.  Any raw tie remains review_required.
        top = sorted(raw_top, key=lambda code: route_rank.get(code, len(route_rank)) )
        # Review flags on low-ranking secondary candidates must not hold back
        # an otherwise clear primary route.  Only the top candidate's evidence
        # participates in the primary gate; all lower candidates remain in the
        # audit columns for later cross-reading.
        top_items = [candidates[code] for code in top]
        has_strong = any(source in {"native_path_prefix", "legacy_paper_route", "text_signal_lead", "text_signal_body_head"} for item in top_items for source in item["sources"])
        has_weak_only = bool(ranked) and not has_strong
        review_flag = any(item["review"] for item in top_items)
        source = theme.get("source", "")
        theme_audit = theme.get("audit_status", "")
        route_sources = set(source for item in candidates.values() for source in item["sources"])
        strong_route_sources = route_sources & {"native_path_prefix", "legacy_paper_route"}
        if not ranked:
            candidate_route_status = "no_primary_candidate"
        elif len(raw_top) > 1:
            candidate_route_status = "conflict_or_tie"
        elif has_weak_only:
            candidate_route_status = "concept_only_candidate"
        elif strong_route_sources == {"native_path_prefix"}:
            candidate_route_status = "native_candidate"
        elif strong_route_sources == {"legacy_paper_route"}:
            candidate_route_status = "legacy_candidate"
        elif strong_route_sources:
            candidate_route_status = "mixed_candidate"
        elif any(source.startswith("text_signal") for item in candidates.values() for source in item["sources"]):
            candidate_route_status = "text_signal_candidate"
        else:
            candidate_route_status = "concept_only_candidate"

        # Formal classification status is intentionally conservative.  The
        # source map's old audited rows may be reused only when the new route
        # is a single, non-broad candidate.  New first-pass rows remain in a
        # review queue even when a strong route exists.  Manual decisions are
        # mapped to the framework's six allowed states without conflating
        # "reviewed_needs_revision" and "manual_provisional".
        body_present = bool((article.get("text") or "").strip())
        lexical_present = bool((article.get("lexical") or "").strip())
        image_count = image_counts.get(aid, 0)
        image_review_required = bool(image_count and any(
            (status or "").lower() not in {"reviewed", "confirmed", "complete"}
            for status in image_statuses.get(aid, [])
        ))
        material_uncertain = not body_present and (not lexical_present or image_review_required)
        manual_status = manual.get("classification_status", "") or manual.get("audit_status", "") or (theme_audit if source == "manual_decision" else "")
        explicit_manual_topic = unique([
            manual.get("primary_print_topic", ""),
            manual.get("primary_print_topic_code", ""),
            manual.get("a_topic", ""),
        ])
        explicit_manual_topic = [code for code in explicit_manual_topic if code in registry]
        # Only a row with an explicit A00-A21 code can produce
        # manual_confirmed/manual_provisional.
        manual_code = explicit_manual_topic[0] if explicit_manual_topic else ""
        if manual_code and manual_status in {"manual_confirmed", "reviewed_agree"}:
            status = "manual_confirmed"
        elif manual_code and manual_status == "manual_provisional":
            status = "manual_provisional"
        elif manual_status in {"reviewed_agree", "reviewed_needs_revision"}:
            status = "review_required"
        elif material_uncertain:
            status = "uncertain"
        elif not ranked or has_weak_only or len(raw_top) > 1:
            status = "needs_human_classification"
        elif review_flag:
            status = "review_required"
        elif source == "new_first_pass_candidate":
            status = "review_required"
        elif source == "reused_audited_map" and theme_audit == "audited":
            status = "audited"
        else:
            status = "needs_human_classification"

        primary = manual_code or (top[0] if top else "A00")
        if not manual_code and has_weak_only and source != "manual_decision":
            primary = "A00"
        if not primary:
            primary = "A00"
        manual_secondary = [
            code for code in unique((manual.get("secondary_print_topic_codes", "") or "").split(";"))
            if code in registry and code != primary
        ]
        secondary = manual_secondary + [code for code, _ in ranked if code != primary and code not in manual_secondary]
        secondary = secondary[:3]
        matched_rules = unique(candidates[primary]["rules"] if primary in candidates else [])
        # Keep the complete candidate evidence, not only the selected route.
        # The audit queue needs to explain why an alternative A-topic appeared
        # before a reviewer can accept, reassign, or remove it.
        candidate_rule_ids = unique(
            rule_id
            for code, _ in ranked
            for rule_id in candidates[code]["rules"]
            if rule_id
        )
        candidate_rule_ids = unique(candidate_rule_ids + secondary_native_rules)
        candidate_evidence = unique(
            f"{code}:{','.join(unique(candidates[code]['sources']))}"
            for code, _ in ranked
            if unique(candidates[code]["sources"])
        )
        candidate_evidence = unique(candidate_evidence + secondary_native_evidence)
        candidate_trace = ";".join(
            f"{code}:{candidates[code]['score']}" for code, _ in ranked
        )
        if manual_code:
            matched_rules = unique([f"MANUAL:{manual_code}", *matched_rules])
        row = {
            "source_ordinal": ordinal,
            "id": aid,
            "title": article.get("title", ""),
            "primary_print_topic": primary,
            "primary_print_topic_name": registry.get(primary, {}).get("name", "跨域行动语法与待审"),
            "secondary_print_topics": ";".join(secondary),
            "topic_candidate_codes": ";".join(code for code, _ in ranked),
            "primary_topic_rule_ids": ";".join(matched_rules),
            "candidate_topic_rule_ids": ";".join(candidate_rule_ids),
            "candidate_topic_evidence": ";".join(candidate_evidence),
            "secondary_native_topic_codes": ";".join(unique(secondary_native_codes)),
            "secondary_native_rule_ids": ";".join(unique(secondary_native_rules)),
            "secondary_native_evidence": ";".join(unique(secondary_native_evidence)),
            "topic_candidate_score_trace": candidate_trace,
            "topic_candidate_score": candidates.get(primary, {}).get("score", 0),
            "topic_candidate_source_level": candidates.get(primary, {}).get("level", 0),
            "topic_candidate_tie_count": len(raw_top),
            "primary_topic_sources": ";".join(unique(candidates.get(primary, {}).get("sources", []))),
            "candidate_route_status": "manual_decision" if manual_code else candidate_route_status,
            "primary_topic_status": status,
            "classification_status": status,
            "manual_theme_review_status": manual_status,
            "manual_a_topic": ";".join(explicit_manual_topic),
            "manual_decision_basis": manual.get("decision_basis", "") or manual.get("basis", ""),
            "primary_topic_review_required": "true" if status in {"review_required", "needs_human_classification", "manual_provisional", "uncertain"} else "false",
            "image_count": image_count,
            "image_review_required": "true" if image_review_required else "false",
            "source_material_status": "text_present" if body_present else ("lexical_or_image_only" if lexical_present else "text_missing"),
            "legacy_theme_primary": theme.get("primary", ""),
            "legacy_theme_all": theme.get("concepts", ""),
            "legacy_theme_audit_status": theme.get("audit_status", ""),
            "official_assignment_status": native.get("native_assignment_status", "unassigned"),
            "official_category_paths": ";".join(native_paths),
            "official_root_names": native.get("native_root_names", ""),
            "source_note": "候选路由层；candidate_route_status 不是定稿状态。classification_status 仅使用框架正式枚举，主专题仍需按 rule_id 与正文审计。",
        }
        rows.append(row)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "records": len(rows),
        "unique_ids": len({r["id"] for r in rows}),
        "primary_topic_counts": {code: sum(r["primary_print_topic"] == code for r in rows) for code in registry},
        "status_counts": {status: sum(r["classification_status"] == status for r in rows) for status in sorted({r["classification_status"] for r in rows})},
        "candidate_route_status_counts": {status: sum(r["candidate_route_status"] == status for r in rows) for status in sorted({r["candidate_route_status"] for r in rows})},
        "image_review_required": sum(r["image_review_required"] == "true" for r in rows),
        "source_material_status_counts": {status: sum(r["source_material_status"] == status for r in rows) for status in sorted({r["source_material_status"] for r in rows})},
        "official_unassigned": sum(r["official_assignment_status"] != "confirmed" for r in rows),
        "output": str(args.out),
        "method": "official path and legacy paper route outrank concepts; candidate_route_status is separate from framework classification_status; ties and weak-only concepts remain needs_human_classification",
    }
    summary_path = args.out.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
