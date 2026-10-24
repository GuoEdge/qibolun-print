// 《岐伯论选》书封完整体系（封面 + 书脊 + 封底）DOCX 设计
// 核心美学：
//  1. 现代典藏画册风格（沉浸图文风） + 原色纯正黑白拓片；
//  2. 包含完整三部件：封面（第1页）、独立书脊设计（第2页）、封底（第3页）；
//  3. 书脊宽度精确模拟 38mm 物理厚度（双对齐标尺，含大字书名、全息实存哲学标、鹏城谨制与底端印章）；
//  4. Word / WPS 原生纯净排版，用户可直接自由增删改查。

const fs = require('fs');
const path = require('path');
const {
  Document, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeightRule, VerticalAlign,
  PageBreak
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const ASSETS_DIR = path.join(ROOT, 'research-rebuild/assets');
const SEAL_PATH = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1/cover-seal.png');
const FULL_MAP_PATH = path.join(ASSETS_DIR, 'star_map_authentic_full.png');
const BACK_MAP_PATH = path.join(ASSETS_DIR, 'star_map_back_clean.png');
const SPINE_STRIP_PATH = path.join(ASSETS_DIR, 'star_map_spine_strip.png');

const OUT_DOCX = path.join(ROOT, '岐伯论选·封面与封底设计.docx');

// 字体体系
const FONT_HUIDIAN  = { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' };
const FONT_CHANGLI  = { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W' };
const FONT_XIACHAN  = { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W' };
const FONT_LIQI     = { ascii: '方正礼器碑隶书 简繁', eastAsia: '方正礼器碑隶书 简繁' };

// 色彩设计
const COLOR_MAIN    = '181615'; // 沉着玄黑
const COLOR_RED     = 'A83226'; // 点睛朱砂
const COLOR_GRAY    = '59544E'; // 宿墨深灰
const COLOR_MUTED   = '8C857B'; // 优雅淡墨
const COLOR_LINE    = 'D4CFCA'; // 极淡辅助线
const COLOR_SPINE_BG= 'FAF8F5'; // 书脊微纸白

function createFullBookJacketDoc() {
  console.log('正在构建包含【封面 + 书脊 + 封底】的完整书封 DOCX...');

  const sealImg = fs.readFileSync(SEAL_PATH);
  const fullMapImg = fs.readFileSync(FULL_MAP_PATH);
  const backMapImg = fs.readFileSync(BACK_MAP_PATH);
  const spineStripImg = fs.readFileSync(SPINE_STRIP_PATH);

  // ===========================================================================
  // 第 1 页：封面（COVER）
  // ===========================================================================
  const coverElements = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 360, line: 260, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '全 息 實 存 哲 學  ·  一 百 二 十 篇 定 本',
          font: FONT_XIACHAN,
          size: 22,
          color: COLOR_MUTED
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 480 },
      children: [
        new ImageRun({
          data: fullMapImg,
          transformation: { width: 490, height: 218 },
          type: 'png'
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 420 },
      children: [
        new TextRun({
          text: '————————  ·  ————————',
          font: FONT_CHANGLI,
          size: 18,
          color: COLOR_LINE
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 200, line: 560, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '岐  伯  論  選',
          font: FONT_HUIDIAN,
          size: 116,
          bold: true,
          color: COLOR_MAIN
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 440, line: 280, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '〔 典 藏 精 編 本 〕',
          font: FONT_CHANGLI,
          size: 28,
          bold: true,
          color: COLOR_RED
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 180, after: 140, line: 360, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '立 骨 於 濁 世    求 道 於 近 思',
          font: FONT_XIACHAN,
          size: 38,
          color: COLOR_GRAY
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 420, line: 260, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '五十五冊宏帙四千三百餘篇精裁  ·  現代人的立身與心智哲學',
          font: FONT_CHANGLI,
          size: 22,
          color: COLOR_MUTED
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 180, line: 240, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '歲在丙午金秋  成杰囑命編纂  ·  鵬城謹製',
          font: FONT_LIQI,
          size: 22,
          color: COLOR_GRAY
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 0 },
      children: [
        new ImageRun({
          data: sealImg,
          transformation: { width: 44, height: 44 },
          type: 'png'
        })
      ]
    })
  ];

  // ===========================================================================
  // 第 2 页：独立书脊（SPINE DESIGN）
  // 结构说明：
  //   以居中 38mm 实体比例单列立式表格排版（宽 2154 twips ≈ 38mm，高铺满版心）
  //   左侧与右侧标尺留白，完全符合实际装订包装裁切规范！
  // ===========================================================================
  const spineElements = [
    // 顶部装订说明（非印刷说明）
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 200 },
      children: [
        new TextRun({
          text: '【 書 脊 設 計 規 模 】  厚度測算：38 mm (對應 420 頁雙面典藏本)  ·  可直接打印或裁切套版',
          font: FONT_CHANGLI,
          size: 18,
          color: COLOR_MUTED
        })
      ]
    }),

    // 居中立式书脊条框
    new Table({
      alignment: AlignmentType.CENTER,
      width: { size: 2200, type: WidthType.DXA }, // 约 38.8 mm
      borders: {
        top: { style: BorderStyle.SINGLE, size: 6, color: COLOR_LINE },
        bottom: { style: BorderStyle.SINGLE, size: 6, color: COLOR_LINE },
        left: { style: BorderStyle.DASHED, size: 4, color: COLOR_LINE },
        right: { style: BorderStyle.DASHED, size: 4, color: COLOR_LINE }
      },
      rows: [
        new TableRow({
          height: { value: 14000, rule: HeightRule.AT_LEAST },
          children: [
            new TableCell({
              width: { size: 2200, type: WidthType.DXA },
              shading: { fill: COLOR_SPINE_BG },
              margins: { top: 200, bottom: 200, left: 60, right: 60 },
              verticalAlign: VerticalAlign.CENTER,
              children: [
                // 书脊顶端古典朱红装订线
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 60, after: 120 },
                  children: [
                    new TextRun({
                      text: '—————',
                      font: FONT_CHANGLI,
                      size: 20,
                      color: COLOR_RED
                    })
                  ]
                }),

                // 书脊天头星宿拓片切条
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 320 },
                  children: [
                    new ImageRun({
                      data: spineStripImg,
                      transformation: { width: 34, height: 110 },
                      type: 'png'
                    })
                  ]
                }),

                // 书脊主书名（纵排大字：汉仪字酷堂会典楷书 W）
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 100, line: 360, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '岐', font: FONT_HUIDIAN, size: 64, bold: true, color: COLOR_MAIN })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 100, line: 360, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '伯', font: FONT_HUIDIAN, size: 64, bold: true, color: COLOR_MAIN })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 100, line: 360, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '論', font: FONT_HUIDIAN, size: 64, bold: true, color: COLOR_MAIN })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 480, line: 360, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '選', font: FONT_HUIDIAN, size: 64, bold: true, color: COLOR_MAIN })]
                }),

                // 书脊篇卷标（朱红竖列）
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 260, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '一', font: FONT_XIACHAN, size: 26, color: COLOR_RED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 260, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '百', font: FONT_XIACHAN, size: 26, color: COLOR_RED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 260, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '二', font: FONT_XIACHAN, size: 26, color: COLOR_RED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 260, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '十', font: FONT_XIACHAN, size: 26, color: COLOR_RED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 520, line: 260, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '篇', font: FONT_XIACHAN, size: 26, color: COLOR_RED })]
                }),

                // 学术定性：实存哲学
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 240, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '實', font: FONT_CHANGLI, size: 22, color: COLOR_MUTED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 240, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '存', font: FONT_CHANGLI, size: 22, color: COLOR_MUTED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 60, line: 240, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '哲', font: FONT_CHANGLI, size: 22, color: COLOR_MUTED })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 600, line: 240, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '學', font: FONT_CHANGLI, size: 22, color: COLOR_MUTED })]
                }),

                // 底部出版标：鹏城谨制
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 50, line: 220, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '鵬', font: FONT_CHANGLI, size: 20, color: COLOR_GRAY })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 50, line: 220, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '城', font: FONT_CHANGLI, size: 20, color: COLOR_GRAY })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 50, line: 220, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '謹', font: FONT_CHANGLI, size: 20, color: COLOR_GRAY })]
                }),
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 180, line: 220, lineRule: 'atLeast' },
                  children: [new TextRun({ text: '製', font: FONT_CHANGLI, size: 20, color: COLOR_GRAY })]
                }),

                // 书脊底端印章（小印款）
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 100 },
                  children: [
                    new ImageRun({
                      data: sealImg,
                      transformation: { width: 32, height: 32 },
                      type: 'png'
                    })
                  ]
                }),

                // 底端朱红横线
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 0, after: 40 },
                  children: [
                    new TextRun({
                      text: '—————',
                      font: FONT_CHANGLI,
                      size: 20,
                      color: COLOR_RED
                    })
                  ]
                })
              ]
            })
          ]
        })
      ]
    })
  ];

  // ===========================================================================
  // 第 3 页：封底（BACK COVER）
  // ===========================================================================
  const backElements = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 180, after: 260 },
      children: [
        new ImageRun({
          data: backMapImg,
          transformation: { width: 460, height: 160 },
          type: 'png'
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 60, after: 160, line: 300, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '八  卷  全  息  架  構  考',
          font: FONT_HUIDIAN,
          size: 34,
          bold: true,
          color: COLOR_RED
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 260 },
      children: [
        new TextRun({
          text: '——————————————————————————',
          font: FONT_CHANGLI,
          size: 16,
          color: COLOR_LINE
        })
      ]
    }),
    new Table({
      alignment: AlignmentType.CENTER,
      width: { size: 8800, type: WidthType.DXA },
      columnWidths: [4400, 4400],
      borders: {
        top: { style: BorderStyle.NONE, size: 0 },
        bottom: { style: BorderStyle.NONE, size: 0 },
        left: { style: BorderStyle.NONE, size: 0 },
        right: { style: BorderStyle.NONE, size: 0 },
        insideHorizontal: { style: BorderStyle.DOTTED, size: 4, color: 'E2DED9' },
        insideVertical: { style: BorderStyle.NONE, size: 0 }
      },
      rows: [
        new TableRow({
          height: { value: 720, rule: HeightRule.AT_LEAST },
          children: [
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷一 · 本根敦倫 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十八篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '家庭宗族邊界與代際權柄契約', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            }),
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷五 · 度勢居貨 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十二篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '職場博弈、面向紀要與資財籌謀', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            })
          ]
        }),
        new TableRow({
          height: { value: 720, rule: HeightRule.AT_LEAST },
          children: [
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷二 · 陰陽合離 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '兩性本質、婚戀契約與淨輸出', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            }),
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷六 · 觀風察變 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十六篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '時代思潮、消費主義與世相反思', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            })
          ]
        }),
        new TableRow({
          height: { value: 720, rule: HeightRule.AT_LEAST },
          children: [
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷三 · 酬酢進退 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十五篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '人我邊界、SOP規矩與應世防身', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            }),
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷七 · 滌除玄覽 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(三十四篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '本體哲學、心智模型與玄覽極境', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            })
          ]
        }),
        new TableRow({
          height: { value: 720, rule: HeightRule.AT_LEAST },
          children: [
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷四 · 存神調息 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(十篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '身心安頓、行動單元與生理節律', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            }),
            new TableCell({
              width: { size: 4400, type: WidthType.DXA },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({ text: '卷八 · 格物鑄器 ', font: FONT_XIACHAN, size: 24, bold: true, color: COLOR_MAIN }),
                    new TextRun({ text: '(五篇)\n', font: FONT_CHANGLI, size: 20, color: COLOR_RED }),
                    new TextRun({ text: '百工技藝、功夫底層與造物實相', font: FONT_CHANGLI, size: 20, color: COLOR_MUTED })
                  ]
                })
              ]
            })
          ]
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 320, after: 70, line: 280, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '「 世間無抽象孤立之是非，唯有誰在此事中擁有權責邊界之實存。」',
          font: FONT_CHANGLI,
          size: 22,
          color: COLOR_GRAY
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 70, line: 280, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '「 倫理其實是一件武器，為人的行為設立強硬之軌道。」',
          font: FONT_CHANGLI,
          size: 22,
          color: COLOR_GRAY
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 320, line: 280, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '「 收回對自身之評價權，心性如金剛，不毀不損。」',
          font: FONT_CHANGLI,
          size: 22,
          color: COLOR_GRAY
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 50, line: 220, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '《岐伯論選》· 一百二十篇典藏精編本',
          font: FONT_HUIDIAN,
          size: 24,
          color: COLOR_MAIN
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 50, line: 200, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: '內部學術典藏 · 非賣品 · 二〇二六年十月',
          font: FONT_CHANGLI,
          size: 19,
          color: COLOR_MUTED
        })
      ]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 0, line: 220, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: 'ISBN 978-7-98026-120-8',
          font: FONT_XIACHAN,
          size: 22,
          color: COLOR_GRAY
        })
      ]
    })
  ];

  // 组装文档为 3 页（封面 -> 书脊 -> 封底）
  const doc = new Document({
    sections: [
      {
        properties: {
          page: {
            size: { width: 11906, height: 16838 }, // A4 竖版
            margin: { top: 900, right: 1080, bottom: 900, left: 1080 }
          }
        },
        children: [
          ...coverElements,
          new Paragraph({ children: [new PageBreak()] }),
          ...spineElements,
          new Paragraph({ children: [new PageBreak()] }),
          ...backElements
        ]
      }
    ]
  });

  return doc;
}

// 写入生成
const doc = createFullBookJacketDoc();
const Packer = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx').Packer;

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(OUT_DOCX, buffer);
  console.log(`✓ 包含完整【封面 + 书脊 + 封底】DOCX 文件生成成功！大小: ${(buffer.length / 1024).toFixed(1)} KB`);
  console.log(`文件路径: ${OUT_DOCX}`);
}).catch(err => {
  console.error('生成失败:', err);
});
