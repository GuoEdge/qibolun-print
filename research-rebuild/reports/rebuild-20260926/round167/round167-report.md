# round167 正文复核报告（2026-09-26）

本报告对应落盘文件 `round167-decisions.tsv`、`round167-body-evidence-audit.tsv`、
`round167-revision-log.csv`。判定规则见 `../REVIEWER_PROTOCOL.md`，专题口径见
`../../final-classification-framework-v2.md` 第三节（主专题目录与互斥原则）与第五节（状态解释），
代码与名称以 `../../../data/print-topic-registry-v2.csv` 的 A00–A21 为准。

## 一、输入与覆盖

- 输入（只读，未修改）：`round167-selection.csv`（16 行）、`round167-fulltext.json`（16 篇，含逐篇 `text`）。
- 方法：逐篇通读 `text` 全文（不以标题、`question`、`manual_*`、`concept_tags`、`index.deepseek_*` 代替正文），
  先确定“作者实际要回答的中心问题或行动场景”，再按 R1/R2/R3 判定。
- 正文字符总数：**28,755**；单篇区间 **1,434–2,271**；16 篇 `len(text)` 与选择清单 `body_char_count` 逐篇一致。
- reviewer：`subagent+round167-body-review`；reviewed_at：`2026-09-26`。

## 二、判定结果

| 指标 | 值 |
|---|---:|
| 文章数 | 16 |
| `manual_confirmed` | **16** |
| `manual_provisional` | **0** |
| 阻塞原因分布 | 空（无暂定行，R2 表 7 个取值全部未使用） |
| 归入 A00 | 0 |
| 主专题修订 | **1** |
| 副专题修订 | **8** |
| 状态修订 | 16（全部 `manual_provisional` → `manual_confirmed`） |

16 篇均满足 R1：(a) 正文含作者自己的中心处理，非题面复述、非裸引文、非外链标题、非检索指引、非截断残句；
(b) 该处理能把主专题唯一确定到 A01–A21 之一；(c) 逐字引文已写入 `body_evidence_quote` 并通过原文命中校验；
(d) 本轮全文复核即框架要求的第二次复核。

### 决策表

| id | 标题 | primary | secondary | status |
|---|---|---|---|---|
| dbd7bab9-d695-5e8a-96b9-49ce7510e790 | 俗 | A15 | A03 | manual_confirmed |
| 777e32cf-f889-52a0-ba04-13dcc9370c4d | 开心 | A01 | A08 | manual_confirmed |
| 0b17f32e-e171-5888-9b3d-d5b1c7d3dca9 | 德雷克医生 | **A15** | A16;A07 | manual_confirmed |
| 5c7a7815-24a4-5722-b78b-83403189114f | 怀疑与猜疑 | A03 | A09;A01 | manual_confirmed |
| 5fcaadb8-9bba-5d43-9f03-0c374dfc9729 | 农村的未来 | A18 | A13;A20 | manual_confirmed |
| f371ffd1-f98c-5fcb-8109-ad183fd9df86 | 直升珠峰 | A13 | A18 | manual_confirmed |
| 2d127a86-0787-59e0-9ad0-36940d65f94e | 圣蓝 | A15 | A20;A11 | manual_confirmed |
| e07ef7cd-dbd2-571f-b8d0-39b3970e5f9a | 演员的自我修养 | A03 | A11;A18 | manual_confirmed |
| 35a66bd4-874d-57c9-89f8-16e0c4a0ee43 | 信仰是什么 | A11 | A03 | manual_confirmed |
| 0db27234-3f9b-52e8-a594-f5e3de3e9d39 | 眼神灵动 | A18 | （0 个） | manual_confirmed |
| da098d20-c643-5f18-a4ae-2fd637101811 | 汉字基准字体 | A15 | A13;A10 | manual_confirmed |
| f9d288d4-cbf7-51e0-ae6f-a7180096ce4c | 不怯场 | A16 | A03;A20 | manual_confirmed |
| 5a0bd06a-a65b-5410-9161-e4dd82420236 | 下三路 | A16 | A03;A12 | manual_confirmed |
| 44f8c341-fd3e-56d1-a321-7aa65d97043d | 讽刺 | A16 | A03 | manual_confirmed |
| c947b0a0-3a44-571d-bef7-8663f537fb19 | 能力 | A04 | A03 | manual_confirmed |
| aa50fc78-aa1c-5741-a889-ab0d28e54746 | 真正想做的事 | A01 | （0 个） | manual_confirmed |

