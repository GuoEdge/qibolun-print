// Full wrap cover: back flap + back cover + estimated 42.3 mm spine + front cover + front flap.
// A single editable DOCX page at the physical trim spread size (542.3 × 240 mm).
const fs = require('fs');
const path = require('path');
const {
  Document, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign, Header, TableLayoutType
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BG_PATH = path.join(ROOT, 'research-rebuild/assets/qibo_jacket_background.png');
const SEAL_PATH = path.join(ROOT, 'research-rebuild/assets/seal_tight.png');
const OUT_PATH = path.join(ROOT, '岐伯论选·封面书脊封底完整书封_WPS修复版.docx');
const bgImage = fs.readFileSync(BG_PATH);
const sealImage = fs.readFileSync(SEAL_PATH);

const FONT_H = '汉仪字酷堂会典楷书 W';
const FONT_C = '汉仪昌黎宋刻本原版W';
const FONT_X = '汉仪永字夏蝉 95W';
const RED = '912F27';
const INK = '201D1A';
const MUTED = '524D46';
// 70g 纯质纸旧打样约 0.095 mm/张；正文 420 叶=840 物理页。
// 仅正文估算 840/2*0.095 + 0.5 = 40.4 mm；暂计前置内容约 20 叶后取 42.3 mm。
// 精装厂需按实物纸样和最终总物理页数复核。
const SPINE_MM = 42.3;
const SPREAD_MM = 80 + 170 + SPINE_MM + 170 + 80;
const PAGE_W = Math.round(SPREAD_MM * 1440 / 25.4);
const PAGE_H = Math.round(240 * 1440 / 25.4);
const mm = v => Math.round(v * 1440 / 25.4);
const SPREAD_ROW_H = PAGE_H - mm(1);

function p(text, options = {}) {
  return new Paragraph({
    alignment: options.alignment || AlignmentType.LEFT,
    spacing: { before: 0, after: 0, line: options.line || 260, lineRule: 'atLeast' },
    indent: options.indent,
    children: [new TextRun({
      text,
      font: { ascii: options.font || FONT_C, eastAsia: options.font || FONT_C },
      size: options.size || 22,
      bold: options.bold || false,
      color: options.color || INK
    })]
  });
}

function regionCell(widthMm, children, shading = 'FFFFFF') {
  const width = mm(widthMm);
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    margins: { top: 0, bottom: 0, left: mm(3), right: mm(3) },
    shading: { fill: shading },
    verticalAlign: VerticalAlign.CENTER,
    children
  });
}

const flapLeft = [
  p('編選識', { alignment: AlignmentType.CENTER, font: FONT_H, size: 31, color: RED, line: 360 }),
  p('────────────────', { alignment: AlignmentType.CENTER, font: FONT_C, size: 12, color: 'A79B89', line: 220 }),
  p('《岐伯論》五十五冊，通收四千三百九十一篇。本選以文本精研為準繩，考其概念發軔，析其論辯骨架，辨其經世分寸，精裁一百二十篇，使讀者由篇章見全貌，由問題入義理。', { alignment: AlignmentType.BOTH, font: FONT_C, size: 19, line: 380 }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: mm(12), after: 0 }, children: [new ImageRun({ data: sealImage, transformation: { width: 32, height: 32 }, type: 'png' })] })
];

const back = [
  p('岐 伯 論 選  /  全 書 綱 領', { font: FONT_X, size: 18, color: MUTED }),
  p('八卷通覽', { font: FONT_H, size: 48, color: RED, line: 650 }),
  p('由近及遠，由下學而至上達。八卷相貫，自家庭倫常、人我進退、身心安頓與世事觀察，推至本體之思與格物之用。', { font: FONT_C, size: 22, color: INK, line: 340 }),
  p('卷一　本根敦倫　　家庭、宗族與代際契約', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷二　陰陽合離　　兩性名理與婚戀契約', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷三　酬酢進退　　人我邊界與應世防身', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷四　存神調息　　身心安頓與生命節律', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷五　度勢居貨　　職場博弈與資財籌謀', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷六　觀風察變　　時代思潮與世相反思', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷七　滌除玄覽　　本體哲學與心智模型', { font: FONT_X, size: 21, color: RED, line: 360 }),
  p('卷八　格物鑄器　　百工技藝與造物實相', { font: FONT_X, size: 21, color: RED, line: 360 })
];

