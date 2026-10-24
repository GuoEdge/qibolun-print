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
const QR_DIR = path.join(OUT_DIR, 'b01_qr_stamps');

// 文人书法字体矩阵
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
const COLOR_BORDER_LINE = '7A7368';
const COLOR_MUTED = '8C857B';       // 古籍墨线外框
const COLOR_FOOTER      = '808080';       // 篇末题注深灰
const COLOR_PAGE_NUM    = '000000';       // 浓黑叶码

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

// 读入全量正文与编目
const artMap = {};
fs.readFileSync(MERGED_CORPUS, 'utf-8').split('\n').forEach(l => {
  if (l.trim()) {
    const d = JSON.parse(l);
    artMap[d.id] = d;
  }
});

const b01Articles = [];
fs.readFileSync(CATALOG_PATH, 'utf-8').split('\n').forEach(l => {
  if (l.trim()) {
    const r = JSON.parse(l);
    if (r.booklet_code === 'B01') {
      const full = artMap[r.original_id] || {};
      r.full_text = full.text || '';
      b01Articles.push(r);
    }
  }
});

console.log('Building B01 booklet with articles:', b01Articles.length);

const docElements = [];

// ==================== 1. 典藏内扉页 (Title Page) ====================
docElements.push(
  new Paragraph({
    spacing: { before: 1800, after: 300 },
    alignment: AlignmentType.CENTER,
    children: [
      new TextRun({
        text: '岐  伯  論',
        font: FONT_HEADER,
        size: 56, // 28pt
        bold: true,
        color: COLOR_SEAL,
        letterSpacing: 80
      })
    ]
  }),
  new Paragraph({
    spacing: { before: 200, after: 400 },
    alignment: AlignmentType.CENTER,
    children: [
      new TextRun({
        text: '【 卷 一 】 本 根 敦 倫',
        font: FONT_TITLE,
        size: 32, // 16pt
        color: '1A1715',
        letterSpacing: 40
      })
    ]
  }),
  new Paragraph({
    spacing: { before: 100, after: 1200 },
    alignment: AlignmentType.CENTER,
    children: [
      new TextRun({
        text: '甲 冊 · 幼 兒 啟 蒙 與 性 情 習 慣',
        font: FONT_TITLE,
        size: 36, // 18pt
        bold: true,
        color: '1A1715',
        letterSpacing: 30
      })
    ]
  }),
  new Paragraph({
    spacing: { before: 800, after: 200 },
    alignment: AlignmentType.CENTER,
    border: {
      top: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 12 }
    },
    children: [
      new TextRun({
        text: '全 冊 凡 五 十 二 篇  ·  成 傑 研 讀 批 校 本',
        font: FONT_FOOTER,
        size: 22,
        color: COLOR_MUTED,
        letterSpacing: 20
      })
    ]
  }),
  new Paragraph({ pageBreakBefore: true, children: [] })
);

// ==================== 2. 卷内总目页 (Table of Contents) ====================
const tocRows = [
  new TableRow({
    children: [
      new TableCell({
        width: { size: 9000, type: WidthType.DXA },
        margins: { top: 0, bottom: 200, left: 0, right: 0 },
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 100, after: 300 },
            border: {
              bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE, space: 8 }
            },
            children: [
              new TextRun({
                text: '甲 冊 篇 目 綱 錄',
                font: FONT_HEADER,
                size: 28,
                bold: true,
                color: COLOR_SEAL,
                letterSpacing: 30
              })
            ]
          })
        ]
      })
    ]
  })
];

// 将 52 篇分为两列并列排布的雅致纲录表
const tocListCellsLeft = [];
const tocListCellsRight = [];

b01Articles.forEach((art, i) => {
  const ordStr = String(i + 1).padStart(2, '0');
  const p = new Paragraph({
    spacing: { before: 40, after: 60 },
    children: [
      new TextRun({
        text: ordStr + '  ',
        font: FONT_PAGE_NUM,
        size: 18,
        color: COLOR_SEAL
      }),
      new TextRun({
        text: '《' + art.title + '》',
        font: FONT_BODY,
        size: 20,
        color: COLOR_INK
      })
    ]
  });

  if (i < 26) {
    tocListCellsLeft.push(p);
  } else {
    tocListCellsRight.push(p);
  }
});

const tocTable = new Table({
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
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 0, bottom: 0, left: 100, right: 100 },
          children: tocListCellsLeft
        }),
        new TableCell({
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 0, bottom: 0, left: 100, right: 100 },
          children: tocListCellsRight
        })
      ]
    })
  ]
});