## 三、主专题修订（1 篇）

| 文章 | 旧 → 新 | 正文依据 |
|---|---|---|
| 德雷克医生 | `A16` → `A15` | 正文自述“说实在的，真正的要害是这些文案到底是不是董自己写的”，并给出行业规范判断“编剧、导演、美术和武指才是创作团队的核心”“当明星还要抢幕后人员的功，这是行内不可容忍的缺德行为”，落点是文化生产中的署名归属与创作团队伦理，A15 更能解释文章的主要判断与冲突；网友站队、“平民明星战胜资本”的梦与舆论逆转的讨论转为副码 A16，行业组织约束（编剧工会、编剧协会封杀与诉讼）保留副码 A07。 |

## 四、副专题修订（8 篇，删除 9 个正文不支持的副码）

| 文章 | 旧副码 → 新副码 | 删除的码与理由（详见 `decision_reason`） |
|---|---|---|
| 开心 | A08;A06 → A08 | 删 A06：正文对“合群”只有“合群重不重要，这个再说”的明确搁置，全文无朋友、群体归属或亲密关系展开，A06 只由题面引入。 |
| 德雷克医生 | A07;A15 → A16;A07 | A15 升为主码、A16 转副码；A07 保留（母公司为无形资产模糊答案、文案团队、编剧协会封杀与诉讼）。 |
| 农村的未来 | A13;A20;A08 → A13;A20 | 删 A08：正文只有“经济上的优势是压倒性的”“经济结构都会几乎被取消”等效果性表述，无财富获取、消费、劳动回报或市场交换论域，属邻近领域联想。 |
| 直升珠峰 | A18;A21 → A18 | 删 A21：登山只作背景与受影响方出现，正文中心是直升机工程可行性，按 A21“仅以体育作例子、背景或比喻时仍按实际中心领域归类”的边界删除。 |
| 眼神灵动 | A03 → （清空为 0 个） | 删 A03：末段讨论跨物种表情读取与亲近度，中日文字、中国人与西班牙人的类比只是说明相似度的比喻，正文无事实、证据、定义或论证方法证据域。 |
| 讽刺 | A03;A11 → A03 | 删 A11：正文只在末尾引《道德经》与“放下屠刀，立地成佛”作格言式论据，无信仰、神、祈祷或自然法论证。 |
| 能力 | A03;A13 → A03 | 删 A13：工程制图、UML、三维建模只是表达能力的练习科目，全文无工程方案、技术路线、制造或产业论证。 |
| 真正想做的事 | A04 → （清空为 0 个） | 删 A04：正文对父母人为塑造“延迟享受”体验只作批判性举例，并明确声明“这个教育本质的问题，不是这里的主题，我们另外再谈”；“学习欣赏困难”是快感机制重建而非教育制度或能力形成论域。 |

其余 8 篇副码（俗 A03；怀疑与猜疑 A09;A01；圣蓝 A20;A11；演员的自我修养 A11;A18；信仰是什么 A03；
汉字基准字体 A13;A10；不怯场 A03;A20；下三路 A03;A12）均有正文连续段落支持，予以保留。
全部 16 行 `primary` 均未出现在 `secondary`，副码数量 0–3。

## 五、版本限制与图片状态（独立于主题判定）

- 待续/不完整标记：`信仰是什么`（“（待续）”）、`能力`（“（未完，待续）”）、`真正想做的事`（“（未完，待续）”）。
  三篇中心问题在现有正文中已可唯一确定，按 R1 确认，`risk_note` 均写明“本确认只覆盖现有可见正文，不追认未发表部分”。
- `礼` 不在本轮；本批《俗》《怀疑与猜疑》《圣蓝》《演员的自我修养》《农村的未来》《直升珠峰》《眼神灵动》
  经逐字通读未见“未完/待续”或句中截断标记，正文均以完整句收束，未按 `source_truncated` 处理。
