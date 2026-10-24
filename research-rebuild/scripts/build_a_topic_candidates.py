#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build auditable A01-A21 print-topic candidates.

This is a routing proposal for the print workflow.  It deliberately keeps
the official Sooon paths, the existing 23-concept route labels, and the
question/title cues in separate evidence columns.  It does not alter the
corpus, official edges, DeepSeek records, or the existing theme map.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
OUT = REPORTS

REGISTRY = DATA / "print-topic-registry-v2.csv"
THEME_MAP = REPORTS / "article-theme-map-v2.csv"
NATIVE_SUMMARY = REPORTS / "native-article-category-summary.csv"
NATIVE_EDGES = REPORTS / "native-article-category-edges.csv"
LEGACY_ROUTES = ROOT / "research/data/article_paper_route_map.csv"
PRINT_CROSSWALK = DATA / "print-topic-crosswalk-v2.csv"

# The order here is the registry order, with A00 reserved for unresolved
# cross-domain cases.  A01-A21 are intended as printable primary binders;
# official and legacy evidence remain visible alongside the candidate.
TOPICS = {
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
ORDER = list(TOPICS)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_legacy_routes(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    return {
        row.get("id", ""): unique((row.get("paperRoutes") or "").split(";"))
        for row in read_csv(path)
        if row.get("id")
    }


def read_jsonl(path: Path) -> dict[str, dict]:
    result = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                result[row["id"]] = row
    return result


def unique(values):
    result = []
    seen = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            seen.add(value); result.append(value)
    return result


def path_parts(path: str) -> tuple[str, str, str]:
    bits = [x.strip() for x in path.split("/") if x.strip()]
    return tuple((bits + ["", "", ""])[:3])


def add(scores: Counter, basis: dict[str, list[str]], topic: str, score: int, why: str) -> None:
    if topic not in TOPICS:
        return
    scores[topic] += score
    basis.setdefault(topic, []).append(why)


def official_scores(paths: list[str]) -> tuple[Counter, dict[str, list[str]]]:
    scores: Counter = Counter(); basis: dict[str, list[str]] = {}
    for path in paths:
        root, object_name, practice = path_parts(path)
        # Object/practice routing follows the official tree.  Specific object
        # paths outrank a generic root, making the candidate inspectable.
        if root == "与亲族":
            add(scores, basis, "A05", 10, f"official:{path}")
            if object_name == "与动物伙伴":
                add(scores, basis, "A18", 5, f"official-animal:{path}")
        elif root == "与友人":
            add(scores, basis, "A06", 10, f"official:{path}")
            if object_name == "与同志":
                add(scores, basis, "A17", 8, f"official-identity:{path}")
            if object_name == "与邻人":
                add(scores, basis, "A10", 2, f"official-community-order:{path}")
        elif root == "与合作者":
            add(scores, basis, "A07", 11, f"official:{path}")
            if object_name in {"与受教者", "与教导者"}:
                add(scores, basis, "A04", 7, f"official-teaching:{path}")
        elif root == "与自然":
            add(scores, basis, "A18", 12, f"official:{path}")
        elif root == "与其它":
            if object_name == "与AI":
                add(scores, basis, "A14", 14, f"official:{path}")
            elif object_name == "与敌人":
                add(scores, basis, "A12", 14, f"official:{path}")
            elif object_name == "与陌生人":
                add(scores, basis, "A10", 4, f"official-stranger-order:{path}")
                add(scores, basis, "A06", 2, f"official-stranger-relation:{path}")
        elif root == "与社会":
            if object_name == "与舆论":
                add(scores, basis, "A16", 13, f"official:{path}")
            elif object_name == "与历史":
                add(scores, basis, "A20", 13, f"official:{path}")
            elif object_name == "与艺术":
                add(scores, basis, "A15", 13, f"official:{path}")
            elif object_name == "与技术":
                add(scores, basis, "A13", 12, f"official:{path}")
            elif object_name == "与组织":
                add(scores, basis, "A07", 8, f"official-organization:{path}")
                add(scores, basis, "A10", 2, f"official-public-order:{path}")
            elif object_name == "与文化":
                add(scores, basis, "A15", 8, f"official:{path}")
                add(scores, basis, "A20", 4, f"official-cultural-history:{path}")
            elif object_name == "与社区":
                add(scores, basis, "A10", 5, f"official-community:{path}")
        elif root == "与自己":
            if object_name == "与能力":
                add(scores, basis, "A04", 11, f"official:{path}")
            elif object_name == "与情绪":
                add(scores, basis, "A01", 13, f"official:{path}")
            elif object_name == "与身体":
                add(scores, basis, "A02", 10, f"official:{path}")
                add(scores, basis, "A09", 3, f"official-body-care:{path}")
            elif object_name == "与财富":
                add(scores, basis, "A08", 11, f"official:{path}")
            elif object_name in {"与信念", "与原则"}:
                add(scores, basis, "A11", 7, f"official-belief-principle:{path}")
                add(scores, basis, "A01", 5, f"official-self-formation:{path}")
            elif object_name in {"与理想", "与欲望", "与名誉", "与时间"}:
                add(scores, basis, "A01", 10, f"official:{path}")
    return scores, basis


LEGACY_TO_TOPIC = {
    "心理与主体": "A01", "性别与身体": "A02", "事实与证据": "A03",
    "定义与达意": "A03", "能力与学习": "A04", "照料与家庭": "A05",
    "爱与回应": "A06", "边界与许可": "A06", "劳动与组织": "A07",
    "财富与市场": "A08", "成本与总账": "A08", "净输出与不掠夺": "A08",
    "法律与秩序": "A10", "权力与异议": "A10", "宗教与自然法": "A11",
    "技术与工程": "A13", "人工智能与机器": "A14", "文明与历史": "A20",
    "民族与身份": "A17", "生态与自然": "A18", "信用与信任": "A06",
}

KEYWORDS = [
    ("A19", r"死亡|去世|葬|丧|祭祀|祭奠|悼念|遗嘱|墓|烧七|周年|纪念"),
    ("A12", r"战争|军事|军队|战役|外交|国际秩序|军纪|备战|交战|敌人"),
    ("A09", r"疾病|病患|治疗|医生|医院|医疗|抑郁症|诊断|用药|手术|受伤|骨折"),
    ("A16", r"媒体|舆论|网红|新闻|传播|声明|热搜|公共形象|宣传"),
    ("A15", r"艺术|审美|电影|演员|绘画|书法|音乐|舞蹈|创作|文化生产"),
    ("A17", r"民族|族群|种族|国籍|移民|华人|身份认同|爱国"),
    ("A14", r"人工智能|\bAI\b|机器学习|机器人|自动驾驶|大模型|ChatGPT|GPT"),
    ("A13", r"技术|工程|软件|算法|芯片|制造|产业|能源|基础设施"),
    ("A18", r"生态|环境|气候|动物|植物|自然|污染|农业|能源|科学"),
]

# These are deliberately narrower than the 23-concept cues.  They exist to
# catch a concrete domain named by the title/question/body when a broad
# official relation path (for example, ``与友人 / 与朋友``) would otherwise
# hide the article's actual centre.  A hit remains a candidate signal and is
# written to the row for later sample review; it is never treated as a
# research conclusion by itself.
STRONG_DOMAIN_RULES = [
    ("A19", "death-ritual-memory", [
        r"死亡|去世|逝世|死者|亡者|亡故|丧葬|丧事|丧礼|葬礼|殡仪|墓碑|坟墓|祭祀|祭奠|悼念|悼亡|弥留|临终|遗体|祖先|家祭|纪念亡|太空葬",
    ]),
    ("A12", "war-military-diplomacy", [
        r"战争|军事|军队|军力|军训|军校|军舰|军服|军衔|军纪|军团|国防|外交|敌我|战犯|战争罪|交战|备战|军事同盟|俄乌|北约|武装冲突|军事训练",
    ]),
    ("A17", "ethnicity-identity", [
        r"民族|族群|种族|汉族|少数民族|民族团结|民族主义|身份政治|身份认同|移民|华人|混血|部落|族裔",
    ]),
    ("A09", "medical-disease-care", [
        r"疾病|病患|生病|医疗|医药|医生|医院|治疗|护理|照护|精神科|精神分裂|抑郁症|诊断|手术|传染病|疫情|病人|康复|方舱",
    ]),
    ("A14", "ai-machine-future", [
        r"人工智能|(?<![A-Za-z])AI(?![A-Za-z])|机器学习|机器人|生成式|大语言模型|自动驾驶|ChatGPT|GPT",
    ]),
    ("A21", "sports-exercise-competition", [
        r"体育|运动员|竞技|运动项目|体育赛事|群众体育|职业体育|业余体育|体育生态|体育体系|体育产业|体育治理|体育强国|体育大国|奥运会|足球|篮球|排球|网球|羽毛球|乒乓球|射击|射箭|马拉松|格斗|拳击|武术|健身",
    ]),
]

# A few legacy paper routes were added after the original 23-theme corpus
# work.  Their presence is useful as weak corroboration, but the route map is
# intentionally noisy, so it never outranks a concrete title/question cue.
LEGACY_ROUTE_TOPICS = {
    "25": "A09", "27": "A12", "30": "A19", "31": "A17",
    "32": "A18", "33": "A14", "28": "A15", "29": "A16",
}


def lexical_scores(article: dict) -> tuple[Counter, dict[str, list[str]]]:
    text = " ".join(str(article.get(k, "")) for k in ("title", "question"))
    scores: Counter = Counter(); basis: dict[str, list[str]] = {}
    for topic, pattern in KEYWORDS:
        hits = re.findall(pattern, text, flags=re.I)
        if hits:
            add(scores, basis, topic, min(3, len(hits)), f"title-question:{','.join(unique(hits))}")
    return scores, basis


def strong_domain_scores(article: dict) -> tuple[Counter, dict[str, list[str]], dict[str, dict]]:
    """Find explicit domain evidence that can expose an over-broad route.

    Question and body evidence are preferred.  A title-only hit is accepted
    only for an unambiguous phrase such as ``太空葬`` or ``俄乌战争``; generic
    metaphorical uses such as ``大军`` are intentionally not in the patterns.
    The score is a routing weight, not a confidence claim.
    """
    title = str(article.get("title", ""))
    question = str(article.get("question", ""))
    body = str(article.get("text", "") or article.get("lexical", ""))
    tq = f"{title} {question}"
    qbody = f"{question} {body}"
    scores: Counter = Counter()
    basis: dict[str, list[str]] = {}
    details: dict[str, dict] = {}
    for topic, rule_name, patterns in STRONG_DOMAIN_RULES:
        qbody_hits: list[str] = []
        tq_hits: list[str] = []
        title_hits: list[str] = []
        for pattern in patterns:
            qbody_hits.extend(re.findall(pattern, qbody, flags=re.I))
            tq_hits.extend(re.findall(pattern, tq, flags=re.I))
            title_hits.extend(re.findall(pattern, title, flags=re.I))
        qbody_hits = unique(qbody_hits)
        tq_hits = unique(tq_hits)
        title_hits = unique(title_hits)
        if topic == "A14":
            # Ignore generic English words containing the token AI (e.g.
            # ``said``) while keeping standalone AI/ChatGPT/GPT references.
            qbody_hits = [h for h in qbody_hits if h.upper() in {"AI", "GPT", "CHATGPT"} or any(x in h for x in ("人工智能", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶"))]
            tq_hits = [h for h in tq_hits if h.upper() in {"AI", "GPT", "CHATGPT"} or any(x in h for x in ("人工智能", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶"))]
            title_hits = [h for h in title_hits if h.upper() in {"AI", "GPT", "CHATGPT"} or any(x in h for x in ("人工智能", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶"))]
        if topic == "A09":
            # ``疾病/生病/医疗`` often appears in a hypothetical list or a
            # comparison.  Require a concrete care/clinical term before a
            # title/question cue can override a relation path.
            specific = {"生病", "病患", "医生", "医院", "治疗", "护理", "照护", "精神科", "精神分裂", "抑郁症", "诊断", "手术", "传染病", "疫情", "病人", "康复", "方舱"}
            if not any(hit in specific for hit in tq_hits):
                tq_hits = []
            if len([hit for hit in qbody_hits if hit in specific]) == 0:
                qbody_hits = []
        if topic == "A19":
            # Death alone is not a memorial/ritual article: traffic, war and
            # medical reports frequently mention a death incidentally.  Keep
            # ritual, burial, remembrance and explicit mortality questions.
            ritual = {"丧葬", "丧事", "丧礼", "葬礼", "殡仪", "墓碑", "坟墓", "祭祀", "祭奠", "悼念", "悼亡", "弥留", "临终", "祖先", "家祭", "纪念亡", "太空葬"}
            explicit = re.search(r"死亡的意义|害怕死亡|面对死亡|去世后|去世前|死亡是什么|处理.*骨灰|自主.*结束生命|安乐死|死亡如此", tq)
            if not explicit and not any(hit in ritual for hit in tq_hits):
                tq_hits = []
            if not any(hit in ritual for hit in qbody_hits) and not explicit:
                qbody_hits = []
        if topic == "A17":
            # Identity terms in the article body can be examples rather than
            # the article's centre.  A title/question cue is required for a
            # strong ethnicity/identity candidate.
            if not tq_hits:
                qbody_hits = []
        # Explicit question/body evidence is strongest.  Title-only evidence
        # is retained for clearly domain-specific phrases and marked for
        # review, so it cannot silently become a final classification.
        # A single incidental body mention is not enough for a long answer.
        # The question/title or at least two distinct body cues must support
        # the domain before it can compete with an official route.
        explicit_domain = bool(tq_hits or title_hits)
        if explicit_domain or len(qbody_hits) >= 2:
            # The article's question/title expresses its requested centre;
            # body-only mentions are useful but deliberately weaker because a
            # long answer may cite medicine, war, or identity only as an
            # example.  Body-only hits therefore flag a review candidate but
            # do not outrank a specific official path.
            score = min(25, 22 + len(tq_hits)) if tq_hits else min(4, 2 + len(qbody_hits) // 2)
            details[topic] = {"rule": rule_name, "qbody_hits": qbody_hits, "tq_hits": tq_hits, "title_hits": title_hits, "title_only": bool(title_hits and not tq_hits), "body_only": not explicit_domain}
            if explicit_domain:
                add(scores, basis, topic, score, f"strong:{rule_name}:{','.join(qbody_hits)}")
        elif title_hits and any(len(hit) >= 2 for hit in title_hits):
            score = 16
            add(scores, basis, topic, score, f"strong-title:{rule_name}:{','.join(title_hits)}")
            details[topic] = {"rule": rule_name, "qbody_hits": [], "tq_hits": [], "title_hits": title_hits, "title_only": True}
    return scores, basis, details


def choose(scores: Counter) -> tuple[str, list[str], str]:
    positive = [(topic, score) for topic, score in scores.items() if score > 0]
    if not positive:
        return "A00", [], "needs_human"
    ranked = sorted(positive, key=lambda item: (-item[1], ORDER.index(item[0])))
    top_score = ranked[0][1]
    top = [topic for topic, score in ranked if score == top_score]
    # Keep at most three secondary topics; a close tie remains explicitly
    # reviewable rather than pretending to be a settled primary assignment.
    secondary = [topic for topic, _ in ranked[1:4]]
    status = "needs_human" if len(top) > 1 or (top_score <= 2 and len(ranked) > 1) else "candidate"
    return top[0], secondary, status


def main() -> None:
    articles = read_jsonl(V2)
    theme_rows = {row["id"]: row for row in read_csv(THEME_MAP)}
    native_rows = {row["article_id"]: row for row in read_csv(NATIVE_SUMMARY)}
    legacy_routes = load_legacy_routes(LEGACY_ROUTES)
    edges: dict[str, list[str]] = defaultdict(list)
    for row in read_csv(NATIVE_EDGES):
        if row.get("article_id") and row.get("native_parent_path_names"):
            edges[row["article_id"]].append(row["native_parent_path_names"])

    rows = []
    for ordinal, (aid, article) in enumerate(articles.items(), 1):
        theme = theme_rows.get(aid, {})
        native = native_rows.get(aid, {})
        paths = unique(edges.get(aid, []))
        legacy = unique((theme.get("concepts") or "").split(";"))
        scores, basis = official_scores(paths)
        # Legacy concepts are deliberately weak.  The old paper-route map is
        # retained as provenance only: its route sets are broad (often 15+
        # routes per article), so treating route numbers as primary evidence
        # would create systematic false A14/A17/A18 assignments.
        for concept in legacy:
            target = LEGACY_TO_TOPIC.get(concept)
            if target:
                add(scores, basis, target, 2, f"legacy:{concept}")
        legacy_route_values = legacy_routes.get(aid, [])
        lex_scores, lex_basis = lexical_scores(article)
        for target, score in lex_scores.items():
            add(scores, basis, target, score, ";".join(lex_basis[target]))
        strong_scores, strong_basis, strong_details = strong_domain_scores(article)
        for target, score in strong_scores.items():
            add(scores, basis, target, score, ";".join(strong_basis[target]))
        primary, secondary, status = choose(scores)
        official_topics = [topic for topic in ORDER if any(x.startswith("official") for x in basis.get(topic, []))]
        strong_topics = [topic for topic in ORDER if topic in strong_scores]
        # Explicit domain cues outrank broad official paths.  A disagreement
        # is retained as a review conflict rather than hidden by the official
        # relation label.  A single strong cue still remains a candidate, not
        # a completed human classification.
        # Body-only matches are diagnostics, not a primary routing signal.
        primary_strong_topics = [
            topic for topic, detail in strong_details.items()
            if not detail.get("body_only")
        ]
        if primary_strong_topics:
            strong_topics = primary_strong_topics
            if len(strong_topics) > 1 or (official_topics and primary not in strong_topics):
                status = "strong_domain_conflict"
            elif len(strong_topics) == 1:
                status = "strong_domain_candidate"
        elif official_topics:
            status = "official_direct" if len(official_topics) == 1 and primary == official_topics[0] else "official_multi"
        elif legacy:
            status = "legacy_route" if status == "candidate" else "legacy_needs_human"
        basis_labels = []
        if paths: basis_labels.append("official_path")
        if legacy: basis_labels.append("legacy_23_theme")
        if legacy_route_values: basis_labels.append("legacy_paper_route_provenance")
        if lex_scores: basis_labels.append("title_question_hint")
        if strong_scores: basis_labels.append("strong_domain_cue")
        if primary == "A00": basis_labels.append("no_reliable_signal")
        note_parts = [f"scores={';'.join(f'{t}:{scores[t]}' for t in sorted(scores, key=lambda t: (-scores[t], ORDER.index(t)))[:6])}"]
        if paths: note_parts.append("official_paths=" + " | ".join(paths[:5]))
        if strong_details:
            note_parts.append("strong_domain=" + ";".join(f"{t}:{','.join(d.get('tq_hits') or d.get('qbody_hits') or d.get('title_hits') or [])}" for t, d in strong_details.items()))
        if official_topics and strong_topics and set(official_topics) != set(strong_topics):
            note_parts.append("official_vs_strong_conflict=" + ",".join(official_topics) + "->" + ",".join(strong_topics))
        if not paths and native.get("native_assignment_status") != "confirmed": note_parts.append("official_node_unassigned")
        rows.append({
            "source_ordinal": ordinal, "id": aid, "title": article.get("title", ""),
            "primary_print_topic": primary, "primary_print_topic_name": TOPICS[primary],
            "secondary_print_topics": ";".join(secondary), "classification_status": status,
            "classification_basis": ";".join(basis_labels), "classification_note": " | ".join(note_parts),
            "topic_score_trace": ";".join(f"{t}:{scores[t]}" for t in sorted(scores, key=lambda t: (-scores[t], ORDER.index(t)))),
            "strong_domain_topics": ";".join(strong_topics),
            "strong_domain_hits": ";".join(f"{t}:{','.join(d.get('tq_hits') or d.get('qbody_hits') or d.get('title_hits') or [])}" for t, d in strong_details.items()),
            "official_paths": ";".join(paths), "official_root_names": native.get("native_root_names", ""),
            "official_assignment_status": native.get("native_assignment_status", "unassigned"),
            "legacy_primary": theme.get("primary", ""), "legacy_concepts": theme.get("concepts", ""),
            "legacy_paper_routes": ";".join(legacy_route_values),
            "legacy_audit_status": theme.get("audit_status", ""), "question": article.get("question", ""),
        })

    fields = list(rows[0])
    csv_path = OUT / "a-topic-candidates-v2.csv"
    summary_path = OUT / "a-topic-candidates-v2-summary.json"
    method_path = OUT / "a-topic-candidates-v2-method.md"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
    counts = Counter(row["primary_print_topic"] for row in rows)
    statuses = Counter(row["classification_status"] for row in rows)
    strong_counts = Counter(row["strong_domain_topics"] for row in rows if row["strong_domain_topics"])
    root_counts = Counter(row["official_root_names"] for row in rows if row["official_root_names"])
    summary = {
        "records": len(rows), "topic_count": 21, "candidate_primary_counts": dict(counts),
        "classification_status_counts": dict(statuses), "official_assignment_status_counts": Counter(row["official_assignment_status"] for row in rows),
        "strong_domain_rows": sum(bool(row["strong_domain_topics"]) for row in rows),
        "strong_domain_topic_combinations": dict(strong_counts),
        "strong_domain_conflict_rows": statuses.get("strong_domain_conflict", 0),
        "rows_with_official_paths": sum(bool(row["official_paths"]) for row in rows),
        "rows_without_official_paths": sum(not bool(row["official_paths"]) for row in rows),
        "rows_primary_a00": counts.get("A00", 0), "root_membership_counts": dict(root_counts),
        "outputs": [str(csv_path), str(summary_path), str(method_path)],
        "note": "候选主专题供打印索引审阅；不覆盖23主题或官方边表。具体领域线索可覆盖泛官方路径，但仍标为候选/冲突，必须抽样回到正文。",
    }
    # Counter is not JSON serializable without conversion.
    summary["official_assignment_status_counts"] = dict(summary["official_assignment_status_counts"])
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    method = """# A01-A21 打印主专题候选规则

本表是打印研究索引的候选层，不改变原始语料、素问官方分类、DeepSeek 初读或岐伯论 23 主题映射。

## 证据优先级

1. 素问官方具体路径（对象/实践）是强证据；例如“与亲族”路由到 A05，“与合作者”路由到 A07，“与社会/与舆论”路由到 A16，“与其它/与AI”路由到 A14。
2. 既有 23 主题只作弱补充，主要用于官方未归类的 616 篇和官方路径过宽节点。
3. 标题和提问关键词只作低权重提示；不能凭标题把文章定为正式专题。
4. `needs_human`、`legacy_needs_human`、`official_multi` 均需回到正文和官方边证据决定主专题；A00 是没有可靠信号时的待审占位。

## 输出字段

- `primary_print_topic` / `secondary_print_topics`：供打印分册候选；次级最多保留3个。
- `classification_status`：`official_direct`、`official_multi`、`legacy_route`、`legacy_needs_human`、`needs_human`。
- `classification_basis`：逐行说明使用的官方路径、旧主题或标题/问题提示。
- `topic_score_trace` 与 `classification_note`：保留规则可复核证据，不是作者观点结论。
"""
    method_path.write_text(method, encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
