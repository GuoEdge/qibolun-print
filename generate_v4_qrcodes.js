#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const QR = require('./research-rebuild/reports/gemini-flash-reclassification-v1/lib_qr_generator.js');

// 读取 v4 增量分配文件
const assignmentPath = './v4_increment_final_assignment_2026-10-09.jsonl';
const lines = fs.readFileSync(assignmentPath, 'utf8').trim().split('\n').filter(l => l);
const articles = lines.map(l => JSON.parse(l));

// 读取主编目获取 workbook_ordinal
const catalogPath = './research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl';
const catalogLines = fs.readFileSync(catalogPath, 'utf8').trim().split('\n').filter(l => l);
const catalog = catalogLines.map(l => JSON.parse(l));

// 构建 article_id -> workbook_ordinal 映射
const idToOrdinal = new Map();
catalog.forEach(entry => {
  const id = entry.article_id || entry.original_id;
  if (id && entry.workbook_ordinal) {
    idToOrdinal.set(id, entry.workbook_ordinal);
  }
});

// 卷册目录映射
const volumeDirs = {
  'V1': '卷一', 'V2': '卷二', 'V3': '卷三', 'V4': '卷四',
  'V5': '卷五', 'V6': '卷六', 'V7': '卷七', 'V8': '卷八'
};

const bookletNames = {
  'B01': '甲册', 'B03': '丙册', 'B04': '丁册', 'B06': '己册',
  'B12': '乙册', 'B15': '乙册', 'B17': '甲册', 'B18': '乙册', 'B19': '丙册',
  'B20A': '甲册', 'B22': '丙册', 'B23': '甲册', 'B24': '乙册', 'B26': '丁册',
  'B27': '戊册', 'B28': '己册', 'B29': '庚册', 'B30': '辛册',
  'B32': '乙册', 'B34': '丁册', 'B39': '甲册'
};

async function main() {
  console.log(`准备生成 ${articles.length} 个二维码...\n`);
  
  let success = 0, skipped = 0, failed = 0;
  
  for (const art of articles) {
    const ordinal = idToOrdinal.get(art.article_id);
    if (!ordinal) {
      console.log(`⚠ 跳过: ${art.title} (找不到 workbook_ordinal)`);
      skipped++;
      continue;
    }
    
    const volDir = volumeDirs[art.volume_code];
    const bookletDir = bookletNames[art.booklet_code];
    if (!volDir || !bookletDir) {
      console.log(`⚠ 跳过: ${art.title} (无效的卷册代码)`);
      skipped++;
      continue;
    }
    
    const qrDir = path.join('.', volDir, bookletDir, '_qr');
    if (!fs.existsSync(qrDir)) {
      fs.mkdirSync(qrDir, { recursive: true });
    }
    
    const qrPath = path.join(qrDir, `qr_${ordinal}.png`);
    
    if (fs.existsSync(qrPath)) {
      console.log(`✓ 已存在: ${qrPath}`);
      skipped++;
      continue;
    }
    
    try {
      await QR.generateQr(qrPath, art.url);
      console.log(`✓ 已生成: ${qrPath}`);
      success++;
    } catch (err) {
      console.error(`✗ 失败: ${qrPath} - ${err.message}`);
      failed++;
    }
  }
  
  console.log(`\n汇总: 成功 ${success}, 跳过 ${skipped}, 失败 ${failed}`);
}

main().catch(err => {
  console.error('致命错误:', err);
  process.exit(1);
});
