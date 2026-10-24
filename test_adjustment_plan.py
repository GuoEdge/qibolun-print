#!/usr/bin/env python3
import json

catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl'
booklet_meta = {}
with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        bc = item.get('booklet_code')
        vc = item.get('volume_code')
        key = f"{vc}-{bc}"
        if key not in booklet_meta:
            booklet_meta[key] = {
                'volume_code': vc,
                'volume_prefix': item.get('volume_prefix'),
                'volume_full_title': item.get('volume_full_title'),
                'booklet_code': bc,
                'booklet_name': item.get('booklet_name'),
                'booklet_stem': item.get('booklet_stem'),
                'booklet_stem_title': item.get('booklet_stem_title'),
                'full_citation': item.get('full_citation')
            }

print(f"Loaded {len(booklet_meta)} unique volume-booklet metadata templates.")
for k in sorted(booklet_meta.keys()):
    print(f"  {k}: {booklet_meta[k]['volume_prefix']} · {booklet_meta[k]['booklet_stem_title']}")
