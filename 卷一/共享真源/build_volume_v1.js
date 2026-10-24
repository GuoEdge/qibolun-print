#!/usr/bin/env node
// 卷一批量成书生成器的副本；唯一可执行真源是 research-rebuild/reports/gemini-flash-reclassification-v1/build_volume_v1.js。
// 此集中副本只作阅读入口，含原工程绝对路径；运行前须同步原工程真源版本。
require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/build_volume_v1.js');
/*
// 卷一 V1 分册生成器：一次只生成一个目标分册；B02 按文章顺序拆为三等份。
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { Document, Packer, Paragraph, TextRun, Footer, PageNumber, AlignmentType, SectionType } = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');
const QRCode = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/qrcode');
const L = require('./lib_qibo_layout.js');
const X = require('./extract_qibo_content.js');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BASE = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1');
const VOLUME = path.join(ROOT, '卷一');
const CATALOG = path.join(BASE, 'workbook-40b-all-catalog.jsonl');
const CORPUS = path.join(BASE, 'all-articles-merged-v3.jsonl');
const CLEAN = path.join(BASE, 'all-articles-merged-v3-clean.jsonl');
const PY = '/data/service/hnp/bin/python3';
const NODE_MODULES = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules';
const F = L.FONTS, C = L.COLORS, M = L.METRICS;

const PARTS = {
  B02A: { code: 'B02', stem: '乙上', name: '學業功課與學校日常·上', dir: '乙册-上', file: '岐伯论·卷一·乙册·上·學業功課與學校日常.docx' },
  B02B: { code: 'B02', stem: '乙中', name: '學業功課與學校日常·中', dir: '乙册-中', file: '岐伯论·卷一·乙册·中·學業功課與學校日常.docx' },
  B02C: { code: 'B02', stem: '乙下', name: '學業功課與學校日常·下', dir: '乙册-下', file: '岐伯论·卷一·乙册·下·學業功課與學校日常.docx' },
  B03: { code: 'B03', stem: '丙', name: '言傳身教與獎懲邊界', dir: '丙册', file: '岐伯论·卷一·丙册·言傳身教與獎懲邊界.docx' },
  B04: { code: 'B04', stem: '丁', name: '親子溝通與青春叛逆', dir: '丁册', file: '岐伯论·卷一·丁册·親子溝通與青春叛逆.docx' },
  B05: { code: 'B05', stem: '戊', name: '父母控制欲與精神解绑', dir: '戊册', file: '岐伯论·卷一·戊册·父母控制欲與精神解绑.docx' },
  B06: { code: 'B06', stem: '己', name: '成年子女自立與邊界', dir: '己册', file: '岐伯论·卷一·己册·成年子女自立與邊界.docx' },
  B07: { code: 'B07', stem: '庚', name: '隔代教養與長輩相處', dir: '庚册', file: '岐伯论·卷一·庚册·隔代教養與長輩相處.docx' },
  B08: { code: 'B08', stem: '辛', name: '手足同胞與家族親戚', dir: '辛册', file: '岐伯论·卷一·辛册·手足同胞與家族親戚.docx' },
  B09: { code: 'B09', stem: '壬', name: '家族傳承與家風家范', dir: '壬册', file: '岐伯论·卷一·壬册·家族傳承與家風家范.docx' },
  B10: { code: 'B10', stem: '癸', name: '臨終關懷與白事奠儀', dir: '癸册', file: '岐伯论·卷一·癸册·臨終關懷與白事奠儀.docx' }
};
const key = (process.argv[2] || '').toUpperCase();
if (!PARTS[key]) throw new Error('用法：node build_volume_v1.js [B02A|B02B|B02C|B03-B10]');
const part = PARTS[key];
const outDir = path.join(VOLUME, part.dir);
fs.mkdirSync(outDir, { recursive: true });
const qrDir = path.join(outDir, '_qr');
fs.mkdirSync(qrDir, { recursive: true });

const catalog = fs.readFileSync(CATALOG, 'utf8').split('\n').filter(Boolean).map(JSON.parse);
const corpus = Object.fromEntries(fs.readFileSync(CORPUS, 'utf8').split('\n').filter(Boolean).map(x => { const d = JSON.parse(x); return [d.id, d]; }));
let records = catalog.filter(x => x.booklet_code === part.code);
if (part.code === 'B02') {
  const n = records.length, size = Math.ceil(n / 3), index = { B02A: 0, B02B: 1, B02C: 2 }[key];
  records = records.slice(index * size, Math.min(n, (index + 1) * size));
}
if (!records.length) throw new Error('未找到分册记录: ' + key);
const first = records[0];
const bookletLabel = part.stem + '冊 · ' + part.name;
const ctx = { volPrefix: first.volume_prefix, volFull: first.volume_full_title, stem: part.stem, bookletTrad: part.name };
const arts = records.map(c => { const rec = corpus[c.original_id] || {}; const content = X.resolveContent(rec); return { ...c, answer: content.answer || '', narrative: content.narrative || '' }; });

const blank = () => new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: [] });
const front = [L.buildCover({ volName: '【 卷  一 】 ' + first.volume_prefix, bookletLabel, subLine: '全冊通收' + arts.length + '篇 · 研讀批校工作本' }), blank(), L.breakPara()];
const body = [], report = [], startLeaf = new Map();
for (const art of arts) {
  const items = [];
  const ns = art.narrative.trim().split('\n').map(s => s.trim()).filter(Boolean);
  const as = art.answer.trim().split('\n').map(s => s.trim()).filter(Boolean);
  if (ns.length) { items.push({ text: L.LABEL_NARRATIVE, kind: 'narrative-label' }); ns.forEach(t => items.push({ text: t, kind: 'narrative' })); items.push({ text: L.MARKER_QIBO, kind: 'marker' }); }
  as.forEach(t => items.push({ text: t, kind: 'answer' }));
  const pages = L.paginateByHeight(items, art.question);
  const qrPath = path.join(qrDir, 'qr_' + art.workbook_ordinal + '.png');
  const url = art.url || art.source_url || art.article_url || ('https://www.zhihu.com/question/' + (art.original_id || art.id));
  if (!fs.existsSync(qrPath)) {
    execFileSync(process.execPath, ['-e', `const q=require(${JSON.stringify('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/qrcode')}); q.toFile(${JSON.stringify(qrPath)}, ${JSON.stringify(url)}, {width:34, margin:0}).then(()=>process.exit(0)).catch(e=>{console.error(e);process.exit(1)});`]);
  }
  pages.forEach((pg, i) => {
    const res = L.buildArticlePage({ title: art.title, isContinuation: i > 0, question: i === 0 ? art.question : null, paragraphs: pg.items, qrPngPath: qrPath, showFooter: i === pages.length - 1, chineseDate: L.toChineseDate(art.published_at), startOfSection: body.length === 0 }, ctx);
    if (i === 0) startLeaf.set(art.title, report.length + 1);
    body.push(...res.elements);
    report.push({ 篇: art.title, 叶: i + 1, 篇内叶数: pages.length, 正文段数: pg.items.length, 左栏高: +res.leftH.toFixed(1), 批校行: res.nRail, 札记行: res.fillerLines, 页块高: +(M.HEADER_PT + M.FRAME_MIN_PT).toFixed(1), 超限: M.HEADER_PT + M.FRAME_MIN_PT > M.PAGE_CONTENT_PT });
  });
}
const chineseLeaf = n => { const d = ['零','一','二','三','四','五','六','七','八','九']; if (n < 10) return d[n]; if (n < 100) { const t = Math.floor(n / 10), o = n % 10; return (t === 1 ? '' : d[t]) + '十' + (o ? d[o] : ''); } const h = Math.floor(n / 100), r = n % 100; return d[h] + '百' + (r ? (r < 10 ? '零' + d[r] : chineseLeaf(r)) : ''); };
front.push(L.buildToc(arts.map(a => ({ title: a.title, startLeafLabel: chineseLeaf(startLeaf.get(a.title)) }))));
front.push(blank());
const needsBackBlank = report.length % 2 === 0;
const footer = side => new Footer({ children: [new Paragraph({ alignment: side === 'even' ? AlignmentType.LEFT : AlignmentType.RIGHT, spacing: { before: 0, after: 0, line: 300, lineRule: 'atLeast' }, children: [new TextRun({ text: '第 ', font: F.FONT_PAGE_NUM, bold: true, size: 26 }), new TextRun({ children: [PageNumber.CURRENT], font: F.FONT_PAGE_NUM, bold: true, size: 26 }), new TextRun({ text: ' 葉', font: F.FONT_PAGE_NUM, bold: true, size: 26 })] })] });
const page = { size: { width: 11906, height: 16838 }, margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT } };
const doc = new Document({ styles: { default: { document: { run: { font: F.FONT_BODY, size: 23, color: C.COLOR_INK } } } }, sections: [
  { properties: { page }, children: front },
  { properties: { type: SectionType.NEXT_PAGE, page: { ...page, pageNumbers: { start: 1 } } }, footers: { default: footer('odd'), even: footer('even') }, children: body },
  { properties: { type: SectionType.NEXT_PAGE, page }, footers: { default: new Footer({ children: [new Paragraph({ children: [] })] }), even: new Footer({ children: [new Paragraph({ children: [] })] }) }, children: [...(needsBackBlank ? [new Paragraph({ children: [] }), blank()] : []), L.buildBackCover({ bookletLabel })] }
] });

(async () => {
  const out = path.join(outDir, part.file);
  fs.writeFileSync(out, await Packer.toBuffer(doc));
  const reportPath = path.join(outDir, '_pagination-report-' + key + '.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 1));
  const pp = fs.readFileSync(path.join(BASE, 'postprocess_docx.py'), 'utf8').replace(/BASE = .*\n/, `BASE = ${JSON.stringify(outDir + '/') }\n`).replace(/DOCX = BASE \+ .*\n/, `DOCX = BASE + ${JSON.stringify(part.file)}\n`).replace(/PROTOTYPE = BASE \+ .*\n/, `PROTOTYPE = ${JSON.stringify(path.join(BASE, '岐伯论-现代学者批校手卷本-可编辑原型.docx'))}\n`);
  const ppPath = path.join(outDir, 'postprocess_docx.py'); fs.writeFileSync(ppPath, pp);
  const verify = `#!/usr/bin/env python3\nimport zipfile,os,json,re,sys\nDOCX=${JSON.stringify(out)}\nREPORT=${JSON.stringify(reportPath)}\nLABEL=${JSON.stringify(bookletLabel)}\nEXPECTED=${arts.length}\nfail=[]\ndef ck(n,v):\n print('[%s] %s' % ('PASS' if v else 'FAIL',n)); fail.append(n) if not v else None\nwith zipfile.ZipFile(DOCX) as z:\n ck('ZIP完整',z.testzip() is None); d=z.read('word/document.xml').decode(); s=z.read('word/settings.xml').decode()\n ck('三节',len(re.findall(r'<w:sectPr(?:\\s[^>]*)?>',d))==3); ck('正文起始页码', 'chineseCountingThousand' in d and 'w:start="1"' in d); ck('镜像页边距','mirrorMargins' in s); ck('固定表格', '<w:tblLayout w:type="fixed"/>' in d); ck('目录标签', '本 冊 篇 目 總 覽' in d); ck('封底标签',LABEL in d); ck('分页报告无超限',not any(x.get('超限') for x in json.load(open(REPORT)))); ck('篇数',len(set(x['篇'] for x in json.load(open(REPORT))))==EXPECTED); media=[n for n in z.namelist() if n.startswith('word/media/') and n != 'word/media/']; ck('二维码有效',bool(media) and all(z.read(n).startswith(b'\\x89PNG') for n in media))\nprint('结果：'+('通过' if not fail else '失败 '+','.join(fail))); sys.exit(bool(fail))\n`;
  const vp = path.join(outDir, 'verify_' + key.toLowerCase() + '_docx.py'); fs.writeFileSync(vp, verify);
  execFileSync(PY, [ppPath], { stdio: 'inherit' });
  execFileSync(PY, [vp], { stdio: 'inherit' });
  fs.writeFileSync(path.join(outDir, 'build-manifest.json'), JSON.stringify({ part: key, booklet_code: part.code, article_count: arts.length, docx: out, report: reportPath, verify: vp }, null, 2));
  console.log('已生成: ' + out);
})().catch(e => { console.error(e.stack || e); process.exit(1); });
*/
