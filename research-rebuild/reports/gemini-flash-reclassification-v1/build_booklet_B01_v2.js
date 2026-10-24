// 岐伯論 · 卷一 · 甲冊（B01）── 版式修正版 v2
//
// 相对 build_booklet_B01_strict.js 的修正：
//   1) 分页不再按「每页 360/480 字」的硬编码字符预算，改为按真实版面高度（twips）装箱
//      —— 原预算仅为实际容量 4 成左右，导致每叶只填一半、一本小册被撑到 243 叶。
//   2) 古籍外框行高设为 atLeast 满页高度 —— 原外框高度由内容撑开，内容少时框塌成一条短框，
//      看起来像「空白叶」。
//   3) 右侧「随文批校」虚线栏按整叶高度铺满 —— 每叶版心完整、批注栏贯穿全叶。
//   4) 篇末叶若剩余空间较多，自动补「案語札記」虚线区填满版心，不留大片空白。
//   5) 行距一律改为「固定值(exact)」，使分页模型与 WPS 实际渲染完全一致（可确定性分页）。
//   6) 分页符改用 pageBreakBefore 挂在天头段上，不再推入独立空段落 —— 杜绝空段落自成一叶。
//   7) 篇内末叶过短时自动均衡重排，避免「只剩两三行」的残叶。

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, ImageRun, Footer, PageNumber, HeightRule
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const OUT_DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/';
const QR_DIR = path.join(OUT_DIR, 'qr_cache_b01');
const MERGED_CORPUS = path.join(OUT_DIR, 'all-articles-merged-v3.jsonl');
const CATALOG_PATH = path.join(OUT_DIR, 'workbook-40b-all-catalog.jsonl');

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

/* =======================================================================
 *  版面度量模型（单位 twips = 1/20 pt）
 *  A4 纵向：11906 × 16838；页边距 上1020 右1020 下1134 左1587
 *  全篇行距统一设为「固定值」，模型与渲染一一对应 → 分页可确定
 * ======================================================================= */
const PAGE_W = 11906, PAGE_H = 16838;
const MT = 1020, MB = 1134, ML = 1587, MR = 1020;
const CONTENT_H = PAGE_H - MT - MB;                  // 14684 版心高

const HEAD_LINE = 320, HEAD_AFTER = 140;             // 天头题眉（11pt）
const HEAD_BLOCK = HEAD_LINE + HEAD_AFTER;           // 460
const FRAME_PAD = 280;                               // 古籍外框单元格上下留白（140×2）
const FRAME_AVAIL = CONTENT_H - HEAD_BLOCK - FRAME_PAD;   // 13944 框内最大可用高

const WS_GAP = 100;                                  // 正文/批校表单元格上下留白
const LAYOUT_SAFETY = 250;                           // 版面安全余量
const ROW_TOTAL_BUDGET = FRAME_AVAIL - WS_GAP - LAYOUT_SAFETY;   // 13594 一叶可装内容总预算

const BODY_LINE = 340, PARA_BEFORE = 50, PARA_AFTER = 120;
const PARA_GAP = PARA_BEFORE + PARA_AFTER;           // 170
const TITLE_LINE = 700, TITLE_BLOCK = TITLE_LINE + 60 + 160;     // 920 框内大标题
const Q_LINE = 460, Q_BLOCK_BASE = Q_LINE + 30 + 160;            // 650（单行）
const COLOPHON_LINE = 300, COLOPHON_BLOCK = COLOPHON_LINE * 2 + 30 + 150;  // 780 落款栏
const RAIL_HEAD = 30 + 120 + 200;                    // 366 批校栏题头
const RAIL_LINE = 320 + 240;                         // 560 批校虚线行
const FILLER_HEAD = 160 + 100 + 220;                 // 480 案語札記题头
const FILLER_LINE = 320 + 240;                       // 560 札记虚线行

const LEFT_CELL_W = 6850, LEFT_PAD_R = 200, FIRST_INDENT = 460;
const TEXT_W = LEFT_CELL_W - LEFT_PAD_R;             // 6650 正文可用宽
const TW_PER_PT = 20;
const CW = 11.5 * TW_PER_PT;                         // 230 正文全角字宽
const FIRST_LINE_CH = Math.floor((TEXT_W - FIRST_INDENT) / CW);  // 26
const CONT_LINE_CH  = Math.floor(TEXT_W / CW);                   // 28
const Q_PREFIX_W = 2 * 280 + 190;                    // 【問】(14pt 两字) + 间隔
const Q_CH_W = 12 * TW_PER_PT;                       // 240 问题字宽

