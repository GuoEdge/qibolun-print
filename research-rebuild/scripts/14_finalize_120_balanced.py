#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
精细化八卷均衡编排与定稿120篇黄金版：
目标分布（共计120篇）：
卷一【本根敦倫】: 18篇 (增加长篇大论《反欺凌》《孩子不说话》等)
卷二【陰陽合離】: 10篇 (增加《姬别霸王》《傲骨贤妻》等)
卷三【酬酢進退】: 15篇 (增加《道歉》《自证大礼包》《好感》《与人交》等)
卷四【存神調息】: 10篇 (增加《职业规划》《三认》《经验驱动》等)
卷五【度勢居貨】: 12篇 (增加商业博弈与组织管理名篇)
卷六【觀風察變】: 16篇 (增加社会思潮深度解剖)
卷七【滌除玄覽】: 34篇 (增加《财富观》9095字、《疗愈艺术》7497字、《美德》(Poetic Irony)等压卷之作)
卷八【格物鑄器】: 5篇  (百工技艺、生活美学与工程治理)
合计: 120篇
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
    
    # 目标卷配比：共计 120 篇
    target_quotas = {
        'V1': 18, # 本根敦伦
        'V2': 10, # 阴阳合离
        'V3': 15, # 酬酢进退
        'V4': 10, # 存神调息
        'V5': 12, # 度势居货
        'V6': 16, # 观风察变
        'V7': 34, # 涤除玄览
        'V8': 5,  # 格物铸器
    }
    
    vol_groups = {}
    for a in scored_articles:
        v = a['volume_code']
        vol_groups.setdefault(v, []).append(a)
    
    for v in vol_groups:
        vol_groups[v].sort(key=lambda x: -x['score'])
        
    final_selected = []
    for v, quota in target_quotas.items():
        candidates = vol_groups.get(v, [])
        if v == 'V8':
            candidates.sort(key=lambda x: (len(x.get('concept_hits', [])) > 0, len(x.get('answer', '')) > 500, x['score']), reverse=True)
        selected = candidates[:quota]
        final_selected.extend(selected)
        print(f"卷 {v}: 目标 {quota} 篇，实际选中 {len(selected)} 篇 (最高分 {selected[0]['score']}，最低分 {selected[-1]['score']})")
    
    print(f"\n总选定篇数: {len(final_selected)}")
    
    total_chars = sum(len(a.get('answer', '')) for a in final_selected)
    print(f"总正文字数: {total_chars} 字，平均每篇: {total_chars/len(final_selected):.1f} 字")
    
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
    out_jsonl = base / 'research-rebuild/data/qibo_wenxuan_120_final.jsonl'
    with open(out_jsonl, 'w', encoding='utf-8') as f:
        for rec in final_selected:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            
    print(f"\n✓ 最终120篇精选清单已写入 {out_jsonl}")

if __name__ == '__main__':
    main()
