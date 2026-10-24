# A01-A21 打印主专题候选规则

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
