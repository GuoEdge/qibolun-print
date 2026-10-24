# WPS / Word 工具调研与本机可用性结论

更新日期：2026-09-27
环境：OpenHarmony 平板，系统 Python 3.12.9，Node 内置可用，npm 可用，国内 npm 与 PyPI 镜像可访问。

## 结论摘要

**推荐长期主路线：Node + `docx` 库。**
**保留应急路线：本机 Python 手工 OOXML 编译器 `build_wps_docx.py`。**
**不推荐在本机继续使用：`python-docx` / `lxml` / `uv` / `html-to-docx` 托管环境。**

## 一、GitHub / 开源生态中值得关注的工具

### 1. Node `docx`

- 仓库：`https://github.com/dolanmiu/docx`
- npm：`docx`
- 用途：以 JavaScript 生成 DOCX，支持段落、样式、标题、页眉页脚、目录、图片、分节、页码等。
- 本机实测：**可用**。
- 安装：

```sh
npm install docx --registry=https://registry.npmmirror.com
```

优点：

- 纯 JavaScript，无原生 `.so` 依赖；
- 在鸿蒙平板上可直接 `require('docx')`；
- 已实测生成 DOCX，文件大小 8,829 字节，结构完整；
- 产物包含 `styles.xml`、`numbering.xml`、`settings.xml`、`fontTable.xml`、`comments.xml`、`footnotes.xml` 等；
- 比手工 OOXML 更适合复杂排版和长期维护；
- 适合将设计配置直接映射为 Word 样式和段落。

限制：

- 输出是程序化生成，复杂版式仍需 WPS 人工微调；
- 页码/目录域需要后续专门处理；
- 图片嵌入需要额外处理 media 关系。

### 2. Mammoth

- 仓库：`https://github.com/mwilliamson/python-mammoth` 及 Node 移植/相关生态
- npm：`mammoth`
- 用途：DOCX → HTML / 语义化提取。
- 本机实测：**可安装并加载成功**，但本次未做完整转换测试。
- 适合用途：
  - 从 DOCX 提取结构化内容；
  - 做 DOCX → HTML 校验；
  - 检查样式映射；
  - 反向核对生成的 DOCX 是否被正确解析。

### 3. docxtpl（python-docx-template）

- 仓库：`https://github.com/elapouya/python-docx-template`
- 用途：用 Word 模板 + Jinja2 变量批量生成 DOCX。
- 特点：模板在 Word/WPS 中做好，Python 只填充数据。
- 本机可用性：**当前不可用**，因为它依赖 `python-docx`，而 `python-docx` 依赖 `lxml`，`lxml` 原生扩展在本机报：

```text
PyModule_AddObject: symbol not found
```

- 如果未来 `lxml` 问题被解决，这是非常适合“WPS 做好模板 → 批量填充文章”的路线。
- 当前不建议投入。

### 4. rdocx（Rust 文档引擎，Python 绑定）

- 仓库：`https://github.com/tensorbee/rdocx`
- 特点：自带排版和渲染能力，不需要 Word/LibreOffice/Java/.NET。
- 本机可用性：**未验证，暂不建议**。
- 需要平台 wheel 或 Rust 工具链；当前鸿蒙环境不适合优先尝试。
- 若在 PC 或 openEuler 上，可作为高保真排版候选。

### 5. Pandoc

- 用途：Markdown / DOCX / HTML / EPUB 等格式互转。
- 本机可用性：**未安装**。
- 当前鸿蒙环境未见可用二进制。
- 在 PC/Linux 上非常适合：
  - Markdown → DOCX；
  - DOCX → HTML；
  - 批量格式转换；
  - 用 `--reference-doc` 套用 Word 模板样式。

### 6. LibreOffice Headless

- 用途：DOCX → PDF、ODT ↔ DOCX、批量转换。
- 本机可用性：**不可用**。
- 鸿蒙平板没有 LibreOffice。
- 若在 Linux/PC 上，这是 DOCX → PDF 保真度较好的方案。

### 7. WPS JS 宏 / WPS 加载项

- 用途：在 WPS 内部做批量查找替换、样式修改、导出 PDF、目录更新、页码刷新。
- 本机可用性：**取决于 WPS 鸿蒙版是否开放宏编辑器**。
- 这是本项目很值得尝试的方向，因为它可以让批量修改发生在 WPS 内部，不依赖外部 Python/Node。
- 适合后续任务：
  - 批量替换样式；
  - 批量插入分页；
  - 批量更新目录；
  - 批量导出 PDF；
  - 批量设置页眉页脚；
  - 批量清理空段落。

## 二、本机实测结果

### 可用

- Python 3.12.9：可用；
- Node：可用；
- npm：可用；
- npm 镜像 `https://registry.npmmirror.com`：可用；
- PyPI 清华/阿里/腾讯镜像：可用；
- `docx` Node 库：可安装、可加载、可生成 DOCX；
- `mammoth` Node 库：可安装、可加载；
- 手工 OOXML Python 编译器：可生成 DOCX。

### 不可用

- `uv` ELF：无法执行；
- `lxml` aarch64 wheel：原生扩展无法加载；
- `python-docx`：因 `lxml` 不可用而不可用；
- `pandoc`：未安装；
- `libreoffice`：未安装；
- openEuler Codex：用户反馈难用，已回退本机路线。

## 三、两种本机 DOCX 路线对比

| 项目 | Python 手工 OOXML | Node docx 库 |
|---|---|---|
| 依赖 | 仅标准库 | node_modules |
| 原生扩展 | 无 | 无 |
| 样式控制 | 手工写 XML，可控但繁琐 | API 封装，样式更完整 |
| 产物结构 | 16 个部件 | 22 个部件 |
| 图片嵌入 | 需手工处理 | 有 API 支持 |
| 目录/页码域 | 需手工实现 | 需额外实现但结构更完整 |
| 维护成本 | 中高 | 较低 |
| 推荐度 | 应急/零依赖 | **长期主路线** |

