# 暂定文章正文复核协议（2026-09-26 重建轮次）

本文件是本轮所有复核执行者（主线程与子代理）必须遵守的同一套规则。它由
`research-rebuild/reports/final-classification-framework-v2.md` 与
`岐伯论_完整交接_2026-09-26.md` 推出，只补充本轮可复现的判定线，不修改主框架。

## 0. 不可越界事项

- 不修改 `sooon-q9adg-articles-v2.jsonl`、旧语料、`print-topic-manual-decisions-v2.csv`、
  `article-classification-v2.csv`、`print-index/print-research-index.csv`。
- 不重新抓取，不读写 Cookie / CSRF / session。
- 不删除排除候选文章。
- 不编造未发生的审核记录、审核人或日期。
- 每篇决定必须能回到正文原句；**禁止用标题、question、关键词或图片代替正文依据**。
- 本轮的审核日期统一写 `2026-09-26`；审核人字段写自己实际使用的标签。

## 1. 输入

对每篇文章读取以下字段（`research-rebuild/reports/rebuild-20260926/pending-92-fulltext.json`
已包含全部字段，只读）：

- `text`：主语料正文，**唯一**决定主专题的正文依据；
- `question`：题面（只用于理解作者在回答什么，不构成专题依据）；
- `manual_*`：现有手工决定与历史复核注记（用于对照，不构成升级依据）；
- `index.official_*`：素问官方对象—实践路径（辅助多标签层）；
- `index.deepseek_*`：DeepSeek 首轮证据（辅助入口，不是定稿）；
- `index.concept_tags`：23 概念标签（跨文比较层，不替代主专题）。

## 2. 判定顺序

1. 正文中作者实际要回答的中心问题或行动场景；
2. 该中心问题**能否由正文本身辨认**（不是由题面或标题补足）；
3. 官方对象—实践路径指向的主要关系对象（辅助）；
4. 连续展开的证据域；
5. 标题、旧路由、机器候选只作辅助。

每篇只能有 **1 个** 打印主专题，副专题 **0–3 个**。

## 3. 升级 / 保持规则

### R1 升级为 `manual_confirmed`（必须同时满足）

- (a) 正文包含**作者自己的**中心处理：不是题面复述、不是裸引文、不是外链标题、
  不是检索指引、不是截断残句；
- (b) 该处理能把主专题唯一确定到注册表 A01–A21 / A00 之一；
- (c) 正文证据以逐字引文写入决定行（`body_evidence_quote`），引文必须能在
  `text` 中原文命中；
- (d) 本轮全文复核即为框架要求的第二次复核，无需另找历史轮次。

### R2 保持 `manual_provisional`

不满足 R1 时保持暂定，并把阻塞原因写入 `blocking_reason`，取值只能是：

| 值 | 含义 |
|---|---|
| `source_empty` | 正文为空（0 字符） |
| `source_truncated` | 正文在句中截断（明显不完整） |
| `body_is_quotation` | 正文全部或几乎全部是引文，无作者论述 |
| `body_is_pointer` | 正文是检索指引、外链标题或资料指引 |
| `body_question_mismatch` | 正文与题面明显不匹配，中心无法确定 |
| `body_too_short_for_center` | 正文过短（< 20 字），无法完成中心操作 |
| `a00_registry_gap` | 中心可辨但现有专题表确无合适入口（保留 A00 + 暂定） |

### R3 短正文阈值

正文少于 **20 个字符**时一律视为 `body_too_short_for_center`，保持暂定：
该长度的文本是残句、引语或成语，任何专题归属都必须从标题或题面引入，违反正文优先原则。

## 4. 明确禁止的暂定理由

`final-classification-framework-v2.md` 规定：**不得仅因事实主张未核验而使用临时状态**。
因此下列理由**不能**用来保持暂定，必须改为把风险写进 `risk_note`：

- “作者的技术/医学/法律/历史判断未外部核验”；
- “引文出处 / 译本未核验”；
- “作者使用怀疑、很可能等措辞”；
- “图片未审完”（图片审计与主题分类是两个独立决定）。

## 5. 副专题修订规则

- 副专题必须有正文支持；仅由审核者附加的风险语境、邻近领域联想一律删除；
- 删除时必须在 `decision_reason` 里写明删的是哪一个码、为什么正文不支持；
- 主专题不得同时出现在副专题；
- 副专题最多 3 个；原副专题若全部无正文支持，可清空为 0 个。

## 6. 每轮必须落盘的文件（写入 `research-rebuild/reports/rebuild-20260926/roundNNN/`）

1. `roundNNN-selection.csv`：本轮选择清单（沿用 live queue 列）。
2. `roundNNN-fulltext.json`：本轮正文包（只读抽取结果，含逐篇 `text`）。
3. `roundNNN-decisions.tsv`：列
   `id, title, primary, secondary, status, basis, risk_note`。
4. `roundNNN-body-evidence-audit.tsv`：列
   `id, title, source_ordinal, body_char_count, old_primary, old_secondary, old_status,
   new_primary, new_secondary, new_status, blocking_reason, body_evidence_quote,
   decision_reason, reviewer, reviewed_at`。
5. `roundNNN-revision-log.csv`：列
   `id, title, old_primary, old_secondary, old_status, new_primary, new_secondary,
   new_status, basis, risk_note, revision_source, revised_at`（只写发生变化的行）。
6. `roundNNN-report.md`：本轮说明，必须写明
   正文字符总数、确认数、保持暂定数、阻塞原因分布、主/副专题修订数、
   以及“本轮只覆盖现有正文，未追认未发表部分”的限制声明。

## 7. 复核完成后的机械校验（每轮都必须跑并记录结果）

- 每篇 `body_evidence_quote` 去掉引号/空白后，其 **≥12 字的连续片段必须能在该篇
  `text` 中原文命中**；否则该行判为 FAIL 并重做。
- `primary` / `secondary` 必须都在 `print-topic-registry-v2.csv` 的 A00–A21 内。
- `primary` 不得出现在 `secondary`。
- 每篇只能有 1 个 `primary`。
- 行数与选择清单一致，ID 集合完全相等。
- 保持 `manual_provisional` 的行必须填 `blocking_reason` 且取值在 R2 表内。
