#!/usr/bin/env python3
"""检查B39数据完整性并尝试从原始数据恢复"""

import json

# 1. 检查catalog中B39的数据情况
catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
original_path = 'sooon-q9adg-articles-v2.jsonl'

print("=" * 60)
print("检查 workbook-40b-all-catalog.jsonl 中的 B39 数据")
print("=" * 60)

b39_articles = []
with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        if data.get('booklet_code') == 'B39':
            b39_articles.append(data)

print(f"\nB39共有 {len(b39_articles)} 篇文章")

# 检查字段完整性
empty_answer = 0
empty_narrative = 0
has_text = 0

for art in b39_articles:
    if not art.get('answer'):
        empty_answer += 1
    if not art.get('narrative'):
        empty_narrative += 1
    if art.get('text'):
        has_text += 1

print(f"- answer字段为空: {empty_answer} 篇")
print(f"- narrative字段为空: {empty_narrative} 篇")
print(f"- text字段有内容: {has_text} 篇")

# 2. 建立原始数据索引
print("\n" + "=" * 60)
print("建立原始数据索引")
print("=" * 60)

original_data = {}
with open(original_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        article_id = data.get('id')
        if article_id:
            original_data[article_id] = data

print(f"原始数据共 {len(original_data)} 条记录")

# 3. 尝试匹配并检查
print("\n" + "=" * 60)
print("匹配检查")
print("=" * 60)

matched = 0
not_matched = 0
original_has_answer = 0

for art in b39_articles:
    orig_id = art.get('original_id')
    if orig_id in original_data:
        matched += 1
        orig = original_data[orig_id]
        if orig.get('answer'):
            original_has_answer += 1
    else:
        not_matched += 1
        print(f"  未匹配: {art.get('title')} (ID: {orig_id})")

print(f"\n匹配成功: {matched} 篇")
print(f"匹配失败: {not_matched} 篇")
print(f"原始数据中有answer字段: {original_has_answer} 篇")

# 4. 抽样显示
if b39_articles:
    print("\n" + "=" * 60)
    print("抽样显示 (前3篇)")
    print("=" * 60)
    
    for i, art in enumerate(b39_articles[:3], 1):
        print(f"\n第{i}篇: {art.get('title')}")
        print(f"  original_id: {art.get('original_id')}")
        print(f"  text长度: {len(art.get('text', ''))}")
        print(f"  answer长度: {len(art.get('answer', ''))}")
        print(f"  narrative长度: {len(art.get('narrative', ''))}")
        
        orig_id = art.get('original_id')
        if orig_id in original_data:
            orig = original_data[orig_id]
            print(f"  原始answer长度: {len(orig.get('answer', ''))}")
            print(f"  原始text长度: {len(orig.get('text', ''))}")
            if 'lexical' in orig:
                print(f"  原始有lexical字段")