const spine = [
  p('岐', { alignment: AlignmentType.CENTER, font: FONT_H, size: 30, color: 'FFFFFF', line: 480 }),
  p('伯', { alignment: AlignmentType.CENTER, font: FONT_H, size: 30, color: 'FFFFFF', line: 480 }),
  p('論', { alignment: AlignmentType.CENTER, font: FONT_H, size: 30, color: 'FFFFFF', line: 480 }),
  p('選', { alignment: AlignmentType.CENTER, font: FONT_H, size: 30, color: 'FFFFFF', line: 620 }),
  p('一百二十篇', { alignment: AlignmentType.CENTER, font: FONT_X, size: 12, color: 'FFFFFF', line: 300 }),
  p('鵬城', { alignment: AlignmentType.CENTER, font: FONT_C, size: 11, color: 'F4F0E9', line: 240 })
];

const front = [
  p('全 息 實 存 哲 學  ·  一 百 二 十 篇', { alignment: AlignmentType.CENTER, font: FONT_X, size: 20, color: MUTED, line: 340 }),
  p('', { alignment: AlignmentType.CENTER, line: 1750 }),
  p('岐伯論選', { alignment: AlignmentType.CENTER, font: FONT_H, size: 120, bold: true, color: INK, line: 1500 }),
  p('典 藏 精 編 本', { alignment: AlignmentType.CENTER, font: FONT_C, size: 32, color: RED, line: 420 }),
  p('', { alignment: AlignmentType.CENTER, line: 1500 }),
  p('立骨於濁世　求道於近思', { alignment: AlignmentType.CENTER, font: FONT_X, size: 40, color: MUTED, line: 540 }),
  p('', { alignment: AlignmentType.CENTER, line: 900 }),
  p('歲在丙午金秋　成杰囑命編纂　·　鵬城謹製', { alignment: AlignmentType.CENTER, font: FONT_C, size: 20, color: MUTED, line: 300 })
];

const flapRight = [
  p('讀法指要', { alignment: AlignmentType.CENTER, font: FONT_H, size: 31, color: RED, line: 360 }),
  p('────────────────', { alignment: AlignmentType.CENTER, font: FONT_C, size: 12, color: 'A79B89', line: 220 }),
  p('切己體察，莫作看客。順藤摸瓜，統攬脈絡。得意忘言，貴在踐履。篇目循八卷次第編排，宜先通讀全編以見其體，再就專題反覆涵泳以得其用。', { alignment: AlignmentType.BOTH, font: FONT_C, size: 19, line: 380 }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: mm(12), after: 0 }, children: [new ImageRun({ data: sealImage, transformation: { width: 32, height: 32 }, type: 'png' })] })
];

const spread = new Table({
  width: { size: PAGE_W, type: WidthType.DXA },
  columnWidths: [mm(80), mm(170), mm(SPINE_MM), mm(170), mm(80)],
  layout: TableLayoutType.FIXED,
  indent: { size: 0, type: WidthType.DXA },
  alignment: AlignmentType.LEFT,
  borders: {
    top: { style: BorderStyle.NONE, size: 0 }, bottom: { style: BorderStyle.NONE, size: 0 },
    left: { style: BorderStyle.NONE, size: 0 }, right: { style: BorderStyle.NONE, size: 0 },
    insideVertical: { style: BorderStyle.NONE, size: 0 }, insideHorizontal: { style: BorderStyle.NONE, size: 0 }
  },
  rows: [new TableRow({
    height: { value: SPREAD_ROW_H, rule: HeightRule.AT_LEAST },
    cantSplit: true,
    children: [
      regionCell(80, flapLeft),
      regionCell(170, back),
      regionCell(SPINE_MM, spine, '302D2A'),
      regionCell(170, front),
      regionCell(80, flapRight)
    ]
  })]
});

const doc = new Document({
  sections: [{
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.LEFT,
          spacing: { before: 0, after: 0, line: 1, lineRule: 'exact' },
          children: [new ImageRun({ data: bgImage, transformation: { width: PAGE_W / 20, height: PAGE_H / 20 }, type: 'png' })]
        })]
      })
    },
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H },
        margin: { top: 0, right: 0, bottom: 0, left: 0, header: 0, footer: 0 },
        pageBorders: {
          display: 'allPages',
          offsetFrom: 'page',
          zOrder: 'front',
          top: { style: BorderStyle.SINGLE, size: 4, color: 'BDB5AA', space: 0 },
          bottom: { style: BorderStyle.SINGLE, size: 4, color: 'BDB5AA', space: 0 },
          left: { style: BorderStyle.SINGLE, size: 4, color: 'BDB5AA', space: 0 },
          right: { style: BorderStyle.SINGLE, size: 4, color: 'BDB5AA', space: 0 }
        }
      }
    },
    children: [spread]
  }]
});

const Packer = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx').Packer;
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(OUT_PATH, buffer);
  console.log(`✓ 完整展开书封 DOCX 生成：${OUT_PATH} (${(buffer.length/1024).toFixed(1)} KB)`);
}).catch(err => { console.error(err); process.exitCode = 1; });
