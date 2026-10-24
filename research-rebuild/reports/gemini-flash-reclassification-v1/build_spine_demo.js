#!/usr/bin/env node
/**
 * 岐伯论 · 书脊设计与全包裹外封面 Demo 生成器
 * 严格按照成杰的定制规格：
 * 1. 题签框：干净的纯字悬浮留白（主书名：方正王羲之行书 简繁，暗红 8F2D26）
 * 2. 文字朝向：单字直下竖排
 * 3. 卷次天干：小一号字直排
 * 4. 分册副题：全称展示（典雅宋楷）
 * 5. 底端落款：缩微版朱红小印章（cover-seal.png）
 * 
 * 生成三本不同厚度的实测 Demo：
 * - 样例 1（厚本）：卷四·甲册上 (B17A, 脊宽 12.6mm, 254P)
 * - 样例 2（中本）：卷二·乙册 (B12, 脊宽 8.2mm, 162P)
 * - 样例 3（薄本）：卷一·戊册 (B05, 脊宽 3.4mm, 62P)
 */

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign, PageOrientation
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BASE = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1');
const SEAL_IMG_PATH = path.join(BASE, 'cover-seal.png');
const sealImgBuffer = fs.readFileSync(SEAL_IMG_PATH);

const FONTS = {
  TITLE: '方正王羲之行书 简繁',
  SUB: '方正爨宝子碑楷书',
  BODY: '汉仪字酷堂会典楷书 W',
  SEAL: '方正礼器碑隶书'
};

const COLORS = {
  TITLE_RED: '8F2D26',
  VOL_BROWN: '5C544D',
  TEXT_DARK: '1A1715',
  BORDER_LINE: '7A7368',
  BG_PAPER: 'FAF7F2'
};

// 工具函数：将文本拆为单字直下竖排的段落数组
function buildVerticalTextParas(text, fontName, fontSizeHalfPt, colorHex, extraSpacing = {}) {
  const chars = Array.from(text);
  return chars.map(ch => new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0, line: extraSpacing.line || 240, lineRule: 'exact' },
    children: [
      new TextRun({
        text: ch,
        font: { ascii: fontName, eastAsia: fontName, hAnsi: fontName, cs: fontName },
        size: fontSizeHalfPt,
        color: colorHex,
        bold: extraSpacing.bold || false
      })
    ]
  }));
}

// 构建书脊单元格
function buildSpineCell(spineWidthDxa, spineWidthMm, data) {
  // 根据书脊物理宽度调整字号，确保薄册不溢出
  const isThin = spineWidthMm < 6.0;
  const isMedium = spineWidthMm >= 6.0 && spineWidthMm < 11.0;
  
  const titleSize = isThin ? 20 : (isMedium ? 24 : 28); // 10pt / 12pt / 14pt
  const subSize = isThin ? 14 : (isMedium ? 16 : 18);   // 7pt / 8pt / 9pt
  const descSize = isThin ? 12 : (isMedium ? 14 : 16);  // 6pt / 7pt / 8pt
  
  const sealWidthPt = isThin ? 10 : (isMedium ? 14 : 18);

  const cellChildren = [];

  // 顶部留白
  cellChildren.push(new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }));

  // 1. 主书名：岐 伯 論（王羲之行书，纯字悬浮）
  cellChildren.push(...buildVerticalTextParas('岐伯論', FONTS.TITLE, titleSize, COLORS.TITLE_RED, { bold: true, line: isThin ? 220 : 280 }));

  // 间隔
  cellChildren.push(new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }));

  // 2. 卷次：【卷四】 或 卷四
  cellChildren.push(...buildVerticalTextParas(data.volLabel, FONTS.SUB, subSize, COLORS.VOL_BROWN, { line: isThin ? 180 : 220 }));

  // 间隔
  cellChildren.push(new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }));

  // 3. 天干分册：甲冊上 / 乙冊
  cellChildren.push(...buildVerticalTextParas(data.stemLabel, FONTS.BODY, subSize, COLORS.TEXT_DARK, { bold: true, line: isThin ? 180 : 220 }));

  // 间隔
  cellChildren.push(new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }));

  // 4. 分册全称（长副题）：情志平復與容貌自和
  cellChildren.push(...buildVerticalTextParas(data.themeFull, FONTS.BODY, descSize, COLORS.TEXT_DARK, { line: isThin ? 160 : 200 }));

  // 柔和弹性间隔推到底部
  cellChildren.push(new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }));

  // 5. 底端落款：缩微版朱红小印章
  cellChildren.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 100, after: 300 },
    children: [
      new ImageRun({
        data: sealImgBuffer,
        transformation: { width: sealWidthPt, height: sealWidthPt }
      })
    ]
  }));

  return new TableCell({
    width: { size: spineWidthDxa, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 20, right: 20 },
    borders: {
      left: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' },  // 浅色折痕压槽辅助线
      right: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' }, // 浅色折痕压槽辅助线
      top: { style: BorderStyle.NONE, size: 0 },
      bottom: { style: BorderStyle.NONE, size: 0 }
    },
    children: cellChildren
  });
}

