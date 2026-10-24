#!/usr/bin/env node
/** DOCX 校验：部件完整性、XML 合法性、页码域、页眉页脚、样式、图片、文本内容抽样 */
import fs from 'node:fs';
import path from 'node:path';
import JSZip from 'jszip';
import { DOMParser } from '@xmldom/xmldom';
import mammoth from 'mammoth';

const file = process.argv[2];
if (!file) { console.error('用法：node verify-docx.mjs <file.docx>'); process.exit(1); }

const buf = fs.readFileSync(file);
const zip = await JSZip.loadAsync(buf);
const names = Object.keys(zip.files).sort();

const W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main';
let xmlOk = 0, xmlBad = [];
const texts = {};
for (const n of names) {
  if (!n.endsWith('.xml') && !n.endsWith('.rels')) continue;
  const s = await zip.files[n].async('string');
  try {
    new DOMParser({ onError: () => { throw new Error('parse'); } }).parseFromString(s, 'text/xml');
    xmlOk++;
  } catch (e) { xmlBad.push(n); }
  texts[n] = s;
}

const doc = texts['word/document.xml'] || '';
const count = (re, s = doc) => (s.match(re) || []).length;
const styles = texts['word/styles.xml'] || '';
const headers = names.filter((n) => /word\/header\d*\.xml/.test(n));
const footers = names.filter((n) => /word\/footer\d*\.xml/.test(n));
const media = names.filter((n) => n.startsWith('word/media/') && !n.endsWith('/'));
const rels = texts['word/_rels/document.xml.rels'] || '';

const footerText = await Promise.all(footers.map((n) => zip.files[n].async('string')));
const footerStr = footerText.join('');
const headerText = await Promise.all(headers.map((n) => zip.files[n].async('string')));
const headerStr = headerText.join('');

const html = await mammoth.convertToHtml({ buffer: buf });
const text = html.value.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');

const report = {
  file: path.basename(file),
  bytes: buf.length,
  parts: names.length,
  xmlOk,
  xmlBad,
  hasDocument: !!doc,
  hasStyles: !!styles,
  qblStyles: (styles.match(/w:styleId="QBL[A-Za-z]+"/g) || []).length,
  paragraphs: count(/<w:p[ >]/g),
  pageBreaks: count(/w:type="page"/g),
  pageNumberFields: {
    PAGE: count(/PAGE/g, doc + headerStr + footerStr),
    NUMPAGES: count(/NUMPAGES/g, doc + headerStr + footerStr),
  },
  headers: headers.length,
  footers: footers.length,
  footerHasPageField: /PAGE/.test(footerStr),
  headerSample: (headerStr.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 120)),
  media: media.length,
  imageDrawings: count(/<w:drawing/g),
  mediaList: media.slice(0, 8),
  hyperlinks: count(/<w:hyperlink/g),
  sectPr: count(/<w:sectPr/g),
  textChars: text.length,
  textHead: text.slice(0, 240),
  hasTOCMarker: /目录/.test(text),
  hasIndexMarker: /索引/.test(text),
  hasSeal: /岐\s*伯\s*论/.test(text),
};
console.log(JSON.stringify(report, null, 2));