// 目录外层古籍边框
docElements.push(
  new Table({
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
            margins: { top: 180, bottom: 180, left: 200, right: 200 },
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { after: 150 },
                children: [
                  new TextRun({
                    text: '岐伯論 · 本根敦倫',
                    font: FONT_HEADER,
                    size: 22,
                    color: COLOR_SEAL,
                    letterSpacing: 20
                  })
                ]
              }),
              tocTable
            ]
          })
        ]
      })
    ]
  }),
  new Paragraph({ pageBreakBefore: true, children: [] })
);

// ==================== 3. 全部 52 篇正文叶排版 ====================
function buildArticlePage(params) {
  const {
    title,
    isContinuation,
    question,
    paragraphs,
    qrPngPath,
    showFooter,
    chineseDate
  } = params;

  const pageElements = [];

  // 天头题眉
  const headerText = isContinuation
    ? '岐伯論 · ' + title + '（承前）'
    : '岐伯論 · 本根敦倫';

  const outOfFrameHeaderP = new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 140 },
    children: [
      new TextRun({
        text: headerText,
        font: FONT_HEADER,
        size: 22,
        color: COLOR_SEAL,
        letterSpacing: 20
      })
    ]
  });
  pageElements.push(outOfFrameHeaderP);

  const innerElements = [];

  // 篇名居中
  if (!isContinuation) {
    innerElements.push(
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 80, after: 180 },
        children: [
          new TextRun({
            text: title,
            font: FONT_TITLE,
            size: 44,
            bold: true,
            color: '1A1715',
            letterSpacing: 40
          })
        ]
      })
    );
  }

  // 正文主论与批校走廊
  const leftCells = [];
  if (!isContinuation && question) {
    leftCells.push(new Paragraph({
      spacing: { before: 40, after: 180 },
      border: {
        left: { style: BorderStyle.SINGLE, size: 16, color: COLOR_SEAL, space: 8 },
        bottom: { style: BorderStyle.DASHED, size: 4, color: 'DEDAD0', space: 8 }
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
      indent: { firstLine: 460 },
      spacing: { before: 60, after: 140, line: 320, lineRule: 'atLeast' },
      alignment: AlignmentType.BOTH,
      children: [
        new TextRun({
          text: p,
          font: FONT_BODY,
          size: 23,
          color: COLOR_INK
        })
      ]
    }));
  }

  // 短篇案语札记
  const charTotal = paragraphs.join('').length;
  if (!isContinuation && charTotal < 300) {
    leftCells.push(
      new Paragraph({
        spacing: { before: 200, after: 120 },
        border: {
          top: { style: BorderStyle.DASHED, size: 4, color: 'D8D4C8', space: 6 }
        },
        children: [
          new TextRun({
            text: '〔 案 語 札 記 〕',
            font: FONT_NOTE_TITLE,
            size: 16,
            color: 'A8A297',
            letterSpacing: 20
          })
        ]
      })
    );
    for (let k = 0; k < 4; k++) {
      leftCells.push(new Paragraph({
        spacing: { after: 260, line: 320, lineRule: 'atLeast' },
        border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
        children: [new TextRun({ text: ' ', size: 20 })]
      }));
    }
  }

  // 随文批校走廊
  const rightCells = [
    new Paragraph({
      spacing: { before: 40, after: 120 },
      children: [
        new TextRun({
          text: '〔 随 文 批 校 〕',
          font: FONT_NOTE_TITLE,
          size: 16,
          color: 'B0A99F',
          letterSpacing: 20
        })
      ]
    })
  ];

  const neededLines = Math.max(8, Math.min(22, Math.floor(paragraphs.length * 1.5) + (question ? 3 : 0)));
  for (let li = 0; li < neededLines; li++) {
    rightCells.push(new Paragraph({
      spacing: { after: 240, line: 320, lineRule: 'atLeast' },
      border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 4 } },
      children: [new TextRun({ text: ' ', size: 20 })]
    }));
  }

  const workspaceTable = new Table({
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
            width: { size: 6850, type: WidthType.DXA },
            borders: {
              right: { style: BorderStyle.DASHED, size: 4, color: 'E6E3D8' }
            },
            margins: { top: 0, bottom: 120, left: 0, right: 200 },
            children: leftCells
          }),
          new TableCell({
            width: { size: 2150, type: WidthType.DXA },
            margins: { top: 0, bottom: 120, left: 200, right: 0 },
            children: rightCells
          })
        ]
      })
    ]
  });
  innerElements.push(workspaceTable);

  // 篇末落款题注与右侧押角印
  if (showFooter) {
    let qrImage = null;
    if (fs.existsSync(qrPngPath)) {
      qrImage = new ImageRun({
        data: fs.readFileSync(qrPngPath),
        transformation: { width: 34, height: 34 }
      });
    }

    const colophonTable = new Table({
      width: { size: 9000, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: 'E8E5DC' },
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
              width: { size: 7600, type: WidthType.DXA },
              margins: { top: 140, bottom: 40, left: 0, right: 100 },
              children: [
                new Paragraph({
                  alignment: AlignmentType.LEFT,
                  spacing: { before: 0, after: 30 },
                  children: [
                    new TextRun({
                      text: '〔 專 題 〕 本根敦倫 —— 血親宗族與家庭撫育 · 甲冊 幼兒啟蒙與性情習慣',
                      font: FONT_FOOTER,
                      size: 20,
                      color: COLOR_FOOTER
                    })
                  ]
                }),
                new Paragraph({
                  alignment: AlignmentType.LEFT,
                  spacing: { before: 0, after: 0 },
                  children: [
                    new TextRun({
                      text: '〔 錄 於 〕 ' + chineseDate,
                      font: FONT_FOOTER,
                      size: 20,
                      color: COLOR_FOOTER
                    })
                  ]
                })
              ]
            }),
            new TableCell({
              width: { size: 1400, type: WidthType.DXA },
              margins: { top: 120, bottom: 40, left: 0, right: 0 },
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

    innerElements.push(colophonTable);
  }

  // 古籍墨线外框
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
            margins: { top: 140, bottom: 140, left: 180, right: 180 },
            children: innerElements
          })
        ]
      })
    ]
  });

  pageElements.push(outerBorderTable);
  return pageElements;
}

