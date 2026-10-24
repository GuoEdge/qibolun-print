#!/usr/bin/env python3
"""
为 v3 新增的 37 篇文章补充分类
"""
import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# 23 个主题概念
CONCEPTS = [
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
]

# 关键词线索
CUES = {
    "照料与家庭": ["家庭", "父母", "子女", "亲属", "兄弟", "亲戚", "婚姻", "夫妻", "孩子", "养育", "抚养"],
    "爱与回应": ["恋爱", "感情", "伴侣", "分手", "暧昧", "网友", "友谊", "约会", "爱", "关心", "尊重", "回应", "帮助", "关系"],
    "能力与学习": ["学习", "教育", "能力", "知识", "读书", "学校", "训练", "经验", "学生", "老师", "技能"],
    "劳动与组织": ["工作", "职场", "同事", "公司", "组织", "管理", "团队", "招聘", "员工", "老板", "企业"],
    "财富与市场": ["钱", "财富", "收入", "借贷", "投资", "消费", "市场", "买", "卖", "经济", "价格", "成本"],
    "法律与秩序": ["法律", "犯罪", "诈骗", "刑罚", "警察", "司法", "违法", "安全", "合法", "法院"],
    "权力与异议": ["权力", "政府", "政治", "官员", "制度", "阶层", "统治", "异议", "社会", "公共"],
    "技术与工程": ["技术", "工程", "软件", "互联网", "平台", "算法", "设备", "系统", "代码", "数据"],
    "人工智能与机器": ["人工智能", "AI", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶", "深度学习", "神经网络"],
    "性别与身体": ["女性", "男性", "性别", "身体", "生育", "性关系", "怀孕", "同意", "生理", "性"],
    "心理与主体": ["心理", "情绪", "焦虑", "抑郁", "孤独", "性格", "自我", "精神", "感受", "心态"],
    "生态与自然": ["自然", "生态", "气候", "环境", "能源", "动物", "植物", "天气", "资源", "污染"],
    "文明与历史": ["历史", "文明", "社会", "文化", "民族", "国家", "古代", "传统", "习俗", "朝代"],
    "事实与证据": ["事实", "证据", "数据", "研究", "统计", "为什么", "原因", "证明", "调查", "真相"],
    "定义与达意": ["意思", "定义", "概念", "区别", "如何理解", "所谓", "含义", "解释"],
    "选择与自由": ["选择", "自由", "决定", "要不要", "是否应该", "怎么办", "判断", "抉择"],
    "责任与后果": ["责任", "后果", "风险", "代价", "承担", "应该", "义务", "担当"],
    "成本与总账": ["成本", "收益", "代价", "投入", "回报", "效率", "划算", "值得"],
    "信用与信任": ["信任", "信用", "可靠", "欺骗", "诚实", "背叛", "承诺", "诚信"],
    "边界与许可": ["边界", "拒绝", "隐私", "许可", "限制", "规则", "同意", "底线"],
    "净输出与不掠夺": ["掠夺", "剥削", "伤害", "占用", "公平", "互惠", "利用", "索取"],
    "宗教与自然法": ["宗教", "信仰", "道德", "正义", "自然法", "神", "伦理", "善恶"],
    "民族与身份": ["民族", "身份", "国籍", "移民", "种族", "认同", "族群"],
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

base_dir = Path('/storage/Users/currentUser/Documents/岐伯论')

# 读取 v2 IDs
print("读取 v2 语料...")
v2_ids = set()
with open(base_dir / 'sooon-q9adg-articles-v2.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            v2_ids.add(json.loads(line)['id'])

print(f"  v2: {len(v2_ids)} 篇")

# 读取分类库
print("\n读取分类库...")
all_records = []
new_articles_need_classify = []

clean_path = base_dir / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v3-clean.jsonl'
with open(clean_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            record = json.loads(line)
            all_records.append(record)
            
            # 检查是否是新增且未分类的文章
            if record['id'] not in v2_ids:
                if 'classification' not in record or not record['classification']:
                    new_articles_need_classify.append(record)

print(f"  总记录: {len(all_records)} 篇")
print(f"  需要分类的新增文章: {len(new_articles_need_classify)} 篇")

# 对新文章进行分类
print("\n开始分类...")
concept_stats = defaultdict(int)
classified_count = 0

for i, article in enumerate(new_articles_need_classify, 1):
    classification = classify_article(
        article.get('text', ''),
        article.get('title', ''),
        article.get('question', '')
    )
    
    # 添加分类信息
    article['classification'] = {
        'concepts': classification['concepts'],
        'primary': classification['primary'],
        'scores': classification['scores'],
        'method': 'keyword-matching-v1',
        'status': 'auto-classified',
        'classified_at': datetime.now().isoformat()
    }
    
    classified_count += 1
    
    # 统计
    for concept in classification['concepts']:
        concept_stats[concept] += 1
    
    if i % 10 == 0:
        print(f"  已分类: {i}/{len(new_articles_need_classify)}")

print(f"\n✓ 分类完成: {classified_count} 篇")

# 写入更新后的分类库
output_path = base_dir / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'
print(f"\n生成新分类库: {output_path.name}")

with open(output_path, 'w', encoding='utf-8') as f:
    for record in all_records:
        f.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')

print(f"  输出: {len(all_records)} 篇")

# 生成报告
print("\n生成分类报告...")
report_path = base_dir / '岐伯论_v3新增37篇分类报告_2026-10-09.md'

with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# 岐伯论 v3 新增文章分类报告\n\n")
    f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("## 一、同步概要\n\n")
    f.write("| 指标 | 数值 |\n")
    f.write("|------|------|\n")
    f.write("| v2 语料 | 4,305 篇 |\n")
    f.write("| v3 语料 | 4,342 篇 |\n")
    f.write("| 本次新增 | 37 篇 |\n")
    f.write("| 已完成分类 | 37 篇 |\n")
    f.write("| 分类方法 | 关键词匹配 |\n")
    f.write("| 分类库版本 | v4 |\n\n")
    
    f.write("## 二、主题分布\n\n")
    
    for concept, count in sorted(concept_stats.items(), key=lambda x: -x[1]):
        pct = count / classified_count * 100 if classified_count > 0 else 0
        f.write(f"- **{concept}**: {count} 篇 ({pct:.1f}%)\n")
    
    f.write("\n## 三、新增文章列表\n\n")
    
    # 按 ordinal 排序显示
    new_sorted = sorted(
        [r for r in all_records if r['id'] not in v2_ids],
        key=lambda x: x.get('ordinal', 0)
    )
    
    for i, article in enumerate(new_sorted, 1):
        f.write(f"### {i}. {article['title']}\n\n")
        f.write(f"- **Ordinal**: {article.get('ordinal', 'N/A')}\n")
        f.write(f"- **ID**: `{article['id']}`\n")
        
        if 'classification' in article and article['classification']:
            cls = article['classification']
            f.write(f"- **主要主题**: {cls.get('primary', '未分类')}\n")
            if len(cls.get('concepts', [])) > 1:
                other_concepts = cls['concepts'][1:]
                f.write(f"- **相关概念**: {', '.join(other_concepts)}\n")
        
        # 摘要
        text = article.get('text', '')
        if text:
            preview = text[:80] + ('...' if len(text) > 80 else '')
            f.write(f"- **摘要**: {preview}\n")
        
        f.write("\n")

print(f"  报告: {report_path.name}")

# 输出统计
print(f"\n主题分布（Top 10）:")
for concept, count in sorted(concept_stats.items(), key=lambda x: -x[1])[:10]:
    pct = count / classified_count * 100 if classified_count > 0 else 0
    print(f"  {concept}: {count} 篇 ({pct:.1f}%)")

print(f"\n✅ 任务完成！")
print(f"  - 新分类库: all-articles-merged-v4-clean.jsonl (4,342 篇)")
print(f"  - 分类报告: {report_path.name}")