const FRAME_MIN_HEIGHT = FRAME_AVAIL - 14;           // 13930 版框恒定满叶

// 全角计 1、半角计 0.5
function glyphLen(s) {
  let n = 0;
  for (const ch of s) {
    n += /[\u1100-\u11FF\u2E80-\u9FFF\uA960-\uA97F\uAC00-\uD7FF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFF60\uFFE0-\uFFE6]/.test(ch) ? 1 : 0.5;
  }
  return n;
}

// 段落实体：indent 表示是否首行缩进两字（跨叶续段不缩进）
function linesOf(L, indented) {
  const first = indented ? FIRST_LINE_CH : CONT_LINE_CH;
  return 1 + Math.max(0, Math.ceil((L - first) / CONT_LINE_CH));
}
function itemCost(it) {
  return linesOf(glyphLen(it.text), it.indent) * BODY_LINE + it.before + it.after;
}
function mkItem(text) {
  return { text, indent: true, before: PARA_BEFORE, after: PARA_AFTER };
}
function paraCost(p) {
  return itemCost(mkItem(p));
}

function questionCost(q) {
  if (!q) return 0;
  const L = glyphLen(q);
  const cpl1 = Math.floor((TEXT_W - Q_PREFIX_W) / Q_CH_W);
  const cplN = Math.floor(TEXT_W / Q_CH_W);
  const lines = L <= cpl1 ? 1 : 1 + Math.ceil((L - cpl1) / cplN);
  return lines * Q_LINE + 30 + 160;
}

// 超长段落按标点自然断开（保证单段绝不超出一叶预算）
function splitLongParagraph(p, maxChars = 240) {
  if (glyphLen(p) <= maxChars) return [p];
  const sentences = p.split(/(?<=[。！？；：])/g);
  const chunks = [];
  let curr = '';
  for (const sentence of sentences) {
    if (!sentence) continue;
    if (glyphLen(sentence) > maxChars) {
      if (curr) { chunks.push(curr); curr = ''; }
      for (let i = 0; i < sentence.length; i += maxChars) chunks.push(sentence.slice(i, i + maxChars));
    } else if (glyphLen(curr + sentence) > maxChars && curr) {
      chunks.push(curr);
      curr = sentence;
    } else {
      curr += sentence;
    }
  }
  if (curr) chunks.push(curr);
  return chunks;
}

// 在句子边界处把一段切成「本叶剩余空间刚好装得下」的头 + 尾巴
const MIN_SPLIT_HEAD = 12;   // 头段至少几个字，否则不值得拆
const MIN_SPLIT_TAIL = 3;    // 尾段至少几个字
function splitAtGlyph(str, maxGlyphs) {
  let cut = 0, acc = 0;
  const sentEnds = [], anyEnds = [];
  for (let i = 0; i < str.length; i++) {
    const g = glyphLen(str[i]);
    if (acc + g > maxGlyphs) break;
    acc += g; cut = i + 1;
    if (/[。！？；]/.test(str[i])) sentEnds.push(cut);
    else if (/[，、：]/.test(str[i])) anyEnds.push(cut);
  }
  if (cut <= 0 || cut >= str.length) return null;
  const pick = (arr) => { const ok = arr.filter(b => b >= cut * 0.55); return ok.length ? ok[ok.length - 1] : 0; };
  let at = pick(sentEnds) || pick(anyEnds) || cut;
  if (at <= 0 || at >= str.length) return null;
  return [str.slice(0, at), str.slice(at)];
}

/* =======================================================================
 *  按高度装箱的分页器
 * ======================================================================= */
