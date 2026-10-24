#!/usr/bin/env python3
"""Write conservative Round118 per-image visual review and decision reports."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
MANIFEST = REPORTS / "round118-image-manifest.csv"
REVIEW = REPORTS / "round118-image-review.tsv"
DECISIONS = REPORTS / "round118-decisions.tsv"

COMMON = "仅作当前图片可见内容记录；来源、时间、文字真伪及外部事实未独立核验，不能据图推出正文之外的事实。"
rows_by_key: dict[tuple[str, str], tuple[str, str, str, str]] = {}


def add(aid: str, idx: int, visible: str, relation: str, consistency: str = "consistent", limitation: str = COMMON) -> None:
    rows_by_key[(aid, str(idx))] = (visible, relation, consistency, limitation)


aid = "e8efc7f4-9d13-58cd-a7b8-2572233298ae"
maps = [
    ("长沙市卫星地图，红色定位点标出‘革命烈士陵园’。", "直接对应正文讨论烈士陵园及其公共记忆空间的地理语境。"),
    ("武汉市城区卫星地图，定位点标出‘北伐战争烈士陵园’。", "支持正文将具体陵园置于城市纪念地理中讨论。"),
    ("河源市卫星地图，定位点标出一处革命烈士陵园。", "支持正文关于不同地区烈士陵园及纪念空间的例证。"),
    ("城市卫星图，红色定位点标出‘革命烈士陵园’，周边可见道路与村镇。", "对应正文将陵园与地方城市/社区空间联系起来的叙述。"),
    ("上海市卫星地图，定位点标出‘龙华烈士陵园’。", "直接对应正文列举城市烈士陵园与公共记忆的视觉材料。"),
    ("珠海市卫星地图，定位点标出‘珠海烈士陵园’。", "支持正文比较不同地方纪念设施及其空间位置。"),
]
for i, (v, r) in enumerate(maps, 1):
    add(aid, i, v, r, "limited", "地图名称、定位点、比例和来源未独立核验，不能单独证明陵园行政归属、历史或公共记忆影响。")

add("a687351f-28f0-5b9a-8d9c-41682da6e7a8", 1, "《一拳超人》角色埼玉的彩色头像，红色拳套和白色披风清晰可见。", "对应正文以‘一拳’和能力差异讨论竞争与击败对手的漫画语境。", "limited", "只能确认画面是该角色风格的动漫头像，不能据图证明能力、情节或公平竞争判断。")

aid = "b7783aac-09f8-5124-bd0f-03efe1ca23aa"
add(aid, 1, "黑白钉板示意图：上部均匀排列圆点/钉子，下部为竖向通道和多个收集格。", "直接对应正文关于高尔顿钉板、随机路径和结果分布的说明。", "consistent", "图示未标明来源和比例，不能单独验证概率推导或混沌系统的普遍性。")
add(aid, 2, "黑白钉板示意图，顶部有手形/入口，中部密集钉点，底部多个分格。", "直接支持正文把知识、预测和决策边界类比为钉板随机过程。", "consistent", "示意图无实验数据和参数，不能独立证明正文的预测边界结论。")

aid = "a3789420-2208-5538-8511-460e4a95ab7b"
add(aid, 1, "长篇中文页面截图，顶部有北美地图，下方分为‘背景’‘宣战’‘过程’等段落，内容涉及美墨战争。", "直接对应正文关于越境战争、侵略者定义及战后政治结果的历史案例。", "limited", "页面文字、地图和历史断言未逐项核验，截图不能独立确认战争因果或政治结论。")
add(aid, 2, "新闻/访谈缩略图，两名人物并列，画面叠有英文‘DON'T BE NAIVE’。", "支持正文讨论当代战争叙事、外交表态和国际秩序的视觉语境。", "limited", "人物身份、节目来源、字幕上下文和事件真实性未独立核验。")

add("0069ab17-6b87-579a-b7f6-a4ada4c5dff3", 1, "深色社交媒体评论截图，英文讨论逐步行动、减少平民伤亡及假设台湾遭入侵时的做法。", "直接对应正文关于俄乌战争状态、战略行动和援助/入侵边界的讨论。", "limited", "账号、时间、翻译和评论事实未核验，不能据图证明军事行动或伤亡判断。")
add("8a232e01-e8d5-5a3c-ba97-1d9f3e83ff76", 1, "影视剧近景，一名男子在昏暗室内说话，画面下方有中文字幕。", "仅支持正文把‘单纯’、责任和合作放入影视化人物对话语境。", "limited", "影片、人物、字幕和上下文未核验，不能据图证明合作责任或动机判断。")
add("e108515f-375c-53c9-8f6d-1ee2c16b275a", 1, "夜间影视片段，几名人物在建筑外/室内交谈，字幕出现‘兽医，兽医—动物’。", "只能确认题面所附视频/影视语境，无法从图像确认‘最大成长速度’的历史地理或长城论证。", "inconclusive", "图片内容与题名的对应关系不清，字幕、影片来源及正文中心均未核验；图片不足以升级分类。")

aid = "bb64707c-4cba-502c-add2-2fc5fe19c902"
add(aid, 1, "黑色背景中远处亮起的火箭/光束，前景为一条通向光源的道路。", "作为‘看不到希望’的象征性视觉材料，呼应正文对希望、注意和主观感知的讨论。", "limited", "明显是象征/宣传式画面，不能证明国家、经济或现实希望判断。")
add(aid, 2, "阳光下盛开的黄色蒲公英花田，天空有云。", "以明亮自然景象与正文的希望/注意比喻形成对照。", "limited", "图片为一般性自然景观，不能据图证明情绪机制或现实前景。")
add(aid, 3, "道路尽头的火箭升空画面，天空有云和强烈亮光。", "继续作为‘希望’与可见目标的象征性例证，未改变主体心理专题。", "limited", "图片来源及事件真实性未核验，不能由图推出航天、国家或经济事实。")

aid = "c5354fb0-7345-5864-8522-2c0cfdad3c2e"
horse = [
    "彩色绘画中的两匹马相向腾跃，表现鬃毛、肌肉和动态姿态。",
    "黑白版画描绘马匹翻倒/挣扎，底部可见英文说明‘The black was jerked off his feet.’。",
    "黑白/灰色画面中两匹马并列或相向，突出头部、鬃毛和姿态。",
    "铅笔素描描绘一匹马跨在另一匹马背上，强调马体和鬃毛结构。",
    "黑白点描画面中两匹马相互交错，前景为深色马、后方为浅色马。",
    "棕灰色素描中的骑乘/腾跃马匹，表现头部和鬃毛动态。",
    "淡色铅笔肖像，近距离描绘马头、鬃毛和前胸。",
]
for i, v in enumerate(horse, 1):
    add(aid, i, v, "直接对应正文以马匹图像讨论战马、骑乘/战斗形态及历史材料的视觉语境。", "limited", "画面只能确认马匹及绘画表现，未显示阉割、年代、战场或史料来源，不能独立支持相关历史和生理断言。")

add("f56baf4c-6d3c-5b38-aba5-1a38b413f041", 1, "黑色背景上放置一枚彩色、带复杂纹理的椭圆形艺术物件，并有倒影。", "可作为正文关于‘讨厌的那种人’和复杂心理投射的抽象视觉隐喻。", "limited", "物件身份、作者和隐喻关系未核验，不能据图证明人格或心理判断。")
add("e122a811-8341-594f-bce6-b50983b7e485", 1, "白底人物资料图，标注‘兰迪·鲍许 Randy Frederick Pausch’，中间为黑白男性肖像。", "仅对应正文所附视频/人物材料，说明题面可能引用该人物。", "limited", "姓名、肖像来源及与文章主旨的关系未独立核验；正文材料不足，不能因图片升级分类。")
add("b95e3891-a76b-5252-86ca-12733a306294", 1, "中国画风格人物图：白衣长须老人骑在白色羊/山羊上，顶部有书法题字和印章。", "仅提供宗教/文化艺术图像语境，不能直接证明正文关于犹太教、基督教或反犹现象的历史论证。", "inconclusive", "题字、作者、人物身份和来源未核验，图像与文章主专题的关系不确定。")

add("4624f253-14ce-513a-b166-b8a351df55eb", 1, "日式和弓结构图，列出弓部名称、弦、握位及长度比例等中英/日文标注。", "直接对应正文关于和弓非对称结构、材料力学、弓长和效能约束的工程解释。", "consistent", "图中文字、比例和来源未逐项核验，不能单独证明力学参数或历史演变。")
add("4624f253-14ce-513a-b166-b8a351df55eb", 2, "灰色线稿飞机/双翼机三视角插图，与和弓结构无明显直接对应。", "与正文和弓技术主题的对应关系不清，不能作为弓结构或战场用途证据。", "inconclusive", "图片来源和插入关系未核验，可能是误配或跨主题材料；保留 provisional。")

add("0b54ec8d-aa37-59a6-b038-56f399ee3586", 1, "停车场中一辆汽车被透明塑料膜整体包裹，背景有树木、高层建筑和车辆。", "可对应正文关于异常天气/灾害时采取临时防护措施的视觉语境。", "limited", "不能据图确认天气事件、保护效果、车辆或公共灾备方案的安全性。")

aid = "f07a766c-e718-5b57-9da3-9a29d2d2451c"
laundry = [
    "深色定制柜中的洗衣机和烘干机，一名女性蹲在机器旁，画面标出约60厘米的竖向尺寸。",
    "整洁的洗衣区，双机置于木色柜体下方，上方有挂杆、衣物和收纳层板。",
    "浅色厨房/洗衣柜，洗烘机上下叠放，旁边有水槽、毛巾篮和收纳。",
    "白色柜体中两台并排洗衣机，前方有藤编推车，背景为石材墙面。",
]
for i, v in enumerate(laundry, 1):
    add(aid, i, v, "直接对应正文关于大型家电空间布局、人体工学、收纳和施工/使用安全的讨论。", "consistent", "图片更接近家装示例或宣传图，尺寸、设备型号、安装条件和安全效果未独立核验。")

aid = "456dd348-f6bc-5f2f-a53d-491d6dd60813"
orn = [
    "金色/棕金色长链或项饰，呈连续镂空、编织状结构，置于展陈布面上。",
    "链节局部特写，可见矩形金属节和密集卷草/镂空纹样。",
    "黑底展陈中的一对金色龙凤/鸟形立体饰件，细部有丝状卷曲纹样。",
    "黑底金色凤鸟或瑞兽立体饰物特写，装饰线条和镂空细节清晰。",
    "黑底金色花叶簪/饰件，层叠花瓣和叶片形成整体造型。",
    "带多枚彩色宝石的金色镂空长柄饰件，周边有卷草和花瓣纹样。",
]
for i, v in enumerate(orn, 1):
    add(aid, i, v, "直接支持正文关于掐丝、镂空、饰物结构、重量与审美工艺的视觉语境。", "limited", "图片只能确认金色饰物与纹样，材质、重量、工艺年代、作者和价格未独立核验。")

add("42d075df-3ae5-51cd-aefc-fbcc77efc298", 1, "以‘素问’为中心的彩色放射状关系/分类图，向外展开大量节点和分支。", "可对应正文讨论自由、自我价值与外部评价的概念网络/分类语境。", "limited", "图中节点文字较小且来源、制作方法及与正文论证的对应关系未核验。")
add("378fa426-595e-55c4-b84c-8df607af5d8d", 1, "信息图标题为‘均值模糊（Average Blur）原理图解’，展示矩阵平均值计算及山景图模糊前后对比。", "直接对应算法/图像处理概念，但与正文关于国家孝治、宗族连坐和基层秩序的主专题对应关系不清。", "inconclusive", "信息图文字和来源未逐项核验，可能是插图误配；不能用它替代正文制度史判断。")

aid = "b5636f46-9279-5242-a25e-95ce95de0ce0"
add(aid, 1, "手机/电商截图中的304不锈钢钢丝绳产品尺寸表，列出直径、股数、承重/破断力等栏目，多行被紫色圈出。", "直接对应正文以钢丝绳、无人机/输送线和高层火灾救援技术方案讨论材料参数。", "limited", "表格数值、产品型号、承重条件和来源未独立核验，不能证明救援方案可行。")
add(aid, 2, "与上一张相同的304不锈钢钢丝绳产品尺寸表，另一组规格行被圈出。", "继续支持正文比较钢丝绳规格、强度和救援设备配置的工程语境。", "limited", "重复电商/产品表不能独立验证安全系数、固定点或实际救援效果。")

add("71e89445-dd77-54af-899d-8cb1747538e9", 1, "黑底产品信息图，标注‘三层螺旋绳合、高密高韧’，显示内置钢丝芯、编织绳截面和双重防护文字。", "直接对应正文关于火灾速降设备、绳缆材料、固定点和路线安全的工程操作条件。", "limited", "产品宣传文字、结构和安全性能未独立核验，不能据图替代救援设备标准或实测。")

add("17649db4-9574-57a1-b386-d7f3e181d218", 1, "超长微信聊天截图，双方围绕孩子晚睡、教育方式、夫妻/家长沟通、情绪与边界反复讨论，中间插有婴儿照片。", "直接对应正文关于家庭儿童教育、夫妻共同决策、情绪承认和权力边界的讨论。", "consistent", "聊天参与者、时间、事件真实性和医学/教育效果未核验；截图文字不替代正文事实审计。")


def main() -> None:
    with MANIFEST.open(encoding="utf-8-sig", newline="") as fh:
        manifest = list(csv.DictReader(fh))
    assert len(manifest) == 46, len(manifest)
    fields = ["ordinal", "id", "title", "image_index", "local_file", "download_status", "visible_content", "relation_to_text", "changes_topic_judgment", "image_text_consistency", "limitations", "review_status", "review_date"]
    out = []
    for m in manifest:
        key = (m["id"], m["image_index"])
        assert key in rows_by_key, f"missing visual review {key}"
        visible, relation, consistency, limitation = rows_by_key[key]
        out.append({**{k: m.get(k, "") for k in fields}, "visible_content": visible, "relation_to_text": relation,
                    "changes_topic_judgment": "no", "image_text_consistency": consistency,
                    "limitations": limitation, "review_status": "reviewed", "review_date": "2026-09-24"})
    assert len(out) == len(rows_by_key) == 46
    with REVIEW.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader(); writer.writerows(out)

    # This report records the evidence review without changing formal manual decisions.
    candidate_ids = {
        "e8efc7f4-9d13-58cd-a7b8-2572233298ae",  # memorial maps align with A19
        "b7783aac-09f8-5124-bd0f-03efe1ca23aa",  # Galton board diagrams align with A03
        "a3789420-2208-5538-8511-460e4a95ab7b",  # war case material aligns with A12
        "f07a766c-e718-5b57-9da3-9a29d2d2451c",  # laundry layout images align with A13
        "456dd348-f6bc-5f2f-a53d-491d6dd60813",  # craft images align with A03
        "17649db4-9574-57a1-b386-d7f3e181d218",  # family dialogue aligns with A05
    }
    manual_path = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
    with manual_path.open(encoding="utf-8-sig", newline="") as fh:
        manual = {r["id"]: r for r in csv.DictReader(fh)}
    review_by_id = {}
    for r in out:
        review_by_id.setdefault(r["id"], []).append(r)
    decisions = []
    for aid, rs in review_by_id.items():
        m = manual[aid]
        recommendation = "candidate_for_confirmation_after_text_and_source_audit" if aid in candidate_ids else "retain_provisional"
        visible = "；".join(dict.fromkeys(r["visible_content"] for r in rs))
        relation = "；".join(dict.fromkeys(r["relation_to_text"] for r in rs))
        limitations = "；".join(dict.fromkeys(r["limitations"] for r in rs))
        decisions.append({"id": aid, "title": m["title"], "primary": m["primary_print_topic_code"], "secondary": m["secondary_print_topic_codes"],
                          "status": m["classification_status"], "recommendation": recommendation, "basis": m["decision_basis"],
                          "risk_note": f"Round118 image review {len(rs)}/{len(rs)}; changes_topic_judgment=no; visible={visible}; relation={relation}; limitations={limitations}; 图片仅记录可见内容，不替代OCR或外部事实核验。"})
    decisions.sort(key=lambda r: r["id"])
    with DECISIONS.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id", "title", "primary", "secondary", "status", "recommendation", "basis", "risk_note"], delimiter="\t")
        writer.writeheader(); writer.writerows(decisions)
    print(f"wrote {REVIEW} rows={len(out)} articles={len(review_by_id)}")
    print(f"wrote {DECISIONS} rows={len(decisions)} candidates={len(candidate_ids)}")


if __name__ == "__main__":
    main()
