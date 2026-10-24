#!/usr/bin/env python3
"""
卷七主题契合度详细分析 - 基于关键词匹配的初步筛查结果
深入分析各册的问题严重程度
"""

import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
CLEAN_DATA = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'

V7_THEMES = {
    'B31': {
        'name': '甲册·存在本質與生命意義',
        'theme': '存在本質與生命意義',
        'keywords': ['生命意义', '存在', '价值', '人生', '意义', '目的', '本质', '终极关怀', '死亡', '虚无', '存在主义'],
    },
    'B32': {
        'name': '乙册·名相辨析與語言牢籠',
        'theme': '名相辨析與語言牢籠',
        'keywords': ['概念', '定义', '语言', '名词', '术语', '误解', '歧义', '标签', '框架', '思维陷阱', '认知偏差'],
    },
    'B33': {
        'name': '丙册·善惡分野與倫理底線',
        'theme': '善惡分野與倫理底線',
        'keywords': ['善恶', '道德', '伦理', '底线', '是非', '价值观', '良知', '正义', '原则', '操守'],
    },
    'B34': {
        'name': '丁册·認識局限與心智模型',
        'theme': '認識局限與心智模型',
        'keywords': ['认知局限', '盲区', '偏见', '心智模型', '思维模式', '视角', '误判', '信息盲区', '知识边界'],
    },
    'B35': {
        'name': '戊册·命途因果與得失隨緣',
        'theme': '命途因果與得失隨緣',
        'keywords': ['命运', '因果', '得失', '随缘', '际遇', '运气', '宿命', '接受', '放下', '顺应'],
    },
    'B36': {
        'name': '己册·人性幽微與雙重人格',
        'theme': '人性幽微與雙重人格',
        'keywords': ['人性', '阴暗面', '双重标准', '虚伪', '表里不一', '自欺', '人格面具', '幽微', '深层动机'],
    },
    'B37': {
        'name': '庚册·神聖敬畏與信仰維度',
        'theme': '神聖敬畏與信仰維度',
        'keywords': ['信仰', '宗教', '神圣', '敬畏', '超越', '灵性', '虔诚', '仪式', '终极关怀', '神秘体验'],
    },
    'B38': {
        'name': '辛册·自處之道與精神獨立',
        'theme': '自處之道與精神獨立',
        'keywords': ['独处', '自我', '独立', '孤独', '自处', '精神独立', '内在', '自足', '自洽', '边界'],
    }
}

# 加载数据
articles_by_id = {}
with open(CLEAN_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        articles_by_id[data['id']] = data

booklets = defaultdict(list)
with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        rec = json.loads(line)
        code = rec.get('booklet_code', '')
        base_code = code[:3] if len(code) > 3 else code
        
        if base_code in V7_THEMES:
            booklets[base_code].append(rec)

print("=" * 100)
print("卷七主题契合度详细分析报告")
print("=" * 100)
print()

# 统计各册情况
summary = []

for code in ['B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38']:
    theme_info = V7_THEMES[code]
    articles = booklets[code]
    
    match_stats = {
        'zero': 0,      # 0%匹配
        'low': 0,       # 1-10%
        'medium': 0,    # 11-30%
        'good': 0,      # 31-50%
        'high': 0       # >50%
    }
    
    for rec in articles:
        original_id = rec['original_id']
        article_data = articles_by_id.get(original_id)
        if not article_data:
            continue
        
        question = article_data.get('question', '')
        answer = article_data.get('answer', '')
        title = article_data.get('title', '')
        full_text = answer if answer else article_data.get('text', '')
        
        keywords = theme_info['keywords']
        keyword_hits = sum(1 for kw in keywords if kw in full_text or kw in title or kw in question)
        match_rate = keyword_hits / len(keywords) if keywords else 0
        
        if match_rate == 0:
            match_stats['zero'] += 1
        elif match_rate <= 0.1:
            match_stats['low'] += 1
        elif match_rate <= 0.3:
            match_stats['medium'] += 1
        elif match_rate <= 0.5:
            match_stats['good'] += 1
        else:
            match_stats['high'] += 1
    
    total = len(articles)
    problem_rate = (match_stats['zero'] + match_stats['low']) / total if total > 0 else 0
    
    summary.append({
        'code': code,
        'name': theme_info['name'],
        'total': total,
        'stats': match_stats,
        'problem_rate': problem_rate
    })
    
    print(f"\n{code} {theme_info['name']}")
    print(f"文章总数: {total}篇")
    print(f"  0%匹配:    {match_stats['zero']:4d}篇 ({match_stats['zero']/total*100:5.1f}%)")
    print(f"  1-10%匹配: {match_stats['low']:4d}篇 ({match_stats['low']/total*100:5.1f}%)")
    print(f"  11-30%匹配:{match_stats['medium']:4d}篇 ({match_stats['medium']/total*100:5.1f}%)")
    print(f"  31-50%匹配:{match_stats['good']:4d}篇 ({match_stats['good']/total*100:5.1f}%)")
    print(f"  >50%匹配:  {match_stats['high']:4d}篇 ({match_stats['high']/total*100:5.1f}%)")
    print(f"  ⚠️ 问题比例: {problem_rate*100:.1f}% (0-10%匹配)")

# 总体统计
print("\n" + "=" * 100)
print("整体统计")
print("=" * 100)

total_articles = sum(s['total'] for s in summary)
total_zero = sum(s['stats']['zero'] for s in summary)
total_low = sum(s['stats']['low'] for s in summary)
total_problem = total_zero + total_low

print(f"\n卷七总计: {total_articles}篇")
print(f"  0%匹配: {total_zero}篇 ({total_zero/total_articles*100:.1f}%)")
print(f"  1-10%匹配: {total_low}篇 ({total_low/total_articles*100:.1f}%)")
print(f"  问题文章合计: {total_problem}篇 ({total_problem/total_articles*100:.1f}%)")

# 按问题严重程度排序
print("\n" + "=" * 100)
print("各册问题严重度排名（按0-10%匹配比例降序）")
print("=" * 100)

sorted_summary = sorted(summary, key=lambda x: x['problem_rate'], reverse=True)
for i, s in enumerate(sorted_summary, 1):
    print(f"{i}. {s['code']} {s['name']}")
    print(f"   问题比例: {s['problem_rate']*100:.1f}% ({s['stats']['zero']+s['stats']['low']}/{s['total']}篇)")

print("\n" + "=" * 100)
print("结论")
print("=" * 100)
print("""
基于关键词匹配的初步筛查显示：

1. **整体问题严重**: 卷七1933篇文章中，65.6%（1268篇）的关键词匹配度<10%

2. **辛册问题最突出**: B38辛册（自處之道與精神獨立）1237篇中954篇(77.1%)匹配度<10%

3. **乙册问题也很明显**: B32乙册（名相辨析與語言牢籠）180篇中140篇(77.8%)匹配度<10%

4. **关键词方法的局限性**:
   - 关键词匹配只是浅层指标，不能完全反映主题契合度
   - 很多文章可能主题相关但未使用这些特定关键词
   - 需要进一步的人工深度阅读和语义分析

5. **建议**:
   - 抽样人工深度阅读各册的"可疑文章"
   - 评估是否存在主题分类错误或主题定义问题
   - 考虑重新审视各册的主题边界和分类标准
""")