#!/usr/bin/env node
/**
 * 岐伯论 · 阅读工作本 DOCX 生成器（Node docx 主路线）
 *
 * 输入：print-20260926-rebuilt-v2/<专题目录>/volume-NN.md（只读）
 *       print-design-20260927/design-studio/data/images.json（图片索引，备用）
 * 输出：可用于 WPS 阅读 / 批注 / 勾画 / 局部排版的 DOCX
 *
 * 用法：
 *   node build-qbl-docx.mjs --topic A21 --volume 1 --page A5
 *   node build-qbl-docx.mjs --topic A15 --volume 1 --page B5 --note-lines 6 --article-break 1
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import QRCode from 'qrcode';
import {
  Document, Packer, Paragraph, TextRun, ImageRun, ExternalHyperlink,
  Header, Footer, PageNumber, AlignmentType, TabStopType, LeaderType,
  BorderStyle, Table, TableRow, TableCell, WidthType, VerticalAlign,
} from 'docx';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RESEARCH = path.resolve(HERE, '..', '..');           // research-rebuild
const PROJECT = path.resolve(RESEARCH, '..');              // 岐伯论
const PRINT_V2 = path.join(RESEARCH, 'print-20260926-rebuilt-v2');
const DESIGN_DATA = path.join(RESEARCH, 'print-design-20260927', 'design-studio', 'data');
const DEFAULT_OUT_DIR = path.join(RESEARCH, 'wps-sample-20260927', 'docx-output');

const MM = 56.6929; // 1mm = 56.6929 twips
const TWIP_PER_PX = 15; // 96dpi

const PAGE_PRESETS = {
  A5: { label: 'A5 148×210mm', width: Math.round(148 * MM), height: Math.round(210 * MM) },
  B5: { label: 'B5 176×250mm', width: Math.round(176 * MM), height: Math.round(250 * MM) },
  A4: { label: 'A4 210×297mm', width: Math.round(210 * MM), height: Math.round(297 * MM) },
  A6: { label: 'A6 105×148mm', width: Math.round(105 * MM), height: Math.round(148 * MM) },
};

const INK = '1F1B16';      // 墨色正文
const CINNABAR = 'A74736'; // 朱色
const SUB = '6B6258';      // 小字灰褐
const HINT = '7A6D5E';
const RULE = 'C9B99F';     // 分隔线
const NOTE_RULE = 'D9C9AE';

/** 字体可通过命令行整体替换（--font-body / --font-head / --font-meta / --font-seal） */
const asFont = (n) => ({ ascii: n, eastAsia: n, hAnsi: n });
let SONG = asFont('书宋-简');  // 正文（宋体类）
let HEAD = asFont('书宋-简');  // 标题（宋体类）
let HEI = asFont('黑体-简');   // 标签、小字、页眉页脚（黑体类）
let COVER = asFont('汉仪昌黎宋刻本原版W'); // 封面题名（宋刻本，按名引用不嵌入）
let KAI = asFont('汉仪篆书繁');  // 方印（篆书）

