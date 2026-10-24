#!/usr/bin/env node
/**
 * 批量生成专题册 DOCX（Node docx 路线）
 * 默认 dry-run：只统计，不写文件。确认后加 --run 才真正生成。
 *
 * 用法：
 *   node build-all-volumes.mjs                 # 统计全部专题册
 *   node build-all-volumes.mjs --only A21,A15  # 只看指定专题
 *   node build-all-volumes.mjs --run --page B5 # 真正生成（B5 版式）
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RESEARCH = path.resolve(HERE, '..', '..');
const PRINT_V2 = path.join(RESEARCH, 'print-20260926-rebuilt-v2');
const OUT_DIR = path.join(RESEARCH, 'wps-sample-20260927', 'docx-output');

const args = { page: 'A5', run: false, only: null, plan: null };
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i], n = () => process.argv[++i];
  if (a === '--run') args.run = true;
  else if (a === '--page') args.page = n();
  else if (a === '--only') args.only = n().split(',');
  else if (a === '--plan') args.plan = n();
}

/** 按平衡方案出册：plan 由 plan-volume-balance.py 生成 */
if (args.plan) {
  const planPath = args.plan.startsWith('/') ? args.plan : path.join(RESEARCH, 'wps-sample-20260927', args.plan);
  const plan = JSON.parse(fs.readFileSync(planPath, 'utf8'));
  const items = args.only ? plan.plan.filter((p) => args.only.includes(p.code)) : plan.plan;
  if (!args.run) {
    console.log(JSON.stringify({
      mode: 'dry-run(plan)', plan: planPath, volumes: items.length,
      pages: { min: Math.min(...plan.plan.map((p) => p.estPages)), max: Math.max(...plan.plan.map((p) => p.estPages)), avg: plan.estPagesAvg },
      preview: items.slice(0, 5),
    }, null, 2));
    console.log('\n实际生成：追加 --run');
    process.exit(0);
  }
  fs.mkdirSync(OUT_DIR, { recursive: true });
  let done = 0;
  for (const p of items) {
    const out = execFileSync('node', [path.join(HERE, 'build-qbl-docx.mjs'),
      '--topic', p.code, '--from', String(p['from']), '--to', String(p.to),
      '--volume-index', String(p.volume), '--volume-count', String(p.volumes),
      '--page', args.page], { encoding: 'utf8' });
    const info = JSON.parse(out.slice(out.indexOf('{')).trim());
    done++;
    console.log(`完成 ${p.dir} 第${p.volume}/${p.volumes}册 -> ${path.basename(info.out)} (${info.bytes} 字节, ${info.articles} 篇, ${info.images} 图)`);
  }
  console.log(JSON.stringify({ generated: done, page: args.page, mode: 'balanced' }, null, 2));
  process.exit(0);
}

const dirs = fs.readdirSync(PRINT_V2)
  .filter((d) => /^(A\d{2}|99)-/.test(d))
  .sort();

const rows = [];
let totalArticles = 0, totalImages = 0, totalImageBytes = 0;

for (const dir of dirs) {
  const code = dir.slice(0, dir.indexOf('-'));
  if (args.only && !args.only.includes(code)) continue;
  const full = path.join(PRINT_V2, dir);
  if (!fs.statSync(full).isDirectory()) continue;
  const volumes = fs.readdirSync(full).filter((f) => /^volume-\d+\.md$/.test(f)).sort();
  for (const v of volumes) {
    const text = fs.readFileSync(path.join(full, v), 'utf8');
    const arts = text.split(/^##\s+/m).slice(1);
    const imgs = [...text.matchAll(/^!\[图\s*\d+\]\((.+)\)$/gm)];
    let bytes = 0;
    for (const m of imgs) {
      const fp = path.resolve(full, m[1]);
      try { bytes += fs.statSync(fp).size; } catch { /* 缺失图片跳过 */ }
    }
    totalArticles += arts.length;
    totalImages += imgs.length;
    totalImageBytes += bytes;
    rows.push({
      code, dir, volume: v, articles: arts.length, images: imgs.length,
      imageMB: +(bytes / 1048576).toFixed(2),
      out: path.join(OUT_DIR, `${dir}-${v.replace('.md', '')}-阅读工作本-Node.docx`),
    });
  }
}

if (!args.run) {
  console.log(JSON.stringify({
    mode: 'dry-run', page: args.page, volumes: rows.length,
    totalArticles, totalImages, totalImageMB: +(totalImageBytes / 1048576).toFixed(1),
    volumesPreview: rows.slice(0, 6),
    tail: rows.slice(-3),
  }, null, 2));
  console.log('\n实际生成：追加 --run（可加 --page B5 / --only A21,A15）');
  process.exit(0);
}

fs.mkdirSync(OUT_DIR, { recursive: true });
const done = [];
for (const r of rows) {
  const vol = Number(r.volume.match(/(\d+)/)[1]);
  const out = execFileSync('node', [path.join(HERE, 'build-qbl-docx.mjs'),
    '--topic', r.code, '--volume', String(vol), '--page', args.page, '--out', r.out], { encoding: 'utf8' });
  const info = JSON.parse(out.slice(out.indexOf('{')).trim());
  done.push(info);
  console.log(`完成 ${r.code} ${r.volume} -> ${path.basename(r.out)} (${info.bytes} 字节, ${info.articles} 篇, ${info.images} 图)`);
}
console.log(JSON.stringify({ generated: done.length, page: args.page }, null, 2));
