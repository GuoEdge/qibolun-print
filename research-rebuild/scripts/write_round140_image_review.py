#!/usr/bin/env python3
"""Write the audited visual review for the mixed-success Round140 batch.

Round140 contains 49 image nodes. Six 5G source downloads are failed response
placeholders; they stay in the audit as source_incomplete and are never counted
as reviewed. The article JSONL remains read-only.
"""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
MANIFEST_PATH = REPORTS / "round140-image-manifest.csv"
SELECTION_PATH = REPORTS / "round140-image-selection.csv"
REVIEW_PATH = REPORTS / "round140-image-review.tsv"
DECISION_PATH = REPORTS / "round140-image-decisions.tsv"
INVENTORY_PATH = ROOT / "research-rebuild/data/image-inventory.csv"
MANUAL_PATH = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"


LIMITATIONS = {
    "弓箭的杀伤力": "图片来源、年代、武器型号和历史语境未独立核验；画面只能提供军用弓箭/铠甲的插图语境，不能证明正文的穿透率、射程或后勤判断。",
    "5G": "图片来源、统计年份、样本口径、图中文字和数据未独立核验；部分源图下载/解码失败，不能以相邻图片替代，也不能由图片单独证明通信、医疗或产业预测。",
    "斑点狗": "图片来源、处理方式和原始分辨率未独立核验；图像只能证明作者展示了视觉材料，不能证明关于智能、宗教或进化的推论。",
    "移星换斗": "图片来源、拍摄/发布时间和具体语境未独立核验；街机和射箭图只能提供距离类比，不能证明轨道力学或反卫星判断。",
    "人所不能者": "图片来源、人物/作品身份和上下文未独立核验；画面与正文中心缺少可确认对应，不能证明霸凌、自杀、医疗或教育管理主张。",
    "SOP": "图片来源、商品型号、操作条件和成品质量未独立核验；图片支持流程理解但不能替代食品安全、加热参数和效果验证。",
}

