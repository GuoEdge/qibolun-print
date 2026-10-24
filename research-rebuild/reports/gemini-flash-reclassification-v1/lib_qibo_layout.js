// 岐伯論 · 排版引擎（共用库）
// ---------------------------------------------------------------------------
// 【核心问题】
//  1) 古籍外框是「单元格里嵌表格」结构，高度一旦超过一页版心，WPS/Word 不会在嵌套
//     表格内折行，只会把整张框推到下一叶 → 出现空页。故必须按真实物理高度（pt）装箱。
//  2) 旧版页边距 bottom=1134 而 footer=708，页脚几乎贴在版心下沿，表格稍微满版就会
//     「挤占」页码。现改为 bottom=1500 / footer=900，给页脚让出充裕空间。
//  3) 行高必须可预测：全篇段落显式指定 lineRule=atLeast，并在后处理中关闭 snapToGrid，
//     避免 WPS 按文档网格（linePitch=360，即 18pt）重排行高导致版面失控。
//
// 【版面度量】A4 = 16838 twips（842pt）
//   上边距 1020(51pt) / 下边距 1500(75pt) → 版心 14318 twips = 715.9pt
//   单叶块预算 BLOCK_BUDGET = 655pt（版心下再留 61pt + 页脚前 14pt = 75pt 净空）
// ---------------------------------------------------------------------------

const fs = require('fs');
const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, ImageRun, TableLayoutType, HeightRule,
  Tab, TabStopType, LeaderType
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

