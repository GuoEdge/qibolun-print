#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the four-layer classification index for the v2 corpus.

The source corpus, native outline edges, DeepSeek first-pass output and the
legacy 23-concept map are read-only inputs.  This script creates a separate
printing spine (one primary A-topic plus up to three secondary A-topics) and
keeps the native paths and 23-concept route layer beside it.

The printing spine is deliberately evidence-ranked rather than a rename of
``article-theme-map-v2.csv``: manual decisions outrank native paths with text
support, which outrank legacy paper routes, which outrank concept-only cues.
Unresolved new articles retain a candidate primary and an explicit review
status so coverage is complete without disguising provisional work as final.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
OUT = REPORTS / "article-classification-v2.csv"
OUT_JSONL = REPORTS / "article-classification-v2.jsonl"
SUMMARY = REPORTS / "article-classification-v2-summary.json"
SUMMARY_MD = REPORTS / "article-classification-v2-summary.md"
TOPIC_DIR = REPORTS / "by-print-topic"

REGISTRY = DATA / "print-topic-registry-v2.csv"
THEME_MAP = REPORTS / "article-theme-map-v2.csv"
LEGACY_ROUTES = ROOT / "research/data/article_paper_route_map.csv"
NATIVE_SUMMARY = REPORTS / "native-article-category-summary.csv"
NATIVE_EDGES = REPORTS / "native-article-category-edges.csv"
NATIVE_COVERAGE = REPORTS / "native-category-coverage.json"
CANDIDATES = REPORTS / "print-topic-candidates-v2.csv"
MANUAL = DATA / "manual-theme-decisions-v2.csv"
PRINT_MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
PRINT_MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DS_DIR = ROOT / "research-rebuild/out"
REVIEWS = REPORTS / "independent-reviews.jsonl"

TOPIC_NAMES = {
    "A01": "心理主体与情绪劳动",
    "A02": "性别身体与同意",
    "A03": "认识论事实与论证",
    "A04": "教育学习与能力形成",
    "A05": "家庭亲属与代际秩序",
    "A06": "亲密关系友人与婚恋",
    "A07": "职场组织与合作",
    "A08": "财富劳动与市场",
    "A09": "医疗疾病与照料",
    "A10": "国家法律犯罪与司法",
    "A11": "宗教自然法与世俗论证",
    "A12": "战争军事外交与大国秩序",
    "A13": "技术工程与产业路径",
    "A14": "人工智能机器与未来秩序",
    "A15": "艺术审美与文化生产",
    "A16": "媒体舆论与公共认知",
    "A17": "民族族群与身份秩序",
    "A18": "生态能源与自然科学",
    "A19": "死亡祭祀与纪念",
    "A20": "历史文明与历时演变",
    "A21": "体育、运动与竞技伦理",
    "A00": "跨域行动语法与待审",
}
TOPIC_ORDER = [f"A{i:02d}" for i in range(1, 22)] + ["A00"]

