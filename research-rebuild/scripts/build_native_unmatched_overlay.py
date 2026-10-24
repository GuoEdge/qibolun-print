#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a non-final candidate overlay for local articles absent from the
official native-category inventory.

The official edge table is deliberately left untouched.  This output is a
review queue: lexical hints and old-theme crosswalks help route reading, but
do not assert a native classification.
"""
from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
REPORTS = ROOT / "research-rebuild/reports"
TREE = REPORTS / "official-outline-tree.csv"
EDGES = REPORTS / "native-article-category-edges.csv"
THEMES = REPORTS / "article-theme-map-v2.csv"
OUT_CSV = REPORTS / "native-unmatched-candidate-overlay.csv"
OUT_JSON = REPORTS / "native-unmatched-candidate-report.json"
OUT_METHOD = REPORTS / "native-unmatched-candidate-method.md"
SEED = "qibo-native-unmatched-overlay-20260921-v1"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_corpus() -> dict[str, dict]:
    out: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                item = json.loads(line)
                out[str(item["id"])] = item
    return out


def build_tree(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_id = {r["id"]: r for r in rows}
    for row in rows:
        chain = [row]
        seen = {row["id"]}
        parent = row.get("parentId") or ""
        while parent and parent in by_id:
            if parent in seen:
                raise ValueError(f"classification tree cycle at {parent}")
            seen.add(parent)
            chain.append(by_id[parent])
            parent = by_id[parent].get("parentId") or ""
        chain.reverse()
        row["path_ids"] = "/".join(x["id"] for x in chain)
        row["path_names"] = " / ".join(x["name"] for x in chain)
        row["root_name"] = chain[0].get("name", "")
    return rows


def article_text(article: dict) -> str:
    # Keep this evidence boundary aligned with the corpus, without parsing
    # lexical JSON into a second, potentially divergent text representation.
    return "\n".join(str(article.get(k) or "") for k in ("title", "question", "brief", "text"))


def excerpt(article: dict, limit: int = 700) -> str:
    value = article_text(article).replace("\r", " ").replace("\n", " ")
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit] + ("..." if len(value) > limit else "")


def grams(value: str) -> list[str]:
    value = str(value or "").lower()
    # Chinese bigrams are useful for descriptions; ASCII words cover AI,
    # UBI, and other non-Chinese labels in the native outline.
    chinese = re.findall(r"[\u4e00-\u9fff]+", value)
    result: list[str] = []
    for block in chinese:
        if len(block) >= 2:
            result.extend(block[i : i + 2] for i in range(len(block) - 1))
    result.extend(re.findall(r"[a-z0-9][a-z0-9_-]{1,}", value))
    return result


def parse_date(value: object) -> str:
    try:
        number = float(value or 0)
        # sooon stores epoch milliseconds in this corpus.
        return datetime.fromtimestamp(number / 1000, tz=timezone.utc).date().isoformat()
    except (ValueError, TypeError, OverflowError, OSError):
        return ""


def lexical_candidates(text: str, leaves: list[dict[str, str]], limit: int = 5):
    text_lower = text.lower()
    text_terms = Counter(grams(text_lower))
    # IDF makes generic description terms less dominant than distinctive ones.
    doc_freq = Counter()
    node_terms: dict[str, Counter] = {}
    for node in leaves:
        terms = Counter(grams(f"{node.get('name', '')} {node.get('description', '')}"))
        node_terms[node["id"]] = terms
        for term in terms:
            doc_freq[term] += 1
    scored = []
    total = max(1, len(leaves))
    for node in leaves:
        name = str(node.get("name") or "").strip().lower()
        desc = str(node.get("description") or "").strip().lower()
        name_hits = text_lower.count(name) if name else 0
        # Name occurrence is a stronger routing hint than description overlap.
        score = float(name_hits * 12)
        matched: list[str] = []
        for term, count in text_terms.items():
            if term not in node_terms[node["id"]]:
                continue
            idf = math.log((total + 1) / (doc_freq[term] + 1)) + 1
            contribution = min(count, 3) * idf
            score += contribution
            if contribution >= 1.2:
                matched.append(term)
        # A direct description phrase is useful, but capped to avoid a long
        # description overpowering a more specific name match.
        desc_hits = sum(1 for term in set(grams(desc)) if len(term) > 1 and term in text_lower)
        score += min(desc_hits, 4) * 0.8
        if score > 0:
            scored.append((score, node, sorted(set(matched), key=lambda x: (-len(x), x))[:12]))
    scored.sort(key=lambda item: (-item[0], item[1].get("path_names", ""), item[1].get("id", "")))
    return scored[:limit]


def image_count(article: dict) -> int:
    lexical = article.get("lexical")
    if isinstance(lexical, dict):
        encoded = json.dumps(lexical, ensure_ascii=False)
        return len(re.findall(r"(?:image|upload|img)", encoded, flags=re.I))
    return 0


def load_first_pass() -> dict[str, tuple[str, str]]:
    """Return article_id -> (status, batch_id) from validated DeepSeek output."""
    result: dict[str, tuple[str, str]] = {}
    out_dir = ROOT / "research-rebuild/out"
    for path in sorted(out_dir.glob("*.out.jsonl")):
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                aid = str(record.get("article_id") or "")
                if not aid:
                    continue
                reading = record.get("reading") or {}
                result[aid] = ("read", str(reading.get("batch_id") or path.stem))
    return result


def main() -> None:
    corpus = load_corpus()
    old_ids = set()
    old_path = ROOT / "sooon-q9adg-articles.jsonl"
    if old_path.exists():
        with old_path.open(encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    old_ids.add(str(json.loads(line)["id"]))
    first_pass = load_first_pass()
    tree = build_tree(read_csv(TREE))
    leaves = [row for row in tree if row.get("kind") == "LeoPractice"]
    edges = read_csv(EDGES)
    native_ids = {row["article_id"] for row in edges}
    themes = {row["id"]: row for row in read_csv(THEMES)}
    unmatched = [article for aid, article in corpus.items() if aid not in native_ids]

    # The latest corpus date is evidence for a possible synchronization gap,
    # not proof: all such records remain candidate_nonfinal.
    latest_ms = max(float(x.get("publishedAt") or 0) for x in corpus.values())
    latest_date = parse_date(latest_ms)
    rows: list[dict[str, str]] = []
    for article in sorted(unmatched, key=lambda x: (float(x.get("publishedAt") or 0), str(x.get("id")))):
        aid = str(article["id"])
        text = article_text(article)
        candidates = lexical_candidates(text, leaves)
        old = themes.get(aid, {})
        scores = [round(item[0], 3) for item in candidates]
        top = scores[0] if scores else 0
        second = scores[1] if len(scores) > 1 else 0
        date = parse_date(article.get("publishedAt"))
        body_len = len(str(article.get("text") or ""))
        images = image_count(article)
        if date.startswith("2026-09"):
            date_stratum = "2026-09"
        elif date.startswith("2026-07") or date.startswith("2026-08"):
            date_stratum = "2026-07_08"
        elif date:
            date_stratum = "pre_2026-07"
        else:
            date_stratum = "unknown"
        first_pass_status, first_pass_batch = first_pass.get(aid, ("missing_first_pass", ""))
        if not candidates:
            candidate_status = "no_lexical_candidate"
        elif top >= 10 and (top - second >= 5):
            candidate_status = "high_candidate"
        else:
            candidate_status = "review_candidate"
        if date and date >= "2026-09-01":
            gap_hypothesis = "recent_sync_gap_candidate"
        elif not body_len and images:
            gap_hypothesis = "image_dependent_review"
        elif top < 4:
            gap_hypothesis = "possible_unclassified_or_weak_evidence"
        else:
            gap_hypothesis = "classification_or_version_gap_candidate"
        if not body_len and not images:
            gap_hypothesis = "empty_text_needs_source_check"
        evidence = []
        if article.get("title"):
            evidence.append("title")
        if article.get("question"):
            evidence.append("question")
        if article.get("brief"):
            evidence.append("brief")
        if body_len:
            evidence.append("body")
        if images:
            evidence.append("image")
        priority = 1 if first_pass_status == "missing_first_pass" else 2
        if not candidates or (top - second < 5):
            priority = min(priority, 2)
        if date_stratum == "2026-09":
            priority = min(priority, 2)
        if not body_len:
            priority = 1
        row = {
            "article_id": aid,
            "title": str(article.get("title") or ""),
            "publishedAt": str(article.get("publishedAt") or ""),
            "published_date_utc": date,
            "corpus_boundary": "new_v2_increment" if aid not in old_ids else "old_reused_in_v2",
            "date_stratum": date_stratum,
            "first_pass_status": first_pass_status,
            "first_pass_batch": first_pass_batch,
            "old_primary_theme": str(old.get("primary") or ""),
            "old_concepts": str(old.get("concepts") or ""),
            "official_native_status": "unmatched_local",
            "candidate_status": candidate_status,
            "gap_hypothesis": gap_hypothesis,
            "candidate_1_id": candidates[0][1]["id"] if len(candidates) > 0 else "",
            "candidate_1_path": candidates[0][1].get("path_names", "") if len(candidates) > 0 else "",
            "candidate_1_score": str(scores[0]) if len(scores) > 0 else "",
            "candidate_1_matched_terms": ";".join(candidates[0][2]) if len(candidates) > 0 else "",
            "candidate_2_id": candidates[1][1]["id"] if len(candidates) > 1 else "",
            "candidate_2_path": candidates[1][1].get("path_names", "") if len(candidates) > 1 else "",
            "candidate_2_score": str(scores[1]) if len(scores) > 1 else "",
            "candidate_2_matched_terms": ";".join(candidates[1][2]) if len(candidates) > 1 else "",
            "candidate_margin": str(round(top - second, 3)) if candidates else "",
            "body_char_count": str(body_len),
            "image_signal_count": str(images),
            "evidence_source": ";".join(evidence),
            "review_priority": str(priority),
            "evidence_excerpt": excerpt(article),
            "audit_decision": "pending_manual_read",
            "decision_note": "",
        }
        rows.append(row)

    fields = list(rows[0]) if rows else []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["gap_hypothesis"] for row in rows)
    weak = sum(1 for row in rows if row["candidate_status"] == "no_lexical_candidate")
    status_counts = Counter(row["candidate_status"] for row in rows)
    report = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "corpusRecords": len(corpus),
        "officialNativeMatchedRecords": len(native_ids & set(corpus)),
        "unmatchedLocalRecords": len(rows),
        "practiceNodesUsedForCandidates": len(leaves),
        "latestCorpusDateUtc": latest_date,
        "gapHypothesisCounts": dict(sorted(counts.items())),
        "candidateStatusCounts": dict(sorted(status_counts.items())),
        "weakOrNoLexicalCandidateCount": weak,
        "outputs": [str(OUT_CSV), str(OUT_JSON), str(OUT_METHOD)],
        "interpretation": "所有候选均为候选状态；不能据此修改官方分类边表。gap_hypothesis 只用于安排审计优先级。",
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    method = f"""# 官方未命中文章候选 overlay