function paginateArticleByHeight(rawParas, qText) {
  const items = [];
  for (const p of rawParas) for (const seg of splitLongParagraph(p, 240)) items.push(mkItem(seg));

  const qCost = questionCost(qText);
  // 第 idx 叶「正文 + 批校栏」这一行的高度额度
  const rowCap = (idx) => ROW_TOTAL_BUDGET - (idx === 0 ? TITLE_BLOCK + qCost : 0);

  const pages = [];
  let cur = [], cost = 0;

  for (const it of items) {
    const c = itemCost(it);
    const cap = rowCap(pages.length);
    if (cur.length && cost + c > cap) {
      // 若本叶还剩两行以上，就在句读处把这一段拆开，把本叶填满
      const space = cap - cost;
      const linesAvail = Math.floor((space - it.before) / BODY_LINE);
      const L = glyphLen(it.text);
      const maxChars = (it.indent ? FIRST_LINE_CH : CONT_LINE_CH) + Math.max(0, linesAvail - 1) * CONT_LINE_CH;
      let done = false;
      if (linesAvail >= 2 && L - maxChars >= MIN_SPLIT_TAIL) {
        const sp = splitAtGlyph(it.text, maxChars);
        if (sp && glyphLen(sp[0]) >= MIN_SPLIT_HEAD && glyphLen(sp[1]) >= MIN_SPLIT_TAIL) {
          const head = { text: sp[0], indent: it.indent, before: it.before, after: 0 };
          const tail = { text: sp[1], indent: false, before: 0, after: it.after };
          const hc = itemCost(head);
          if (cost + hc <= cap) {
            cur.push(head); cost += hc;
            pages.push({ paras: cur, cost });
            cur = [tail]; cost = itemCost(tail);
            done = true;
          }
        }
      }
      if (!done) { pages.push({ paras: cur, cost }); cur = [it]; cost = c; }
    } else {
      cur.push(it); cost += c;
    }
  }
  if (cur.length) pages.push({ paras: cur, cost });

  // 末叶必须容得下落款栏
  let guard = 0;
  while (pages.length > 1 && guard++ < 200) {
    const li = pages.length - 1, last = pages[li];
    if (last.cost + COLOPHON_BLOCK <= rowCap(li)) break;
    const moved = last.paras.pop();
    last.cost -= itemCost(moved);
    if (!last.paras.length) { last.paras.push(moved); last.cost += itemCost(moved); break; }
    pages.push({ paras: [moved], cost: itemCost(moved) });
  }

  // 末叶只剩两三行 → 从上一叶末尾匀几段过来（不越界）
  if (pages.length > 1) {
    const li = pages.length - 1, prev = pages[li - 1], last = pages[li];
    let g2 = 0;
    while (prev.paras.length > 1 && last.cost < rowCap(li) * 0.3 && g2++ < 40) {
      const moved = prev.paras.pop();
      const c = itemCost(moved);
      if (last.cost + c > rowCap(li) - COLOPHON_BLOCK) { prev.paras.push(moved); break; }
      prev.cost -= c;
      last.paras.unshift(moved);
      last.cost += c;
    }
  }
  return pages;
}

function railLines(rowBudget) {
  return Math.max(6, Math.min(26, Math.floor((rowBudget - RAIL_HEAD) / RAIL_LINE)));
}

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

/* =======================================================================
 *  单叶渲染
 * ======================================================================= */
const B = { style: BorderStyle.NONE };

function noBorderTable() {
  return {
    top: B, bottom: B, left: B, right: B,
    insideHorizontal: B, insideVertical: B
  };
}

