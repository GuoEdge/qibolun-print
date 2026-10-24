#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
关联四个数据源，生成全库篇目信号表
输入：
  - sooon-q9adg-articles-v6.jsonl
  - sooon-q9adg-sources.jsonl
  - research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl
  - research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl
输出：
  - research-rebuild/data/all_articles_signals.jsonl（每篇一条，包含所有信号）
"""

import json
import sys
from pathlib import Path

def load_jsonl(path):
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def main():
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    
    # 加载四个数据源
    print("加载 articles-v6...")
    articles = {r['id']: r for r in load_jsonl(base / 'sooon-q9adg-articles-v6.jsonl')}
    
    print("加载 sources...")
    sources = {r['id']: r for r in load_jsonl(base / 'sooon-q9adg-sources.jsonl')}
    
    print("加载 catalog...")
    catalog = {r['original_id']: r for r in load_jsonl(
        base / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
    )}
    
    print("加载 clean...")
    clean = {r['id']: r for r in load_jsonl(
        base / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'
    )}
    
    # 按catalog的4391条记录为主干，关联其他三个表
    merged = []
    missing_in_articles = []
    missing_in_sources = []
    missing_in_clean = []
    
    for cat_id, cat_rec in catalog.items():
        art = articles.get(cat_id)
        src = sources.get(cat_id)
        cln = clean.get(cat_id)
        
        if not art:
            missing_in_articles.append(cat_id)
        if not src:
            missing_in_sources.append(cat_id)
        if not cln:
            missing_in_clean.append(cat_id)
        
        # 合并记录
        record = {
            'id': cat_id,
            'workbook_ordinal': cat_rec.get('workbook_ordinal'),
            'title': cat_rec.get('title'),
            'volume_code': cat_rec.get('volume_code'),
            'booklet_code': cat_rec.get('booklet_code'),
            'booklet_name': cat_rec.get('booklet_name'),
            'text_len': cat_rec.get('text_len'),
            'full_citation': cat_rec.get('full_citation'),
            
            # 从articles取
            'url': art.get('url') if art else None,
            'question': art.get('question') if art else None,
            'brief': art.get('brief') if art else None,
            'publishedAt': art.get('publishedAt') if art else None,
            'updatedAt': art.get('updatedAt') if art else None,
            'has_lexical': bool(art and art.get('lexical')),
            
            # 从sources取
            'planLevel': src.get('planLevel') if src else None,
            'keywords': src.get('keywords') if src else [],
            'collections': src.get('collections') if src else [],
            
            # 从clean取（已分离的answer和narrative）
            'answer_len': len(cln.get('answer', '')) if cln else 0,
            'narrative_len': len(cln.get('narrative', '')) if cln else 0,
        }
        
        merged.append(record)
    
    # 写出
    out_dir = base / 'research-rebuild/data'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'all_articles_signals.jsonl'
    
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in merged:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"\n✓ 已生成 {out_path}")
    print(f"  总计：{len(merged)} 条记录")
    print(f"  缺失情况：")
    print(f"    - articles-v6 中缺失：{len(missing_in_articles)} 条")
    print(f"    - sources 中缺失：{len(missing_in_sources)} 条")
    print(f"    - clean 中缺失：{len(missing_in_clean)} 条")
    
    # 统计分布
    volume_dist = {}
    planLevel_dist = {}
    for rec in merged:
        vol = rec['volume_code']
        volume_dist[vol] = volume_dist.get(vol, 0) + 1
        
        pl = rec['planLevel']
        planLevel_dist[pl] = planLevel_dist.get(pl, 0) + 1
    
    print(f"\n  卷分布：")
    for vol in sorted(volume_dist.keys()):
        print(f"    {vol}: {volume_dist[vol]} 篇")
    
    print(f"\n  planLevel分布：")
    for pl in sorted(planLevel_dist.keys(), key=lambda x: (x is None, x)):
        print(f"    {pl}: {planLevel_dist[pl]} 篇")

if __name__ == '__main__':
    main()