/* ============================ 字体矩阵 ============================ */
const FONT_HEADER     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_TITLE      = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W', hAnsi: '汉仪字酷堂会典楷书 W', cs: '汉仪字酷堂会典楷书 W' };
const FONT_Q_MARK     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_Q_TEXT     = { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W', hAnsi: '汉仪昌黎宋刻本原版W', cs: '汉仪昌黎宋刻本原版W' };
const FONT_BODY       = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_NOTE_TITLE = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W', hAnsi: '汉仪永字夏蝉 95W', cs: '汉仪永字夏蝉 95W' };
const FONT_FOOTER     = { ascii: '方正礼器碑隶书 简繁', eastAsia: '方正礼器碑隶书 简繁', hAnsi: '方正礼器碑隶书 简繁', cs: '方正礼器碑隶书 简繁' };
const FONT_SYSTEM     = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体', cs: '宋体' };
const FONT_TOC_LEAF   = { ascii: '汉仪字酷堂荫嘉楷书 W', eastAsia: '汉仪字酷堂荫嘉楷书 W', hAnsi: '汉仪字酷堂荫嘉楷书 W', cs: '汉仪字酷堂荫嘉楷书 W' };

const COLOR_INK         = '23201D';
const COLOR_SEAL        = '8F2D26';
const COLOR_BORDER_LINE = '7A7368';
const COLOR_FOOTER      = '808080';
const COLOR_MUTED       = '8C857B';

/* ======================= 版面度量（pt） ======================= */
const MARGIN_TOP = 900, MARGIN_BOTTOM = 1500, MARGIN_LEFT = 1587, MARGIN_RIGHT = 1020;
const FOOTER_DIST = 900;
const PAGE_CONTENT_PT = (16838 - MARGIN_TOP - MARGIN_BOTTOM) / 20;   // 715.9
const BLOCK_BUDGET = 600;                                            // WPS 兼容预算：为嵌套表格实际行高留出余量
const FRAME_MIN_PT = 600;                                            // 统一正文框的最小视觉高度

const HEADER_PT  = 260 / 20 + 140 / 20;        // 20.0  天头题眉
const TITLE_PT   = 560 / 20 + 60 / 20 + 160 / 20; // 39.0 篇名
const Q_LINE     = 320 / 20;                    // 16.0
const Q_SPACE    = (30 + 160) / 20;             // 9.5
const BODY_LINE  = 320 / 20;                    // 16.0
const PARA_SPACE = (60 + 140) / 20;             // 10.0
const RAIL_HEAD  = 30 / 20 + 200 / 20 + 120 / 20; // 17.5
const RAIL_LINE  = 320 / 20 + 240 / 20;         // 28.0
const FILLER_HEAD = 160 / 20 + 320 / 20 + 100 / 20; // 29.0
const FILLER_LINE = 320 / 20 + 240 / 20;        // 28.0
const OUTER_MARGIN = (140 + 140) / 20;          // 14.0
const WS_MARGIN  = (0 + 100) / 20;              // 5.0
const COLOPHON_PT = 48;                         // 篇末落款栏
const FRAME_INNER_PT = FRAME_MIN_PT - OUTER_MARGIN; // 586：正文框内净高（框高减去外框单元格上下留白）

// 边界标记：提问者叙述结束、岐伯入话的句读符号
const MARKER_QIBO = '〔 岐 伯 語 〕';
// 提问者叙述的起始标签
const LABEL_NARRATIVE = '〔 原 問 〕';

const CPL_FIRST = 26, CPL_CONT = 28;

/* ---- 横向尺度（dxa）----
   版心宽 = 11906 - 1587(左) - 1020(右) = 9299 dxa
   旧版外框 9355 > 版心，WPS 会强制重排列宽并改变行数 → 必须收回版心之内。 */
const TEXT_W      = 11906 - MARGIN_LEFT - MARGIN_RIGHT;   // 9299
const OUTER_TBL_W = TEXT_W - 19;                          // 9280  外框
const OUTER_PAD   = 180;                                  // 外框单元格左右留白
const INNER_TBL_W = OUTER_TBL_W - OUTER_PAD * 2;          // 8920  左右双栏
const COL_LEFT_W  = 6850;                                 // 正文栏：保持原型宽度，避免改变正文换行
const COL_RIGHT_W = INNER_TBL_W - COL_LEFT_W;             // 2070  批校栏
const COL_FOOT_L  = 7520;                                 // 落款左（專題/錄於）
const COL_FOOT_R  = INNER_TBL_W - COL_FOOT_L;             // 1400  二维码押角

/* ======================= 文本度量 ======================= */
function glyphLen(s) {
  let n = 0;
  for (const ch of s) {
    n += /[\u1100-\u11FF\u2E80-\u9FFF\uA960-\uA97F\uAC00-\uD7FF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFF60\uFFE0-\uFFE6]/.test(ch) ? 1 : 0.5;
  }
  return n;
}
function bodyLines(text, indented) {
  const L = glyphLen(text);
  const first = indented ? CPL_FIRST : CPL_CONT;
  return 1 + Math.max(0, Math.ceil((L - first) / CPL_CONT));
}
function paraPt(text, indented) {
  if (text === MARKER_QIBO || text === LABEL_NARRATIVE) return 24;
  return bodyLines(text, indented) * BODY_LINE + PARA_SPACE;
}
function questionLines(q) {
  const L = glyphLen(q);
  return L <= 24 ? 1 : 1 + Math.ceil((L - 24) / 28);
}
function questionPt(q) {
  return q ? questionLines(q) * Q_LINE + Q_SPACE : 0;
}

// 段落切分：接受 {text, kind} 或纯字符串，长段按句读切分并保留 kind
function splitLongParagraphs(items, maxChars = 200) {
  const out = [];
  for (const it of items) {
    const p = typeof it === 'string' ? it : it.text;
    const kind = (typeof it === 'object' && it.kind) || undefined;
    if (!p) continue;
    if (glyphLen(p) <= maxChars) { out.push({ text: p, indent: true, kind }); continue; }
    const sentences = p.split(/(?<=[。！？；：])/g);
    let curr = '';
    const push = (t) => { if (t) out.push({ text: t, indent: true, kind }); };
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
  const pick = (a) => { const ok = a.filter(b => b >= cut * 0.6); return ok.length ? ok[ok.length - 1] : 0; };
  const at = pick(sentEnds) || pick(anyEnds) || cut;
  if (at <= 0 || at >= chars.length) return null;
  return [chars.slice(0, at).join(''), chars.slice(at).join('')];
}

/* ======================= 逐叶装箱 ======================= */
// 左栏正文预算：可见框内净高扣除标题/问（都在左栏）与末叶落款（全宽）。
// 题眉已移入外层工作区，与外框同属一个不可拆单元，故不占用框内净高。
// 提问者叙述（kind=narrative）与岐伯回答一样作为正文逐叶排流，不单独预留。
// 
// 2026-10-08 修正：回退预算系数到 1.0，确保所有页左栏不超 586pt、外框统一保持 atLeast 600pt
// 不自动扩展。1.05 倍虽提升填充率但导致部分页外框超 600pt → 高度不一致 + 与页码重叠。
function bodyBudget(isFirst, question, isLast) {
  let b = FRAME_INNER_PT;  // 586pt，严格不超框内净高
  if (isFirst) b -= TITLE_PT;
  if (isFirst && question) b -= questionPt(question);
  if (isLast) b -= COLOPHON_PT;
  return b;
}

// 右栏批校线目标：框内净高，只扣末叶全宽落款，不扣标题/问（它们都在左栏）
function railTarget(isLast) {
  return FRAME_INNER_PT - (isLast ? COLOPHON_PT : 0);
}
function railCount(isLast) {
  // 末叶还要容纳札记线与篇末落款，主动留出一行的 WPS 实际排版余量。
  const reserve = isLast ? RAIL_LINE : 0;
  const target = railTarget(isLast);
  return Math.max(6, Math.min(30, Math.floor((target - RAIL_HEAD - reserve) / RAIL_LINE)));
}

function paginateByHeight(items, question) {
  const seq = splitLongParagraphs(items);
  const pages = [];
  let cur = [], curH = 0;

  for (let i = 0; i < seq.length; i++) {
    const it = seq[i];
    const isFirst = pages.length === 0;
    const isLast = (i === seq.length - 1);
    const budget = bodyBudget(isFirst, isFirst ? question : null, isLast);
    const h = paraPt(it.text, it.indent);

    if (cur.length > 0 && curH + h > budget) {
      const space = budget - curH;
      const linesAvail = Math.floor((space - PARA_SPACE) / BODY_LINE);
      const maxGlyphs = (it.indent ? CPL_FIRST : CPL_CONT) + Math.max(0, linesAvail - 1) * CPL_CONT;
      let done = false;
      if (linesAvail >= 2) {
        const sp = splitAtGlyph(it.text, maxGlyphs);
        if (sp && glyphLen(sp[0]) >= 8 && glyphLen(sp[1]) >= 3) {
          const headH = paraPt(sp[0], it.indent);
          if (curH + headH <= budget) {
            cur.push({ text: sp[0], indent: it.indent, kind: it.kind });
            pages.push({ items: cur, height: curH + headH });
            cur = [{ text: sp[1], indent: false, kind: it.kind }];
            curH = paraPt(sp[1], false);
            done = true;
          }
        }
      }
      if (!done) {
        pages.push({ items: cur, height: curH });
        cur = [it]; curH = h;
      }
    } else {
      cur.push(it); curH += h;
    }
  }
  if (cur.length) pages.push({ items: cur, height: curH });

  // 末叶须容得下落款
  {
    const capLast = bodyBudget(false, null, true);
    let guard = 0;
    while (pages.length > 1 && pages[pages.length - 1].height > capLast && guard++ < 500) {
      const last = pages[pages.length - 1];
      if (last.items.length <= 1) break;
      const moved = last.items.pop();
      last.height -= paraPt(moved.text, moved.indent);
      pages.push({ items: [moved], height: paraPt(moved.text, moved.indent) });
    }
  }

  // 末叶过短 → 匀若干段（不动摇上一叶的充实度）
  if (pages.length > 1) {
    const last = pages[pages.length - 1];
    const prev = pages[pages.length - 2];
    const capLast = bodyBudget(false, null, true);
    const capPrev = bodyBudget(pages.length - 2 === 0, pages.length - 2 === 0 ? question : null, false);
    let guard = 0;
    while (prev.items.length > 2 && last.height < capLast * 0.45 && guard++ < 60) {
      const cand = prev.items[prev.items.length - 1];
      const h = paraPt(cand.text, cand.indent);
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
  const dig = ['〇', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
  const y = String(d.getFullYear()).split('').map(c => dig[Number(c)]).join('') + '年';
  const mNum = d.getMonth() + 1;
  const m = (mNum <= 10 ? (mNum === 10 ? '十' : dig[mNum]) : (mNum === 11 ? '十一' : '十二')) + '月';
  const dn = d.getDate();
  let day = '';
  if (dn <= 10) day = (dn === 10 ? '十' : dig[dn]);
  else if (dn < 20) day = '十' + dig[dn % 10];
  else if (dn === 20) day = '二十';
  else if (dn < 30) day = '二十' + dig[dn % 10];
  else day = '三十' + (dn === 31 ? '一' : '');
  return y + m + day + '日';
}

/* ======================= 单叶渲染 ======================= */
const B = { style: BorderStyle.NONE };
const noBorders = () => ({ top: B, bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B });

// ctx: { volPrefix, volFull, stem, bookletTrad }
function buildArticlePage(opts, ctx) {
  const { title, isContinuation, question, paragraphs, qrPngPath, showFooter, chineseDate, startOfSection = false } = opts;

  // 天头题眉：移入外层不可拆工作区单元格，与可见正文框成为同一个表格行的内容。
  // 这样 WPS/Word 无法把题眉单独留在一页——它与正文框是同一个不可拆单元。
  const headerPara = new Paragraph({
    alignment: AlignmentType.CENTER,
    pageBreakBefore: !startOfSection,
    keepNext: true,
    spacing: { before: 0, after: 140, line: 260, lineRule: 'atLeast' },
    children: [new TextRun({
      text: isContinuation ? '岐伯論 · ' + title + '（承前）' : '岐伯論 · ' + ctx.volPrefix + (ctx.unitName ? ' · ' + ctx.unitName : ''),
      font: FONT_HEADER, size: 22, color: COLOR_SEAL, letterSpacing: 20
    })]
  });

  const inner = [];
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

  // 正文段落按 kind 分流：narrative=提问者叙述（宋刻本淡墨），marker=入话标记，其余=岐伯答
  for (const it of paragraphs) {
    if (it.text === MARKER_QIBO) {
      left.push(new Paragraph({
        spacing: { before: 180, after: 140, line: 260, lineRule: 'atLeast' },
        border: { top: { style: BorderStyle.SINGLE, size: 8, color: COLOR_SEAL, space: 6 } },
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: MARKER_QIBO, font: FONT_NOTE_TITLE, bold: true, size: 17, color: COLOR_SEAL, letterSpacing: 20 })]
      }));
      continue;
    }
    if (it.kind === 'narrative-label') {
      left.push(new Paragraph({
        spacing: { before: 60, after: 60, line: 260, lineRule: 'atLeast' },
        children: [new TextRun({ text: it.text, font: FONT_NOTE_TITLE, bold: true, size: 16, color: '8C857B', letterSpacing: 20 })]
      }));
      continue;
    }
    const isNarrative = it.kind === 'narrative';
    const o = {
      spacing: { before: 60, after: 140, line: 320, lineRule: 'atLeast' },
      alignment: AlignmentType.BOTH,
      children: [new TextRun({
        text: it.text,
        font: isNarrative ? FONT_Q_TEXT : FONT_BODY,
        size: 23,
        color: isNarrative ? '5A534B' : COLOR_INK
      })]
    };
    if (it.indent) o.indent = { firstLine: 460 };
    left.push(new Paragraph(o));
  }

  let usedH = 0;
  if (!isContinuation && question) usedH += questionPt(question);
  for (const it of paragraphs) usedH += paraPt(it.text, it.indent);

  const isLast = !!showFooter;
  const budget = bodyBudget(!isContinuation, !isContinuation ? question : null, isLast);

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
  const nRail = railCount(isLast);

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
    width: { size: INNER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [COL_LEFT_W, COL_RIGHT_W],
    borders: noBorders(),
    rows: [new TableRow({
      // 内层双栏允许在外框内自然排流；不可拆约束只放在外层工作区。
      children: [
        new TableCell({
          width: { size: COL_LEFT_W, type: WidthType.DXA },
          borders: { right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' } },
          margins: { top: 0, bottom: 100, left: 0, right: 200 },
          children: left
        }),
        new TableCell({
          width: { size: COL_RIGHT_W, type: WidthType.DXA },
          margins: { top: 0, bottom: 100, left: 200, right: 0 },
          children: right
        })
      ]
    })]
  }));

  if (showFooter) {
    let qrImage = null;
    if (qrPngPath && fs.existsSync(qrPngPath)) {
      // 二维码图片：明确指定PNG格式，尺寸50x50pt
      qrImage = new ImageRun({ 
        data: fs.readFileSync(qrPngPath), 
        transformation: { width: 50, height: 50 },
        type: 'png'
      });
    }
    inner.push(new Table({
      width: { size: INNER_TBL_W, type: WidthType.DXA },
      layout: TableLayoutType.FIXED,
      columnWidths: [COL_FOOT_L, COL_FOOT_R],
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC' },
        bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B
      },
      rows: [new TableRow({
        children: [
          new TableCell({
            width: { size: COL_FOOT_L, type: WidthType.DXA },
            margins: { top: 140, bottom: 40, left: 0, right: 100 },
            children: [
              new Paragraph({
                spacing: { before: 0, after: 30, line: 260, lineRule: 'atLeast' },
                children: [new TextRun({
                  text: '〔 專 題 〕 ' + ctx.volFull + ' · ' + ctx.stem + '冊 ' + ctx.bookletTrad,
                  font: FONT_FOOTER, size: 20, color: COLOR_FOOTER
                })]
              }),
              ...(question ? [new Paragraph({
                spacing: { before: 0, after: 0, line: 260, lineRule: 'atLeast' },
                children: [new TextRun({
                  text: '〔 原 問 〕 ' + question,
                  font: FONT_FOOTER, size: 20, color: COLOR_FOOTER
                })]
              })] : []),
            ]
          }),
          new TableCell({
            width: { size: COL_FOOT_R, type: WidthType.DXA },
            margins: { top: 120, bottom: 40, left: 0, right: 0 },
            children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: qrImage ? [qrImage] : [] })]
          })
        ]
      })]
    }));
  }

  // 可见古籍正文框（内层，带双墨线边框）
  const frame = new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [OUTER_TBL_W],
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      cantSplit: true,
      height: { value: FRAME_MIN_PT * 20, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: OUTER_PAD, right: OUTER_PAD },
        children: inner
      })]
    })]
  });

  // 外层工作区：无边框、不可拆，把题眉与可见正文框绑成同一个不可分割的整体。
  // 这是「题眉孤立成页」的结构性解法——只要外层行 cantSplit，
  // WPS 就不能把题眉留在上一页、把方框推到下一页。
  const pageElements = [new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [OUTER_TBL_W],
    borders: noBorders(),
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 0, bottom: 0, left: 0, right: 0 },
        children: [headerPara, frame]
      })]
    })]
  })];

  return { elements: pageElements, leftH, budget, nRail, fillerLines };
}

