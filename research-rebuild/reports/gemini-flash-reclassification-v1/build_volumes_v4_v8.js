#!/usr/bin/env node
// V4-V8 通用构建脚本：支持全部24个分册，卷名繁体化
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
const CATALOG = path.join(BASE, 'workbook-40b-all-catalog.jsonl');
const CORPUS = path.join(BASE, 'all-articles-merged-v3.jsonl');
const CLEAN = path.join(BASE, 'all-articles-merged-v3-clean.jsonl');
const PY = '/data/service/hnp/bin/python3';
const NODE_MODULES = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules';
const F = L.FONTS, C = L.COLORS, M = L.METRICS;

// 卷名繁体映射
const VOLUME_TRAD = {
  'V3': { prefix: '酬酢進退', full: '酬酢進退——人我分寸與處世防線', dirName: '卷三', coverLabel: '【 卷  三 】' },
  'V4': { prefix: '存神調息', full: '存神調息——身心安頓與心性知行', dirName: '卷四', coverLabel: '【 卷  四 】' },
  'V5': { prefix: '度勢居貨', full: '度勢居貨——職場博弈與財富商道', dirName: '卷五', coverLabel: '【 卷  五 】' },
  'V6': { prefix: '觀風察變', full: '觀風察變——時代思潮與家國時局', dirName: '卷六', coverLabel: '【 卷  六 】' },
  'V7': { prefix: '滌除玄覽', full: '滌除玄覽——深層哲思與義理名相', dirName: '卷七', coverLabel: '【 卷  七 】' },
  'V8': { prefix: '格物鑄器', full: '格物鑄器——造物工程與歷史治亂', dirName: '卷八', coverLabel: '【 卷  八 】' }
};

