#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const QR = require('./research-rebuild/reports/gemini-flash-reclassification-v1/lib_qr_generator.js');

const assignmentPath = './v5_increment_final_assignment.json';
const articles = JSON.parse(fs.readFileSync(assignmentPath, 'utf8'));

const catalogPath = './research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v5.jsonl';
const catalogLines = fs.readFileSync(catalogPath, 'utf8').trim().split('\n').filter(l => l);
const catalog = catalogLines.map(l => JSON.parse(l));

const idToOrdinal = new Map();
catalog.forEach(entry => {
  const id = entry.original_id || entry.article_id;
  if (id && entry.workbook_ordinal) {
    idToOrdinal.set(id, entry.workbook_ordinal);
  }
});

const volumeDirs = {
  'V1': '卷一', 'V2': '卷二', 'V3': '卷三', 'V4': '卷四',
  'V5': '卷五', 'V6': '卷六', 'V7': '卷七', 'V8': '卷八'
};

const bookletDirs = {
  'B04': '丁册',
  'B20A': '甲册',
  'B24': '乙册',
  'B28': '己册',
  'B30': '辛册',
  'B39': '甲册',
  'B40': '乙册'
};

async function main() {
  console.log(`准备为 v5 新增的 ${articles.length} 篇文章生成真实二维码...\n`);
  
  let success = 0, skipped = 0, failed = 0;
  
  for (const art of articles) {
    const ordinal = idToOrdinal.get(art.article_id);
    if (!ordinal) {
      console.log(`⚠ 跳过: ${art.title} (找不到 workbook_ordinal)`);
      skipped++;
      continue;
    }
    
    const volDir = volumeDirs[art.volume_code];
    const bDir = bookletDirs[art.booklet_code];
    if (!volDir || !bDir) {
      console.log(`⚠ 跳过: ${art.title} (无效目录映射)`);
      skipped++;
      continue;
    }
    
    const qrDir = path.join('.', volDir, bDir, '_qr');
    if (!fs.existsSync(qrDir)) {
      fs.mkdirSync(qrDir, { recursive: true });
    }
    
    const qrPath = path.join(qrDir, `qr_${ordinal}.png`);
    
    try {
      await QR.generateQr(qrPath, art.url);
      console.log(`✓ 已生成二维码 [${ordinal}]: ${qrPath} (${art.title} -> ${art.url})`);
      success++;
    } catch (err) {
      console.error(`✗ 失败: ${qrPath} - ${err.message}`);
      failed++;
    }
  }
  
  console.log(`\n二维码生成汇总: 成功 ${success}, 失败 ${failed}`);
}

main().catch(err => {
  console.error('致命错误:', err);
  process.exit(1);
});
