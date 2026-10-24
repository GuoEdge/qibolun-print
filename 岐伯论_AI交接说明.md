# 岐伯论项目：AI 接手说明

> **最新 openEuler Codex 交接包：** [岐伯论_Codex交接_2026-09-27.md](/storage/Users/currentUser/Documents/岐伯论/岐伯论_Codex交接_2026-09-27.md)。接手时先读该文件，再读完整交接文档。
>
> 当前主交接文档已更新至 [岐伯论_完整交接_2026-09-26.md](D:/岐伯论/岐伯论_完整交接_2026-09-26.md)。本文件保留为 2026-09-19 的历史说明，不能替代新交接文档；如两者数字或状态不同，以新交接文档及其证据快照为准。

更新时间：2026-09-19

这份文档供新的 AI 接手“岐伯论”项目使用。它区分三种东西：已经落盘并验证的研究成果、只读检查得到的当前状态、以及尚未完成的下一步工作。不要把研究者的跨文归纳改写成岐伯本人自称的理论，也不要把未验证的在线增量说成已经抓取。

## 1. 项目目标与研究边界

项目研究对象是公开网络上的 q9adg（岐伯）文本，目标是在可回到原文的证据上重建：

- 作者如何定义问题、作出判断、给出理由；
- 文章中明确的反驳对象、假设、条件和行动要求；
- 跨文章反复出现的概念关系、命题谱系和内部张力。

研究只呈现文本内部的作者观点。历史、法律、医学、心理、政治、科技等内容不能由 AI 用自己的外部价值判断替作者裁决。跨文概念网络、专题分类、体系名称和总体结论必须标记为“研究重建”，不能写成岐伯自称已经完成的统一教义。

证据优先级固定为：

1. `sooon-q9adg-articles.jsonl` 原始文章正文及元数据；
2. `research/close-reading/` 逐篇细读记录；
3. `research/data/author_view_evidence*.jsonl` 结构化作者视角证据层；
4. 论文、知乎稿和统计索引。

`faithfulSummary`、概念网络和专题论文是研究工具，不替代原文。遇到冲突时回到原始 JSONL，检查主体、否定范围、引述块、转折、条件和文章上下文。

## 2. 已完成的本地语料

截至本次工作区检查，根目录的旧语料包含：

- `4050` 条唯一记录；
- 文本时间约为 `2017-09-08` 至 `2026-07-16`；
- 抓取批次记录为 `2026-07-17`；
- 正文字符总量约 `4,620,564`，篇均约 `1,140.88` 字，中位数约 `883`；
- 来源包括知乎、爱发电等，原始 URL 保存在每条记录中；
- 本地完整语料的 README 记录 SHA-256：
  `5C609F734DBD7AE27C96467C9D2AAFF17C12EF2EEA500B222A7314779ED9B06E`。

本次核对得到的来源域名数量为：知乎相关域名约 `3268` 条，afdian/ifdian 约 `778` 条，另有少量其他已记录来源。具体分布应以逐条读取 JSONL 后重新统计为准，不要仅凭域名数量推断文章类型。

## 3. 现有研究成果

主要文件入口：

- `README.md`：项目总说明、许可和数据边界；
- `研究总目录.md`：总目录；
- `研究总论_内部观点重建.md`：系统总论；
- `research/README.md`：研究集说明、逐篇细读说明、论文目录和复现方法；
- `research/papers/00_研究方法与证据规范.md`：证据和归属规范；
- `research/papers/01_语料画像.md`：语料规模、时间和平台结构；
- `research/close-reading/`：4050 篇逐篇细读主体；
- `research/data/corpus_index.csv`：文章级索引；
- `research/data/author_view_evidence_clean.jsonl`：作者视角结构化证据层；
- `research/data/core_concept_dictionary.csv`：核心概念词典；
- `research/data/article_paper_route_map.csv`：文章到专题论文的导航；
- `research/data/source_quote_validation_failures.csv`：短引失败清单，当前应为空；
- `research/zhihu/`：系列总序、34 篇论文转换稿和发布清单。

目前已形成 34 篇编号研究论文、1 篇系统总论、35 篇知乎发布稿。项目 README 记录的质量状态包括：4050/4050 篇逐篇细读完成；20 套专题核心证据共 839 条；登记短引和论文直接短引均有逐字核验；论文—文章引用和文章入口审计已完成。重新运行验证脚本时，以当前文件和脚本输出为准。

