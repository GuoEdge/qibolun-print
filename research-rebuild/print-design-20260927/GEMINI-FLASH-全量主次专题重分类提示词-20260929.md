# Gemini Flash 全量主专题与次专题重分类提示词

版本：2026-09-29
用途：对“岐伯论”4305篇文章重新归纳主专题与次专题，允许突破现有 A01–A21 分类体系；原有 23 概念标签及其方法暂不参与本轮重分类，也不删除、不覆盖。

---

## 使用前提：唯一输入文件与安全边界

Gemini 不应在“岐伯论”文件夹里自行搜索、修改或覆盖文件。请只把下面这一个文件作为本轮文章语料输入：

```text
/storage/Users/currentUser/Documents/岐伯论/sooon-q9adg-articles-v2.jsonl
```

这是 4305 篇文章的原始 JSONL 语料，**只读使用**。每行是一篇文章，包含文章 ID、标题、提问、正文、日期及原始来源等字段。请先读取并确认该文件的总行数、字段名和唯一文章数量，再开始分析。

禁止读取或修改以下内容作为本轮分类输入：

- `/storage/Users/currentUser/Documents/岐伯论/research-rebuild/` 下的任何旧分类、旧专题、旧印刷包或旧 DOCX；
- `reports/article-classification-v2.csv`；
- `print-20260926-rebuilt-v2/`；
- `research/` 下的历史分析文件；
- 任意已有 A01–A21 分类结果；
- 原有 23 概念标签字段。

这些文件只属于旧方案和审计资料，不能作为 Gemini 发现新分类体系的依据。不要修改、删除、重命名或覆盖“岐伯论”目录中的任何原始文件。

所有 Gemini 输出只写到一个新建的、与原始资料分离的输出位置：

```text
/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/
```

建议输出文件：

```text
taxonomy-discovered.json
batch-0001.jsonl
batch-0002.jsonl
...
audit-0001.jsonl
merged-classification.jsonl
merge-report.json
run-manifest.json
```

如果 Gemini 无法直接写入上述本地路径，就只返回结果文本或可下载文件，**不要尝试在“岐伯论”目录中自行创建、移动或覆盖其它文件**。输出回来后再由宁远统一保存、校验和合并。

不要把 4305 篇文章一次性要求模型直接输出最终分类。推荐使用三阶段：

1. **阶段一：分类体系发现**——让 Gemini 从文章全文中自主归纳候选分类体系；
2. **阶段二：体系冻结后分批分类**——用阶段一确认的分类注册表，每批分类 100–300 篇；
3. **阶段三：边界复核与一致性检查**——专门检查相近专题、主次颠倒、跨域文章和低置信度文章。

每次调用都必须保留：模型版本、提示词版本、输入文件范围、批次编号、时间和原始输出。不要覆盖现有 `article-classification-v2.csv`，新结果另存为新版本。

---

# 阶段一：从全文发现新的分类体系

### 给 Gemini 的文件范围声明（建议放在提示词最前面）

```text
本轮唯一输入文件：
/storage/Users/currentUser/Documents/岐伯论/sooon-q9adg-articles-v2.jsonl

请只读这一个 JSONL 文件。不要搜索、遍历、打开、修改、删除或覆盖“岐伯论”目录中的其它文件。不要读取 research/、research-rebuild/、旧分类 CSV、旧印刷包、旧 DOCX 或任何 A01–A21/23 概念结果。

如果你无法直接读取本地路径，我会把这个 JSONL 文件作为唯一附件提供；不要要求我上传整个项目文件夹。

你的输出只需返回 JSON/JSONL 文本或下载文件，不要尝试修改本地文件。
```

将下面提示词发给 Gemini Flash，并明确要求它只读取上面指定的 `sooon-q9adg-articles-v2.jsonl`。如果 Gemini 不能直接读取本地路径，就由你把该 JSONL 文件作为唯一附件提供；不要把整个“岐伯论”文件夹作为附件，也不要让它自行搜索文件夹。阶段一可以分批提供该文件的连续片段，但必须记录每批的行号范围，不能混入旧分类文件。文章必须至少包含：稳定序号、标题、日期、原始提问、正文全文和图片/结构说明（若有）。

