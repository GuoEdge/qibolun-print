
# -*- coding: utf-8 -*-
import json
import os

catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl'
corpus_v3 = 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3-clean.jsonl'
corpus_v4 = 'sooon-q9adg-articles-v4.jsonl'

# 1. 收集 V3 的所有文章元数据
v3_articles = []
with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        if item.get('volume_code') == 'V3':
            v3_articles.append(item)

print(f'V3总篇数: {len(v3_articles)}')

# 2. 建立 ID 映射加载正文
art_map = {a['original_id']: a for a in v3_articles}

# 从 v3 clean 加载
with open(corpus_v3, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        c = json.loads(line)
        cid = c.get('id') or c.get('original_id')
        if cid in art_map:
            art_map[cid]['content_question'] = c.get('question', '')
            art_map[cid]['content_answer'] = c.get('answer', '')
            art_map[cid]['narrative'] = c.get('narrative', '')
            art_map[cid]['full_text'] = c.get('text', '')

# 从 v4 增量补全
with open(corpus_v4, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        c = json.loads(line)
        cid = c.get('id') or c.get('original_id')
        if cid in art_map and 'full_text' not in art_map[cid]:
            art_map[cid]['content_question'] = c.get('question', '')
            art_map[cid]['content_answer'] = c.get('answer', '')
            art_map[cid]['narrative'] = c.get('narrative', '')
            art_map[cid]['full_text'] = c.get('text', '')

# 验证是否全部加载
for a in v3_articles:
    if 'full_text' not in a or not a['full_text']:
        print(f'警告: {a["title"]} 缺少全文!')

# 保存整理好的完整 V3 数据供深度审查
with open('v3_full_articles_for_audit.json', 'w', encoding='utf-8') as f:
    json.dump(v3_articles, f, ensure_ascii=False, indent=2)

print('已生成 v3_full_articles_for_audit.json')