## 4. 当前“素问”在线抓取状态

本章区分三件事：站点是否可访问（已复核）、首次在线增量是否完成（**已完成**）、书稿层是否已经合并（**尚未**）。

### 4.1 站点与接口（2026-09-19 复核）

1. `https://sooon.ai` 可访问，首页返回 HTTP `200`，标题“素问”。
2. `https://sooon.ai/robots.txt` 返回 HTTP `200`，内容为 `User-agent: *`、`Allow: /`。
3. 首页 `build-timestamp` 为 `1789786064982`，对应 `2026-09-19 10:47:44 +0800`，说明前端当日有更新。
4. 站点使用 urql persisted query：只接受带哈希的请求，明文查询返回 `CANNOT_SEND_PQ_ID_AND_BODY`，
   哈希缺 `sha256:` 前缀返回 `PERSISTED_QUERY_NOT_IN_LIST`。
5. 关键接口与权限：`SourcesByPage`（列表，需登录，`pageSize∈{5,10,20,30}`、
   `sortOrder∈{NewFirst,NewLast,LongFirst,LongLast}`）、`SourceLexical`（正文，需登录）、
   `SimpleSourcesByIds`（元数据，匿名可读）。无会话时列表返回 `Not authorized to resolve Query.sourcesByPage`。
   哈希表与调用方式见 `research/online-increment/README.md`。

### 4.2 首次增量同步（2026-09-19 完成）

使用用户已登录的浏览器会话（凭据只存在本地 `.session-curl`，未入库、未打印、未写入任何产物）：

- 在线全量枚举：`140` 页 × `30` 条 = `4,200` 篇；
- 对账：新增 `246`、下线 `96`、`updatedAt` 变新 `305`、未变 `3,649`；
  `4050 − 96 + 246 = 4200`，与在线总数一致；
- 抓取：`551` 条（新增 246 + 变更 305），正文合计 `617,551` 字符，字段缺失 `0`、空正文 `0`、凭据泄漏 `0`；
- 产物：`research/online-increment/` 下的 `sooon-increment-merged-20260919-173305.jsonl`、
  `raw/`（列表 140 份 + 正文 551 份）、`reconcile-20260919-165357.json`、
  报告 `sync-report-2026-09-19.md`；工具为 `research/scripts/fetch_sooon_increment.ps1`
  与 `research/scripts/reconcile_sooon_increment.ps1`、`research/scripts/merge_sooon_increment.ps1`。

### 4.3 语料 v2（2026-09-19 完成）

`research/scripts/build_corpus_v2.ps1` 产出了**语料总集** `sooon-q9adg-articles-v2.jsonl`（4,296 条，
SHA-256 `E8617186FB3A82FD117C790499191B0E7B14D7A0C06E084C6D91CB5C5BF6AAA4`，见同名 `.stats.json`）：

- 前 4,050 行从 `sooon-q9adg-articles.jsonl` **逐字节原样复制**，因此 ordinal 1—4050 与旧语料完全一致，
  既有逐篇精读、clean 作者证据层、命题索引、论文引用与短引核验全部继续有效；
- 在线新增 246 篇追加为 ordinal 4051—4296（append-only，带 `provenance` 标注），**尚未精读**；
- 305 篇 `updatedAt` 变新的文章**不改写 v2 中的旧记录**，新版正文另存
  `research/online-increment/version-diff-20260919-184307.jsonl`（含新版 `lexical`/`text`），
  因为既有 11,978 条登记短引与 891 条论文直接短引都是针对旧版正文核验的；
- 96 篇在线已下线文章的清单另存 `research/online-increment/offline-20260919-184307.csv`；
- 统计见 `sooon-q9adg-articles-v2.stats.json`：正文合计 4,885,054 字符，空正文 2 篇（图像承载），
  平台知乎 3,467 / 爱发电 829，重复 ID 0；
- 复核包 `research/online-increment/review-packet-2026-09-19.md` 按"口径差异 158 / 排版 ≤10 字 132 /
  小幅增删 11—60 字 13 / 大幅改写 >60 字 2"分层，列出逐条对照。

