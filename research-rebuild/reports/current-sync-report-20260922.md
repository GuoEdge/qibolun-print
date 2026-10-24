# 岐伯论分类重建同步报告

生成时间：2026-09-22 23:12（Asia/Shanghai）

## 当前基线

- 权威语料：`sooon-q9adg-articles-v2.jsonl`
- 记录数：4,305；唯一 ID：4,305；重复 ID：0
- 最新发布时间：2026-09-21 19:00（北京时间）
- 当前 SHA-256：`CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`
- 原始 JSONL 保持只读

## 分类进度

人工决定表 `data/print-topic-manual-decisions-v2.csv` 当前 812 篇：

- `manual_confirmed`：723
- `manual_provisional`：89
- 本轮新增逐篇细读：58 篇（其中 50 篇为短文弹性批次）
- 正式打印索引：4,305 行，全部有唯一主专题入口
- 实时未人工分类队列：3,493 篇

正式索引的分类状态：

- `manual_confirmed`：723
- `manual_provisional`：89
- `audited`：313
- `review_required`：1,691
- `needs_human_classification`：1,539

结构审计结果：`pass=true`，错误 0，警告 0。该 PASS 只证明 ID、字段、专题代码、副专题上限和派生一致性，不代表全量语义细读已经完成。

## 本轮细读修正

本轮已将短文批次由 8 篇提升为目标 50 篇：正文不超过 1,000 字、无图片依赖的文章按总字数预算集中处理；长文另行限量。新增了弹性选择器 `scripts/select_live_manual_batch_v2.py`，不会将长文硬塞进短文批次。

本轮 8 篇均来自实时队列，正文完整且无图片依赖。已修正若干题面词导致的机器候选过度：

- 《situationship》：A06 主专题，A02/A01 为副专题
- 《不是缺钾》：A01 主专题，医疗设问不构成 A09 主轴
- 《三岁》：A05 主专题，法律为责任接口
- 《七岁》：A04 主专题，博物馆/标本只作触发场景，不列 A18
- 《和气生财神》：A08 主专题，战争和历史为解释副轴
- 《夺门而入》：A12 主专题，工程和古代历史为副轴

《不熟人》《situationship》《不是缺钾》《三岁》《和气生财神》《夺门而入》已确认；《热的路》《七岁》暂列 `manual_provisional`，留待边界抽样复核。

## DeepSeek 初读缺口

初读记录仍为 4,296 篇，缺口正好 9 篇，均为新增尾部文章（权威序位 4297–4305）：

`无赢的宇宙`、`吹倒屋`、`见机行事`、`猫咬人`、`勤行`、`授时郎`、`小骇客`、`无章办事`、`老宋`。

这些文章正文并非空缺，而是增量抓取后尚未重新导出 DeepSeek 批次；在正式索引中保持独立的人工/审核状态，不把机器初读缺失伪装为完成。

## 可交付文件

- 人工决定：[data/print-topic-manual-decisions-v2.csv](../data/print-topic-manual-decisions-v2.csv)
- 全量打印索引：[print-index/print-research-index.csv](print-index/print-research-index.csv)
- 全量分类索引：[article-classification-v2.csv](article-classification-v2.csv)
- 实时人工队列：[live-manual-classification-queue-v2.csv](live-manual-classification-queue-v2.csv)
- 分类框架：[final-classification-framework-v2.md](final-classification-framework-v2.md)
- 结构审计：[print-topic-structure-audit-v2.md](print-topic-structure-audit-v2.md)

## 后续动作

继续从实时队列按风险分层抽取 6–10 篇，逐篇阅读全文并记录证据短摘录；每批完成后同步人工表、重建索引、刷新审计和队列。新增 9 篇先进入人工优先队列；图片依赖和 A02/A09/A12/A19/A00 边界文章继续优先复核。
