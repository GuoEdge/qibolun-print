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
const COLOR_BORDER_LINE = '7A7368';       // 古籍墨线外框
const COLOR_FOOTER      = '808080';       // 篇末题注深灰
const COLOR_PAGE_NUM    = '000000';       // 浓黑叶码

const TRAD_VOL_MAP = {
  'V1': { prefix: '本根敦倫', full: '本根敦倫 —— 血親宗族與家庭撫育' },
  'V2': { prefix: '陰陽合離', full: '陰陽合離 —— 兩性親密與婚戀博弈' },
  'V3': { prefix: '酬酢防身', full: '酬酢防身 —— 熟人世道與處世防線' },
  'V4': { prefix: '存神調息', full: '存神調息 —— 身心安頓與心性知行' },
  'V5': { prefix: '度勢居貨', full: '度勢居貨 —— 職場生態與財富經營' },
  'V6': { prefix: '觀風察變', full: '觀風察變 —— 時代透視與群體思潮' },
  'V7': { prefix: '滌除玄覽', full: '滌除玄覽 —— 深層哲思與名相辨析' },
  'V8': { prefix: '鑑往鑄器', full: '鑑往鑄器 —— 藝文美學與歷史治亂' }
};

const TRAD_BOOKLET_MAP = {
  'B01': '幼兒啟蒙與性情習慣', 'B02': '學業功課與學校日常', 'B03': '言傳身教與獎懲邊界', 'B04': '親子溝通與青春叛逆',
  'B05': '父母控制欲與精神解綁', 'B06': '成年子女自立與邊界', 'B07': '隔代教養與長輩相處', 'B08': '手足同胞與家族親戚',
  'B09': '家族傳承與家風家範', 'B10': '臨終關懷與白事奠儀',
  'B11': '擇偶標準與兩性吸引', 'B12': '婚姻存續與夫妻日常', 'B13': '親密背叛與離異止損',
  'B14': '人情往來與禮數分寸', 'B15': '社交距離與孤立自處', 'B16': '危機識人與權義守界',
  'B17': '情志平復與容貌自和', 'B18': '作息節律與病理常識', 'B19': '知行精進與克服拖延',
  'B20': '職場匯報與權責留痕', 'B21': '體制生存與職業自保', 'B22': '商業競爭與資產投資',
  'B23': '公共熱點與事件剖析', 'B24': '青年心境與躺平反思', 'B25': '網絡生態與群體極化', 'B26': '性別議題與兩性輿論',
  'B27': '教育體制與社會流動', 'B28': '消費主義與生活觀念', 'B29': '現代科技與工具反思', 'B30': '文明演進與社會秩序',
  'B31': '存在本質與生命意義', 'B32': '名相辨析與語言牢籠', 'B33': '善惡分野與倫理底線', 'B34': '認識局限與心智模型',
  'B35': '命途因果與得失隨緣', 'B36': '人性幽微與雙重人格', 'B37': '神聖敬畏與信仰維度', 'B38': '自處之道與精神獨立',
  'B39': '藝能創作與生活美學', 'B40': '治亂興亡與國家工程'
};

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
    volCode,
    bookletCode,
    isContinuation,
    question,
    paragraphs,
    qrPngPath,
    showFooter,
    chineseDate
  } = params;

  const pageElements = [];

  const volData = TRAD_VOL_MAP[volCode] || { prefix: '本根敦倫', full: '本根敦倫 —— 血親宗族與家庭撫育' };
  const bookletTrad = TRAD_BOOKLET_MAP[bookletCode] || '臨終關懷與白事奠儀';

  // 1. 天头题眉（框外居中）
  const headerText = isContinuation
    ? '岐伯論 · ' + title + '（承前）'
    : '岐伯論 · ' + volData.prefix;

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

  // 2. 篇名处理：二维码移至篇末后，篇名在框内顶端完全居中！大字开阔磅礴
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
            size: 44, // 22pt，居中大标题，气象沉稳
            bold: true,
            color: '1A1715',
            letterSpacing: 40
          })
        ]
      })
    );
  }

  // 3. 正文主论与随文批校栅格
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

  // 极短篇案语札记区
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

  // 4. 【核心重构】：篇末落款题注栏 + 右侧压角朱砂小印二维码
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
            text: '〔 專 題 〕 ' + volData.full + ' · ' + bookletTrad,
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

  // 5. 外层古籍边框包裹
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

const docElements = [];

articles.forEach((art, artIdx) => {
  const title = art.title;
  const cat = catalogMap[title] || {};
  const volCode = cat.volume_code || 'V1';
  const bookletCode = cat.booklet_code || 'B10';
  const chineseDate = toChineseDate(art.publishedAt);
  const qrPngPath = path.join(OUT_DIR, 'qr_stamp_' + (
    title === '铺路石' ? 'puluoshi' :
    title === '奠仪几何' ? 'dianyi' :
    title === '何金银' ? 'hejinyin' :
    title === '先辈说' ? 'xianbeishuo' :
    title === '穷关心' ? 'qiongguanxin' : 'wenerhoujie'
  ) + '.png');

  const allParas = (art.text || '').trim().split(String.fromCharCode(10)).map(p => p.trim()).filter(Boolean);

  if (allParas.length > 28) {
    const pPart1 = allParas.slice(0, 26);
    const pPart2 = allParas.slice(26);

    const page1Elements = buildArticlePage({
      title,
      volCode,
      bookletCode,
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
      volCode,
      bookletCode,
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
      volCode,
      bookletCode,
      isContinuation: false,
      question: art.question,
      paragraphs: allParas,
      qrPngPath,
      showFooter: true,
      chineseDate
    });
    docElements.push(...pageElements);
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

Packer.toBuffer(doc).then(buffer => {
  const docxPath = path.join(OUT_DIR, '岐伯论-现代学者批校手卷本-可编辑原型.docx');
  fs.writeFileSync(docxPath, buffer);
  console.log('DOCX with colophon QR seal compiled successfully at:', docxPath);
}).catch(err => {
  console.error('Error generating DOCX:', err);
  process.exit(1);
});