// 构建前盖面（封一）
function buildFrontCoverCell(widthDxa, data) {
  return new TableCell({
    width: { size: widthDxa, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 300, bottom: 300, left: 300, right: 300 },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLORS.BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLORS.BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLORS.BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLORS.BORDER_LINE }
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 1000, after: 200 },
        children: [
          new TextRun({ text: '岐  伯  論', font: { ascii: FONTS.TITLE, eastAsia: FONTS.TITLE }, color: COLORS.TITLE_RED, size: 120, bold: true })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 200 },
        children: [
          new TextRun({ text: data.volFull, font: { ascii: FONTS.SUB, eastAsia: FONTS.SUB }, color: COLORS.VOL_BROWN, size: 28 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 200 },
        children: [
          new TextRun({ text: data.stemLabel + ' · ' + data.themeFull, font: { ascii: FONTS.BODY, eastAsia: FONTS.BODY }, color: COLORS.TEXT_DARK, size: 36, bold: true })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 1500, after: 200 },
        children: [
          new ImageRun({
            data: sealImgBuffer,
            transformation: { width: 42, height: 42 }
          })
        ]
      })
    ]
  });
}

// 构建后底盖面（封四）
function buildBackCoverCell(widthDxa, data) {
  return new TableCell({
    width: { size: widthDxa, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 300, bottom: 300, left: 300, right: 300 },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLORS.BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLORS.BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLORS.BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLORS.BORDER_LINE }
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 1500, after: 200 },
        children: [
          new TextRun({ text: '岐 伯 論 · 典 藏 手 卷 本', font: { ascii: FONTS.SEAL, eastAsia: FONTS.SEAL }, color: COLORS.VOL_BROWN, size: 24 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 200 },
        children: [
          new TextRun({ text: '全 五 十 五 冊 · 通 收 四 千 三 百 七 十 六 篇', font: { ascii: FONTS.SEAL, eastAsia: FONTS.SEAL }, color: '8C857B', size: 18 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 1800, after: 200 },
        children: [
          new TextRun({ text: '三 季 蟲 輯 印 · 歲 次 丙 午 刊', font: { ascii: FONTS.SEAL, eastAsia: FONTS.SEAL }, color: '8C857B', size: 18 })
        ]
      })
    ]
  });
}

// 构建一整张宽幅外包封展开图（A3横向或定制宽幅）
function createSpreadSection(data, spineWidthMm) {
  // 1mm ≈ 56.7 dxa
  const spineDxa = Math.round(spineWidthMm * 56.7);
  const coverWidthDxa = 8000; // 封一面与封四面宽度
  const totalTableWidth = coverWidthDxa * 2 + spineDxa;

  return {
    properties: {
      page: {
        size: { width: 18000, height: 12500 }, // 宽幅横版
        margin: { top: 600, bottom: 600, left: 600, right: 600 }
      }
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 200 },
        children: [
          new TextRun({ text: `【外包封展开打样】${data.title}（物理脊宽: ${spineWidthMm.toFixed(1)} mm / 70g纯质纸）`, font: { ascii: '宋体', eastAsia: '宋体' }, size: 20, color: '666666' })
        ]
      }),
      new Table({
        width: { size: totalTableWidth, type: WidthType.DXA },
        alignment: AlignmentType.CENTER,
        rows: [
          new TableRow({
            height: { value: 10500, rule: HeightRule.ATLEAST },
            cantSplit: true,
            children: [
              buildBackCoverCell(coverWidthDxa, data),
              buildSpineCell(spineDxa, spineWidthMm, data),
              buildFrontCoverCell(coverWidthDxa, data)
            ]
          })
        ]
      })
    ]
  };
}

async function main() {
  const samples = [
    {
      title: '样例 1 · 厚本手卷 (B17A)',
      volLabel: '卷四',
      volFull: '【 卷  四 】 存神調息',
      stemLabel: '甲冊·上',
      themeFull: '情志平復與容貌自和',
      spineMm: 12.6
    },
    {
      title: '样例 2 · 中本手卷 (B12)',
      volLabel: '卷二',
      volFull: '【 卷  二 】 陰陽合離',
      stemLabel: '乙冊',
      themeFull: '婚姻存續與夫妻日常',
      spineMm: 8.2
    },
    {
      title: '样例 3 · 极薄手卷 (B05)',
      volLabel: '卷一',
      volFull: '【 卷  一 】 本根敦倫',
      stemLabel: '戊冊',
      themeFull: '長輩相處與精神解綁',
      spineMm: 3.4
    }
  ];

  const doc = new Document({
    sections: samples.map(s => createSpreadSection(s, s.spineMm))
  });

  const outPath = path.join(ROOT, '岐伯论·书脊与外包封设计Demo.docx');
  fs.writeFileSync(outPath, await Packer.toBuffer(doc));
  console.log('Demo docx generated at:', outPath);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