b01Articles.forEach((art, artIdx) => {
  const title = art.title;
  const chineseDate = toChineseDate(art.published_at);
  const qrPngPath = path.join(QR_DIR, art.original_id + '.png');
  const allParas = (art.full_text || '').trim().split('\n').map(p => p.trim()).filter(Boolean);

  if (allParas.length > 28) {
    const pPart1 = allParas.slice(0, 26);
    const pPart2 = allParas.slice(26);

    const page1 = buildArticlePage({
      title,
      isContinuation: false,
      question: art.question,
      paragraphs: pPart1,
      qrPngPath,
      showFooter: false,
      chineseDate
    });
    docElements.push(...page1);
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

    const page2 = buildArticlePage({
      title,
      isContinuation: true,
      question: null,
      paragraphs: pPart2,
      qrPngPath,
      showFooter: true,
      chineseDate
    });
    docElements.push(...page2);
  } else {
    const page = buildArticlePage({
      title,
      isContinuation: false,
      question: art.question,
      paragraphs: allParas,
      qrPngPath,
      showFooter: true,
      chineseDate
    });
    docElements.push(...page);
  }

  // 篇章间分页 (最后一篇除外)
  if (artIdx < b01Articles.length - 1) {
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));
  }
});

// ==================== 4. 册末整册研读大案语页 (Afterword) ====================
docElements.push(
  new Paragraph({ pageBreakBefore: true, children: [] }),
  new Table({
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
            margins: { top: 200, bottom: 200, left: 240, right: 240 },
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { after: 200 },
                children: [
                  new TextRun({
                    text: '岐伯論 · 本根敦倫',
                    font: FONT_HEADER,
                    size: 22,
                    color: COLOR_SEAL,
                    letterSpacing: 20
                  })
                ]
              }),
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 100, after: 300 },
                children: [
                  new TextRun({
                    text: '甲 冊 研 讀 札 記 總 案',
                    font: FONT_TITLE,
                    size: 36,
                    bold: true,
                    color: '1A1715',
                    letterSpacing: 30
                  })
                ]
              }),
              ...Array.from({ length: 16 }).map(() =>
                new Paragraph({
                  spacing: { after: 320, line: 360, lineRule: 'atLeast' },
                  border: { bottom: { style: BorderStyle.DASHED, size: 4, color: 'EAE7DF', space: 6 } },
                  children: [new TextRun({ text: ' ', size: 20 })]
                })
              )
            ]
          })
        ]
      })
    ]
  })
);

const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: FONT_BODY,
          size: 23,
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
          margin: {
            top: 1020,
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
              alignment: AlignmentType.RIGHT,
              children: [
                new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
                new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
                new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
              ]
            })
          ]
        }),
        even: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.LEFT,
              children: [
                new TextRun({ text: '第 ', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
                new TextRun({ children: [PageNumber.CURRENT], font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM }),
                new TextRun({ text: ' 葉', font: FONT_PAGE_NUM, bold: true, size: 26, color: COLOR_PAGE_NUM })
              ]
            })
          ]
        })
      },
      children: docElements
    }
  ]
});

const FINAL_BOOKLET_PATH = path.join(OUT_DIR, '岐伯论·卷一本根敦伦·甲册_幼儿启蒙与性情习惯.docx');

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(FINAL_BOOKLET_PATH, buffer);
  console.log('Booklet B01 successfully compiled at:', FINAL_BOOKLET_PATH);
}).catch(err => {
  console.error('Error generating B01 Booklet:', err);
  process.exit(1);
});
