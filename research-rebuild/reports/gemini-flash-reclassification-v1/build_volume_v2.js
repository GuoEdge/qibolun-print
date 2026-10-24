#!/usr/bin/env node
// 卷二 V2 分册生成器：一次生成一个目标分册。
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { Document, Packer, Paragraph, TextRun, Footer, PageNumber, AlignmentType, SectionType } = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');
const QRCode = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/qrcode');
const L = require('./lib_qibo_layout.js');
const X = require('./extract_qibo_content.js');
const { buildCoverTemplate } = require('./lib_cover_template.js');
const QR = require('./lib_qr_generator.js');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BASE = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1');
const VOLUME = path.join(ROOT, '卷二');
const CATALOG = path.join(BASE, 'workbook-40b-all-catalog.jsonl');
const CORPUS = path.join(BASE, 'all-articles-merged-v3.jsonl');
const CLEAN = path.join(BASE, 'all-articles-merged-v3-clean.jsonl');
const PY = '/data/service/hnp/bin/python3';
const NODE_MODULES = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules';
const F = L.FONTS, C = L.COLORS, M = L.METRICS;

const PARTS = {
  B11: { code: 'B11', stem: '甲', name: '擇偶標準與兩性吸引', dir: '甲册', file: '岐伯论·卷二·甲册·擇偶標準與兩性吸引.docx' },
  B12: { code: 'B12', stem: '乙', name: '婚姻存續與夫妻日常', dir: '乙册', file: '岐伯论·卷二·乙册·婚姻存續與夫妻日常.docx' },
  B13: { code: 'B13', stem: '丙', name: '親密背叛與離異止損', dir: '丙册', file: '岐伯论·卷二·丙册·親密背叛與離異止損.docx' },
  B38E: { code: 'B38E', stem: '丁', name: '情義本真與兩性名理', dir: '丁册', file: '岐伯论·卷二·丁册·情義本真與兩性名理.docx' }
};
const key = (process.argv[2] || '').toUpperCase();
if (!PARTS[key]) throw new Error('用法：node build_volume_v2.js [B11|B12|B13|B38E]');
const part = PARTS[key];
const outDir = path.join(VOLUME, part.dir);
fs.mkdirSync(outDir, { recursive: true });
const qrDir = path.join(outDir, '_qr');
fs.mkdirSync(qrDir, { recursive: true });

const catalog = fs.readFileSync(CATALOG, 'utf8').split('\n').filter(Boolean).map(JSON.parse);
const corpus = Object.fromEntries(fs.readFileSync(CORPUS, 'utf8').split('\n').filter(Boolean).map(x => { const d = JSON.parse(x); return [d.id, d]; }));
let records = catalog.filter(x => x.booklet_code === part.code);
if (!records.length) throw new Error('未找到分册记录: ' + key);
const first = records[0];
const bookletLabel = part.stem + '冊 · ' + part.name;
const ctx = { volPrefix: first.volume_prefix, volFull: first.volume_full_title, stem: part.stem, bookletTrad: part.name };
const arts = records.map(c => { const rec = corpus[c.original_id] || {}; const content = X.resolveContent(rec); return { ...c, answer: content.answer || '', narrative: content.narrative || '' }; });
const groups = L.loadUnits(part.code, arts);
const unitCount = groups.length;

