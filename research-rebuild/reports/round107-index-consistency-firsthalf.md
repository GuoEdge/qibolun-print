# Round107 索引一致性核验

## 范围与方法

- 决定表：`research-rebuild/reports/round107-decisions.tsv`，31 条、31 个唯一 ID。
- 索引表：`research-rebuild/reports/print-index/print-research-index.csv`，4,305 条、4,305 个唯一 ID。
- 按 `id` 对齐，逐项比较 `title`、`primary` 与 `primary_print_topic`、`secondary` 与 `secondary_print_topics`、`status` 与 `primary_topic_status`。副码比较按分号拆分后按集合比较，不受顺序影响。

## 汇总结果

| 项目 | 结果 |
|---|---:|
| 决定表条目 | 31 |
| 在索引中找到 | 31/31 |
| 标题一致 | 31/31 |
| 主码一致 | 31/31 |
| 副码集合一致 | 31/31 |
| status 一致 | 31/31 |
| 决定表重复 ID | 0 |
| 索引表重复 ID | 0 |

**结论：** `round107-decisions.tsv` 的 31 篇决定与最新 `print-research-index.csv` 在主码、副码和 status 上全部一致。

## 分半表提示

为识别中间稿漂移，另将 `round107-firsthalf-decisions.tsv` 与 `round107-secondhalf-decisions.tsv` 合并后和汇总决定表复核。31 条中有 2 条副码仍不同；主码和 status 均一致。汇总表及索引表采用的值如下：

| id | title | 分半表副码 | 汇总表/索引副码 |
|---|---|---|---|
| `7d32dc18-d43f-5b31-b663-2cc96f87ef69` | 工程师 | A18 | A12 |
| `42dc07a1-5588-5b46-b96a-5d80e842a5b4` | 泼了一身 | A09;A01 | A02;A01 |

本报告仅记录核验结果，未修改任何决定表、索引或原始语料。
