#!/usr/bin/env python3
"""为 v4 新增 29 篇文章预生成二维码"""
import json
import qrcode
from pathlib import Path

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
CATALOG = BASE / 'workbook-40b-all-catalog.jsonl'
QR_DIR = BASE / 'qr_cache_all'
QR_DIR.mkdir(exist_ok=True)

# 读取 catalog，筛选 ordinal >= 4341 的新增文章
with open(CATALOG, 'r', encoding='utf-8') as f:
    records = [json.loads(line) for line in f if line.strip()]

new_articles = [r for r in records if r['workbook_ordinal'] >= 4341]
print(f'找到 {len(new_articles)} 篇新增文章（ordinal 4341-4369）')

generated = 0
skipped = 0

for rec in new_articles:
    ordinal = rec['workbook_ordinal']
    qr_path = QR_DIR / f'qr_{ordinal}.png'
    
    if qr_path.exists():
        skipped += 1
        continue
    
    # 优先使用 url 字段，其次 article_url，最后拼接 original_id
    url = rec.get('url') or rec.get('article_url') or f"https://www.zhihu.com/question/{rec.get('original_id', rec['id'])}"
    
    # 生成二维码
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(str(qr_path))
    
    generated += 1
    if generated % 5 == 0:
        print(f'  已生成 {generated}/{len(new_articles)}...')

print(f'\n✓ 二维码生成完成')
print(f'  新生成: {generated} 个')
print(f'  已存在: {skipped} 个')
print(f'  总计: {generated + skipped} 个')
