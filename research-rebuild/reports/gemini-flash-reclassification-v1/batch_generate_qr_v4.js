#!/usr/bin/env node
// 为 v4 新增 29 篇文章批量预生成二维码
const fs = require('fs');
const path = require('path');
const QR = require('./lib_qr_generator.js');

const BASE = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1';
const CATALOG = path.join(BASE, 'workbook-40b-all-catalog.jsonl');
const QR_DIR = path.join(BASE, 'qr_cache_all');

if (!fs.existsSync(QR_DIR)) fs.mkdirSync(QR_DIR, { recursive: true });

const records = fs.readFileSync(CATALOG, 'utf8')
  .split('\n')
  .filter(Boolean)
  .map(JSON.parse);

const newArticles = records.filter(r => r.workbook_ordinal >= 4341);
console.log(`找到 ${newArticles.length} 篇新增文章（ordinal 4341-4369）`);

let generated = 0;
let skipped = 0;
let failed = [];

(async () => {
  for (const rec of newArticles) {
    const ordinal = rec.workbook_ordinal;
    const qrPath = path.join(QR_DIR, `qr_${ordinal}.png`);
    
    if (fs.existsSync(qrPath)) {
      skipped++;
      continue;
    }
    
    const url = rec.url || rec.article_url || `https://www.zhihu.com/question/${rec.original_id || rec.id}`;
    
    try {
      await QR.generateQr(qrPath, url);
      generated++;
      if (generated % 5 === 0) {
        console.log(`  已生成 ${generated}/${newArticles.length}...`);
      }
    } catch (err) {
      failed.push({ ordinal, url, error: err.message });
      console.error(`✗ 生成失败 qr_${ordinal}.png: ${err.message}`);
    }
  }
  
  console.log(`\n✓ 二维码生成完成`);
  console.log(`  新生成: ${generated} 个`);
  console.log(`  已存在: ${skipped} 个`);
  console.log(`  失败: ${failed.length} 个`);
  console.log(`  总计: ${generated + skipped} 个`);
  
  if (failed.length > 0) {
    console.log(`\n失败记录:`);
    failed.forEach(f => console.log(`  - ordinal ${f.ordinal}: ${f.error}`));
    process.exit(1);
  }
})();