/* ======================= 扉页 ======================= */
// head: { volName, bookletLabel, subLine }
function buildCover(head) {
  const box = [
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 1500, after: 260, line: 480, lineRule: 'atLeast' },
      children: [new TextRun({ text: '岐  伯  論', font: FONT_HEADER, size: 36, color: COLOR_SEAL, letterSpacing: 40 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 0, after: 520, line: 360, lineRule: 'atLeast' },
      children: [new TextRun({ text: head.volName, font: FONT_HEADER, size: 26, color: '5C544D', letterSpacing: 20 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 0, after: 260, line: 700, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE, space: 12 } },
      children: [new TextRun({ text: head.bookletLabel, font: FONT_TITLE, size: 48, bold: true, color: '1A1715', letterSpacing: 30 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 340, after: 1500, line: 340, lineRule: 'atLeast' },
      children: [new TextRun({ text: head.subLine, font: FONT_FOOTER, size: 22, color: COLOR_MUTED, letterSpacing: 15 })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 800, after: 340, line: 340, lineRule: 'atLeast' },
      children: [new TextRun({ text: '成 傑  手 訂 批 閱', font: FONT_NOTE_TITLE, size: 22, color: '7D756C', letterSpacing: 30 })]
    })
  ];
  return new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 200, bottom: 200, left: OUTER_PAD, right: OUTER_PAD },
        children: box
      })]
    })]
  });
}

