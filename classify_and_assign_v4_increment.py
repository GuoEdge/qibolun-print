#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""深度阅读v4新增29篇文章，准确分配到对应卷册"""
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
INCREMENT = ROOT / "research/online-increment/sooon-increment-20261009-195354.jsonl"
CATALOG = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl"
V3_CORPUS = ROOT / "sooon-q9adg-articles-v3.jsonl"
OUTPUT_ASSIGNMENT = ROOT / "v4_increment_assignment_2026-10-09.jsonl"
OUTPUT_REPORT = ROOT / "v4增量分册详细分析_2026-10-09.md"

# 卷册定义（从catalog提取）
BOOKLET_DEFS = {
    # 卷一：本根敦倫——血亲宗族与家庭抚育
    "B02": {"name": "学业功课与学校日常", "volume": "V1", "keywords": ["学校", "学习", "考试", "作业", "老师", "同学", "学生", "教育", "班级"]},
    "B03": {"name": "言传身教与奖惩边界", "volume": "V1", "keywords": ["教育", "管教", "奖惩", "规矩", "言传身教", "父母", "孩子"]},
    "B04": {"name": "亲子沟通与青春叛逆", "volume": "V1", "keywords": ["叛逆", "青春期", "沟通", "理解", "父母", "孩子", "代沟"]},
    "B05": {"name": "父母控制欲与精神解绑", "volume": "V1", "keywords": ["控制", "独立", "自主", "摆脱", "父母", "压力"]},
    "B06": {"name": "成年子女自立与边界", "volume": "V1", "keywords": ["成年", "独立", "自立", "边界", "父母", "啃老", "自己"]},
    "B07": {"name": "隔代教养与长辈相处", "volume": "V1", "keywords": ["爷爷", "奶奶", "外公", "外婆", "隔代", "长辈", "老人"]},
    "B08": {"name": "手足同胞与家族亲戚", "volume": "V1", "keywords": ["兄弟", "姐妹", "亲戚", "家族", "堂兄", "表妹", "手足"]},
    "B09": {"name": "家族传承与家风家范", "volume": "V1", "keywords": ["传承", "家风", "家训", "祖辈", "家族", "传统"]},
    "B10": {"name": "临终关怀与白事奠仪", "volume": "V1", "keywords": ["去世", "葬礼", "奠仪", "临终", "丧事", "悼念", "死亡"]},
    
    # 卷二：阴阳合离——两性亲密与婚恋博弈
    "B11": {"name": "择偶标准与两性吸引", "volume": "V2", "keywords": ["择偶", "恋爱", "吸引", "相亲", "找对象", "喜欢"]},
    "B12": {"name": "婚姻存续与夫妻日常", "volume": "V2", "keywords": ["夫妻", "婚姻", "老公", "老婆", "伴侣", "配偶"]},
    "B13": {"name": "亲密背叛与离异止损", "volume": "V2", "keywords": ["出轨", "背叛", "离婚", "分手", "第三者", "外遇"]},
    
    # 卷三：酬酢防身——人际交往与危机应对
    "B14": {"name": "人情往来与礼数分寸", "volume": "V3", "keywords": ["人情", "礼物", "送礼", "客套", "礼数", "往来"]},
    "B15": {"name": "社交距离与孤立自处", "volume": "V3", "keywords": ["社交", "独处", "孤独", "朋友", "交际", "社恐"]},
    "B16": {"name": "危机识人与权义守界", "volume": "V3", "keywords": ["识人", "防范", "警惕", "危险", "权利", "界限"]},
    
    # 卷四：存神调息——身心安顿与心性知行
    "B17": {"name": "情志平复与容貌自和", "volume": "V4", "keywords": ["情绪", "心理", "焦虑", "抑郁", "压力", "心情", "精神", "自我", "内心"]},
    "B18": {"name": "作息节律与病理常识", "volume": "V4", "keywords": ["睡眠", "作息", "健康", "疾病", "身体", "医疗"]},
    "B19": {"name": "知行精进与克服拖延", "volume": "V4", "keywords": ["拖延", "效率", "行动", "执行", "目标", "自律"]},
    
    # 卷五：度势居货——职场生态与财富经营
    "B20A": {"name": "职场汇报与权责留痕", "volume": "V5", "keywords": ["工作", "职场", "领导", "同事", "汇报", "责任", "职责"]},
    "B21": {"name": "体制生存与职业自保", "volume": "V5", "keywords": ["体制", "单位", "公务员", "国企", "职业", "自保"]},
    "B22": {"name": "商业竞争与资产投资", "volume": "V5", "keywords": ["商业", "投资", "创业", "生意", "资产", "财富", "赚钱"]},
    
    # 卷六：观风察变——时代透视与群体思潮
    "B23": {"name": "公共热点与事件剖析", "volume": "V6", "keywords": ["新闻", "热点", "事件", "社会", "现象", "评价"]},
    "B24": {"name": "青年心境与躺平反思", "volume": "V6", "keywords": ["躺平", "内卷", "青年", "年轻人", "迷茫", "困境"]},
    "B25": {"name": "网络生态与群体极化", "volume": "V6", "keywords": ["网络", "互联网", "社交媒体", "网民", "舆论", "极化"]},
    "B26": {"name": "性别议题与两性舆论", "volume": "V6", "keywords": ["性别", "女性", "男性", "女权", "两性", "性别议题"]},
    "B27": {"name": "教育体制与社会流动", "volume": "V6", "keywords": ["教育体制", "高考", "学历", "阶层", "流动", "寒门"]},
    "B28": {"name": "消费主义与生活观念", "volume": "V6", "keywords": ["消费", "购物", "生活", "品质", "消费主义", "物质"]},
    "B29": {"name": "现代科技与工具反思", "volume": "V6", "keywords": ["科技", "技术", "AI", "人工智能", "互联网", "工具", "科学"]},
    "B30": {"name": "文明演进与社会秩序", "volume": "V6", "keywords": ["文明", "历史", "社会", "秩序", "演进", "发展"]},
    
    # 卷七：涤除玄览——深层哲思与名相辨析
    "B31A": {"name": "存在本质与生命意义", "volume": "V7", "keywords": ["存在", "意义", "生命", "本质", "哲学", "价值", "为什么活着"]},
    "B32": {"name": "名相辨析与语言牢笼", "volume": "V7", "keywords": ["定义", "概念", "意思", "区别", "如何理解", "所谓", "什么是"]},
    "B33": {"name": "善恶分野与伦理底线", "volume": "V7", "keywords": ["善恶", "道德", "伦理", "正义", "底线", "是非"]},
    "B34": {"name": "认识局限与心智模型", "volume": "V7", "keywords": ["认知", "思维", "局限", "偏见", "理解", "智慧", "思考"]},
    "B35": {"name": "命途因果与得失随缘", "volume": "V7", "keywords": ["命运", "因果", "得失", "随缘", "福报", "运气"]},
    "B36": {"name": "人性幽微与双重人格", "volume": "V7", "keywords": ["人性", "性格", "人格", "心理", "本性", "双重"]},
    "B37": {"name": "神圣敬畏与信仰维度", "volume": "V7", "keywords": ["信仰", "宗教", "神", "敬畏", "信念", "超越"]},
    
    # 卷八：鉴往铸器——艺文美学与历史治乱
    "B01": {"name": "艺能创作与生活美学", "volume": "V8", "keywords": ["艺术", "美学", "创作", "文学", "音乐", "绘画", "审美", "艺能"]}
}

