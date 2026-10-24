# 素问（sooon.ai）在线增量抓取

本目录只存放**增量**产物：在线新文章与变更文章的原始响应和规范化记录。
旧语料 `sooon-q9adg-articles.jsonl` 始终只读，本流程不修改、不覆盖它。

目录内容（默认不入库，见根目录 `.gitignore`）：

```text
raw/                            原始 GraphQL 响应，逐请求一份，含抓取时间
list-manifest.json              列表分页枚举结果（新/旧、publishedAt、updatedAt）
sooon-increment-<time>.jsonl    规范化增量记录，字段与旧语料同构
sooon-increment-<time>.stats.json  本次抓取统计与状态
.session-curl / .session-cookie 会话材料，仅本地，绝不入库、绝不打印
```

## 一、接口契约（2026-09-19 前端构建）

站点是 urql + persisted query：只接受带哈希的请求，不接受明文 GraphQL 文档。

| 用途 | operation | persisted-query 哈希 | 变量 |
|---|---|---|---|
| 文章列表（需登录） | `SourcesByPage` | `sha256:359519eb873359468dcfd369ce81bde64fde8adc3d78c6f175c49ededfb655df` | `input:{page,pageSize,sortOrder,unnotedOnly}` |
| 正文（需登录） | `SourceLexical` | `sha256:a2382b193df80a0875431821aa628d1ea2c49b7ac2b76469d18bcfa1bf0f324d` | `input:{sourceId}` |
| 元数据（匿名可读） | `SimpleSourcesByIds` | `sha256:2a2510d086d94df331d830cfb52a23d4c50f1453d8ea2a1acfaaa93844b42ade` | `input:{ids}` |

约束与已知行为：

- `pageSize` 只接受 **5/10/20/30**（服务端报错：`must be a multiple of 5`、`>=5`）。
- `sortOrder` 只接受 `NewFirst` / `NewLast` / `LongFirst` / `LongLast`（来自前端 `router` 分片）。
- 端点固定为 `https://sooon.ai/api/graphql`，需带 `x-graphql-csrf` 头（前端每次生成随机 UUID，服务端只校验存在性）。
- 明文 GraphQL 请求返回 `CANNOT_SEND_PQ_ID_AND_BODY`；哈希缺 `sha256:` 前缀返回 `PERSISTED_QUERY_NOT_IN_LIST`。
- 匿名访问 `sourcesByPage` / `homeStoryList` 返回 `Not authorized to resolve ...`；匿名读 `SourceLexical` 时 `lexical` 为 `null`。**正文增量必须使用已登录会话。**
- 站点前端重建后哈希可能整体失效；重取方式见第四节。

## 二、提供会话（三选一）

1. **Copy as cURL（推荐）**：在已登录的浏览器中打开 `https://sooon.ai`，F12 → Network → 任意一条 `graphql` 请求 → 右键 → Copy → Copy as cURL (bash)，粘贴保存为
   `research/online-increment/.session-curl`
2. **Cookie 单行**：把 `cookie:` 请求头的值单独存为 `research/online-increment/.session-cookie`
3. **环境变量**：`$env:SOOON_COOKIE = '<cookie 值>'`

脚本只输出会话的长度与 cookie 名清单，用于确认会话存在；不打印、不落盘任何凭据。
`.session-curl`、`.session-cookie` 已在 `.gitignore` 中。

## 三、运行

```powershell
# 1. 探针：验证会话、列表与正文两条链路，不写增量数据
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Probe

# 2. 枚举列表（自动在进入旧语料覆盖区时停止）
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode List

# 3. 抓正文：只抓新 id；-IncludeUpdated 时同时重抓 updatedAt 变新的旧 id
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Fetch -IncludeUpdated

# 或一次跑完
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode All
```

参数要点：`-PageSize`（5/10/20/30）、`-DelayMs`（默认 700ms，实测建议 ≥1500）、`-MaxPages`（默认 200）、
`-MaxArticles`（试跑条数上限）、`-Since yyyy-MM-dd`（覆盖增量截止线）、`-NoRaw`（不留档原始响应）、
`-NoResume`（忽略已有增量文件全量重抓；默认按 id + updatedAt 断点续抓）、
`-FullList`（枚举全部分页，不在旧语料覆盖区提前停止）、`-ManifestName`（指定清单文件名）。

完整同步流程：

```powershell
# 1. 探针（验证会话与正文权限）
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Probe

# 2. 全量枚举 + 对账（算出新增/下线/变更三类）
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode List -PageSize 30 -FullList -ManifestName list-manifest-full.json
pwsh -NoLogo -NoProfile -File .\research\scripts\reconcile_sooon_increment.ps1

# 3. 抓正文（只抓新 id 与 updatedAt 变新的旧 id，可随时中断后重跑续抓）
pwsh -NoLogo -NoProfile -File .\research\scripts\fetch_sooon_increment.ps1 -Mode Fetch -IncludeUpdated `
    -ManifestName list-manifest-full.json -DelayMs 1500

