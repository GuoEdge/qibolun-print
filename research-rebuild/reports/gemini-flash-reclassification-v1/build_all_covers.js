#!/usr/bin/env node
/**
 * 岐伯论 · 全量 55 册外包封展开图（Cover Spread）生成流水线
 * 严格应用成杰在 Demo 中的微调规制：
 * 1. 书脊：
 *    - 主书名：方正王羲之行书 简繁（暗红 8F2D26，大字竖排）
 *    - 卷次：汉仪松竹梅 U（深灰棕 5C544D，小一号竖排；超薄册开启 bold 提亮）
 *    - 天干：汉仪字酷堂会典楷书 W（加粗，黑 1A1715）
 *    - 分册副题全称：汉仪字酷堂会典楷书 W（黑 1A1715，紧凑直排）
 *    - 底部：缩微版朱红小印章（cover-seal.png）
 * 2. 封一（前盖）：
 *    - 主书名：方正王羲之行书 简繁（大字 144 / 72pt，暗红 8F2D26）
 *    - 卷次卷名：方正礼器碑隶书 简繁（字号 28 / 14pt，深灰棕 5C544D）
 *    - 分册全称：汉仪字酷堂会典楷书 W（字号 36 / 18pt，黑 1A1715）
 *    - 底部：三季蟲印章图（42pt）
 * 3. 封四（后底盖）：
 *    - 大题：方正孫過庭草書 繁U（字号 60 / 30pt），间隔号 · 设为暗红 8F2D26 朱点点睛
 *    - 题记：全 五 十 五 冊 · 通 收 四 千 三 百 七 十 六 篇（汉仪松竹梅 U，字号 20 / 10pt）
 *    - 刊记：三 季 蟲 輯 印 · 歲 次 丙 午 刊（汉仪永字夏蝉 95W，字号 21 / 10.5pt）
 */

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

// 封四总篇数：从主编目实时统计，转为逐字空格的汉字数（如「四 千 三 百 九 十 二」）
const TOTAL_ARTS = fs.readFileSync(path.join(BASE, 'workbook-40b-all-catalog.jsonl'), 'utf8').split('\n').filter(Boolean).length;
const TOTAL_ARTS_CN = (n => {
  const d = '零一二三四五六七八九', u = ['千', '百', '十', ''];
  const s = String(n).padStart(4, '0');
  let out = '', zero = false;
  for (let i = 0; i < 4; i++) {
    const v = +s[i];
    if (v === 0) { zero = out !== ''; continue; }
    if (zero) { out += '零'; zero = false; }
    out += d[v] + u[i];
  }
  return out.split('').join(' ');
})(TOTAL_ARTS);

// 卷名映射
const VOL_NAMES = {
  V1: { num: '【 卷  一 】', full: '【 卷  一 】 本根敦倫', prefix: '卷一', dir: '卷一' },
  V2: { num: '【 卷  二 】', full: '【 卷  二 】 陰陽合離', prefix: '卷二', dir: '卷二' },
  V3: { num: '【 卷  三 】', full: '【 卷  三 】 酬酢進退', prefix: '卷三', dir: '卷三' },
  V4: { num: '【 卷  四 】', full: '【 卷  四 】 存神調息', prefix: '卷四', dir: '卷四' },
  V5: { num: '【 卷  五 】', full: '【 卷  五 】 度勢居貨', prefix: '卷五', dir: '卷五' },
  V6: { num: '【 卷  六 】', full: '【 卷  六 】 觀風察變', prefix: '卷六', dir: '卷六' },
  V7: { num: '【 卷  七 】', full: '【 卷  七 】 滌除玄覽', prefix: '卷七', dir: '卷七' },
  V8: { num: '【 卷  八 】', full: '【 卷  八 】 格物鑄器', prefix: '卷八', dir: '卷八' }
};

