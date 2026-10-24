#!/usr/bin/env node
/**
 * 《岐伯论选》（一百二十篇·权威精编定本）DOCX 排版构建脚本
 * 
 * 核心设计：
 * 1. 封面：使用 lib_wenxuan_cover.js，带“岐伯论选·典藏精编本·成杰嘱命编纂”等专属铭牌与双墨线外框。
 * 2. 扉页与留白：严格遵循成杰定稿规范（物理页控制、正文恒起纸正面）。
 * 3. 前言总序：完整排入《总序：立骨于浊世，求道于近思》，带有独立章节与署名。
 * 4. 目录：分卷细目排布，采用多叶避溢规则。
 * 5. 正文：一百二十篇按卷分编，复用经过数十轮检验的 lib_qibo_layout.js 工作区防断裂双墨线方框与批校栏装箱算法。
 * 6. 后处理管线：自动执行 postprocess_docx.py 修复网格吸附、汉字叶码、对称镜像装订与分节符压段。
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const {
  Document, Packer, Paragraph, TextRun, Footer, PageNumber, AlignmentType, SectionType,
  Table, TableRow, TableCell, WidthType, BorderStyle, HeightRule, VerticalAlign
} = require('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/tools/node/node_modules/docx');

const ROOT = '/storage/Users/currentUser/Documents/岐伯论';
const BASE = path.join(ROOT, 'research-rebuild/reports/gemini-flash-reclassification-v1');
const L = require(path.join(BASE, 'lib_qibo_layout.js'));
const X = require(path.join(BASE, 'extract_qibo_content.js'));
const { buildWenxuanCover } = require('./lib_wenxuan_cover.js');

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

const CORPUS_120 = path.join(ROOT, 'research-rebuild/data/qibo_wenxuan_120_final.jsonl');
const QUESTIONS_MAP = path.join(BASE, 'questions_map.json');
const PREFACE_MD = path.join(ROOT, 'research-rebuild/reports/qibo_wenxuan_preface.md');
const DOCTRINES_MD = path.join(ROOT, 'research-rebuild/reports/qibo_wenxuan_essential_doctrines.md');
const QR_DIR = path.join(BASE, 'qr_cache_all');
const POSTPROCESS = path.join(BASE, 'postprocess_docx.py');
const PY = '/data/service/hnp/bin/python3';

const OUT_DOCX = path.join(ROOT, '岐伯论选·一百二十篇典藏本.docx');

const VOL_TRAD = {
  'V1': { name: '本根敦倫', full: '卷一 · 本根敦倫', label: '本根敦倫 —— 家庭、宗族與倫常之骨架' },
  'V2': { name: '陰陽合離', full: '卷二 · 陰陽合離', label: '卷二 · 陰陽合離 —— 兩性名理與婚戀契約' },
  'V3': { name: '酬酢進退', full: '卷三 · 酬酢進退', label: '卷三 · 酬酢進退 —— 人我邊界與處世防線' },
  'V4': { name: '存神調息', full: '卷四 · 存神調息', label: '卷四 · 存神調息 —— 身心安頓與心性節律' },
  'V5': { name: '度勢居貨', full: '卷五 · 度勢居貨', label: '卷五 · 度勢居貨 —— 職場博弈與資財籌謀' },
  'V6': { name: '觀風察變', full: '卷六 · 觀風察變', label: '卷六 · 觀風察變 —— 時代思潮與世相反思' },
  'V7': { name: '滌除玄覽', full: '卷七 · 滌除玄覽', label: '卷七 · 滌除玄覽 —— 哲學本體與心智模型' },
  'V8': { name: '格物鑄器', full: '卷八 · 格物鑄器', label: '卷八 · 格物鑄器 —— 百工技藝與造物實相' },
};

// 构建核心概念图谱表格（Markdown → docx.Table）
function buildConceptMapTable(lines) {
  // 解析Markdown表格
  const rows = lines
    .filter(l => l.trim().startsWith('|'))
    .map(l => l.split('|').slice(1, -1).map(c => c.trim()));
  
  // 跳过表头分隔行（|------|）
  const dataRows = rows.filter(r => !r[0].startsWith('---'));
  
  // 表格总宽度：页面宽度 - 左右边距
  const pageWidth = 11906; // A4纸宽 (210mm = 11906 twips)
  const margins = 1020 + 1587; // 右边距 + 左边距
  const tableWidth = pageWidth - margins; // 9299 twips
  
  // 4列等宽
  const colWidth = Math.floor(tableWidth / 4);
  
  // 构建docx表格
  const table = new Table({
    width: { size: tableWidth, type: WidthType.DXA },
    columnWidths: [colWidth, colWidth, colWidth, colWidth],
    rows: dataRows.map((rowCells, rowIdx) => {
      return new TableRow({
        height: { value: rowIdx === 0 ? 800 : 1200, rule: HeightRule.AT_LEAST },
        children: rowCells.map((cellText, colIdx) => {
          // 解析单元格内容（加粗、换行）
          const cellRuns = parseCellContent(cellText);
          
          // 表头行样式
          const isHeader = rowIdx === 0;
          const bgColor = isHeader ? '8F2D26' : (rowIdx % 2 === 1 ? 'FFFFFF' : 'F5F5F5');
          const textColor = isHeader ? 'FFFFFF' : '1A1715';
          const fontSize = isHeader ? 22 : 20;
          
          return new TableCell({
            width: { size: colWidth, type: WidthType.DXA },
            shading: { fill: bgColor },
            verticalAlign: VerticalAlign.CENTER,
            margins: {
              top: 150,
              bottom: 150,
              left: 200,
              right: 200
            },
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { line: 320, lineRule: HeightRule.AT_LEAST },
                children: cellRuns.map(run => 
                  new TextRun({
                    text: run.text,
                    font: { ascii: '方正书宋-简', eastAsia: '方正书宋-简' },
                    size: fontSize,
                    bold: run.bold || isHeader,
                    color: textColor
                  })
                )
              })
            ]
          });
        })
      });
    })
  });
  
  return table;
}

// 解析单元格内容（支持 **加粗** 和 <br/> 换行）
function parseCellContent(text) {
  const runs = [];
  
  // 先按<br/>分割
  const lines = text.split('<br/>');
  
  lines.forEach((line, idx) => {
    if (idx > 0) {
      runs.push({ text: '\n', bold: false }); // 换行
    }
    
    // 解析加粗标记
    const parts = line.split(/(\*\*.*?\*\*)/);
    parts.forEach(part => {
      if (!part) return;
      
      if (part.startsWith('**') && part.endsWith('**')) {
        runs.push({ text: part.slice(2, -2), bold: true });
      } else {
        runs.push({ text: part, bold: false });
      }
    });
  });
  
  return runs;
}

function main() {
  console.log('=== 开始构建《岐伯论选》（一百二十篇典藏精编本）===');
  
  // 读取120篇语料
  const articles = fs.readFileSync(CORPUS_120, 'utf8')
    .split('\n')
    .filter(Boolean)
    .map(JSON.parse);
    
  console.log(`已加载语料：${articles.length} 篇`);

  // 加载原问映射
  const questionsMap = JSON.parse(fs.readFileSync(QUESTIONS_MAP, 'utf8'));
  console.log(`已加载原问映射：${Object.keys(questionsMap).length} 条`);

  const frontMatter = [];
  const docElements = [];

  // 1. 封面
  frontMatter.push(buildWenxuanCover());
  // 封面背面空白页（物理隔断）
  frontMatter.push(L.spacerPara(), L.buildBlankPage(), L.spacerPara());

  // 2. 总序（排入前置节）
  console.log('排入出版级总序...');
  const prefaceRaw = fs.readFileSync(PREFACE_MD, 'utf8');
  const prefaceLines = prefaceRaw.split('\n');
  
  // 总序标题
  frontMatter.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 800, after: 600, line: 360, lineRule: 'atLeast' },
    children: [
      new TextRun({
        text: '岐伯論選 · 總序',
        font: { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁' },
        size: 52,
        color: '8F2D26'
      })
    ]
  }));

  // 总序正文（增强代码块支持 + 表格转换）
  let inCodeBlock = false;
  let inTable = false;
  let tableLines = [];
  
  for (const line of prefaceLines) {
    // 检测表格边界
    if (line.trim() === '<table:concept_map>') {
      inTable = true;
      tableLines = [];
      continue;
    }
    if (line.trim() === '</table:concept_map>') {
      inTable = false;
      // 构建docx表格
      const table = buildConceptMapTable(tableLines);
      frontMatter.push(table);
      continue;
    }
    if (inTable) {
      tableLines.push(line);
      continue;
    }
    
    // 检测代码块边界
    if (line.trim().startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      continue; // 跳过```标记本身
    }
    
    const s = line.trim();
    if (!s && !inCodeBlock) continue; // 代码块内保留空行
    
    // 代码块内容：等宽字体、左对齐、无首行缩进
    if (inCodeBlock) {
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 0, line: 280, lineRule: 'exact' },
        children: [
          new TextRun({
            text: line, // 保留原始空格，不trim
            font: { ascii: 'Consolas', eastAsia: '方正等线 Light' },
            size: 18,
            color: '3A3A3A'
          })
        ]
      }));
      continue;
    }
    
    // 标题（改为居中）
    if (s.startsWith('#')) {
      const headingText = s.replace(/^#+\s*/, '');
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 400, after: 200, line: 280, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: headingText,
            font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
            size: 28,
            bold: true,
            color: '1A1715'
          })
        ]
      }));
    } else if (s.startsWith('**岁在丙午') || s.startsWith('**时在二〇')) {
      // 落款（题记字体：汉仪字酷堂会典楷书 W）
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { before: 300, after: 100, line: 240, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: s.replace(/\*\*/g, ''),
            font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
            size: 22,
            color: '8C857B'
          })
        ]
      }));
    } else {
      // 正文（汉仪昌黎宋刻本原版W）
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.BOTH,
        spacing: { before: 60, after: 60, line: 300, lineRule: 'atLeast' },
        indent: { firstLine: 480 },
        children: [
          new TextRun({
            text: s.replace(/\*\*/g, ''),
            font: { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W' },
            size: 21,
            color: '222222'
          })
        ]
      }));
    }
  }

  // 总序后物理分页留白
  frontMatter.push(L.spacerPara(), L.buildBlankPage(), L.spacerPara());

  // 2.5 深度理论专论：岐伯论精要之义（排入前置节）
  console.log('排入万言哲学专论《岐伯论精要之义》...');
  const doctrinesRaw = fs.readFileSync(DOCTRINES_MD, 'utf8');
  const doctrinesLines = doctrinesRaw.split('\n');

  // 精要之义标题
  frontMatter.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 800, after: 400, line: 360, lineRule: 'atLeast' },
    children: [
      new TextRun({
        text: '岐伯論精要之義',
        font: { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁' },
        size: 52,
        color: '8F2D26'
      })
    ]
  }));
  frontMatter.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 600, line: 240, lineRule: 'atLeast' },
    children: [
      new TextRun({
        text: '現代人的立身與心智哲學',
        font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
        size: 32,
        bold: true,
        color: '5C544D'
      })
    ]
  }));

  // 精要之义正文（增强代码块支持）
  let inCodeBlock2 = false;
  for (const line of doctrinesLines) {
    // 检测代码块边界
    if (line.trim().startsWith('```')) {
      inCodeBlock2 = !inCodeBlock2;
      continue;
    }
    
    const s = line.trim();
    if (!s && !inCodeBlock2) continue;
    if (s.startsWith('# ')) continue; // 跳过顶级标题，已单独排版
    
    // 代码块内容：等宽字体、左对齐、无首行缩进
    if (inCodeBlock2) {
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 0, line: 280, lineRule: 'exact' },
        children: [
          new TextRun({
            text: line, // 保留原始空格
            font: { ascii: 'Consolas', eastAsia: '方正等线 Light' },
            size: 18,
            color: '3A3A3A'
          })
        ]
      }));
      continue;
    }
    
    if (s.startsWith('## ')) {
      // 章节标题（改为居中）
      const headingText = s.replace(/^##\s*/, '');
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 500, after: 240, line: 300, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: headingText,
            font: { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁' },
            size: 34,
            bold: true,
            color: '8F2D26'
          })
        ]
      }));
    } else if (s.startsWith('### ')) {
      const subHeading = s.replace(/^###\s*/, '');
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 360, after: 180, line: 260, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: subHeading,
            font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
            size: 26,
            bold: true,
            color: '1A1715'
          })
        ]
      }));
    } else if (s.startsWith('> ')) {
      // 题记引用块（改用汉仪字酷堂会典楷书 W）
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.BOTH,
        spacing: { before: 160, after: 200, line: 280, lineRule: 'atLeast' },
        indent: { left: 480, right: 480 },
        children: [
          new TextRun({
            text: s.replace(/^>\s*/, '').replace(/\*\*/g, ''),
            font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
            size: 20,
            color: '5C544D'
          })
        ]
      }));
    } else if (s.startsWith('**岁在丙午') || s.startsWith('**时在二〇')) {
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { before: 300, after: 100, line: 240, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: s.replace(/\*\*/g, ''),
            font: { ascii: '汉仪字酷堂会典楷书 W', eastAsia: '汉仪字酷堂会典楷书 W' },
            size: 22,
            color: '8C857B'
          })
        ]
      }));
    } else {
      // 正文（改用汉仪昌黎宋刻本原版W）
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.BOTH,
        spacing: { before: 60, after: 60, line: 300, lineRule: 'atLeast' },
        indent: { firstLine: 480 },
        children: [
          new TextRun({
            text: s.replace(/\*\*/g, ''),
            font: { ascii: '汉仪昌黎宋刻本原版W', eastAsia: '汉仪昌黎宋刻本原版W' },
            size: 21,
            color: '222222'
          })
        ]
      }));
    }
  }

  // 精要之义后物理分页留白，使目录起于纸正面
  frontMatter.push(L.spacerPara(), L.buildBlankPage(), L.spacerPara());

  // 3. 全书目录（多叶防溢）
  console.log('生成八卷通览目录...');
  frontMatter.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 600, after: 400, line: 360, lineRule: 'atLeast' },
    children: [
      new TextRun({
        text: '目    錄',
        font: { ascii: '方正爨宝子碑楷书 简繁', eastAsia: '方正爨宝子碑楷书 简繁' },
        size: 48,
        color: '8F2D26'
      })
    ]
  }));

  // 按卷输出目录条目
  let curVol = '';
  for (let idx = 0; idx < articles.length; idx++) {
    const art = articles[idx];
    if (art.volume_code !== curVol) {
      curVol = art.volume_code;
      const vInfo = VOL_TRAD[curVol];
      frontMatter.push(new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 280, after: 140, line: 260, lineRule: 'atLeast' },
        children: [
          new TextRun({
            text: `【 ${vInfo.full} 】`,
            font: { ascii: '汉仪松竹梅 U', eastAsia: '汉仪松竹梅 U' },
            size: 26,
            bold: true,
            color: '8F2D26'
          })
        ]
      }));
    }

    const cnIdx = toCnNum(idx + 1);
    frontMatter.push(new Paragraph({
      alignment: AlignmentType.BOTH,
      spacing: { before: 40, after: 40, line: 240, lineRule: 'atLeast' },
      children: [
        new TextRun({
          text: `第${cnIdx}篇  ${art.title}`,
          font: { ascii: '汉仪韩林朴岩彩 W', eastAsia: '汉仪韩林朴岩彩 W' },
          size: 21,
          color: '222222'
        }),
        new TextRun({
          text: `  ……  ${art.concept_hits ? art.concept_hits.join(' / ') : ''}`,
          font: { ascii: '汉仪永字夏蝉 95W', eastAsia: '汉仪永字夏蝉 95W' },
          size: 18,
          color: '8C857B'
        })
      ]
    }));
  }

  // 目录后确保正文恒起纸正面
  frontMatter.push(L.spacerPara(), L.buildBlankPage(), L.spacerPara());

  // 4. 正文一百二十篇排装
  console.log('开始装箱排入一百二十篇正文...');
  let bodyPageCount = 0;
  
  for (let idx = 0; idx < articles.length; idx++) {
    const art = articles[idx];
    const vInfo = VOL_TRAD[art.volume_code];
    const qrPngPath = path.join(QR_DIR, 'qr_' + art.workbook_ordinal + '.png');
    
    // 语料分段
    const answerParas = (art.answer || '').trim().split('\n').map(s => s.trim()).filter(Boolean);
    const narrativeParas = (art.narrative || '').trim().split('\n').map(s => s.trim()).filter(Boolean);

    const items = [];
    if (narrativeParas.length) {
      items.push({ text: L.LABEL_NARRATIVE, kind: 'narrative-label' });
      for (const np of narrativeParas) items.push({ text: np, kind: 'narrative' });
      items.push({ text: L.MARKER_QIBO, kind: 'marker' });
    }
    for (const ap of answerParas) items.push({ text: ap, kind: 'answer' });

    // 逐叶装箱
    const pages = L.paginateByHeight(items, art.question);
    const ctx = {
      volPrefix: vInfo.name,
      volFull: vInfo.full,
      stem: '選',
      bookletTrad: '精編百二十篇'
    };

    pages.forEach((pg, i) => {
      const isFirst = (i === 0);
      const isLast = (i === pages.length - 1);
      const res = L.buildArticlePage({
        title: art.title,
        isContinuation: !isFirst,
        question: isFirst ? (questionsMap[art.id] || art.question) : null,
        paragraphs: pg.items,
        qrPngPath: fs.existsSync(qrPngPath) ? qrPngPath : null,
        showFooter: isLast,
        chineseDate: L.toChineseDate(art.publishedAt || art.published_at),
        startOfSection: (bodyPageCount === 0)
      }, ctx);

      docElements.push(...res.elements);
      bodyPageCount++;
    });

    if ((idx + 1) % 20 === 0 || idx === articles.length - 1) {
      console.log(`进度：已完成 ${idx + 1} / ${articles.length} 篇 (当前累计 ${bodyPageCount} 叶)`);
    }
  }

  // 5. 封底补页
  if (bodyPageCount % 2 === 1) {
    docElements.push(L.spacerPara(), L.buildBlankPage(), L.spacerPara());
  }

  // 6. 构造 Document 实例
  console.log('创建 DOCX 文档结构...');
  const doc = new Document({
    sections: [
      // 前置节：无页脚/无页码
      {
        properties: {
          type: SectionType.CONTINUOUS,
          page: {
            size: { width: 11906, height: 16838 }, // A4
            margin: { top: 1200, bottom: 1200, left: 1440, right: 1440 }
          }
        },
        children: frontMatter
      },
      // 正文节：自第一叶开始汉字计数叶码
      {
        properties: {
          type: SectionType.NEW_PAGE,
          page: {
            size: { width: 11906, height: 16838 },
            margin: { top: 1200, bottom: 1500, left: 1440, right: 1440, footer: 600 },
            pageNumbers: { start: 1 }
          }
        },
        footers: {
          default: new Footer({
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [
                  new TextRun({
                    children: [PageNumber.CURRENT],
                    font: { ascii: '方正书宋-简', eastAsia: '方正书宋-简' },
                    size: 18,
                    color: '5C544D'
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

  console.log(`正在写入 DOCX：${OUT_DOCX} ...`);
  Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync(OUT_DOCX, buffer);
    console.log(`✓ 原始 DOCX 生成成功，大小: ${(buffer.length / 1024 / 1024).toFixed(2)} MB`);
    
    // 7. 执行 Python 后处理管线
    console.log('执行 Python 深度后处理（清除网格吸附、汉字页码、分节符挤压）...');
    try {
      execFileSync(PY, [POSTPROCESS, OUT_DOCX], { stdio: 'inherit' });
      console.log('✓ 后处理管线执行完毕！');
      console.log(`\n🎉🎉🎉 《岐伯论选》典藏精编本已完美交付！`);
      console.log(`文件路径: ${OUT_DOCX}`);
    } catch (e) {
      console.error('后处理出现警告或非致命错误，请检查:', e.message);
    }
  });
}

main();