def deep_analyze_article(article):
    """深度分析单篇文章，返回最合适的booklet"""
    article_id = article["id"]
    title = article["title"]
    question = article.get("question", "")
    brief = article.get("brief", "")
    text = article.get("text", "")
    
    # 合并所有文本
    full_text = f"{title} {question} {brief} {text}"
    
    print(f"\n{'='*80}")
    print(f"【{title}】")
    print(f"ID: {article_id}")
    print(f"问题: {question[:100]}..." if len(question) > 100 else f"问题: {question}")
    print(f"字数: {len(text)}")
    print(f"\n正文预览:")
    print(text[:300] + "..." if len(text) > 300 else text)
    
    # 计算每个册的匹配分数
    scores = {}
    matches = {}
    
    for booklet_code, info in BOOKLET_DEFS.items():
        score = 0
        matched_keywords = []
        
        for keyword in info["keywords"]:
            count = full_text.count(keyword)
            if count > 0:
                score += count
                matched_keywords.append(f"{keyword}({count})")
        
        if score > 0:
            scores[booklet_code] = score
            matches[booklet_code] = matched_keywords
    
    # 按分数排序
    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    
    print(f"\n匹配分析（Top 5）:")
    for i, (booklet_code, score) in enumerate(ranked[:5], 1):
        info = BOOKLET_DEFS[booklet_code]
        keywords_str = ", ".join(matches[booklet_code][:5])
        print(f"  {i}. {booklet_code} {info['name']} (分数:{score})")
        print(f"     {info['volume']} · 关键词: {keywords_str}")
    
    if not ranked:
        print("  ⚠️ 未找到明确匹配，需要人工判断")
        return None, None, {}
    
    # 返回最佳匹配
    best_booklet = ranked[0][0]
    best_score = ranked[0][1]
    
    return best_booklet, best_score, matches

