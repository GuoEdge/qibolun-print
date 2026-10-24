// 岐伯論 · 卷一 · 甲冊（B01）── 版面高度精确装箱版（彻底根除空页）
//
// 【病根】外层古籍方框是「单元格里套表格」的嵌套结构。只要该单元格内容高度超过
//   一页 A4 版心（734pt），WPS/Word 就无法在嵌套表格内折行，只能把整张方框推到
//   下一页 —— 于是出现「题眉孤零零占一页（看似空页）＋ 页数翻倍（237 叶）」。
//   经实测诊断：旧文件 113 个页块中绝大多数高达 790~2200pt，远超 734pt 版心。
//
// 【治法】
//   1. 不再按「段数」估算，改为按「真实物理高度 pt」逐段装箱；
//   2. 每页总预算锁定 706pt（版心 734pt，留 28pt 安全余量）；
//      逐项扣除：天头题眉 / 篇名 / 客问 / 篇末落款 / 内外框留白；
//   3. 右侧随文批校走廊「动态铺满」——行数由本页剩余高度反算，
//      使左侧正论不论长短，版框都恰好铺到页面底端，绝不半页悬空；
//   4. 换页符直接挂在「天头题眉」段上（pageBreakBefore），
//      取消独立的空段落 —— 杜绝空段落自成一叶；
//   5. 外层方框行加 cantSplit，双保险，禁止跨页撕裂。
//
// 【视觉参数】与成杰审定的《岐伯论-现代学者批校手卷本-可编辑原型.docx》逐项一致。

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, ImageRun, Footer, PageNumber
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const OUT_DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/';
const QR_DIR = path.join(OUT_DIR, 'qr_cache_b01');
const MERGED_CORPUS = path.join(OUT_DIR, 'all-articles-merged-v3.jsonl');
const CATALOG_PATH = path.join(OUT_DIR, 'workbook-40b-all-catalog.jsonl');