# visible content, relation to text, consistency. The descriptions were made
# from the original files and the five Round140 contact sheets, not filenames.
DESCRIPTIONS = {
    "弓箭的杀伤力": {
        1: ("中世纪弓箭手、弓箭、铠甲和军阵的历史插图。", "直接对应正文关于军用箭、铠甲、射程和杀伤力的军事语境；是插图而非正文证据。", "consistent"),
    },
    "5G": {
        5: ("2017年中国人口年龄结构金字塔图。", "直接对应正文医疗章节关于人口老龄化和未来医疗需求的论述。", "consistent"),
        6: ("中国人口学历占比环图，标有研究生、本科、大专和中专等比例。", "直接对应正文关于高教育程度医护人员占比和人才结构的论述；统计口径仍需核验。", "consistent"),
        7: ("医护人员职称占比环图，区分高级、中级和初级职称。", "直接支撑正文关于高级职称医师不足和医疗人力结构的论述；数据来源仍需核验。", "consistent"),
        8: ("另一张医师职称结构占比环图。", "继续支撑正文关于医疗人力职称结构和资源配置的论述。", "consistent"),
        9: ("医院/三甲医院区域分布比例图，显示东部、中部、西部等区域。", "直接对应正文关于医疗资源集中于东部和区域分布不均的论述；图中文字和分母需核验。", "consistent"),
        10: ("三甲医院区域和省份分布比例图，列出北京、广东、江苏等省份。", "直接对应正文关于三甲医院区域集中和省份差异的论述；统计年份和口径需核验。", "consistent"),
        11: ("黑底上的血管/解剖影像，显示复杂血管结构。", "直接对应正文关于医疗影像、复杂三维重建和高带宽传输的论述。", "consistent"),
        12: ("彩色三维血管重建图，红蓝血管分层显示。", "直接对应正文关于医疗影像数据量和远程医疗场景的论述。", "consistent"),
        13: ("医院或大型公共大厅中拥挤的人群。", "直接对应正文关于医疗需求集中、就医拥堵和医疗资源不足的论述。", "consistent"),
        14: ("医院/车站式大厅中排队和聚集的人群，带有窗口与标识。", "对应正文关于医疗服务拥堵和集中需求的论述；与图13功能相近，可择一保留。", "consistent"),
        15: ("玻璃展厅中的劳动者雕像，人物持框或工具。", "正文没有明确图注或对应段落；至多提供劳动、生产历史的泛化语境，关联不充分。", "limited"),
        16: ("展厅中的搬运/劳动者雕像。", "与文章工业劳动或制造业章节只有宽泛关联，不能确认具体论证功能。", "limited"),
        17: ("展厅中坐在桌前的人物雕像。", "正文无明确对应描述，关系不明。", "weak"),
        18: ("推车搬运者雕像。", "可泛化联想到物流和劳动，但正文没有明确引用，倾向省略。", "limited"),
        21: ("腓尼基人在地中海的商业网络地图，标有港口、路线和地名。", "直接对应正文末尾关于腓尼基贸易节点、航海补给和技术突破的论述；地图地名、年代和路线仍需核验。", "consistent"),
    },
    "斑点狗": {
        1: ("土/草地中的斑纹蛇。", "直接对应正文从背景中识别异常、识别草丛中的蛇的第一层例子。", "consistent"),
        2: ("黑白随机斑块图。", "对应正文所称第一幅随机混沌图，用于说明尚不能稳定识别对象。", "consistent"),
        3: ("另一幅黑白随机斑块/伪像图。", "承接图2，说明大脑可能强行看出河马、鳄鱼等对象。", "consistent"),
        4: ("黑白斑块中可辨认出斑点狗及树影的图。", "直接构成正文核心比喻‘上帝就是这条斑点狗’的视觉材料。", "consistent"),
        5: ("与图4基本相同的斑点狗黑白斑块图。", "与图4重复，不能提供新的论证内容；若确认像素级重复可省略。", "limited"),
    },
    "移星换斗": {
        1: ("街机游戏机画面。", "弱对应正文‘游乐场篮球机投篮’的近似比喻，但并非卫星或反卫星材料。", "weak"),
        2: ("运动员在靶场射箭。", "弱对应正文‘射70米靶’的距离类比，不能支持轨道力学和反卫星判断。", "weak"),
    },
    "人所不能者": {
        1: ("古典雕像中的儿童/爱神形象。", "正文主要讨论霸凌、自杀、社会宽容和人格锻炼，没有明确图像对应。", "weak"),
        2: ("影视/游戏式战斗场景，人群持武器。", "与正文没有可确认的论证对应；文章正文不依赖该图。", "weak"),
    },
    "SOP": {
        1: ("带刻度的量杯组。", "对应准确配比和体积记录。", "consistent"),
        2: ("手动打蛋器及鸡蛋。", "对应正文指定的低技巧、手动搅拌工具。", "consistent"),
        3: ("手动搅拌器深入蛋液的示意/照片。", "对应避免打入气泡的操作方法。", "consistent"),
        4: ("电动打蛋器及配件。", "对应正文明确不使用电动搅拌器的反例/工具对比。", "limited"),
        5: ("电动搅拌器的不同搅拌头。", "继续作为正文工具选择的反例和对比。", "limited"),
        6: ("手持搅拌/起泡工具及配件。", "用于手动工具与电动工具的对比，功能与图2/3有重复。", "limited"),
        7: ("量勺。", "对应定量调味和稳定配比。", "consistent"),
        8: ("窄而高的陶瓷碗。", "对应准备工具中的打蛋碗，辅助理解器具选择。", "limited"),
        9: ("深色浅盘和餐具。", "对应蒸盘、成品展示和表面状态观察。", "limited"),
        10: ("保鲜膜及带切割盒。", "对应覆盖蛋羹、防止冷凝水滴落的流程。", "consistent"),
        11: ("硅胶蒸篮。", "对应装盘、搬运和蒸制流程。", "consistent"),
        12: ("蒸锅/蒸格。", "对应电磁炉蒸制流程。", "consistent"),
        13: ("电磁炉。", "对应加热设备和时间/火力控制。", "consistent"),
        14: ("搅拌头完全浸没于量杯中的操作示意图，带中文说明。", "直接解释核心防气泡方法。", "consistent"),
        15: ("量杯中搅拌蛋液的实际照片。", "对应蛋液调配和搅拌过程。", "consistent"),
        16: ("灰卡/中性灰卡。", "对应正文对标准化拍摄和白平衡的要求；若只研究烹饪步骤则为辅助图。", "limited"),
        17: ("表面平滑的成品蛋羹。", "对应目标质量、表面完整和平滑的验收标准。", "consistent"),
        18: ("另一张表面较浅且平整的成品蛋羹照片。", "对应成品对照，与图17部分重复，可择一保留。", "limited"),
        19: ("蛋羹被勺取开，显示凝固状态和表面破损。", "对应缺陷、口感和出品检查。", "consistent"),
    },
}

FAILED_5G = {1, 2, 3, 4, 19, 20}


