#!/usr/bin/env python3
"""Build native-category edges and corpus coverage reports.

The raw API pages contain stable IDs and article records.  Names/descriptions
are joined from official-outline-tree.csv because one API response snapshot
contains replacement glyphs for Chinese labels while IDs remain intact.
"""
from __future__ import annotations

import csv
import glob
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "research-rebuild", "data")
RAW_DIR = os.path.join(DATA, "native-raw")
REPORTS = os.path.join(ROOT, "research-rebuild", "reports")
TREE_PATH = os.path.join(REPORTS, "official-outline-tree.csv")
CORPUS_PATH = os.path.join(ROOT, "sooon-q9adg-articles-v2.jsonl")
THEME_PATH = os.path.join(REPORTS, "article-theme-map-v2.csv")


def latest_raw() -> str:
    paths = glob.glob(os.path.join(RAW_DIR, "native-category-pages-*.json"))
    if not paths:
        raise SystemExit("没有找到 native-category-pages JSON")
    return max(paths, key=os.path.getmtime)


def load_tree():
    rows = {}
    with open(TREE_PATH, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rows[row["id"]] = row
    # Build stable root-to-node paths from the ID links.
    for row in rows.values():
        chain = []
        seen = set()
        cur = row
        while cur:
            ident = cur["id"]
            if ident in seen:
                raise ValueError(f"分类树循环: {ident}")
            seen.add(ident)
            chain.append(cur)
            pid = cur.get("parentId") or ""
            cur = rows.get(pid)
        row["path_ids"] = "/".join(reversed([x["id"] for x in chain]))
        row["path_names"] = " / ".join(reversed([x["name"] for x in chain]))
        row["root_id"] = chain[-1]["id"]
        row["root_name"] = chain[-1]["name"]
    return rows


def load_corpus():
    out = {}
    with open(CORPUS_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                out[str(item["id"])] = item
    return out


def load_themes():
    out = {}
    if not os.path.exists(THEME_PATH):
        return out
    with open(THEME_PATH, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            out[str(row["id"])] = row
    return out


def main():
    tree = load_tree()
    corpus = load_corpus()
    themes = load_themes()
    raw_path = latest_raw()
    raw = json.load(open(raw_path, encoding="utf-8"))

    # De-duplicate pages defensively.  A category can have multiple pages.
    category_items = defaultdict(dict)
    for page in raw:
        c = page.get("category") or {}
        cid = str(c.get("id", ""))
        if not cid:
            continue
        node = tree.get(cid, {})
        payload = (((page.get("response") or {}).get("data") or {}).get("leoCategorySourceList") or {})
        for item in payload.get("items") or []:
            aid = str(item.get("id", ""))
            if aid:
                category_items[cid][aid] = item

    edge_rows = []
    by_article = defaultdict(list)
    cat_counts = {}
    for cid, items in category_items.items():
        node = tree.get(cid, {"id": cid, "name": "", "parentId": "", "path_ids": cid, "path_names": "", "kind": "", "description": ""})
        cat_counts[cid] = {
            "native_category_id": cid,
            "native_category_name": node.get("name", ""),
            "native_parent_id": node.get("parentId", ""),
            "native_parent_path_ids": node.get("path_ids", cid),
            "native_parent_path_names": node.get("path_names", ""),
            "native_kind": node.get("kind", ""),
            "native_description": node.get("description", ""),
            "api_unique_article_count": len(items),
            "local_match_count": 0,
        }
        for aid, item in items.items():
            local = aid in corpus
            if local:
                cat_counts[cid]["local_match_count"] += 1
            row = {
                "article_id": aid,
                "native_category_id": cid,
                "native_category_name": node.get("name", ""),
                "native_parent_id": node.get("parentId", ""),
                "native_parent_path_ids": node.get("path_ids", cid),
                "native_parent_path_names": node.get("path_names", ""),
                "native_kind": node.get("kind", ""),
                "native_description": node.get("description", ""),
                "source_count": len(items),
                "match_method": "id_exact" if local else "not_in_local_corpus",
                "match_confidence": "confirmed" if local else "unmatched",
                "assignment_status": "confirmed" if local else "official_only",
                "snapshot_id": os.path.basename(raw_path),
                "source_url": item.get("url", ""),
                "native_title": item.get("title", ""),
                "native_question": item.get("question", ""),
                "native_published_at": item.get("publishedAt", ""),
                "native_updated_at": item.get("updatedAt", ""),
            }
            edge_rows.append(row)
            by_article[aid].append(row)

    edge_fields = [
        "article_id", "native_category_id", "native_category_name", "native_parent_id", "native_parent_path_ids",
        "native_parent_path_names", "native_kind", "native_description", "source_count", "match_method",
        "match_confidence", "assignment_status", "snapshot_id", "source_url", "native_title", "native_question",
        "native_published_at", "native_updated_at",
    ]
    edge_path = os.path.join(REPORTS, "native-article-category-edges.csv")
    with open(edge_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=edge_fields, extrasaction="ignore")
        w.writeheader(); w.writerows(sorted(edge_rows, key=lambda x: (x["article_id"], x["native_category_id"])))

    summary_rows = []
    for aid, article in corpus.items():
        edges = by_article.get(aid, [])
        leaf = [e for e in edges if e["native_kind"] == "LeoPractice"]
        roots = sorted({e["native_parent_path_names"].split(" / ")[0] for e in edges if e["native_parent_path_names"]})
        cats = sorted({e["native_category_name"] for e in edges})
        t = themes.get(aid, {})
        summary_rows.append({
            "article_id": aid, "title": article.get("title", ""), "publishedAt": article.get("publishedAt", ""),
            "native_category_count": len(cats), "native_leaf_count": len(leaf),
            "native_category_names": ";".join(cats), "native_root_names": ";".join(roots),
            "native_assignment_status": "confirmed" if leaf else ("object_only" if edges else "unassigned"),
            "old_primary_theme": t.get("primary", ""), "old_concepts": t.get("concepts", ""),
        })
    summary_fields = list(summary_rows[0].keys()) if summary_rows else []
    summary_path = os.path.join(REPORTS, "native-article-category-summary.csv")
    with open(summary_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=summary_fields); w.writeheader(); w.writerows(sorted(summary_rows, key=lambda x: x["article_id"]))

    # Category-level crosswalk: old 23-theme primary labels against native categories.
    crosswalk = []
    for cid, c in sorted(cat_counts.items(), key=lambda kv: (kv[1]["native_parent_path_names"], kv[1]["native_category_name"])):
        theme_counts = Counter(themes.get(aid, {}).get("primary", "") for aid in category_items[cid] if aid in corpus)
        theme_counts.pop("", None)
        total = sum(theme_counts.values())
        top = theme_counts.most_common(5)
        crosswalk.append({
            **c,
            "local_match_ratio": round(c["local_match_count"] / len(corpus), 6) if corpus else 0,
            "top_old_primary_themes": ";".join(f"{k}:{v}" for k, v in top),
            "top_theme": top[0][0] if top else "",
            "top_theme_count": top[0][1] if top else 0,
            "top_theme_purity": round(top[0][1] / total, 4) if total else 0,
        })
    cross_fields = list(crosswalk[0].keys()) if crosswalk else []
    cross_path = os.path.join(REPORTS, "native-category-summary.csv")
    with open(cross_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cross_fields); w.writeheader(); w.writerows(crosswalk)

    all_native = set(by_article)
    local_native = all_native & set(corpus)
    leaf_local = {aid for aid, es in by_article.items() if aid in corpus and any(e["native_kind"] == "LeoPractice" for e in es)}
    multi = {aid for aid, es in by_article.items() if aid in corpus and len(es) > 1}
    old_theme_counts = Counter(themes.get(aid, {}).get("primary", "") for aid in corpus)
    root_counts = Counter()
    root_local_counts = Counter()
    for cid, c in cat_counts.items():
        root = tree.get(cid, {}).get("root_name", "")
        root_counts[root] += len(category_items[cid])
        root_local_counts[root] += sum(1 for aid in category_items[cid] if aid in corpus)
    report = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "corpusPath": CORPUS_PATH, "corpusRecords": len(corpus), "rawSnapshot": os.path.basename(raw_path),
        "nativeTreeNodes": len(tree), "nativeObjectNodes": sum(1 for x in tree.values() if x.get("kind") == "LeoObject"),
        "nativePracticeNodes": sum(1 for x in tree.values() if x.get("kind") == "LeoPractice"),
        "nativeCategoriesWithArticles": len(category_items), "nativePages": len(raw),
        "nativeUniqueArticleInventory": len(all_native), "nativeLocalMatchedArticles": len(local_native),
        "nativeLocalMatchRatio": round(len(local_native) / len(corpus), 6) if corpus else 0,
        "nativeLocalWithLeafCategory": len(leaf_local), "nativeLocalWithLeafRatio": round(len(leaf_local) / len(corpus), 6) if corpus else 0,
        "nativeUnmatchedLocalArticles": len(set(corpus) - all_native),
        "officialOnlyArticles": len(all_native - set(corpus)),
        "nativeMultiCategoryLocalArticles": len(multi), "nativeDuplicateEdgeCount": len(edge_rows) - len(all_native),
        "oldThemePrimaryCounts": dict(old_theme_counts),
        "rootApiEdgeCounts": dict(root_counts), "rootLocalEdgeCounts": dict(root_local_counts),
        "outputs": [edge_path, summary_path, cross_path],
        "note": "source_count is the unique item count returned for the category in this snapshot; API payload exposes nextCursor but no separate sourceCount field.",
    }
    with open(os.path.join(REPORTS, "native-category-coverage.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
