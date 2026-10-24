#!/usr/bin/env python3
"""
对 v3 语料中的新增文章进行分类
使用关键词匹配为新文章分配主题概念
"""
import json
import re
from pathlib import Path
from collections import defaultdict

# 23 个主题概念
CONCEPTS = [
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
]

# 保守的关键词线索
CUES = {
    "照料与家庭": ["家庭", "父母", "子女", "亲属", "兄弟", "亲戚", "婚姻", "夫妻", "孩子", "养育"],
    "爱与回应": ["恋爱", "感情", "伴侣", "分手", "暧昧", "网友", "友谊", "约会", "爱", "关心", "尊重", "回应", "帮助", "关系"],
    "能力与学习": ["学习", "教育", "能力", "知识", "读书", "学校", "训练", "经验", "学生", "老师"],
    "劳动与组织": ["工作", "职场", "同事", "公司", "组织", "管理", "团队", "招聘", "员工", "老板"],
    "财富与市场": ["钱", "财富", "收入", "借贷", "投资", "消费", "市场", "买", "卖", "经济", "价格"],
    "法律与秩序": ["法律", "犯罪", "诈骗", "刑罚", "警察", "司法", "违法", "安全", "合法"],
    "权力与异议": ["权力", "政府", "政治", "官员", "制度", "阶层", "统治", "异议", "社会"],
    "技术与工程": ["技术", "工程", "软件", "互联网", "平台", "算法", "设备", "系统", "代码"],
    "人工智能与机器": ["人工智能", "AI", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶", "深度学习"],
    "性别与身体": ["女性", "男性", "性别", "身体", "生育", "性关系", "怀孕", "同意", "生理"],
    "心理与主体": ["心理", "情绪", "焦虑", "抑郁", "孤独", "性格", "自我", "精神", "感受"],
    "生态与自然": ["自然", "生态", "气候", "环境", "能源", "动物", "植物", "天气", "资源"],
    "文明与历史": ["历史", "文明", "社会", "文化", "民族", "国家", "古代", "传统", "习俗"],
    "事实与证据": ["事实", "证据", "数据", "研究", "统计", "为什么", "原因", "证明", "调查"],
    "定义与达意": ["意思", "定义", "概念", "区别", "如何理解", "所谓", "含义"],
    "选择与自由": ["选择", "自由", "决定", "要不要", "是否应该", "怎么办", "判断"],
    "责任与后果": ["责任", "后果", "风险", "代价", "承担", "应该", "义务"],
    "成本与总账": ["成本", "收益", "代价", "投入", "回报", "效率", "划算"],
    "信用与信任": ["信任", "信用", "可靠", "欺骗", "诚实", "背叛", "承诺"],
    "边界与许可": ["边界", "拒绝", "隐私", "许可", "限制", "规则", "同意"],
    "净输出与不掠夺": ["掠夺", "剥削", "伤害", "占用", "公平", "互惠", "利用"],
    "宗教与自然法": ["宗教", "信仰", "道德", "正义", "自然法", "神", "伦理"],
    "民族与身份": ["民族", "身份", "国籍", "移民", "种族", "认同"],
}

def classify_article(text, title, question):
    """根据关键词为文章分类"""
    full_text = f"{title} {question} {text}"
    
    scores = {concept: 0 for concept in CONCEPTS}
    matched_cues = {}
    
    for concept, cues in CUES.items():
        for cue in cues:
            # 统计该线索出现次数（最多计3次）
            hits = min(len(re.findall(re.escape(cue), full_text, flags=re.IGNORECASE)), 3)
            if hits > 0:
                scores[concept] += hits
                if concept not in matched_cues:
                    matched_cues[concept] = []
                matched_cues[concept].append(cue)
    
    # 按分数降序排列，取前6个
    ranked = sorted(
        [(concept, score) for concept, score in scores.items() if score > 0],
        key=lambda x: (-x[1], x[0])
    )
    
    top_concepts = [c for c, s in ranked[:6]]
    
    return {
        'concepts': top_concepts,
        'primary': top_concepts[0] if top_concepts else '未分类',
        'scores': {c: s for c, s in ranked[:6]},
        'matched_cues': matched_cues
    }

def main():
    base_dir = Path('/storage/Users/currentUser/Documents/岐伯论')
    v3_path = base_dir / 'sooon-q9adg-articles-v3.jsonl'
    old_corpus_path = base_dir / 'sooon-q9adg-articles.jsonl'
    clean_path = base_dir / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3-clean.jsonl'
    
    # 读取旧语料的 ID 集合
    print("读取旧语料 ID...")
    old_ids = set()
    with open(old_corpus_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                old_ids.add(record['id'])
    
    print(f"  旧语料：{len(old_ids)} 篇")
    
    # 读取已分类的记录
    print("读取已分类记录...")
    classified_ids = set()
    classified_records = {}
    with open(clean_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                classified_ids.add(record['id'])
                classified_records[record['id']] = record
    
    print(f"  已分类：{len(classified_ids)} 篇")
    
    # 找出新增文章
    print("\n处理 v3 语料...")
    new_articles = []
    ordinal = 0
    
    with open(v3_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                ordinal += 1
                record = json.loads(line)
                rec_id = record['id']
                
                if rec_id not in classified_ids:
                    new_articles.append({
                        'ordinal': ordinal,
                        'id': rec_id,
                        'title': record.get('title', ''),
                        'question': record.get('question', ''),
                        'text': record.get('text', ''),
                        'brief': record.get('brief', ''),
                        'url': record.get('url', ''),
                        'publishedAt': record.get('publishedAt', 0),
                        'provenance': record.get('provenance', {})
                    })
    
    print(f"  新增文章：{len(new_articles)} 篇")
    
    # 对新增文章进行分类
    print("\n开始分类...")
    classified_new = []
    concept_stats = defaultdict(int)
    
    for i, article in enumerate(new_articles, 1):
        classification = classify_article(
            article['text'],
            article['title'],
            article['question']
        )
        
        classified_record = {
            'ordinal': article['ordinal'],
            'id': article['id'],
            'title': article['title'],
            'question': article['question'],
            'brief': article['brief'],
            'text': article['text'],
            'url': article['url'],
            'publishedAt': article['publishedAt'],
            'provenance': article['provenance'],
            'classification': {
                'concepts': classification['concepts'],
                'primary': classification['primary'],
                'scores': classification['scores'],
                'method': 'keyword-matching-v1',
                'status': 'auto-classified'
            }
        }
        
        classified_new.append(classified_record)
        
        # 统计
        for concept in classification['concepts']:
            concept_stats[concept] += 1
        
        if i % 50 == 0:
            print(f"  已分类：{i}/{len(new_articles)}")
    
    print(f"\n分类完成：{len(classified_new)} 篇")
    
    # 合并到完整分类库
    output_path = base_dir / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'
    
    print(f"\n生成新分类库：{output_path.name}")
    
    # 先写入已有的分类记录
    with open(output_path, 'w', encoding='utf-8') as f:
        with open(clean_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                if line.strip():
                    f.write(line)
        
        # 追加新分类的记录
        for record in classified_new:
            f.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')
    
    # 输出统计
    print(f"\n✓ 分类完成")
    print(f"  总记录：{len(classified_ids) + len(classified_new)} 篇")
    print(f"  已有分类：{len(classified_ids)} 篇")
    print(f"  新增分类：{len(classified_new)} 篇")
    print(f"\n新增文章主题分布（Top 10）：")
    for concept, count in sorted(concept_stats.items(), key=lambda x: -x[1])[:10]:
        print(f"  {concept}: {count} 篇")
    
    # 生成分类报告
    report_path = base_dir / f'新增文章分类报告_{len(classified_new)}篇.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# 新增文章分类报告\n\n")
        f.write(f"分类时间：2026-10-09\n\n")
        f.write(f"## 概要\n\n")
        f.write(f"- 新增文章：{len(classified_new)} 篇\n")
        f.write(f"- 分类方法：关键词匹配\n")
        f.write(f"- 概念体系：23 个主题概念\n\n")
        f.write(f"## 主题分布\n\n")
        
        for concept, count in sorted(concept_stats.items(), key=lambda x: -x[1]):
            pct = count / len(classified_new) * 100
            f.write(f"- {concept}: {count} 篇 ({pct:.1f}%)\n")
        
        f.write(f"\n## 新增文章列表\n\n")
        for record in classified_new:
            f.write(f"### {record['ordinal']}. {record['title']}\n\n")
            f.write(f"- ID: `{record['id']}`\n")
            f.write(f"- 主题：{record['classification']['primary']}\n")
            if len(record['classification']['concepts']) > 1:
                f.write(f"- 相关概念：{', '.join(record['classification']['concepts'][1:])}\n")
            f.write(f"\n")
    
    print(f"\n分类报告：{report_path.name}")

if __name__ == '__main__':
    main()
