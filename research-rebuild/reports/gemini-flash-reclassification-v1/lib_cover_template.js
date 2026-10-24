// 岐伯論 · 封面模板生成器（像素级复原成杰原版）
// ---------------------------------------------------------------------------
// 严格按照乙册-中用户在 WPS 中实际排版的 cover_table.xml 原版参数构建：
//  段落 1: 岐  伯  論 (王羲之行书, 220, 8F2D26, before=1500, after=260)
//  段落 2: 【 卷  一 】 (汉仪松竹梅 U, 36, 5C544D, before=0, after=520)
//  段落 3: 卷主题 (方正爨宝子碑楷书, 72, 5C544D, before=0, after=520)
//  段落 4: 分册名与主题 (汉仪字酷堂会典楷书 W, 加粗, 56, 1A1715, 下带双墨线下划线, after=260)
//  段落 5: 全冊通收XX篇 · 研讀批校工作本 (方正礼器碑隶书, 22, 8C857B, before=340, after=1500)
//  段落 6: 落款印章图片 (三季蟲輯印, 48.3pt x 48.3pt, before=340, after=1500)
// ---------------------------------------------------------------------------

const fs = require('fs');
const {
  Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const COLOR_BORDER = '7A7368';
const SEAL_IMG_PATH = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/cover-seal.png';

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

/**
 * 构建封面表格
 * @param {string} volumeNum - 卷号，如 "【 卷  一 】"
 * @param {string} volumeTheme - 卷主题，如 "本根敦伦"
 * @param {string} bookletFullTitle - 分册全称，如 "乙中冊 · 學業功課與學校日常·中"
 * @param {number} articleCount - 篇数
 * @returns {Table} docx Table 对象
 */
function buildCoverTemplate(volumeNum, volumeTheme, bookletFullTitle, articleCount) {
  const sealImg = fs.readFileSync(SEAL_IMG_PATH);
  const countCn = toCnNum(articleCount);
  
  return new Table({
    width: { size: 9280, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER },
      insideHorizontal: { style: BorderStyle.NONE, size: 0 },
      insideVertical: { style: BorderStyle.NONE, size: 0 }
    },
    rows: [
      new TableRow({
        height: { value: 14318, rule: HeightRule.EXACT },
        cantSplit: true,
        children: [
          new TableCell({
            width: { size: 9280, type: WidthType.DXA },
            margins: { top: 200, left: 180, bottom: 200, right: 180 },
            verticalAlign: VerticalAlign.CENTER,
            children: [
              // 段落 1: 大标题 岐  伯  論
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 1500, after: 260, line: 480, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '岐  伯  論',
                    font: {
                      ascii: '方正王羲之行书 简繁',
                      eastAsia: '方正王羲之行书 简繁',
                      hAnsi: '方正王羲之行书 简繁',
                      cs: '方正王羲之行书 简繁'
                    },
                    color: '8F2D26',
                    size: 220
                  })
                ]
              }),
              
              // 段落 2: 卷号 【 卷  一 】
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 520, line: 360, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: volumeNum,
                    font: {
                      ascii: '汉仪松竹梅 U',
                      eastAsia: '汉仪松竹梅 U',
                      hAnsi: '汉仪松竹梅 U',
                      cs: '汉仪松竹梅 U'
                    },
                    color: '5C544D',
                    size: 36
                  })
                ]
              }),
              
              // 段落 3: 卷主题
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 520, line: 360, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: volumeTheme,
                    font: {
                      ascii: '方正爨宝子碑楷书 简繁',
                      eastAsia: '方正爨宝子碑楷书 简繁',
                      hAnsi: '方正爨宝子碑楷书 简繁',
                      cs: '方正爨宝子碑楷书 简繁'
                    },
                    color: '5C544D',
                    size: 72
                  })
                ]
              }),
              
              // 段落 4: 分册名与主题（下带双墨线下划线）
              new Paragraph({
                alignment: AlignmentType.CENTER,
                border: {
                  bottom: { style: BorderStyle.DOUBLE, size: 12, space: 12, color: COLOR_BORDER }
                },
                spacing: { before: 0, after: 260, line: 700, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: bookletFullTitle,
                    bold: true,
                    font: {
                      ascii: '汉仪字酷堂会典楷书 W',
                      eastAsia: '汉仪字酷堂会典楷书 W',
                      hAnsi: '汉仪字酷堂会典楷书 W',
                      cs: '汉仪字酷堂会典楷书 W'
                    },
                    color: '1A1715',
                    size: 56
                  })
                ]
              }),
              
              // 段落 5: 篇数说明
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 340, after: 1500, line: 340, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: `全冊通收${countCn}篇 · 研讀批校工作本`,
                    font: {
                      ascii: '方正礼器碑隶书 简繁',
                      eastAsia: '方正礼器碑隶书 简繁',
                      hAnsi: '方正礼器碑隶书 简繁',
                      cs: '方正礼器碑隶书 简繁'
                    },
                    color: '8C857B',
                    size: 22
                  })
                ]
              }),
              
              // 段落 6: 底部落款印章（三季蟲輯）
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 340, after: 1500, line: 340, lineRule: 'atLeast' },
                children: [
                  new ImageRun({
                    data: sealImg,
                    transformation: { width: 48.3, height: 48.3 }
                  })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}

module.exports = { buildCoverTemplate };