生成时间：{report['generatedAt']}；固定种子：`{SEED}`。

本表针对本地语料中未出现在官方分类库存的 {len(rows)} 篇文章。官方边表保持只读；本表的 `candidate_1/2` 仅是由官方 LeoPractice 名称、描述与文章标题/提问/摘要/正文进行词面重合和逆文档频率排序得到的阅读路由提示。`candidate_status`（`high_candidate`、`review_candidate`、`no_lexical_candidate`）仍然是候选状态，不能当作已确认分类。

## 缺口假设

- `recent_sync_gap_candidate`：文章日期为 2026-09-01 以后，可能是同步时差，但仍需官方页面或下一快照核验。
- `classification_or_version_gap_candidate`：有一定词面线索，可能是分类遗漏、文章版本/ID差异或接口库存差异。
- `possible_unclassified_or_weak_evidence`：词面证据弱，需人工判断是否确实没有合适实践节点。
- `image_dependent_review` / `empty_text_needs_source_check`：正文不足，先核验图片或来源版本。

## 人工审核

审核时填写 `audit_decision`：`confirmed_candidate`、`reassign_to_existing`、`native_unassigned_valid`、`api_or_version_gap`、`needs_image_review` 或 `uncertain`。缺失首读的文章先补读，不因候选分数升格。只有人工阅读并附证据后，才可进入独立 overlay 的正式边表；不覆盖官方原始数据。
"""
    OUT_METHOD.write_text(method, encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
