#!/usr/bin/env python3
"""
卷五（度势居货——职场生态与财富经营）文章内容与主题契合度深度审查脚本
审查方法：全文通读，逐篇实质性判断，不使用关键词匹配法。
"""

import json
from pathlib import Path

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
CLEAN = BASE / 'all-articles-merged-v4-clean.jsonl'
CATALOG = BASE / 'workbook-40b-all-catalog-v4.jsonl'
INC = Path('/storage/Users/currentUser/Documents/岐伯论/research/online-increment/sooon-increment-20261009-195354.jsonl')

# 1. 加载正文语料
articles_map = {}
if CLEAN.exists():
    with open(CLEAN, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            articles_map[item['id']] = item

if INC.exists():
    with open(INC, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            aid = item.get('id') or item.get('article_id')
            if aid and aid not in articles_map:
                articles_map[aid] = item

# 2. 提取卷五编目条目
v5_entries = []
with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        if item.get('volume_code') == 'V5':
            oid = item.get('original_id')
            c = articles_map.get(oid, {})
            text = c.get('text') or c.get('answer') or item.get('text') or ''
            question = item.get('question') or c.get('question') or ''
            
            # 规范化分册代码
            bcode = item.get('booklet_code')
            bname = item.get('booklet_name', '')
            if '上册' in bname: slot = 'B20A'
            elif '中册' in bname: slot = 'B20B'
            elif '下册' in bname: slot = 'B20C'
            elif bcode == 'B21': slot = 'B21'
            elif bcode == 'B22': slot = 'B22'
            elif bcode == 'B20A' or '职场汇报' in bname: slot = 'B20A'
            else: slot = bcode

            v5_entries.append({
                'ordinal': item.get('workbook_ordinal'),
                'id': oid,
                'title': item.get('title'),
                'slot': slot,
                'raw_bcode': bcode,
                'raw_bname': bname,
                'question': question,
                'text': text,
                'url': item.get('url', '')
            })

print(f"Loaded {len(v5_entries)} entries in V5.")

# 将条目导出为按分册组织的精读中间文件，方便逐篇实质性审查
by_slot = {}
for e in v5_entries:
    by_slot.setdefault(e['slot'], []).append(e)

summary = {s: len(lst) for s, lst in sorted(by_slot.items())}
print("Slot breakdown:", summary)

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'w', encoding='utf-8') as f:
    json.dump(v5_entries, f, ensure_ascii=False, indent=2)

print("Exported v5_entries_for_reading.json successfully.")
