#!/usr/bin/env python3
"""Write the verified visual audit for Round151.

Round151 contains 41 successfully downloaded and PIL-decoded image nodes from
20 articles.  The audit records image-to-body relevance independently from
article retention and never changes an article's print-topic assignment.
"""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild" / "reports"
DATA = ROOT / "research-rebuild" / "data"
ROUND = 151
MANIFEST_PATH = REPORTS / f"round{ROUND}-image-manifest.csv"
SELECTION_PATH = REPORTS / f"round{ROUND}-image-selection.csv"
REVIEW_PATH = REPORTS / f"round{ROUND}-image-review.tsv"
DECISION_PATH = REPORTS / f"round{ROUND}-image-decisions.tsv"
INVENTORY_PATH = DATA / "image-inventory.csv"
MANUAL_PATH = DATA / "print-topic-manual-decisions-v2.csv"


LIMITATIONS = (
    "图片来源、截图文字出处、时间/型号、统计口径和外部事实未独立核验；"
    "视觉复核只能判断图像内容及其与正文的关系，不能单独证明作者的历史、科学、法律、医学、"
    "政治或社会因果判断；OCR未完成。"
)


# image_index -> (visible content, relation to body, consistency)
DESCRIPTIONS: dict[str, dict[int, tuple[str, str, str]]] = {
    "辜鸿铭的辫子": {
        1: (
            "英文书页截图，显示《论语》第一章及‘wise and good man’等译文。",
            "正文逐句批评辜鸿铭对‘人不知而不愠’和‘君子’的英译；该截图是文章直接讨论的译文材料。",
            "consistent",
        ),
        2: (
            "倒置的英文网页/电视节目文字截图，内容为公共广播节目介绍。",
            "与正文关于辜鸿铭、论语翻译和学术成就的中心材料不对应，疑似错配附件；不能支持文章判断。",
            "weak",
        ),
    },
    "宗教的意义": {
        1: (
            "人民日报微博截图，报道大连轿车撞人逃逸案件，含死亡和伤者数字。",
            "只能提供社会暴力新闻的语境；正文提到的是另一个案件和电影链接，不能把此图当作正文所述案件的证据。",
            "limited",
        ),
    },
    "执行力": {
        1: (
            "电子游戏主菜单/进度界面截图，含100%完成度等游戏化界面元素。",
            "直接对应正文用游戏进度条解释执行力和进度可视化的比喻，但不能证明工时或管理方法本身有效。",
            "consistent",
        ),
    },
    "三重门": {
        1: (
            "太空舱/宇航员在地球上空的宣传式图像。",
            "正文在这里讨论平流层跳伞和死亡边界，但图像没有清楚显示跳伞或相关纪录，关系较弱；文章不依赖此图。",
            "weak",
        ),
    },
    "镜面不锈钢": {
        1: (
            "中文长截图，题为‘一次道歉赔偿实践’，叙述维修师傅因维修失误向顾客赔偿并改进的案例。",
            "正文在‘这个才是处理这类问题的正确态度’之后直接引用该案例，用来说明公开承认、赔偿和建立信誉的论点。",
            "consistent",
        ),
    },
    "星舰爆炸": {
        1: (
            "按国家列出的2022年全球发射统计表，含美国、中国、俄罗斯、欧洲、印度等成功/失败数量。",
            "正文明确写出‘2022全球发射排行’并据此比较中美、欧盟和印度；属于正文核心图表材料，数据口径仍需核验。",
            "consistent",
        ),
    },
    "玩主": {
        1: (
            "纸板折叠椅、纸板桌和纸材家具/装置的图片集合。",
            "直接例示正文关于简单材料、反复制作和把玩具发展成手艺的论述，也呼应其对纸面结构的讨论。",
            "consistent",
        ),
        2: (
            "纸板家具和再生纸用品的产品/设计拼图。",
            "提供正文所说‘材料简单、手法无穷并有实际用途’的视觉例子；不是儿童玩具安全或教育效果的证据。",
            "consistent",
        ),
        3: (
            "白色折纸/折叠纸材雕塑和家具装置照片。",
            "与正文关于折纸、平面折叠组合结构和持续改进的例子直接对应。",
            "consistent",
        ),
        4: (
            "纸材收纳用品、纸板家具及纸浆/再生材料设计图片集合。",
            "继续展示简单材料的设计潜力，与正文的手艺类玩具和实际用途论点相符；出处未核验。",
            "consistent",
        ),
    },
    "圣木耳": {
        1: (
            "卡通化的僧人/禅者坐像插图。",
            "可提供取经、信仰和宗教人物的泛化语境，但正文的核心是唐玄奘式长期冒险和见证，不是该人物图像。",
            "limited",
        ),
    },
    "厨房清洁策略": {
        1: (
            "一次性木皮船小碟、纸托和木勺图片。",
            "正文在‘一次性器皿’之后直接列举木皮船小碟；图像承担具体用品示例功能。",
            "consistent",
        ),
        2: (
            "黑色、银色一次性酱油碟/塑料碟托盘图片。",
            "直接对应正文列举的一次性酱油碟，用于减少碗碟清洁。",
            "consistent",
        ),
        3: (
            "标有1至7号的不同尺寸纸制烘焙/盛装盒图片。",
            "直接对应正文关于淋膜防油纸盒和按用途选一次性容器的说明。",
            "consistent",
        ),
        4: (
            "多色心形和圆形小盘/碗的商品图片。",
            "对应正文‘装蛋糕的，够少女了吧’的轻松示例，但主要是同类用品展示，不是清洁原理证据。",
            "limited",
        ),
        5: (
            "不同规格、材质和颜色的一次性纸盒/烘焙纸托商品拼图。",
            "继续对应正文的纸盒和一次性盛装策略；图片文字和商品参数尚未核验。",
            "consistent",
        ),
    },
    "兑换银钱的人": {
        1: (
            "欧元兑卢布汇率走势图截图，显示0.0093欧元等数值和时间轴。",
            "正文紧接图后写出‘制裁前0.011，现在已经0.0093’，图表是该段汇率论证的直接材料。",
            "consistent",
        ),
    },
    "大男子主义": {
        1: (
            "恭王府游览示意地图，红框圈出内院/后院区域并标注房屋、门和道路。",
            "正文明确要求读者看红圈内的内院，并以其说明女性活动受限；地图是文章核心历史空间比喻材料。",
            "consistent",
        ),
    },
    "自下人一等": {
        1: (
            "一名戴眼镜、留胡须男子的肖像照片。",
            "位于正文‘下面这是同一个人’之后，作为A/B外貌比较的第一张图；身份、是否同一人及前后关系未核验。",
            "consistent",
        ),
        2: (
            "一名穿黑衬衫男子的正式肖像照片。",
            "位于正文A/B比较的第二张图，用来展示整理外貌、发型和衣着后的视觉差异；不能证明吸引力结论。",
            "consistent",
        ),
        3: (
            "纵向视频截图，拼列多名男性肖像和女性评价反应，并带中英文字幕。",
            "补充正文关于外貌评价和‘帅’的视觉语境；视频出处、人物身份和字幕语境未核验。",
            "limited",
        ),
    },
    "精武门": {
        1: (
            "民国/武术题材影视剧照，多人穿制服或传统服装站在一起。",
            "正文以‘看上去大概是这样’描述严于律己、宽以待人的强者形象，剧照可作文化类比，但不是人格或能力证据。",
            "limited",
        ),
    },
    "评价表现": {
        1: (
            "新加坡新冠新增病例/七日均值曲线截图。",
            "正文逐一比较新加坡、比利时、东京、香港和上海的疫情峰值；该图是直接比较材料。",
            "consistent",
        ),
        2: (
            "比利时新冠新增病例/七日均值曲线截图。",
            "对应正文列出的比利时基线，支持数量级比较；数据时间、来源和统计口径仍需核验。",
            "consistent",
        ),
        3: (
            "东京新冠新增病例/七日均值曲线截图。",
            "对应正文列出的东京基线，支持数量级比较；不能单独证明治理能力结论。",
            "consistent",
        ),
        4: (
            "香港新冠新增病例/七日均值曲线截图。",
            "对应正文列出的香港基线，支持数量级比较；来源和时间范围仍需核验。",
            "consistent",
        ),
        5: (
            "中国大陆上海新冠新增病例/七日均值曲线截图。",
            "对应正文列出的上海结果，和前四张一起构成‘有效基线’比较；数据口径不能由截图单独确认。",
            "consistent",
        ),
    },
    "气泡膜": {
        1: (
            "手指捏压气泡膜的近景照片。",
            "直接把正文‘把假装甘于平庸的人当减压玩具、挨个捏爆’的比喻视觉化；不构成心理学证据。",
            "limited",
        ),
        2: (
            "与图1几乎相同的捏气泡膜照片。",
            "重复同一比喻，未增加正文信息；可视为重复图片，保留一张即可。",
            "weak",
        ),
    },
    "学英语": {
        1: (
            "非洲高档餐厅视频缩略图，字幕称遇到总统。",
            "对应正文关于小语种/中文人才在一带一路国家获得跨文化机会的想象，但视频内容和人物身份未核验。",
            "limited",
        ),
        2: (
            "在阿富汗国家会议/室内场景中的中文旅行视频截图。",
            "提供正文所说海外交往和接触当地权力人物的语境；不能证明英语教育政策或就业规模判断。",
            "limited",
        ),
        3: (
            "标注‘2700000平方米豪宅’的非洲富豪/房产视频缩略图。",
            "可作正文关于当地豪强、财富和海外机会的语境插图，来源与数字未核验。",
            "limited",
        ),
        4: (
            "非洲村落参观视频截图，字幕提到当地家庭和环境。",
            "对应正文关于到海外小城市/部落建立联系的叙述，但不支持其宏观外贸和语言需求判断。",
            "limited",
        ),
    },
    "开心": {
        1: (
            "手扶拖拉机/手摇启动视频截图，带中文视频标题和播放界面。",
            "插在正文‘两冲程循环’和‘冷启动’之后，直接把发动机冷启动作为比喻视觉化；不是快乐机制的实证。",
            "limited",
        ),
    },
    "怀疑与猜疑": {
        1: (
            "扫雷游戏界面截图，显示数字、雷区和已标记格子。",
            "正文明确把有效怀疑比作扫雷，图片是该方法论比喻的直接视觉示例。",
            "consistent",
        ),
    },
    "无目的": {
        1: (
            "手机截图，正文句子被红色手绘圈线和箭头标注。",
            "插在‘settle’段落后，用标注图示说明亲密关系中固定形状/勉强匹配的逻辑；文字与标注关系需OCR核对。",
            "consistent",
        ),
        2: (
            "另一张带红色标注的手机截图，圈出‘接受可能性’等关系定义。",
            "插在‘果冻’比喻后，直接辅助说明接受可能性和同意边界；不能替代正文定义。",
            "consistent",
        ),
    },
    "直升珠峰": {
        1: (
            "直升机在高山积雪和强风中悬停/飞行的照片。",
            "直接对应正文关于珠峰风、积雪、悬停和下人风险的讨论。",
            "consistent",
        ),
        2: (
            "直升机在雪峰上空飞行的远景照片。",
            "直接提供正文讨论高海拔飞行和雪坡环境的视觉对象；不能单独证明可安全下人。",
            "consistent",
        ),
        3: (
            "YouTube页面截图，标题为‘World Record - Mount Everest AS350 B3 landing’，含8850米记录和来源链接。",
            "正文PS段明确讨论该珠峰直升机‘着陆’视频；截图是作者反驳‘可安全下人’时引用的材料。",
            "consistent",
        ),
    },
}