// 分册配置：27个分册完整定义（含V3）
const PARTS = {
  // V3 酬酢防身
  B14: { volume: 'V3', code: 'B14', stem: '甲', name: '人情往來與禮數分寸', dir: '甲册' },
  B15: { volume: 'V3', code: 'B15', stem: '乙', name: '社交距離與孤立自處', dir: '乙册' },
  B16: { volume: 'V3', code: 'B16', stem: '丙', name: '危機識人與權義守界', dir: '丙册' },
  B38C: { volume: 'V3', code: 'B38C', stem: '丁', name: '處世分寸與人我進退', suffix: '上册', dir: '丁册/上册' },
  B38D: { volume: 'V3', code: 'B38D', stem: '丁', name: '處世分寸與人我進退', suffix: '下册', dir: '丁册/下册' },
  // V4 存神調息
  B17A: { volume: 'V4', code: 'B17A', stem: '甲', name: '情志平復與容貌自和', suffix: '上册', dir: '甲册/上册' },
  B17B: { volume: 'V4', code: 'B17B', stem: '甲', name: '情志平復與容貌自和', suffix: '下册', dir: '甲册/下册' },
  B18: { volume: 'V4', code: 'B18', stem: '乙', name: '知行合一與作息身息', dir: '乙册' },
  // V5 度勢居貨
  // B20 拆分为上中下3册
  B20A: { volume: 'V5', code: 'B20A', stem: '甲', name: '職場彙報與權責留痕', suffix: '上册', dir: '甲册/上册' },
  B20B: { volume: 'V5', code: 'B20B', stem: '甲', name: '職場彙報與權責留痕', suffix: '中册', dir: '甲册/中册' },
  B20C: { volume: 'V5', code: 'B20C', stem: '甲', name: '職場彙報與權責留痕', suffix: '下册', dir: '甲册/下册' },
  B22A: { volume: 'V5', code: 'B22A', stem: '乙', name: '商業競爭與資產投資', suffix: '上册', dir: '乙册/上册' },
  B22B: { volume: 'V5', code: 'B22B', stem: '乙', name: '商業競爭與資產投資', suffix: '下册', dir: '乙册/下册' },
  // V6 觀風察變
  B23A: { volume: 'V6', code: 'B23A', stem: '甲', name: '公共熱點與事件剖析', suffix: '上册', dir: '甲册/上册' },
  B23B: { volume: 'V6', code: 'B23B', stem: '甲', name: '公共熱點與事件剖析', suffix: '下册', dir: '甲册/下册' },
  B24: { volume: 'V6', code: 'B24', stem: '乙', name: '青年心境與躺平反思', dir: '乙册' },
  B25: { volume: 'V6', code: 'B25', stem: '丙', name: '網絡生態與群體極化', dir: '丙册' },
  B26: { volume: 'V6', code: 'B26', stem: '丁', name: '性別議題與兩性輿論', dir: '丁册' },
  B27: { volume: 'V6', code: 'B27', stem: '戊', name: '教育體制與社會流動', dir: '戊册' },
  B28: { volume: 'V6', code: 'B28', stem: '己', name: '消費主義與生活觀念', dir: '己册' },
  B29: { volume: 'V6', code: 'B29', stem: '庚', name: '現代科技與工具反思', dir: '庚册' },
  B30: { volume: 'V6', code: 'B30', stem: '辛', name: '文明演進與社會秩序', dir: '辛册' },
  B36A: { volume: 'V6', code: 'B36A', stem: '壬', name: '時局經緯與家國論衡', suffix: '上册', dir: '壬册/上册' },
  B36B: { volume: 'V6', code: 'B36B', stem: '壬', name: '時局經緯與家國論衡', suffix: '下册', dir: '壬册/下册' },
  // V7 滌除玄覽
  // B31 拆分为上下2册
  B31A: { volume: 'V7', code: 'B31A', stem: '甲', name: '存在本質與生命意義', suffix: '上册', dir: '甲册/上册' },
  B31B: { volume: 'V7', code: 'B31B', stem: '甲', name: '存在本質與生命意義', suffix: '下册', dir: '甲册/下册' },
  B32A: { volume: 'V7', code: 'B32A', stem: '乙', name: '名相辨析與語言牢籠', suffix: '上册', dir: '乙册/上册' },
  B32B: { volume: 'V7', code: 'B32B', stem: '乙', name: '名相辨析與語言牢籠', suffix: '下册', dir: '乙册/下册' },
  B33: { volume: 'V7', code: 'B33', stem: '丙', name: '善惡分野與人性幽微', dir: '丙册' },
  B34: { volume: 'V7', code: 'B34', stem: '丁', name: '認識局限與心智模型', dir: '丁册' },
  B35: { volume: 'V7', code: 'B35', stem: '戊', name: '命途因果與得失隨緣', dir: '戊册' },
  B37: { volume: 'V7', code: 'B37', stem: '己', name: '神聖敬畏與信仰維度', dir: '己册' },
  // B38 庚册纯正哲思4册（子丑寅卯）
  B38A: { volume: 'V7', code: 'B38A', stem: '庚', name: '心性自持與精神獨立', suffix: '子册', dir: '庚册/子册' },
  B38B: { volume: 'V7', code: 'B38B', stem: '庚', name: '心性自持與精神獨立', suffix: '丑册', dir: '庚册/丑册' },
  B38I: { volume: 'V7', code: 'B38I', stem: '庚', name: '世情人性與義理雜談', suffix: '寅册', dir: '庚册/寅册' },
  B38J: { volume: 'V7', code: 'B38J', stem: '庚', name: '世情人性與義理雜談', suffix: '卯册', dir: '庚册/卯册' },
  // V8 鑑往鑄器
  B38G: { volume: 'V8', code: 'B38G', stem: '丙', name: '格物致知與機巧萬類', dir: '丙册' },
  B38H: { volume: 'V8', code: 'B38H', stem: '丁', name: '治家器術與聲藝百工', dir: '丁册' },
  B39: { volume: 'V8', code: 'B39', stem: '甲', name: '藝能創作與生活美學', dir: '甲册' },
  B40: { volume: 'V8', code: 'B40', stem: '乙', name: '治亂興亡與國家工程', dir: '乙册' }
};

