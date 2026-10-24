#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
生成高信号篇目清单，作为深度阅读的优先队列
筛选条件：
1. 包含19个自创概念标签之一
2. planLevel为2或3
3. 篇幅>1500字
优先级：自创概念 > planLevel > 篇幅
"""

import json
from pathlib import Path

CORE_CONCEPTS = [
    '人己权界', '自强', '神性享乐', '净输出', '信源管理',
    '择善固执', 'SOP', 'Poetic Irony', '旷野', '不以恶为业',
    '错得对', '元技能', '爱不生债', '评价权', 'CARITAS',
    '王天下', '内务班子', '人神分野', '成功税'
]

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
    signals_path = base / 'research-rebuild/data/all_articles_signals.jsonl'
    
    print("加载信号表...")
    signals = load_jsonl(signals_path)
    
    # 筛选高信号篇目
    high_signal = []
    
    for sig in signals:
        keywords = sig.get('keywords', [])
        keyword_labels = [kw.get('label') for kw in keywords]
        
        # 检查是否包含自创概念
        concept_hits = [c for c in CORE_CONCEPTS if c in keyword_labels]
        
        # 检查planLevel
        plan_level = sig.get('planLevel')
        is_high_level = plan_level in [2, 3]
        
        # 检查篇幅
        text_len = sig.get('text_len', 0)
        is_long = text_len > 1500
        
        # 计算优先级分数
        priority_score = 0
        if concept_hits:
            priority_score += 100 + len(concept_hits) * 10
        if is_high_level:
            priority_score += 50 if plan_level == 3 else 30
        if is_long:
            priority_score += min(text_len // 500, 20)  # 最多加20分
        
        # 至少满足一个条件才入选
        if concept_hits or is_high_level or is_long:
            high_signal.append({
                'id': sig['id'],
                'workbook_ordinal': sig['workbook_ordinal'],
                'full_citation': sig['full_citation'],
                'title': sig['title'],
                'volume_code': sig['volume_code'],
                'booklet_name': sig['booklet_name'],
                'text_len': text_len,
                'planLevel': plan_level,
                'keywords': keyword_labels,
                'concept_hits': concept_hits,
                'priority_score': priority_score,
            })
    
    # 按优先级排序
    high_signal.sort(key=lambda x: -x['priority_score'])
    
    # 写出
    out_path = base / 'research-rebuild/data/high_signal_articles.jsonl'
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in high_signal:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"\n✓ 已生成 {out_path}")
    print(f"  总计：{len(high_signal)} 篇高信号文章")
    
    # 统计
    concept_count = sum(1 for r in high_signal if r['concept_hits'])
    level23_count = sum(1 for r in high_signal if r['planLevel'] in [2, 3])
    long_count = sum(1 for r in high_signal if r['text_len'] > 1500)
    
    print(f"\n  包含自创概念：{concept_count} 篇")
    print(f"  planLevel 2/3：{level23_count} 篇")
    print(f"  篇幅>1500字：{long_count} 篇")
    
    # 按卷统计
    volume_dist = {}
    for rec in high_signal:
        vol = rec['volume_code']
        volume_dist[vol] = volume_dist.get(vol, 0) + 1
    
    print(f"\n  卷分布：")
    for vol in sorted(volume_dist.keys()):
        print(f"    {vol}: {volume_dist[vol]} 篇")
    
    # 展示优先级最高的前20篇
    print(f"\n  优先级最高的前二十篇：")
    for i, rec in enumerate(high_signal[:20], 1):
        concepts_str = ','.join(rec['concept_hits']) if rec['concept_hits'] else ''
        print(f"    {i:2d}. [{rec['priority_score']:3d}分] {rec['full_citation']}")
        if concepts_str:
            print(f"        概念：{concepts_str}")

if __name__ == '__main__':
    main()
