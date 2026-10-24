
const fs = require('fs');
const path = require('path');
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  WidthType,
  BorderStyle,
  AlignmentType,
  ImageRun,
  Footer,
  PageNumber
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const OUT_DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/';
const MERGED_CORPUS = path.join(OUT_DIR, 'all-articles-merged-v3.jsonl');
const CATALOG_PATH = path.join(OUT_DIR, 'workbook-40b-all-catalog.jsonl');

// 成杰指定的四大文人书法字体
const FONT_HEADER = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_TITLE  = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W', hAnsi: '汉仪字酷堂会典楷书 W', cs: '汉仪字酷堂会典楷书 W' };
const FONT_BODY   = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_KAI    = { ascii: '楷体', eastAsia: '楷体', hAnsi: '楷体', cs: '楷体' };
const FONT_NOTE_TITLE = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W', hAnsi: '汉仪永字夏蝉 95W', cs: '汉仪永字夏蝉 95W' };
const FONT_FOOTER = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体', cs: '宋体' };

const COLOR_INK = '23201D';       // 熟墨色
const COLOR_SEAL = '8F2D26';      // 沉敛朱砂红
const COLOR_MUTED = '8C857B';     // 雅致浅灰

// 汉字纪年转换辅助
function toChineseDate(rawTs) {
  if (!rawTs) return '';
  const d = new Date(Number(rawTs));
  const digits = ['〇', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
  const y = String(d.getFullYear()).split('').map(c => digits[Number(c)]).join('') + '年';
  const mNum = d.getMonth() + 1;
  const m = (mNum <= 10 ? (mNum === 10 ? '十' : digits[mNum]) : (mNum === 11 ? '十一' : '十二')) + '月';
  const dNum = d.getDate();
  let dayStr = '';
  if (dNum <= 10) {
    dayStr = (dNum === 10 ? '十' : digits[dNum]);
  } else if (dNum < 20) {
    dayStr = '十' + digits[dNum % 10];
  } else if (dNum === 20) {
    dayStr = '二十';
  } else if (dNum < 30) {
    dayStr = '二十' + digits[dNum % 10];
  } else {
    dayStr = '三十' + (dNum === 31 ? '一' : '');
  }
  return y + m + dayStr + '日';
}

// 读取编目元数据
const catalogMap = {};
const catLines = fs.readFileSync(CATALOG_PATH, 'utf-8').split(String.fromCharCode(10));
for (const l of catLines) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  catalogMap[d.title] = d;
}

// 读取文章
const targetTitles = ['铺路石', '奠仪几何', '何金银', '稳而后解'];
const articleMap = {};
const lines = fs.readFileSync(MERGED_CORPUS, 'utf-8').split(String.fromCharCode(10));
for (const l of lines) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  if (targetTitles.includes(d.title)) {
    articleMap[d.title] = d;
  }
}

const articles = targetTitles.map(t => articleMap[t]).filter(Boolean);

