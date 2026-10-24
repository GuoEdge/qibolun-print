#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
执行混合精选策略，定稿约100篇：
1. 基础盘（80篇）：从103篇5星候选按评分降序选出前80篇
2. 均衡补充（约20篇）：从77篇4星候选（及薄弱卷候选）中补足薄弱卷（V2, V4, V8, V5等），使八卷覆盖完整
3. 检查去重与概念覆盖度
4. 最终输出精选100篇清单（含卷册分布、核心概念、理由）
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
    
    # 加载前800篇已提取的原文记录
    b1 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0001_0100.jsonl')
    b2 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0101_0300.jsonl')
    b3 = load_jsonl(base / 'research-rebuild/data/high_signal_content/batch_0301_0800.jsonl')
    
    all_recs = b1 + b2 + b3
    print(f"总计提取文章数: {len(all_recs)}")
    
    # 建立映射及评分
    scored_articles = []
    seen_ids = set()
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
    
    # 分流 5星 与 4星
    five_stars = [a for a in scored_articles if a['rating'] == '★★★★★']
    four_stars = [a for a in scored_articles if a['rating'] == '★★★★☆']
    
    # 按评分降序
    five_stars.sort(key=lambda x: -x['score'])
    four_stars.sort(key=lambda x: -x['score'])
    
    print(f"5星篇数: {len(five_stars)}, 4星篇数: {len(four_stars)}")
    
    # 1. 基础盘80篇
    base_80 = five_stars[:80]
    selected_ids = {a['id'] for a in base_80}
    
    # 统计80篇的卷分布
    def get_vol_dist(items):
        dist = {}
        for x in items:
            v = x['volume_code']
            dist[v] = dist.get(v, 0) + 1
        return dist
    
    vol_dist_80 = get_vol_dist(base_80)
    print("基础盘80篇卷分布:", vol_dist_80)
    
    # 剩余未入选的候选池（包括剩余的5星23篇和4星77篇）
    remaining_candidates = five_stars[80:] + four_stars
    remaining_candidates.sort(key=lambda x: -x['score'])
    
    # 分析各卷在全书中的目标配比
    # 55册总体规模：V1(11册), V2(4册), V3(5册), V4(3册), V5(5册), V6(11册), V7(12册), V8(4册)
    # 100篇理想分布参考：
    # V1 (本根敦伦): 16篇
    # V2 (阴阳合离): 8篇
    # V3 (酬酢进退): 10篇
    # V4 (存神调息): 6篇
    # V5 (度势居货): 10篇
    # V6 (观风察变): 16篇
    # V7 (涤除玄览): 28篇 (核心哲学与元认知)
    # V8 (格物铸器): 6篇
    # 共计 100篇
    
    # 查看当前80篇分布
    # 针对相对薄弱卷（V8, V4, V2, V5）做定向补充，直到凑齐恰好100篇
    supplements = []
    # 卷八格物铸器优先补充
    for a in remaining_candidates:
        if a['id'] in selected_ids:
            continue
        if a['volume_code'] == 'V8' and len([x for x in base_80 + supplements if x['volume_code'] == 'V8']) < 6:
            supplements.append(a)
            selected_ids.add(a['id'])
    
    # 卷四存神调息补充
    for a in remaining_candidates:
        if a['id'] in selected_ids:
            continue
        if a['volume_code'] == 'V4' and len([x for x in base_80 + supplements if x['volume_code'] == 'V4']) < 6:
            supplements.append(a)
            selected_ids.add(a['id'])
            
    # 卷二阴阳合离补充
    for a in remaining_candidates:
        if a['id'] in selected_ids:
            continue
        if a['volume_code'] == 'V2' and len([x for x in base_80 + supplements if x['volume_code'] == 'V2']) < 8:
            supplements.append(a)
            selected_ids.add(a['id'])
            
    # 卷五度势居货补充
    for a in remaining_candidates:
        if a['id'] in selected_ids:
            continue
        if a['volume_code'] == 'V5' and len([x for x in base_80 + supplements if x['volume_code'] == 'V5']) < 10:
            supplements.append(a)
            selected_ids.add(a['id'])

    # 卷三酬酢进退补充
    for a in remaining_candidates:
        if a['id'] in selected_ids:
            continue
        if a['volume_code'] == 'V3' and len([x for x in base_80 + supplements if x['volume_code'] == 'V3']) < 10:
            supplements.append(a)
            selected_ids.add(a['id'])

    # 若还不足100篇，按剩余分数最高补齐
    for a in remaining_candidates:
        if len(base_80) + len(supplements) >= 100:
            break
        if a['id'] not in selected_ids:
            supplements.append(a)
            selected_ids.add(a['id'])
            
    final_100 = base_80 + supplements
    print(f"最终精选篇数: {len(final_100)}")
    
    final_dist = get_vol_dist(final_100)
    print("最终100篇卷分布:", final_dist)
    
    # 检查核心概念覆盖情况
    concept_coverage = {}
    for a in final_100:
        for c in a.get('concept_hits', []):
            concept_coverage[c] = concept_coverage.get(c, 0) + 1
    print("核心概念覆盖情况:", concept_coverage)
    
    # 按原55册架构卷册顺序编排（卷一至卷八，同卷内按workbook_ordinal升序）
    final_100.sort(key=lambda x: (x['volume_code'], x.get('workbook_ordinal', 0)))
    
    # 写出最终100篇JSONL
    out_jsonl = base / 'research-rebuild/data/qibo_wenxuan_100.jsonl'
    with open(out_jsonl, 'w', encoding='utf-8') as f:
        for rec in final_100:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f"✓ 最终精选100篇已保存至 {out_jsonl}")

if __name__ == '__main__':
    main()
