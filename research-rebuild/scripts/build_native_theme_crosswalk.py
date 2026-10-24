#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build an explicit native-outline -> old 23-theme crosswalk.

This is a statistical research aid, not a replacement of either taxonomy.
Practice nodes use their matched article distributions; object nodes aggregate
their descendant practices.  Every node receives a disjoint mapping_status so
coverage and ambiguity are visible instead of hidden in a top label.
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
TREE = REPORTS / "official-outline-tree.csv"
EDGES = REPORTS / "native-article-category-edges.csv"
THEMES = REPORTS / "article-theme-map-v2.csv"
COVERAGE = REPORTS / "native-category-coverage.json"
OUT_CSV = REPORTS / "native-theme-crosswalk-200.csv"
OUT_JSON = REPORTS / "native-theme-crosswalk-report.json"
OUT_METHOD = REPORTS / "native-theme-crosswalk-method.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    tree_rows = read_csv(TREE)
    tree = {row["id"]: row for row in tree_rows}
    children: dict[str, list[str]] = defaultdict(list)
    for row in tree_rows:
        parent = row.get("parentId") or ""
        if parent:
            children[parent].append(row["id"])

    # The persisted tree is intentionally flat and ID-stable.  Derive paths
    # here so the crosswalk remains readable even if parent display names are
    # changed by a later API snapshot.
    for row in tree_rows:
        chain = [row]
        seen = {row["id"]}
        parent = row.get("parentId") or ""
        while parent and parent in tree:
            if parent in seen:
                raise ValueError(f"classification tree cycle at {parent}")
            seen.add(parent)
            chain.append(tree[parent])
            parent = tree[parent].get("parentId") or ""
        chain.reverse()
        row["path_names"] = " / ".join(x.get("name", "") for x in chain)

    themes = {row["id"]: row for row in read_csv(THEMES)}
    edges = read_csv(EDGES)
    by_category: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        by_category[edge["native_category_id"]].add(edge["article_id"])

    def descendants(node_id: str) -> list[str]:
        result = [node_id]
        for child in children.get(node_id, []):
            result.extend(descendants(child))
        return result

    rows: list[dict[str, str]] = []
    status_counts = Counter()
    kind_status = Counter()
    all_local = set()
    for node in tree_rows:
        node_ids = descendants(node["id"])
        article_ids = set().union(*(by_category.get(cid, set()) for cid in node_ids)) if node_ids else set()
        article_ids = {aid for aid in article_ids if aid in themes}
        all_local.update(article_ids)
        counts = Counter(themes[aid].get("primary", "") for aid in article_ids)
        counts.pop("", None)
        total = sum(counts.values())
        ranked = counts.most_common()
        top_theme, top_count = ranked[0] if ranked else ("", 0)
        top_purity = (top_count / total) if total else 0.0
        distinct = len(counts)

        # Mutually exclusive, deliberately conservative statuses:
        # - unmapped: no matched local evidence (includes empty practice nodes)
        # - narrow: <=2 articles, too little evidence for a stable mapping
        # - direct: a well-supported dominant old theme
        # - broad: diffuse across many themes or no theme >=40%
        # - multi: the remaining genuinely mixed nodes
        if not article_ids:
            status = "unmapped"
        elif len(article_ids) <= 2:
            status = "narrow"
        elif top_purity >= 0.70:
            status = "direct"
        elif top_purity < 0.40 or distinct >= 8:
            status = "broad"
        else:
            status = "multi"
        status_counts[status] += 1
        kind_status[(node.get("kind", ""), status)] += 1

        parent = tree.get(node.get("parentId", ""), {})
        rows.append({
            "native_node_id": node["id"],
            "native_name": node.get("name", ""),
            "native_kind": node.get("kind", ""),
            "native_parent_id": node.get("parentId", ""),
            "native_parent_name": parent.get("name", ""),
            "native_path": node.get("path_names", ""),
            "native_description": node.get("description", ""),
            "descendant_node_count": str(len(node_ids)),
            "matched_local_article_count": str(len(article_ids)),
            "old_theme_distinct_count": str(distinct),
            "old_theme_counts": ";".join(f"{name}:{count}" for name, count in ranked[:10]),
            "top_old_theme": top_theme,
            "top_old_theme_count": str(top_count),
            "top_old_theme_purity": f"{top_purity:.4f}",
            "second_old_theme": ranked[1][0] if len(ranked) > 1 else "",
            "second_old_theme_count": str(ranked[1][1]) if len(ranked) > 1 else "",
            "mapping_status": status,
            "mapping_basis": "practice_articles" if node.get("kind") == "LeoPractice" else "descendant_practice_articles",
            "review_decision": "pending_crosswalk_audit",
            "review_note": "",
        })

    fields = list(rows[0]) if rows else []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    report = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "nativeTreeNodes": len(tree_rows),
        "nativeObjectNodes": sum(1 for row in tree_rows if row.get("kind") == "LeoObject"),
        "nativePracticeNodes": sum(1 for row in tree_rows if row.get("kind") == "LeoPractice"),
        "crosswalkRows": len(rows),
        "mappingStatusCounts": dict(status_counts),
        "mappingStatusByKind": {f"{kind}:{status}": count for (kind, status), count in sorted(kind_status.items())},
        "matchedLocalArticlesUsed": len(all_local),
        "officialUnmatchedLocalArticles": coverage.get("nativeUnmatchedLocalArticles", 0),
        "officialInventoryUniqueArticles": coverage.get("nativeUniqueArticleInventory", 0),
        "officialLocalMatchRatio": coverage.get("nativeLocalMatchRatio", 0),
        "outputs": [str(OUT_CSV), str(OUT_JSON), str(OUT_METHOD)],
        "interpretation": "crosswalk 是旧23主题与官方200节点之间的证据统计，不是把两套分类强行合并为单一层级。",
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    method = f"""# 官方岐伯分类到旧 23 主题 crosswalk

生成时间：{report['generatedAt']}。本表覆盖官方分类树全部 {len(rows)} 个节点（{report['nativeObjectNodes']} 个 LeoObject、{report['nativePracticeNodes']} 个 LeoPractice）。

## 统计单位

- LeoPractice：使用该实践节点官方边表中精确命中的本地文章；
- LeoObject：汇总其所有后代实践节点的文章集合；
- 旧主题：使用 `article-theme-map-v2.csv` 的 `primary` 字段，仅作为已有研究索引，不视为官方分类的同义标签。

## 互斥映射状态

- `unmapped`：没有可用的本地命中文章证据（含空实践节点）；
- `narrow`：命中文章不超过 2 篇，证据太少，暂不建立稳定对应；
- `direct`：命中文章至少 3 篇，最高主题纯度 >= 70%；
- `broad`：主题分布很散（最高纯度 < 40%，或涉及至少 8 个旧主题）；
- `multi`：其余有两个或以上显著主题的混合节点。

## 当前统计

- 映射状态：{json.dumps(dict(status_counts), ensure_ascii=False)}
- 官方库存唯一文章：{coverage.get('nativeUniqueArticleInventory', 0)}；本地精确命中：{coverage.get('nativeLocalMatchedArticles', 0)}；本地命中率：{coverage.get('nativeLocalMatchRatio', 0)}；未命中本地文章：{coverage.get('nativeUnmatchedLocalArticles', 0)}。

`top_old_theme` 只能用于导航和抽样分层。最终研究索引仍保留官方多标签、旧 23 主题多主题和人工审计证据三层；不得依据本表直接覆盖官方边表或把一个节点压缩为单一主题。
"""
    OUT_METHOD.write_text(method, encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