当前建议：

1. 长期改稿与批量生成用 **Node `docx`**；
2. 保留 `build_wps_docx.py` 作为零依赖应急生成器；
3. 不再投入 `lxml` / `uv` / `python-docx` 路线；
4. 未来若 WPS 鸿蒙版支持 JS 宏，优先把批量修改做成 WPS 内部宏。

## 四、下一步建议

1. 用 Node `docx` 重写 A21 样册生成器；
2. 建立 `QBL-*` 样式映射；
3. 加入图片嵌入；
4. 加入页眉页脚和页码域；
5. 加入目录域；
6. 在 WPS 中打开验证；
7. 确认模板后批量生成 31 个专题册和附录册；
8. 最终 PDF 交付若本机不可行，再考虑 PC/LibreOffice 或 WPS 导出。

## 五、Node docx 生成器已落地（2026-09-27）

代码位置：`research-rebuild/tools/node/`
（依赖 `docx@9.7.2`、`mammoth@1.13.0`、校验用的 `jszip` + `@xmldom/xmldom`，已装在 `tools/node/node_modules`，由 npmmirror 镜像安装）

| 文件 | 作用 |
| --- | --- |
| `build-qbl-docx.mjs` | 单册生成器（封面 / 说明 / 目录 / 正文 / 图片 / 篇末研究信息 / 笔记区 / 索引 / 页眉页脚页码） |
| `verify-docx.mjs` | 产物校验（部件完整性、XML 合法性、页码域、样式、图片、正文抽样） |
| `build-all-volumes.mjs` | 批量入口，默认 dry-run，加 `--run` 才写文件 |

### 单册生成

```sh
cd research-rebuild/tools/node
node build-qbl-docx.mjs --topic A21 --volume 1 --page A5
node build-qbl-docx.mjs --topic A15 --volume 1 --page B5 --with-images 3 --out /path/样张.docx
```

参数：

| 参数 | 默认 | 说明 |
| --- | --- | --- |
| `--topic` | 必填 | 专题代码，如 A21 |
| `--volume` | 1 | 卷号 |
| `--page` | A5 | A5 / B5 / A4 / A6 |
| `--out` | 自动 | 输出 docx 路径 |
| `--note-lines` | 4 | 篇末研究笔记最少横线数（按正文长度自动增加，最多 12） |
| `--article-break` | 1 | 每篇是否另起一页 |
| `--extra-note-pages` | 2 | 册末整页笔记页数 |
| `--seal` | 岐伯论 | 封面朱文方印文字 |
| `--limit N` | — | 只取前 N 篇（做样张） |
| `--with-images N` | — | 只取前 N 篇有图的文章（验证图片通道） |

### 产物结构（A21 实测）

- 部件 26 个，`document.xml` / `styles.xml` / `settings.xml` / `header1.xml` / `footer1.xml` 等；XML 全部解析通过
- 20 个 `QBL-*` 段落样式，东亚字体写入 `w:eastAsia`（宋体 / 微软雅黑 / 楷体）
- 分两节：前置节（封面 / 说明 / 目录）无页眉页脚；正文节带页眉页脚，页码 `start=1`
- 页脚：`— PAGE —　共 NUMPAGES 页`，`settings.xml` 打开 `updateFields`，WPS 打开后可更新域
- 页眉：左「岐伯论 · 阅读正文版」，右「专题代码　专题名　第 N 册」
- 页面：A5 8391×11906 twips；页边距 top 1021 / bottom 1134 / left 1247 / right 992 / gutter 227 / header+footer 709
- 封面朱文方印为 1×1 表格对象（红框 3pt + 朱色宋体），WPS 中可整体选中、拖动、改写
- 图片：自动解析 JPEG/PNG 原始尺寸，按版心宽度（A5 约 395px）等比缩放，图注「图 N　源序号 XXXX」
- 篇末研究信息中的原文链接写成真正的外部超链接

### 已验证产物

| 文件 | 内容 |
| --- | --- |
| `docx-output/A21-体育、运动与竞技伦理-阅读工作本-Node.docx` | 27,216 字节，5 篇，5 处超链接，8 处分页 |
| `docx-output/图片通道验证样张-A15-含图3篇.docx` | 1,694,625 字节，3 篇 35 图，36 个 media 部件，图片宽全部 ≤ 395px |

### 批量

```sh
node build-all-volumes.mjs            # dry-run：统计不写文件
node build-all-volumes.mjs --run      # 真正生成 32 册
node build-all-volumes.mjs --run --page B5 --only A21,A15
```

dry-run 实测：**32 卷（31 专题册 + 附录档案册），4303 篇，736 张图，图片原始约 119.6MB**。

注意：图片按原图嵌入，不做压缩，全量生成体积会偏大。批量前建议先决定图片处理策略（见下）。

### 待决策

1. **图片压缩**：可用本机 `~/.harmonybrew/bin/ffmpeg` 把图片统一缩到长边 1200–1600px、质量 80，预计总体积降到 1/3 左右；也可保持原图（WPS 中可再手工替换）。
2. **版式**：A5 / B5 需成杰在 WPS 中看实际排版后定；生成器已参数化，一条命令即可全量重出。
3. **页码回填**：目录与索引页码仍为「待回填」，最终排版后需在 WPS 更新域或改用自动目录。
4. **PDF 输出**：本机无 pandoc / LibreOffice，建议 WPS 导出 PDF。
