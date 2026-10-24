#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
汇总前300篇分析结果，生成候选池清单
"""

import json
from pathlib import Path

def load_batch_results(batch_file):
    """加载批次文件并重新评分"""
    with open(batch_file, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f if line.strip()]
    
    results = []
    for rec in articles:
        answer_len = len(rec['answer'])
        concept_hits = rec.get('concept_hits', [])
        plan_level = rec.get('planLevel')
        
        score = 0
        if concept_hits:
            score += 100 + len(concept_hits) * 10
        if plan_level == 3:
            score += 50
        elif plan_level == 2:
            score += 30
        if answer_len >= 2000:
            score += 20
        elif answer_len >= 1000:
            score += 10
        elif answer_len < 500:
            score -= 20
        
        answer = rec['answer']
        method_keywords = ['怎么', '如何', '方法', '策略', '步骤', '原则', '标准', '判断', '选择', '规则', '框架']
        if sum(1 for kw in method_keywords if kw in answer) >= 3:
            score += 15
        
        originality_markers = ['其实', '实则', '要害', '问题不在', '真正的', '关键', '本质', '看似', '实际', '表面', '根本', '核心', '往往', '总是']
        if sum(1 for m in originality_markers if answer.count(m) >= 2) >= 5:
            score += 15
        
        if score >= 160:
            rating = "★★★★★"
        elif score >= 140:
            rating = "★★★★☆"
        elif score >= 120:
            rating = "★★★☆☆"
        elif score >= 100:
            rating = "★★☆☆☆"
        else:
            rating = "★☆☆☆☆"
        
        results.append({
            'id': rec['id'],
            'citation': rec['full_citation'],
            'title': rec['title'],
            'concept_hits': concept_hits,
            'planLevel': plan_level,
            'answer_len': answer_len,
            'score': score,
            'rating': rating,
        })
    
    return results

def main():
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    
    print("加载批次1 (1-100)...")
    batch1 = load_batch_results(base / 'research-rebuild/data/high_signal_content/batch_0001_0100.jsonl')
    
    print("加载批次2 (101-300)...")
    batch2 = load_batch_results(base / 'research-rebuild/data/high_signal_content/batch_0101_0300.jsonl')
    
    all_results = batch1 + batch2
    all_results.sort(key=lambda x: -x['score'])
    
    # 统计评级分布
    rating_dist = {}
    for r in all_results:
        rating_dist[r['rating']] = rating_dist.get(r['rating'], 0) + 1
    
    print(f"\n前300篇评级统计：")
    print(f"  ★★★★★：{rating_dist.get('★★★★★', 0)} 篇")
    print(f"  ★★★★☆：{rating_dist.get('★★★★☆', 0)} 篇")
    print(f"  ★★★☆☆：{rating_dist.get('★★★☆☆', 0)} 篇")
    print(f"  ★★☆☆☆：{rating_dist.get('★★☆☆☆', 0)} 篇")
    print(f"  ★☆☆☆☆：{rating_dist.get('★☆☆☆☆', 0)} 篇")
    
    # 提取5星+4星候选池
    candidates = [r for r in all_results if r['rating'] in ['★★★★★', '★★★★☆']]
    
    print(f"\n高价值候选池：{len(candidates)} 篇")
    
    # 写出综合报告
    out_path = base / 'research-rebuild/reports/candidate_pool_top300.md'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# 岐伯文选候选池（前300篇分析）\n\n")
        f.write(f"**分析时间**：2026-10-17\n\n")
        f.write("## 总体统计\n\n")
        f.write(f"- 分析范围：前300篇高信号文章\n")
        f.write(f"- 核心必选（★★★★★）：{rating_dist.get('★★★★★', 0)} 篇\n")
        f.write(f"- 高价值候选（★★★★☆）：{rating_dist.get('★★★★☆', 0)} 篇\n")
        f.write(f"- **高价值候选池总计：{len(candidates)} 篇**\n\n")
        
        f.write("## 候选池清单（按评分降序）\n\n")
        
        for i, r in enumerate(candidates, 1):
            f.write(f"### {i}. {r['citation']}\n")
            f.write(f"**标题**：{r['title']}\n")
            f.write(f"**评级**：{r['rating']} (得分:{r['score']})\n")
            f.write(f"**概念**：{', '.join(r['concept_hits']) if r['concept_hits'] else '无'}\n")
            f.write(f"**planLevel**：{r['planLevel']}\n")
            f.write(f"**篇幅**：{r['answer_len']}字\n")
            f.write(f"**ID**：{r['id']}\n\n")
    
    print(f"\n✓ 综合报告已写入 {out_path}")
    
    # 导出候选池ID列表（供后续精选使用）
    id_list_path = base / 'research-rebuild/data/candidate_pool_ids.txt'
    with open(id_list_path, 'w', encoding='utf-8') as f:
        for r in candidates:
            f.write(f"{r['id']}\n")
    
    print(f"✓ 候选池ID列表已写入 {id_list_path}")

if __name__ == '__main__':
    main()
