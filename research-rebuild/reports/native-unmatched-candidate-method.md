# 官方未命中文章候选 overlay

生成时间：2026-09-21T15:56:47.645482+00:00；固定种子：`qibo-native-unmatched-overlay-20260921-v1`。

本表针对本地语料中未出现在官方分类库存的 616 篇文章。官方边表保持只读；本表的 `candidate_1/2` 仅是由官方 LeoPractice 名称、描述与文章标题/提问/摘要/正文进行词面重合和逆文档频率排序得到的阅读路由提示。`candidate_status`（`high_candidate`、`review_candidate`、`no_lexical_candidate`）仍然是候选状态，不能当作已确认分类。

## 缺口假设

- `recent_sync_gap_candidate`：文章日期为 2026-09-01 以后，可能是同步时差，但仍需官方页面或下一快照核验。
- `classification_or_version_gap_candidate`：有一定词面线索，可能是分类遗漏、文章版本/ID差异或接口库存差异。
- `possible_unclassified_or_weak_evidence`：词面证据弱，需人工判断是否确实没有合适实践节点。
- `image_dependent_review` / `empty_text_needs_source_check`：正文不足，先核验图片或来源版本。

## 人工审核

审核时填写 `audit_decision`：`confirmed_candidate`、`reassign_to_existing`、`native_unassigned_valid`、`api_or_version_gap`、`needs_image_review` 或 `uncertain`。缺失首读的文章先补读，不因候选分数升格。只有人工阅读并附证据后，才可进入独立 overlay 的正式边表；不覆盖官方原始数据。
