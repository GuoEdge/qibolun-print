# Round107 索引一致性核验（后半13篇）

核验日期：2026-09-24

## 输入与比对字段

- 决定表：`research-rebuild/reports/round107-secondhalf-decisions.tsv`
- Round107 全量决定表（用于31篇交叉检查）：`research-rebuild/reports/round107-decisions.tsv`
- 最新打印索引：`research-rebuild/reports/print-index/print-research-index.csv`

按 `id` 精确匹配；逐条比较决定表的 `title`、`primary`、`secondary`、`status` 与索引的 `title`、`primary_print_topic`、`secondary_print_topics`、`primary_topic_status`。另检查索引 `classification_status` 是否与决定表 `status` 一致，并检查 ID 缺失或重复。未修改原始语料或任何决定表。

## 总体结果

- Round107 全量：31/31 个 ID 唯一匹配，主码、副码、status 全部一致；标题也全部一致。
- 后半13篇：13/13 个 ID 唯一匹配，主码、副码、status 全部一致；标题也全部一致。
- 后半13篇：主码不一致 0，副码不一致 0，status 不一致 0，索引 `classification_status` 不一致 0，缺失 ID 0，重复 ID 0。
- 后半13篇 status：`manual_provisional` 2，`manual_confirmed` 11。
- 后半13篇索引 `print_index_status`：`hold_provisional_theme` 2，`index_ready_with_source_caveat` 11，与两类 status 分布对应。

## 后半13篇逐条结果

| fulltext序号 | id | title | source_ordinal | primary | secondary | status | 结果 |
|---:|---|---|---:|---|---|---|---|
| 19 | `251d8f00-f6a7-5f72-8e55-691d2f0ef223` | 拖拉机 | 3976 | A04 | A05;A01 | manual_provisional | 一致 |
| 20 | `6565e946-d35d-5651-9ba8-b4db73c846d4` | 悲观与乐观 | 3979 | A01 | A09;A03;A11 | manual_provisional | 一致 |
| 21 | `f9e70dc0-7997-5be5-9018-d7513f222741` | 越人学远射 | 3985 | A03 | A20;A12 | manual_confirmed | 一致 |
| 22 | `5fdad7e4-98d9-529e-9713-4365605c2e99` | 作为信仰的科学 | 3988 | A03 | A11;A18 | manual_confirmed | 一致 |
| 23 | `c6d37a0c-4ca1-55e6-bbe6-23a0c078ddc8` | 家里不富裕 | 3990 | A05 | A08;A04 | manual_confirmed | 一致 |
| 24 | `0e51496b-6fcf-5316-bf1f-31e45418b49c` | 艺术解读 | 3993 | A15 | A03;A11 | manual_confirmed | 一致 |
| 25 | `21424ddc-deec-5454-834c-c1fa2d9551d1` | 因果报应 | 3996 | A11 | A03;A18 | manual_confirmed | 一致 |
| 26 | `464b34c9-ffd6-5429-ad0b-5b742bc0a0b0` | 地狱这东西 | 4004 | A11 | A19;A03;A20 | manual_confirmed | 一致 |
| 27 | `ca18e138-9e1b-564a-928b-eeb0fa966c58` | 慈善 | 4007 | A08 | A11;A09 | manual_confirmed | 一致 |
| 28 | `8a49d412-0d16-53de-8b16-89f95e650b50` | 宁不畏死 | 4032 | A19 | A01;A20 | manual_confirmed | 一致 |
| 29 | `98debe38-40de-5cf4-a63d-d230bbc7af3d` | 节水呼吁 | 4034 | A18 | A16;A20 | manual_confirmed | 一致 |
| 30 | `72e97bb7-5f36-581b-885a-ad52843ff29c` | 动物的未来 | 4036 | A18 | A20;A13 | manual_confirmed | 一致 |
| 31 | `80c38b2d-3c5b-5fe9-913e-b3324a867a58` | 北方菜 | 4050 | A20 | A12;A17 | manual_confirmed | 一致 |

## 结论

当前最新 `print-research-index.csv` 已准确承载 Round107 决定表中的后13篇主题和状态，无需一致性修订。两篇暂定记录（序号19、20）在索引中同样保留为 `manual_provisional`，并对应 `hold_provisional_theme`；其余11篇均为 `manual_confirmed`，对应 `index_ready_with_source_caveat`。
