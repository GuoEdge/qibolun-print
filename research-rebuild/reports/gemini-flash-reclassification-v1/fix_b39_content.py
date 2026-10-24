#!/usr/bin/env python3
"""修复B39文章的正文数据"""

import json
import shutil
from datetime import datetime

CATALOG = 'workbook-40b-all-catalog.jsonl'
SOURCE = '/storage/Users/currentUser/Documents/岐伯论/sooon-q9adg-articles-v2.jsonl'

# 备份
backup = f'{CATALOG}.bak-before-b39-fix'
shutil.copy(CATALOG, backup)
print(f'已备份: {backup}')

# 加载原始数据源
print('加载原始数据源...')
source_data = {}
with open(SOURCE, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            art = json.loads(line)
            source_data[art['id']] = art

print(f'原始数据源: {len(source_data)} 篇')

# 修复catalog
print('\n修复catalog中B39的正文数据...')
catalog = []
fixed_count = 0

with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        
        rec = json.loads(line)
        
        # 如果是B39的文章且缺失正文
        if rec['booklet_code'] == 'B39' and not rec.get('answer', '').strip():
            orig_id = rec['original_id']
            
            if orig_id in source_data:
                source = source_data[orig_id]
                
                # 从原始数据恢复正文字段
                rec['text'] = source.get('text', '')
                rec['answer'] = source.get('answer', '')
                rec['narrative'] = source.get('narrative', '')
                
                fixed_count += 1
                print(f'  修复: 编号{rec["workbook_ordinal"]:4d} | {rec["title"][:30]}')
        
        catalog.append(rec)

# 保存修复后的catalog
print(f'\n保存修复后的catalog...')
with open(CATALOG, 'w', encoding='utf-8') as f:
    for rec in catalog:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'\n完成！已修复 {fixed_count} 篇文章的正文数据')
