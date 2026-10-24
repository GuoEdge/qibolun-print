
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
const QR_DIR = path.join(OUT_DIR, 'qr_cache_b01');
const MERGED_CORPUS = path.join(OUT_DIR, 'all-articles-merged-v3.jsonl');
const CATALOG_PATH = path.join(OUT_DIR, 'workbook-40b-all-catalog.jsonl');

// 文人书法字体矩阵
const FONT_HEADER     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_TITLE      = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W', hAnsi: '汉仪字酷堂会典楷书 W', cs: '汉仪字酷堂会典楷书 W' };
const FONT_Q_MARK     = { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁', hAnsi: '方正爨宝子碑楷书 简繁', cs: '方正爨宝子碑楷书 简繁' };
const FONT_Q_TEXT     = { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W', hAnsi: '汉仪昌黎宋刻本原版W', cs: '汉仪昌黎宋刻本原版W' };
const FONT_BODY       = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_NOTE_TITLE = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W', hAnsi: '汉仪永字夏蝉 95W', cs: '汉仪永字夏蝉 95W' };
const FONT_FOOTER     = { ascii: '方正礼器碑隶书 简繁', eastAsia: '方正礼器碑隶书 简繁', hAnsi: '方正礼器碑隶书 简繁', cs: '方正礼器碑隶书 简繁' };
const FONT_PAGE_NUM   = { ascii: '方正文沁永乐大典体M 简', eastAsia: '方正文沁永乐大典体M 简', hAnsi: '方正文沁永乐大典体M 简', cs: '方正文沁永乐大典体M 简' };
const FONT_SYSTEM     = { ascii: '宋体', eastAsia: '宋体', hAnsi: '宋体', cs: '宋体' };

const COLOR_INK         = '23201D';       // 熟墨色
const COLOR_SEAL        = '8F2D26';       // 朱砂红
const COLOR_BORDER_LINE = '7A7368';       // 古籍墨线外框
const COLOR_FOOTER      = '808080';
const COLOR_MUTED       = '8C857B';       // 篇末题注深灰
const COLOR_PAGE_NUM    = '000000';       // 浓黑叶码

const VOL_PREFIX_TRAD = '本根敦倫';
const VOL_FULL_TRAD   = '本根敦倫 —— 血親宗族與家庭撫育';
const BOOKLET_STEM    = '甲';
const BOOKLET_TRAD    = '幼兒啟蒙與性情習慣';

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

// 1. 读取 B01 编目列表
const catLines = fs.readFileSync(CATALOG_PATH, 'utf-8').split(String.fromCharCode(10));
const b01Catalog = [];
for (const l of catLines) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  if (d.booklet_code === 'B01') {
    b01Catalog.push(d);
  }
}
console.log('B01 catalog entries: ' + b01Catalog.length);

// 2. 读取语料库正文
const corpusMap = {};
const corpusLines = fs.readFileSync(MERGED_CORPUS, 'utf-8').split(String.fromCharCode(10));
for (const l of corpusLines) {
  if (!l.trim()) continue;
  const d = JSON.parse(l);
  corpusMap[d.id] = d;
}

// 3. 构建单篇页面渲染函数
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

  // 天头题眉（框外居中）
  const headerText = isContinuation
    ? '岐伯論 · ' + title + '（承前）'
    : '岐伯論 · ' + VOL_PREFIX_TRAD;

  pageElements.push(new Paragraph({
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
  }));

  // 框内顶端大标题（居中，44号加粗）
  const innerElements = [];
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

  // 正文主论单元格
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

  // 极短篇案语札记区 (不足300字篇目)
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

  // 右侧随文批校走廊
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

  // 篇末落款题注栏 + 右侧押角朱砂小印二维码
  if (showFooter) {
    let qrImage = null;
    if (fs.existsSync(qrPngPath)) {
      qrImage = new ImageRun({
        data: fs.readFileSync(qrPngPath),
        transformation: { width: 34, height: 34 }
      });
    }

    const colophonLeft = [
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 30 },
        children: [
          new TextRun({
            text: '〔 專 題 〕 ' + VOL_FULL_TRAD + ' · ' + BOOKLET_STEM + '冊 ' + BOOKLET_TRAD,
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
    ];

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
              children: colophonLeft
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

  // 外层古籍边框
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

// 4. 构建分册扉页与目录页
function buildBookletFrontMatter(articles) {
  const elements = [];

  // --- 册名扉页 (Title Page) ---
  const coverBox = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 1800, after: 300 },
      children: [
        new TextRun({
          text: '岐  伯  論',
          font: FONT_HEADER,
          size: 36,
          color: COLOR_SEAL,
          letterSpacing: 40
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 600 },
      children: [
        new TextRun({
          text: '【 卷  一 】 本 根 敦 倫',
          font: FONT_HEADER,
          size: 26,
          color: '5C544D',
          letterSpacing: 20
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 300 },
      border: {
        bottom: { style: BorderStyle.DOUBLE, size: 12, color: COLOR_BORDER_LINE, space: 12 }
      },
      children: [
        new TextRun({
          text: '甲冊 · 幼兒啟蒙與性情習慣',
          font: FONT_TITLE,
          size: 48,
          bold: true,
          color: '1A1715',
          letterSpacing: 30
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 400, after: 1800 },
      children: [
        new TextRun({
          text: '全冊通收五十二篇 · 研讀批校工作本',
          font: FONT_FOOTER,
          size: 22,
          color: COLOR_MUTED,
          letterSpacing: 15
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 1000, after: 400 },
      children: [
        new TextRun({
          text: '成 傑  手 訂 批 閱',
          font: FONT_NOTE_TITLE,
          size: 22,
          color: '7D756C',
          letterSpacing: 30
        })
      ]
    })
  ];

  const coverTable = new Table({
    width: { size: 9355, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.DOUBLE, size: 16, color: COLOR_BORDER_LINE },
      bottom: { style: BorderStyle.DOUBLE, size: 16, color: COLOR_BORDER_LINE },
      left: { style: BorderStyle.SINGLE, size: 12, color: COLOR_BORDER_LINE },
      right: { style: BorderStyle.SINGLE, size: 12, color: COLOR_BORDER_LINE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 9355, type: WidthType.DXA },
            margins: { top: 300, bottom: 300, left: 300, right: 300 },
            children: coverBox
          })
        ]
      })
    ]
  });
  elements.push(coverTable);
  elements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

  // --- 分册总目录 (Table of Contents) ---
  const tocBox = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 300 },
      border: {
        bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_BORDER_LINE, space: 6 }
      },
      children: [
        new TextRun({
          text: '本 冊 篇 目 總 覽',
          font: FONT_TITLE,
          size: 32,
          bold: true,
          color: '1A1715',
          letterSpacing: 25
        })
      ]
    })
  ];

  const tocRows = [];
  for (let i = 0; i < articles.length; i += 2) {
    const a1 = articles[i];
    const a2 = (i + 1 < articles.length) ? articles[i + 1] : null;

    const cell1Children = [
      new Paragraph({
        spacing: { before: 40, after: 60 },
        children: [
          new TextRun({ text: (i + 1) + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
          new TextRun({ text: '《' + a1.title + '》', font: FONT_BODY, size: 21, bold: true, color: COLOR_INK }),
          new TextRun({ text: ' (' + a1.charCount + '字)', font: FONT_SYSTEM, size: 16, color: COLOR_MUTED })
        ]
      })
    ];

    const cell2Children = a2 ? [
      new Paragraph({
        spacing: { before: 40, after: 60 },
        children: [
          new TextRun({ text: (i + 2) + '. ', font: FONT_HEADER, size: 19, color: COLOR_SEAL }),
          new TextRun({ text: '《' + a2.title + '》', font: FONT_BODY, size: 21, bold: true, color: COLOR_INK }),
          new TextRun({ text: ' (' + a2.charCount + '字)', font: FONT_SYSTEM, size: 16, color: COLOR_MUTED })
        ]
      })
    ] : [];

    tocRows.push(new TableRow({
      children: [
        new TableCell({
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 30, bottom: 30, left: 40, right: 40 },
          children: cell1Children
        }),
        new TableCell({
          width: { size: 4500, type: WidthType.DXA },
          margins: { top: 30, bottom: 30, left: 40, right: 40 },
          children: cell2Children
        })
      ]
    }));
  }

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
    rows: tocRows
  });
  tocBox.push(tocTable);

  const outerTocBorder = new Table({
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
            children: tocBox
          })
        ]
      })
    ]
  });
  elements.push(outerTocBorder);
  elements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

  return elements;
}

