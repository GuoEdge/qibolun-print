# 素问增量同步核对（2026-09-22）

本记录只汇总现有本地文件和无会话探针结果，不包含 Cookie、CSRF 或任何会话值。

## 结论

已同步到 2026-09-21（Asia/Shanghai）当地日期，但“在线清单”本身只抓取了最新 10 页/300 条，不是全站 141 页的重新枚举。当前 v2 语料已包含 4,305 条，最大 `publishedAt` 为 2026-09-21 19:00；9 月 21 日记录 6 条。

## 证据

- `research/online-increment/list-manifest.json`
  - `fetchedAt`: `2026-09-21T22:42:50+08:00`
  - `pagesFetched`: 10，`totalPage`: 141，`itemCount`: 300，`corpusCount`: 4050
  - 清单最大 `publishedAt`: `2026-09-21 19:00:00`（当地）
  - 清单日期计数：9 月 18 日 4、19 日 1、20 日 2、21 日 6
- `research/online-increment/sooon-increment-20260921-224243.stats.json`
  - 目标/写入 9 条，全部为新文章，正文失败 0，状态 `PASS`
- `research/online-increment/sooon-increment-merged-20260921-224556.stats.json`
  - 合并 560 条增量记录，去重后 560 条，新增 255、更新 305，缺字段/空正文/坏行均 0，状态 `PASS`
- `sooon-q9adg-articles-v2.stats.json`
  - 4,305 条（旧 4,050 + 新增 255），最大 `publishedAt` 与清单一致为 2026-09-21 19:00，状态 `PASS`
- `research-rebuild/reports/native-coverage/incremental-date-audit.md`
  - 新增 255 条；其中 246 条已有 DeepSeek 初读，9 条缺初读，缺口日期为 9 月 19--21 日

## 在线工具状态

在未提供会话的情况下运行 `fetch_sooon_increment.ps1 -Mode Probe -NoRaw`，接口返回 `Not authorized to resolve Query.sourcesByPage`。这证明脚本/网络调用路径正常，但当前进程没有可用登录态；没有使用或打印 Cookie。

## 建议

1. 将当前 `sooon-q9adg-articles-v2.jsonl` 视为已覆盖至 9 月 21 日的研究基线。
2. 不要把 `list-manifest.json` 的 300 条视作全站覆盖证明；若需下线/历史完整性核对，应在登录态下使用 `-FullList` 全页枚举，并生成新清单，再单独合并增量。
3. 先补 9 条缺失 DeepSeek 初读，再进入人工主专题分类；不要因官方未命中候选直接写分类边。
4. 下一次抓取沿用 `fetch_sooon_increment.ps1` 的只读增量流程，先 Probe，再 List/Fetch/Merge；保持原始 JSONL 不变。
