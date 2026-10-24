#!/usr/bin/env python3
"""从增量数据中修复缺失的37条URL"""

import json
import glob
import shutil

# 1. 加载所有增量数据
print("=" * 60)
print("加载增量数据")
print("=" * 60)

increment_data = {}
increment_files = glob.glob('research/online-increment/*.jsonl')

for fpath in increment_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                article_id = data.get('id')
                if article_id:
                    # 保留有URL的记录
                    if data.get('url'):
                        increment_data[article_id] = data
            except:
                continue

print(f"增量数据共 {len(increment_data)} 条记录（有URL）")

# 2. 加载catalog并修复
catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'

print("\n" + "=" * 60)
print("加载catalog并修复缺失URL")
print("=" * 60)

all_records = []
fixed_count = 0
still_missing = []

with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line.strip())
        
        # 如果URL为空，尝试从增量数据修复
        if not record.get('article_url') or record.get('article_url').strip() == '':
            orig_id = record.get('original_id')
            
            if orig_id in increment_data:
                url = increment_data[orig_id].get('url', '').strip()
                if url:
                    record['article_url'] = url
                    record['url'] = url
                    fixed_count += 1
                    print(f"  ✓ 修复: {record.get('title')} -> {url[:60]}...")
                else:
                    still_missing.append(record.get('title'))
            else:
                still_missing.append(record.get('title'))
        
        all_records.append(record)

# 3. 统计并保存
print(f"\n修复统计:")
print(f"  成功修复: {fixed_count} 条")
print(f"  仍然缺失: {len(still_missing)} 条")

if still_missing:
    print("\n仍然缺失URL的文章:")
    for title in still_missing[:10]:
        print(f"    - {title}")
    if len(still_missing) > 10:
        print(f"    ... 还有 {len(still_missing) - 10} 条")

if fixed_count > 0:
    # 备份
    backup_path = catalog_path + '.bak-before-url-fix'
    shutil.copy2(catalog_path, backup_path)
    print(f"\n原文件已备份至: {backup_path}")
    
    # 写入
    with open(catalog_path, 'w', encoding='utf-8') as f:
        for record in all_records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    
    print(f"修复后的数据已写入: {catalog_path}")
    print("\n✅ URL修复完成！")
else:
    print("\n⚠️  没有URL被修复")
