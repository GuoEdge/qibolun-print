// 《岐伯论选》（一百二十篇·权威精编定本）专属封面生成器
// ---------------------------------------------------------------------------
// 继承原典《现代学者批校手卷本》典雅规制：
//  段落 1: 岐  伯  論  選 (王羲之行书, 200, 8F2D26, before=1300, after=260)
//  段落 2: 【 典藏精編本 】 (汉仪松竹梅 U, 36, 5C544D, before=0, after=400)
//  段落 3: 八卷通貫 · 一百二十篇 (方正爨宝子碑楷书, 56, 5C544D, before=0, after=400)
//  段落 4: 立骨於濁世 · 求道於近思 (汉仪字酷堂会典楷书 W, 加粗, 48, 1A1715, 下带双墨线下划线, after=260)
//  段落 5: 成傑總編 · 研讀批校工作本 (方正礼器碑隶书, 22, 8C857B, before=340, after=1200)
//  段落 6: 落款印章图片 (三季蟲輯印, 48.3pt x 48.3pt)
// ---------------------------------------------------------------------------

const fs = require('fs');
const {
  Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const COLOR_BORDER = '7A7368';
const SEAL_IMG_PATH = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/cover-seal.png';

function buildWenxuanCover() {
  const sealImg = fs.readFileSync(SEAL_IMG_PATH);
  
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
              // 段落 1: 大标题 岐  伯  論  選
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 1300, after: 260, line: 480, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '岐  伯  論  選',
                    font: {
                      ascii: '方正王羲之行书 简繁',
                      eastAsia: '方正王羲之行书 简繁',
                      hAnsi: '方正王羲之行书 简繁',
                      cs: '方正王羲之行书 简繁'
                    },
                    size: 190,
                    color: '8F2D26'
                  })
                ]
              }),
              // 段落 2: 规格标签
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 360, line: 240, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '【 典  藏  精  編  本 】',
                    font: {
                      ascii: '汉仪松竹梅 U',
                      eastAsia: '汉仪松竹梅 U',
                      hAnsi: '汉仪松竹梅 U',
                      cs: '汉仪松竹梅 U'
                    },
                    size: 34,
                    color: '5C544D'
                  })
                ]
              }),
              // 段落 3: 架构说明
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 360, line: 360, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '八卷通貫 · 一百二十篇',
                    font: {
                      ascii: '方正爨宝子碑楷书 简繁',
                      eastAsia: '方正爨宝子碑楷书 简繁',
                      hAnsi: '方正爨宝子碑楷书 简繁',
                      cs: '方正爨宝子碑楷书 简繁'
                    },
                    size: 54,
                    color: '5C544D'
                  })
                ]
              }),
              // 段落 4: 副题（双墨线下划线）
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 260, line: 360, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '立骨於濁世  ·  求道於近思',
                    bold: true,
                    underline: { type: 'double', color: COLOR_BORDER },
                    font: {
                      ascii: '汉仪字酷堂会典楷书 W',
                      eastAsia: '汉仪字酷堂会典楷书 W',
                      hAnsi: '汉仪字酷堂会典楷书 W',
                      cs: '汉仪字酷堂会典楷书 W'
                    },
                    size: 46,
                    color: '1A1715'
                  })
                ]
              }),
              // 段落 5: 编订标注
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 340, after: 1200, line: 240, lineRule: 'atLeast' },
                children: [
                  new TextRun({
                    text: '成傑囑命編纂 · 研讀批校工作本',
                    font: {
                      ascii: '方正礼器碑隶书 简繁',
                      eastAsia: '方正礼器碑隶书 简繁',
                      hAnsi: '方正礼器碑隶书 简繁',
                      cs: '方正礼器碑隶书 简繁'
                    },
                    size: 22,
                    color: '8C857B'
                  })
                ]
              }),
              // 段落 6: 印章（明确指定PNG格式）
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 0, after: 0 },
                children: [
                  new ImageRun({
                    data: sealImg,
                    transformation: { width: 48.3, height: 48.3 },
                    type: 'png'
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

module.exports = { buildWenxuanCover };