/* ============================ 字体矩阵 ============================ */
const FONT_HEADER     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_TITLE      = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W', hAnsi: '汉仪字酷堂会典楷书 W', cs: '汉仪字酷堂会典楷书 W' };
const FONT_Q_MARK     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_Q_TEXT     = { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W', hAnsi: '汉仪昌黎宋刻本原版W', cs: '汉仪昌黎宋刻本原版W' };
const FONT_BODY       = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_NOTE_TITLE = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W', hAnsi: '汉仪永字夏蝉 95W', cs: '汉仪永字夏蝉 95W' };
const FONT_FOOTER     = { ascii: '方正礼器碑隶书 简繁', eastAsia: '方正礼器碑隶书 简繁', hAnsi: '方正礼器碑隶书 简繁', cs: '方正礼器碑隶书 简繁' };
const FONT_PAGE_NUM   = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_SYSTEM     = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体', cs: '宋体' };

const COLOR_INK         = '23201D';
const COLOR_SEAL        = '8F2D26';
const COLOR_BORDER_LINE = '7A7368';
const COLOR_FOOTER      = '808080';
const COLOR_MUTED       = '8C857B';
const COLOR_PAGE_NUM    = '000000';

const VOL_PREFIX_TRAD = '本根敦倫';
const VOL_FULL_TRAD   = '本根敦倫 —— 血親宗族與家庭撫育';
const BOOKLET_STEM    = '甲';
const BOOKLET_TRAD    = '幼兒啟蒙與性情習慣';

/* ======================= 版面度量模型（单位 pt） ======================= */
// A4: 16838 twips 高；上下页边距 1020 / 1134 twips
const PAGE_CONTENT_PT = (16838 - 1020 - 1134) / 20;   // 734.2pt 版心
const BLOCK_BUDGET    = 688;                          // 单个页块安全预算（版心 734pt，留 46pt 余量）

const HEADER_LINE = 260 / 20;   // 13.0  天头题眉行高
const HEADER_AFTER = 140 / 20;  // 7.0
const HEADER_PT = HEADER_LINE + HEADER_AFTER;         // 20.0

const TITLE_LINE = 560 / 20;    // 28.0  篇名行高
const TITLE_PT = TITLE_LINE + 60 / 20 + 160 / 20;     // 39.0

const Q_LINE = 320 / 20;        // 16.0  客问行高
const Q_SPACE = (30 + 160) / 20; // 9.5

const BODY_LINE = 320 / 20;     // 16.0  正文行高（与生成参数一致）
const PARA_SPACE = (60 + 140) / 20; // 10.0 段前+段后

const RAIL_HEAD = 30 / 20 + 200 / 20 + 120 / 20;      // 17.5 批校栏题眉
const RAIL_LINE = 320 / 20 + 240 / 20;                // 28.0 批校虚线每行

const FILLER_HEAD = 160 / 20 + 320 / 20 + 100 / 20;   // 29.0 案语札记题眉
const FILLER_LINE = 320 / 20 + 240 / 20;              // 28.0

const OUTER_MARGIN = (140 + 140) / 20;                // 14.0 外层方框上下留白
const WS_MARGIN = (0 + 100) / 20;                     // 5.0  工作区表格下留白
const COLOPHON_PT = 48;                               // 篇末落款栏（含押角朱砂印）

const BODY_CPL_FIRST = 26;   // 正文首行可容字节数（含两字缩进）
const BODY_CPL_CONT  = 28;

/* ======================= 文本度量与切分 ======================= */
function glyphLen(s) {
  let n = 0;
  for (const ch of s) {
    n += /[\u1100-\u11FF\u2E80-\u9FFF\uA960-\uA97F\uAC00-\uD7FF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFF60\uFFE0-\uFFE6]/.test(ch) ? 1 : 0.5;
  }
  return n;
}
function bodyLines(text, indented) {
  const L = glyphLen(text);
  const first = indented ? BODY_CPL_FIRST : BODY_CPL_CONT;
  return 1 + Math.max(0, Math.ceil((L - first) / BODY_CPL_CONT));
}
function paraPt(text, indented) {
  return bodyLines(text, indented) * BODY_LINE + PARA_SPACE;
}
function questionLines(q) {
  const L = glyphLen(q);
  const cpl = 24;   // 客问字号 12pt，扣【問】前缀后约 24 字/行
  return L <= cpl ? 1 : 1 + Math.ceil((L - cpl) / (cpl + 4));
}
function questionPt(q) {
  return q ? questionLines(q) * Q_LINE + Q_SPACE : 0;
}

// 超长自然段按标点平滑拆分（单段上限 200 字，保证纵横比协调）
function splitLongParagraphs(rawParas, maxChars = 200) {
  const out = [];
  for (const p of rawParas) {
    if (glyphLen(p) <= maxChars) { out.push({ text: p, indent: true }); continue; }
    const sentences = p.split(/(?<=[。！？；：])/g);
    let curr = '';
    const push = (t) => { if (t) out.push({ text: t, indent: true }); };
    for (const s of sentences) {
      if (!s) continue;
      if (glyphLen(s) > maxChars) {
        push(curr); curr = '';
        const chars = Array.from(s);
        for (let i = 0; i < chars.length; i += maxChars) push(chars.slice(i, i + maxChars).join(''));
      } else if (glyphLen(curr + s) > maxChars && curr) {
        push(curr); curr = s;
      } else {
        curr += s;
      }
    }
    push(curr);
  }
  return out;
}

// 在句读处把一段切成「刚好填满剩余空间」的头 + 尾
function splitAtGlyph(str, maxGlyphs) {
  const chars = Array.from(str);
  let cut = 0, acc = 0;
  const sentEnds = [], anyEnds = [];
  for (let i = 0; i < chars.length; i++) {
    const g = glyphLen(chars[i]);
    if (acc + g > maxGlyphs) break;
    acc += g; cut = i + 1;
    if (/[。！？；]/.test(chars[i])) sentEnds.push(cut);
    else if (/[，、：]/.test(chars[i])) anyEnds.push(cut);
  }
  if (cut <= 0 || cut >= chars.length) return null;
  const pick = (arr) => { const ok = arr.filter(b => b >= cut * 0.6); return ok.length ? ok[ok.length - 1] : 0; };
  const at = pick(sentEnds) || pick(anyEnds) || cut;
  if (at <= 0 || at >= chars.length) return null;
  return [chars.slice(0, at).join(''), chars.slice(at).join('')];
}

/* ======================= 按高度逐页装箱 ======================= */
// 每页可用「工作区行高」= 总预算 - 天头 - 外框留白 - 工作区留白 - 篇名 - 客问 - 落款
function workspaceBudget(isFirst, hasQuestion, isLast) {
  let b = BLOCK_BUDGET - HEADER_PT - OUTER_MARGIN - WS_MARGIN;
  if (isFirst) b -= TITLE_PT;
  if (isFirst && hasQuestion) b -= questionPt(hasQuestion);
  if (isLast) b -= COLOPHON_PT;
  return b;
}

// 批校栏行数：按本页实际行高铺满
function railCount(rowHeight) {
  return Math.max(6, Math.min(30, Math.floor((rowHeight - RAIL_HEAD) / RAIL_LINE)));
}

function paginateByHeight(rawParas, question) {
  const items = splitLongParagraphs(rawParas);
  const pages = [];
  let cur = [];
  let curH = 0;

  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    const isFirst = pages.length === 0;
    const isLast = (i === items.length - 1);
    // 预判：本段放下后是否仍可能成为末页
    const budget = workspaceBudget(isFirst, isFirst ? question : null, isLast);
    const h = paraPt(it.text, it.indent);

    if (cur.length > 0 && curH + h > budget) {
      // 尝试在句读处拆开，填满本页
      const space = budget - curH;
      const linesAvail = Math.floor((space - PARA_SPACE) / BODY_LINE);
      const maxGlyphs = (it.indent ? BODY_CPL_FIRST : BODY_CPL_CONT) + Math.max(0, linesAvail - 1) * BODY_CPL_CONT;
      let done = false;
      if (linesAvail >= 2) {
        const sp = splitAtGlyph(it.text, maxGlyphs);
        if (sp && glyphLen(sp[0]) >= 8 && glyphLen(sp[1]) >= 3) {
          const headH = paraPt(sp[0], it.indent);
          if (curH + headH <= budget) {
            cur.push({ text: sp[0], indent: it.indent });
            pages.push({ items: cur, height: curH + headH });
            cur = [{ text: sp[1], indent: false }];
            curH = paraPt(sp[1], false);
            done = true;
          }
        }
      }
      if (!done) {
        pages.push({ items: cur, height: curH });
        cur = [it];
        curH = h;
      }
    } else {
      cur.push(it);
      curH += h;
    }
  }
  if (cur.length) pages.push({ items: cur, height: curH });

  // 末页必须容得下落款：反复匀段直到完全放进预算内
  {
    const capLast = workspaceBudget(false, null, true);
    let guard = 0;
    while (pages.length > 1 && pages[pages.length - 1].height > capLast && guard++ < 500) {
      const last = pages[pages.length - 1];
      if (last.items.length <= 1) break;
      const moved = last.items.pop();
      last.height -= paraPt(moved.text, moved.indent);
      pages.push({ items: [moved], height: paraPt(moved.text, moved.indent) });
    }
  }

  // 末页过短 → 从上一叶匀若干段过来（改善观感；但绝不把上一叶挖空，也绝不越预算）
  if (pages.length > 1) {
    const last = pages[pages.length - 1];
    const prev = pages[pages.length - 2];
    const capLast = workspaceBudget(false, null, true);
    const capPrev = workspaceBudget(pages.length - 2 === 0, pages.length - 2 === 0 ? question : null, false);
    let guard = 0;
    while (prev.items.length > 2 && last.height < capLast * 0.45 && guard++ < 60) {
      const cand = prev.items[prev.items.length - 1];
      const h = paraPt(cand.text, cand.indent);
      // 上一叶匀出后不得低于其预算的 80%，末叶不得越预算
      if (last.height + h > capLast) break;
      if (prev.height - h < capPrev * 0.80) break;
      prev.items.pop(); prev.height -= h;
      last.items.unshift(cand); last.height += h;
    }
  }
  return pages;
}

