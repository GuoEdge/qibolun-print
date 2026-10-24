#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
深度阅读分析：批量标记候选篇目（第101-300篇）
"""

import json
from pathlib import Path

# 复用相同的分析规则
def analyze_article(rec):
    """深度分析单篇文章"""
    title = rec['title']
    answer = rec['answer']
    answer_len = len(answer)
    concept_hits = rec.get('concept_hits', [])
    plan_level = rec.get('planLevel')
    
    score = 0
    tags = []
    
    # 1. 核心概念权重最高
    if concept_hits:
        score += 100 + len(concept_hits) * 10
        tags.append(f"C:{','.join(concept_hits)}")
    
    # 2. planLevel高权重
    if plan_level == 3:
        score += 50
        tags.append("T")
    elif plan_level == 2:
        score += 30
        tags.append("T")
    
    # 3. 篇幅因素
    if answer_len >= 2000:
        score += 20
        tags.append("F")
    elif answer_len >= 1000:
        score += 10
        tags.append("F")
    elif answer_len < 500:
        score -= 20
    
    # 4. 方法论价值
    method_keywords = ['怎么', '如何', '方法', '策略', '步骤', '原则', '标准', '判断', '选择', '规则', '框架']
    method_count = sum(1 for kw in method_keywords if kw in answer)
    if method_count >= 3:
        score += 15
        tags.append("M")
    
    # 5. 独创性
    originality_markers = [
        '其实', '实则', '要害', '问题不在', '真正的', '关键', '本质',
        '看似', '实际', '表面', '根本', '核心', '往往', '总是'
    ]
    originality_count = sum(1 for marker in originality_markers if answer.count(marker) >= 2)
    if originality_count >= 5:
        score += 15
        tags.append("O")
    
    # 评级判定
    if score >= 160:
        rating = "★★★★★"
        status = "✓ 核心必选"
    elif score >= 140:
        rating = "★★★★☆"
        status = "高价值候选"
    elif score >= 120:
        rating = "★★★☆☆"
        status = "一般候选"
    elif score >= 100:
        rating = "★★☆☆☆"
        status = "低优先级"
    else:
        rating = "★☆☆☆☆"
        status = "暂不收录"
    
    core_thesis = f"{', '.join(concept_hits)}" if concept_hits else "（待人工补充）"
    
    reasons = []
    if concept_hits:
        reasons.append(f"引入核心概念{len(concept_hits)}个")
    if plan_level in [2, 3]:
        reasons.append(f"planLevel {plan_level}")
    if answer_len >= 2000:
        reasons.append(f"篇幅充实（{answer_len}字）")
    if 'M' in tags:
        reasons.append("方法论清晰")
    if 'O' in tags:
        reasons.append("具有独创洞察")
    
    reason = "；".join(reasons) if reasons else "（需人工复核）"
    
    return {
        'rating': rating,
        'tags': tags,
        'core_thesis': core_thesis,
        'reason': reason,
        'status': status,
        'score': score,
    }

def main():
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    batch_file = base / 'research-rebuild/data/high_signal_content/batch_0101_0300.jsonl'
    
    print("加载批次文件...")
    with open(batch_file, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f if line.strip()]
    
    print(f"开始分析 {len(articles)} 篇文章...\n")
    
    results = []
    for i, rec in enumerate(articles, 101):
        analysis = analyze_article(rec)
        results.append({
            'seq': i,
            'id': rec['id'],
            'citation': rec['full_citation'],
            'title': rec['title'],
            'concept_hits': rec.get('concept_hits', []),
            'planLevel': rec.get('planLevel'),
            'answer_len': len(rec['answer']),
            **analysis
        })
    
    # 按评分排序
    results.sort(key=lambda x: -x['score'])
    
    # 写出markdown报告
    out_path = base / 'research-rebuild/reports/batch_0101_0300_analysis.md'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# 第101-300篇高信号文章深度分析报告\n\n")
        f.write(f"**分析时间**：2026-10-17\n\n")
        f.write("## 评级统计\n\n")
        
        rating_dist = {}
        for r in results:
            rating_dist[r['rating']] = rating_dist.get(r['rating'], 0) + 1
        
        f.write(f"- ★★★★★ (核心必选)：{rating_dist.get('★★★★★', 0)} 篇\n")
        f.write(f"- ★★★★☆ (高价值候选)：{rating_dist.get('★★★★☆', 0)} 篇\n")
        f.write(f"- ★★★☆☆ (一般候选)：{rating_dist.get('★★★☆☆', 0)} 篇\n")
        f.write(f"- ★★☆☆☆ (低优先级)：{rating_dist.get('★★☆☆☆', 0)} 篇\n")
        f.write(f"- ★☆☆☆☆ (暂不收录)：{rating_dist.get('★☆☆☆☆', 0)} 篇\n\n")
        
        f.write("## 详细标记清单\n\n")
        f.write("### 核心必选（★★★★★）\n\n")
        
        for r in [x for x in results if x['rating'] == '★★★★★']:
            f.write(f"#### 第{r['seq']}篇：{r['citation']}\n")
            f.write(f"**标题**：{r['title']}\n")
            f.write(f"**评级**：{r['rating']} (得分:{r['score']})\n")
            f.write(f"**核心命题**：{r['core_thesis']}\n")
            f.write(f"**理由**：{r['reason']}\n\n")
        
        f.write("### 高价值候选（★★★★☆）\n\n")
        for r in [x for x in results if x['rating'] == '★★★★☆']:
            f.write(f"#### 第{r['seq']}篇：{r['citation']}\n")
            f.write(f"**标题**：{r['title']}\n")
            f.write(f"**评级**：{r['rating']} (得分:{r['score']})\n")
            f.write(f"**核心命题**：{r['core_thesis']}\n")
            f.write(f"**理由**：{r['reason']}\n\n")
        
        f.write("### 其他候选（★★★☆☆及以下）\n\n")
        f.write("_仅列出篇目_\n\n")
        for r in [x for x in results if x['rating'] not in ['★★★★★', '★★★★☆']]:
            f.write(f"- [{r['rating']}] 第{r['seq']}篇：{r['citation']} ({r['answer_len']}字)\n")
    
    print(f"\n✓ 分析报告已写入 {out_path}")
    print(f"\n评级统计：")
    print(f"  ★★★★★：{rating_dist.get('★★★★★', 0)} 篇")
    print(f"  ★★★★☆：{rating_dist.get('★★★★☆', 0)} 篇")
    print(f"  ★★★☆☆：{rating_dist.get('★★★☆☆', 0)} 篇")
    print(f"  ★★☆☆☆：{rating_dist.get('★★☆☆☆', 0)} 篇")
    print(f"  ★☆☆☆☆：{rating_dist.get('★☆☆☆☆', 0)} 篇")

if __name__ == '__main__':
    main()