# Direct topic cues.  Each tuple is (pattern, weight).  Broad method words
# have low weight; domain-specific phrases have higher weight.  The cue layer
# is only one input and never overwrites an explicit manual decision.
CUES: dict[str, list[tuple[str, int]]] = {
    "A14": [(r"人工智能|AI|机器学习|大语言模型|生成式|机器人|自动驾驶|OpenAI|智能体", 7),
            (r"算法|自动化|模型", 2)],
    "A12": [(r"战争|军事|军队|国防|军备|交战|战役|战略|外交|敌我|国际秩序|大国|俄乌|北约", 6),
            (r"军屯|军需|军食", 3)],
    "A10": [(r"战争罪|战犯|刑事责任|审判|法律|犯罪|刑罚|司法|警察|法院|违法|判决|刑事|航空安全|安检|监管|执法|政策", 7),
            (r"秩序|权利|有权|责任", 1)],
    "A09": [(r"医疗|医学|疾病|医生|医院|治疗|药物|诊断|病人|生病|病痛|看病|探病|病情|护理|痛经|症状|健康", 7)],
    "A02": [(r"女性|男性|性别|生育|怀孕|月经|痛经|性关系|性行为|同意|身体自主|性骚扰", 7),
            (r"身体|欲望", 2)],
    "A05": [(r"家庭|父母|子女|孩子|兄弟|姐妹|亲属|抚养|养老|代际|家委会|家长", 6),
            (r"亲戚|祖先", 4)],
    "A06": [(r"恋爱|婚姻|配偶|伴侣|分手|朋友|友情|亲密|邻居|同学|约会|冒犯|交往|情侣", 6),
            (r"陌生人|回应|爱", 2)],
    "A07": [(r"职场|公司|同事|团队|组织|管理者|员工|招聘|老板|共事|合作|合同|服务", 6),
            (r"工作|劳动|管理", 2)],
    "A08": [(r"财富|赚钱|收入|投资|消费|市场|生意|经济|借贷|财务|价格|买卖|利润", 6),
            (r"成本|收益|回报|效率", 2)],
    "A04": [(r"教育|学习|学校|大学|老师|学生|训练|读书|考试|课堂|教师|能力形成|作业|课程|宿舍|毕业|专业", 6),
            (r"能力|成长|经验", 2)],
    "A11": [(r"宗教|信仰|上帝|神|祈祷|自然法|神学|圣经|道德正义", 7),
            (r"原则|正义", 2)],
    "A13": [(r"技术|工程|软件|程序|互联网|平台|芯片|制造|基础设施|设备|充电宝|5G|能源技术", 6),
            (r"技术路线|产业|供应链", 5)],
    "A15": [(r"艺术|审美|绘画|素描|电影|音乐|小说|创作|美学|设计|文化生产|演员|表演|戏剧", 7),
            (r"作品|风格", 2)],
    "A16": [(r"媒体|舆论|新闻|宣传|传播|舆情|公众认知|评论区|差评|信息环境", 7),
            (r"名誉|形象", 2)],
    "A17": [(r"民族|族群|种族|国籍|移民|华人|身份政治|文化归属|同化|殖民", 7),
            (r"身份", 3)],
    "A18": [(r"生态|环境|气候|污染|自然资源|动物|植物|生灵|物种|进化|猫|狗", 6),
            (r"自然|能源|天气", 2)],
    "A19": [(r"死亡|去世|葬|祭祀|悼|遗体|祖先|纪念|哀悼|遗愿", 7)],
    "A20": [(r"历史|文明|古代|传统|时代变迁|演变|历史经验|社会史|文化史", 6),
            (r"传承", 2)],
    "A21": [(r"群众体育|竞技体育|职业体育|体育伦理|运动伦理|体育生态|体育赛事|体育治理|体育运动体系|体育大国|体育强国|体育产业|运动员健康|运动员伤病|竞技训练|中国足球|足球发展|群众足球|赛事运营|赛事组织|赛事执行|开幕式运营|训练备战", 8),
            (r"运动员|奥运会|奥运|足球|篮球|排球|网球|羽毛球|乒乓球|射击|射箭|马拉松|体操|游泳|格斗赛事|拳击比赛", 4)],
    "A01": [(r"心理|情绪|焦虑|抑郁|孤独|自我|性格|恐惧|人格|主体|精神", 6),
            (r"心态|内心|修复", 3)],
    "A03": [(r"事实|证据|定义|概念|逻辑|证明|知识|论证|误解|真假|如何理解", 3),
            (r"为什么|原因|解释|区别", 1)],
}

CONCEPT_TOPIC = {
    "心理与主体": ["A01"], "性别与身体": ["A02"], "事实与证据": ["A03"],
    "定义与达意": ["A03"], "能力与学习": ["A04"], "照料与家庭": ["A05", "A09"],
    "爱与回应": ["A06"], "信用与信任": ["A06", "A07", "A08"],
    "边界与许可": ["A06", "A07", "A10"], "净输出与不掠夺": ["A06", "A07", "A08"],
    "劳动与组织": ["A07"], "财富与市场": ["A08"], "成本与总账": ["A08", "A13"],
    "法律与秩序": ["A10"], "权力与异议": ["A10", "A12"],
    "技术与工程": ["A13"], "文明与历史": ["A20"], "民族与身份": ["A17"],
    "生态与自然": ["A18"], "人工智能与机器": ["A14"], "宗教与自然法": ["A11"],
    "责任与后果": ["A00", "A05", "A07", "A10"], "选择与自由": ["A00", "A06", "A07", "A10"],
}