def main():
    # 加载v3语料库ID集合
    v3_ids = set()
    with V3_CORPUS.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                v3_ids.add(str(item["id"]))
    
    print(f"v3语料库：{len(v3_ids)} 篇\n")
    
    # 加载增量文件
    new_articles = []
    with INCREMENT.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                article = json.loads(line)
                article_id = str(article["id"])
                
                # 只处理新文章
                if article_id not in v3_ids:
                    new_articles.append(article)
    
    print(f"新增文章：{len(new_articles)} 篇")
    print(f"{'='*80}\n")
    print("开始深度分析...")
    
    # 分析每篇文章
    assignments = []
    for i, article in enumerate(new_articles, 1):
        print(f"\n进度: {i}/{len(new_articles)}")
        
        booklet_code, score, matches = deep_analyze_article(article)
        
        if booklet_code:
            booklet_info = BOOKLET_DEFS[booklet_code]
            assignment = {
                "article_id": article["id"],
                "title": article["title"],
                "booklet_code": booklet_code,
                "booklet_name": booklet_info["name"],
                "volume_code": booklet_info["volume"],
                "match_score": score,
                "matched_keywords": matches.get(booklet_code, []),
                "url": article["url"],
                "text_len": len(article.get("text", "")),
                "published_at": article["publishedAt"]
            }
        else:
            assignment = {
                "article_id": article["id"],
                "title": article["title"],
                "booklet_code": "UNASSIGNED",
                "booklet_name": "待人工分配",
                "volume_code": "UNKNOWN",
                "match_score": 0,
                "matched_keywords": [],
                "url": article["url"],
                "text_len": len(article.get("text", "")),
                "published_at": article["publishedAt"]
            }
        
        assignments.append(assignment)
        
        print(f"\n>>> 分配结果: {assignment['booklet_code']} - {assignment['booklet_name']}")
    
    # 写入分配结果
    with OUTPUT_ASSIGNMENT.open("w", encoding="utf-8") as f:
        for assignment in assignments:
            f.write(json.dumps(assignment, ensure_ascii=False, separators=(',', ':')) + "\n")
    
    print(f"\n{'='*80}")
    print(f"✓ 分配结果已写入：{OUTPUT_ASSIGNMENT}")
    
    # 生成详细报告
    from collections import Counter
    booklet_counter = Counter(a["booklet_code"] for a in assignments)
    volume_counter = Counter(a["volume_code"] for a in assignments)
    
    with OUTPUT_REPORT.open("w", encoding="utf-8") as f:
        f.write("# v4增量29篇文章分册详细分析\n\n")
        f.write(f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**文章数量**：{len(assignments)} 篇\n\n")
        
        f.write("## 一、分卷统计\n\n")
        f.write("| 卷代码 | 文章数 |\n")
        f.write("|--------|--------|\n")
        for vol in sorted(volume_counter.keys()):
            count = volume_counter[vol]
            f.write(f"| {vol} | {count} |\n")
        
        f.write("\n## 二、分册统计\n\n")
        f.write("| 册代码 | 册名 | 文章数 |\n")
        f.write("|--------|------|--------|\n")
        for booklet in sorted(booklet_counter.keys()):
            count = booklet_counter[booklet]
            name = BOOKLET_DEFS.get(booklet, {}).get("name", "未知")
            f.write(f"| {booklet} | {name} | {count} |\n")
        
        f.write("\n## 三、详细分配清单\n\n")
        
        # 按卷分组
        by_volume = {}
        for assignment in assignments:
            vol = assignment["volume_code"]
            if vol not in by_volume:
                by_volume[vol] = []
            by_volume[vol].append(assignment)
        
        for vol in sorted(by_volume.keys()):
            f.write(f"### {vol}\n\n")
            
            for assignment in by_volume[vol]:
                f.write(f"#### {assignment['title']}\n\n")
                f.write(f"- **ID**: `{assignment['article_id']}`\n")
                f.write(f"- **分配至**: {assignment['booklet_code']} - {assignment['booklet_name']}\n")
                f.write(f"- **匹配分数**: {assignment['match_score']}\n")
                if assignment['matched_keywords']:
                    keywords_str = ", ".join(assignment['matched_keywords'][:10])
                    f.write(f"- **匹配关键词**: {keywords_str}\n")
                f.write(f"- **字数**: {assignment['text_len']}\n")
                f.write(f"- **URL**: {assignment['url']}\n")
                f.write("\n")
    
    print(f"✓ 详细报告已写入：{OUTPUT_REPORT}")
    
    # 打印摘要
    print(f"\n{'='*80}")
    print("分配摘要:")
    print(f"\n分卷分布:")
    for vol in sorted(volume_counter.keys()):
        print(f"  {vol}: {volume_counter[vol]}篇")
    
    print(f"\n分册分布 (Top 10):")
    for booklet, count in booklet_counter.most_common(10):
        name = BOOKLET_DEFS.get(booklet, {}).get("name", "未知")
        print(f"  {booklet} {name}: {count}篇")

if __name__ == "__main__":
    main()