另有 2 篇大幅改写（《天堂有路》《生育抑郁》）按用户 2026-09-19 决定**采用在线新版**写入 v2：
旧版保存在两条记录的 `superseded` 字段中，决定台账见 `research/online-increment/version-decisions.csv`。
由此影响的 1 条登记短引已同步为新版对应句（`quote-updates-2026-09-19.csv`），
对 v2 复跑 `validate_source_quotes.ps1` 仍为 11,978/11,978 逐字命中 `PASS`；34 篇论文的直接短引未受影响。

构成核对脚本：`research/scripts/verify_corpus_v2.ps1`（行数、前缀一致性、ID 完整性、字段完整性、
六个派生研究层的覆盖率）。核对结论：新增 246 篇在 v2 总集内，但各派生层仍为 4,050 篇，新增部分待精读。

`sooon-q9adg-articles-v2.jsonl` 与 `sooon-q9adg-articles.jsonl` 同受 `.gitignore` 保护，不入库。

### 4.4 尚未完成

- v2 的 246 篇新文章未精读：`research/close-reading/`、`author_view_evidence_clean.jsonl`、
  命题索引与论文均仍只覆盖 4,050 篇，新增部分不得混入既有证据层；
- 未处理 `96` 篇下线文章与 `305` 篇版本差异的归档决策；
- 未重新统计合并后的数量、时间范围、平台分布与重复 ID；
- 增量层尚未进入逐篇精读、clean 证据层与论文引用审计流程。

任何接手 AI 都不应把“增量已抓取”说成“研究层已更新”：新文章尚未被精读，也尚未进入任何论文证据链。


## 5. 在线增量抓取的流程

接口契约已经还原并落盘（`research/online-increment/README.md`），下列第 1—3 步只在站点前端重建、
哈希失效（表现为 `PERSISTED_QUERY_NOT_IN_LIST`）时才需要重做；日常增量直接执行第 4 步起的脚本命令。

目标格式继续兼容旧 JSONL。实际落盘的字段是 9 个（旧语料本身没有 `keywords` 与 `collections`）：

```text
id, url, title, question, brief, text, lexical, publishedAt, updatedAt
```

增量记录另附 `source` 元数据（平台、publicQuestionId、planLevel、status、changeKind、
previousUpdatedAt、fetchedAt、哈希、text 派生口径）。

完整流程（每一步都已实现为脚本，不再需要手工抓包）：

```powershell
# 探针：验证会话与正文权限
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Probe
# 全量枚举
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode List -PageSize 30 -FullList -ManifestName list-manifest-full.json
# 对账：新增 / 下线 / updatedAt 变更
pwsh -NoLogo -NoProfile -File .\research\scripts\reconcile_sooon_increment.ps1
# 抓正文（断点续抓；站点约 110 次连续请求后会挂连接，-DelayMs 建议 >=1500）
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Fetch -IncludeUpdated -ManifestName list-manifest-full.json -DelayMs 1500
# 合并增量
pwsh -NoLogo -NoProfile -File .\research\scripts\merge_sooon_increment.ps1
# 构建语料 v2 与版本差异、下线清单
pwsh -NoLogo -NoProfile -File .\research\scripts\build_corpus_v2.ps1
```

边界：原始响应与增量全文只留在本地 `research/online-increment/`（含 `raw/`），不入库；
会话凭据只放 `.session-curl`（已 gitignore，脚本只报告长度与 cookie 名，不打印值）。

## 6. PowerShell 7 约定与复现

本机项目约定使用 PowerShell 7：

```powershell
pwsh -NoLogo -NoProfile -File .\research\scripts\validate_close_reading.ps1
pwsh -NoLogo -NoProfile -File .\research\scripts\build_author_view_evidence.ps1
pwsh -NoLogo -NoProfile -File .\research\scripts\validate_all_paper_direct_quotes.ps1
```

环境注意（2026-09-19 实测）：

- 若在 WSL/Linux 侧工作，本机没有 `pwsh`，需通过 Windows PowerShell 7 interop 调用：
  `/mnt/c/Program Files/PowerShell/7/pwsh.exe -NoLogo -NoProfile -File 'D:\岐伯论\research\scripts\<script>.ps1'`；
  中文输出需先设 `[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)`。
- `validate_all_paper_direct_quotes.ps1` 只有带 `-NormalizeNonExact` 时才会改写论文正文（第 71 行）；
  不带开关时是只读的（仅重写 `review/` 下两个 CSV）。