function buildArticleElements(art, isLast) {
  const elements = [];
  const title = art.title;
  const cat = catalogMap[title] || {};
  const volFull = cat.volume_full_title || '本根敦伦——血亲宗族与家庭抚育';
  const volPrefix = cat.volume_prefix || '本根敦伦';
  const bookletName = cat.booklet_name || '临终关怀与白事奠仪';
  const chineseDate = toChineseDate(art.publishedAt);

  // 1. 篇首题眉：遵照成杰第一页修改（居中，方正爨宝子碑楷书 简繁，朱砂红 #8F2D26，字号 21，繁体【岐伯論 · 本根敦倫】）
  elements.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'C8C4B7', space: 4 }
    },
    children: [
      new TextRun({
        text: '岐伯論 · ' + volPrefix,
        font: FONT_HEADER,
        size: 21,
        color: COLOR_SEAL
      })
    ]
  }));

  // 2. 标题与朱砂印章二维码
  const qrPngPath = path.join(OUT_DIR, 'qr_stamp_' + (
    title === '铺路石' ? 'puluoshi' :
    title === '奠仪几何' ? 'dianyi' :
    title === '何金银' ? 'hejinyin' : 'wenerhoujie'
  ) + '.png');

  let qrImage = null;
  if (fs.existsSync(qrPngPath)) {
    qrImage = new ImageRun({
      data: fs.readFileSync(qrPngPath),
      transformation: { width: 34, height: 34 }
    });
  }

  const titleTable = new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.NONE },
      bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE },
      right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 8200, type: WidthType.DXA },
            margins: { top: 0, bottom: 200, left: 0, right: 100 },
            children: [
              new Paragraph({
                spacing: { before: 100, after: 150 },
                children: [
                  new TextRun({
                    text: title,
                    font: FONT_TITLE,
                    size: 42,
                    bold: true,
                    color: '1A1715',
                    letterSpacing: 40
                  })
                ]
              })
            ]
          }),
          new TableCell({
            width: { size: 1155, type: WidthType.DXA },
            margins: { top: 60, bottom: 200, left: 0, right: 0 },
            children: [
              new Paragraph({
                alignment: AlignmentType.RIGHT,
                children: qrImage ? [qrImage] : []
              })
            ]
          })
        ]
      })
    ]
  });
  elements.push(titleTable);

  // 3. 核心布局：非对称双栏
  const leftCells = [];

  // 【問】客问区域：采用繁体【問】，楷体沉静
  leftCells.push(new Paragraph({
    spacing: { before: 100, after: 200 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 16, color: COLOR_SEAL, space: 8 },
      bottom: { style: BorderStyle.DASHED, size: 4, color: 'DEDAD0', space: 6 }
    },
    children: [
      new TextRun({
        text: '【問】 ',
        font: FONT_HEADER,
        bold: true,
        size: 19,
        color: COLOR_SEAL
      }),
      new TextRun({
        text: art.question || '',
        font: FONT_KAI,
        size: 20,
        color: '453F3A'
      })
    ]
  }));

  // 正文段落：采用成杰精选的【方正文沁永乐大典体M 简】
  const paragraphs = (art.text || '').trim().split(String.fromCharCode(10));
  for (const p of paragraphs) {
    if (!p.trim()) continue;
    leftCells.push(new Paragraph({
      indent: { firstLine: 420 },
      spacing: { after: 180, line: 380, lineRule: 'atLeast' },
      alignment: AlignmentType.JUSTIFIED,
      children: [
        new TextRun({
          text: p.trim(),
          font: FONT_BODY,
          size: 21,
          color: COLOR_INK
        })
      ]
    }));
  }

  // 右侧走廊：批注留白（题头采用成杰精选的【汉仪永字夏蝉 95W】）
  const rightCells = [
    new Paragraph({
      spacing: { before: 100, after: 150 },
      children: [
        new TextRun({
          text: '〔 随 文 批 校 〕',
          font: FONT_NOTE_TITLE,
          size: 16,
          color: 'B0A99F',
          letterSpacing: 20
        })
      ]
    }),
    new Paragraph({
      spacing: { after: 300, line: 400, lineRule: 'atLeast' },
      border: {
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 6 }
      },
      children: [new TextRun({ text: ' ', size: 20 })]
    }),
    new Paragraph({
      spacing: { after: 300, line: 400, lineRule: 'atLeast' },
      border: {
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 6 }
      },
      children: [new TextRun({ text: ' ', size: 20 })]
    }),
    new Paragraph({
      spacing: { after: 300, line: 400, lineRule: 'atLeast' },
      border: {
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 6 }
      },
      children: [new TextRun({ text: ' ', size: 20 })]
    })
  ];

  const workspaceTable = new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.NONE },
      bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE },
      right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 6100, type: WidthType.DXA },
            margins: { top: 0, bottom: 200, left: 0, right: 280 },
            borders: {
              right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' }
            },
            children: leftCells
          }),
          new TableCell({
            width: { size: 3255, type: WidthType.DXA },
            margins: { top: 0, bottom: 200, left: 280, right: 0 },
            children: rightCells
          })
        ]
      })
    ]
  });
  elements.push(workspaceTable);

  // 4. 篇末典雅落款：彻底剔除“全文898字·岐伯答论”，呈现【專題標籤】与【收錄日期】
  elements.push(new Paragraph({
    spacing: { before: 260, after: 60 },
    alignment: AlignmentType.RIGHT,
    border: {
      top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC', space: 8 }
    },
    children: [
      new TextRun({
        text: '〔 專 題 〕 ' + volFull + ' · ' + bookletName,
        font: FONT_FOOTER,
        size: 15, // 7.5pt
        color: COLOR_MUTED,
        letterSpacing: 10
      })
    ]
  }));

  elements.push(new Paragraph({
    spacing: { before: 0, after: 120 },
    alignment: AlignmentType.RIGHT,
    children: [
      new TextRun({
        text: '〔 錄 於 〕 ' + chineseDate,
        font: FONT_FOOTER,
        size: 15,
        color: COLOR_MUTED,
        letterSpacing: 10
      })
    ]
  }));

  if (!isLast) {
    elements.push(new Paragraph({
      pageBreakBefore: true,
      children: []
    }));
  }

  return elements;
}

const docElements = [];
articles.forEach((art, idx) => {
  const isLast = idx === articles.length - 1;
  docElements.push(...buildArticleElements(art, isLast));
});

const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: FONT_BODY,
          size: 21,
          color: COLOR_INK
        }
      }
    }
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1247, right: 1020, bottom: 1134, left: 1587 }
        }
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({ text: '· ', font: FONT_FOOTER, size: 17, color: '999999' }),
                new TextRun({ children: [PageNumber.CURRENT], font: FONT_FOOTER, size: 17, color: '999999' }),
                new TextRun({ text: ' ·', font: FONT_FOOTER, size: 17, color: '999999' })
              ]
            })
          ]
        })
      },
      children: docElements
    }
  ]
});

Packer.toBuffer(doc).then(buffer => {
  const docxPath = path.join(OUT_DIR, '岐伯论-现代学者批校手卷本-可编辑原型.docx');
  fs.writeFileSync(docxPath, buffer);
  console.log('DOCX successfully compiled with user fonts & footer metadata:', docxPath);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
