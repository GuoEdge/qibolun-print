// 岐伯論 · 卷一 · 甲冊（B01）── 以《现代学者批校手卷本》原型版式为唯一参照
// 原型文件只读参考，绝不修改。封面与目录为无页码前置节；正文另起节从第一叶编号。
// 正文页脚距 600 twips；后处理关闭网格吸附并保留正文节的页码起点。
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Footer, PageNumber, AlignmentType, SectionType
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');
const L = require('./lib_qibo_layout.js');
const X = require('./extract_qibo_content.js');

const OUT_DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/';
const QR_DIR = path.join(OUT_DIR, 'qr_cache_b01');
const MERGED_CORPUS = path.join(OUT_DIR, 'all-articles-merged-v3.jsonl');
const CATALOG_PATH = path.join(OUT_DIR, 'workbook-40b-all-catalog.jsonl');

const F = L.FONTS, C = L.COLORS, M = L.METRICS;

const CTX = {
  volPrefix: '本根敦倫',
  volFull: '本根敦倫 —— 血親宗族與家庭撫育',
  stem: '甲',
  bookletTrad: '幼兒啟蒙與性情習慣'
};

/* 读取编目与语料 */
const b01 = [];
for (const l of fs.readFileSync(CATALOG_PATH, 'utf-8').split('\n')) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  if (d.booklet_code === 'B01') b01.push(d);
}
const corpus = {};
for (const l of fs.readFileSync(MERGED_CORPUS, 'utf-8').split('\n')) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  corpus[d.id] = d;
}
// 从 lexical 结构分离「岐伯回答」与「提问者叙述」，替代拍扁的 text 字段
const arts = b01.map(c => {
  const rec = corpus[c.original_id] || {};
  const content = X.resolveContent(rec);
  return { ...c, answer: content.answer, narrative: content.narrative };
});
arts.forEach(a => a.charCount = ((a.answer || '').length + (a.narrative || '').length));

const frontMatter = [];
const docElements = [];

/* 扉页 + 目录：独立无页码节 */
frontMatter.push(L.buildCover({
  volName: '【 卷  一 】 本 根 敦 倫',
  bookletLabel: '甲冊 · 幼兒啟蒙與性情習慣',
  subLine: '全冊通收五十二篇 · 研讀批校工作本'
}));
// 封面背面留空：第二个物理页完全空白，目录从第三页正面开始。
frontMatter.push(new Paragraph({
  pageBreakBefore: true, spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: []
}));
frontMatter.push(L.breakPara());

let bodyPageCount = 0, overflow = 0;
const report = [];

for (const art of arts) {
  const chineseDate = L.toChineseDate(art.published_at);
  const qrPngPath = path.join(QR_DIR, 'qr_' + art.workbook_ordinal + '.png');
  const answerParas = (art.answer || '').trim().split('\n').map(s => s.trim()).filter(Boolean);
  const narrativeParas = (art.narrative || '').trim().split('\n').map(s => s.trim()).filter(Boolean);

  // 组合：〔原問〕标签 + 提问者叙述 + 〔岐伯語〕入话标记 + 岐伯回答，统一参与逐叶装箱
  const items = [];
  if (narrativeParas.length) {
    items.push({ text: L.LABEL_NARRATIVE, kind: 'narrative-label' });
    for (const np of narrativeParas) items.push({ text: np, kind: 'narrative' });
    items.push({ text: L.MARKER_QIBO, kind: 'marker' });
  }
  for (const ap of answerParas) items.push({ text: ap, kind: 'answer' });

  const pages = L.paginateByHeight(items, art.question);

  pages.forEach((pg, i) => {
    const isFirst = i === 0, isLast = i === pages.length - 1;
    const res = L.buildArticlePage({
      title: art.title,
      isContinuation: !isFirst,
      question: isFirst ? art.question : null,
      paragraphs: pg.items,
      qrPngPath,
      showFooter: isLast,
      chineseDate,
      startOfSection: bodyPageCount === 0
    }, CTX);
    docElements.push(...res.elements);
    bodyPageCount++;

    // 页块总高 = 天头题眉 + 可见外框（框高固定 FRAME_MIN_PT，含其上下留白 OUTER_MARGIN）
    // 题眉与外框同属一个不可拆工作区行，故二者之和才是真实占高。
    let blockH = M.HEADER_PT + M.FRAME_MIN_PT;
    if (blockH > M.PAGE_CONTENT_PT) overflow++;
    report.push({
      篇: art.title, 叶: i + 1, 篇内叶数: pages.length,
      正文段数: pg.items.length, 左栏高: +res.leftH.toFixed(1),
      批校行: res.nRail, 札记行: res.fillerLines,
      页块高: +blockH.toFixed(1), 超限: blockH > M.PAGE_CONTENT_PT
    });
  });
}

