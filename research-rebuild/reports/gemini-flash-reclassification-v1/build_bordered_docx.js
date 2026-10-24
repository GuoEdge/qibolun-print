
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

// 字体体系
const FONT_HEADER = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_TITLE  = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W', hAnsi: '汉仪字酷堂会典楷书 W', cs: '汉仪字酷堂会典楷书 W' };
const FONT_BODY   = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_KAI    = { ascii: '楷体', eastAsia: '楷体', hAnsi: '楷体', cs: '楷体' };
const FONT_NOTE_TITLE = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W', hAnsi: '汉仪永字夏蝉 95W', cs: '汉仪永字夏蝉 95W' };
const FONT_FOOTER = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体', cs: '宋体' };

const COLOR_INK = '23201D';       // 熟墨色
const COLOR_SEAL = '8F2D26';      // 沉敛朱砂红
const COLOR_MUTED = '8C857B';     // 雅致浅灰
const COLOR_BORDER_LINE = '7A7368'; // 古籍墨线色 (约 0.75-1pt 沉着细线)

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

const catalogMap = {};
const catLines = fs.readFileSync(CATALOG_PATH, 'utf-8').split(String.fromCharCode(10));
for (const l of catLines) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  catalogMap[d.title] = d;
}

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

function buildBorderedArticle(art, isLast) {
  const elements = [];
  const title = art.title;
  const cat = catalogMap[title] || {};
  const volFull = cat.volume_full_title || '本根敦伦——血亲宗族与家庭抚育';
  const volPrefix = cat.volume_prefix || '本根敦伦';
  const bookletName = cat.booklet_name || '临终关怀与白事奠仪';
  const chineseDate = toChineseDate(art.publishedAt);

  // 1. 篇首题眉（居中，方正爨宝子碑楷书 简繁，朱砂红）
  const headerP = new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 160 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 }
    },
    children: [
      new TextRun({
        text: '岐伯論 · ' + volPrefix,
        font: FONT_HEADER,
        size: 21,
        color: COLOR_SEAL
      })
    ]
  });

  // 2. 篇名与朱砂印
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
    width: { size: 9000, type: WidthType.DXA },
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
            width: { size: 7900, type: WidthType.DXA },
            margins: { top: 0, bottom: 160, left: 0, right: 80 },
            children: [
              new Paragraph({
                spacing: { before: 60, after: 120 },
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
            width: { size: 1100, type: WidthType.DXA },
            margins: { top: 40, bottom: 160, left: 0, right: 0 },
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

  // 3. 非对称正文 + 批注走廊
  const leftCells = [];
  leftCells.push(new Paragraph({
    spacing: { before: 80, after: 180 },
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

  const rightCells = [
    new Paragraph({
      spacing: { before: 80, after: 140 },
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
      spacing: { after: 280, line: 380, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    }),
    new Paragraph({
      spacing: { after: 280, line: 380, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    }),
    new Paragraph({
      spacing: { after: 280, line: 380, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    })
  ];

  const bodyGrid = new Table({
    width: { size: 9000, type: WidthType.DXA },
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
            width: { size: 5850, type: WidthType.DXA },
            margins: { top: 0, bottom: 180, left: 0, right: 240 },
            borders: {
              right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' }
            },
            children: leftCells
          }),
          new TableCell({
            width: { size: 3150, type: WidthType.DXA },
            margins: { top: 0, bottom: 180, left: 240, right: 0 },
            children: rightCells
          })
        ]
      })
    ]
  });

  // 4. 篇末题注
  const footerP1 = new Paragraph({
    spacing: { before: 200, after: 40 },
    alignment: AlignmentType.RIGHT,
    border: {
      top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC', space: 6 }
    },
    children: [
      new TextRun({
        text: '〔 專 題 〕 ' + volFull + ' · ' + bookletName,
        font: FONT_FOOTER,
        size: 15,
        color: COLOR_MUTED,
        letterSpacing: 10
      })
    ]
  });

  const footerP2 = new Paragraph({
    spacing: { before: 0, after: 80 },
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
  });

  // 核心：古籍四周方框线（文人雅致线框）
  // 采用双重边框（双边线 Double Border）或典雅单细线，框住整篇内容
  const pageFrameTable = new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },    // 古籍双线天头
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE }, // 古籍双线地脚
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },     // 内侧订口实线
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE }    // 外侧切口实线
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 9355, type: WidthType.DXA },
            margins: { top: 160, bottom: 160, left: 220, right: 220 }, // 框内衬白留空
            children: [
              headerP,
              titleTable,
              bodyGrid,
              footerP1,
              footerP2
            ]
          })
        ]
      })
    ]
  });

  elements.push(pageFrameTable);

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
  docElements.push(...buildBorderedArticle(art, isLast));
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
  console.log('DOCX with classical borders successfully compiled at:', docxPath);
}).catch(err => {
  console.error('Error generating bordered DOCX:', err);
  process.exit(1);
});
