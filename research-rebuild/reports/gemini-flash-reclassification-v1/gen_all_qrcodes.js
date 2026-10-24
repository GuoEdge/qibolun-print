#!/usr/bin/env node
// 为所有分册生成二维码
const fs = require('fs');
const path = require('path');
const { generateQr } = require('./lib_qr_generator.js');

const BASE = __dirname;
const CATALOG_PATH = path.join(BASE, 'workbook-40b-all-catalog.jsonl');
const QR_CACHE_DIR = path.join(BASE, 'qr_cache_all');

// 确保输出目录存在
if (!fs.existsSync(QR_CACHE_DIR)) {
  fs.mkdirSync(QR_CACHE_DIR, { recursive: true });
}

// 加载catalog
const catalog = [];
for (const line of fs.readFileSync(CATALOG_PATH, 'utf-8').split('\n')) {
  if (!line.trim()) continue;
  catalog.push(JSON.parse(line));
}

console.log(`加载catalog: ${catalog.length} 条记录`);

// 统计URL情况
const withUrl = catalog.filter(rec => rec.article_url && rec.article_url.trim());
console.log(`有URL的记录: ${withUrl.length}/${catalog.length} (${(withUrl.length/catalog.length*100).toFixed(1)}%)`);

// 生成二维码
async function generateAll() {
  let success = 0, skip = 0, error = 0;
  
  for (const rec of catalog) {
    const url = (rec.article_url || '').trim();
    if (!url) {
      skip++;
      continue;
    }
    
    const outPath = path.join(QR_CACHE_DIR, `qr_${rec.workbook_ordinal}.png`);
    
    // 如果文件已存在且非空，跳过
    if (fs.existsSync(outPath)) {
      const stat = fs.statSync(outPath);
      if (stat.size > 0) {
        success++;
        continue;
      }
    }
    
    try {
      await generateQr(outPath, url);
      success++;
      if (success % 100 === 0) {
        console.log(`  已生成 ${success}/${withUrl.length} 个二维码...`);
      }
    } catch (e) {
      console.error(`  生成失败 [${rec.workbook_ordinal}]: ${e.message}`);
      error++;
    }
  }
  
  console.log('\n二维码生成完成！');
  console.log(`  成功: ${success}`);
  console.log(`  跳过: ${skip}`);
  console.log(`  失败: ${error}`);
}

generateAll().catch(e => {
  console.error('致命错误:', e);
  process.exit(1);
});