// 前置结构（鸿蒙 WPS 兼容版 + 用户封面模板）：
// 1. 封面：使用用户在乙册-中设计的模板（buildCoverTemplate）
// 2. 留白：全部用整页无边框 cantSplit 表格（L.buildBlankPage）
// 3. 表格之间一律隔 1pt 空段（L.spacerPara）防相邻表格合并
// 4. 不再使用任何 pageBreakBefore 空段
// 封面参数：卷号、分册主题、副标题、篇数
const front = [
  buildCoverTemplate('【 卷  二 】', first.volume_prefix, part.stem + '冊 · ' + part.name, arts.length),
  L.spacerPara(), L.buildBlankPage(), L.spacerPara()
];
const body = [], report = [], startLeaf = new Map();
let unitLeaves = 0;
for (const g of groups) {
if (g.name) { body.push(L.buildUnitPage(g, unitCount, ctx, body.length === 0)); unitLeaves++; }
const uctx = { ...ctx, unitName: g.name };
for (const art of g.arts) {
  const items = [];
  const ns = art.narrative.trim().split('\n').map(s => s.trim()).filter(Boolean);
  const as = art.answer.trim().split('\n').map(s => s.trim()).filter(Boolean);
  if (ns.length) { items.push({ text: L.LABEL_NARRATIVE, kind: 'narrative-label' }); ns.forEach(t => items.push({ text: t, kind: 'narrative' })); items.push({ text: L.MARKER_QIBO, kind: 'marker' }); }
  as.forEach(t => items.push({ text: t, kind: 'answer' }));
  const pages = L.paginateByHeight(items, art.question);
  const qrPath = path.join(qrDir, 'qr_' + art.workbook_ordinal + '.png');
  const url = art.url || art.source_url || art.article_url || ('https://www.zhihu.com/question/' + (art.original_id || art.id));
  if (!fs.existsSync(qrPath)) {
    execFileSync(process.execPath, ['-e', `const QR = require(${JSON.stringify(path.join(BASE, 'lib_qr_generator.js'))}); QR.generateQr(${JSON.stringify(qrPath)}, ${JSON.stringify(url)}).then(()=>process.exit(0)).catch(e=>{console.error(e);process.exit(1)});`]);
  }
  pages.forEach((pg, i) => {
    const res = L.buildArticlePage({ title: art.title, isContinuation: i > 0, question: i === 0 ? art.question : null, paragraphs: pg.items, qrPngPath: qrPath, showFooter: i === pages.length - 1, chineseDate: L.toChineseDate(art.published_at), startOfSection: body.length === 0 }, uctx);
    if (i === 0) startLeaf.set(art.workbook_ordinal, report.length + unitLeaves + 1);
    body.push(...res.elements);
    report.push({ 篇: art.title, 叶: i + 1, 篇内叶数: pages.length, 正文段数: pg.items.length, 左栏高: +res.leftH.toFixed(1), 批校行: res.nRail, 札记行: res.fillerLines, 页块高: +(M.HEADER_PT + M.FRAME_MIN_PT).toFixed(1), 超限: M.HEADER_PT + M.FRAME_MIN_PT > M.PAGE_CONTENT_PT });
  });
}
}
const bodyLeaves = report.length + unitLeaves;
const chineseLeaf = n => { const d = ['零','一','二','三','四','五','六','七','八','九']; if (n < 10) return d[n]; if (n < 100) { const t = Math.floor(n / 10), o = n % 10; return (t === 1 ? '' : d[t]) + '十' + (o ? d[o] : ''); } const h = Math.floor(n / 100), r = n % 100; return d[h] + '百' + (r ? (r < 10 ? '零' + d[r] : chineseLeaf(r)) : ''); };
const tocFrames = L.buildToc(groups, a => chineseLeaf(startLeaf.get(a.workbook_ordinal)));
for (const f of tocFrames) { front.push(f, L.spacerPara()); }
// 目录后留白仅当目录叶数为奇：此时目录末叶落在纸正面（奇数物理页），其背面不能印正文，
// 补一叶留白。目录叶数为偶时目录末叶已是纸背面，下一页即新纸正面，无需留白。
// 目标：正文恒起于纸正面（奇数物理页），前置物理页数恒为偶。
const needsTocBlank = tocFrames.length % 2 === 1;
if (needsTocBlank) front.push(L.buildBlankPage(), L.spacerPara());
// 前置物理页 = 封面1 + 封面背留白1 + 目录N叶 + 目录背留白(0|1)。
const frontPages = 2 + tocFrames.length + (needsTocBlank ? 1 : 0);
// 封底须落在偶数物理页（背面朝外装订），奇偶不足时在封底前再补一张留白。
const needsBackBlank = (frontPages + 1 + bodyLeaves) % 2 === 1;
const footer = side => new Footer({ children: [new Paragraph({ alignment: side === 'even' ? AlignmentType.LEFT : AlignmentType.RIGHT, spacing: { before: 0, after: 0, line: 300, lineRule: 'atLeast' }, children: [new TextRun({ text: '第 ', font: F.FONT_PAGE_NUM, bold: true, size: 26 }), new TextRun({ children: [PageNumber.CURRENT], font: F.FONT_PAGE_NUM, bold: true, size: 26 }), new TextRun({ text: ' 葉', font: F.FONT_PAGE_NUM, bold: true, size: 26 })] })] });
const page = { size: { width: 11906, height: 16838 }, margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT } };
console.log(key + '：篇数 ' + arts.length + '，目录 ' + tocFrames.length + ' 叶，目录背留白 ' + (needsTocBlank ? 1 : 0) + '，前置物理页 ' + frontPages + '，单元 ' + unitCount + '，正文 ' + bodyLeaves + ' 叶（含单元扉叶 ' + unitLeaves + '），封底补白 ' + (needsBackBlank ? 1 : 0) + '，预计物理总页 ' + (frontPages + bodyLeaves + (needsBackBlank ? 1 : 0) + 1));
const doc = new Document({ styles: { default: { document: { run: { font: F.FONT_BODY, size: 23, color: C.COLOR_INK } } } }, sections: [
  { properties: { page }, children: front },
  { properties: { type: SectionType.NEXT_PAGE, page: { ...page, pageNumbers: { start: 1 } } }, footers: { default: footer('odd'), even: footer('even') }, children: body },
  { properties: { type: SectionType.NEXT_PAGE, page }, footers: { default: new Footer({ children: [new Paragraph({ children: [] })] }), even: new Footer({ children: [new Paragraph({ children: [] })] }) }, children: [...(needsBackBlank ? [L.buildBlankPage(), L.spacerPara()] : []), L.buildBackCover({ bookletLabel })] }
] });