ROUTE_TOPIC = {
    "04": ["A05"], "05": ["A06"], "06": ["A07"], "08": ["A04"], "09": ["A03"],
    "10": ["A08"], "11": ["A11"], "12": ["A10"], "13": ["A13", "A20"],
    "14": ["A01"], "15": ["A20"], "16": ["A02"], "17": ["A03", "A20"],
    "18": ["A00"], "19": ["A00"], "20": ["A03"], "21": ["A03"], "22": ["A03"],
    "23": ["A20"], "24": ["A00"], "25": ["A09"], "26": ["A10"], "27": ["A12"],
    "28": ["A15"], "29": ["A16"], "30": ["A19"], "31": ["A17"], "32": ["A18"],
    "33": ["A14"],
}


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                out.append(json.loads(line))
    return out


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def unique(values: list[str]) -> list[str]:
    result = []
    seen = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            result.append(value)
            seen.add(value)
    return result


def join(values: list[str]) -> str:
    return ";".join(unique(values))


def date_cst(raw: object) -> str:
    try:
        return datetime.fromtimestamp(int(raw) / 1000, tz=timezone(timedelta(hours=8))).date().isoformat()
    except (TypeError, ValueError, OSError, OverflowError):
        return ""


def first_pass_map() -> dict[str, dict]:
    result = {}
    for path in sorted(DS_DIR.glob("*.out.jsonl")):
        for row in read_jsonl(path):
            if row.get("article_id"):
                result[row["article_id"]] = row
    return result


def review_map() -> dict[str, dict]:
    result = {}
    for row in read_jsonl(REVIEWS):
        if row.get("article_id"):
            result[row["article_id"]] = row
    return result


def print_manual_map() -> dict[str, dict]:
    """Load article-level A-topic decisions separately from the 23-theme map."""
    result = {}
    for row in read_csv(PRINT_MANUAL):
        if row.get("id"):
            result[row["id"]] = row
    return result


def candidate_map() -> dict[str, dict]:
    """Load the conservative candidate layer as the current A-topic spine."""
    return {row.get("id"): row for row in read_csv(CANDIDATES) if row.get("id")}


def evidence_text(article: dict, ds: dict) -> str:
    analysis = ds.get("analysis") or {}
    provisional = ds.get("provisional_tags") or analysis.get("provisional_tags") or {}
    bits = [article.get("title", ""), article.get("question", ""), article.get("text", "")]
    for key in ("question_context", "summary", "meaning", "evidence", "working_keywords", "domain_candidates", "issue_candidates", "object_candidates", "argument_steps", "conditions"):
        value = analysis.get(key, provisional.get(key, ""))
        if isinstance(value, (list, dict)):
            value = json.dumps(value, ensure_ascii=False)
        bits.append(str(value or ""))
    return " ".join(bits)


def load_native_edges() -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = defaultdict(list)
    for row in read_csv(NATIVE_EDGES):
        if row.get("article_id"):
            result[row["article_id"]].append(row)
    return result


def topic_candidates(text: str) -> tuple[Counter, dict[str, list[str]]]:
    scores: Counter = Counter()
    evidence: dict[str, list[str]] = defaultdict(list)
    for code, patterns in CUES.items():
        for pattern, weight in patterns:
            if re.search(pattern, text, flags=re.I):
                scores[code] += weight
                evidence[code].append(pattern)
    return scores, evidence