```text
你现在是“岐伯论”全量语料的专题体系设计者，不是简单的关键词分类器。

任务：阅读所提供的文章全文，从文章实际讨论的中心问题、冲突结构、行动场景、论证对象和作者给出的解决方式出发，自主发现一套新的“主专题—次专题”分类体系。

重要限制：
1. 不得以现有 A01–A21、A00、旧专题名、旧分类结果、旧 23 概念标签作为分类边界。
2. 不要为了继承旧系统而保留旧分类；只有当旧分类确实能解释文章群时才可以偶然得到相近名称。
3. 本轮不处理 23 概念标签，不评价旧 23 概念方法，也不要把 23 概念名称当作专题候选的默认来源。
4. 不按标题关键词、单个词、文章举例对象或提问表面词语分类。
5. 一篇文章只能有一个主专题；次专题可以有 0–3 个，但必须有正文证据支持。
6. 主专题描述“这篇文章主要在处理什么问题”，而不是“文章提到了什么”。
7. 如果文章无法可靠归入任何专题，允许输出“待审/跨域/材料不足”，但必须解释原因。
8. 不要为了让每篇文章都有漂亮标签而制造过多互相重叠的小专题。

你需要完成以下工作：

A. 先阅读全文，识别稳定重复出现的研究问题群。
B. 比较不同文章的中心问题，而不是只比较关键词。
C. 形成一套层级清楚、互斥性尽可能高、覆盖全库、适合阅读编册和研究检索的主专题体系。
D. 为每个主专题写出清晰的纳入边界、排除边界和典型文章特征。
E. 允许专题数量与旧体系不同。不要追求 21 个、23 个或任何预设数量。
F. 对专题之间最容易混淆的边界给出成对区分规则。
G. 对明显跨域的文章给出“主问题判定优先级”。

请输出 JSON，不要输出泛泛而谈的散文。结构如下：

{
  "taxonomy_version": "gemini-flash-discovered-v1",
  "taxonomy_principles": [
    "本体系按什么原则归纳",
    "主专题与次专题如何区分",
    "如何处理跨域文章"
  ],
  "topic_count": 0,
  "topics": [
    {
      "topic_code": "G01",
      "topic_name": "简洁、可理解、避免过度文学化的专题名",
      "topic_definition": "这个专题真正研究什么",
      "include_when": ["满足什么条件时归入"],
      "exclude_when": ["哪些相似文章不应归入"],
      "typical_question_patterns": ["典型提问结构，不是关键词列表"],
      "typical_argument_patterns": ["典型论证或行动建议"],
      "confusable_with": [
        {
          "other_topic_code": "G02",
          "distinction_rule": "两者如何区分"
        }
      ],
      "representative_ordinals": ["文章稳定序号"],
      "boundary_risk": "low|medium|high"
    }
  ],
  "cross_domain_rules": [
    {
      "case": "容易发生主次颠倒的文章类型",
      "primary_decision_rule": "先看什么，再看什么",
      "secondary_allowed": true,
      "explanation": "为什么"
    }
  ],
  "unclassified_policy": {
    "allowed": true,
    "labels": ["待审", "跨域", "材料不足"],
    "threshold_rule": "什么情况不能强行分类"
  },
  "taxonomy_quality_risks": [
    "本体系可能存在的风险"
  ]
}

质量要求：
- 专题名称必须能让读者大致理解，不得只用抽象哲学词或空泛名词。
- 每个专题必须有明确的“排除边界”。
- 主专题数量宁可适度增加，也不要把不同研究问题塞入过大的万能桶；但不得为了细分而让每个专题只有少量文章。
- 体系必须能容纳现实生活、伦理判断、制度实践、知识论证、技术与文明等不同类型文章，同时保持文章中心问题可解释。
- 不能根据文章数量反推专题数量；先保证概念清楚，再评估规模。
```

---

# 阶段一之后：分类注册表人工审阅要求

Gemini 输出候选体系后，不要直接进入全量分类。先检查：

