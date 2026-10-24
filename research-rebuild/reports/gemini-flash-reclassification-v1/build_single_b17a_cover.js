#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BASE = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1');
const SEAL_IMG_PATH = path.join(BASE, 'cover-seal.png');
const sealImgBuffer = fs.readFileSync(SEAL_IMG_PATH);

const FONTS = {
  TITLE_COVER: '方正王羲之行书 简繁',
  SPINE_VOL: '汉仪松竹梅 U',
  BODY_KAITI: '汉仪字酷堂会典楷书 W',
  SUB_LIQI: '方正礼器碑隶书 简繁',
  BACK_TITLE: '方正孫過庭草書 繁U',
  BACK_SUB: '汉仪松竹梅 U',
  BACK_COLOPHON: '汉仪永字夏蝉 95W'
};

const COLORS = {
  TITLE_RED: '8F2D26',
  VOL_BROWN: '5C544D',
  TEXT_DARK: '1A1715',
  MUTED_GRAY: '8C857B',
  BORDER_LINE: '7A7368'
};

function buildVerticalTextParas(text, fontName, fontSizeHalfPt, colorHex, opts = {}) {
  return Array.from(text).map(ch => new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0, line: opts.line || 220, lineRule: 'exact' },
    children: [
      new TextRun({
        text: ch,
        font: { ascii: fontName, eastAsia: fontName, hAnsi: fontName, cs: fontName },
        size: fontSizeHalfPt,
        color: colorHex,
        ...(opts.bold ? { bold: true } : {})
      })
    ]
  }));
}

function buildSpineCell(spineWidthDxa, spineWidthMm, meta) {
  const cellChildren = [
    new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }),
    ...buildVerticalTextParas('岐伯論', FONTS.TITLE_COVER, 28, COLORS.TITLE_RED, { line: 280 }),
    new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }),
    ...buildVerticalTextParas(meta.volPrefix, FONTS.SPINE_VOL, 18, COLORS.VOL_BROWN, { line: 220 }),
    new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }),
    ...buildVerticalTextParas(meta.stemTitle, FONTS.BODY_KAITI, 18, COLORS.TEXT_DARK, { bold: true, line: 220 }),
    new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }),
    ...buildVerticalTextParas(meta.themeName, FONTS.BODY_KAITI, 16, COLORS.TEXT_DARK, { line: 200 }),
    new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 300 },
      children: [
        new ImageRun({
          data: sealImgBuffer,
          transformation: { width: 18, height: 18 }
        })
      ]
    })
  ];

  return new TableCell({
    width: { size: spineWidthDxa, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 20, right: 20 },
    borders: {
      left: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' },
      right: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' },
      top: { style: BorderStyle.NONE, size: 0 },
      bottom: { style: BorderStyle.NONE, size: 0 }
    },
    children: cellChildren
  });
}

function buildFrontCoverCell(widthDxa, meta) {
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
          new TextRun({ text: '岐  伯  論', font: { ascii: FONTS.TITLE_COVER, eastAsia: FONTS.TITLE_COVER }, color: COLORS.TITLE_RED, size: 144 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 200 },
        children: [
          new TextRun({ text: meta.volFull, font: { ascii: FONTS.SUB_LIQI, eastAsia: FONTS.SUB_LIQI }, color: COLORS.VOL_BROWN, size: 28 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 200 },
        children: [
          new TextRun({ text: meta.stemTitle + ' · ' + meta.themeName, font: { ascii: FONTS.BODY_KAITI, eastAsia: FONTS.BODY_KAITI }, color: COLORS.TEXT_DARK, size: 36, bold: true })
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

function buildBackCoverCell(widthDxa) {
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
          new TextRun({ text: '岐 伯 論 ', font: { ascii: FONTS.BACK_TITLE, eastAsia: FONTS.BACK_TITLE }, color: COLORS.VOL_BROWN, size: 60 }),
          new TextRun({ text: '·', font: { ascii: FONTS.BACK_TITLE, eastAsia: FONTS.BACK_TITLE }, color: COLORS.TITLE_RED, size: 60, bold: true }),
          new TextRun({ text: ' 典 藏 手 卷 本', font: { ascii: FONTS.BACK_TITLE, eastAsia: FONTS.BACK_TITLE }, color: COLORS.VOL_BROWN, size: 60 })
        ]
      }),
      new Paragraph({ spacing: { before: 100, after: 100 }, children: [] }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 200 },
        children: [
          new TextRun({ text: '全 五 十 五 冊 · 通 收 四 千 三 百 九 十 一 篇', font: { ascii: FONTS.BACK_SUB, eastAsia: FONTS.BACK_SUB }, color: COLORS.MUTED_GRAY, size: 20 })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 1800, after: 200 },
        children: [
          new TextRun({ text: '三 季 蟲 輯 印 · 歲 次 丙 午 刊', font: { ascii: FONTS.BACK_COLOPHON, eastAsia: FONTS.BACK_COLOPHON }, color: COLORS.MUTED_GRAY, size: 21 })
        ]
      })
    ]
  });
}

async function main() {
  const meta = {
    fullDesc: '卷四·甲册·上·情志平復與容貌自和',
    volPrefix: '卷四',
    volFull: '【 卷  四 】 存神調息',
    stemTitle: '甲冊·上',
    themeName: '情志平復與容貌自和',
    spine_mm: 12.8
  };

  const spineDxa = Math.round(meta.spine_mm * 56.7);
  const coverWidthDxa = 8000;
  const totalTableWidth = coverWidthDxa * 2 + spineDxa;

  const doc = new Document({
    sections: [{
      properties: {
        page: {
          size: { width: 18000, height: 12500 },
          margin: { top: 600, bottom: 600, left: 600, right: 600 }
        }
      },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 200 },
          children: [
            new TextRun({ 
              text: `【外包封展开图】${meta.fullDesc}（脊宽: ${meta.spine_mm} mm · 70g纯质纸施工基准）`, 
              font: { ascii: '宋体', eastAsia: '宋体' }, 
              size: 20, 
              color: '666666' 
            })
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
                buildBackCoverCell(coverWidthDxa),
                buildSpineCell(spineDxa, meta.spine_mm, meta),
                buildFrontCoverCell(coverWidthDxa, meta)
              ]
            })
          ]
        })
      ]
    }]
  });

  const outPath = '/storage/Users/currentUser/Documents/岐伯论/试打样交付包_卷四甲册上/02_外包封展开图_岐伯论·卷四·甲册上·情志平復與容貌自和.docx';
  fs.writeFileSync(outPath, await Packer.toBuffer(doc));
  console.log('Saved B17A cover spread to:', outPath);
}

main().catch(e => { console.error(e); process.exit(1); });
