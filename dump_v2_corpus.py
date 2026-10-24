#!/usr/bin/env python3
"""
Full substantive reading and theme alignment review for Volume 2 (阴阳合离)
Reads all 179 articles (Question + Answer + Context) and assesses fit.
"""

import json
from pathlib import Path

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CAT_FILE = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl'
CLEAN_FILE = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'
V4_INC = BASE / 'sooon-q9adg-articles-v4.jsonl'

articles = {}
with open(CLEAN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        item = json.loads(line)
        articles[item['title']] = item

if V4_INC.exists():
    with open(V4_INC, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            if item.get('title') not in articles:
                articles[item['title']] = item

v2_list = []
with open(CAT_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        item = json.loads(line)
        if item.get('volume_code') == 'V2':
            t = item['title']
            art = articles.get(t, {})
            merged = {
                'title': t,
                'booklet_code': item.get('booklet_code'),
                'booklet_name': item.get('booklet_name'),
                'ordinal': item.get('workbook_ordinal'),
                'question': art.get('question') or item.get('question', ''),
                'text': art.get('text') or art.get('answer') or item.get('text_preview', ''),
                'url': item.get('url', ''),
            }
            v2_list.append(merged)

# Dump reading list for thorough offline inspection
with open('v2_full_reading_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(v2_list, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(v2_list)} articles to v2_full_reading_corpus.json")
