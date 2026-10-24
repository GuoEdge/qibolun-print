#!/usr/bin/env python3
"""
卷七文章内容与主题契合度深度审查
全量读取1933篇文章，逐篇分析与所在册主题的契合度
"""

import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
CLEAN_DATA = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'

# 卷七各册主题定义
V7_THEMES = {
    'B31': {
        'name': '甲册·存在本質與生命意義',
        'theme': '存在本質與生命意義',
        'keywords': ['生命意义', '存在', '价值', '人生', '意义', '目的', '本质', '终极关怀', '死亡', '虚无', '存在主义'],
        'scope': '探讨生命存在的根本价值、人生意义、存在焦虑、死亡意识等终极性哲学问题'
    },
    'B32': {
        'name': '乙册·名相辨析與語言牢籠',
        'theme': '名相辨析與語言牢籠',
        'keywords': ['概念', '定义', '语言', '名词', '术语', '误解', '歧义', '标签', '框架', '思维陷阱', '认知偏差'],
        'scope': '辨析概念定义、揭示语言框架对思维的束缚、澄清常见认知误区'
    },
    'B33': {
        'name': '丙册·善惡分野與倫理底線',
        'theme': '善惡分野與倫理底線',
        'keywords': ['善恶', '道德', '伦理', '底线', '是非', '价值观', '良知', '正义', '原则', '操守'],
        'scope': '探讨道德判断标准、伦理底线、善恶分野的界定与实践'
    },
    'B34': {
        'name': '丁册·認識局限與心智模型',
        'theme': '認識局限與心智模型',
        'keywords': ['认知局限', '盲区', '偏见', '心智模型', '思维模式', '视角', '误判', '信息盲区', '知识边界'],
        'scope': '揭示认知的局限性、思维盲区、心智模型的固化与突破'
    },
    'B35': {
        'name': '戊册·命途因果與得失隨緣',
        'theme': '命途因果與得失隨緣',
        'keywords': ['命运', '因果', '得失', '随缘', '际遇', '运气', '宿命', '接受', '放下', '顺应'],
        'scope': '探讨命运观、因果关系、得失心态、随遇而安的人生智慧'
    },
    'B36': {
        'name': '己册·人性幽微與雙重人格',
        'theme': '人性幽微與雙重人格',
        'keywords': ['人性', '阴暗面', '双重标准', '虚伪', '表里不一', '自欺', '人格面具', '幽微', '深层动机'],
        'scope': '剖析人性的幽微复杂、表里不一、双重标准等深层心理现象'
    },
    'B37': {
        'name': '庚册·神聖敬畏與信仰維度',
        'theme': '神聖敬畏與信仰維度',
        'keywords': ['信仰', '宗教', '神圣', '敬畏', '超越', '灵性', '虔诚', '仪式', '终极关怀', '神秘体验'],
        'scope': '探讨信仰、宗教、神圣感、敬畏心等精神维度'
    },
    'B38': {
        'name': '辛册·自處之道與精神獨立',
        'theme': '自處之道與精神獨立',
        'keywords': ['独处', '自我', '独立', '孤独', '自处', '精神独立', '内在', '自足', '自洽', '边界'],
        'scope': '探讨独处之道、精神独立、自我完整性、内在自洽等议题'
    }
}

# 加载文章ID到内容的映射
articles_by_id = {}
print("正在加载文章内容...")
with open(CLEAN_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        articles_by_id[data['id']] = data

print(f"已加载 {len(articles_by_id)} 篇文章内容\n")

# 加载编目并按册分组
booklets = defaultdict(list)
print("正在加载编目...")
with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        rec = json.loads(line)
        code = rec.get('booklet_code', '')
        base_code = code[:3] if len(code) > 3 else code
        
        if base_code in V7_THEMES:
            booklets[base_code].append(rec)

print(f"卷七共 {sum(len(v) for v in booklets.values())} 篇文章\n")
print("=" * 80)

# 逐册深度审查
total_issues = []

for code in ['B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38']:
    theme_info = V7_THEMES[code]
    articles = booklets[code]
    
    print(f"\n{code} {theme_info['name']}")
    print(f"主题: {theme_info['theme']}")
    print(f"范围: {theme_info['scope']}")
    print(f"文章数: {len(articles)}篇")
    print("-" * 80)
    
    issues_in_booklet = []
    
    for i, rec in enumerate(articles, 1):
        title = rec['title']
        original_id = rec['original_id']
        ordinal = rec['workbook_ordinal']
        
        # 获取完整文章内容
        article_data = articles_by_id.get(original_id)
        if not article_data:
            print(f"  ⚠️  #{ordinal:4d} 《{title}》- 找不到内容数据")
            issues_in_booklet.append({
                'ordinal': ordinal,
                'title': title,
                'issue': '数据缺失'
            })
            continue
        
        # 提取关键信息
        question = article_data.get('question', '')
        answer = article_data.get('answer', '')
        full_text = answer if answer else article_data.get('text', '')
        
        # 分析契合度
        # 1. 关键词匹配
        keywords = theme_info['keywords']
        keyword_hits = sum(1 for kw in keywords if kw in full_text or kw in title or kw in question)
        
        # 2. 主题契合度评估（简单启发式）
        theme_match_score = keyword_hits / len(keywords) if keywords else 0
        
        # 标记可疑文章（关键词匹配度<10%）
        if theme_match_score < 0.1:
            preview = full_text[:100].replace('\n', ' ')
            print(f"  ❓ #{ordinal:4d} 《{title}》")
            print(f"       关键词匹配: {keyword_hits}/{len(keywords)} ({theme_match_score*100:.0f}%)")
            print(f"       内容预览: {preview}...")
            
            issues_in_booklet.append({
                'ordinal': ordinal,
                'title': title,
                'keyword_match': keyword_hits,
                'match_rate': theme_match_score,
                'preview': preview
            })
    
    # 汇总本册问题
    if issues_in_booklet:
        print(f"\n  ⚠️  本册发现 {len(issues_in_booklet)} 篇可疑文章（关键词匹配<10%）")
        total_issues.extend([(code, issue) for issue in issues_in_booklet])
    else:
        print(f"\n  ✓ 本册文章主题契合度良好")

print("\n" + "=" * 80)
print(f"\n审查完成！")
print(f"卷七总计: {sum(len(booklets[c]) for c in booklets)} 篇文章")
print(f"标记可疑: {len(total_issues)} 篇 ({len(total_issues)/sum(len(booklets[c]) for c in booklets)*100:.1f}%)")

# 输出详细报告
if total_issues:
    print("\n" + "=" * 80)
    print("可疑文章详细清单:")
    print("=" * 80)
    
    for code, issue in total_issues:
        theme_name = V7_THEMES[code]['name']
        print(f"\n[{code}] {theme_name}")
        print(f"  #{issue['ordinal']:4d} 《{issue['title']}》")
        if 'keyword_match' in issue:
            print(f"  关键词匹配: {issue['keyword_match']} ({issue['match_rate']*100:.0f}%)")
            print(f"  内容: {issue['preview']}...")
        else:
            print(f"  问题: {issue['issue']}")
