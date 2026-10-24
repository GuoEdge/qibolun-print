#!/usr/bin/env node
/**
 * 为37篇新增文章生成二维码
 */

const L = require('./lib_qr_generator.js');
const fs = require('fs');

console.log('=' .repeat(60));
console.log('为37篇新增文章生成二维码');
console.log('=' .repeat(60));

// 读取catalog
const catalog = fs.readFileSync('workbook-40b-all-catalog.jsonl', 'utf-8')
  .split('\n')
  .filter(l => l.trim())
  .map(l => JSON.parse(l));

// 这37篇的ordinal
const ordinals = [4304,4305,4306,4307,4308,4309,4310,4311,4312,4313,4314,4315,4316,4317,4318,4319,4320,4321,4322,4323,4324,4325,4326,4327,4328,4329,4330,4331,4332,4333,4334,4335,4336,4337,4338,4339,4340];

let generated = 0;
let failed = 0;

for (const ord of ordinals) {
  const art = catalog.find(a => a.workbook_ordinal === ord);
  if (art && art.article_url) {
    const qrPath = `../../../qr_cache_all/qr_${art.original_id}.png`;
    try {
      L.generateQr(art.article_url, qrPath);
      generated++;
      console.log(`  ✓ ${art.title} (${art.booklet_code})`);
    } catch (err) {
      failed++;
      console.log(`  ✗ ${art.title}: ${err.message}`);
    }
  } else {
    failed++;
    console.log(`  ✗ ordinal ${ord}: 未找到或URL为空`);
  }
}

console.log('\n' + '='.repeat(60));
console.log(`成功生成: ${generated} 个`);
console.log(`失败: ${failed} 个`);
console.log('='.repeat(60));
