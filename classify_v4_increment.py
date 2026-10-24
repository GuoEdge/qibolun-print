#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对v4新增的29篇文章进行主题分类"""
import json
import re
import csv
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).parent
V3_CORPUS = ROOT / "sooon-q9adg-articles-v3.jsonl"
V4_CORPUS = ROOT / "sooon-q9adg-articles-v4.jsonl"
INCREMENT = ROOT / "research/online-increment/sooon-increment-20261009-195354.jsonl"
OUT_REPORT = ROOT / "岐伯论_v4新增29篇分类报告_2026-10-09.md"
OUT_CSV = ROOT / "v4-increment-classification.csv"

CONCEPTS = [
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
]

CUES = {
    "照料与家庭": ["家庭", "父母", "子女", "亲属", "兄弟", "亲戚", "婚姻", "夫妻", "孩子"],
    "爱与回应": ["恋爱", "感情", "伴侣", "分手", "暧昧", "网友", "友谊", "约会", "爱", "关心", "尊重", "回应", "帮助", "关系"],
    "能力与学习": ["学习", "教育", "能力", "知识", "读书", "学校", "训练", "经验"],
    "劳动与组织": ["工作", "职场", "同事", "公司", "组织", "管理", "团队", "招聘"],
    "财富与市场": ["钱", "财富", "收入", "借贷", "投资", "消费", "市场", "买", "卖"],
    "法律与秩序": ["法律", "犯罪", "诈骗", "刑罚", "警察", "司法", "违法", "安全"],
    "权力与异议": ["权力", "政府", "政治", "官员", "制度", "阶层", "统治", "异议"],
    "技术与工程": ["技术", "工程", "软件", "互联网", "平台", "算法", "设备"],
    "人工智能与机器": ["人工智能", "AI", "机器学习", "机器人", "生成式", "大语言模型", "自动驾驶"],
    "性别与身体": ["女性", "男性", "性别", "身体", "生育", "性关系", "怀孕", "同意"],
    "心理与主体": ["心理", "情绪", "焦虑", "抑郁", "孤独", "性格", "自我", "精神"],
    "生态与自然": ["自然", "生态", "气候", "环境", "能源", "动物", "植物", "天气"],
    "文明与历史": ["历史", "文明", "社会", "文化", "民族", "国家", "古代", "传统"],
    "事实与证据": ["事实", "证据", "数据", "研究", "统计", "为什么", "原因", "证明"],
    "定义与达意": ["意思", "定义", "概念", "区别", "如何理解", "所谓"],
    "选择与自由": ["选择", "自由", "决定", "要不要", "是否应该", "怎么办"],
    "责任与后果": ["责任", "后果", "风险", "代价", "承担", "应该"],
    "成本与总账": ["成本", "收益", "代价", "投入", "回报", "效率"],
    "信用与信任": ["信任", "信用", "可靠", "欺骗", "诚实", "背叛"],
    "边界与许可": ["边界", "拒绝", "隐私", "许可", "限制", "规则", "安全"],
    "净输出与不掠夺": ["掠夺", "剥削", "伤害", "占用", "公平", "互惠"],
    "宗教与自然法": ["宗教", "信仰", "道德", "正义", "自然法", "神"],
}

def classify_article(article):
    """对单篇文章进行分类"""
    # 合并标题、问题、简介、正文
    text = " ".join([
        article.get("title", ""),
        article.get("question", ""),
        article.get("brief", ""),
        article.get("text", "")
    ])
    
    scores = {concept: 0 for concept in CONCEPTS}
    matched = {}
    
    for concept, cues in CUES.items():
        for cue in cues:
            # 统计关键词出现次数，最多计3次
            hits = min(len(re.findall(re.escape(cue), text, flags=re.I)), 3)
            if hits:
                scores[concept] += hits
                matched.setdefault(concept, []).append(f"{cue}({hits})")
    
    # 按分数降序排序，取前6个
    ranked = [
        (c, score) 
        for c, score in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])) 
        if score > 0
    ][:6]
    
    concepts = [c for c, _ in ranked]
    primary = concepts[0] if concepts else ""
    
    return {
        "concepts": concepts,
        "primary": primary,
        "scores": scores,
        "matched": matched,
        "top_score": ranked[0][1] if ranked else 0,
        "concept_count": len(concepts)
    }

