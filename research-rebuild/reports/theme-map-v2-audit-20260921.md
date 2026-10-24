# v2 主题映射审计（2026-09-21）

## 结论

当前 `article-theme-map-v2.csv` 可以作为路由草案，但不能作为正式分类结果。审计发现一个确定的 DeepSeek 覆盖缺口、一个确定的 cue 配置覆盖错误，以及若干会放大误分的宽泛关键词。原始语料未修改。

本次已按审计建议修复分类脚本并重建派生报告；下方覆盖数字是重建前的基线，重建后数字见报告末尾。

## 覆盖核对

| 项目 | 数量 | 证据 |
|---|---:|---|
| v2 语料记录 | 4,305 | `sooon-q9adg-articles-v2.jsonl`，ID 唯一 |
| DeepSeek 输出记录 | 4,296 | `research-rebuild/out/*.out.jsonl`，609 文件、ID 唯一 |
| v2 ID 在 DeepSeek 输出中 | 4,296 | 无多余 DS ID |
| v2 ID 缺失于 DeepSeek 输出 | 9 | 全部为序号 4051--4059 |
| 旧审计映射复用 | 4,050 | `source=reused_audited_map` |
| 新增记录 | 255 | `source=new_first_pass_candidate` |
| 新增且有 DS 输出 | 246 | 255 - 缺失的 9 篇 |
| 映射中 `unassigned` | 0 | 9 篇缺失 DS 的记录已有 `manual_provisional` 决定 |

缺失 ID 与标题为：`e76102ee-ccaa-52ce-9f89-963d7ff78f09`（无赢的宇宙）、`3bbdb46c-6320-5796-8650-9d1b2ce336c7`（吹倒屋）、`720a6074-5ee5-5efe-8383-97fb31a49682`（见机行事）、`dce8f994-09c1-5f06-bf02-ec18e9fa3823`（猫咬人）、`63aa2f41-076f-58b7-af53-bff5fe9e5f24`（勤行）、`e73c63c4-c40f-5ebb-bc24-6d1ce9863a8f`（授时郎）、`b3043594-20ef-5b8b-8f5b-5c7f676c207e`（小骇客）、`ad542f73-5ec1-5efe-9163-05d5e07ddaaf`（无章办事）、`423cdf0a-6e07-5795-87bf-43bbb0bc6451`（老宋）。

这 9 篇后来已依据原始 question/text/lexical 完成独立的 provisional 初读，写入 `research-rebuild/data/manual-theme-decisions-v2.csv`；因此当前映射不再将其计作 `missing_first_pass`，但仍不能视为最终分类。

## 确定的脚本错误

历史版本 `classify_v2_with_sampling.py:39` 和 `:59` 对字典 `CUES` 使用了重复键 `爱与回应`；本次已删除重复键并合并列表。后续仍应对“帮助”“关系”等宽泛词降低权重或要求关系上下文。

历史版本 `classify_v2_with_sampling.py:49` 的单字 cue `性` 会匹配任何包含该字的词；本次已删除，改用“性关系”等多字词。重建后 map 中精确单字 cue 命中数为 0。

## 低置信度与 tie 风险

在 DS 覆盖的 246 篇新增文章中，有 6 篇最高 cue 计数只有 1，且多数主题并列：`四正道`、`the rule of hope`、`掐丝镂空`、`动感光波`、`the king of games`、`好运道`。这些文章当前被强行写入最多 6 个候选主题，首主题主要由字典排序的 tie-break 决定，不应被视为主主题。建议记录 `top_score`、`tie_count`、`matched_cues`，并在 `top_score<=1` 或最高分并列时标记 `needs_human_classification`。

当前分层样本为 66 篇，均为 `audit_status=pending`。抽样规则不能证明 255 篇新增分类正确；应优先审计低分与并列记录，再扩展到各主主题至少一篇有明确证据的样本。

## 可直接执行的改进顺序

1. 9 个缺失 ID 已从原始 `question/text/lexical` 完成 provisional 初读；需在人工复核表中正式确认后，才可进入正式主题统计。
2. （已完成）合并重复的 `爱与回应` cue；删除单字 `性`，并保留 `matched_cues`、`top_score`、`tie_count` 到候选审计输出。
3. 对 `top_score<=1`、并列最高分、以及命中宽泛 cue（`为什么`、`社会`、`自然`、`安全`、`关系`、`帮助`）的文章统一标记人工复核。
4. 修正 progress method 文本为“新增255篇，其中 DS 覆盖246篇、缺失9篇”，并将 `new_unassigned` 拆成 `missing_first_pass` 与 `cue_unmatched` 两项。
5. （已完成重建）重建 map 和 sample 后再做主题统计；在抽样审计完成前继续保留 `review_required`，不把候选主主题写成正式结论。

## 修复后验证

`classify_v2_with_sampling.py` 已通过 `py_compile` 并成功重建：

- `v2_records=4305`，`reused_old_records=4050`，`new_records=255`
- `deepseek_covered_new=246`，`missing_first_pass=0`（9 篇已有 `manual_provisional`）
- `needs_human_classification=68`，`cue_unmatched=0`
- 样本 `66` 篇；另有 `theme-human-review-queue.csv` 共 81 条（含 13 条既有 provisional 决定）
- map 中 `audit_status` 明确区分 `audited`、`missing_first_pass`、`needs_human_classification`、`review_required`
- 重建后的新映射不再有精确匹配的单字 cue `性`

## 人工决定表建议

`theme-human-review-queue.csv` 提供 81 条可追溯记录，至少记录：`id`、原始 question、正文/DeepSeek 证据、候选主题、`top_score`、`tie_count`、人工主主题、保留概念、排除理由和审核者。首批应优先处理 DS 覆盖且 `top_score<=1` 的记录与 `tie_count>=3` 的记录；不能仅按当前 `primary` 自动确认。