def native_candidates(paths: list[str]) -> tuple[Counter, list[str]]:
    scores: Counter = Counter()
    rules: list[str] = []
    # Longest path first prevents a broad root rule from hiding a specific one.
    for path in paths:
        for rule_id, prefix, codes, priority, needs_review in NATIVE_RULES:
            if path == prefix or path.startswith(prefix + " /"):
                for code in codes:
                    scores[code] += max(1, priority // 10)
                rules.append(rule_id)
    return scores, unique(rules)


def choose_primary(scores: Counter) -> tuple[str, int, int]:
    if not scores:
        return "A00", 0, 0
    ordered = sorted(scores.items(), key=lambda item: (-item[1], TOPIC_ORDER.index(item[0]) if item[0] in TOPIC_ORDER else 999))
    top = ordered[0][1]
    ties = sum(value == top for _, value in ordered)
    return ordered[0][0], top, ties


def main() -> int:
    global NATIVE_RULES
    registry = read_csv(REGISTRY)
    registry_codes = {row.get("code", "") for row in registry}
    NATIVE_RULES = []
    for row in read_csv(DATA / "print-topic-crosswalk-v2.csv"):
        if row.get("source_type") != "native_path_prefix":
            continue
        codes = [code for code in row.get("topic_codes", "").split(";") if code in registry_codes]
        if not codes:
            continue
        try:
            priority = int(row.get("priority") or 0)
        except ValueError:
            priority = 0
        NATIVE_RULES.append((row.get("rule_id", ""), row.get("source_value", ""), codes, priority, row.get("review_required") == "true"))
    NATIVE_RULES.sort(key=lambda item: (-len(item[1]), -item[3], item[0]))

    articles = read_jsonl(V2)
    by_id = {row.get("id"): row for row in articles}
    themes = {row.get("id"): row for row in read_csv(THEME_MAP)}
    routes = {row.get("id"): row for row in read_csv(LEGACY_ROUTES)}
    manual = {row.get("id"): row for row in read_csv(MANUAL) if row.get("id")}
    print_manual = print_manual_map()
    candidates = candidate_map()
    native_edges = load_native_edges()
    native_summary = {row.get("article_id"): row for row in read_csv(NATIVE_SUMMARY)}
    ds = first_pass_map()
    reviews = review_map()
    rows = []

    for ordinal, article in enumerate(articles, 1):
        aid = article.get("id", "")
        theme = themes.get(aid, {})
        route = routes.get(aid, {})
        manual_row = manual.get(aid, {})
        print_manual_row = print_manual.get(aid, {})
        first = ds.get(aid, {})
        edges = native_edges.get(aid, [])
        paths = unique([edge.get("native_parent_path_names", "") for edge in edges if edge.get("native_parent_path_names")])
        native_score, native_rule_ids = native_candidates(paths)
        cue_scores, cue_evidence = topic_candidates(evidence_text(article, first))
        route_score: Counter = Counter()
        for route_id in (route.get("paperRoutes", "") or "").split(";"):
            for code in ROUTE_TOPIC.get(route_id, []):
                # A13 is a mixed technology/history route; defer to text when
                # both candidates are present.
                route_score[code] += 2 if route_id != "13" else 1
        concept_score: Counter = Counter()
        concepts = [x for x in (theme.get("concepts", "") or "").split(";") if x]
        for concept in concepts:
            for code in CONCEPT_TOPIC.get(concept, []):
                concept_score[code] += 1

        # Evidence hierarchy: explicit A-topic decision, domain cues, native
        # path, legacy audited route, then 23-concept route. Official paths
        # remain a separate axis; broad nodes must not erase strong body cues.
        scores: Counter = Counter()
        for code, value in cue_scores.items():
            scores[code] += value
        for code, value in concept_score.items():
            scores[code] += value
        for code, value in route_score.items():
            scores[code] += value
        for code, value in native_score.items():
            scores[code] += value

        manual_concepts = [x for x in (manual_row.get("concepts", "") or "").split(";") if x]
        manual_candidates: Counter = Counter()
        for concept in manual_concepts:
            for code in CONCEPT_TOPIC.get(concept, []):
                manual_candidates[code] += 1
        for code, value in manual_candidates.items():
            scores[code] += 12 + value

        # Make an explicit, high-specificity cue decisive when it conflicts
        # with a generic old route.  This is particularly important for AI,
        # medicine, war, death and gender articles.
        for code in ("A14", "A12", "A09", "A19", "A02", "A15", "A21"):
            if cue_scores.get(code, 0) >= 7:
                scores[code] += 8

        explicit_primary = (print_manual_row.get("primary_print_topic_code") or "").strip()
        explicit_secondary = [x for x in (print_manual_row.get("secondary_print_topic_codes") or "").split(";") if x]
        if explicit_primary in TOPIC_ORDER:
            primary = explicit_primary
            top_score = scores.get(primary, 0)
            tie_count = 1
        else:
            primary, top_score, tie_count = choose_primary(scores)
        # A00 is reserved for genuinely unsupported/cross-domain cases.  If a
        # method cue is the only weak signal, leave the candidate visible but
        # mark it for review instead of presenting it as settled.
        if top_score < 4 and not explicit_primary:
            primary = "A00"

        # Secondary topics are evidence-backed alternatives, capped at three.
        if explicit_primary in TOPIC_ORDER:
            secondary = [x for x in explicit_secondary if x in TOPIC_ORDER and x != primary][:3]
        else:
            secondary = []
            for code, value in sorted(scores.items(), key=lambda item: (-item[1], TOPIC_ORDER.index(item[0]) if item[0] in TOPIC_ORDER else 999)):
                if code == primary or code == "A00":
                    continue
                if value >= max(3, int(top_score * 0.45)):
                    secondary.append(code)
                if len(secondary) == 3:
                    break

        old = ordinal <= 4050
        original_status = theme.get("audit_status", "")
        if explicit_primary in TOPIC_ORDER:
            classification_status = print_manual_row.get("classification_status") or "manual_provisional"
        elif manual_row:
            if original_status == "reviewed_agree":
                classification_status = "manual_confirmed"
            elif original_status == "manual_provisional":
                classification_status = "manual_provisional"
            else:
                classification_status = "review_required"
        elif old:
            classification_status = "audited" if primary != "A00" else "uncertain"
        elif not first:
            classification_status = "manual_provisional" if top_score >= 4 else "needs_human_classification"
        else:
            classification_status = original_status if original_status in {"review_required", "needs_human_classification"} else "review_required"

        # The candidate layer is the current conservative routing authority.
        # Keep the legacy score result below as an explicit comparison field,
        # but never let full-text cue accumulation overwrite the candidate's
        # primary topic.  Manual A-topic decisions are already incorporated
        # by derive_print_topics_v2.py and therefore remain highest priority.
        legacy_primary = primary
        legacy_secondary = list(secondary)
        legacy_status = classification_status
        candidate_row = candidates.get(aid, {})
        candidate_primary = (candidate_row.get("primary_print_topic") or "").strip()
        # An explicit manual decision is the authoritative print decision.
        # The candidate layer remains useful for undecided rows, but it must
        # never replace either the manually selected primary or its explicit
        # secondary topics.
        if candidate_primary in TOPIC_ORDER and not explicit_primary:
            primary = candidate_primary
            secondary = [x for x in (candidate_row.get("secondary_print_topics") or "").split(";") if x in TOPIC_ORDER and x != primary][:3]
            classification_status = candidate_row.get("classification_status") or candidate_row.get("primary_topic_status") or "review_required"
            basis = ["print_topic_candidate_layer"]
            if candidate_row.get("candidate_route_status"):
                basis.append(f"candidate_route:{candidate_row['candidate_route_status']}")
            if candidate_row.get("primary_topic_sources"):
                basis.append(f"candidate_sources:{candidate_row['primary_topic_sources']}")
            note_bits = [
                f"candidate_layer_primary={primary}",
                f"candidate_status={classification_status}",
                f"legacy_derived_primary={legacy_primary}",
            ]
            if candidate_row.get("topic_candidate_score_trace"):
                note_bits.append(f"candidate_scores={candidate_row['topic_candidate_score_trace']}")
            if candidate_row.get("candidate_topic_rule_ids"):
                note_bits.append(f"candidate_rules={candidate_row['candidate_topic_rule_ids']}")

        basis = []
        if explicit_primary in TOPIC_ORDER:
            basis.append("print_topic_manual_decision")
        if manual_row:
            basis.append("manual_decision")
        if native_rule_ids:
            basis.append("official_native_path")
        if cue_evidence:
            basis.append("question_body_first_pass_cues")
        if route_score:
            basis.append("legacy_paper_route")
        if concept_score:
            basis.append("23_concept_route")
        note_bits = [f"candidate_scores={';'.join(f'{k}:{v}' for k, v in sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:6])}"]
        if explicit_primary in TOPIC_ORDER:
            note_bits.append(f"manual_primary={explicit_primary}")
        if tie_count > 1:
            note_bits.append(f"top_tie={tie_count}")
        if primary == "A00":
            note_bits.append("no domain score reached threshold; retain A00 until human decision")
        if native_rule_ids:
            note_bits.append(f"native_rules={','.join(native_rule_ids)}")
        review = reviews.get(aid, {})
        reading = first.get("reading") or {}
        structure = first.get("structure") or {}
        native = native_summary.get(aid, {})
        row = {
            "ordinal": ordinal,
            "id": aid,
            "title": article.get("title", ""),
            "published_at": article.get("publishedAt", ""),
            "published_date": date_cst(article.get("publishedAt")),
            "url": article.get("url", ""),
            "primary_print_topic_code": primary,
            "primary_print_topic": TOPIC_NAMES.get(primary, primary),
            "secondary_print_topic_codes": ";".join(secondary),
            "secondary_print_topics": ";".join(TOPIC_NAMES.get(code, code) for code in secondary),
            "classification_rule": ";".join(basis),
            "classification_status": classification_status,
            "classification_note": " | ".join(note_bits),
            "candidate_primary_print_topic": candidate_row.get("primary_print_topic", ""),
            "candidate_secondary_print_topics": candidate_row.get("secondary_print_topics", ""),
            # Preserve the candidate layer's numeric routing evidence for the
            # formal index and live review queue.  Without these fields the
            # downstream index silently falls back to zero for every article.
            "primary_topic_candidate_score": candidate_row.get("topic_candidate_score", scores.get(primary, 0)),
            "primary_topic_tie_count": candidate_row.get("topic_candidate_tie_count", tie_count),
            "candidate_classification_status": candidate_row.get("classification_status", ""),
            "candidate_route_status": candidate_row.get("candidate_route_status", ""),
            "candidate_topic_codes": candidate_row.get("topic_candidate_codes", ""),
            "candidate_topic_rule_ids": candidate_row.get("candidate_topic_rule_ids", ""),
            "candidate_topic_evidence": candidate_row.get("candidate_topic_evidence", ""),
            "legacy_derived_primary_print_topic": legacy_primary,
            "legacy_derived_secondary_print_topics": ";".join(legacy_secondary),
            "legacy_derived_classification_status": legacy_status,
            "legacy_theme_primary": theme.get("primary", ""),
            "concept_tags": theme.get("concepts", ""),
            "concept_primary": theme.get("primary", ""),
            "theme_audit_status": original_status,
            "native_root_names": native.get("native_root_names", ""),
            "native_object_paths": ";".join(paths),
            "native_category_names": native.get("native_category_names", ""),
            "native_assignment_status": native.get("native_assignment_status", "unassigned"),
            "native_category_count": native.get("native_category_count", "0"),
            "native_leaf_count": native.get("native_leaf_count", "0"),
            "native_snapshot_ids": ";".join(unique(edge.get("snapshot_id", "") for edge in edges)),
            "reading_status": reading.get("status", "missing_first_pass"),
            "deepseek_available": "true" if bool(first) else "false",
            "deepseek_full_text_checked": "true" if bool(structure.get("full_text_checked")) else "false",
            "deepseek_image_count": str(len(structure.get("images") or [])),
            "independent_review_status": review.get("conclusion", "not_reviewed"),
            "evidence_basis": ";".join(basis),
        }
        rows.append(row)

    fields = list(rows[0])
    REPORTS.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with OUT_JSONL.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    TOPIC_DIR.mkdir(parents=True, exist_ok=True)
    for code in TOPIC_ORDER:
        members = [row for row in rows if row["primary_print_topic_code"] == code]
        if not members:
            continue
        path = TOPIC_DIR / f"{code}-{TOPIC_NAMES[code].replace('/', '_')}.csv"
        with path.open("w", encoding="utf-8-sig", newline="") as fh:
            out_fields = ["ordinal", "id", "title", "published_date", "primary_print_topic", "secondary_print_topics", "classification_status", "classification_rule", "classification_note", "native_root_names", "native_object_paths", "concept_tags", "reading_status", "independent_review_status", "url"]
            writer = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(members)

    coverage = json.loads(NATIVE_COVERAGE.read_text(encoding="utf-8")) if NATIVE_COVERAGE.exists() else {}
    summary = {
        "generated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "corpus_records": len(rows),
        "unique_ids": len({row["id"] for row in rows}),
        "duplicate_ids": len(rows) - len({row["id"] for row in rows}),
        "primary_topic_counts": dict(Counter(row["primary_print_topic_code"] for row in rows)),
        "secondary_topic_memberships": dict(Counter(code for row in rows for code in row["secondary_print_topic_codes"].split(";") if code)),
        "classification_status_counts": dict(Counter(row["classification_status"] for row in rows)),
        "new_article_status_counts": dict(Counter(row["classification_status"] for row in rows if row["ordinal"] > 4050)),
        "new_articles": sum(row["ordinal"] > 4050 for row in rows),
        "new_articles_with_first_pass": sum(row["ordinal"] > 4050 and row["deepseek_available"] == "true" for row in rows),
        "new_articles_without_first_pass": sum(row["ordinal"] > 4050 and row["deepseek_available"] != "true" for row in rows),
        "a00_count": sum(row["primary_print_topic_code"] == "A00" for row in rows),
        "secondary_overlap_errors": sum(row["primary_print_topic_code"] in row["secondary_print_topic_codes"].split(";") for row in rows if row["secondary_print_topic_codes"]),
        "native_coverage": coverage,
        "review_queue_records": sum(row["classification_status"] in {"review_required", "needs_human_classification", "manual_provisional"} for row in rows),
        "outputs": [str(OUT), str(OUT_JSONL), str(SUMMARY), str(SUMMARY_MD), str(TOPIC_DIR)],
        "method": "A主专题由人工决定、官方路径与正文/初读证据、旧论文路由、23概念按优先级推导；候选和待审状态不伪装成正式定稿。",
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 岐伯论 v2 A专题分类覆盖报告", "",
        "本报告是独立于旧23概念映射的打印主专题层。原始语料、官方边表和 DeepSeek 初读均保持只读。", "",
        f"- 语料：{len(rows):,} 篇；唯一ID：{summary['unique_ids']:,}；重复ID：{summary['duplicate_ids']}",
        f"- 主专题覆盖：{len(rows):,}/{len(rows):,}；A00 待审：{summary['a00_count']:,}",
        f"- 新增：{summary['new_articles']:,}；有初读 {summary['new_articles_with_first_pass']:,}；缺初读 {summary['new_articles_without_first_pass']:,}",
        f"- 主专题待审核/临时状态：{summary['review_queue_records']:,}", "",
        "## 主专题数量", "", "|代码|专题|篇数|", "|---|---|---:|",
    ]
    for code in TOPIC_ORDER:
        lines.append(f"|{code}|{TOPIC_NAMES[code]}|{summary['primary_topic_counts'].get(code, 0):,}|")
    lines += ["", "## 状态数量", "", "|状态|篇数|", "|---|---:|"]
    for status, count in sorted(summary["classification_status_counts"].items()):
        lines.append(f"|{status}|{count:,}|")
    lines += ["", "## 解释", "", "主专题用于打印时一文一处；副专题、官方路径和23概念用于交叉检索。`review_required`、`needs_human_classification`、`manual_provisional` 均不能写成已完成细读结论。"]
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