- `validate_close_reading.ps1` 只校验序号、ID 与标题覆盖，不校验批次文件名，也不校验每篇的 9 个字段是否齐全；
  索引与文件名的对应关系由 `build_close_reading_index.ps1` 负责（已改为以细读文件为准）。

不要使用 Windows PowerShell 5.1 特有假设。修改文件使用 `apply_patch`；不要通过脚本覆盖用户已有的原始语料。抓取脚本应把网络原始响应写到单独的增量目录，成功校验后再合并。


## 7. 版权、隐私与交付边界

原始第三方文章全文仅作为本地研究输入，不应未经确认直接公开发布。仓库 README 已明确不分发抓取缓存、会话凭据和可能实质性复现原文的全量中间层。后续若做打印书稿，应先确定版权和授权路径，并在出版稿中区分原文引用、研究者概括、编辑性改写和 AI 辅助文字。

不得把以下内容写入交接文档、日志或公开输出：登录 Cookie、CSRF token、API key、浏览器本地存储中的秘密或完整会话头。

## 8. 给下一 AI 的第一条任务指令

> 请先阅读 `岐伯论_AI交接说明.md`、`README.md`、`research/README.md` 和 `research/papers/00_研究方法与证据规范.md`。
> 文件统计、逐篇细读状态与在线增量均已于 2026-09-19 复核并完成（`validate_close_reading.ps1` 实跑 PASS；
> clean 层 11,978 条登记短引逐字命中；首次在线同步 246 新增 / 305 变更 / 96 下线；语料 v2 已构建，见第 4 节）。
> 因此下一步不是重新抓取，也不是重新合并，而是：
> 1）为 v2 追加的 246 篇建立逐篇精读，并单独标记它们尚未进入作者证据层与论文；
> 2）处理 `review-packet-2026-09-19.md` 里的 2 篇大幅改写与 13 篇小幅增删，记录采用哪一版；
> 3）把 96 篇下线文章登记进书稿索引，避免引用失效链接。
> 不要覆盖 `sooon-q9adg-articles.jsonl`，不要把摘要当正文，不要把跨文研究重建归给岐伯本人。
> 需要再次联网时使用 `research/scripts/fetch_sooon_increment.ps1`（先 `-Mode Probe` 验证会话），全程不输出或保存凭据。

## 9. 文档一致性状态（2026-09-19 已修复与仍待处理）

**已修复**（数字已与数据层对齐，可正常引用）：

| 位置 | 修复后 |
|---|---|
| `README.md`、`研究总目录.md` | 335,282 个汉字、591,754 个非空白字符（= `paper_inventory.csv`） |
| `README.md`、`研究总目录.md`、`research/zhihu/00_系列总序.md` | 1,250 组论文—文章引用（= `paper_citation_audit.stats.json`） |
| 同上 | 1,233 组篇名提及（= `paper_named_source_coverage_audit.stats.json`） |
| `research/当前进度与质量.md` | 知乎稿 341,976 个汉字（= `zhihu-publishing-manifest.stats.json`） |
| `research/close-reading/index.csv` | 已重建：4,050 行全部指向真实存在的批次文件（旧表 1,660 行失效） |
| `research/scripts/build_close_reading_index.ps1` | 已重写为"以细读文件为准"的索引器（旧版按固定 BatchSize 反推文件名，无法复现磁盘批次号） |

**仍待处理**：

- 仓库有 196 个文件已修改但未提交（34 篇论文、34 篇知乎稿、128 个数据文件），本交接说明与
  `research/online-increment/` 下的新文件也尚未纳入版本管理；提交前请确认"仓库 HEAD"与"当前成果"不是同一状态。
- `research/README.md` 的论文目录与数据清单尚未登记本轮新增的脚本
  （`fetch_sooon_increment.ps1`、`reconcile_sooon_increment.ps1`、`merge_sooon_increment.ps1`、`build_corpus_v2.ps1`）
  与语料 v2。
- 站点侧仍有一处口径差异需要记住：158 篇文章的在线 `lexical` 已不含开头的提问者长描述，
  而本地旧语料含之；引用这类文章的"提问语境"时应使用本地版本，不要以在线当前文本为唯一依据。

