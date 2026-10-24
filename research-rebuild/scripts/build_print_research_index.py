#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a print-oriented, traceable article research index.

This is a reporting layer only.  It does not edit the v2 corpus, the first
pass output, or any existing classification.  Each article remains one row in
the master index, while per-topic and per-official-root files repeat an article
when it has multiple memberships.  The repeated files are intentional: they
are convenient print batches, not a replacement for the one-row master.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
DEFAULT_REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_OUT = DEFAULT_REPORTS / "print-index"
DEFAULT_DS = ROOT / "research-rebuild/out"
DEFAULT_REGISTRY = ROOT / "research-rebuild/data/print-topic-registry-v2.csv"
DEFAULT_LEGACY_ROUTES = ROOT / "research/data/article_paper_route_map.csv"
DEFAULT_CLASSIFICATION = ROOT / "research-rebuild/reports/article-classification-v2.csv"

# Keep this order identical to classify_v2_with_sampling.py.  It is only a
# presentation order; labels and memberships are read from the current map.
THEMES = [
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
]
ROOTS = ["与自己", "与其它", "与亲族", "与社会", "与合作者", "与自然", "与友人"]

# A-topic codes are the mutually exclusive printing spine defined in
# final-classification-framework-v2.md.  The registry remains the source of
# names/descriptions; this fallback order only resolves an article with more
# than one legacy paper route.
ROUTE_PRIORITY = [
    "A09", "A10", "A12", "A14", "A21", "A02", "A05", "A06", "A07", "A08",
    "A04", "A11", "A13", "A15", "A16", "A17", "A18", "A19", "A20",
    "A01", "A03", "A00",
]


