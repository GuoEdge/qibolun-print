# 《岐伯论》分类与印刷工程

本仓库保存《岐伯论》从文章分类、编目校订、55 册结构重建，到 DOCX 排版、书脊测算、封面输出和质量校验的完整工程资料。

## 快速入口

- [当前项目状态与接续说明](当前项目状态与接续说明_2026-10-07.md)
- [全书编纂体系与结构升级说明](全书编纂体系与结构升级说明文档_2026-10-16.md)
- [55 册物理印装书脊厚度测算表](55册物理印装书脊厚度测算表.md)
- [DOCX 内容完整性审核报告](DOCX文件内容完整性审核报告_2026-10-08.md)
- [公开范围与第三方内容说明](PUBLICATION_SCOPE.md)

## 主要内容

- `卷一/` 至 `卷八/`：55 册书稿、分页报告、二维码及分册校验产物；
- `research-rebuild/reports/gemini-flash-reclassification-v1/`：当前编目总表、分册构建器、版式库、单元结构、书脊清单和排版原型；
- `research-rebuild/` 其余目录：分类复核、批量判读、图片审查、印刷样张与历史构建资料；
- 根目录脚本与报告：增量文章分类、分册调整、全量审计、DOCX 重建与完整性检查；
- `_legacy_archive_20261016/`：已归档但仍可追溯的早期脚本与书稿；
- `research/online-increment/`：在线增量的处理工具和统计记录，不含原始会话凭据。

## 当前构建链路

```bash
python3 research-rebuild/reports/gemini-flash-reclassification-v1/units/validate_units.py
python3 rebuild_all_docx.py ALL
python3 research-rebuild/reports/gemini-flash-reclassification-v1/units/verify_final_upgraded_docx.py
```

`rebuild_all_docx.py` 统一调度 `build_volume_v1.js`、`build_volume_v2.js` 和 `build_volumes_v4_v8.js`，也支持用分册代码或卷号单独构建。

构建脚本记录的是项目原始绝对路径 `/storage/Users/currentUser/Documents/岐伯论`。在其他目录复现时，需要同步调整脚本中的 `ROOT`、`BASE` 和依赖路径，或把仓库放在该路径下。

## 当前语料

构建器使用：

- `research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl`
- `research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3.jsonl`
- `research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3-clean.jsonl`

历史语料快照、重复备份、运行时缓存和会话凭据未纳入本仓库。

## 权利与许可

- `LICENSE-CODE` 适用于本仓库中的原创构建代码；
- `LICENSE-RESEARCH` 适用于原创说明与分析文本；
- 第三方文章、问答、标题、平台内容和外部链接的权利仍归原权利人，不在本仓库许可范围内。使用或再发布前请自行确认授权与适用法律。