/* ======================= 日期 ======================= */
function toChineseDate(rawTs) {
  if (!rawTs) return '';
  const d = new Date(Number(rawTs));
  const digits = ['〇', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
  const y = String(d.getFullYear()).split('').map(c => digits[Number(c)]).join('') + '年';
  const mNum = d.getMonth() + 1;
  const m = (mNum <= 10 ? (mNum === 10 ? '十' : digits[mNum]) : (mNum === 11 ? '十一' : '十二')) + '月';
  const dNum = d.getDate();
  let dayStr = '';
  if (dNum <= 10) dayStr = (dNum === 10 ? '十' : digits[dNum]);
  else if (dNum < 20) dayStr = '十' + digits[dNum % 10];
  else if (dNum === 20) dayStr = '二十';
  else if (dNum < 30) dayStr = '二十' + digits[dNum % 10];
  else dayStr = '三十' + (dNum === 31 ? '一' : '');
  return y + m + dayStr + '日';
}

/* ======================= 单叶渲染 ======================= */
const B = { style: BorderStyle.NONE };
function noBorders() {
  return { top: B, bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B };
}

function buildArticlePage(opts) {
  const { title, isContinuation, question, paragraphs, qrPngPath, showFooter, chineseDate } = opts;

  const pageElements = [];

  // 天头题眉（出框居中）—— 换页符挂在此段
  pageElements.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    pageBreakBefore: true,
    spacing: { before: 0, after: 140, line: 260, lineRule: 'atLeast' },
    children: [new TextRun({
      text: isContinuation ? '岐伯論 · ' + title + '（承前）' : '岐伯論 · ' + VOL_PREFIX_TRAD,
      font: FONT_HEADER, size: 22, color: COLOR_SEAL, letterSpacing: 20
    })]
  }));

  const inner = [];

  // 篇名（框内顶端居中）
  if (!isContinuation) {
    inner.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 60, after: 160, line: 560, lineRule: 'atLeast' },
      children: [new TextRun({
        text: title, font: FONT_TITLE, size: 44, bold: true, color: '1A1715', letterSpacing: 40
      })]
    }));
  }

  const left = [];

  // 客问问难
  if (!isContinuation && question) {
    left.push(new Paragraph({
      spacing: { before: 30, after: 160, line: 320, lineRule: 'atLeast' },
      border: {
        left: { style: BorderStyle.SINGLE, size: 16, color: COLOR_SEAL, space: 8 },
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'DEDAD0', space: 8 }
      },
      children: [
        new TextRun({ text: '【問】', font: FONT_Q_MARK, bold: true, size: 28, color: COLOR_SEAL }),
        new TextRun({ text: ' ', font: FONT_Q_MARK, size: 19, color: COLOR_SEAL }),
        new TextRun({ text: question, font: FONT_Q_TEXT, bold: true, size: 24, color: '453F3A' })
      ]
    }));
  }

  // 正文
  for (const it of paragraphs) {
    const o = {
      spacing: { before: 60, after: 140, line: 320, lineRule: 'atLeast' },
      alignment: AlignmentType.BOTH,
      children: [new TextRun({ text: it.text, font: FONT_BODY, size: 23, color: COLOR_INK })]
    };
    if (it.indent) o.indent = { firstLine: 460 };
    left.push(new Paragraph(o));
  }

  // 计算已用高度 → 反算批校栏行数与札记行数
  let usedH = 0;
  if (!isContinuation && question) usedH += questionPt(question);
  for (const it of paragraphs) usedH += paraPt(it.text, it.indent);

  const isLast = !!showFooter;
  const budget = workspaceBudget(!isContinuation, !isContinuation ? question : null, isLast);

  // 末叶空白较多 → 补案语札记，把版心填满
  let fillerLines = 0;
  if (isLast) {
    const leftover = budget - usedH;
    if (leftover >= FILLER_HEAD + FILLER_LINE * 3) {
      fillerLines = Math.min(12, Math.floor((leftover - FILLER_HEAD) / FILLER_LINE) - 1);
    }
    if (fillerLines > 0) {
      left.push(new Paragraph({
        spacing: { before: 160, after: 100, line: 320, lineRule: 'atLeast' },
        border: { top: { style: BorderStyle.DASHED, size: 4, color: 'D8D4C8', space: 6 } },
        children: [new TextRun({ text: '〔 案 語 札 記 〕', font: FONT_NOTE_TITLE, size: 16, color: 'A8A297', letterSpacing: 20 })]
      }));
      for (let k = 0; k < fillerLines; k++) {
        left.push(new Paragraph({
          spacing: { after: 240, line: 320, lineRule: 'atLeast' },
          border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
          children: [new TextRun({ text: ' ', size: 20 })]
        }));
      }
    }
  }

  const leftH = usedH + (fillerLines > 0 ? FILLER_HEAD + fillerLines * FILLER_LINE : 0);
  const rowTarget = Math.max(leftH, 0);
  const nRail = railCount(budget);

  // 右侧随文批校走廊（铺满本页剩余高度）
  const right = [new Paragraph({
    spacing: { before: 30, after: 120, line: 200, lineRule: 'atLeast' },
    children: [new TextRun({ text: '〔 随 文 批 校 〕', font: FONT_NOTE_TITLE, size: 16, color: 'B0A99F', letterSpacing: 20 })]
  })];
  for (let i = 0; i < nRail; i++) {
    right.push(new Paragraph({
      spacing: { after: 240, line: 320, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    }));
  }

  inner.push(new Table({
    width: { size: 9000, type: WidthType.DXA },
    borders: noBorders(),
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 6850, type: WidthType.DXA },
          borders: { right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' } },
          margins: { top: 0, bottom: 100, left: 0, right: 200 },
          children: left
        }),
        new TableCell({
          width: { size: 2150, type: WidthType.DXA },
          margins: { top: 0, bottom: 100, left: 200, right: 0 },
          children: right
        })
      ]
    })]
  }));

  // 篇末落款题注栏 + 押角朱砂小印二维码
  if (showFooter) {
    let qrImage = null;
    if (qrPngPath && fs.existsSync(qrPngPath)) {
      qrImage = new ImageRun({ data: fs.readFileSync(qrPngPath), transformation: { width: 34, height: 34 } });
    }
    inner.push(new Table({
      width: { size: 9000, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC' },
        bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B
      },
      rows: [new TableRow({
        children: [
          new TableCell({
            width: { size: 7600, type: WidthType.DXA },
            margins: { top: 140, bottom: 40, left: 0, right: 100 },
            children: [
              new Paragraph({
                spacing: { before: 0, after: 30, line: 260, lineRule: 'atLeast' },
                children: [new TextRun({
                  text: '〔 專 題 〕 ' + VOL_FULL_TRAD + ' · ' + BOOKLET_STEM + '冊 ' + BOOKLET_TRAD,
                  font: FONT_FOOTER, size: 20, color: COLOR_FOOTER
                })]
              }),
              new Paragraph({
                spacing: { before: 0, after: 0, line: 260, lineRule: 'atLeast' },
                children: [new TextRun({ text: '〔 錄 於 〕 ' + chineseDate, font: FONT_FOOTER, size: 20, color: COLOR_FOOTER })]
              })
            ]
          }),
          new TableCell({
            width: { size: 1400, type: WidthType.DXA },
            margins: { top: 120, bottom: 40, left: 0, right: 0 },
            children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: qrImage ? [qrImage] : [] })]
          })
        ]
      })]
    }));
  }

  // 外层古籍双墨线方框（行禁止跨页撕裂）
  pageElements.push(new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: 180, right: 180 },
        children: inner
      })]
    })]
  }));

  return { elements: pageElements, leftH, budget, nRail, fillerLines };
}