1. 是否有多个专题只是换了说法；
2. 是否存在一个“其他/杂项/综合”万能桶；
3. 是否把研究对象误当成研究问题；
4. 是否把文章中的例子误当成主专题；
5. 是否把价值判断、事实描述、行动建议混成一个专题；
6. 是否有专题边界无法写出排除条件；
7. 是否有专题数量过多，导致未来纸质编册碎片化；
8. 是否有专题数量过少，导致文章中心问题被抹平；
9. 是否能从每个专题中抽取代表性文章，并解释为什么归入；
10. 是否保留了“待审/跨域/材料不足”的安全出口。

人工确认后，把 `topics` 原样冻结为唯一分类注册表。冻结后不要让 Gemini 在不同批次中自行改名、增删专题。

---

# 阶段二：使用冻结注册表分批分类

将下面提示词与“已冻结的分类注册表”一起发送给 Gemini。每批建议 100–300 篇，批次之间保持相同的提示词、注册表和输出格式。

```text
你现在是“岐伯论”文章的逐篇专题鉴别员。

你将使用一份已经冻结的主专题注册表，对本批文章进行主专题与次专题分类。

严格规则：
1. 只能使用冻结注册表中的 topic_code，禁止临时创造新专题、改写专题名或合并专题。
2. 每篇文章必须先阅读“原始提问”和“正文全文”，再判断中心问题。
3. 主专题只能有一个。
4. 次专题可以是 0–3 个；没有正文实质证据时不要添加次专题。
5. 不按标题关键词、单个名词、举例对象或文章提及次数分类。
6. 判断顺序：
   - 文章真正要回答的中心问题；
   - 文章主要冲突或行动场景；
   - 连续论证和解决方案指向；
   - 最后才参考提问中的对象和关键词。
7. 文章讨论“如何处理某对象”时，优先看它真正处理的是关系、制度、知识、身体、财富、技术、伦理还是其他核心问题。
8. 文章只是举例说明某领域时，不要把例子所在领域当作主专题。
9. 如果两个专题都很接近，必须在 `boundary_note` 中解释为何一个是主专题、另一个是次专题或为何排除。
10. 如果无法可靠判断，允许输出 `review_required`、`cross_domain` 或 `insufficient_evidence`，不得强行分类。
11. 不要使用 23 概念标签，不要输出旧 A01–A21 代码，除非它们恰好与冻结的新体系文本一致；分类依据只来自本文提供的新注册表。
12. 不修改原文，不概括成作者没有说过的观点，不把引述对象的观点当作作者本人观点。

每篇输出一个 JSON 对象，字段必须完整：
{
  "ordinal": 0,
  "id": "原始稳定 ID",
  "title": "原始标题",
  "primary_topic_code": "G01 或 review_required",
  "primary_topic_name": "注册表中的名称或待审",
  "secondary_topics": [
    {
      "topic_code": "G02",
      "topic_name": "注册表名称",
      "evidence": "正文中支持该次专题的简短证据"
    }
  ],
  "primary_reason": "为什么主专题是它，必须围绕中心问题解释",
  "boundary_note": "与最相近专题如何区分；若无冲突可写 null",
  "evidence_quotes": [
    "来自提问或正文的短摘录 1",
    "来自提问或正文的短摘录 2"
  ],
  "confidence": 0.0,
  "status": "confirmed|provisional|review_required|cross_domain|insufficient_evidence",
  "classification_flags": [
    "title_misleading|example_not_center|multiple_centers|short_text|missing_text|image_dependent|boundary_case"
  ]
}

输出要求：
- 只输出 JSONL，每行一个文章对象；
- 不要输出 Markdown 表格、解释性前言或代码围栏；
- `confidence` 是对本篇主专题判断的可信度，不是文章质量评分；
- 置信度低于 0.70 时原则上使用 `review_required` 或 `provisional`；
- 置信度高但证据摘录无法支持时，仍必须降级；
- `evidence_quotes` 不得凭空生成，必须能在提供的原文中找到或近似核对。
```

---

# 阶段三：边界复核与一致性检查

将阶段二输出和原文重新提供给 Gemini，使用下面提示词：