# 4. 合并多个增量文件（按 id 去重、保留 updatedAt 最新一条，产出 canonical 层）
pwsh -NoLogo -NoProfile -File .\research\scripts\merge_sooon_increment.ps1
```

实现要点（踩过的坑）：

- HTTP 层用 `curl.exe`（`max-time=30`、`connect-timeout=10`、`retry=2`、`retry-all-errors`）。
  PowerShell 的 `Invoke-WebRequest` 在服务端静默挂起连接时不遵守 `-TimeoutSec`，会在批量抓取中途永久卡死。
- cookie 通过 stdin 传给 curl 配置（`curl -K -`），不写任何临时凭据文件。
- 站点实测在约 110 次连续请求后会挂起连接；`-DelayMs 1500` 可稳定跑完 551 篇。
- 抓取可中断续跑：重跑时按已有增量文件的 `id + updatedAt` 跳过已完成条目。


## 四、字段与派生口径

增量记录与旧语料同构，共 9 个字段：
`id, url, title, question, brief, text, lexical, publishedAt, updatedAt`，
并额外附 `source` 元数据（平台、publicQuestionId、planLevel、status、是否旧语料既有、抓取时间、哈希、派生口径）。

`text` 由 `lexical` 派生：忽略 `linebreak` 节点，`root` 各子块以单个 `\n` 连接。
对旧语料 4,050 篇复算的结果是：2,757 篇逐字相同，1,292 篇**字符完全相同、仅换行位置不同**，
1 篇为子串关系。因此 `lexical` 是权威字段，`text` 只作检索与阅读用；书稿整理阶段应以 `lexical` 为准。

## 五、去重、版本差异与失败处理

- 以稳定 `id` 去重：`inCorpus=false` 记为新增；`inCorpus=true` 且 `updatedAt` 变大记为变更（需 `-IncludeUpdated`）。
- 抓取按 `MaxPages` / `MaxArticles` 设上限；`-DelayMs` 限速，不做并发。
- 出现 `Not authorized`、HTTP 401/403、或响应无法解析为 JSON 时**立即停止**，不盲目重试；
  单篇失败会记入 stats 的 `failures` 并继续下一篇。
- 重新启用前先跑 `-Mode Probe`，确认哈希与会话仍然有效。

## 六、会话失效或站点重建后如何重取哈希

1. 打开 `https://sooon.ai`，F12 → Sources，搜索 `__meta__:{hash:`；
2. 或在本站点根目录执行：
   `curl -s https://sooon.ai/ | grep -o '/assets/[^"]*\.js'` 逐个下载后检索 `sha256:`；
3. 用新哈希替换 `research/scripts/fetch_sooon_increment.ps1` 顶部的 `$Queries` 表；
4. 哈希失效的表现是 `PERSISTED_QUERY_NOT_IN_LIST`，不是 `Not authorized`。

## 七、已完成的同步

| 时间 | 在线总量 | 新增 | 下线 | updatedAt 变更 | 抓取记录 |
|---|---|---|---|---|---|
| 2026-09-19 | 4,200 | 246 | 96 | 305 | 551（合并于 `sooon-increment-merged-20260919-173305.jsonl`，状态 `PASS`） |

明细、口径分层与后续待办见 [`sync-report-2026-09-19.md`](sync-report-2026-09-19.md)；
对账机器可读结果见 `reconcile-20260919-165357.json`。

### 阅读与检查入口

| 想看什么 | 打开 |
|---|---|
| 一表总览（551 行，Excel 可按平台/日期/差异类型筛选） | `increment-index-2026-09-19.csv` |
| 246 篇新增文章全文（每 10 篇一个文件，共 25 个） | `read/新增-batch-*.md` |
| 2 篇大幅改写的新旧两版全文对照 | `read/大幅改写-新旧对照.md` |
| 13 篇小幅增删的逐条 diff、158 篇口径差异分层 | `review-packet-2026-09-19.md` |
| 96 篇在线已下线清单 | `offline-20260919-184307.csv` |
| 机器可读全量（4,296 条） | `../../sooon-q9adg-articles-v2.jsonl` |
| 版本决定台账（哪几篇用在线新版） | `version-decisions.csv` |
| 短引同步记录（版本变更导致的短引更新） | `quote-updates-2026-09-19.csv` |

在线原文页：`https://sooon.ai/s/<id>`（`id` 即索引表中的 `id` 列）；每篇的知乎／爱发电原始地址在索引表的「原始链接」列。

### 语料 v2 构成核对

```powershell
pwsh -NoLogo -NoProfile -File .\research\scripts\verify_corpus_v2.ps1
```

逐项核对：v2 行数与追加数、与前 4,050 行的一致性（版本决定替换的 2 篇单列为例外）、ID 重复与缺失、
追加记录字段完整性，以及六个派生研究层各自覆盖到哪一层。

版本决定：2 篇大幅改写按用户决定采用**在线新版**，写入 v2 时旧版保留在 `superseded` 字段；
由此影响的 1 条登记短引已同步到新版对应句，`validate_source_quotes.ps1` 对 v2 复跑为
11,978/11,978 逐字命中、状态 `PASS`。

`read/`、`review-packet-*.md`、`version-diff-*.jsonl`、`offline-*.csv`、`raw/`、`list-manifest*.json`
与 `.session-*` 均含第三方全文或凭据，已在 `.gitignore` 中排除；索引 CSV、本 README、同步报告与
`reconcile-*.json` 可以入库。

## 八、版权与交付边界

原始响应与增量全文只作本地研究输入，不入库、不公开发布；引用第三方原文的版权仍归原权利人。
整理书稿时继续区分：原文档案、逐篇导读、跨文研究重建、出版编辑文本四层。