def read(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = "\t") -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    manifest = read(MANIFEST_PATH)
    selection = {row["id"]: row for row in read(SELECTION_PATH)}
    assert len(manifest) == 49, len(manifest)
    assert set(row["title"] for row in manifest) == {"弓箭的杀伤力", "5G", "斑点狗", "移星换斗", "人所不能者", "SOP"}

    reviews: list[dict[str, str]] = []
    for row in manifest:
        title = row["title"]
        index = int(row["image_index"])
        failed = title == "5G" and index in FAILED_5G
        if failed:
            visible = "源图下载/解码失败，当前文件是36字节失败响应占位，无法进行视觉判断。"
            relation = "不可判断；不能以相邻成功图片替代，也不能据此决定图片用途。"
            consistency = "source_incomplete"
            review_status = "source_incomplete"
        else:
            try:
                visible, relation, consistency = DESCRIPTIONS[title][index]
            except KeyError as exc:
                raise AssertionError(f"missing visual description: {title} image {index}") from exc
            review_status = "reviewed"
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
            "limitations": LIMITATIONS[title],
            "review_status": review_status,
            "review_date": "2026-09-25",
            "ocr_status": "not_started",
        })

    fields = [
        "ordinal", "id", "title", "image_index", "local_file", "download_status",
        "visible_content", "relation_to_text", "changes_topic_judgment",
        "image_text_consistency", "limitations", "review_status", "review_date", "ocr_status",
    ]
    write(REVIEW_PATH, fields, reviews)

    # Keep transport status and the long-lived image inventory synchronized with
    # the review. Failed nodes remain explicit source_incomplete placeholders.
    review_by_key = {(x["id"], x["image_index"]): x for x in reviews}
    for row in manifest:
        item = review_by_key[(row["id"], row["image_index"])]
        row["status"] = "reviewed" if item["review_status"] == "reviewed" else "source_incomplete"
        row["notes"] = (
            f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；"
            f"限制：{item['limitations']}；"
            f"{'视觉复核完成' if item['review_status'] == 'reviewed' else '来源不完整，未作视觉判断'}；OCR未核验。"
        )
    manifest_fields = list(manifest[0])
    with MANIFEST_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manifest)

    inventory = read(INVENTORY_PATH)
    for row in inventory:
        item = review_by_key.get((row.get("id", ""), row.get("image_index", "")))
        if item:
            row["status"] = "reviewed" if item["review_status"] == "reviewed" else "source_incomplete"
            row["ocr_status"] = "not_started"
            row["notes"] = (
                f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；"
                f"限制：{item['limitations']}；"
                f"{'视觉复核完成' if item['review_status'] == 'reviewed' else '来源不完整，未作视觉判断'}；OCR未核验。"
            )
    inventory_fields = list(inventory[0])
    with INVENTORY_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=inventory_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(inventory)

    decision_rows = []
    for title, article_id in (
        ("弓箭的杀伤力", "7d799cfe-6820-5bd2-992d-9abfbeb346b1"),
        ("5G", "5a32a445-202b-593a-a880-21c3716cd9cc"),
        ("斑点狗", "cd6a03a2-7490-55c7-9848-cabeca788913"),
        ("移星换斗", "4b4e3d38-7985-5823-aafd-9f44c2d3d20b"),
        ("人所不能者", "3f6a6867-71a7-57fa-9071-39d374b1621b"),
        ("SOP", "87c24ce9-61ee-534e-8417-fe0b89090e3b"),
    ):
        article = selection[article_id]
        if title == "5G":
            decision = "retain_article_source_incomplete"
        elif title in {"移星换斗", "人所不能者"}:
            decision = "retain_article_image_omit"
        elif title in {"弓箭的杀伤力", "斑点狗", "SOP"}:
            decision = "retain_article_image_required_or_selected"
        else:
            decision = "retain_article_image_optional"
        decision_rows.append({
            "id": article_id,
            "title": title,
            "primary_before": article.get("candidate_primary", ""),
            "secondary_before": article.get("candidate_secondary", ""),
            "primary_after": article.get("candidate_primary", ""),
            "secondary_after": article.get("candidate_secondary", ""),
            "primary_changed": "no",
            "secondary_changed": "no",
            "final_status": "manual_provisional",
            "decision": decision,
            "basis": "Round140 逐图视觉复核完成；成功节点的内容与正文关系、失败节点的来源不完整状态均已逐条记录；未据图片改变专题。",
            "reason": "正文足以独立构成研究对象；文章保留与图片保留分开决定。来源、OCR及正文中的外部历史/技术/医学/政治主张仍需独立核验。",
        })
    decision_fields = list(decision_rows[0])
    write(DECISION_PATH, decision_fields, decision_rows)

    # Add an auditable pointer to the long-lived article classification records.
    manual = read(MANUAL_PATH)
    decisions_by_id = {x["id"]: x for x in decision_rows}
    counts = {}
    for row in reviews:
        counts[row["id"]] = counts.get(row["id"], 0) + (1 if row["review_status"] == "reviewed" else 0)
    for row in manual:
        item = decisions_by_id.get(row.get("id", ""))
        if not item:
            continue
        total = sum(1 for review in reviews if review["id"] == item["id"])
        marker = f"Round140 visual review=reports/round140-image-review.tsv ({counts[item['id']]}/{total} decoded/reviewed; no topic change)"
        note = row.get("review_note", "").rstrip("; ")
        if marker not in note:
            row["review_note"] = note + ("; " if note else "") + marker + "; image retention is separate; source/OCR/factual claims remain unverified."
        reviewer = row.get("reviewer", "")
        if "round140-image-review" not in reviewer:
            row["reviewer"] = (reviewer + "+round140-image-review").strip("+")
    with MANUAL_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manual[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)

    print({
        "review_rows": len(reviews),
        "reviewed_rows": sum(x["review_status"] == "reviewed" for x in reviews),
        "source_incomplete_rows": sum(x["review_status"] == "source_incomplete" for x in reviews),
        "decision_rows": len(decision_rows),
        "review": str(REVIEW_PATH),
        "decisions": str(DECISION_PATH),
    })


if __name__ == "__main__":
    main()