// 1pt 隔离段：插在两张相邻表格之间，避免 WPS/Word 把属性不同的相邻表格并成一张。
// 不设 pageBreakBefore——它只起隔离作用，分页由后续表格的 cantSplit 行自然溢出完成。
const spacerPara = () => new Paragraph({
  spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: []
});

// 整页留白：占满版心的无边框不可拆表格（EXACT 14318tw = 715.9pt，版心 721.9pt 余 6pt）。
// 鸿蒙 WPS 对「连续空段 + pageBreakBefore」渲染不稳定（乙册-中曾多出一张空白页），
// 留白页改为实体整页表格：放不进当前页剩余空间时整行推到下一页，行为在所有渲染器下一致。
// 用法：前一张表格 + spacerPara() + buildBlankPage() + spacerPara() + 后一张表格。
function buildBlankPage() {
  return new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [OUTER_TBL_W],
    borders: noBorders(),
    rows: [new TableRow({
      cantSplit: true,
      height: { value: 14318, rule: HeightRule.EXACT },   // 注意：本版 docx 库只有 EXACT，EXACTLY 不存在（会静默丢 hRule）
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 0, bottom: 0, left: 0, right: 0 },
        children: [spacerPara()]
      })]
    })]
  });
}

// 封底模板：像素级复原成杰在庚册中的最新精修设计（汉仪方篆 U 竖排三行 + 汉仪字酷堂会典楷书 W 册名）
function buildBackCover(head) {
  const FONT_FANGZHUAN = {
    ascii: '汉仪方篆 U',
    eastAsia: '汉仪方篆 U',
    hAnsi: '汉仪方篆 U',
    cs: '汉仪方篆 U'
  };
  const FONT_HUIDIAN = {
    ascii: '汉仪字酷堂会典楷书 W',
    eastAsia: '汉仪字酷堂会典楷书 W',
    hAnsi: '汉仪字酷堂会典楷书 W',
    cs: '汉仪字酷堂会典楷书 W'
  };

  const box = [
    // 1. 岐
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 3100, after: 360, line: 80, lineRule: 'exact' },
      children: [
        new TextRun({
          text: '岐  ',
          font: FONT_FANGZHUAN,
          size: 96,
          color: '8F2D26'
        })
      ]
    }),
    // 2. 伯
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 3100, after: 360, line: 80, lineRule: 'exact' },
      children: [
        new TextRun({
          text: '伯 ',
          font: FONT_FANGZHUAN,
          size: 96,
          color: '8F2D26'
        })
      ]
    }),
    // 3. 論
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 3100, after: 360, line: 80, lineRule: 'exact' },
      children: [
        new TextRun({
          text: ' 論',
          font: FONT_FANGZHUAN,
          size: 96,
          color: '8F2D26'
        })
      ]
    }),
    // 4. 分册名称
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 0, line: 360, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: head.bookletLabel,
          font: FONT_HUIDIAN,
          size: 44,
          color: '23201D'
        })
      ]
    })
  ];

  return new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [OUTER_TBL_W],
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      height: { value: FRAME_MIN_PT * 20, rule: HeightRule.ATLEAST },
      cantSplit: true,
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: OUTER_PAD, right: OUTER_PAD },
        children: box
      })]
    })]
  });
}

