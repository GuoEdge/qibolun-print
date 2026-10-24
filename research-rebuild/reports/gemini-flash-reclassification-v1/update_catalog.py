#!/usr/bin/env python3
"""
更新catalog文件，将39篇错放文章重新分配到正确的分册
"""
import json

# 读取重新分配计划
with open('relocation_plan.json', 'r', encoding='utf-8') as f:
    relocation_plan = json.load(f)

# 构建article_id -> target_booklet的映射
relocation_map = {}
for item in relocation_plan:
    relocation_map[item['article_id']] = item['target_booklet']

print(f"加载了 {len(relocation_map)} 篇待重新分配文章")

# 读取catalog文件
catalog = []
with open('workbook-40b-all-catalog.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            catalog.append(json.loads(line))

print(f"加载了 {len(catalog)} 条catalog记录")

# 执行重新分配
updated_count = 0
for record in catalog:
    article_id = record.get('original_id')
    if article_id in relocation_map:
        old_booklet = record['booklet_code']
        new_booklet = relocation_map[article_id]
        record['booklet_code'] = new_booklet
        updated_count += 1
        print(f"✓ {record['title']}: {old_booklet} → {new_booklet}")

print(f"\n总计更新了 {updated_count} 篇文章的分册归属")

# 写回catalog文件
with open('workbook-40b-all-catalog-updated.jsonl', 'w', encoding='utf-8') as f:
    for record in catalog:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

print(f"已写入更新后的catalog文件: workbook-40b-all-catalog-updated.jsonl")

# 统计各分册的文章数变化
booklet_stats = {}
for record in catalog:
    booklet = record['booklet_code']
    booklet_stats[booklet] = booklet_stats.get(booklet, 0) + 1

# 找出有变化的分册
affected_booklets = set()
for item in relocation_plan:
    affected_booklets.add(item['from_booklet'])
    affected_booklets.add(item['target_booklet'])

print(f"\n受影响的分册及其文章数：")
for booklet in sorted(affected_booklets):
    count = booklet_stats.get(booklet, 0)
    print(f"  {booklet}: {count} 篇")