/* ======================= 扉页与目录 ======================= */
function buildFrontMatter(articles) {
  const els = [];

  const coverBox = [
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 1600, after: 300 },
      children: [new TextRun({ text: '岐  伯  論', font: FONT_HEADER, size: 36, color: COLOR_SEAL, letterSpacing: 40 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 0, after: 600 },
      children: [new TextRun({ text: '【 卷  一 】 本 根 敦 倫', font: FONT_HEADER, size: 26, color: '5C544D', letterSpacing: 20 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 0, after: 300 },
      border: { bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE, space: 12 } },
      children: [new TextRun({ text: '甲冊 · 幼兒啟蒙與性情習慣', font: FONT_TITLE, size: 48, bold: true, color: '1A1715', letterSpacing: 30 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 400, after: 1600 },
      children: [new TextRun({ text: '全冊通收五十二篇 · 研讀批校工作本', font: FONT_FOOTER, size: 22, color: COLOR_MUTED, letterSpacing: 15 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 900, after: 400 },
      children: [new TextRun({ text: '成 傑  手 訂 批 閱', font: FONT_NOTE_TITLE, size: 22, color: '7D756C', letterSpacing: 30 })]
    })
  ];

  els.push(new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 200, bottom: 200, left: 180, right: 180 },
        children: coverBox
      })]
    })]
  }));

  // 目录（前置一段独立换页符，确保目录独占一叶）
  els.push(new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 0, line: 240, lineRule: 'atLeast' }, children: [] }));
  const tocBox = [new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 100, after: 180, line: 420, lineRule: 'atLeast' },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 } },
    children: [new TextRun({ text: '本 冊 篇 目 總 覽', font: FONT_TITLE, size: 32, bold: true, color: '1A1715', letterSpacing: 25 })]
  })];

  const tocRows = [];
  for (let i = 0; i < articles.length; i += 2) {
    const mk = (idx, a) => a ? [new Paragraph({
      spacing: { before: 40, after: 40, line: 300, lineRule: 'atLeast' },
      children: [
        new TextRun({ text: idx + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
        new TextRun({ text: '《' + a.title + '》', font: FONT_BODY, size: 20, bold: true, color: COLOR_INK }),
        new TextRun({ text: ' ' + a.charCount + '字', font: FONT_SYSTEM, size: 14, color: COLOR_MUTED })
      ]
    })] : [];
    tocRows.push(new TableRow({
      children: [
        new TableCell({ width: { size: 4500, type: WidthType.DXA }, margins: { top: 20, bottom: 20, left: 40, right: 40 }, children: mk(i + 1, articles[i]) }),
        new TableCell({ width: { size: 4500, type: WidthType.DXA }, margins: { top: 20, bottom: 20, left: 40, right: 40 }, children: mk(i + 2, articles[i + 1]) })
      ]
    }));
  }
  const tocTable = new Table({ width: { size: 9000, type: WidthType.DXA }, borders: noBorders(), rows: tocRows });
  tocBox.push(tocTable);

  els.push(new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: 180, right: 180 },
        children: tocBox
      })]
    })]
  }));

  return els;
}