function buildArticlePage(p) {
  const {
    title, isContinuation, question, paragraphs, qrPngPath,
    showFooter, chineseDate, railCount, fillerLines
  } = p;

  const pageElements = [];

  // 天头题眉（框外居中）—— 换页符直接挂在本段，不再另推空段落
  pageElements.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    pageBreakBefore: true,
    spacing: { before: 0, after: HEAD_AFTER, line: HEAD_LINE, lineRule: 'exact' },
    children: [new TextRun({
      text: isContinuation ? '岐伯論 · ' + title + '（承前）' : '岐伯論 · ' + VOL_PREFIX_TRAD,
      font: FONT_HEADER, size: 22, color: COLOR_SEAL, letterSpacing: 20
    })]
  }));

  const innerElements = [];

  if (!isContinuation) {
    innerElements.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 60, after: 160, line: TITLE_LINE, lineRule: 'exact' },
      children: [new TextRun({
        text: title, font: FONT_TITLE, size: 44, bold: true, color: '1A1715', letterSpacing: 40
      })]
    }));
  }

  const leftCells = [];

  if (!isContinuation && question) {
    leftCells.push(new Paragraph({
      spacing: { before: 30, after: 160, line: Q_LINE, lineRule: 'exact' },
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

  for (const t of paragraphs) {
    const opts = {
      spacing: { before: t.before, after: t.after, line: BODY_LINE, lineRule: 'exact' },
      alignment: AlignmentType.BOTH,
      children: [new TextRun({ text: t.text, font: FONT_BODY, size: 23, color: COLOR_INK })]
    };
    if (t.indent) opts.indent = { firstLine: FIRST_INDENT };
    leftCells.push(new Paragraph(opts));
  }

  // 篇末叶剩余空间 → 案語札記虚线区，把版心填满
  if (fillerLines && fillerLines >= 2) {
    leftCells.push(new Paragraph({
      spacing: { before: 160, after: 100, line: 320, lineRule: 'exact' },
      border: { top: { style: BorderStyle.DASHED, size: 4, color: 'D8D4C8', space: 6 } },
      children: [new TextRun({ text: '〔 案 語 札 記 〕', font: FONT_NOTE_TITLE, size: 16, color: 'A8A297', letterSpacing: 20 })]
    }));
    for (let k = 0; k < fillerLines; k++) {
      leftCells.push(new Paragraph({
        spacing: { after: 240, line: 320, lineRule: 'exact' },
        border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
        children: [new TextRun({ text: ' ', size: 20 })]
      }));
    }
  }

  // 右侧随文批校走廊（按整叶高度铺满）
  const rightCells = [
    new Paragraph({
      spacing: { before: 30, after: 120, line: 200, lineRule: 'exact' },
      children: [new TextRun({ text: '〔 随 文 批 校 〕', font: FONT_NOTE_TITLE, size: 16, color: 'B0A99F', letterSpacing: 20 })]
    })
  ];
  for (let li = 0; li < railCount; li++) {
    rightCells.push(new Paragraph({
      spacing: { after: 240, line: 320, lineRule: 'exact' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    }));
  }

  innerElements.push(new Table({
    width: { size: 9000, type: WidthType.DXA },
    borders: noBorderTable(),
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 6850, type: WidthType.DXA },
          borders: { right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' } },
          margins: { top: 0, bottom: 100, left: 0, right: 200 },
          children: leftCells
        }),
        new TableCell({
          width: { size: 2150, type: WidthType.DXA },
          margins: { top: 0, bottom: 100, left: 200, right: 0 },
          children: rightCells
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
    innerElements.push(new Table({
      width: { size: 9000, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC' },
        bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B
      },
      rows: [new TableRow({
        children: [
          new TableCell({
            width: { size: 7600, type: WidthType.DXA },
            margins: { top: 120, bottom: 30, left: 0, right: 100 },
            children: [
              new Paragraph({
                alignment: AlignmentType.LEFT,
                spacing: { before: 0, after: 30, line: COLOPHON_LINE, lineRule: 'exact' },
                children: [new TextRun({
                  text: '〔 專 題 〕 ' + VOL_FULL_TRAD + ' · ' + BOOKLET_STEM + '冊 ' + BOOKLET_TRAD,
                  font: FONT_FOOTER, size: 20, color: COLOR_FOOTER
                })]
              }),
              new Paragraph({
                alignment: AlignmentType.LEFT,
                spacing: { before: 0, after: 0, line: COLOPHON_LINE, lineRule: 'exact' },
                children: [new TextRun({ text: '〔 錄 於 〕 ' + chineseDate, font: FONT_FOOTER, size: 20, color: COLOR_FOOTER })]
              })
            ]
          }),
          new TableCell({
            width: { size: 1400, type: WidthType.DXA },
            margins: { top: 100, bottom: 30, left: 0, right: 0 },
            children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: qrImage ? [qrImage] : [] })]
          })
        ]
      })]
    }));
  }

  // 外层古籍边框 —— 行高 atLeast 满叶，任何一叶的版框都完整
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
      height: { value: FRAME_MIN_HEIGHT, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: 180, right: 180 },
        children: innerElements
      })]
    })]
  }));

  return pageElements;
}