console.log('Compiling complete Booklet B01 document elements...');

const b01FullArticles = b01Catalog.map(catEntry => {
  const corpusEntry = corpusMap[catEntry.original_id] || {};
  return {
    ...catEntry,
    text: corpusEntry.text || '',
    url: corpusEntry.url || '',
    charCount: (corpusEntry.text || '').length
  };
});

const docElements = [];

// 前置：扉页与目录
docElements.push(...buildBookletFrontMatter(b01FullArticles));

// 正文 52 篇全部按规制编译
b01FullArticles.forEach((art, artIdx) => {
  const title = art.title;
  const chineseDate = toChineseDate(art.published_at);
  const qrPngPath = path.join(QR_DIR, 'qr_' + art.workbook_ordinal + '.png');

  const allParas = (art.text || '').trim().split(String.fromCharCode(10)).map(p => p.trim()).filter(Boolean);

  // 跨页长文处理
  if (allParas.length > 28) {
    const pPart1 = allParas.slice(0, 26);
    const pPart2 = allParas.slice(26);

    const page1Elements = buildArticlePage({
      title,
      isContinuation: false,
      question: art.question,
      paragraphs: pPart1,
      qrPngPath,
      showFooter: false,
      chineseDate
    });
    docElements.push(...page1Elements);
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));

    const page2Elements = buildArticlePage({
      title,
      isContinuation: true,
      question: null,
      paragraphs: pPart2,
      qrPngPath,
      showFooter: true,
      chineseDate
    });
    docElements.push(...page2Elements);
  } else {
    const pageElements = buildArticlePage({
      title,
      isContinuation: false,
      question: art.question,
      paragraphs: allParas,
      qrPngPath,
      showFooter: true,
      chineseDate
    });
    docElements.push(...pageElements);
  }

  if (artIdx < b01FullArticles.length - 1) {
    docElements.push(new Paragraph({ pageBreakBefore: true, children: [] }));
  }
});

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

const outDocxPath = path.join(OUT_DIR, '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx');
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outDocxPath, buffer);
  console.log('Successfully compiled complete booklet to: ' + outDocxPath + ' (Size: ' + (buffer.length/1024).toFixed(1) + ' KB)');
}).catch(err => {
  console.error('Error generating booklet docx:', err);
  process.exit(1);
});