// 正文始于物理第 5 页；偶数叶正文结束在偶数页，才需补白让封底落在外侧。
const startLeafByTitle = new Map();
for (const [index, entry] of report.entries()) {
  if (entry.叶 === 1) startLeafByTitle.set(entry.篇, index + 1);
}
const toChineseLeaf = (n) => {
  if (!Number.isInteger(n) || n < 1 || n > 999) throw new Error('目录起始叶码超出范围: ' + n);
  const digits = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
  const underHundred = (value, omitLeadingOne = false) => {
    if (value < 10) return digits[value];
    const tens = Math.floor(value / 10), ones = value % 10;
    return (omitLeadingOne && tens === 1 ? '' : digits[tens]) + '十' + (ones ? digits[ones] : '');
  };
  if (n < 100) return underHundred(n, true);
  const hundreds = Math.floor(n / 100), remainder = n % 100;
  return digits[hundreds] + '百' + (remainder === 0 ? '' :
    (remainder < 10 ? '零' + digits[remainder] : underHundred(remainder)));
};
const tocEntries = arts.map(a => ({
  title: a.title,
  startLeafLabel: toChineseLeaf(startLeafByTitle.get(a.title))
}));
frontMatter.push(L.buildToc(tocEntries));
// 目录背面留空：正文节的 nextPage 从第五个物理页正面开始。
frontMatter.push(new Paragraph({
  pageBreakBefore: true, spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: []
}));

const needsBackBlank = bodyPageCount % 2 === 0;
console.log('篇数: ' + arts.length);
console.log('正文叶数（从第一叶计）: ' + bodyPageCount);
console.log('预计物理页数（封面+空白+目录+空白+正文+封底前必要留白+封底）: ' +
  (bodyPageCount + 5 + (needsBackBlank ? 1 : 0)));
console.log('版心: ' + M.PAGE_CONTENT_PT.toFixed(1) + 'pt   单叶预算: ' + M.BLOCK_BUDGET + 'pt');
console.log('超限页块: ' + overflow + '  (须为 0)');
const mid = report.filter(r => r.叶 < r.篇内叶数);
console.log('中间叶左栏 min=' + Math.min(...mid.map(r => r.左栏高)).toFixed(1) + ' 平均=' + (mid.reduce((a, b) => a + b.左栏高, 0) / mid.length).toFixed(1));
fs.writeFileSync(path.join(OUT_DIR, '_pagination-report-B01.json'), JSON.stringify(report, null, 1));

const doc = new Document({
  styles: { default: { document: { run: { font: F.FONT_BODY, size: 23, color: C.COLOR_INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT }
      }
    },
    children: frontMatter
  }, {
    properties: {
      type: SectionType.NEXT_PAGE,
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT },
        pageNumbers: { start: 1 }
      }
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { before: 0, after: 0, line: 300, lineRule: 'atLeast' },
        children: [
          new TextRun({ text: '第 ', font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM }),
          new TextRun({ children: [PageNumber.CURRENT], font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM }),
          new TextRun({ text: ' 葉', font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM })
        ]
      })] }),
      even: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 0, line: 300, lineRule: 'atLeast' },
        children: [
          new TextRun({ text: '第 ', font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM }),
          new TextRun({ children: [PageNumber.CURRENT], font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM }),
          new TextRun({ text: ' 葉', font: F.FONT_PAGE_NUM, bold: true, size: 26, color: C.COLOR_PAGE_NUM })
        ]
      })] })
    },
    children: docElements
  }, {
    // 正文末页后另起节：封底预设不显示叶码，不继承正文的页脚。
    properties: {
      type: SectionType.NEXT_PAGE,
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT }
      }
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ children: [] })] }),
      even: new Footer({ children: [new Paragraph({ children: [] })] })
    },
    children: [
      ...(needsBackBlank ? [
        // 正文叶数为偶数时补一张空白背页；节首段不设分页，避免 WPS 忽略。
        new Paragraph({ spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: [] }),
        new Paragraph({ pageBreakBefore: true, keepNext: true, spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: [] })
      ] : []),
      L.buildBackCover({ bookletLabel: '甲冊 · 幼兒啟蒙與性情習慣' })
    ]
  }]
});

const out = path.join(OUT_DIR, '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(out, buf);
  console.log('已生成: ' + out + ' (' + (buf.length / 1024).toFixed(1) + ' KB)');

  // 关键：必须随后处理管线，node docx 库不会自动写入以下五项：
  //   mirrorMargins/evenAndOddHeaders（对称镜像装订 + 奇偶页脚）
  //   pgNumType=chineseCountingThousand（汉字大写叶码）
  //   snapToGrid=0 + docGrid linePitch=0（关闭网格吸附，否则 WPS 把 16pt 行拉成 18pt，
  //                                        这正是「表格一高一低」在 WPS 中的真正成因）
  //   pgMar bottom=1500/footer=600（给页脚让位，并将叶码下移）
  // 缺失任一项，产出的 DOCX 在 WPS 中都会出问题。历史上曾因漏跑此步返工。
  const { execFileSync } = require('child_process');
  const PY = '/data/service/hnp/bin/python3';
  try {
    console.log('\n--- 后处理管线 ---');
    console.log(execFileSync(PY, [path.join(OUT_DIR, 'postprocess_docx.py')],
      { encoding: 'utf-8' }));
  } catch (e) {
    console.error('后处理失败：', e.stdout || e.message);
    process.exitCode = 1;
    return;
  }

  // 随后自动跑体检，任一项 FAIL 即视为不合格
  try {
    console.log('\n--- 成书体检 ---');
    console.log(execFileSync(PY, [path.join(OUT_DIR, 'verify_b01_docx.py')],
      { encoding: 'utf-8' }));
  } catch (e) {
    console.error('体检未通过：', e.stdout || e.message);
    process.exitCode = 1;
  }
}).catch(e => { console.error(e); process.exit(1); });