// 工具函数：拆单字直下竖排
function buildVerticalTextParas(text, fontName, fontSizeHalfPt, colorHex, opts = {}) {
  const chars = Array.from(text);
  return chars.map(ch => new Paragraph({
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

// 构建书脊单元格
function buildSpineCell(spineWidthDxa, spineWidthMm, meta) {
  const isThin = spineWidthMm < 6.0;
  const isMedium = spineWidthMm >= 6.0 && spineWidthMm < 11.0;
  
  const titleSize = isThin ? 20 : (isMedium ? 24 : 28);
  const subSize = isThin ? 14 : (isMedium ? 16 : 18);
  const descSize = isThin ? 12 : (isMedium ? 14 : 16);
  const sealWidthPt = isThin ? 10 : (isMedium ? 14 : 18);
  
  const cellChildren = [];

  // 顶部留白
  cellChildren.push(new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }));

  // 1. 主书名：岐 伯 論
  cellChildren.push(...buildVerticalTextParas('岐伯論', FONTS.TITLE_COVER, titleSize, COLORS.TITLE_RED, { line: isThin ? 220 : 280 }));

  // 间距
  cellChildren.push(new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }));

  // 2. 卷次：汉仪松竹梅 U (薄册加粗保证清晰度)
  cellChildren.push(...buildVerticalTextParas(meta.volPrefix, FONTS.SPINE_VOL, subSize, COLORS.VOL_BROWN, { bold: isThin, line: isThin ? 180 : 220 }));

  // 间距
  cellChildren.push(new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }));

  // 3. 天干分册：汉仪会典楷书
  cellChildren.push(...buildVerticalTextParas(meta.stemTitle, FONTS.BODY_KAITI, subSize, COLORS.TEXT_DARK, { bold: true, line: isThin ? 180 : 220 }));

  // 间距
  cellChildren.push(new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }));

  // 4. 分册全称：汉仪会典楷书
  cellChildren.push(...buildVerticalTextParas(meta.themeName, FONTS.BODY_KAITI, descSize, COLORS.TEXT_DARK, { line: isThin ? 160 : 200 }));

  // 底部弹性推挤
  cellChildren.push(new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }));

  // 5. 缩微朱红小印章
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
      left: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' },
      right: { style: BorderStyle.DASHED, size: 4, color: 'D0C9BE' },
      top: { style: BorderStyle.NONE, size: 0 },
      bottom: { style: BorderStyle.NONE, size: 0 }
    },
    children: cellChildren
  });
}

// 构建前盖（封一）
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

// 构建后盖（封四）
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
          new TextRun({ text: '全 五 十 五 冊 · 通 收 ' + TOTAL_ARTS_CN + ' 篇', font: { ascii: FONTS.BACK_SUB, eastAsia: FONTS.BACK_SUB }, color: COLORS.MUTED_GRAY, size: 20 })
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

// 构建单个分册的外包封展开 Section
function buildCoverSpreadSection(meta) {
  const spineDxa = Math.round(meta.spine_mm * 56.7);
  const coverWidthDxa = 8000;
  const totalTableWidth = coverWidthDxa * 2 + spineDxa;

  return {
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
  };
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(path.join(BASE, 'spine_manifest.json'), 'utf8'));
  console.log(`载入 55 册元数据，开始批量编译外包封展开图...`);

  // 解析每个分册的结构化信息
  const allParsed = manifest.map(item => {
    // 样例 desc: '卷四·甲册·上·情志平復與容貌自和' 或 '卷一·甲册·幼兒啟蒙與性情習慣'
    const parts = item.desc.split('·');
    const volPrefix = parts[0]; // '卷四'
    const volInfo = Object.values(VOL_NAMES).find(v => v.prefix === volPrefix) || { num: `【 ${volPrefix} 】`, full: `【 ${volPrefix} 】`, dir: volPrefix };
    
    let stemTitle = '';
    let themeName = '';
    if (parts.length === 3) {
      stemTitle = parts[1]; // '甲册'
      themeName = parts[2]; // '幼兒啟蒙與性情習慣'
    } else if (parts.length === 4) {
      stemTitle = parts[1] + '·' + parts[2]; // '甲册·上'
      themeName = parts[3]; // '情志平復與容貌自和'
    }

    return {
      ...item,
      fullDesc: item.desc,
      volPrefix: volPrefix,
      volNum: volInfo.num,
      volFull: volInfo.full,
      volDir: volInfo.dir,
      stemTitle: stemTitle,
      themeName: themeName
    };
  });

  // 1. 按卷生成 8 本各卷外包封合订文档，保存在各卷目录下
  const byVol = {};
  allParsed.forEach(m => {
    byVol[m.volDir] = byVol[m.volDir] || [];
    byVol[m.volDir].push(m);
  });

  for (const [volDir, list] of Object.entries(byVol)) {
    const doc = new Document({
      sections: list.map(buildCoverSpreadSection)
    });
    const outVolPath = path.join(ROOT, volDir, `岐伯论·${volDir}·外包封展开图全集.docx`);
    fs.writeFileSync(outVolPath, await Packer.toBuffer(doc));
    console.log(`  ✓ 生成: ${volDir} 外包封集 (${list.length} 册) -> ${path.basename(outVolPath)}`);
  }

  // 2. 生成全书 55 册完整外包封总合集 (根目录下方便印厂一次性取用)
  const fullDoc = new Document({
    sections: allParsed.map(buildCoverSpreadSection)
  });
  const fullOutPath = path.join(ROOT, `岐伯论·全五十五册·外包封展开图总汇.docx`);
  fs.writeFileSync(fullOutPath, await Packer.toBuffer(fullDoc));
  console.log(`\n🎉 全书 55 册外包封总集生成成功: ${fullOutPath} (${(fs.statSync(fullOutPath).size / 1024).toFixed(1)} KB)`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