// 目录：titles = [{title, startLeafLabel}]
// 返回「外框表格数组」，每叶一块（26 行/叶，块内 52 篇）。
// 每个外框行 cantSplit 且高 600pt：当前页放不下时整块推到下一叶，
// 多块目录自然一叶一块排流，无需任何分页段。
// 乙册 101 篇 → 51 行 → 2 叶；若整块塞进单个 cantSplit 行会超过版心，
// WPS 会把超页块推走留出空白页（乙册-中「封面后两张空白页」的真正根因）。
const TOC_ROWS_PER_PAGE = 26;
function buildTocLegacy(titles) {
  const header = new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 160, line: 420, lineRule: 'atLeast' },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 } },
    children: [new TextRun({ text: '本 冊 篇 目 總 覽', font: FONT_TITLE, size: 32, bold: true, color: '1A1715', letterSpacing: 25 })]
  });
  const rows = [];
  for (let i = 0; i < titles.length; i += 2) {
    const mk = (idx, a) => a ? [new Paragraph({
      spacing: { before: 30, after: 30, line: 300, lineRule: 'atLeast' },
      children: [
        new TextRun({ text: idx + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
        new TextRun({ text: '《' + a.title + '》', font: FONT_BODY, size: 20, bold: true, color: COLOR_INK }),
        new TextRun({ text: ' · 第' + a.startLeafLabel + '葉', font: FONT_TOC_LEAF, size: 14, color: COLOR_MUTED })
      ]
    })] : [];
    rows.push(new TableRow({
      // 固定行高让目录表在纵向铺满内框，不再由文字自然收缩。
      height: { value: 425, rule: HeightRule.EXACT },
      cantSplit: true,
      children: [
        new TableCell({ width: { size: 4460, type: WidthType.DXA }, margins: { top: 14, bottom: 14, left: 40, right: 40 }, children: mk(i + 1, titles[i]) }),
        new TableCell({ width: { size: 4460, type: WidthType.DXA }, margins: { top: 14, bottom: 14, left: 40, right: 40 }, children: mk(i + 2, titles[i + 1]) })
      ]
    }));
  }
  const frames = [];
  for (let i = 0; i < rows.length; i += TOC_ROWS_PER_PAGE) {
    const chunk = rows.slice(i, i + TOC_ROWS_PER_PAGE);
    const box = [];
    if (i === 0) box.push(header);
    // 目录内表格必须显式 fixed + columnWidths；否则 WPS 会按文字宽度收缩，
    // 截图中就会出现表格只占外框左半边的现象。
    box.push(new Table({
      width: { size: INNER_TBL_W, type: WidthType.DXA },
      layout: TableLayoutType.FIXED,
      columnWidths: [4460, 4460],
      borders: noBorders(),
      rows: chunk
    }));
    frames.push(new Table({
      width: { size: OUTER_TBL_W, type: WidthType.DXA },
      layout: TableLayoutType.FIXED,
      columnWidths: [OUTER_TBL_W],
      borders: {
        top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
        bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
        left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
        right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
        insideHorizontal: B, insideVertical: B
      },
      rows: [new TableRow({
        height: { value: FRAME_MIN_PT * 20, rule: HeightRule.ATLEAST },
        cantSplit: true,
        children: [new TableCell({
          width: { size: OUTER_TBL_W, type: WidthType.DXA },
          margins: { top: 140, bottom: 140, left: OUTER_PAD, right: OUTER_PAD },
          children: box
        })]
      })]
    }));
  }
  return frames;
}

/* ======================= 册内单元 ======================= */
const CN_NUM = ['〇','一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十'];

function toCnNum(n) {
  const chs = ['〇','一','二','三','四','五','六','七','八','九'];
  if (n < 10) return chs[n];
  if (n < 20) return '十' + (n % 10 ? chs[n % 10] : '');
  if (n < 100) return chs[Math.floor(n / 10)] + '十' + (n % 10 ? chs[n % 10] : '');
  if (n < 1000) {
    const h = chs[Math.floor(n / 100)] + '百';
    const rem = n % 100;
    if (rem === 0) return h;
    if (rem < 10) return h + '〇' + chs[rem];
    if (rem < 20) return h + '一十' + (rem % 10 ? chs[rem % 10] : '');
    return h + chs[Math.floor(rem / 10)] + '十' + (rem % 10 ? chs[rem % 10] : '');
  }
  return String(n);
}
const frameBorders = () => ({
  top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
  bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
  left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
  right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
  insideHorizontal: B, insideVertical: B
});
const frameTable = (children) => new Table({
  width: { size: OUTER_TBL_W, type: WidthType.DXA },
  layout: TableLayoutType.FIXED,
  columnWidths: [OUTER_TBL_W],
  borders: frameBorders(),
  rows: [new TableRow({
    height: { value: FRAME_MIN_PT * 20, rule: HeightRule.ATLEAST },
    cantSplit: true,
    children: [new TableCell({
      width: { size: OUTER_TBL_W, type: WidthType.DXA },
      margins: { top: 140, bottom: 140, left: OUTER_PAD, right: OUTER_PAD },
      children
    })]
  })]
});

// 读取 units/out/{code}.json，按单元顺序重排 records；单元表缺失时整册视为一个无名单元。
function loadUnits(code, records) {
  const p = require('path').join(__dirname, 'units', 'out', code + '.json');
  if (!fs.existsSync(p)) return [{ index: 1, name: '', intro: '', arts: records.slice() }];
  const j = JSON.parse(fs.readFileSync(p, 'utf8'));
  const byOrd = new Map(records.map(r => [r.workbook_ordinal, r]));
  const used = new Set();
  const groups = j.units.map((u, i) => {
    const arts = u.ordinals.filter(o => byOrd.has(o)).map(o => { used.add(o); return byOrd.get(o); });
    return { index: i + 1, name: u.name, intro: u.intro, arts };
  });
  const rest = records.filter(r => !used.has(r.workbook_ordinal));
  if (rest.length) throw new Error(code + ' 有 ' + rest.length + ' 篇未分入单元（序号 ' + rest.slice(0, 5).map(r => r.workbook_ordinal).join(',') + '），请先更新 units/out/' + code + '.json');
  return groups.filter(g => g.arts.length);
}

// 把单元组在单元边界上切成 k 份（用于 B02 上中下），返回第 idx 份；单元序号保持全册连续。
function splitGroups(groups, k, idx) {
  const total = groups.reduce((s, g) => s + g.arts.length, 0);
  // prefix[i] = 前 i 个单元的篇数；第 c 个切点取最接近 total*c/k 的单元边界
  const prefix = [0];
  groups.forEach(g => prefix.push(prefix[prefix.length - 1] + g.arts.length));
  const bounds = [0];
  for (let c = 1; c < k; c++) {
    const target = total * c / k;
    let best = bounds[c - 1] + 1;
    for (let i = bounds[c - 1] + 1; i <= groups.length - (k - c); i++) {
      if (Math.abs(prefix[i] - target) < Math.abs(prefix[best] - target)) best = i;
    }
    bounds.push(best);
  }
  bounds.push(groups.length);
  return groups.slice(bounds[idx], bounds[idx + 1]);
}

// 单元扉叶：与正文叶同构（题眉 + 600pt 双线框，外层不可拆），占一叶。
function buildUnitPage(unit, unitCount, ctx, startOfSection) {
  const sp = (t) => t.split('').join(' ');
  const headerPara = new Paragraph({
    alignment: AlignmentType.CENTER,
    pageBreakBefore: !startOfSection,
    keepNext: true,
    spacing: { before: 0, after: 140, line: 260, lineRule: 'atLeast' },
    children: [new TextRun({ text: '岐伯論 · ' + ctx.volPrefix, font: FONT_HEADER, size: 22, color: COLOR_SEAL, letterSpacing: 20 })]
  });
  const box = [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 3000, after: 300, line: 360, lineRule: 'atLeast' },
      children: [new TextRun({ text: sp('第' + CN_NUM[unit.index] + '單元'), font: FONT_FOOTER, size: 26, color: COLOR_SEAL, letterSpacing: 20 })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 360, line: 1000, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE, space: 14 } },
      children: [new TextRun({ text: sp(unit.name), font: FONT_TITLE, size: 72, color: '1A1715', letterSpacing: 40 })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240, after: 200, line: 400, lineRule: 'atLeast' },
      children: [new TextRun({ text: unit.intro, font: FONT_Q_TEXT, size: 24, color: '453F3A' })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 0, line: 320, lineRule: 'atLeast' },
      // 汉仪永字夏蝉 95W 一律用“册”而非“冊”
      children: [new TextRun({ text: (ctx.stem + '冊 ' + ctx.bookletTrad + ' · 凡' + toCnNum(unitCount) + '單元 · 本單元收文 ' + toCnNum(unit.arts.length) + ' 篇').replace(/冊/g, '册'),
        font: FONT_NOTE_TITLE, size: 18, color: COLOR_MUTED, letterSpacing: 10 })] })
  ];
  return new Table({
    width: { size: OUTER_TBL_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    columnWidths: [OUTER_TBL_W],
    borders: noBorders(),
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: OUTER_TBL_W, type: WidthType.DXA },
        margins: { top: 0, bottom: 0, left: 0, right: 0 },
        children: [headerPara, frameTable(box)]
      })]
    })]
  });
}