// ---------------------------------------------------------------- 参数
function parseArgs(argv) {
  const args = { page: 'A4', volume: 1, noteLines: 2, articleBreak: 0, seal: '岐伯论', extraNotePages: 2, qr: true, showConcepts: false, showUuid: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    const next = () => argv[++i];
    if (a === '--topic') args.topic = next();
    else if (a === '--volume') args.volume = Number(next());
    else if (a === '--page') args.page = next();
    else if (a === '--out') args.out = next();
    else if (a === '--note-lines') args.noteLines = Number(next());
    else if (a === '--article-break') args.articleBreak = Number(next());
    else if (a === '--extra-note-pages') args.extraNotePages = Number(next());
    else if (a === '--limit') args.limit = Number(next());
    else if (a === '--with-images') args.withImages = Number(next());
    else if (a === '--seal') args.seal = next();
    else if (a === '--font-body') args.fontBody = next();
    else if (a === '--font-head') args.fontHead = next();
    else if (a === '--font-meta') args.fontMeta = next();
    else if (a === '--font-seal') args.fontSeal = next();
    else if (a === '--font-cover') args.fontCover = next();
    else if (a === '--qr') args.qr = Number(next()) !== 0;
    else if (a === '--no-qr') args.qr = false;
    else if (a === '--show-concepts') args.showConcepts = true;
    else if (a === '--show-uuid') args.showUuid = true;
    else if (a === '--from') args.from = Number(next());
    else if (a === '--to') args.to = Number(next());
    else if (a === '--volume-index') args.volumeIndex = Number(next());
    else if (a === '--volume-count') args.volumeCount = Number(next());
    else if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

// ---------------------------------------------------------------- 工具
function argOut(args) {
  if (args.out) return path.resolve(args.out);
  const dir = fs.readdirSync(PRINT_V2).find((d) => d.startsWith(args.topic + '-') || d.startsWith(args.topic + '　'));
  const base = dir ? `${args.topic}-${dir.slice(args.topic.length + 1)}` : args.topic;
  if (args.volumeIndex) {
    return path.join(DEFAULT_OUT_DIR, `${base}-第${String(args.volumeIndex).padStart(2, '0')}册-阅读工作本-Node.docx`);
  }
  return path.join(DEFAULT_OUT_DIR, `${base}-阅读工作本-Node.docx`);
}

function findTopicDir(topic) {
  const dir = fs.readdirSync(PRINT_V2).find((d) => d.startsWith(topic + '-') || d.startsWith(topic + '　'));
  if (!dir) throw new Error(`未找到专题目录：${topic}`);
  return dir;
}

function findVolumeFile(topic, volume) {
  const dir = findTopicDir(topic);
  const name = `volume-${String(volume).padStart(2, '0')}.md`;
  const p = path.join(PRINT_V2, dir, name);
  if (!fs.existsSync(p)) throw new Error(`未找到卷文件：${p}`);
  return { dir, file: p };
}

/** 平衡分册模式：读取专题全部卷，合并文章后按篇索引切片（1-based，含端点） */
function loadTopicArticles(topic, from, to) {
  const dir = findTopicDir(topic);
  const full = path.join(PRINT_V2, dir);
  const files = fs.readdirSync(full).filter((f) => /^volume-\d+\.md$/.test(f)).sort();
  let all = [];
  for (const f of files) all = all.concat(parseVolume(fs.readFileSync(path.join(full, f), 'utf8')).articles);
  const start = Math.max(1, from || 1);
  const end = Math.min(all.length, to || all.length);
  return { dir, files, all, slice: all.slice(start - 1, end), start, end };
}

/** 解析 JPEG / PNG 像素尺寸（无第三方依赖） */
function imageSize(buf) {
  if (buf.length > 4 && buf[0] === 0xff && buf[1] === 0xd8) {
    let i = 2;
    while (i + 9 < buf.length) {
      if (buf[i] !== 0xff) { i++; continue; }
      const marker = buf[i + 1];
      if (marker === 0xd8 || marker === 0x01 || (marker >= 0xd0 && marker <= 0xd9)) { i += 2; continue; }
      const len = buf.readUInt16BE(i + 2);
      if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc) {
        return { height: buf.readUInt16BE(i + 5), width: buf.readUInt16BE(i + 7) };
      }
      i += 2 + len;
    }
  }
  if (buf.length > 24 && buf[0] === 0x89 && buf[1] === 0x50) {
    return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
  }
  return null;
}

// ---------------------------------------------------------------- 解析卷 Markdown
function parseVolume(text) {
  const parts = text.split(/^##\s+/m).slice(1);
  const head = text.split(/^##\s+/m)[0];
  const articles = [];
  for (const part of parts) {
    const lines = part.split(/\r?\n/);
    const m = /^(\d+)　(.+)$/.exec(lines[0].trim());
    if (!m) continue;
    const ordinal = m[1];
    const title = m[2];
    const rest = lines.slice(1).join('\n').trim();
    const article = { ordinal, title, question: null, url: null, uuid: null, meta: [], concepts: null, images: [], body: [] };
    for (const raw of rest.split(/\r?\n/)) {
      const line = raw.trim();
      if (!line || line === '---') continue;
      const img = /^!\[图\s*(\d+)\]\((.+)\)$/.exec(line);
      if (img) { article.images.push({ index: Number(img[1]), src: img[2] }); continue; }
      if (line.startsWith('**问**：')) { article.question = line.slice(5).trim(); continue; }
      if (line.startsWith('- 源 ID：')) {
        const uuidMatch = /源 ID：`?([\w-]+)`?/.exec(line);
        const urlMatch = /原文链接：(https?:\/\/\S+)/.exec(line);
        if (uuidMatch) article.uuid = uuidMatch[1];
        if (urlMatch) article.url = urlMatch[1];
        continue;
      }
      if (line.startsWith('- 原文链接：')) { article.url = line.split('原文链接：')[1].trim(); continue; }
      if (line.startsWith('- 23 概念标签：')) { article.concepts = line.split('23 概念标签：')[1].trim(); continue; }
      if (/^[-*]\s+/.test(line)) { article.meta.push(line.replace(/^[-*]\s+/, '').replace(/`/g, '')); continue; }
      if (line.startsWith('**') || line.startsWith('<!--')) continue;
      article.body.push(line);
    }
    articles.push(article);
  }
  return { head, articles };
}

function parseHead(head) {
  const info = { title: '', topicCode: '', topicName: '', scope: '', volumes: '', corpus: '', sha: '' };
  for (const raw of head.split(/\r?\n/)) {
    const line = raw.trim();
    if (line.startsWith('# ')) {
      const m = /^#\s+(\S+)　(.+?)　第\s*(\d+)\s*册（共\s*(\d+)\s*册）/.exec(line);
      if (m) { info.topicCode = m[1]; info.topicName = m[2]; info.volumeIndex = Number(m[3]); info.volumeCount = Number(m[4]); }
      info.title = line.slice(2);
      continue;
    }
    if (line.startsWith('- 专题代码：')) {
      const m = /专题代码：(\S+)　专题名称：(.+)/.exec(line);
      if (m) { info.topicCode = m[1]; info.topicName = m[2]; }
    }
    if (line.startsWith('- 专题界定：')) info.scope = line.split('专题界定：')[1].trim();
    if (line.startsWith('- 本册：')) info.volumes = line.replace(/^-\s*/, '');
    if (line.startsWith('- 语料：')) info.corpus = line.replace(/^-\s*/, '');
  }
  return info;
}

// ---------------------------------------------------------------- 段落构造
function p(text, opts = {}) {
  const {
    size = 21, bold = false, color = INK, align, indent = 0, before = 0, after = 120,
    font = SONG, style, rule, lineRule = 'auto', line = 360, tabStops, spacing,
  } = opts;
  const pPr = {};
  if (style) pPr.style = style;
  if (align) pPr.alignment = align;
  if (indent) pPr.indent = { firstLineChars: indent * 100 };
  pPr.spacing = spacing || { before, after, line, lineRule };
  if (rule) pPr.border = { bottom: { style: BorderStyle.SINGLE, size: 6, color: rule, space: 4 } };
  if (tabStops) pPr.tabStops = tabStops;
  return new Paragraph({
    ...pPr,
    children: [new TextRun({ text, bold, color, size, font })],
  });
}

function noteBlock(lines) {
  const out = [p('研究笔记', { size: 16, bold: true, color: HINT, font: HEI, before: 160, after: 60, style: 'QBLNoteLabel' })];
  for (let i = 0; i < lines; i++) {
    out.push(new Paragraph({
      style: 'QBLNoteRule',
      spacing: { before: 0, after: 200, line: 360, lineRule: 'auto' },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NOTE_RULE, space: 2 } },
      children: [new TextRun({ text: '', size: 16 })],
    }));
  }
  return out;
}

/** 朱文方印：1×1 表格，可在 WPS 中直接选中修改 */
function sealTable(text) {
  const chars = [...text];
  return new Table({
    alignment: AlignmentType.CENTER,
    width: { size: 1560, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
      bottom: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
      left: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
      right: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 1560, type: WidthType.DXA },
            margins: { top: 80, bottom: 80, left: 60, right: 60 },
            verticalAlign: VerticalAlign.CENTER,
            borders: {
              top: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
              bottom: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
              left: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
              right: { style: BorderStyle.SINGLE, size: 24, color: CINNABAR },
            },
            children: chars.map((c) => new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 0, after: 0, line: 260, lineRule: 'auto' },
              children: [new TextRun({ text: c, size: 32, bold: true, color: CINNABAR, font: KAI })],
            })),
          }),
        ],
      }),
    ],
  });
}

function imageParagraph(imgFile, maxW, maxH, caption) {
  let buf;
  try { buf = fs.readFileSync(imgFile); } catch (e) { return [p(`〔图片缺失：${path.basename(imgFile)}〕`, { size: 16, color: SUB, font: HEI, align: AlignmentType.CENTER })]; }
  const dim = imageSize(buf);
  let w = Math.round(maxW * 0.92), h = Math.round(maxW * 0.6);
  if (dim && dim.width) {
    const scale = Math.min(maxW / dim.width, maxH / dim.height, 1);
    w = Math.max(40, Math.round(dim.width * scale));
    h = Math.max(30, Math.round(dim.height * scale));
  }
  const out = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 160, after: 60 },
      children: [new ImageRun({
        type: imgFile.toLowerCase().endsWith('.png') ? 'png' : 'jpg',
        data: buf,
        transformation: { width: w, height: h },
        altText: { name: caption, title: caption, description: caption },
      })],
    }),
  ];
  if (caption) out.push(p(caption, { size: 15, color: SUB, font: HEI, align: AlignmentType.CENTER, after: 200 }));
  return out;
}

// ---------------------------------------------------------------- 文章
async function qrImage(url, size = 96) {
  if (!url) return null;
  try { return await QRCode.toBuffer(url, { type: 'png', width: size, margin: 1, errorCorrectionLevel: 'M' }); }
  catch { return null; }
}

async function articleBlocks(article, ctx, index) {
  const { volumeDir, contentPx, noteLines, articleBreak, maxImageH, qr, showConcepts, showUuid } = ctx;
  const out = [];
  const bodyChars = article.body.join('').length;
  const breakBefore = (articleBreak === 1 && index > 0)
    || (articleBreak === 2 && index > 0 && (bodyChars > 1600 || article.images.length >= 3));

  out.push(new Paragraph({
    style: 'QBLArticleTitle',
    pageBreakBefore: !!breakBefore,
    keepNext: true,
    spacing: { before: index === 0 ? 0 : 140, after: 100 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } },
    children: [new TextRun({ text: `${article.ordinal}　${article.title}`, size: 32, bold: true, color: INK, font: HEAD })],
  }));

  if (article.question) {
    out.push(new Paragraph({
      style: 'QBLQuestionLabel', keepNext: true,
      spacing: { before: 120, after: 40 },
      children: [new TextRun({ text: '提问', size: 15, bold: true, color: CINNABAR, font: HEI })],
    }));
    out.push(new Paragraph({
      style: 'QBLQuestion', keepNext: false,
      spacing: { after: 120 },
      children: [new TextRun({ text: article.question, size: 22, color: INK, font: SONG })],
    }));
  }

  out.push(new Paragraph({
    style: 'QBLBodyLabel', keepNext: true,
    spacing: { before: 120, after: 40 },
    children: [new TextRun({ text: '正文', size: 15, bold: true, color: CINNABAR, font: HEI })],
  }));
  for (let i = 0; i < article.body.length; i++) {
    const para = article.body[i];
    out.push(new Paragraph({
      style: 'QBLBody',
      keepLines: true,
      spacing: { after: 100, line: 350, lineRule: 'auto' },
      indent: { firstLineChars: 200 },
      children: [new TextRun({ text: para, size: 21, color: INK, font: SONG })],
    }));
  }

  if (article.images.length) {
    for (const img of article.images) {
      const file = path.resolve(volumeDir, img.src);
      out.push(...imageParagraph(file, contentPx, maxImageH, `图 ${img.index}　源序号 ${article.ordinal}`));
    }
  }

  if (article.meta.length || article.url) {
    out.push(new Paragraph({
      style: 'QBLResearchLabel', keepNext: true,
      spacing: { before: 160, after: 40 },
      children: [new TextRun({ text: '篇末研究信息', size: 15, bold: true, color: HINT, font: HEI })],
    }));
    const dateLine = article.meta.find((x) => x.startsWith('日期：')) || '';
    const topicLine = article.meta.find((x) => x.startsWith('主专题：')) || '';
    const secondaryLine = article.meta.find((x) => x.startsWith('副专题：')) || '';
    const pathLine = article.meta.find((x) => x.startsWith('官方对象—实践路径：')) || '';
    const qr = ctx.qr ? await qrImage(article.url, 96) : null;
    if (qr) {
      out.push(new Paragraph({
        style: 'QBLResearchMeta', spacing: { before: 0, after: 20 },
        children: [
          new ImageRun({ type: 'png', data: qr, transformation: { width: 72, height: 72 }, altText: { name: `原文二维码 ${article.ordinal}`, title: '原文入口', description: article.url || '' } }),
          new TextRun({ text: `  原文入口　${article.ordinal}　${dateLine.replace('日期：', '')}`, size: 16, color: SUB, font: HEI }),
        ],
      }));
    } else if (article.url) {
      out.push(new Paragraph({ style: 'QBLResearchMeta', spacing: { before: 0, after: 20 }, children: [new TextRun({ text: `原文入口　${article.ordinal}　`, size: 16, color: SUB, font: HEI }), new ExternalHyperlink({ link: article.url, children: [new TextRun({ text: article.url, size: 16, color: '2F5FA8', underline: {}, font: HEI })] })] }));
    }
    for (const line of [topicLine, secondaryLine, pathLine]) {
      if (line) out.push(p(line, { size: 16, color: SUB, font: HEI, after: 20, style: 'QBLResearchMeta' }));
    }
    if (showUuid && article.uuid) out.push(p(`内部 UUID：${article.uuid}`, { size: 13, color: SUB, font: HEI, after: 20, style: 'QBLResearchMeta' }));
    if (showConcepts && article.concepts) out.push(p(`候选概念：${article.concepts}`, { size: 14, color: SUB, font: HEI, after: 20, style: 'QBLResearchMeta' }));
    for (const line of article.meta) {
      if (!/^(日期：|主专题：|副专题：|官方对象—实践路径：|23 概念标签：|源 ID：|原文链接：)/.test(line)) {
        out.push(p(line, { size: 16, color: SUB, font: HEI, after: 20, style: 'QBLResearchMeta' }));
      }
    }
  }

  // 短文不机械留篇末横线；篇幅增加时渐进增加 0–2 行，完整笔记空间放在册末。
  const lines = bodyChars >= 2200 ? Math.min(2, noteLines) : bodyChars >= 900 ? Math.min(1, noteLines) : 0;
  if (lines > 0) out.push(...noteBlock(lines));
  return out;
}

// ---------------------------------------------------------------- 样式
function buildStyles() {
  const ps = (id, name, run, paragraph, basedOn, next) => ({
    id, name, run, paragraph, ...(basedOn ? { basedOn } : {}), ...(next ? { next } : {}),
  });
  return {
    default: {
      document: { run: { font: SONG, size: 21, color: INK } },
      hyperlink: { run: { color: '2F5FA8', underline: {} } },
    },
    paragraphStyles: [
      ps('QBLBody', 'QBL 正文', { font: SONG, size: 21, color: INK }, { spacing: { after: 100, line: 350, lineRule: 'auto' }, indent: { firstLineChars: 200 } }),
      ps('QBLArticleTitle', 'QBL 篇题', { font: HEAD, size: 32, bold: true, color: INK }, { spacing: { before: 0, after: 100 } }),
      ps('QBLQuestion', 'QBL 提问', { font: SONG, size: 22, color: INK }, { spacing: { after: 160, line: 360, lineRule: 'auto' } }),
      ps('QBLQuestionLabel', 'QBL 提问标签', { font: HEI, size: 15, bold: true, color: CINNABAR }, { spacing: { before: 120, after: 40 }, keepNext: true }),
      ps('QBLBodyLabel', 'QBL 正文标签', { font: HEI, size: 15, bold: true, color: CINNABAR }, { spacing: { before: 180, after: 40 } }),
      ps('QBLResearchMeta', 'QBL 研究信息', { font: HEI, size: 16, color: SUB }, { spacing: { after: 20, line: 300, lineRule: 'auto' } }),
      ps('QBLResearchLabel', 'QBL 研究标签', { font: HEI, size: 15, bold: true, color: HINT }, { spacing: { before: 200, after: 40 } }),
      ps('QBLNoteLabel', 'QBL 笔记标签', { font: HEI, size: 16, bold: true, color: HINT }, { spacing: { before: 160, after: 60 } }),
      ps('QBLNoteRule', 'QBL 笔记横线', { font: SONG, size: 16 }, { spacing: { after: 200, line: 360, lineRule: 'auto' }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NOTE_RULE, space: 2 } } }),
      ps('QBLCoverTitle', 'QBL 封面题名', { font: COVER, size: 64, bold: true, color: INK }, { alignment: AlignmentType.CENTER, spacing: { before: 2000, after: 600 } }),
      ps('QBLCoverSubtitle', 'QBL 封面专题', { font: COVER, size: 28, color: CINNABAR }, { alignment: AlignmentType.CENTER, spacing: { after: 900 } }),
      ps('QBLCoverEdition', 'QBL 封面版本', { font: COVER, size: 20, color: HINT }, { alignment: AlignmentType.CENTER, spacing: { after: 400 } }),
      ps('QBLCoverMeta', 'QBL 封面说明', { font: HEI, size: 15, color: SUB }, { alignment: AlignmentType.CENTER, spacing: { after: 120, line: 300, lineRule: 'auto' } }),
      ps('QBLFrontTitle', 'QBL 前置标题', { font: HEAD, size: 28, bold: true, color: INK }, { spacing: { after: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } } }),
      ps('QBLFrontBody', 'QBL 前置正文', { font: SONG, size: 21, color: INK }, { spacing: { after: 200, line: 360, lineRule: 'auto' }, indent: { firstLineChars: 200 } }),
      ps('QBLTOC', 'QBL 目录', { font: HEI, size: 20, color: INK }, { spacing: { after: 60, line: 320, lineRule: 'auto' } }),
      ps('QBLIndex', 'QBL 索引', { font: HEI, size: 16, color: INK }, { spacing: { after: 30, line: 300, lineRule: 'auto' } }),
      ps('QBLHint', 'QBL 提示', { font: HEI, size: 17, color: HINT }, { spacing: { before: 240, after: 120, line: 320, lineRule: 'auto' } }),
      ps('QBLHeader', 'QBL 页眉', { font: HEI, size: 17, color: HINT }, { spacing: { after: 0 } }),
      ps('QBLFooter', 'QBL 页脚', { font: HEI, size: 17, color: HINT }, { alignment: AlignmentType.CENTER, spacing: { before: 0 } }),
    ],
  };
}

// ---------------------------------------------------------------- 主流程
async function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.topic) {
    console.log('用法：node build-qbl-docx.mjs --topic A21 [--volume 1] [--page A5|A4|B5|A6] [--out file.docx] [--note-lines 4] [--article-break 1] [--extra-note-pages 2] [--seal 岐伯论] [--font-body 书宋-简] [--font-head 书宋-简] [--font-meta 黑体-简] [--font-seal 汉仪篆书繁] [--font-cover 汉仪昌黎宋刻本原版W] [--from N --to N --volume-index N --volume-count M（平衡分册模式）]');
    return;
  }
  if (args.fontBody) SONG = asFont(args.fontBody);
  if (args.fontHead) HEAD = asFont(args.fontHead);
  if (args.fontMeta) HEI = asFont(args.fontMeta);
  if (args.fontSeal) KAI = asFont(args.fontSeal);
  if (args.fontCover) COVER = asFont(args.fontCover);
  const preset = PAGE_PRESETS[args.page] || PAGE_PRESETS.A5;
  const sliceMode = !!(args.from || args.to);
  let topicDir, volumeFile, allArticles, articles, info;
  if (sliceMode) {
    const r = loadTopicArticles(args.topic, args.from, args.to);
    topicDir = r.dir;
    volumeFile = path.join(PRINT_V2, r.dir, r.files[0]);
    allArticles = r.all;
    articles = r.slice;
    info = parseHead(fs.readFileSync(volumeFile, 'utf8').split(/^##\s+/m)[0]);
    info.sliceInfo = `第 ${r.start}–${r.end} 篇 / 全专题 ${r.all.length} 篇`;
  } else {
    const r = findVolumeFile(args.topic, args.volume);
    topicDir = r.dir;
    volumeFile = r.file;
    const parsed = parseVolume(fs.readFileSync(volumeFile, 'utf8'));
    info = parseHead(parsed.head);
    allArticles = parsed.articles;
    articles = allArticles;
  }
  if (args.volumeIndex) info.volumeIndex = args.volumeIndex;
  if (args.volumeCount) info.volumeCount = args.volumeCount;
  if (args.withImages && args.withImages > 0) articles = allArticles.filter((a) => a.images.length > 0).slice(0, args.withImages);
  else if (args.limit && args.limit > 0) articles = allArticles.slice(0, args.limit);

  const margin = { top: 1021, right: 992, bottom: 1134, left: 1247, header: 709, footer: 709, gutter: 227 };
  const contentTwip = preset.width - margin.left - margin.right - margin.gutter;
  const contentPx = Math.round(contentTwip / TWIP_PER_PX);
  const maxImageH = Math.round(contentPx * 1.6);

  const ctx = {
    volumeDir: path.dirname(volumeFile),
    contentPx,
    maxImageH,
    noteLines: args.noteLines,
    articleBreak: args.articleBreak,
    qr: args.qr,
    showConcepts: args.showConcepts,
    showUuid: args.showUuid,
  };

  // 前置：封面
  const front = [];
  front.push(p('岐　伯　论', { size: 64, bold: true, align: AlignmentType.CENTER, before: 2000, after: 600, font: COVER, style: 'QBLCoverTitle' }));
  front.push(p(info.topicName || args.topic, { size: 28, color: CINNABAR, align: AlignmentType.CENTER, after: 900, font: COVER, style: 'QBLCoverSubtitle' }));
  front.push(p('阅读正文版 · 研究工作本', { size: 20, color: HINT, align: AlignmentType.CENTER, after: 400, font: COVER, style: 'QBLCoverEdition' }));
  front.push(p(`${info.topicCode}　第 ${info.volumeIndex || args.volume} 册 / 共 ${info.volumeCount || 1} 册`, { size: 20, color: HINT, align: AlignmentType.CENTER, after: 700, style: 'QBLCoverEdition' }));
  front.push(sealTable(args.seal));
  front.push(p('', { size: 20, after: 600 }));
  const countLabel = info.sliceInfo
    ? `${info.sliceInfo}　第 ${info.volumeIndex || args.volume} / ${info.volumeCount || 1} 册　版式 ${preset.label}`
    : (articles.length === allArticles.length
      ? `收录 ${articles.length} 篇　版式 ${preset.label}`
      : `样张 ${articles.length} 篇 / 全册 ${allArticles.length} 篇　版式 ${preset.label}`);
  front.push(p(countLabel, { size: 15, color: SUB, font: HEI, align: AlignmentType.CENTER, after: 120, style: 'QBLCoverMeta' }));
  front.push(new Paragraph({ pageBreakBefore: true, children: [new TextRun({ text: '' })] }));

  // 前置：本册说明
  front.push(p('本册说明', { size: 28, bold: true, after: 200, style: 'QBLFrontTitle' }));
  front.push(p(`本册为 ${info.topicCode} ${info.topicName} 的阅读工作本。正文保留发表顺序、提问、正文与篇末研究信息；篇末留有研究笔记横线，页边留有批注空间，供阅读时勾画与批注。`, { size: 21, indent: 2, after: 200, style: 'QBLFrontBody' }));
  if (info.scope) front.push(p(`专题界定：${info.scope}`, { size: 21, indent: 2, after: 200, style: 'QBLFrontBody' }));
  front.push(p('使用约定：篇题下为提问与正文；正文之后为图片；篇末以小字保留原文链接、分类标签与官方路径；页码在最终排版后回填。', { size: 21, indent: 2, after: 200, style: 'QBLFrontBody' }));
  if (info.corpus) front.push(p(info.corpus.replace(/`/g, ''), { size: 15, color: SUB, font: HEI, indent: 0, after: 200, style: 'QBLFrontBody' }));

  // 前置：目录（页码待回填）
  front.push(p('本册目录', { size: 24, bold: true, before: 320, after: 160, style: 'QBLFrontTitle' }));
  const tocTab = [{ type: TabStopType.RIGHT, position: contentTwip, leader: LeaderType.DOT }];
  for (const a of articles) {
    front.push(new Paragraph({
      style: 'QBLTOC',
      tabStops: tocTab,
      spacing: { after: 60, line: 320, lineRule: 'auto' },
      children: [
        new TextRun({ text: `${a.ordinal}　${a.title}`, size: 20, font: HEI }),
        new TextRun({ text: '\t待回填', size: 18, color: SUB, font: HEI }),
      ],
    }));
  }
  front.push(p('说明：目录页码需在 WPS 最终排版后回填；也可删除本页改用 WPS 自动目录域。', { size: 16, color: HINT, font: HEI, before: 200, after: 120, style: 'QBLHint' }));

  // 正文
  const body = [];
  for (let i = 0; i < articles.length; i++) body.push(...await articleBlocks(articles[i], ctx, i));

  // 册末：索引 + 研究笔记页
  body.push(new Paragraph({ pageBreakBefore: true, children: [new TextRun({ text: '' })] }));
  body.push(p('本册索引', { size: 28, bold: true, after: 200, style: 'QBLFrontTitle' }));
  for (const a of articles) {
    const sub = (a.meta.find((m) => m.startsWith('日期：')) || '').replace('日期：', '').split('　')[0];
    body.push(p(`${a.ordinal}　${a.title}　${sub ? '日期 ' + sub + '　' : ''}页码待回填`, { size: 16, font: HEI, after: 30, style: 'QBLIndex' }));
  }
  body.push(p('全书索引与交叉索引（副专题、官方路径、23 概念、图片、异常）另行成册，页码在最终排版后统一回填。', { size: 16, color: HINT, font: HEI, before: 200, after: 120, style: 'QBLHint' }));

  for (let i = 0; i < args.extraNotePages; i++) {
    body.push(new Paragraph({ pageBreakBefore: true, children: [new TextRun({ text: '' })] }));
    body.push(p('研究笔记页', { size: 20, bold: true, color: HINT, font: HEI, after: 120, style: 'QBLNoteLabel' }));
    body.push(...noteBlock(14));
  }

  body.push(p('WPS 编辑提示：可直接修改字体、页边距、分页与样式；方印为表格对象，可整体拖动或改写；图片可替换或缩放。', { size: 17, color: HINT, font: HEI, before: 240, style: 'QBLHint' }));

  const headerText = `岐伯论 · 阅读正文版`;
  const rightText = `${info.topicCode || args.topic}　${info.topicName || ''}　第 ${info.volumeIndex || args.volume} 册`;

  const makeHeader = () => new Header({
    children: [
      new Paragraph({
        style: 'QBLHeader',
        tabStops: [{ type: TabStopType.RIGHT, position: contentTwip }],
        spacing: { after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
        children: [
          new TextRun({ text: headerText, size: 17, color: HINT, font: HEI }),
          new TextRun({ text: '\t' + rightText, size: 17, color: HINT, font: HEI }),
        ],
      }),
    ],
  });

  const makeFooter = () => new Footer({
    children: [
      new Paragraph({
        style: 'QBLFooter',
        alignment: AlignmentType.CENTER,
        spacing: { before: 0 },
        children: [
          new TextRun({ text: '— ', size: 17, color: HINT, font: HEI }),
          new TextRun({ children: [PageNumber.CURRENT], size: 17, color: HINT, font: HEI }),
          new TextRun({ text: ' —　共 ', size: 17, color: HINT, font: HEI }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 17, color: HINT, font: HEI }),
          new TextRun({ text: ' 页', size: 17, color: HINT, font: HEI }),
        ],
      }),
    ],
  });

  const doc = new Document({
    title: `岐伯论 · ${info.topicName || args.topic} · 阅读工作本`,
    creator: '岐伯论编册生成器（Node docx）',
    description: `源卷：${path.relative(PROJECT, volumeFile)}`,
    styles: buildStyles(),
    features: { updateFields: true },
    sections: [
      {
        properties: { page: { size: { width: preset.width, height: preset.height }, margin } },
        children: front,
      },
      {
        properties: {
          page: { size: { width: preset.width, height: preset.height }, margin, pageNumbers: { start: 1 } },
        },
        headers: { default: makeHeader() },
        footers: { default: makeFooter() },
        children: body,
      },
    ],
  });

  const out = argOut(args);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(out, buf);

  const imageCount = articles.reduce((n, a) => n + a.images.length, 0);
  console.log(JSON.stringify({
    out,
    bytes: buf.length,
    topic: info.topicCode,
    topicName: info.topicName,
    volume: info.volumeIndex,
    articles: articles.length,
    images: imageCount,
    page: preset.label,
    contentPx,
    source: path.relative(PROJECT, volumeFile),
  }, null, 2));
}

main().catch((e) => { console.error('生成失败：', e); process.exit(1); });