/* ======================= 编译 ======================= */
const b01Catalog = [];
for (const l of fs.readFileSync(CATALOG_PATH, 'utf-8').split(String.fromCharCode(10))) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  if (d.booklet_code === 'B01') b01Catalog.push(d);
}
const corpusMap = {};
for (const l of fs.readFileSync(MERGED_CORPUS, 'utf-8').split(String.fromCharCode(10))) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  corpusMap[d.id] = d;
}

const arts = b01Catalog.map(c => ({ ...c, text: (corpusMap[c.original_id] || {}).text || '' }));
arts.forEach(a => a.charCount = a.text.length);

const docElements = buildFrontMatter(arts);

let pageCount = 2;   // 封面 + 目录
let overflow = 0;
const report = [];

for (const art of arts) {
  const chineseDate = toChineseDate(art.published_at);
  const qrPngPath = path.join(QR_DIR, 'qr_' + art.workbook_ordinal + '.png');
  const rawParas = (art.text || '').trim().split(String.fromCharCode(10)).map(s => s.trim()).filter(Boolean);

  const pages = paginateByHeight(rawParas, art.question);

  pages.forEach((pg, i) => {
    const isFirst = i === 0;
    const isLast = i === pages.length - 1;
    const res = buildArticlePage({
      title: art.title,
      isContinuation: !isFirst,
      question: isFirst ? art.question : null,
      paragraphs: pg.items,
      qrPngPath,
      showFooter: isLast,
      chineseDate
    });
    docElements.push(...res.elements);
    pageCount++;

    // 页块实际高度（天头 + 外框留白 + 内层最大高 + 落款；leftH 已含客问）
    let blockH = HEADER_PT + OUTER_MARGIN + Math.max(res.leftH, res.nRail * RAIL_LINE + RAIL_HEAD) + WS_MARGIN;
    if (isFirst) blockH += TITLE_PT;
    if (isLast) blockH += COLOPHON_PT;
    if (blockH > PAGE_CONTENT_PT) overflow++;
    report.push({
      篇: art.title, 叶: i + 1, 篇内叶数: pages.length,
      正文段数: pg.items.length, 左栏高: +res.leftH.toFixed(1),
      批校行: res.nRail, 札记行: res.fillerLines,
      页块高: +blockH.toFixed(1), 超限: blockH > PAGE_CONTENT_PT
    });
  });
}