ARTICLE_DECISIONS = {
    "辜鸿铭的辫子": "retain_article_image_required_or_selected",
    "宗教的意义": "retain_article_image_optional",
    "执行力": "retain_article_image_optional",
    "三重门": "retain_article_image_optional",
    "镜面不锈钢": "retain_article_image_required",
    "星舰爆炸": "retain_article_image_required",
    "玩主": "retain_article_image_required_or_selected",
    "圣木耳": "retain_article_image_optional",
    "厨房清洁策略": "retain_article_image_required_or_selected",
    "兑换银钱的人": "retain_article_image_required",
    "大男子主义": "retain_article_image_required",
    "自下人一等": "retain_article_image_required_or_selected",
    "精武门": "retain_article_image_optional",
    "评价表现": "retain_article_image_required",
    "气泡膜": "retain_article_image_optional",
    "学英语": "retain_article_image_optional",
    "开心": "retain_article_image_required_or_selected",
    "怀疑与猜疑": "retain_article_image_required_or_selected",
    "无目的": "retain_article_image_required_or_selected",
    "直升珠峰": "retain_article_image_required",
}


def read(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = "\t") -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    manifest = read(MANIFEST_PATH)
    selection = read(SELECTION_PATH)
    selection_ids = {row["id"] for row in selection}
    assert len(manifest) == 41, len(manifest)
    assert sum(int(row.get("image_count") or 0) for row in selection) == 41
    assert all(row.get("download_status") == "success" for row in manifest)
    assert all(row.get("title") in DESCRIPTIONS for row in manifest)
    assert {row["id"] for row in manifest} == selection_ids

    reviews = []
    for row in manifest:
        title = row["title"]
        index = int(row["image_index"])
        visible, relation, consistency = DESCRIPTIONS[title][index]
        reviews.append(
            {
                "ordinal": row["ordinal"],
                "id": row["id"],
                "title": title,
                "image_index": row["image_index"],
                "local_file": row["local_file"],
                "download_status": row["download_status"],
                "visible_content": visible,
                "relation_to_text": relation,
                "changes_topic_judgment": "no",
                "image_text_consistency": consistency,
                "limitations": LIMITATIONS,
                "review_status": "reviewed",
                "review_date": "2026-09-25",
                "ocr_status": "not_started",
            }
        )

    review_fields = list(reviews[0])
    write(REVIEW_PATH, review_fields, reviews)

    # Persist the review in the long-lived image inventory without touching the
    # raw JSONL corpus.
    inventory = read(INVENTORY_PATH)
    review_by_key = {(row["id"], row["image_index"]): row for row in reviews}
    for row in inventory:
        item = review_by_key.get((row.get("id", ""), row.get("image_index", "")))
        if item:
            row["status"] = "reviewed"
            row["ocr_status"] = "not_started"
            row["notes"] = (
                f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；"
                f"限制：{LIMITATIONS}；视觉复核完成；OCR未核验。"
            )
    inventory_fields = list(inventory[0])
    with INVENTORY_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=inventory_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(inventory)

    manual = read(MANUAL_PATH)
    manual_by_id = {row["id"]: row for row in manual}
    by_article: dict[str, list[dict[str, str]]] = {}
    for row in reviews:
        by_article.setdefault(row["id"], []).append(row)

    decisions = []
    for article_id, rows in by_article.items():
        title = rows[0]["title"]
        article = manual_by_id[article_id]
        decisions.append(
            {
                "id": article_id,
                "title": title,
                "primary_before": article.get("primary_print_topic_code", ""),
                "secondary_before": article.get("secondary_print_topic_codes", ""),
                "primary_after": article.get("primary_print_topic_code", ""),
                "secondary_after": article.get("secondary_print_topic_codes", ""),
                "primary_changed": "no",
                "secondary_changed": "no",
                "final_status": article.get("classification_status", ""),
                "decision": ARTICLE_DECISIONS[title],
                "basis": "Round151逐图视觉复核完成；文章专题主副码不变，图片保留与文章保留分开决定。",
                "reason": "图像内容、图文关系和必要性已逐节点记录；来源、OCR和正文事实主张仍未独立核验。",
            }
        )
        count = len(rows)
        marker = f"Round151 visual review=reports/round151-image-review.tsv ({count}/{count} reviewed; no topic change)"
        note = article.get("review_note", "").rstrip("; ")
        if marker not in note:
            article["review_note"] = note + ("; " if note else "") + marker + "; image retention is separate; source/OCR/factual claims remain unverified."
        reviewer = article.get("reviewer", "")
        if "round151-image-review" not in reviewer:
            article["reviewer"] = (reviewer + "+round151-image-review").strip("+")
        article["reviewed_at"] = "2026-09-25"

    with MANUAL_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manual[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)

    write(DECISION_PATH, list(decisions[0]), decisions)
    print(
        {
            "review_rows": len(reviews),
            "reviewed_rows": sum(row["review_status"] == "reviewed" for row in reviews),
            "article_decision_rows": len(decisions),
            "decision_counts": {value: sum(row["decision"] == value for row in decisions) for value in sorted(set(row["decision"] for row in decisions))},
            "review": str(REVIEW_PATH),
            "decisions": str(DECISION_PATH),
        }
    )


if __name__ == "__main__":
    main()