/* =======================================================================
 *  册首扉页 + 总目录
 * ======================================================================= */
function buildBookletFrontMatter(articles) {
  const elements = [];

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

  elements.push(new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 16, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 16, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 12, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 12, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      height: { value: FRAME_MIN_HEIGHT, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 300, bottom: 300, left: 300, right: 300 },
        children: coverBox
      })]
    })]
  }));
  elements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

  const tocBox = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 260, line: 460, lineRule: 'exact' },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 } },
      children: [new TextRun({ text: '本 冊 篇 目 總 覽', font: FONT_TITLE, size: 32, bold: true, color: '1A1715', letterSpacing: 25 })]
    })
  ];

  const tocRows = [];
  for (let i = 0; i < articles.length; i += 2) {
    const mk = (idx, a) => a ? [new Paragraph({
      spacing: { before: 40, after: 40, line: 300, lineRule: 'exact' },
      children: [
        new TextRun({ text: idx + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
        new TextRun({ text: '《' + a.title + '》', font: FONT_BODY, size: 20, bold: true, color: COLOR_INK }),
        new TextRun({ text: ' ' + a.charCount + '字·' + a.pageSpan + '葉', font: FONT_SYSTEM, size: 14, color: COLOR_MUTED })
      ]
    })] : [];
    tocRows.push(new TableRow({
      children: [
        new TableCell({ width: { size: 4500, type: WidthType.DXA }, margins: { top: 20, bottom: 20, left: 40, right: 40 }, children: mk(i + 1, articles[i]) }),
        new TableCell({ width: { size: 4500, type: WidthType.DXA }, margins: { top: 20, bottom: 20, left: 40, right: 40 }, children: mk(i + 2, articles[i + 1]) })
      ]
    }));
  }
  tocBox.push(new Table({
    width: { size: 9000, type: WidthType.DXA },
    borders: noBorderTable(),
    rows: tocRows
  }));

  elements.push(new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: B, insideVertical: B
    },
    rows: [new TableRow({
      height: { value: FRAME_MIN_HEIGHT, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: 9355, type: WidthType.DXA },
        margins: { top: 140, bottom: 140, left: 180, right: 180 },
        children: tocBox
      })]
    })]
  }));

  return elements;
}

/* =======================================================================
 *  编译
 * ======================================================================= */
const b01Catalog = [];
for (const l of fs.readFileSync(CATALOG_PATH, 'utf-8').split(String.fromCharCode(10))) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  if (d.booklet_code === 'B01') b01Catalog.push(d);
}
console.log('B01 篇目数: ' + b01Catalog.length);

const corpusMap = {};
for (const l of fs.readFileSync(MERGED_CORPUS, 'utf-8').split(String.fromCharCode(10))) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  corpusMap[d.id] = d;
}

const b01FullArticles = b01Catalog.map(catEntry => {
  const corpusEntry = corpusMap[catEntry.original_id] || {};
  return { ...catEntry, text: corpusEntry.text || '', url: corpusEntry.url || '', charCount: (corpusEntry.text || '').length };
});

const plans = [];
b01FullArticles.forEach(art => {
  const rawParas = (art.text || '').trim().split(String.fromCharCode(10)).map(s => s.trim()).filter(Boolean);
  const pages = paginateArticleByHeight(rawParas, art.question);
  art.pageSpan = pages.length;
  plans.push({ art, pages });
});

// ── 分页体检 ──
let total = 0, sumFill = 0, fillN = 0, over = 0, lowFill = 0, bodyChars = 0;
const report = [];
for (const { art, pages } of plans) {
  total += pages.length;
  pages.forEach((pg, i) => {
    const isFirst = i === 0, isLast = i === pages.length - 1;
    let cap = ROW_TOTAL_BUDGET - (isFirst ? TITLE_BLOCK + questionCost(art.question) : 0);
    if (isLast) cap -= COLOPHON_BLOCK;
    const fill = pg.cost / cap;
    sumFill += fill; fillN++;
    if (pg.cost > cap) over++;
    if (fill < 0.6) lowFill++;
    bodyChars += pg.paras.map(x => x.text).join("").length;
    report.push({
      篇: art.title, 叶序号: i + 1, 本叶段数: pg.paras.length,
      本叶字数: pg.paras.map(x => x.text).join("").length, 版面占用: Math.round(pg.cost),
      可用额度: Math.round(cap), 填充率: +(fill).toFixed(3)
    });
  });
}
console.log('正文叶数: ' + total + '（原版 243 叶，减少 ' + (100 - total / 243 * 100).toFixed(0) + '%）');
console.log('平均填充率: ' + (sumFill / fillN * 100).toFixed(1) + '%   超出额度: ' + over + '   填充<60%: ' + lowFill);
console.log('正文总字数: ' + bodyChars + '   平均每叶: ' + Math.round(bodyChars / total) + ' 字（原版 ' + Math.round(bodyChars / 243) + ' 字）');

