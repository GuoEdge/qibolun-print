# 23 概念标签审计结论

## 结论

23 概念层目前**不适合直接作为纸质阅读正文的文章标签**。它可以保留为后台研究候选层，但必须和已经通过逐篇通读与证据复核的概念索引区分。

## 当前数据证据

来自 `reports/article-classification-v2.csv`：

- 语料记录：4305 篇；
- `classification_status`：4298 篇 `manual_confirmed`，7 篇 `manual_provisional`；
- `reading_status`：4041 篇 `read`，255 篇 `needs_reread`，9 篇 `missing_first_pass`；
- `theme_audit_status`：4046 篇 `audited`，169 篇 `review_required`，62 篇 `needs_human_classification`，16 篇 `reviewed_needs_revision`，8 篇 `reviewed_agree`，4 篇 `manual_provisional`；
- `independent_review_status`：4271 篇 `not_reviewed`，34 篇 `reviewed_needs_revision`；
- `concept_tags`：4305 篇均非空；
- `evidence_basis` 中含 `23_concept_route` 的记录：4262 篇；
- `concept_primary` 频次最高的三项：事实与证据 1507、定义与达意 1112、能力与学习 957；三者合计 3576 篇，约 83.1%。

## 解释

这不意味着 23 概念完全没有研究价值，也不意味着所有标签都是词面命中。原分类框架要求概念标签需要正文、提问或复核证据支持，并把 23 概念定义为跨对象研究层。

但当前全量数据同时显示：

1. 概念路由几乎覆盖全库；
2. 概念层独立复核尚未完成；
3. 概念主项高度集中在三个宽概念；
4. `classification_status` 的确认并不等于概念层单独完成通读复核；
5. `independent_review_status` 几乎全库仍未复核。

因此，当前概念字段更准确的称呼应是：**机器/规则辅助生成、部分人工校验的跨文研究候选标签**，而不是已经完成理论界定的作者思想标签。

## 纸质版处理

普通阅读正文中暂不显示：

- 23 概念标签；
- `concept_primary`；
- UUID / 数据库源 ID；
- 长原文 URL。

普通篇末只显示：

- 四位文章短号；
- 原文二维码；
- 日期；
- 主专题；
- 必要的副专题或官方路径简写；
- 必要异常状态。

## 未来重建的最低标准

若未来恢复概念索引，必须为每个概念建立：

- 操作性定义；
- 纳入条件；
- 排除条件；
- 正例与反例；
- 证据段落；
- 相近概念区分；
- `confirmed / candidate / rejected / not_reviewed` 状态；
- 审核者与日期。

只有 `confirmed` 才能进入“已核验概念索引”；`candidate` 只能进入工作台或候选附录，不得在纸质正文中制造确定性印象。
