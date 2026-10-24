# 岐伯论独立重建研究集

本目录用于对 `sooon-q9adg-articles-v2.jsonl` 的独立精读、复核、分类和综合研究。原始语料只读。

自动索引不等于语义精读。只有阅读记录和独立复核记录完成后，文章才进入已理解或已复核统计。

原始初读基线为4,296条记录，SHA-256为 `E8617186FB3A82FD117C790499191B0E7B14D7A0C06E084C6D91CB5C5BF6AAA4`。该值仅对应初读底本。当前分类重建使用更新后的 `sooon-q9adg-articles-v2.jsonl`，截至2026-09-23为4,305条，SHA-256为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`；当前分类、阅读和抽样进度见 `reports/current-sync-report-20260923.md`。

`data/article-index.csv`、`data/image-inventory.csv`和`records/reading-records.jsonl`仍属于4,296篇初读基线，不能当作更新后全库已经阅读或复核的证明。原始 JSONL 保持只读。

状态必须分开解释：`text_coverage_status=complete`只表示原始提问、正文和结构已覆盖；`understanding_status=understanding_complete`表示已形成有证据定位的精读记录；`review_status=reviewed`才表示独立复核通过。图片文章在图片未核验前不得视为完整理解。

首批校准记录见 `reports/stage-001-calibration.md`。实时进度以 `reports/progress.json` 为准；只有通过机械验收的批次才计入完成，独立复核和图片复核另行记账。