// 篇目总览（单栏双行）：
//   单元行：第X單元 · 單元名（朱红）
//   篇目行：序号 《标题》 ……… 第X葉
//   问题行：【問】读者原问（截断至一行；无问题时以〔摘〕正文首句代替）
// 每行 EXACT 行高，按累计高度装箱，每叶一框。
const TOC_PAGE_BUDGET = 10900;       // 框内可用高度（twips），框净高约 11720，留余量
const TOC_HEAD_H = 900, TOC_UNIT_H = 620, TOC_ENTRY_H = 640;
const TOC_Q_MAX = 44;                // 问题行最大字宽（全角计）
function tocQuestion(a) {
  const norm = s => (s || '').replace(/\s+/g, ' ').trim();
  let q = norm(a.question), mark = '【問】';
  if (!q || q === a.title) { q = norm(a.text_preview).split(/(?<=[。！？])/)[0] || ''; mark = '〔摘〕'; }
  if (glyphLen(q) > TOC_Q_MAX) {
    let out = '', n = 0;
    for (const ch of q) { const w = glyphLen(ch); if (n + w > TOC_Q_MAX - 1) break; out += ch; n += w; }
    q = out + '……';
  }
  return { mark, q };
}
function buildToc(groups, leafLabelOf) {
  const header = new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 160, line: 420, lineRule: 'atLeast' },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 } },
    children: [new TextRun({ text: '本 冊 篇 目 總 覽', font: FONT_TITLE, size: 32, color: '1A1715', letterSpacing: 25 })]
  });
  const RIGHT_TAB = INNER_TBL_W - 120;
  const cell = (children, h) => new TableRow({
    height: { value: h, rule: HeightRule.EXACT }, cantSplit: true,
    children: [new TableCell({ width: { size: INNER_TBL_W, type: WidthType.DXA }, margins: { top: 0, bottom: 0, left: 40, right: 40 }, children })]
  });
  const items = [];   // { row, h }
  let seq = 0;
  for (const g of groups) {
    if (g.name) items.push({ h: TOC_UNIT_H, row: cell([new Paragraph({
      spacing: { before: 200, after: 40, line: 300, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'D8D4C8', space: 2 } },
      children: [
        new TextRun({ text: '第' + toCnNum(g.index) + '單元 · ', font: FONT_FOOTER, size: 20, color: COLOR_SEAL }),
        new TextRun({ text: g.name.split('').join(' '), font: FONT_TITLE, size: 24, color: COLOR_SEAL, letterSpacing: 10 }),
        new TextRun({ text: '　' + toCnNum(g.arts.length) + '篇', font: FONT_TOC_LEAF, size: 15, color: COLOR_MUTED })
      ] })], TOC_UNIT_H) });
    for (const a of g.arts) {
      seq++;
      const { mark, q } = tocQuestion(a);
      items.push({ h: TOC_ENTRY_H, row: cell([
        new Paragraph({
          spacing: { before: 40, after: 0, line: 300, lineRule: 'atLeast' },
          tabStops: [{ type: TabStopType.RIGHT, position: RIGHT_TAB, leader: LeaderType.MIDDLE_DOT }],
          children: [
            new TextRun({ text: seq + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
            new TextRun({ text: '《' + a.title + '》', font: FONT_BODY, size: 21, color: COLOR_INK }),
            new TextRun({ children: [new Tab()], font: FONT_TOC_LEAF, size: 15, color: COLOR_MUTED }),
            new TextRun({ text: '第' + leafLabelOf(a) + '葉', font: FONT_TOC_LEAF, size: 15, color: COLOR_MUTED })
          ]
        }),
        new Paragraph({
          spacing: { before: 0, after: 0, line: 240, lineRule: 'atLeast' },
          indent: { left: 420 },
          children: [
            new TextRun({ text: mark, font: FONT_Q_MARK, size: 15, color: 'A8796F' }),
            new TextRun({ text: q, font: FONT_Q_TEXT, size: 17, color: '6B645B' })
          ]
        })
      ], TOC_ENTRY_H) });
    }
  }
  // 装箱：首叶扣除抬头；单元行不得落在叶末（孤行），否则推到下一叶
  const pages = [];
  let cur = [], used = TOC_HEAD_H;
  items.forEach((it, i) => {
    const needNext = it.h === TOC_UNIT_H && items[i + 1] ? items[i + 1].h : 0;
    if (cur.length && used + it.h + needNext > TOC_PAGE_BUDGET) { pages.push(cur); cur = []; used = 0; }
    cur.push(it.row); used += it.h;
  });
  if (cur.length) pages.push(cur);
  return pages.map((rows, i) => frameTable([
    ...(i === 0 ? [header] : []),
    new Table({ width: { size: INNER_TBL_W, type: WidthType.DXA }, layout: TableLayoutType.FIXED, columnWidths: [INNER_TBL_W], borders: noBorders(), rows })
  ]));
}