def main():
    # 加载v3语料库ID集合
    v3_ids = set()
    with V3_CORPUS.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                v3_ids.add(str(item["id"]))
    
    print(f"v3语料库：{len(v3_ids)} 篇")
    
    # 加载增量文件并分类
    new_articles = []
    with INCREMENT.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                article = json.loads(line)
                article_id = str(article["id"])
                
                # 只处理新文章
                if article_id not in v3_ids:
                    classification = classify_article(article)
                    new_articles.append({
                        "article": article,
                        "classification": classification
                    })
    
    print(f"新增文章：{len(new_articles)} 篇")
    
    # 统计主题分布
    primary_counter = Counter()
    for item in new_articles:
        primary = item["classification"]["primary"]
        if primary:
            primary_counter[primary] += 1
    
    # 生成CSV
    csv_rows = []
    for i, item in enumerate(new_articles, 1):
        article = item["article"]
        cls = item["classification"]
        
        csv_rows.append({
            "序号": i,
            "id": article["id"],
            "标题": article["title"],
            "发布日期": article["publishedAt"],
            "主要主题": cls["primary"],
            "相关主题": ";".join(cls["concepts"]),
            "主题数量": cls["concept_count"],
            "最高分": cls["top_score"],
            "字数": len(article.get("text", "")),
            "URL": article["url"]
        })
    
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        if csv_rows:
            writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
            writer.writeheader()
            writer.writerows(csv_rows)
    
    print(f"✓ CSV已写入：{OUT_CSV}")
    
    # 生成Markdown报告
    with OUT_REPORT.open("w", encoding="utf-8") as f:
        f.write("# 岐伯论 v4 新增29篇文章分类报告\n\n")
        f.write(f"**生成时间**：2026-10-09 19:53\n\n")
        f.write(f"**语料库版本**：v3 → v4\n\n")
        f.write(f"**新增文章数量**：{len(new_articles)} 篇\n\n")
        
        f.write("## 一、主题分布统计\n\n")
        f.write("| 主题 | 文章数 | 占比 |\n")
        f.write("|------|--------|------|\n")
        
        for concept, count in primary_counter.most_common():
            pct = count / len(new_articles) * 100
            f.write(f"| {concept} | {count} | {pct:.1f}% |\n")
        
        if len(new_articles) - sum(primary_counter.values()) > 0:
            unclassified = len(new_articles) - sum(primary_counter.values())
            pct = unclassified / len(new_articles) * 100
            f.write(f"| （未分类） | {unclassified} | {pct:.1f}% |\n")
        
        f.write("\n## 二、分类详情\n\n")
        
        for i, item in enumerate(new_articles, 1):
            article = item["article"]
            cls = item["classification"]
            
            f.write(f"### {i}. {article['title']}\n\n")
            f.write(f"- **ID**：`{article['id']}`\n")
            f.write(f"- **发布日期**：{article['publishedAt']}\n")
            f.write(f"- **字数**：{len(article.get('text', ''))} 字\n")
            f.write(f"- **URL**：{article['url']}\n")
            f.write(f"- **主要主题**：**{cls['primary']}**\n")
            
            if len(cls['concepts']) > 1:
                f.write(f"- **相关主题**：{', '.join(cls['concepts'][1:])}\n")
            
            # 显示匹配的关键词（仅前3个主题）
            if cls['matched']:
                f.write(f"- **关键词匹配**：\n")
                for concept in cls['concepts'][:3]:
                    if concept in cls['matched']:
                        cues = cls['matched'][concept][:5]  # 最多显示5个
                        f.write(f"  - {concept}：{', '.join(cues)}\n")
            
            f.write("\n")
        
        f.write("## 三、总结\n\n")
        f.write(f"本次从素问网站抓取到 {len(new_articles)} 篇新文章，")
        f.write(f"已全部完成主题分类。主要集中在以下领域：\n\n")
        
        top3 = primary_counter.most_common(3)
        for concept, count in top3:
            f.write(f"- **{concept}**：{count} 篇\n")
        
        f.write(f"\n语料库已从 v3（4342篇）更新至 v4（4371篇）。\n")
    
    print(f"✓ 报告已写入：{OUT_REPORT}")
    
    # 打印摘要
    print("\n=== 主题分布 ===")
    for concept, count in primary_counter.most_common():
        print(f"{concept}: {count} 篇")

if __name__ == "__main__":
    main()
