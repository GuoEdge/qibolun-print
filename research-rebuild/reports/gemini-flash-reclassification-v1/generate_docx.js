
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

const FONT_SERIF = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体' };
const FONT_KAI = { ascii: '楷体', eastAsia: '楷体', hAnsi: '楷体' };
const COLOR_INK = '23201D';
const COLOR_MUTED = '8C857B';

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
  const rawTs = art.publishedAt;
  let dateStr = '';
  if (rawTs) {
    const d = new Date(Number(rawTs));
    dateStr = d.getFullYear() + '.' + String(d.getMonth() + 1).padStart(2, '0') + '.' + String(d.getDate()).padStart(2, '0');
  }
  const charCount = (art.text || '').length;

  // 1. 篇首导航
  elements.push(new Paragraph({
    alignment: AlignmentType.RIGHT,
    spacing: { after: 200 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'C8C4B7', space: 4 }
    },
    children: [
      new TextRun({
        text: '岐伯论 · 本根敦伦',
        font: FONT_SERIF,
        size: 17,
        color: COLOR_MUTED,
        letterSpacing: 30
      }),
      new TextRun({
        text: '        ' + dateStr,
        font: FONT_SERIF,
        size: 17,
        color: 'A39C91'
      })
    ]
  }));

  // 2. 标题与朱砂印章
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
                    font: FONT_SERIF,
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

  // 3. 核心布局工作台：非对称双栏
  const leftCells = [];

  leftCells.push(new Paragraph({
    spacing: { before: 100, after: 200 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 16, color: '8F2D26', space: 8 },
      bottom: { style: BorderStyle.DASHED, size: 4, color: 'DEDAD0', space: 6 }
    },
    children: [
      new TextRun({
        text: '【问】 ',
        font: FONT_SERIF,
        bold: true,
        size: 19,
        color: '8F2D26'
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
          font: FONT_SERIF,
          size: 21,
          color: COLOR_INK
        })
      ]
    }));
  }

  // 右侧走廊：批注留白
  const rightCells = [
    new Paragraph({
      spacing: { before: 100, after: 150 },
      children: [
        new TextRun({
          text: '〔 随 文 批 校 〕',
          font: FONT_SERIF,
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

  elements.push(new Paragraph({
    spacing: { before: 300, after: 100 },
    alignment: AlignmentType.RIGHT,
    border: {
      top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC', space: 8 }
    },
    children: [
      new TextRun({
        text: '全文 ' + charCount + ' 字 · 岐伯答论',
        font: FONT_SERIF,
        size: 15,
        color: 'B0A99F'
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
          font: FONT_SERIF,
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
          size: {
            width: 11906,
            height: 16838
          },
          margin: {
            top: 1247,
            right: 1020,
            bottom: 1134,
            left: 1587
          }
        }
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({
                  text: '· ',
                  font: FONT_SERIF,
                  size: 17,
                  color: '999999'
                }),
                new TextRun({
                  children: [PageNumber.CURRENT],
                  font: FONT_SERIF,
                  size: 17,
                  color: '999999'
                }),
                new TextRun({
                  text: ' ·',
                  font: FONT_SERIF,
                  size: 17,
                  color: '999999'
                })
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
  console.log('DOCX successfully generated at:', docxPath);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