- 图片状态（图片审计与主题分类是两个独立决定，不因图片状态改动主题，也不声称图片已审）：
  - 已复核：`农村的未来` 12 张（supports_or_direct）、`下三路` 12 张（supports_or_direct）、`汉字基准字体` 2 张（supports_or_direct）、
    `讽刺` 1 张（supports_or_direct）；`俗` 1、`德雷克医生` 1、`圣蓝` 15、`演员的自我修养` 2、`眼神灵动` 10 张为 limited。
  - pending（0 张已审）：`开心` 1、`怀疑与猜疑` 1、`直升珠峰` 3、`不怯场` 2、`能力` 10。

## 六、机械校验（对落盘文件独立复跑，脚本 `_tmp/verify167_168.py`）

| 编号 | 校验项 | 结果 | 明细 |
|---|---|---|---|
| C1 | 每行 `body_evidence_quote` 去引号/空白后 ≥12 字连续片段在该篇 `text` 原文命中 | **PASS** | 16/16；另以最长公共子串复核全部 ≥12 |
| C2 | `primary`/`secondary` 均在注册表 A00–A21 内 | **PASS** | 16/16 |
| C3 | `primary` 不出现在 `secondary` | **PASS** | 无冲突行 |
| C4 | 每篇恰好 1 个 `primary` | **PASS** | 16/16 |
| C5 | 行数与选择清单一致、ID 集合完全相等 | **PASS** | audit=16，decisions=16，selection=16，ID 集合相等 |
| C6 | 保持暂定的行必须填合法 `blocking_reason`（确认行为空） | **PASS** | 暂定 0 行，0 违规 |
| C7 | `decisions.tsv` 与 `body-evidence-audit.tsv` 逐行一致 | **PASS** | 16/16 |
| C8 | `reviewed_at` 一律 `2026-09-26`、`reviewer` 标签正确 | **PASS** | 16/16 |
| C9 | `revision-log.csv` 只含发生变化行且无遗漏 | **PASS** | 16 行 |

总体：**PASS**（无 FAIL 项）。

## 七、并行复核稿差异说明（目录内曾出现另一份同轮草稿）

本目录在 21:02 曾存在另一份 round167 报告（非本代理所写，已保全为
`_tmp/parallel-draft-round167-report.md`），其结论与本报告存在两处差异，处置如下：

- **德雷克医生**：对方为 A16→A15，与本轮复核结论一致，已采纳（见第三节）；
- **真正想做的事**：对方保留副码 A04，本报告删除。理由是正文对该议题有明确的自我排除句
  “这个教育本质的问题，不是这里的主题，我们另外再谈”，且“学习欣赏困难”属快感机制重建而
  非 A04（学校、教师、训练、读书、能力与教育制度）论域，按“副专题须有正文支持”清空为 0 个。

本目录落盘的 `round167-decisions.tsv`、`round167-body-evidence-audit.tsv`、`round167-revision-log.csv`
与本报告同属一套（`reviewer=subagent+round167-body-review`），可由 `_tmp/gen167_168.py` 确定性重放。
若并行代理再次运行其 `_tmp/r167-generate.py`，会以另一套结论覆盖上述三个文件，需由主线程择一保留。

## 八、限制声明

- 本轮只覆盖现有可见正文，未追认未发表部分；所有“待续/疑似截断”篇目均按此口径确认。
- 未修改 `round167-selection.csv`、`round167-fulltext.json`，也未修改 `sooon-q9adg-articles-v2.jsonl`、
  `sooon-q9adg-articles.jsonl`、`print-topic-manual-decisions-v2.csv`、`article-classification-v2.csv`、
  `print-index/print-research-index.csv`、`pending-92-fulltext.json` 等锁定文件。
- 作者的事实主张、引文出处与图片来源未在本轮外部核验；按框架 v2 第五节，这类风险记入 `risk_note`，
  不作为临时状态的依据。
- 本轮无“证据不足需人工复核”篇目：16 篇正文中心均可在现有正文中唯一确定。
