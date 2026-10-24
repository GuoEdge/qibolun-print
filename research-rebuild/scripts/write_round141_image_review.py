#!/usr/bin/env python3
"""Write the human visual review for the verified Round141 image batch."""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
MANIFEST = REPORTS / "round141-image-manifest.csv"
SELECTION = REPORTS / "round141-image-selection.csv"
REVIEW = REPORTS / "round141-image-review.tsv"
DECISIONS = REPORTS / "round141-image-decisions.tsv"

IDS = {
    "下三路": "5a0bd06a-a65b-5410-9161-e4dd82420236",
    "大洪水": "09876c2d-e45f-586f-b3db-7598cc852767",
    "礼": "f2411d1a-c591-5573-b775-8c66bfd10783",
    "农村的未来": "5fcaadb8-9bba-5d43-9f03-0c374dfc9729",
    "疗愈艺术": "f62a367a-978f-5c01-8471-170daaa2eea8",
}


def read(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write(path, fields, rows, delimiter="\t"):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(rows)


LIMITATIONS = {
    "下三路": "图片来源、拍摄时间、坐标对应关系、房屋所有权、造价和房价未独立核验；地图截图和视频字幕不能证明文章对绍伊古、纳瓦尔尼或贪腐的事实判断。",
    "大洪水": "图片来源、时间、地点、比例尺和农业/水文数据未独立核验；水位、根系深度、洪水成因及跨文明历史判断不能由画面单独证明。",
    "礼": "图片为影视/宣传语境的可见记录，人物、片名、情节、礼制含义和历史文化判断未独立核验；画面不能证明文章关于礼、天佑或群体心理的因果主张。",
    "农村的未来": "图片来源、项目地点、技术成熟度、生产效率和生态效果未独立核验；示范图不能证明未来农业工业化、政治经济路径或生态工程预测。",
    "疗愈艺术": "图片来源、示范者、工具参数和训练效果未独立核验；线条质量和绘画练习不能单独证明心理治疗、抑郁免疫或生理机制判断。",
}

DESCRIPTIONS = {
    "下三路": {
        1: ("航拍大型带中式坡屋顶的别墅群，周边有树林、道路和裸地。", "直接展示正文讨论的疑似郊区别墅及其建筑规模、周边环境。", "consistent"),
        2: ("卫星图近景，标出别墅院落和坐标定位点。", "直接对应正文给出的坐标核查步骤，支持读者把房屋放回地理位置。", "consistent"),
        3: ("莫斯科及周边卫星地图，标注巴尔维哈等地点和定位点。", "对应正文把房屋置于莫斯科郊区、巴尔维哈和城市外围距离中的比较。", "consistent"),
        4: ("更大范围卫星图，显示巴尔维哈、道路、树林和农田，带定位坐标。", "支持正文关于房屋位于郊外、周边农田和树林而非城市核心的判断。", "consistent"),
        5: ("卫星地图显示涅米钦诺夫卡、斯科尔科沃及道路、村镇和绿地。", "对应正文继续核对坐标、周边开发和交通环境的公开地图方法。", "consistent"),
        6: ("视频画面中男子站在住宅前指向房屋，画面有中文字幕。", "对应正文用普通家庭自建房作为比较案例的段落；字幕提供可见但未作 OCR 的语境。", "limited"),
        7: ("视频拼图展示施工中的房屋和院落，画面文字提到打基础/施工场景。", "支持正文关于家庭自建房、施工过程和别墅规模比较的例子。", "limited"),
        8: ("施工视频画面，人物在砖墙或楼层上作业，字幕提到第一层完成。", "直接例示正文引用的自建房施工视频，用于反驳把大房屋自动等同于巨额造价。", "limited"),
        9: ("视频画面显示儿童和成人在未完工住宅外活动，带中文字幕。", "支持正文把自建住宅放入普通家庭生活和施工语境的比较。", "limited"),
        10: ("房产列表截图，显示比弗利山庄住宅照片、面积、价格和挂牌信息文字。", "直接对应正文将比弗利山庄房产作为价格和住宅规模参照的段落；截图文字需 OCR/来源核验。", "limited"),
        11: ("多张航拍住宅照片拼图，展示山地住宅、庭院和建筑群。", "支持正文与比弗利山庄住宅环境、规模和价格进行视觉比较。", "limited"),
        12: ("航拍中式坡屋顶别墅、庭院、道路和周边施工地。", "回到正文所讨论的疑似房屋，强化建筑外观和郊区环境对照。", "consistent"),
    },
    "大洪水": {
        1: ("植物根系示意图，对比矮小植物浅根与高大作物深根。", "直接对应正文从根系深度、作物高度和灌溉水位解释农田高差的论证。", "consistent"),
        2: ("整齐排列的田畦和灌溉沟渠，作物沿水沟种植。", "直接例示正文所说水浇地、垄沟水位和作物灌溉条件。", "consistent"),
        3: ("大面积平行田垄，部分沟槽呈蓝色或积水状态。", "支持正文关于平整农田、灌溉和水位变化对农业生产影响的说明。", "consistent"),
        4: ("暴雨或洪水后的农田，田面大范围积水。", "直接对应正文用江面涨水解释农田均匀被淹的视觉例子。", "consistent"),
        5: ("积水稻田与远处山体、树木，水面覆盖田块。", "支持正文关于低洼平原农田遇水位上升后景观变化的描述。", "consistent"),
        6: ("航拍干旱地区的农田、沟谷和裸露山地。", "作为农业平原与干旱地貌的对照材料，帮助正文讨论水、土地和文明地理。", "limited"),
        7: ("近景山地坡面和谷地田块，远处呈现连续平原。", "支持正文关于开阔平原、地形高差和农田视野的空间想象。", "limited"),
        8: ("地图标注美索不达米亚、伊朗和河流/湖泊区域。", "直接对应正文比较近东文明、洪水神话和地理范围的段落。", "limited"),
        9: ("航拍大型人工水道穿过农田、村镇和道路，桥梁横跨水道。", "对应正文关于灌溉工程、河流调度和农业平原水位的论证。", "consistent"),
        10: ("航拍黄色农田、河流和密集田块，呈现平原农业景观。", "支持正文关于古代文明依赖大面积平原和理想耕地的空间语境。", "consistent"),
        11: ("人物站在干裂土地上，地面出现大面积裂纹。", "与正文讨论旱涝对农业景观的对照关系相关，但不能证明具体历史事件。", "limited"),
        12: ("广阔水面、飞鸟和一艘小船，远处几乎没有陆地参照。", "直接对应正文用洞庭湖/水天一色解释‘放眼望去一切被淹’的视觉比喻。", "consistent"),
        13: ("浑浊宽阔水面及远处船只，呈现大型河口或洪水景观。", "支持正文关于洪水造成海天一色、文明聚居地被水覆盖的视觉语境。", "limited"),
    },
    "礼": {
        1: ("黑衣人物成排坐在室内，画面具有电影剧照和正式集会氛围。", "对应正文引用《一代宗师》、仪式感和群体肃容的视觉语境。", "limited"),
        2: ("三名黑衣男子并坐肖像，背景为传统风格室内。", "支持正文以人物姿态、服饰和肃穆气氛讨论知礼与尊敬的修辞例子。", "limited"),
        3: ("多人穿深色服装在大厅中成列，前方有一名居中人物。", "对应正文关于行礼、秩序、身份和正式场合的视觉语境。", "limited"),
        4: ("多人围坐或站立于宴饮场景，桌上有食物和器物。", "支持正文把礼与宴饮、待客、仪式程序联系起来的文化例示。", "limited"),
        5: ("多人合影式电影/宣传画面，前排有儿童和身着深色服装者，上方有标题文字。", "与正文关于电影人物、集体认同和礼仪气氛的讨论相符；画面文字尚未 OCR。", "limited"),
        6: ("传统服饰女性面部近景，呈现电影人物的肃静表情。", "作为正文讨论姿态、神情和‘劲力’的影视语境辅助材料。", "limited"),
    },
    "农村的未来": {
        1: ("室内多层货架式立体农场，紫色补光灯下种植绿叶菜。", "直接对应正文关于高度集约化、实验室条件和立体培养设施的未来农业设想。", "consistent"),
        2: ("室内立体种植架，成排绿叶菜在紫色灯光下生长。", "直接例示正文关于全要素控制、标准化生产和农业工业化的视觉对象。", "consistent"),
        3: ("温室中有自动化移动设备和垂直种植作物，画面呈工程化生产场景。", "支持正文把农业并入工业、使用智能制造和生物技术的论证。", "consistent"),
        4: ("橙色机械臂在室内种植架旁处理生菜。", "直接对应正文关于采摘、加工和生产环节自动化的未来农业设想。", "consistent"),
        5: ("白色机器人手臂在垂直种植架前操作，背景为绿叶菜。", "支持正文关于机器人、自动化和受控环境下批量生产的说明。", "consistent"),
        6: ("田间白色农业机器人在大面积甘蓝类作物间作业。", "把自动化农业从室内设施延伸到现有农田，作为传统农业转型的视觉对照。", "consistent"),
        7: ("农业机器人在露天作物地中作业，旁边有操作人员。", "支持正文关于智能制造、专业化农业和人机协作的未来路径。", "consistent"),
        8: ("温室或生态设施内，一群穿红色服装的人站在成片植物旁。", "对应正文关于生态圈研究、工程人员和未来生态项目占据农村空间的想象。", "limited"),
        9: ("大型玻璃温室/生态建筑群，含金字塔和穹顶结构。", "直接提供正文所说生态圈、受控环境和生态工程项目的建筑视觉参照。", "limited"),
        10: ("荒漠环境中的大型温室和生态建筑，远处有山地。", "支持正文关于在不同地区建设生态圈、恢复生态和工程化管理的设想。", "limited"),
        11: ("城市水岸旁的未来公园与温室/穹顶建筑鸟瞰图。", "对应正文把生态治理、城市群和未来研究设施联系起来的规划想象。", "limited"),
        12: ("大型城市生态公园、温室和花园景观，远处可见海湾和城市设施。", "作为生态恢复、城市农业和生态工程结合的辅助视觉材料。", "limited"),
    },
    "疗愈艺术": {
        1: ("白底上有一条细长的斜直线，几乎没有其他元素。", "直接对应正文教人画直线、观察线条偏差和建立可重复练习的核心任务。", "consistent"),
        2: ("黑白素描显示双手相互握持/交叠的细部，旁有手写或画作标记。", "对应正文后段对‘合拢的双手’、丢勒和从可见作品观察内心的艺术语境。", "limited"),
        3: ("纸面上的三角形和红色箭头/弧线，示意从一点到另一点的画线动作。", "直接支持正文关于几何方向、动作路径和纠错练习的视觉说明。", "consistent"),
        4: ("绘图软件网格界面，画面基本空白，能看到工具栏和等距网格。", "对应正文在 Procreate 等工具中定位角度、辅助画线和记录练习的段落。", "consistent"),
        5: ("绘图软件网格上有一条洋红色斜线，右端带箭头，画面有平台水印。", "直接例示正文要求画出指定角度、控制方向和利用软件辅助定位的练习。", "consistent"),
        6: ("白纸上绘有四边形和由左下指向右上的红色箭头。", "支持正文关于画线动作、起点终点、方向和可重复方法的示意。", "consistent"),
        7: ("白底上再次出现一条细斜线，线条纤细而方向明确。", "与正文反复练习直线、比较稳定性和记录结果的核心要求直接对应。", "consistent"),
    },
}


def main():
    manifest = read(MANIFEST)
    selection = {row["id"]: row for row in read(SELECTION)}
    expected = sum(int(row["deepseek_image_count"]) for row in selection.values())
    if len(manifest) != expected or any(row.get("download_status") != "success" for row in manifest):
        raise RuntimeError("Round141 manifest is not fully download/decode verified")

    review_rows = []
    for row in manifest:
        title = row["title"]
        index = int(row["image_index"])
        visible, relation, consistency = DESCRIPTIONS[title][index]
        review_rows.append({
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
            "review_status": "reviewed",
            "review_date": "2026-09-25",
            "ocr_status": "not_started",
        })

    review_fields = [
        "ordinal", "id", "title", "image_index", "local_file", "download_status",
        "visible_content", "relation_to_text", "changes_topic_judgment",
        "image_text_consistency", "limitations", "review_status", "review_date", "ocr_status",
    ]
    write(REVIEW, review_fields, review_rows)

    # Keep the batch manifest and the long-lived inventory in the same state as
    # the review TSV. The raw article JSONL remains untouched.
    for row in manifest:
        row["status"] = "reviewed"
        item = next(item for item in review_rows if item["id"] == row["id"] and item["image_index"] == row["image_index"])
        row["notes"] = f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；限制：{item['limitations']}；视觉复核完成，OCR未核验。"
    manifest_fields = list(manifest[0])
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manifest)

    inventory_path = ROOT / "research-rebuild/data/image-inventory.csv"
    inventory = read(inventory_path)
    reviewed_by_key = {(item["id"], item["image_index"]): item for item in review_rows}
    for row in inventory:
        item = reviewed_by_key.get((row.get("id", ""), row.get("image_index", "")))
        if item:
            row["status"] = "reviewed"
            row["notes"] = f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；限制：{item['limitations']}；视觉复核完成，OCR未核验。"
    with inventory_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(inventory)

    decisions = []
    for title, article_id in IDS.items():
        article = selection[article_id]
        if title in {"下三路", "大洪水", "农村的未来", "疗愈艺术"}:
            decision = "retain_article_image_required"
        else:
            decision = "retain_article_image_optional"
        decisions.append({
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
            "basis": "Round141 逐图视觉复核 100% 完成；图片与正文主轴关系已记录，未据图片改变专题。",
            "reason": "正文足以独立构成研究对象；图片保留级别依据图文关系决定。来源、OCR及文章中的外部历史/技术/医学/政治主张仍需独立核验。",
        })
    decision_fields = list(decisions[0])
    write(DECISIONS, decision_fields, decisions)

    manual_path = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
    manual = read(manual_path)
    decision_by_id = {item["id"]: item for item in decisions}
    groups = {}
    for item in review_rows:
        groups.setdefault(item["id"], 0)
        groups[item["id"]] += 1
    for row in manual:
        item = decision_by_id.get(row.get("id", ""))
        if not item:
            continue
        marker = f"Round141 visual review=reports/round141-image-review.tsv ({groups[item['id']]}/{groups[item['id']]} images; no topic change)"
        note = row.get("review_note", "").rstrip("; ")
        if marker not in note:
            row["review_note"] = note + ("; " if note else "") + marker + "; image limitations recorded; OCR and factual claims remain unverified."
        reviewer = row.get("reviewer", "")
        if "image-review" not in reviewer:
            row["reviewer"] = (reviewer + "+image-review").strip("+")
    with manual_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manual[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
    print({"review_rows": len(review_rows), "decision_rows": len(decisions), "review": str(REVIEW), "decisions": str(DECISIONS)})


if __name__ == "__main__":
    main()
