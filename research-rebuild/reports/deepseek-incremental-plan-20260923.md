# DeepSeek 初读缺口增量导出方案（2026-09-23）

## 目的

补齐当前权威语料中、旧版 DeepSeek 批次导出未覆盖的 9 篇文章。方案只生成独立输入批次和机械校验报告，不修改 `data/print-topic-manual-decisions-v2.csv` 或原始语料。

## 已核对的基线

- 当前原始语料：`../../sooon-q9adg-articles-v2.jsonl`
- 当前记录数：4,305；SHA-256：`CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`
- 旧 DeepSeek 输入基线：`../deepseek-batches/manifest.json`
- 旧基线记录数：4,296；批次数：609；旧语料哈希：`E8617186FB3A82FD117C790499191B0E7B14D7A0C06E084C6D91CB5C5BF6AAA4`
- 旧批次 ID 与当前语料交集为 4,296，缺失恰为 9 个新 ID；没有旧 ID 被删除或改写。

## 缺口与稳定序位

| reading ordinal | source ordinal | 标题 | 正文字符数 |
|---:|---:|---|---:|
| 4297 | 4059 | 老宋 | 879 |
| 4298 | 4058 | 无章办事 | 661 |
| 4299 | 4057 | 小骇客 | 789 |
| 4300 | 4056 | 授时郎 | 520 |
| 4301 | 4052 | 吹倒屋 | 537 |
| 4302 | 4055 | 勤行 | 1,178 |
| 4303 | 4053 | 见机行事 | 581 |
| 4304 | 4054 | 猫咬人 | 516 |
| 4305 | 4051 | 无赢的宇宙 | 1,141 |

稳定阅读序位仍按 `publishedAt` 升序、`id` 升序；因此不应把 JSONL 源行号当作阅读顺序。

## 可复现命令

在 `D:\岐伯论` 执行：

```powershell
pwsh -NoLogo -NoProfile -File .\research-rebuild\scripts\export_deepseek_incremental.ps1
pwsh -NoLogo -NoProfile -File .\research-rebuild\scripts\validate_deepseek_incremental.ps1
```

默认输出目录为：`research-rebuild/deepseek-batches-incremental-20260923/`。

导出脚本默认生成：

- `r002-b0001.jsonl`：8 篇，5,661 UTF-16 字符，reading ordinal 4297–4304；
- `r002-b0002.jsonl`：1 篇，1,141 UTF-16 字符，reading ordinal 4305；
- `manifest.json`：基线/当前哈希、ID 集、序位、批次预算和校验状态。

校验脚本生成 `validation-report.json`，当前结果为 `PASS`（基线 4,296、当前 4,305、增量 9、输出 2 批）。

## 安全闸门与风险

导出脚本在写目录前会拒绝以下情况：基线目录或批次缺失、旧 ID 在当前语料消失、任何旧文章内容改变、重复 ID、批次超出 8 篇/10,000 字预算、源序位/阅读序位/正文字符数不一致。输出目录必须为空，避免覆盖既有结果。

增量包还不是 DeepSeek 阅读结果；9 篇必须先按既有 `deepseek-v4.1-flash-full-reading.md` 逐篇生成 `article_reading` JSONL，再运行既有逐批验收。增量包的语料哈希是当前 `CDC9...`，不能直接把输出伪装成旧版 `E861...` 全量记录；完成初读后，应按增量 manifest 追加记录并重建/校验全量阅读索引。若同步抓取再次改变当前语料，必须重新运行导出和校验，不能复用旧包。