console.log('篇数: ' + arts.length);
console.log('总叶数（含扉页目录）: ' + pageCount);
console.log('版心高度: ' + PAGE_CONTENT_PT.toFixed(1) + 'pt   页块预算: ' + BLOCK_BUDGET + 'pt');
console.log('超限页块: ' + overflow + '  (必须为 0)');
const hs = report.map(r => r.页块高).sort((a, b) => b - a);
console.log('页块最高前五: ' + hs.slice(0, 5).join(' / ') + ' pt');
const fill = report.map(r => r.左栏高 / BLOCK_BUDGET);
console.log('平均左栏填充率: ' + (fill.reduce((a, b) => a + b, 0) / fill.length * 100).toFixed(1) + '%');
fs.writeFileSync(path.join(OUT_DIR, '_pagination-report-B01.json'), JSON.stringify(report, null, 1));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT_BODY, size: 23, color: COLOR_INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1020, right: 1020, bottom: 1134, left: 1587 }
      }
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [
          new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
          new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
          new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
        ]
      })] }),
      even: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.LEFT,
        children: [
          new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
          new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
          new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
        ]
      })] })
    },
    children: docElements
  }]
});

const out = path.join(OUT_DIR, '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(out, buf);
  console.log('已生成: ' + out + '  (' + (buf.length / 1024).toFixed(1) + ' KB)');
}).catch(e => { console.error(e); process.exit(1); });