const key = (process.argv[2] || '').toUpperCase();
if (!PARTS[key]) {
  console.error('用法：node build_volumes_v4_v8.js [分册代码]');
  console.error('可用分册（含拆分子册）：');
  console.error('  V3: B14, B15, B16');
  console.error('  V4: B17, B18, B19');
  console.error('  V5: B20A/B/C (上中下), B21, B22');
  console.error('  V6: B23-B30');
  console.error('  V7: B31A/B (上下), B32-B37, B38A-B38L (子丑寅卯辰巳午未申酉戌亥)');
  console.error('  V8: B39, B40');
  process.exit(1);
}

const part = PARTS[key];
const vol = VOLUME_TRAD[part.volume];
const VOLUME_DIR = path.join(ROOT, vol.dirName);
const outDir = path.join(VOLUME_DIR, part.dir);
fs.mkdirSync(outDir, { recursive: true });
const qrDir = path.join(BASE, 'qr_cache_all');
fs.mkdirSync(qrDir, { recursive: true });

const catalog = fs.readFileSync(CATALOG, 'utf8').split('\n').filter(Boolean).map(JSON.parse);
const corpus = Object.fromEntries(fs.readFileSync(CORPUS, 'utf8').split('\n').filter(Boolean).map(x => { const d = JSON.parse(x); return [d.id, d]; }));
let records = catalog.filter(x => x.booklet_code === part.code);
if (!records.length) throw new Error('未找到分册记录: ' + key);

const bookletLabel = part.suffix 
  ? (part.stem + ' · ' + part.name + '·' + part.suffix)
  : (part.stem + '冊 · ' + part.name);
const ctx = { 
  volPrefix: vol.prefix,  // 使用繁体卷名
  volFull: vol.full,      // 使用繁体完整标题
  stem: part.stem, 
  bookletTrad: part.name 
};
const arts = records.map(c => { 
  const rec = corpus[c.original_id] || {}; 
  const content = X.resolveContent(rec); 
  return { ...c, answer: content.answer || '', narrative: content.narrative || '' }; 
});
const groups = L.loadUnits(part.code, arts);
const unitCount = groups.length;

// 前置结构（鸿蒙 WPS 兼容版）
const coverLabel = part.suffix 
  ? (part.stem + ' · ' + part.name + '·' + part.suffix)
  : (part.stem + '冊 · ' + part.name);
const front = [
  buildCoverTemplate(vol.coverLabel, vol.prefix, coverLabel, arts.length),
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
  if (ns.length) { 
    items.push({ text: L.LABEL_NARRATIVE, kind: 'narrative-label' }); 
    ns.forEach(t => items.push({ text: t, kind: 'narrative' })); 
    items.push({ text: L.MARKER_QIBO, kind: 'marker' }); 
  }
  as.forEach(t => items.push({ text: t, kind: 'answer' }));
  const pages = L.paginateByHeight(items, art.question);
  const qrPath = path.join(qrDir, 'qr_' + art.workbook_ordinal + '.png');
  const url = art.url || art.source_url || art.article_url || ('https://www.zhihu.com/question/' + (art.original_id || art.id));
  if (!fs.existsSync(qrPath)) {
    execFileSync(process.execPath, ['-e', `const QR = require(${JSON.stringify(path.join(BASE, 'lib_qr_generator.js'))}); QR.generateQr(${JSON.stringify(qrPath)}, ${JSON.stringify(url)}).then(()=>process.exit(0)).catch(e=>{console.error(e);process.exit(1)});`]);
  }
  pages.forEach((pg, i) => {
    const res = L.buildArticlePage({ 
      title: art.title, 
      isContinuation: i > 0, 
      question: i === 0 ? art.question : null, 
      paragraphs: pg.items, 
      qrPngPath: qrPath, 
      showFooter: i === pages.length - 1, 
      chineseDate: L.toChineseDate(art.published_at), 
      startOfSection: body.length === 0 
    }, uctx);
    if (i === 0) startLeaf.set(art.workbook_ordinal, report.length + unitLeaves + 1);
    body.push(...res.elements);
    report.push({ 
      篇: art.title, 
      叶: i + 1, 
      篇内叶数: pages.length, 
      正文段数: pg.items.length, 
      左栏高: +res.leftH.toFixed(1), 
      批校行: res.nRail, 
      札记行: res.fillerLines, 
      页块高: +(M.HEADER_PT + M.FRAME_MIN_PT).toFixed(1), 
      超限: M.HEADER_PT + M.FRAME_MIN_PT > M.PAGE_CONTENT_PT 
    });
  });
}
}
const bodyLeaves = report.length + unitLeaves;

