# 打印主专题 crosswalk 与判定规则（v2）

对应配置：`research-rebuild/data/print-topic-crosswalk-v2.csv`。

本表把已有证据转换为打印主专题候选，不把任何一种证据源直接当作定稿。`native_path_prefix` 是素问官方对象—实践路径，`concept` 是已有 23 概念，`legacy_paper_route` 是第一版论文路由；A21 体育专题另由高辨识度正文线索召回，再回到全文判断。每条规则都有 `rule_id`，生成行级索引时应把命中的规则 ID 写入 `primary_topic_rule_ids` 或审计日志。

## 判定优先级

1. 已有人工决定或本轮人工复核决定；
2. 正文中心场景与官方实践路径一致的 `native_path_prefix`；
3. 第一版已有明确论文路由且原文证据仍能定位的 `legacy_paper_route`；
4. 官方对象路径和第一版路由都缺失时，23 概念只产生副专题候选；
5. 以上证据冲突、分数接近或仅命中宽泛概念时，主专题写为候选并标 `needs_human_classification`，不得用字典序强行决定；
6. A00 只表示跨域中心问题无法拆分或证据不足，不表示“没有官方分类”。官方未命中应在 `native_assignment_status` 独立记录。

## 规则字段含义

- `priority` 是同一证据层内的候选强度提示，不是文章主专题的最终置信度；
- `decision_role=primary_candidate` 表示可参与主专题竞争，`secondary_candidate` 只可进入副专题候选，`tie_breaker` 只能用于抽样和人工提示；
- `review_required=true` 表示即使命中该规则，也要看正文中心问题后才能确认；
- `notes` 记录该路径为什么过宽、为什么可能一对多，以及应回看的边界。

## 建议的机器判定实现

对每篇文章收集命中规则，并保存 `matched_rule_ids`、`candidate_primary_topics` 和 `candidate_secondary_topics`。主专题候选应按证据层分别计分，不能把不同层的字符串命中次数简单相加：

```text
manual_confirmed                -> 直接采用人工决定
native_path + 正文中心一致       -> native 候选确认
legacy_route + 旧文审计通过       -> legacy 候选确认
native_path 与 legacy_route 冲突  -> review_required / needs_human_classification
只有 concept 命中                -> 只写副专题；主专题进入 A00 待审
最高候选并列或仅宽泛路径命中      -> needs_human_classification
``` 

建议把官方路径和第一版路由视为“语义入口”，而不是在 `primary` 上继续沿用旧的字典排序。尤其是 `责任与后果`、`选择与自由`、`成本与总账` 等跨域概念，经常同时出现在多个专题，最多只能作为 tie-breaker 或副标签。

## 审计状态

主专题和官方层要分别记状态。主专题状态可取 `audited`、`manual_confirmed`、`manual_provisional`、`review_required`、`needs_human_classification`、`uncertain`。官方层继续使用 `confirmed`、`reassign_needed`、`native_unassigned_valid`、`api_or_version_gap`、`needs_image_review`、`uncertain`。

以下情况不得进入“已确认主专题”统计：

- 只有关键词 cue 或 DeepSeek provisional 标签，没有正文中心证据；
- 命中 `A00` 但没有人工说明跨域理由；
- 官方路径与第一版路由冲突且没有回看正文；
- 图片承载关键信息但 `needs_image_review`；
- 主专题来自缺失初读文章的临时决定且尚未独立复核。

## 最低验收

- 4,305 篇文章全部有一行主索引，唯一 ID 为 4,305；
- 最终字段存在 `primary_print_topic`，不能以旧 `theme_primary` 代替；
- `primary_print_topic` 为空的文章只能是显式 `A00`/待审状态，不能静默留空；
- 每个 A01–A21 及 A00 的数量都可从主索引重算；
- 每个主专题决定都能回溯至少一个 rule ID、正文证据入口或人工决定；
- 官方未命中、概念标签缺失和主专题待审分别统计，不能合并成“未分类”。

该 crosswalk 是可复现的候选生成层。正式研究结论仍须回到原始正文、逐篇精读和独立复核记录。