def read_jsonl(path: Path) -> Iterable[dict]:
    if not path.exists():
        return
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line.strip():
                row = json.loads(line)
                row["_line"] = line_no
                yield row


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def unique(values: Iterable[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def join(values: Iterable[str]) -> str:
    return ";".join(unique(values))


def as_int(value: object) -> int | None:
    try:
        return int(value) if value not in (None, "") else None
    except (TypeError, ValueError):
        return None


def local_date(value: object) -> str:
    raw = as_int(value)
    if raw is None:
        return ""
    # Source timestamps are milliseconds.  The project uses China Standard
    # Time for displayed dates, matching the site's publication display.
    try:
        return datetime.fromtimestamp(raw / 1000, tz=timezone(timedelta(hours=8))).date().isoformat()
    except (OverflowError, OSError, ValueError):
        return ""


def safe_filename(text: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|\r\n]+", "_", text).strip(" .")
    return value or "未命名"


def first_pass_fields(rec: dict, reading: dict) -> dict[str, object]:
    structure = rec.get("structure") or {}
    analysis = rec.get("analysis") or {}
    metadata = rec.get("metadata") or {}
    rec_reading = rec.get("reading") or {}
    evidence = rec.get("evidence_refs")
    if evidence is None:
        evidence = analysis.get("evidence_locations") or []
    claims = analysis.get("main_claims") or []
    unresolved = analysis.get("unresolved_questions") or analysis.get("open_questions") or []
    images = structure.get("images") or []
    if not isinstance(evidence, list):
        evidence = [evidence] if evidence else []
    if not isinstance(claims, list):
        claims = [claims] if claims else []
    if not isinstance(unresolved, list):
        unresolved = [unresolved] if unresolved else []
    return {
        "deepseek_available": bool(rec),
        "deepseek_batch_id": rec_reading.get("batch_id") or reading.get("batch_id", ""),
        "deepseek_reading_status": rec_reading.get("status") or reading.get("status", ""),
        "deepseek_full_text_checked": bool(structure.get("full_text_checked")),
        "deepseek_text_coverage_status": reading.get("text_coverage_status", ""),
        "deepseek_image_count": len(images),
        "deepseek_image_checked": bool(rec_reading.get("image_checked")),
        "deepseek_evidence_ref_count": len(evidence),
        "deepseek_main_claim_count": len(claims),
        "deepseek_unresolved_question_count": len(unresolved),
        "deepseek_record_line": rec.get("_line", ""),
    }


def derive_evidence_state(first: dict, review: dict, theme_status: str) -> tuple[str, str]:
    """Return a navigation state and a conservative print gate.

    The gate is about whether a printed packet should be flagged for review;
    it is deliberately not a claim that the article's argument is true.
    """
    conclusion = review.get("conclusion", "")
    if conclusion == "reviewed_needs_revision":
        return "independent_review_needs_revision", "hold_review_revision"
    if conclusion == "reviewed_agree":
        evidence_state = "independent_review_agree"
    elif not first["deepseek_available"]:
        evidence_state = "first_pass_missing"
    elif first["deepseek_reading_status"] == "needs_reread":
        evidence_state = "first_pass_needs_reread"
    elif first["deepseek_full_text_checked"]:
        evidence_state = "first_pass_full_text_checked"
    else:
        evidence_state = "first_pass_recorded"

    if theme_status in {"review_required", "needs_human_classification"}:
        return evidence_state, "hold_theme_review"
    if theme_status in {"manual_provisional", "reviewed_needs_revision"}:
        return evidence_state, "hold_provisional_theme"
    if not first["deepseek_available"]:
        return evidence_state, "hold_first_pass_missing"
    if first["deepseek_reading_status"] == "needs_reread" or first["deepseek_image_count"]:
        return evidence_state, "review_before_annotation"
    return evidence_state, "index_ready_with_source_caveat"


def load_first_pass(ds_dir: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted(ds_dir.glob("*.out.jsonl")):
        for row in read_jsonl(path):
            aid = row.get("article_id")
            if aid:
                row["_file"] = path.name
                result[aid] = row
    return result


def load_reading(root: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for row in read_jsonl(root / "research-rebuild/records/reading-records.jsonl"):
        if row.get("id"):
            result[row["id"]] = row
    return result


def load_reviews(root: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for row in read_jsonl(root / "research-rebuild/reports/independent-reviews.jsonl"):
        if row.get("article_id"):
            result[row["article_id"]] = row
    return result


def load_topic_registry(path: Path) -> tuple[dict[str, dict], list[str]]:
    rows = read_csv(path)
    by_code = {r.get("code", ""): r for r in rows if r.get("code")}
    order = [r["code"] for r in sorted(rows, key=lambda r: int(r.get("sort_order") or 999)) if r.get("code")]
    return by_code, order


def load_topic_crosswalk(path: Path) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in read_csv(path):
        grouped[row.get("source_type", "")].append(row)
    return grouped


def load_legacy_routes(path: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for row in read_csv(path):
        if row.get("id"):
            result[row["id"]] = unique(row.get("paperRoutes", "").split(";"))
    return result


def load_manual_decisions(path: Path) -> dict[str, dict]:
    return {row.get("id"): row for row in read_csv(path) if row.get("id")}


def load_classification(path: Path) -> dict[str, dict]:
    """Load the latest A-topic classifier output as the authoritative spine.

    The print index keeps its own native/concept columns, but the classifier
    is the single source for the final A-topic choice.  Older classifier
    revisions used slightly different field names, so both code/name and the
    formal status fields are accepted here.
    """
    return {row.get("id"): row for row in read_csv(path) if row.get("id")}


def route_code_map(rules: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = defaultdict(list)
    for rule in rules:
        for route in (rule.get("source_value", "").split(";") if rule.get("source_value") else []):
            out[route.strip()].append(rule)
    return out


def primary_topic_candidates(
    article: dict,
    aid: str,
    native_edges: list[dict],
    theme_row: dict,
    review: dict,
    manual_row: dict,
    registry: dict[str, dict],
    crosswalk: dict[str, list[dict]],
    legacy_routes: dict[str, list[str]],
    classification_row: dict | None = None,
) -> dict:
    """Derive A-topic candidates with an explicit evidence trail.

    This function intentionally returns candidates plus a status.  It never
    treats the old 23-concept primary label as an A-topic primary.  Official
    paths are the strongest layer, legacy paper routes are the fallback, and
    concepts are navigation-only unless a manually reviewed row has no
    stronger route.  A broad path or a conflict still receives a deterministic
    primary for printing, but is marked `review_required`; only rows without a
    usable route are placed in the human-classification queue.
    """
    native_rules = crosswalk.get("native_path_prefix", [])
    legacy_rules = crosswalk.get("legacy_paper_route", [])
    concept_rules = crosswalk.get("concept", [])
    legacy_by_route = route_code_map(legacy_rules)
    native_scores: Counter[str] = Counter()
    legacy_scores: Counter[str] = Counter()
    evidence: dict[str, list[str]] = defaultdict(list)
    rules_hit: dict[str, list[str]] = defaultdict(list)
    native_review_needed = False
    legacy_review_needed = False
    basis_parts: list[str] = []

    # A separately generated classifier is the final A-topic decision layer.
    # Keep this early return so the print index cannot silently drift from
    # article-classification-v2 while still retaining all native/concept data
    # in the surrounding row.
    if classification_row:
        code = (classification_row.get("primary_print_topic_code") or "").strip()
        if not code:
            name = (classification_row.get("primary_print_topic") or "").strip()
            code = next((c for c, r in registry.items() if r.get("name") == name), "")
        if code in registry:
            secondary_raw = classification_row.get("secondary_print_topic_codes", "")
            secondary = [c for c in unique(secondary_raw.split(";")) if c in registry and c != code][:3]
            candidates = unique((classification_row.get("candidate_primary_print_topics") or code).split(";"))
            candidates = [c for c in candidates if c in registry and c != "A00"]
            if not candidates and code != "A00":
                candidates = [code]
            status = classification_row.get("classification_status") or classification_row.get("primary_topic_status") or "review_required"
            # Initialize fields used by the explicit manual override path.
            # They are populated from the classifier below when no override is
            # present, but must still exist when the formal A-topic table is
            # authoritative.
            rule_ids: list[str] = []
            candidate_rule_ids: list[str] = []
            basis = ""
            note = ""
            # The manual decision table is the final human override.  The
            # classifier is rebuilt from the same table, but accepting the
            # explicit row here prevents stale/partial classifier exports
            # from overwriting a just-reviewed primary, secondary, or status.
            if manual_row:
                manual_code = (manual_row.get("primary_print_topic_code") or "").strip()
                manual_secondary = [c for c in unique((manual_row.get("secondary_print_topic_codes") or "").split(";")) if c in registry and c != manual_code][:3]
                manual_status = (manual_row.get("classification_status") or "").strip()
                if manual_code in registry and manual_status in {"manual_confirmed", "manual_provisional"}:
                    code = manual_code
                    secondary = manual_secondary
                    candidates = [code]
                    status = manual_status
                    basis = manual_row.get("decision_basis") or basis
                    note = manual_row.get("review_note") or note
                    return {
                        "primary": code,
                        "secondary": secondary,
                        "candidate_primary": candidates,
                        "rule_ids": rule_ids,
                        "candidate_rule_ids": candidate_rule_ids,
                        "status": status,
                        "basis": basis,
                        "note": note,
                        "candidate_score": as_int(classification_row.get("primary_topic_candidate_score")) or 0,
                        "candidate_tie_count": 1,
                    }
            # Candidate-only labels from older classifier revisions are not
            # formal states in the framework; preserve the row but normalize
            # them to the review queue.
            if status in {"native_routed_candidate", "legacy_routed_candidate", "candidate", "provisional"}:
                status = "review_required"
            if status not in {"audited", "manual_confirmed", "manual_provisional", "review_required", "needs_human_classification", "uncertain"}:
                status = "review_required"
            basis = classification_row.get("evidence_basis") or classification_row.get("classification_rule") or "article_classification_v2"
            note = classification_row.get("classification_note") or "来自 article-classification-v2.csv；官方路径、23 概念和原文入口保留在本索引其他字段。"
            rule_ids = unique((classification_row.get("primary_topic_rule_ids") or "").split(";"))
            candidate_rule_ids = unique((classification_row.get("candidate_topic_rule_ids") or "").split(";"))
            return {
                "primary": code,
                "secondary": secondary,
                "candidate_primary": candidates,
                "rule_ids": rule_ids,
                "candidate_rule_ids": candidate_rule_ids,
                "status": status,
                "basis": basis,
                "note": note,
                "candidate_score": as_int(classification_row.get("primary_topic_candidate_score")) or as_int(classification_row.get("top_score")) or 0,
                "candidate_tie_count": as_int(classification_row.get("primary_topic_tie_count")) or as_int(classification_row.get("tie_count")) or 1,
            }

    # Longest matching official path wins within the official layer.  Parent
    # and child prefixes can both match; keeping the longest avoids counting a
    # generic root path as stronger than its specific practice path.
    native_hits: list[tuple[int, int, str, str, bool]] = []
    for edge in native_edges:
        path = edge.get("native_parent_path_names", "")
        for rule in native_rules:
            prefix = rule.get("source_value", "")
            if prefix and (path == prefix or path.startswith(prefix + " / ")):
                for code in unique((rule.get("topic_codes") or "").split(";")):
                    if code in registry and code != "A00":
                        native_hits.append((len(prefix), int(rule.get("priority") or 0), code, rule.get("rule_id", ""), rule.get("review_required", "").lower() == "true"))
    max_path = max((h[0] for h in native_hits), default=0)
    for path_len, priority, code, rule_id, needs in native_hits:
        if path_len != max_path:
            continue
        native_scores[code] += priority
        evidence[code].append("official_path")
        rules_hit[code].append(rule_id)
        native_review_needed = native_review_needed or needs
    if native_hits:
        basis_parts.append("official_path")

    # Existing paper routes are a useful audit trail for old articles.  Only
    # route rules designated as primary candidates compete for the primary;
    # secondary/tie-breaker routes remain evidence but never force a topic.
    legacy_hits = []
    for route in legacy_routes.get(aid, []):
        for rule in legacy_by_route.get(route, []):
            if rule.get("decision_role") == "primary_candidate":
                for code in unique((rule.get("topic_codes") or "").split(";")):
                    if code in registry and code != "A00":
                        legacy_hits.append((code, int(rule.get("priority") or 0), rule.get("rule_id", ""), rule.get("review_required", "").lower() == "true"))
    for code, priority, rule_id, needs in legacy_hits:
        legacy_scores[code] += priority
        evidence[code].append("legacy_paper_route")
        rules_hit[code].append(rule_id)
        legacy_review_needed = legacy_review_needed or needs
    if legacy_hits:
        basis_parts.append("legacy_paper_route")

    # Concepts are secondary navigation only unless no other evidence exists.
    # They help build a review queue and cannot silently replace the A-topic
    # distinction between, for example, a family and a workplace article.
    concept_names = unique((theme_row.get("concepts") or "").split(";"))
    for rule in concept_rules:
        if rule.get("source_value") not in concept_names:
            continue
        for code in unique((rule.get("topic_codes") or "").split(";")):
            if code in registry:
                evidence[code].append("23_concept")
                rules_hit[code].append(rule.get("rule_id", ""))

    # Reviewed records may have an explicit manual status.  The current manual
    # file stores the 23-concept decision rather than an A-code, so it can only
    # supply a fallback candidate when no official or legacy route exists.
    manual_status = manual_row.get("audit_status", "") if manual_row else ""
    review_conclusion = review.get("conclusion", "")
    if review_conclusion == "reviewed_agree":
        manual_status = "manual_confirmed"
    elif review_conclusion == "reviewed_needs_revision":
        manual_status = "review_required"

    registry_pos = {code: i for i, code in enumerate(registry)}

    def ordered_top(scores: Counter[str]) -> list[str]:
        candidates = [c for c in scores if c in registry and c != "A00"]
        if not candidates:
            return []
        max_score = max(scores[c] for c in candidates)
        return sorted(
            [c for c in candidates if scores[c] == max_score],
            key=lambda c: (ROUTE_PRIORITY.index(c) if c in ROUTE_PRIORITY else 999, registry_pos.get(c, 999)),
        )

    # Evidence layers are deliberately not summed.  A single official path
    # must outrank a large number of old concept/route hints, while a legacy
    # route remains useful for the 616 records absent from the official tree.
    native_top = ordered_top(native_scores)
    legacy_top = ordered_top(legacy_scores)
    if native_top:
        top = native_top
        primary = top[0]
        basis_parts.append("official_path")
        conflict = bool(legacy_top and set(legacy_top) != {primary})
        if len(top) > 1 or native_review_needed or conflict:
            status = "review_required"
        elif manual_status in {"manual_provisional", "manual_confirmed"}:
            status = manual_status
        elif theme_row.get("source") == "reused_audited_map":
            status = "audited"
        else:
            status = "review_required"
    elif legacy_top:
        top = legacy_top
        primary = top[0]
        basis_parts.append("legacy_paper_route")
        if len(top) > 1 or legacy_review_needed:
            status = "review_required"
        elif manual_status in {"manual_provisional", "manual_confirmed"}:
            status = manual_status
        elif theme_row.get("source") == "reused_audited_map":
            status = "audited"
        else:
            status = "review_required"
    else:
        # A manual decision is the only route allowed to promote a concept
        # mapping when official and legacy evidence are both absent.  It keeps
        # the 28 sampled rows usable without pretending that a keyword-only
        # concept label is a settled classification.
        manual_concepts = unique((manual_row.get("concepts") or "").split(";")) if manual_row else []
        manual_scores: Counter[str] = Counter()
        for concept in manual_concepts:
            for rule in concept_rules:
                if rule.get("source_value") == concept:
                    for code in unique((rule.get("topic_codes") or "").split(";")):
                        if code in registry and code != "A00":
                            manual_scores[code] += int(rule.get("priority") or 0)
        top = ordered_top(manual_scores)
        if top and manual_status in {"manual_provisional", "manual_confirmed", "review_required"}:
            primary = top[0]
            basis_parts.append("manual_concept_decision")
            status = manual_status if manual_status in {"manual_provisional", "manual_confirmed"} else "review_required"
        else:
            primary = "A00"
            top = []
            status = "needs_human_classification"
            basis_parts.append("no_native_or_legacy_primary_evidence")
    # Cross-domain candidates are secondary print routes, capped at three to
    # keep paper packets readable.  They never contain the primary code.
    secondary = []
    combined_scores = native_scores + legacy_scores
    for code in sorted(evidence, key=lambda c: (-combined_scores.get(c, 0), c)):
        if code in registry and code != primary and code != "A00" and code not in secondary:
            secondary.append(code)
    if not secondary and primary == "A00":
        # A00 is itself an explicit queue, not a real domain label.
        secondary = []
    note = "证据层=" + "+".join(unique(basis_parts))
    if len(top) > 1:
        note += ";候选并列=" + ";".join(top)
    if primary == "A00":
        note += ";需要回到正文确定中心场景"
    return {
        "primary": primary,
        "secondary": secondary[:3],
        "candidate_primary": top,
        "rule_ids": unique(rules_hit.get(primary, [])),
        "candidate_rule_ids": unique(rule_id for ids in rules_hit.values() for rule_id in ids),
        "status": status,
        "basis": join(basis_parts),
        "note": note,
        "candidate_score": combined_scores.get(primary, 0),
        "candidate_tie_count": len(top),
    }


def build(args: argparse.Namespace) -> dict:
    articles = list(read_jsonl(args.v2))
    theme_rows = read_csv(args.reports / "article-theme-map-v2.csv")
    theme_by_id = {row.get("id"): row for row in theme_rows if row.get("id")}
    native_rows = read_csv(args.reports / "native-article-category-summary.csv")
    native_by_id = {row.get("article_id"): row for row in native_rows if row.get("article_id")}
    crosswalk_rows = read_csv(args.reports / "native-theme-crosswalk-200.csv")
    crosswalk_by_node = {row.get("native_node_id"): row for row in crosswalk_rows if row.get("native_node_id")}
    edge_by_id: dict[str, list[dict]] = defaultdict(list)
    for row in read_csv(args.reports / "native-article-category-edges.csv"):
        aid = row.get("article_id")
        if aid:
            edge_by_id[aid].append(row)
    first_pass = load_first_pass(args.root / "research-rebuild/out")
    reading = load_reading(args.root)
    reviews = load_reviews(args.root)
    registry, registry_order = load_topic_registry(args.registry)
    crosswalk = load_topic_crosswalk(args.crosswalk)
    legacy_routes = load_legacy_routes(args.legacy_routes)
    classification = load_classification(args.classification)
    # The A-topic print spine is authoritative here.  The older
    # manual-theme-decisions-v2.csv is the separate 23-concept compatibility
    # layer and cannot override A-topic codes or classification status.
    manual_decisions = load_manual_decisions(args.root / "research-rebuild/data/print-topic-manual-decisions-v2.csv")

    rows: list[dict] = []
    for source_ordinal, article in enumerate(articles, 1):
        aid = article.get("id", "")
        t = theme_by_id.get(aid, {})
        n = native_by_id.get(aid, {})
        read = reading.get(aid, {})
        ds = first_pass.get(aid, {})
        review = reviews.get(aid, {})
        manual = manual_decisions.get(aid, {})
        edges = edge_by_id.get(aid, [])
        concepts = unique((t.get("concepts") or "").split(";"))
        primary = t.get("primary") or (concepts[0] if concepts else "")
        secondary = [c for c in concepts if c != primary]
        category_names = unique((n.get("native_category_names") or "").split(";"))
        root_names = unique((n.get("native_root_names") or "").split(";"))
        paths = unique(e.get("native_parent_path_names", "") for e in edges)
        kinds = unique(e.get("native_kind", "") for e in edges)
        methods = unique(e.get("match_method", "") for e in edges)
        confidences = unique(e.get("match_confidence", "") for e in edges)
        snapshot_ids = unique(e.get("snapshot_id", "") for e in edges)
        mapped_statuses = unique(crosswalk_by_node.get(e.get("native_category_id", ""), {}).get("mapping_status", "") for e in edges)
        mapped_decisions = unique(crosswalk_by_node.get(e.get("native_category_id", ""), {}).get("review_decision", "") for e in edges)
        fp = first_pass_fields(ds, read)
        a_topic = primary_topic_candidates(
            article, aid, edges, t, review, manual, registry, crosswalk, legacy_routes,
            classification.get(aid),
        )
        evidence_state, print_gate = derive_evidence_state(fp, review, a_topic["status"])
        primary_code = a_topic["primary"]
        primary_name = registry.get(primary_code, {}).get("name", primary_code)
        secondary_codes = a_topic["secondary"]
        secondary_names = [registry.get(code, {}).get("name", code) for code in secondary_codes]
        candidate_primary_codes = a_topic["candidate_primary"]
        native_status_raw = n.get("native_assignment_status", "unassigned")
        native_status = "confirmed" if native_status_raw == "confirmed" else "native_unassigned_valid"
        reading_status = review.get("conclusion") or fp.get("deepseek_reading_status") or "missing_first_pass"
        body = article.get("text") or ""
        lexical = article.get("lexical") or ""
        # Empty text can still have image/lexical content and must not be
        # silently treated as absent source data.
        source_body_state = "text_present" if body else ("lexical_or_image_only" if lexical else "text_missing")
        row = {
            "source_ordinal": source_ordinal,
            "id": aid,
            "title": article.get("title", ""),
            "published_at_raw": article.get("publishedAt", ""),
            "published_date": local_date(article.get("publishedAt")),
            "updated_at_raw": article.get("updatedAt", ""),
            "updated_date": local_date(article.get("updatedAt")),
            "url": article.get("url", ""),
            "question": article.get("question", ""),
            "body_char_count": len(body),
            "source_body_state": source_body_state,
            # Final A-topic printing spine.  `theme_*` below remains the old
            # 23-concept compatibility layer and is never used as this field.
            "primary_print_topic": primary_code,
            "primary_print_topic_name": primary_name,
            "secondary_print_topics": join(secondary_codes),
            "secondary_print_topic_names": join(secondary_names),
            "candidate_primary_print_topics": join(candidate_primary_codes),
            "primary_topic_rule_ids": join(a_topic["rule_ids"]),
            "candidate_topic_rule_ids": join(a_topic["candidate_rule_ids"]),
            "primary_topic_status": a_topic["status"],
            "primary_topic_basis": a_topic["basis"],
            "primary_topic_note": a_topic["note"],
            "primary_topic_candidate_score": a_topic["candidate_score"],
            "primary_topic_tie_count": a_topic["candidate_tie_count"],
            "classification_status": a_topic["status"],
            "reading_status": reading_status,
            "evidence_basis": join([
                "source_text" if source_body_state == "text_present" else source_body_state,
                "deepseek_first_pass" if fp["deepseek_available"] else "missing_first_pass",
                "independent_review" if review else "no_independent_review",
            ]),
            "theme_primary": primary,
            "legacy_theme_primary": primary,
            "theme_secondary": join(secondary),
            "theme_all": join(concepts),
            "concept_primary": primary,
            "concept_tags": join(concepts),
            "theme_membership_count": len(concepts),
            "theme_source": t.get("source", ""),
            "theme_confidence": t.get("confidence", ""),
            "theme_audit_status": t.get("audit_status", ""),
            "theme_first_pass_status": t.get("first_pass_status", ""),
            "theme_top_score": t.get("top_score", ""),
            "theme_tie_count": t.get("tie_count", ""),
            "theme_matched_cues": t.get("matched_cues", ""),
            "source_version": "sooon-q9adg-articles-v2",
            "official_assignment_status": n.get("native_assignment_status", "unassigned"),
            "native_assignment_status": native_status,
            "official_category_count": n.get("native_category_count", "0"),
            "official_leaf_count": n.get("native_leaf_count", "0"),
            "official_category_names": join(category_names),
            "official_category_paths": join(paths),
            "native_object_paths": join(paths),
            "native_practice_paths": join(paths),
            "native_snapshot_id": join(snapshot_ids),
            "official_root_names": join(root_names),
            "official_native_kinds": join(kinds),
            "official_match_methods": join(methods),
            "official_match_confidences": join(confidences),
            "official_crosswalk_statuses": join(mapped_statuses),
            "official_crosswalk_review_decisions": join(mapped_decisions),
            "official_snapshot_ids": join(snapshot_ids),
            **fp,
            "independent_review_status": review.get("conclusion", "not_reviewed"),
            "independent_review_date": review.get("reviewed_at", ""),
            "independent_reviewer": review.get("reviewer", ""),
            "independent_review_packet": review.get("packet", ""),
            "classification_source": "article-classification-v2.csv" if aid in classification else "crosswalk_fallback",
            "evidence_state": evidence_state,
            "print_index_status": print_gate,
            "provenance_note": "主题/官方节点均为研究索引字段；正文证据与作者主张仍须按 evidence_state 审阅，不能把初读标签当作最终结论。",
        }
        rows.append(row)

    # Stable source order is the default ordering for the master file.  Topic
    # files are sorted by publication date and source ordinal for printing.
    fields = list(rows[0]) if rows else ["id"]
    args.out.mkdir(parents=True, exist_ok=True)
    master_csv = args.out / "print-research-index.csv"
    with master_csv.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    master_jsonl = args.out / "print-research-index.jsonl"
    with master_jsonl.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    by_theme = args.out / "by-topic"
    by_theme.mkdir(exist_ok=True)
    # Remove only stale generated topic files; the master index and official
    # root files are written independently below.
    for stale in by_theme.glob("*.csv"):
        stale.unlink()
    topic_counts: Counter[str] = Counter()
    for index, topic_code in enumerate(registry_order, 1):
        topic_name = registry.get(topic_code, {}).get("name", topic_code)
        members = [r for r in rows if topic_code == r["primary_print_topic"] or topic_code in (r["secondary_print_topics"].split(";") if r["secondary_print_topics"] else [])]
        topic_counts[topic_code] = len(members)
        path = by_theme / f"{index:02d}-{topic_code}-{safe_filename(topic_name)}.csv"
        out_fields = ["topic_membership_role", "source_ordinal", "id", "title", "published_date", "primary_print_topic", "primary_print_topic_name", "secondary_print_topics", "secondary_print_topic_names", "native_root_names", "native_object_paths", "native_practice_paths", "native_assignment_status", "concept_tags", "primary_topic_status", "classification_status", "reading_status", "evidence_state", "print_index_status", "url"]
        with path.open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore")
            writer.writeheader()
            for row in sorted(members, key=lambda r: (r["published_date"] or "9999-99-99", int(r["source_ordinal"]))):
                copy = dict(row)
                copy["topic_membership_role"] = "primary" if row["primary_print_topic"] == topic_code else "secondary"
                writer.writerow(copy)

    by_root = args.out / "by-official-root"
    by_root.mkdir(exist_ok=True)
    root_counts: Counter[str] = Counter()
    for index, root_name in enumerate(ROOTS, 1):
        members = [r for r in rows if root_name in (r["official_root_names"].split(";") if r["official_root_names"] else [])]
        if not members:
            continue
        root_counts[root_name] = len(members)
        path = by_root / f"{index:02d}-{safe_filename(root_name)}.csv"
        out_fields = ["source_ordinal", "id", "title", "published_date", "primary_print_topic", "primary_print_topic_name", "secondary_print_topics", "classification_status", "theme_primary", "theme_secondary", "theme_all", "official_category_names", "official_category_paths", "official_assignment_status", "official_crosswalk_statuses", "theme_audit_status", "evidence_state", "print_index_status", "url"]
        with path.open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore")
            writer.writeheader()
            for row in members:
                writer.writerow(row)

    # A Markdown manifest gives the researcher a printable table of contents;
    # the CSV files hold all filterable columns and are the authoritative list.
    md_path = args.out / "print-research-index.md"
    with md_path.open("w", encoding="utf-8") as fh:
        fh.write("# 岐伯论打印研究索引\n\n")
        fh.write("本索引是 2026-09-21 v2 语料的导航与打印分组层。原始语料、官方快照、DeepSeek 初读和既有 23 概念映射均保持只读；本文档不把初读标签升级为研究结论。\n\n")
        fh.write("## 使用方式\n\n")
        fh.write("- `print-research-index.csv`：每篇文章一行的主索引，可按 `primary_print_topic`、`secondary_print_topics`、`official_root_names`、日期、`classification_status`、`evidence_state` 和 `print_index_status` 筛选。\n")
        fh.write("- `print-research-index.jsonl`：同一主索引的 UTF-8 结构化版本。\n")
        fh.write("- `by-topic/`：按 A01–A21/A00 打印主专题输出；一篇文章只在一个主专题文件出现，也可在最多三个副专题文件出现。\n")
        fh.write("- `by-official-root/`：按素问官方一级对象输出；没有官方节点的文章不强行归类。\n\n")
        fh.write("## 总体统计\n\n")
        stats = {
            "语料文章数": len(rows),
            "主专题文章总数（每文恰好一个）": len(rows),
            "专题交叉归属总数（主+副）": sum(1 + len(r["secondary_print_topics"].split(";")) if r["secondary_print_topics"] else 1 for r in rows),
            "有官方节点文章数": sum(r["official_assignment_status"] == "confirmed" for r in rows),
            "官方未归类文章数": sum(r["official_assignment_status"] != "confirmed" for r in rows),
            "DeepSeek 初读记录数": sum(bool(r["deepseek_available"]) for r in rows),
            "初读缺失数": sum(not r["deepseek_available"] for r in rows),
            "独立复核记录数": sum(r["independent_review_status"] != "not_reviewed" for r in rows),
        }
        for key, value in stats.items():
            fh.write(f"- {key}：{value}\n")
        fh.write("\n## 按打印主专题\n\n|代码|主专题|主专题文章数|交叉归属数|文件|\n|---|---|---:|---:|---|\n")
        for index, topic_code in enumerate(registry_order, 1):
            topic_name = registry.get(topic_code, {}).get("name", topic_code)
            primary_members = [r for r in rows if r["primary_print_topic"] == topic_code]
            count = topic_counts.get(topic_code, 0)
            path = f"by-topic/{index:02d}-{topic_code}-{safe_filename(topic_name)}.csv"
            fh.write(f"|{topic_code}|{topic_name}|{len(primary_members)}|{count}|[{path}]({path})|\n")
        fh.write("\n## 按官方一级对象\n\n|官方一级对象|文章数|文件|\n|---|---:|---|\n")
        for index, root_name in enumerate(ROOTS, 1):
            count = root_counts.get(root_name, 0)
            if count:
                path = f"by-official-root/{index:02d}-{safe_filename(root_name)}.csv"
                fh.write(f"|{root_name}|{count}|[{path}]({path})|\n")
        fh.write("\n## 证据与打印闸门\n\n")
        fh.write("`print_index_status` 仅表示打印前需要做什么检查：`hold_theme_review` 表示 A 专题仍待人工复核；`hold_provisional_theme` 表示人工临时判断；`hold_first_pass_missing` 表示缺少初读；`review_before_annotation` 表示初读需重读或含图片；`index_ready_with_source_caveat` 只表示可进入打印批次导航，不代表外部事实已经核验。\n")

    native_coverage = {}
    native_coverage_path = args.reports / "native-category-coverage.json"
    if native_coverage_path.exists():
        try:
            native_coverage = json.loads(native_coverage_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            native_coverage = {}
    summary = {
        "generated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "corpus_path": str(args.v2),
        "corpus_records": len(rows),
        "master_outputs": [str(master_csv), str(master_jsonl), str(md_path)],
        "topic_files": len(list(by_theme.glob("*.csv"))),
        "official_root_files": len(list(by_root.glob("*.csv"))),
        "primary_topic_counts": {k: sum(r["primary_print_topic"] == k for r in rows) for k in registry_order},
        "topic_membership_counts": dict(topic_counts),
        "secondary_topic_counts": dict(Counter(code for r in rows for code in (r["secondary_print_topics"].split(";") if r["secondary_print_topics"] else []))),
        "classification_status_counts": dict(Counter(r["classification_status"] for r in rows)),
        "official_root_counts": dict(root_counts),
        "native_coverage": native_coverage,
        "theme_audit_status_counts": dict(Counter(r["theme_audit_status"] for r in rows)),
        "evidence_state_counts": dict(Counter(r["evidence_state"] for r in rows)),
        "print_index_status_counts": dict(Counter(r["print_index_status"] for r in rows)),
        "official_assignment_status_counts": dict(Counter(r["official_assignment_status"] for r in rows)),
        "independent_review_status_counts": dict(Counter(r["independent_review_status"] for r in rows)),
        "validation": {
            "unique_article_ids": len({r["id"] for r in rows}),
            "duplicate_article_ids": len(rows) - len({r["id"] for r in rows}),
            "theme_map_rows": len(theme_rows),
            "registry_topics": registry_order,
            "primary_topic_nonempty": sum(bool(r["primary_print_topic"]) for r in rows),
            "primary_topic_invalid": sum(r["primary_print_topic"] not in registry for r in rows),
            "secondary_topic_overlap_errors": sum(r["primary_print_topic"] in (r["secondary_print_topics"].split(";") if r["secondary_print_topics"] else []) for r in rows),
            "secondary_topic_over_three": sum(len(r["secondary_print_topics"].split(";")) > 3 for r in rows if r["secondary_print_topics"]),
            "native_summary_rows": len(native_rows),
            "first_pass_records": len(first_pass),
            "reading_records": len(reading),
            "independent_reviews": len(reviews),
            "classification_rows": len(classification),
            "rows_missing_classification": sum(r["id"] not in classification for r in rows),
            "rows_missing_theme_map": sum(r["id"] not in theme_by_id for r in rows),
            "rows_missing_native_summary": sum(r["id"] not in native_by_id for r in rows),
        },
        "note": "这是可筛选、可打印、可追溯的 A 专题导航层；官方路径和 23 概念允许多标签，主索引仍保持一文一行且主专题恰好一个。",
    }
    summary_path = args.out / "print-research-index-summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    coverage = {
        "generated_at": summary["generated_at"],
        "corpus_records": len(rows),
        "unique_ids": len({r["id"] for r in rows}),
        "duplicate_ids": len(rows) - len({r["id"] for r in rows}),
        "registry_topics": registry_order,
        "primary_topic_counts": summary["primary_topic_counts"],
        "secondary_topic_counts": summary["secondary_topic_counts"],
        "classification_status_counts": summary["classification_status_counts"],
        "official_assignment_status_counts": summary["official_assignment_status_counts"],
        "native_coverage": native_coverage,
        "validation": summary["validation"],
        "outputs": summary["master_outputs"] + [str(summary_path)],
    }
    coverage_path = args.reports / "article-classification-v2-coverage.json"
    coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"summary": str(summary_path), "coverage": str(coverage_path), "master_csv": str(master_csv), "master_jsonl": str(master_jsonl), "markdown": str(md_path), "records": len(rows), "topics": len(list(by_theme.glob("*.csv"))), "official_roots": len(list(by_root.glob("*.csv")))}, ensure_ascii=False, indent=2))
    return summary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--v2", type=Path, default=DEFAULT_V2)
    ap.add_argument("--reports", type=Path, default=DEFAULT_REPORTS)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    ap.add_argument("--crosswalk", type=Path, default=ROOT / "research-rebuild/data/print-topic-crosswalk-v2.csv")
    ap.add_argument("--legacy-routes", type=Path, default=DEFAULT_LEGACY_ROUTES)
    ap.add_argument("--classification", type=Path, default=DEFAULT_CLASSIFICATION)
    args = ap.parse_args()
    build(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