```text
你现在是分类质量审计员，不是重新自由分类。

请审计本批主专题与次专题结果，重点寻找：

1. 主专题是否只是按标题或关键词分类；
2. 主专题是否被文章中的例子误导；
3. 次专题是否没有正文证据；
4. 主专题和次专题是否应该互换；
5. 相同中心问题的文章是否被分成不同专题；
6. 不同中心问题的文章是否被塞进同一专题；
7. 低置信度文章是否被错误标记为 confirmed；
8. 是否存在应进入 review_required 的跨域、短文、正文缺失或图片依赖文章；
9. 分类理由是否真正引用了原文，而不是复述标签名称；
10. 同一批次内是否出现专题命名或边界理解漂移。

不得擅自创造新专题。对每篇输出：
{
  "ordinal": 0,
  "audit_result": "accept|revise_primary|revise_secondary|review_required|insufficient_evidence",
  "old_primary": "Gxx",
  "suggested_primary": "Gxx 或 null",
  "suggested_secondary": ["Gxx"],
  "reason": "必须具体说明问题",
  "evidence": ["原文证据短摘录"],
  "severity": "low|medium|high"
}

只输出 JSONL，每行一个审计对象。
```

---

# 结果合并与验收规则

## 必须保留的字段

最终新版本至少保存：

```text
ordinal
id
title
published_at
primary_topic_code
primary_topic_name
secondary_topic_codes
secondary_topic_names
primary_reason
boundary_note
evidence_quotes
confidence
status
classification_flags
batch_id
model
prompt_version
taxonomy_version
```

## 不得覆盖的旧数据

新结果另存为：

```text
research-rebuild/reports/gemini-flash-reclassification-v1/
  taxonomy-discovered.json
  batch-0001.jsonl
  batch-0002.jsonl
  ...
  audit-0001.jsonl
  merged-classification.jsonl
  merge-report.json
```

不要覆盖：

- `reports/article-classification-v2.csv`
- `reports/print-index/print-research-index.csv`
- `print-20260926-rebuilt-v2/`
- 既有 DOCX 或用户已经批注的文件

## 自动验收指标

得到 Gemini 新结果后，至少检查：

1. 是否覆盖 4305 篇且 ordinal 无重复、无缺失；
2. 每篇是否恰好一个主专题；
3. 次专题是否 0–3 个；
4. 次专题是否与主专题重复；
5. 是否出现大量 `review_required`、`cross_domain` 或 `insufficient_evidence`；
6. 每个专题的文章数是否极端失衡；
7. 是否出现万能专题或大量只有 1–2 篇的碎片专题；
8. 主专题与次专题的共现矩阵是否有明显异常；
9. 低置信度文章占比；
10. 同题/相似文章的分类一致性；
11. 每篇 `primary_reason` 是否非空且与证据摘录相符；
12. 与现有 v2 主专题的差异率，但差异率只用于审计，不用于判定谁正确。

## 比较“哪个更好”时不要只看数量

新旧方案至少从以下方面比较：

- 主专题边界是否更容易用一句话解释；
- 同一专题内文章是否真正围绕共同问题；
- 专题之间是否更少重叠；
- 次专题是否有实际研究价值而不是装饰标签；
- 低置信度和待审文章是否被诚实暴露；
- 纸质分册是否能形成有意义的阅读单元；
- 目录和索引是否更容易使用；
- 人工抽查文章时，分类理由是否能回到原文证据。

不要因为 Gemini 的新专题名称更漂亮，或专题数量更平均，就直接判定新方案更好。
```

---

# 给 Gemini Flash 的最短启动语

如果 Gemini 的上下文窗口或批处理方式不适合一次完成阶段一，可以先使用下面这段启动：

```text
不要继承我现有的文章分类。请先只做“分类体系发现”，不要给每篇文章最终分类。阅读我提供的文章全文后，自主归纳一套新的主专题—次专题体系，并为每个专题写纳入边界、排除边界、相近专题区分规则、代表文章序号和潜在风险。允许突破旧有专题数量和名称，但不能按标题关键词或文章举例对象机械分类。23 概念标签本轮不参与。请只输出可审阅的 JSON 分类注册表，等我确认注册表后，再进行分批逐篇分类。
```
