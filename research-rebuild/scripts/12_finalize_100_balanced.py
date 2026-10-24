#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
精细化八卷均衡编排与定稿100篇：
目标分布：
卷一本根敦伦: 16篇
卷二阴阳合离: 8篇
卷三酬酢进退: 12篇
卷四存神调息: 8篇
卷五度势居货: 10篇
卷六观风察变: 14篇
卷七涤除玄览: 28篇 (核心形而上与元认知)
卷八格物铸器: 4篇  (器物、技艺与工程治理)
合计: 100篇

选篇原则：
1. 各卷内部优先选取5星核心理论篇（概念明确、论证完整、独创深刻）；
2. 确保19个核心自创概念最大化覆盖；
3. 卷八补充代表性篇目：《缪斯性》（神性享乐，2067字）、《无病呻吟》（净输出/信源管理/不以恶为业）、《正果》（王天下/国家工程）、《没有简单》（元技能/功夫）；
4. 篇目按五十五册原典顺序排布，形成清晰结构。
"""

import json
from pathlib import Path

def load_jsonl(path):
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def score_article(rec):
    answer = rec.get('answer', '')
    answer_len = len(answer)
    concept_hits = rec.get('concept_hits', [])
    plan_level = rec.get('planLevel')
    
    score = 0
    tags = []
    if concept_hits:
        score += 100 + len(concept_hits) * 10
        tags.append(f"C:{','.join(concept_hits)}")
    if plan_level == 3:
        score += 50
        tags.append("T")
    elif plan_level == 2:
        score += 30
        tags.append("T")
    if answer_len >= 2000:
        score += 20
        tags.append("F")
    elif answer_len >= 1000:
        score += 10
        tags.append("F")
    elif answer_len < 500:
        score -= 20
    
    method_keywords = ['怎么', '如何', '方法', '策略', '步骤', '原则', '标准', '判断', '选择', '规则', '框架']
    method_count = sum(1 for kw in method_keywords if kw in answer)
    if method_count >= 3:
        score += 15
        tags.append("M")
    
    originality_markers = [
        '其实', '实则', '要害', '问题不在', '真正的', '关键', '本质',
        '看似', '实际', '表面', '根本', '核心', '往往', '总是'
    ]
    originality_count = sum(1 for marker in originality_markers if answer.count(marker) >= 2)
    if originality_count >= 5:
        score += 15
        tags.append("O")
    
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
    
    return score, rating, tags

def main():
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    
    b1 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0001_0100.jsonl')
    b2 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0101_0300.jsonl')
    b3 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0301_0800.jsonl')
    
    all_recs = b1 + b2 + b3
    seen_ids = set()
    scored_articles = []
    for rec in all_recs:
        rid = rec['id']
        if rid in seen_ids:
            continue
        seen_ids.add(rid)
        score, rating, tags = score_article(rec)
        scored_articles.append({
            **rec,
            'score': score,
            'rating': rating,
            'tags': tags
        })
    
    # 目标卷配比：共计 100 篇
    target_quotas = {
        'V1': 16, # 本根敦伦
        'V2': 8,  # 阴阳合离
        'V3': 12, # 酬酢进退
        'V4': 8,  # 存神调息
        'V5': 10, # 度势居货
        'V6': 14, # 观风察变
        'V7': 28, # 涤除玄览
        'V8': 4,  # 格物铸器
    }
    
    # 按卷分组并按评分降序排列
    vol_groups = {}
    for a in scored_articles:
        v = a['volume_code']
        vol_groups.setdefault(v, []).append(a)
    
    for v in vol_groups:
        vol_groups[v].sort(key=lambda x: -x['score'])
        
    final_selected = []
    for v, quota in target_quotas.items():
        candidates = vol_groups.get(v, [])
        # 特殊处理卷八：确保把有代表性的长篇和概念篇排在前列
        if v == 'V8':
            # 排序：有概念且长篇优先
            candidates.sort(key=lambda x: (len(x.get('concept_hits', [])) > 0, len(x.get('answer', '')) > 500, x['score']), reverse=True)
        selected = candidates[:quota]
        final_selected.extend(selected)
        print(f"卷 {v}: 目标 {quota} 篇，实际选中 {len(selected)} 篇 (最高分 {selected[0]['score']}，最低分 {selected[-1]['score']})")
    
    print(f"\n总选定篇数: {len(final_selected)}")
    
    # 统计核心概念覆盖
    concept_coverage = {}
    for a in final_selected:
        for c in a.get('concept_hits', []):
            concept_coverage[c] = concept_coverage.get(c, 0) + 1
    print("\n核心自创概念覆盖情况:")
    for c, count in sorted(concept_coverage.items(), key=lambda x: -x[1]):
        print(f"  - {c}: {count} 篇")
        
    # 按卷编目与原书序号排序
    final_selected.sort(key=lambda x: (x['volume_code'], x.get('workbook_ordinal', 0)))
    
    # 保存 JSONL
    out_jsonl = base / 'research-rebuild/data/qibo_wenxuan_100_final.jsonl'
    with open(out_jsonl, 'w', encoding='utf-8') as f:
        for rec in final_selected:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            
    print(f"\n✓ 最终100篇精选清单已写入 {out_jsonl}")

if __name__ == '__main__':
    main()
