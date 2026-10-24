#!/usr/bin/env python3
"""Write the file-backed visual audit for Round150.

All 40 nodes in this round passed transport and PIL decode.  Visual review
does not change article topics; it records whether an image is evidence,
useful illustration, duplicate/weak context, or a source that should be
omitted while retaining the article.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
ROUND = 150
MANIFEST_PATH = REPORTS / f"round{ROUND}-image-manifest.csv"
SELECTION_PATH = REPORTS / f"round{ROUND}-image-selection.csv"
REVIEW_PATH = REPORTS / f"round{ROUND}-image-review.tsv"
DECISION_PATH = REPORTS / f"round{ROUND}-image-decisions.tsv"
INVENTORY_PATH = DATA / "image-inventory.csv"
MANUAL_PATH = DATA / "print-topic-manual-decisions-v2.csv"


LIMITATIONS = (
    "图片来源、发布时间/型号和文字出处未独立核验；视觉复核只能记录图像内容及其与正文的关系，"
    "不能单独证明作者引用的历史、科学、法律、医学或社会因果判断。"
)


# index -> (visible content, relation to text, consistency)
DESCRIPTIONS: dict[str, dict[int, tuple[str, str, str]]] = {
    "各行其道": {
        1: ("户外院落/道路照片，叠加大量红绿线框和中文标注。", "未见猫或野外捕食内容，与正文关于猫出门和野生动物捕猎的中心不对应；更像错配的原文附图。", "weak"),
        2: ("同一类院落/道路照片，叠加箭头、圈线和中文标注。", "仍未见猫或野外捕食内容，不能支持正文判断。", "weak"),
    },
    "悲欣交集": {
        1: ("书法/题字图片，能辨认出‘悲欣交集’字样。", "只重复文章标题和情绪语境，不能解释正文关于脑补疯狂场景的心理判断。", "limited"),
    },
    "印刷信息量": {
        1: ("中文二维码信息容量说明截图，讨论二维码尺寸、容错和容量。", "直接对应正文关于二维码作为高密度物理记录方式的说明；图中文字和出处仍需OCR及来源核验。", "consistent"),
    },
    "张艺谋想你": {
        1: ("影视/综艺画面中的人物仰头喊话。", "可作不辞而别后戏剧化思念的示意，但不是正文论证证据。", "limited"),
        2: ("影视/综艺画面中的人物拿扩音器喊话。", "与正文‘拿大喇叭’的夸张效果图相符，但属装饰性比喻。", "limited"),
    },
    "沙加": {
        1: ("动画风格人物坐姿冥想/闭目形象。", "只提供《圣斗士》沙加的文化语境，不能证明正文的军事或行动判断。", "limited"),
    },
    "尖头鞋": {
        1: ("现代黑色尖头皮鞋产品图。", "可弱对应尖头鞋形态，但不是哥特板甲或马镫结构的直接证据。", "limited"),
        2: ("古装影视中的人物/服饰画面。", "未能确认鞋部结构，与正文的马镫、鞋跟和护腿功能关系不清。", "weak"),
    },
    "核披萨": {
        1: ("手机界面截图，深色画面上有大量黄色和红色手绘圈线、箭头及轨迹标记。", "看不出披萨、核爆热辐射或距离标尺，不能支持正文的热辐射计算；来源和标注含义不明。", "weak"),
    },
    "还魂丹": {
        1: ("多支薄荷/清凉类吸入产品和包装图。", "直接对应正文关于嗅觉刺激、嗅盐和提神物的举例，但不能证明其实际清醒效果。", "consistent"),
        2: ("Peppermint Field 黑色吸入器产品图。", "直接提供正文所说刺激性气味/吸入器的商品语境，型号和成分仍需核验。", "consistent"),
    },
    "华容道": {
        1: ("带曹操、关羽、张飞等人物方块的木制华容道拼图。", "直接构成正文把曹操比作恶习、把其他方块视为系统性问题的核心比喻。", "consistent"),
    },
    "渔隐": {
        1: ("带人物图案的陶制碗/器物。", "正文讨论野钓、食物和野外生存，图像未显示钓鱼、水域或生存操作，关系弱。", "weak"),
    },
    "不可追": {
        1: ("英文网页截图，标题为‘How do you woo a difficult girl?’并列出追求技巧。", "直接提供正文批评的‘追求/改变他人意愿’的实例语境，但网页出处和建议内容未核验。", "consistent"),
    },
    "雨伞": {
        1: ("Fulton 黑色长柄雨伞产品图。", "直接对应正文关于伞骨、长握柄、主棒和品牌建议的对象；商品型号和耐用性未核验。", "consistent"),
    },
    "防不胜防": {
        1: ("中文体育食品管理规定截图，列出运动员不得外食、购买不明食品等要求。", "直接支撑正文关于国家队食品来源、兴奋剂风险和纪律约束的论证入口；法规版本和出处需核验。", "consistent"),
    },
    "锄奸": {
        1: ("带英文字幕的新闻/视频画面，人物谈及俄罗斯军队与平民。", "提供正文讨论俄乌战争、平民立场和‘锄奸’资格的媒体语境，但不能证明正文的战争事实判断。", "limited"),
    },
    "高中书目": {
        1: ("纵向中文书目/读书推荐长截图，含自然史、科学经典、作者和推荐语。", "直接对应正文给高中生推荐自然史科学经典并说明其作为共同事实基础的内容；文字出处和书目准确性需核验。", "consistent"),
    },
    "新手": {
        1: ("大排量摩托车产品/宣传图。", "直接对应正文讨论公升级摩托车重量、动力、坐姿和新手风险的对象。", "consistent"),
        2: ("人在道路上扶持或尝试控制大排量摩托车的照片。", "直接对应正文关于新手低速操控、车身重量和摔车风险的场景；不能证明具体事故概率。", "consistent"),
    },
    "出于恐惧的仇恨": {
        1: ("山路沿悬崖行驶的道路照片。", "对应正文把日本处境比作无法停车、旁有滑坡和深渊的山路，是类比插图而非国家安全证据。", "limited"),
    },
    "橡皮擦": {
        1: ("白底上红色和蓝色的两个‘1’字形图案。", "可视化正文‘用笔写1、用橡皮擦也能写1’的正反操作比喻，但不能证明关于悲观/乐观的心理判断。", "limited"),
    },
    "礼崩乐坏": {
        1: ("《Westworld》剧集海报，中央为仿真人形象。", "与正文把理想社会比作全员NPC的文化类比相符，但不是历史礼乐制度的证据。", "limited"),
    },
    "MINECRAFT": {
        1: ("Minecraft 游戏世界和角色的宣传图。", "直接提供正文把信息流和世界重造比作游戏的文化语境，但不能证明舆论心理机制。", "limited"),
    },
    "摞你命3000": {
        1: ("影视画面字幕：‘每件都是独当一面的，现在集合一起，怕了没有？’。", "可弱对应正文反对把不同信仰体系简单合并的比喻，具体影片出处和语境未核验。", "limited"),
    },
    "合谁的理": {
        1: ("一组块根/薯类食物照片。", "直接对应正文以南北方地瓜口味差异说明同词不同义的例子。", "consistent"),
        2: ("切开的橙色薯类食物照片。", "继续对应正文关于甜度、食用方式和地域定义差异的类比。", "consistent"),
    },
    "正当防卫门槛": {
        1: ("大型赌场/博彩大厅，桌台和人群密集。", "直接对应正文把正当防卫门槛下降比作下注和链式加码的类比，但不是法律证据。", "limited"),
        2: ("另一张赌场大厅和赌桌人群照片。", "重复强化下注类比，未提供新的法律信息；可与图1择一。", "limited"),
    },
    "对错了": {
        1: ("印象派港口/日出绘画，画面有水面、船和红日。", "直接对应正文用画家、题材和‘画得对不对’说明跨领域思考的艺术语境；不能证明全才能力。", "limited"),
    },
    "西施": {
        1: ("从猿类到现代人的演化序列插图。", "提供正文讨论性选择、形态和人类审美机制的进化语境；图源和演化简化方式未核验。", "consistent"),
        2: ("史前女性雕像/‘维纳斯’类图像及说明文字。", "直接对应正文关于雌性形态、审美和史前人类的例子；文字与年代判断需独立核验。", "consistent"),
    },
    "拍蒜": {
        1: ("手绘刀具/砧板和受力方向示意图。", "直接对应正文关于拍蒜时刀面、砧板、受力和避免刀头触地的操作解释。", "consistent"),
    },
    "高粘液体": {
        1: ("聚合物/局部结晶与交联结构的化学示意和显微图。", "直接对应正文关于高分子链、结晶、交联和是否可视为液体的论证。", "consistent"),
        2: ("剪切流动中聚合物链逐步取向/结晶的示意图。", "直接对应正文关于时间柔性体、内部运动和剪切下结构变化的技术语境。", "consistent"),
    },
    "伊斯兰女性": {
        1: ("中文资料截图，标题为‘伊斯兰女性主义的发展’，讨论早期改革、继承权、财产权和婚姻。", "直接对应正文关于伊斯兰教法早期女性继承/财产权及历史比较的材料入口；截图出处和译引需核验。", "consistent"),
        2: ("中文资料截图，标题为‘妇女继承权’，列出伊斯兰继承规则和男女继承份额。", "直接对应正文关于继承权与财产权的论证，但图中文字不能单独证明历史普遍性。", "consistent"),
    },
    "写实": {
        1: ("湖面、栈桥、山体、热带植物、天鹅和建筑的三维渲染图。", "正文逐项检查桥桩、木材、植被、气候、水位、天鹅和结构稳定性；该图就是被分析的对象。", "consistent"),
    },
    "渐行渐远": {
        1: ("红色波形随时间起伏，并以圆圈和箭头放大其中一段周期的示意图。", "直接对应正文把朋友互动强度描述为长周期波动、并区分周期下行与永久归零的模型。", "consistent"),
    },
}


ARTICLE_DECISIONS = {
    "各行其道": "retain_article_image_omit",
    "悲欣交集": "retain_article_image_omit",
    "印刷信息量": "retain_article_image_required",
    "张艺谋想你": "retain_article_image_optional",
    "沙加": "retain_article_image_optional",
    "尖头鞋": "retain_article_image_optional",
    "核披萨": "retain_article_image_omit",
    "还魂丹": "retain_article_image_required_or_selected",
    "华容道": "retain_article_image_required",
    "渔隐": "retain_article_image_omit",
    "不可追": "retain_article_image_optional",
    "雨伞": "retain_article_image_required",
    "防不胜防": "retain_article_image_required",
    "锄奸": "retain_article_image_optional",
    "高中书目": "retain_article_image_required",
    "新手": "retain_article_image_required_or_selected",
    "出于恐惧的仇恨": "retain_article_image_optional",
    "橡皮擦": "retain_article_image_optional",
    "礼崩乐坏": "retain_article_image_optional",
    "MINECRAFT": "retain_article_image_optional",
    "摞你命3000": "retain_article_image_optional",
    "合谁的理": "retain_article_image_required_or_selected",
    "正当防卫门槛": "retain_article_image_optional",
    "对错了": "retain_article_image_optional",
    "西施": "retain_article_image_required_or_selected",
    "拍蒜": "retain_article_image_required",
    "高粘液体": "retain_article_image_required_or_selected",
    "伊斯兰女性": "retain_article_image_required_or_selected",
    "写实": "retain_article_image_required",
    "渐行渐远": "retain_article_image_required_or_selected",
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
    selection = {row["id"]: row for row in read(SELECTION_PATH)}
    assert len(manifest) == 40, len(manifest)
    assert all(row.get("download_status") == "success" for row in manifest)
    assert all(row.get("title") in DESCRIPTIONS for row in manifest)

    reviews = []
    for row in manifest:
        title = row["title"]
        index = int(row["image_index"])
        visible, relation, consistency = DESCRIPTIONS[title][index]
        reviews.append({
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
        })
    review_fields = list(reviews[0])
    write(REVIEW_PATH, review_fields, reviews)

    # Persist the visual evidence in the long-lived inventory, retaining the
    # original source URL and image node rather than replacing the raw corpus.
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

    # Article-level image retention is separate from the established topic
    # decision.  Use the current manual primary/secondary values unchanged.
    manual = read(MANUAL_PATH)
    manual_by_id = {row["id"]: row for row in manual}
    by_article: dict[str, list[dict[str, str]]] = {}
    for row in reviews:
        by_article.setdefault(row["id"], []).append(row)
    decisions = []
    for article_id, rows in by_article.items():
        title = rows[0]["title"]
        article = manual_by_id[article_id]
        decisions.append({
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
            "basis": "Round150逐图视觉复核完成；文章专题主副码不变，图片保留与文章保留分开决定。",
            "reason": "图像内容、图文关系和必要性已逐节点记录；来源、OCR和正文事实主张仍未独立核验。",
        })
        count = len(rows)
        marker = f"Round150 visual review=reports/round150-image-review.tsv ({count}/{count} reviewed; no topic change)"
        note = article.get("review_note", "").rstrip("; ")
        if marker not in note:
            article["review_note"] = note + ("; " if note else "") + marker + "; image retention is separate; source/OCR/factual claims remain unverified."
        reviewer = article.get("reviewer", "")
        if "round150-image-review" not in reviewer:
            article["reviewer"] = (reviewer + "+round150-image-review").strip("+")
        article["reviewed_at"] = "2026-09-25"

    with MANUAL_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manual[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
    write(DECISION_PATH, list(decisions[0]), decisions)
    print({
        "review_rows": len(reviews),
        "reviewed_rows": sum(row["review_status"] == "reviewed" for row in reviews),
        "article_decision_rows": len(decisions),
        "decision_counts": {value: sum(row["decision"] == value for row in decisions) for value in sorted(set(row["decision"] for row in decisions))},
        "review": str(REVIEW_PATH),
        "decisions": str(DECISION_PATH),
    })


if __name__ == "__main__":
    main()
