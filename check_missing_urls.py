#!/usr/bin/env python3
"""检查catalog中缺失URL的文章"""

import json

catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'

missing_urls = []
total = 0

with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        total += 1
        
        url = data.get('article_url', '')
        if not url or url.strip() == '':
            missing_urls.append({
                'title': data.get('title'),
                'booklet_code': data.get('booklet_code'),
                'original_id': data.get('original_id'),
                'workbook_ordinal': data.get('workbook_ordinal')
            })

print(f"总文章数: {total}")
print(f"缺失URL: {len(missing_urls)}")

if missing_urls:
    print("\n缺失URL的文章:")
    for art in missing_urls:
        print(f"  - {art['booklet_code']}/{art['workbook_ordinal']:03d} {art['title']} (ID: {art['original_id']})")
else:
    print("\n✅ 所有文章都有URL")