(async () => {
  const out = path.join(outDir, part.file);
  fs.writeFileSync(out, await Packer.toBuffer(doc));
  const reportPath = path.join(outDir, '_pagination-report-' + key + '.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 1));
  const pp = fs.readFileSync(path.join(BASE, 'postprocess_docx.py'), 'utf8').replace(/BASE = .*\n/, `BASE = ${JSON.stringify(outDir + '/') }\n`).replace(/DOCX = BASE \+ .*\n/, `DOCX = BASE + ${JSON.stringify(part.file)}\n`).replace(/PROTOTYPE = BASE \+ .*\n/, `PROTOTYPE = ${JSON.stringify(path.join(BASE, '岐伯论-现代学者批校手卷本-可编辑原型.docx'))}\n`);
  const ppPath = path.join(outDir, 'postprocess_docx.py'); fs.writeFileSync(ppPath, pp);
  const verify = `#!/usr/bin/env python3\nimport zipfile,os,json,re,sys\nDOCX=${JSON.stringify(out)}\nREPORT=${JSON.stringify(reportPath)}\nLABEL=${JSON.stringify(bookletLabel)}\nEXPECTED=${arts.length}\nBLANKS=${1 + 1 + (needsTocBlank ? 1 : 0) + (needsBackBlank ? 1 : 0)}\nfail=[]\ndef ck(n,v):\n print('[%s] %s' % ('PASS' if v else 'FAIL',n)); fail.append(n) if not v else None\nwith zipfile.ZipFile(DOCX) as z:\n ck('ZIP完整',z.testzip() is None); d=z.read('word/document.xml').decode(); s=z.read('word/settings.xml').decode()\n ck('三节',len(re.findall(r'<w:sectPr(?:\\s[^>]*)?>',d))==3); ck('正文起始页码', 'chineseCountingThousand' in d and 'w:start="1"' in d); ck('镜像页边距','mirrorMargins' in s); ck('固定表格', '<w:tblLayout w:type="fixed"/>' in d); ck('目录标签', '本 冊 篇 目 總 覽' in d); ck('封底标签',LABEL in d); ck('留白页数',len(re.findall(r'trHeight[^>]*w:val="14318"',d))==BLANKS); ck('分页报告无超限',not any(x.get('超限') for x in json.load(open(REPORT)))); ck('篇数',len(set(x['篇'] for x in json.load(open(REPORT))))==EXPECTED); media=[n for n in z.namelist() if n.startswith('word/media/') and n != 'word/media/']; ck('二维码有效',bool(media) and all(z.read(n).startswith(b'\\x89PNG') for n in media))\nprint('结果：'+('通过' if not fail else '失败 '+','.join(fail))); sys.exit(bool(fail))\n`;
  const vp = path.join(outDir, 'verify_' + key.toLowerCase() + '_docx.py'); fs.writeFileSync(vp, verify);
  execFileSync(PY, [ppPath], { stdio: 'inherit' });
  execFileSync(PY, [vp], { stdio: 'inherit' });
  fs.writeFileSync(path.join(outDir, 'build-manifest.json'), JSON.stringify({ part: key, booklet_code: part.code, article_count: arts.length, docx: out, report: reportPath, verify: vp }, null, 2));
  console.log('已生成: ' + out);
})().catch(e => { console.error(e.stack || e); process.exit(1); });
