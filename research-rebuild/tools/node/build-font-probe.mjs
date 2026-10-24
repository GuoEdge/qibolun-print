#!/usr/bin/env node
/**
 * 字体样张：把候选字体名各排一行，用于在 WPS 中肉眼确认哪些字体名真正生效。
 * 用途：DOCX 只写字体名，不嵌字体；WPS 找不到该名时会回退到默认字体。
 * 用法：node build-font-probe.mjs [--page A5] [--out path]
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Document, Packer, Paragraph, TextRun, AlignmentType, Header, Footer, PageNumber, BorderStyle } from 'docx';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RESEARCH = path.resolve(HERE, '..', '..');
const OUT_DIR = path.join(RESEARCH, 'wps-sample-20260927', 'docx-output');

const args = { page: 'A5', out: path.join(OUT_DIR, '字体样张-字体名生效验证.docx') };
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i], n = () => process.argv[++i];
  if (a === '--page') args.page = n();
  else if (a === '--out') args.out = n();
  else if (a === '--embed') args.embed = n();   // 格式：字体名|字体文件路径
}

const PRESETS = {
  A5: { width: 8391, height: 11906 },
  B5: { width: 9973, height: 14173 },
  A4: { width: 11906, height: 16838 },
};
const preset = PRESETS[args.page] || PRESETS.A5;
const margin = { top: 1021, right: 992, bottom: 1134, left: 1247, header: 709, footer: 709, gutter: 227 };

const SAMPLE = '岐伯论 · 阅读正文版　体育、运动与竞技伦理　永字八法　ABCabc 0123，。；「」';

/** 候选字体名：Windows/通用名 → 系统真实名 */
const CANDIDATES = [
  { group: 'Windows / 通用名（本机系统字库里通常没有）', names: ['宋体', '黑体', '楷体', '仿宋', '微软雅黑', '思源宋体', '思源黑体'] },
  { group: '鸿蒙系统真实字体名（已解析自 /system/fonts）', names: ['书宋-简', '黑体-简', '楷体-简', '仿宋-简', '方正书宋-简', '方正黑体-简', '方正楷体-简', '方正仿宋-简', '汉仪旗黑 L3', 'Noto Serif CJK SC', 'Noto Sans CJK SC'] },
  { group: '你自己下载的字体（~/Download 与 UURemote）—— 若 WPS 未导入，多半会回退', names: [
    '汉仪昌黎宋刻本原版W', '汉仪方篆 U', '汉仪篆书繁', '汉仪墨意圆 简', '汉仪玉渊洛神行 75U',
    '汉仪永字夏蝉 95W', '汉仪盈光 95U', '汉仪韩林朴岩彩 W', '汉仪国图创新红楼梦 85U',
    '汉仪字酷堂会典楷书 W', '汉仪字酷堂荫嘉楷书 W', '汉仪旗黑X4-55W', '汉仪文润宋韵 U',
    '汉仪黑神话 U', '汉仪像素 13px U',
  ] },
  { group: '其它可能名（用于探测回退）', names: ['Source Han Serif SC', 'HarmonyOS Sans', 'Noto Serif CJK', 'FZShuS-SC', 'HYQiHeiL3'] },
];

const children = [
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 600, after: 200 },
    children: [new TextRun({ text: '字体名生效验证样张', size: 40, bold: true })],
  }),
  new Paragraph({
    spacing: { after: 400 },
    children: [new TextRun({
      text: '说明：每行左侧标注的是写入 DOCX 的字体名。若该字体在 WPS 中不存在，会被回退成默认字体——'
        + '请对比各行字形，凡是字形与「书宋-简 / 黑体-简」两组中任一行完全一致的，说明该名未生效。',
      size: 17, color: '6B6258',
    })],
  }),
];

for (const g of CANDIDATES) {
  children.push(new Paragraph({
    spacing: { before: 320, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'C9B99F', space: 4 } },
    children: [new TextRun({ text: g.group, size: 22, bold: true, color: 'A74736' })],
  }));
  for (const name of g.names) {
    children.push(new Paragraph({
      spacing: { before: 120, after: 60 },
      children: [new TextRun({ text: `${name}　│　`, size: 18, color: '7A6D5E' })],
    }));
    children.push(new Paragraph({
      spacing: { before: 0, after: 160 },
      indent: { left: 480 },
      children: [new TextRun({ text: SAMPLE, size: 24, font: { ascii: name, eastAsia: name, hAnsi: name } })],
    }));
  }
}

children.push(new Paragraph({
  spacing: { before: 400, after: 120 },
  children: [new TextRun({
    text: '确认后请把生效的字体名告诉我，我会把它写进生成器（--font-body / --font-head / --font-meta / --font-seal），全量重出各册。',
    size: 18, color: '6B6258',
  })],
}));

/** 嵌入字体测试：把字体文件写进 fontTable，WPS 即便没装该字体也能显示 */
let embedded = null;
if (args.embed) {
  const [fontName, fontPath] = args.embed.split('|');
  const data = fs.readFileSync(fontPath);
  embedded = { name: fontName, data, bytes: data.length };
  children.unshift(
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 80 },
      children: [new TextRun({
        text: `【嵌入字体测试】${fontName}`, size: 44, bold: true,
        font: { ascii: fontName, eastAsia: fontName, hAnsi: fontName },
      })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 120 },
      children: [new TextRun({ text: SAMPLE, size: 24, font: { ascii: fontName, eastAsia: fontName, hAnsi: fontName } })],
    }),
    new Paragraph({
      spacing: { after: 400 },
      children: [new TextRun({ text: '上面两行使用嵌入字体。若下面同名字体的行与之字形一致，说明嵌入生效；若不一致，说明 WPS 忽略了嵌入字体。', size: 16, color: '6B6258' })],
    }),
  );
}

const doc = new Document({
  title: '字体名生效验证样张',
  creator: '岐伯论编册生成器',
  features: { updateFields: true },
  ...(embedded ? { fonts: [{ name: embedded.name, data: embedded.data }] } : {}),
  sections: [{
    properties: { page: { size: { width: preset.width, height: preset.height }, margin, pageNumbers: { start: 1 } } },
    headers: {
      default: new Header({
        children: [new Paragraph({
          spacing: { after: 0 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'C9B99F', space: 4 } },
          children: [new TextRun({ text: '岐伯论 · 字体样张', size: 17, color: '7A6D5E' })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: '— ', size: 17, color: '7A6D5E' }),
            new TextRun({ children: [PageNumber.CURRENT], size: 17, color: '7A6D5E' }),
            new TextRun({ text: ' —　共 ', size: 17, color: '7A6D5E' }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 17, color: '7A6D5E' }),
            new TextRun({ text: ' 页', size: 17, color: '7A6D5E' }),
          ],
        })],
      }),
    },
    children,
  }],
});

fs.mkdirSync(path.dirname(args.out), { recursive: true });
const buf = await Packer.toBuffer(doc);
fs.writeFileSync(args.out, buf);
console.log(JSON.stringify({ out: args.out, bytes: buf.length, fontNames: CANDIDATES.reduce((n, g) => n + g.names.length, 0) }, null, 2));