const chineseLeaf = n => { 
  const d = ['零','一','二','三','四','五','六','七','八','九']; 
  if (n < 10) return d[n]; 
  if (n < 100) { 
    const t = Math.floor(n / 10), o = n % 10; 
    return (t === 1 ? '' : d[t]) + '十' + (o ? d[o] : ''); 
  } 
  const h = Math.floor(n / 100), r = n % 100; 
  return d[h] + '百' + (r ? (r < 10 ? '零' + d[r] : chineseLeaf(r)) : ''); 
};

const tocFrames = L.buildToc(groups, a => chineseLeaf(startLeaf.get(a.workbook_ordinal)));

for (const f of tocFrames) { front.push(f, L.spacerPara()); }

const needsTocBlank = tocFrames.length % 2 === 1;
if (needsTocBlank) front.push(L.buildBlankPage(), L.spacerPara());

const frontPages = 2 + tocFrames.length + (needsTocBlank ? 1 : 0);
const needsBackBlank = (frontPages + 1 + bodyLeaves) % 2 === 1;

const footer = side => new Footer({ 
  children: [new Paragraph({ 
    alignment: side === 'even' ? AlignmentType.LEFT : AlignmentType.RIGHT, 
    spacing: { before: 0, after: 0, line: 300, lineRule: 'atLeast' }, 
    children: [
      new TextRun({ text: '第 ', font: F.FONT_PAGE_NUM, bold: true, size: 26 }), 
      new TextRun({ children: [PageNumber.CURRENT], font: F.FONT_PAGE_NUM, bold: true, size: 26 }), 
      new TextRun({ text: ' 葉', font: F.FONT_PAGE_NUM, bold: true, size: 26 })
    ] 
  })] 
});

const page = { 
  size: { width: 11906, height: 16838 }, 
  margin: { top: M.MARGIN_TOP, right: M.MARGIN_RIGHT, bottom: M.MARGIN_BOTTOM, left: M.MARGIN_LEFT } 
};

console.log(key + '：篇数 ' + arts.length + '，目录 ' + tocFrames.length + ' 叶，目录背留白 ' + (needsTocBlank ? 1 : 0) + '，前置物理页 ' + frontPages + '，单元 ' + unitCount + '，正文 ' + bodyLeaves + ' 叶（含单元扉叶 ' + unitLeaves + '），封底补白 ' + (needsBackBlank ? 1 : 0) + '，预计物理总页 ' + (frontPages + bodyLeaves + (needsBackBlank ? 1 : 0) + 1));

const doc = new Document({ 
  styles: { default: { document: { run: { font: F.FONT_BODY, size: 23, color: C.COLOR_INK } } } }, 
  sections: [
    { properties: { page }, children: front },
    { 
      properties: { 
        type: SectionType.NEXT_PAGE, 
        page: { ...page, pageNumbers: { start: 1 } } 
      }, 
      footers: { default: footer('odd'), even: footer('even') }, 
      children: body 
    },
    { 
      properties: { type: SectionType.NEXT_PAGE, page }, 
      footers: { 
        default: new Footer({ children: [new Paragraph({ children: [] })] }), 
        even: new Footer({ children: [new Paragraph({ children: [] })] }) 
      }, 
      children: [
        ...(needsBackBlank ? [L.buildBlankPage(), L.spacerPara()] : []), 
        L.buildBackCover({ bookletLabel })
      ] 
    }
  ] 
});

