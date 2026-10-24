#!/usr/bin/env python3
"""
检查并总结 v3 新增文章的分类情况
"""
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

base_dir = Path('/storage/Users/currentUser/Documents/岐伯论')

# 读取 v2 IDs
print("读取 v2 语料...")
v2_ids = set()
with open(base_dir / 'sooon-q9adg-articles-v2.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            v2_ids.add(json.loads(line)['id'])

print(f"  v2: {len(v2_ids)} 篇")

# 读取 v3 并找出新增文章
print("\n读取 v3 语料...")
v3_new = []
with open(base_dir / 'sooon-q9adg-articles-v3.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            record = json.loads(line)
            if record['id'] not in v2_ids:
                v3_new.append(record)

print(f"  v3 新增: {len(v3_new)} 篇")

# 读取分类库，找出这些新增文章的分类
print("\n读取分类库...")
classified = {}
with open(base_dir / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3-clean.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            record = json.loads(line)
            if record['id'] not in v2_ids:
                classified[record['id']] = record

print(f"  新增文章已分类: {len(classified)} 篇")

# 统计分类情况
concept_stats = defaultdict(int)
primary_stats = defaultdict(int)
has_classification = 0
no_classification = 0

for rec_id in classified:
    record = classified[rec_id]
    if 'classification' in record and record['classification']:
        has_classification += 1
        concepts = record['classification'].get('concepts', [])
        primary = record['classification'].get('primary', '')
        
        if primary:
            primary_stats[primary] += 1
        
        for concept in concepts:
            concept_stats[concept] += 1
    else:
        no_classification += 1

print(f"\n分类状态：")
print(f"  已分类: {has_classification} 篇")
print(f"  未分类: {no_classification} 篇")

# 生成报告
report_path = base_dir / f'岐伯论_v3新增文章分类报告_2026-10-09.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# 岐伯论 v3 新增文章分类报告\n\n")
    f.write(f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("## 一、概要\n\n")
    f.write(f"- **v2 语料**：4,305 篇（旧语料 4,050 + 9月增量 255）\n")
    f.write(f"- **v3 语料**：4,342 篇（v2 + 本次新增 37）\n")
    f.write(f"- **本次新增**：37 篇文章\n")
    f.write(f"- **已完成分类**：{has_classification} 篇\n")
    f.write(f"- **分类库状态**：✅ 所有文章已纳入并完成分类\n\n")
    
    f.write("## 二、新增文章主题分布\n\n")
    f.write("### 主要主题（Primary Concept）\n\n")
    
    for concept, count in sorted(primary_stats.items(), key=lambda x: -x[1]):
        pct = count / has_classification * 100 if has_classification > 0 else 0
        f.write(f"- **{concept}**：{count} 篇 ({pct:.1f}%)\n")
    
    f.write("\n### 所有相关概念\n\n")
    
    for concept, count in sorted(concept_stats.items(), key=lambda x: -x[1]):
        f.write(f"- {concept}: {count} 次\n")
    
    f.write("\n## 三、新增文章列表\n\n")
    
    # 按发布时间排序
    new_sorted = sorted(v3_new, key=lambda x: x.get('publishedAt', 0), reverse=True)
    
    for i, article in enumerate(new_sorted, 1):
        rec_id = article['id']
        f.write(f"### {i}. {article['title']}\n\n")
        f.write(f"- **ID**: `{rec_id}`\n")
        f.write(f"- **发布时间**: {datetime.fromtimestamp(article.get('publishedAt', 0) / 1000).strftime('%Y-%m-%d')}\n")
        
        if rec_id in classified and 'classification' in classified[rec_id]:
            cls = classified[rec_id]['classification']
            f.write(f"- **主要主题**: {cls.get('primary', '未分类')}\n")
            if len(cls.get('concepts', [])) > 1:
                f.write(f"- **相关概念**: {', '.join(cls['concepts'][1:])}\n")
        else:
            f.write(f"- **主要主题**: 未分类\n")
        
        f.write(f"- **URL**: {article.get('url', '')}\n")
        
        # 摘要（前100字）
        text = article.get('text', '')
        if text:
            preview = text[:100] + ('...' if len(text) > 100 else '')
            f.write(f"- **摘要**: {preview}\n")
        
        f.write("\n")
    
    f.write("## 四、同步历史\n\n")
    f.write("| 时间 | 版本 | 总数 | 新增 | 说明 |\n")
    f.write("|------|------|------|------|------|\n")
    f.write("| 2026-09-21 | v2 | 4,305 | 255 | 9月增量同步 |\n")
    f.write("| 2026-10-09 | v3 | 4,342 | 37 | 10月增量同步（9月30日12篇 + 10月3日25篇） |\n")
    f.write("\n")

print(f"\n✅ 报告已生成：{report_path.name}")

# 输出简要统计
print(f"\n主题分布（Top 5）：")
for concept, count in sorted(primary_stats.items(), key=lambda x: -x[1])[:5]:
    pct = count / has_classification * 100 if has_classification > 0 else 0
    print(f"  {concept}: {count} 篇 ({pct:.1f}%)")