module.exports = {
  FONTS: { FONT_HEADER, FONT_TITLE, FONT_Q_MARK, FONT_Q_TEXT, FONT_BODY, FONT_NOTE_TITLE, FONT_FOOTER, FONT_PAGE_NUM: FONT_BODY, FONT_SYSTEM, FONT_TOC_LEAF },
  COLORS: { COLOR_INK, COLOR_SEAL, COLOR_BORDER_LINE, COLOR_FOOTER, COLOR_MUTED, COLOR_PAGE_NUM: '000000' },
  METRICS: {
    MARGIN_TOP, MARGIN_BOTTOM, MARGIN_LEFT, MARGIN_RIGHT, FOOTER_DIST,
    PAGE_CONTENT_PT, BLOCK_BUDGET, HEADER_PT, TITLE_PT, WS_MARGIN, OUTER_MARGIN, COLOPHON_PT,
    RAIL_HEAD, RAIL_LINE, FILLER_HEAD, FILLER_LINE, FRAME_MIN_PT, FRAME_INNER_PT
  },
  paraPt, questionPt, bodyBudget, railTarget, glyphLen, toChineseDate,
  MARKER_QIBO, LABEL_NARRATIVE,
  paginateByHeight, buildArticlePage, buildCover, buildBackCover, buildToc, buildTocLegacy,
  loadUnits, splitGroups, buildUnitPage,
  buildBlankPage, spacerPara, TOC_ROWS_PER_PAGE,
  breakPara: () => new Paragraph({
    pageBreakBefore: true, spacing: { before: 0, after: 0, line: 240, lineRule: 'atLeast' }, children: []
  })
};
