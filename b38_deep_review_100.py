#!/usr/bin/env python3
"""
B38辛册深度人工审查 - 前100篇完整阅读
逐篇输出完整内容，人工判断主题契合度
"""

import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
CLEAN_DATA = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'

# 加载数据
articles_by_id = {}
with open(CLEAN_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        articles_by_id[data['id']] = data

booklets = defaultdict(list)
with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        rec = json.loads(line)
        code = rec.get('booklet_code', '')
        base_code = code[:3] if len(code) > 3 else code
        
        if base_code == 'B38':
            booklets[base_code].append(rec)

print("=" * 120)
print("B38 辛册·自處之道與精神獨立 - 前100篇深度审查")
print("主题描述: 探讨独处之道、自我认知、精神独立、内在自足、心理边界、个体自主性")
print(f"总文章数: {len(booklets['B38'])}篇")
print("=" * 120)
print()

articles = booklets['B38'][:100]  # 前100篇

for i, rec in enumerate(articles, 1):
    original_id = rec['original_id']
    article_data = articles_by_id.get(original_id)
    if not article_data:
        continue
    
    title = rec['title']
    ordinal = rec['workbook_ordinal']
    question = article_data.get('question', '')
    answer = article_data.get('answer', '')
    text = answer if answer else article_data.get('text', '')
    
    print(f"\n{'=' * 120}")
    print(f"【第{i}篇】序号#{ordinal} 《{title}》")
    print('=' * 120)
    
    if question:
        print(f"\n【提问】")
        print(question)
    
    print(f"\n【完整回答】")
    print(text)
    
    print(f"\n{'─' * 120}")