// 文件名：分册用 "卷名·stem·name·suffix"，非分册用 "卷名·stem册·name"
const fileName = part.suffix
  ? `岐伯论·${vol.dirName}·${part.stem}·${part.name}·${part.suffix}.docx`
  : `岐伯论·${vol.dirName}·${part.stem}册·${part.name}.docx`;

(async () => {
  const out = path.join(outDir, fileName);
  fs.writeFileSync(out, await Packer.toBuffer(doc));
  const reportPath = path.join(outDir, '_pagination-report-' + key + '.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 1));
  
  // 后处理脚本
  const pp = fs.readFileSync(path.join(BASE, 'postprocess_docx.py'), 'utf8')
    .replace(/BASE = .*\n/, `BASE = ${JSON.stringify(outDir + '/')}\n`)
    .replace(/DOCX = BASE \+ .*\n/, `DOCX = BASE + ${JSON.stringify(fileName)}\n`)
    .replace(/PROTOTYPE = BASE \+ .*\n/, `PROTOTYPE = ${JSON.stringify(path.join(BASE, '岐伯论-现代学者批校手卷本-可编辑原型.docx'))}\n`);
  const ppPath = path.join(outDir, 'postprocess_docx.py'); 
  fs.writeFileSync(ppPath, pp);
  
  // 验证脚本
  const verify = `#!/usr/bin/env python3
import zipfile,os,json,re,sys
DOCX=${JSON.stringify(out)}
REPORT=${JSON.stringify(reportPath)}
LABEL=${JSON.stringify(bookletLabel)}
EXPECTED=${arts.length}
BLANKS=${1 + 1 + (needsTocBlank ? 1 : 0) + (needsBackBlank ? 1 : 0)}
fail=[]
def ck(n,v):
 print('[%s] %s' % ('PASS' if v else 'FAIL',n)); fail.append(n) if not v else None
with zipfile.ZipFile(DOCX) as z:
 ck('ZIP完整',z.testzip() is None); d=z.read('word/document.xml').decode(); s=z.read('word/settings.xml').decode()
 ck('三节',len(re.findall(r'<w:sectPr(?:\\s[^>]*)?>',d))==3); ck('正文起始页码', 'chineseCountingThousand' in d and 'w:start="1"' in d); ck('镜像页边距','mirrorMargins' in s); ck('固定表格', '<w:tblLayout w:type="fixed"/>' in d); ck('目录标签', '本 冊 篇 目 總 覽' in d); ck('封底标签',LABEL in d); ck('留白页数',len(re.findall(r'trHeight[^>]*w:val="14318"',d))==BLANKS); ck('分页报告无超限',not any(x.get('超限') for x in json.load(open(REPORT)))); ck('篇数',len(set(x['篇'] for x in json.load(open(REPORT))))==EXPECTED); media=[n for n in z.namelist() if n.startswith('word/media/') and n != 'word/media/']; ck('二维码有效',bool(media) and all(z.read(n).startswith(b'\\x89PNG') for n in media))
print('结果：'+('通过' if not fail else '失败 '+','.join(fail))); sys.exit(bool(fail))
`;
  const vp = path.join(outDir, 'verify_' + key.toLowerCase() + '_docx.py'); 
  fs.writeFileSync(vp, verify);
  
  execFileSync(PY, [ppPath], { stdio: 'inherit' });
  execFileSync(PY, [vp], { stdio: 'inherit' });
  
  fs.writeFileSync(path.join(outDir, 'build-manifest.json'), JSON.stringify({ 
    part: key, 
    booklet_code: part.code, 
    volume: part.volume,
    article_count: arts.length, 
    docx: out, 
    report: reportPath, 
    verify: vp 
  }, null, 2));
  
  console.log('已生成: ' + out);
})().catch(e => { console.error(e.stack || e); process.exit(1); });
