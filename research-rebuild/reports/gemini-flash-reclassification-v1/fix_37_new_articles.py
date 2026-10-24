#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复37篇新增文章（编号4304-4340）的answer字段
从增量数据文件提取text字段
"""

import json
import sys
from pathlib import Path

def main():
    CATALOG = 'workbook-40b-all-catalog.jsonl'
    INCREMENTAL_FILES = [
        '/storage/Users/currentUser/Documents/岐伯论/最新增量文章_2026-09-30.jsonl',
        '/storage/Users/currentUser/Documents/岐伯论/最新增量文章_2026-10-03.jsonl'
    ]
    
    # 加载增量数据
    print('加载增量数据源...')
    incremental = {}
    for fname in INCREMENTAL_FILES:
        if not Path(fname).exists():
            print(f'警告: {fname} 不存在')
            continue
        with open(fname, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    art = json.loads(line)
                    incremental[art['id']] = art
    
    print(f'增量数据: {len(incremental)} 篇\n')
    
    # 备份catalog
    backup = CATALOG + '.bak-before-37-fix'
    Path(backup).write_text(Path(CATALOG).read_text(encoding='utf-8'), encoding='utf-8')
    print(f'已备份: {backup}\n')
    
    # 加载catalog
    print('加载catalog...')
    catalog = []
    with open(CATALOG, encoding='utf-8') as f:
        for line in f:
            if line.strip():
                catalog.append(json.loads(line))
    
    print(f'Catalog: {len(catalog)} 条\n')
    
    # 修复37篇新增文章
    NEW_ORDINALS = list(range(4304, 4341))
    fixed_count = 0
    
    print('修复37篇新增文章:\n')
    for rec in catalog:
        ordinal = rec.get('workbook_ordinal')
        if ordinal not in NEW_ORDINALS:
            continue
        
        orig_id = rec.get('original_id', '')
        if orig_id not in incremental:
            print(f'✗ 编号{ordinal}: original_id={orig_id} 在增量数据中不存在')
            continue
        
        source = incremental[orig_id]
        text = source.get('text', '').strip()
        
        if text:
            rec['answer'] = text
            rec['narrative'] = ''  # 增量数据没有narrative字段
            fixed_count += 1
            text_len = len(text)
            print(f'✓ 编号{ordinal}: {rec["title"]} ({text_len}字符)')
    
    # 保存修复后的catalog
    print(f'\n保存catalog...')
    with open(CATALOG, 'w', encoding='utf-8') as f:
        for rec in catalog:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f'\n完成！共修复 {fixed_count}/37 篇文章')
    return 0 if fixed_count == 37 else 1

if __name__ == '__main__':
    sys.exit(main())
