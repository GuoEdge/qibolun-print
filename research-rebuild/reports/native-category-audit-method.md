# 官方岐伯分类抽样审计

生成日期：2026-09-21；固定种子：qibo-native-outline-20260921-v1。

## 目的

官方分类（与谁或什么对象发生何种实践）与既有 23 主题（文章处理何种跨域研究问题）是两个不同维度。此审计只检查官方分类的覆盖、节点一致性与边界，不把官方标签直接替换旧主题，也不把词面候选当成语义结论。

## 抽样层

- category_coverage：每个有文章的官方 LeoPractice 节点至少 1 篇。
- category_high_frequency：15 个高频节点各取最多 3 篇。
- native_unassigned：本地语料未出现在官方库存的文章取约 10%（至少 60 篇）。
- native_multi_category：官方多标签文章取 30 篇。
- theme_divergence：官方节点内旧主题最高占比低于 60% 的节点抽取 40 篇。
- old_theme_unassigned：旧主题为空的文章全部纳入。

## 审核字段

evidence_excerpt 是提问与正文的短摘录；candidate_native_categories_nonfinal 仅由词面重合生成，不能替代阅读。人工审核填写：

- confirmed：官方标签与文章实际实践关系一致；
- reassign_needed：应改到已有官方节点；
- native_unassigned_valid：官方确实没有合适节点；
- api_or_version_gap：疑似官方接口库存、下线或 ID 版本差异；
- needs_image_review：正文不足，必须核验图片；
- uncertain：证据不足，暂不决定。

## 当前覆盖事实

本地语料 4305 篇；官方树 200 节点，其中 LeoPractice 152 个；有文章的实践节点 140 个，空实践节点 12 个；本地命中 3689 篇，未命中 616 篇；抽样队列 254 篇。

## 研究结构

最终索引保留三列：官方岐伯分类（多标签）、旧 23 主题（多主题）、审计状态与证据。官方分类用于对象—实践导航，旧主题用于跨对象比较；未经审计的候选不得进入定稿结论。
