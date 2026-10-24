
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
  Header,
  Footer,
  PageNumber
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const OUT_DIR = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/';
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

const COLOR_INK         = '23201D';       // 熟墨色
const COLOR_SEAL        = '8F2D26';       // 朱砂红
const COLOR_BORDER_LINE = '7A7368';       // 古籍墨线外框
const COLOR_FOOTER      = '808080';       // 篇末题注浅灰
const COLOR_PAGE_NUM    = '4A453F';       // 沉稳熟褐

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

// 包含经典样本与最新增量样本
const targetTitles = ['铺路石', '先辈说', '何金银', '穷关心', '稳而后解'];
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

function buildArticlePage(params) {
  const {
    title,
    volPrefix,
    isContinuation,
    question,
    paragraphs,
    qrPngPath,
    showFooter,
    volFull,
    bookletName,
    chineseDate
  } = params;

  const headerText = isContinuation
    ? '岐伯論 · ' + title + '（承前）'
    : '岐伯論 · ' + volPrefix;

  const headerP = new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 }
    },
    children: [
      new TextRun({
        text: headerText,
        font: FONT_HEADER,
        size: 21,
        color: COLOR_SEAL
      })
    ]
  });

  let qrImage = null;
  if (!isContinuation && fs.existsSync(qrPngPath)) {
    qrImage = new ImageRun({
      data: fs.readFileSync(qrPngPath),
      transformation: { width: 34, height: 34 }
    });
  }

  const innerRows = [];
  if (!isContinuation) {
    innerRows.push(
      new TableRow({
        children: [
          new TableCell({
            width: { size: 6670, type: WidthType.DXA },
            margins: { top: 0, bottom: 160, left: 0, right: 80 },
            children: [
              new Paragraph({
                spacing: { before: 60, after: 120 },
                alignment: AlignmentType.CENTER,
                children: [
                  new TextRun({
                    text: title,
                    font: FONT_TITLE,
                    size: 42,
                    bold: true,
                    color: '1A1715'
                  })
                ]
              })
            ]
          }),
          new TableCell({
            width: { size: 2330, type: WidthType.DXA },
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
    );
  }

  const leftCells = [];
  if (!isContinuation && question) {
    leftCells.push(new Paragraph({
      spacing: { before: 80, after: 180 },
      border: {
        left: { style: BorderStyle.SINGLE, size: 16, color: COLOR_SEAL, space: 8 },
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'DEDAD0', space: 6 }
      },
      children: [
        new TextRun({
          text: '【問】',
          font: FONT_Q_MARK,
          bold: true,
          size: 28,
          color: COLOR_SEAL
        }),
        new TextRun({
          text: ' ',
          font: FONT_Q_MARK,
          size: 19,
          color: COLOR_SEAL
        }),
        new TextRun({
          text: question,
          font: FONT_Q_TEXT,
          bold: true,
          size: 24,
          color: '453F3A'
        })
      ]
    }));
  }

  for (const p of paragraphs) {
    leftCells.push(new Paragraph({
      indent: { firstLine: 420 },
      spacing: { after: 180, line: 380, lineRule: 'atLeast' },
      alignment: AlignmentType.BOTH,
      children: [
        new TextRun({
          text: p,
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

  innerRows.push(
    new TableRow({
      children: [
        new TableCell({
          width: { size: 6670, type: WidthType.DXA },
          borders: {
            right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' }
          },
          margins: { top: 0, bottom: 180, left: 0, right: 240 },
          children: leftCells
        }),
        new TableCell({
          width: { size: 2330, type: WidthType.DXA },
          margins: { top: 0, bottom: 180, left: 240, right: 0 },
          children: rightCells
        })
      ]
    })
  );

  const innerTable = new Table({
    width: { size: 9000, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.NONE },
      bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE },
      right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: innerRows
  });

  const boxContent = [headerP, innerTable];

  if (showFooter) {
    boxContent.push(
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 200, after: 40 },
        border: {
          top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC', space: 6 }
        },
        children: [
          new TextRun({
            text: '〔 專 題 〕 ' + volFull + ' · ' + bookletName,
            font: FONT_FOOTER,
            size: 20,
            color: COLOR_FOOTER
          })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 80 },
        children: [
          new TextRun({
            text: '〔 錄 於 〕 ' + chineseDate,
            font: FONT_FOOTER,
            size: 20,
            color: COLOR_FOOTER
          })
        ]
      })
    );
  }

  const outerBorderTable = new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 8, color: COLOR_BORDER_LINE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 9355, type: WidthType.DXA },
            margins: { top: 160, bottom: 160, left: 220, right: 220 },
            children: boxContent
          })
        ]
      })
    ]
  });

  return outerBorderTable;
}

const docElements = [];

articles.forEach((art, artIdx) => {
  const title = art.title;
  const cat = catalogMap[title] || {};
  const volFull = cat.volume_full_title || '本根敦伦——血亲宗族与家庭抚育';
  const volPrefix = cat.volume_prefix || '本根敦伦';
  const bookletName = cat.booklet_name || '临终关怀与白事奠仪';
  const chineseDate = toChineseDate(art.publishedAt);
  const qrPngPath = path.join(OUT_DIR, 'qr_stamp_' + (
    title === '铺路石' ? 'puluoshi' :
    title === '奠仪几何' ? 'dianyi' :
    title === '何金银' ? 'hejinyin' :
    title === '先辈说' ? 'xianbeishuo' :
    title === '穷关心' ? 'qiongguanxin' : 'wenerhoujie'
  ) + '.png');

  const allParas = (art.text || '').trim().split(String.fromCharCode(10)).map(p => p.trim()).filter(Boolean);

  if (allParas.length > 25) {
    const pPart1 = allParas.slice(0, 24);
    const pPart2 = allParas.slice(24);

    const page1Table = buildArticlePage({
      title,
      volPrefix,
      isContinuation: false,
      question: art.question,
      paragraphs: pPart1,
      qrPngPath,
      showFooter: false,
      volFull,
      bookletName,
      chineseDate
    });
    docElements.push(page1Table);
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

    const page2Table = buildArticlePage({
      title,
      volPrefix,
      isContinuation: true,
      question: null,
      paragraphs: pPart2,
      qrPngPath,
      showFooter: true,
      volFull,
      bookletName,
      chineseDate
    });
    docElements.push(page2Table);
  } else {
    const pageTable = buildArticlePage({
      title,
      volPrefix,
      isContinuation: false,
      question: art.question,
      paragraphs: allParas,
      qrPngPath,
      showFooter: true,
      volFull,
      bookletName,
      chineseDate
    });
    docElements.push(pageTable);
  }

  if (artIdx < articles.length - 1) {
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));
  }
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
              alignment: AlignmentType.RIGHT,
              children: [
                new TextRun({ text: '第 ', font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM }),
                new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM }),
                new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM })
              ]
            })
          ]
        }),
        even: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.LEFT,
              children: [
                new TextRun({ text: '第 ', font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM }),
                new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM }),
                new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, size: 20, color: COLOR_PAGE_NUM })
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
  console.log('DOCX updated with new articles and full classical styling:', docxPath);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