// ── 生成 ──
const docElements = [...buildBookletFrontMatter(b01FullArticles)];
const planDump = [];

for (const { art, pages } of plans) {
  const chineseDate = toChineseDate(art.published_at);
  const qrPngPath = path.join(QR_DIR, 'qr_' + art.workbook_ordinal + '.png');

  pages.forEach((pg, i) => {
    const isFirst = i === 0, isLast = i === pages.length - 1;
    let rowBudget = ROW_TOTAL_BUDGET - (isFirst ? TITLE_BLOCK + questionCost(art.question) : 0);
    if (isLast) rowBudget -= COLOPHON_BLOCK;

    let fillerLines = 0;
    if (isLast) {
      const leftover = rowBudget - pg.cost;
      fillerLines = Math.floor((leftover - FILLER_HEAD + 120) / FILLER_LINE);
      if (fillerLines < 2) fillerLines = 0;
      if (fillerLines > 16) fillerLines = 16;
    }

    const railCount = railLines(rowBudget);
    planDump.push({
      篇: art.title, 叶: i + 1, 篇内叶数: pages.length,
      首页: isFirst, 末页: isLast, 问: isFirst ? (art.question || '') : '',
      正文: pg.paras.map(x => ({ t: x.text, i: x.indent ? 1 : 0 })),
      批校行数: railCount, 札记行数: fillerLines,
      占用: Math.round(pg.cost), 额度: Math.round(rowBudget), 日期: chineseDate
    });

    docElements.push(...buildArticlePage({
      title: art.title,
      isContinuation: !isFirst,
      question: isFirst ? art.question : null,
      paragraphs: pg.paras,
      qrPngPath,
      showFooter: isLast,
      chineseDate,
      railCount,
      fillerLines
    }));
  });
}

const doc = new Document({
  styles: { default: { document: { run: { font: FONT_BODY, size: 23, color: COLOR_INK } } } },
  sections: [{
    properties: {
      page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MT, right: MR, bottom: MB, left: ML } }
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [
            new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
            new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
          ]
        })]
      }),
      even: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.LEFT,
          children: [
            new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
            new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
          ]
        })]
      })
    },
    children: docElements
  }]
});

const outDocxPath = path.join(OUT_DIR, '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx');
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outDocxPath, buffer);
  fs.writeFileSync(path.join(OUT_DIR, '_pagination-report-B01.json'), JSON.stringify(report, null, 1));
  fs.writeFileSync(path.join(OUT_DIR, '_pagination-plan-B01.json'), JSON.stringify({
    metrics: {
      ROW_TOTAL_BUDGET, FRAME_MIN_HEIGHT, FRAME_AVAIL, HEAD_BLOCK, WS_GAP,
      BODY_LINE, PARA_GAP, TITLE_BLOCK, COLOPHON_BLOCK, RAIL_HEAD, RAIL_LINE,
      FIRST_LINE_CH, CONT_LINE_CH, TEXT_W
    },
    articles: b01FullArticles.map(a => ({ title: a.title, ord: a.workbook_ordinal, chars: a.charCount, 叶数: a.pageSpan })),
    叶: planDump
  }));
  console.log('已生成: ' + outDocxPath + '（' + (buffer.length / 1024).toFixed(1) + ' KB，正文 ' + total + ' 叶 + 扉页/目录 2 叶 = ' + (total + 2) + ' 叶）');
}).catch(err => {
  console.error('生成失败:', err);
  process.exit(1);
});
