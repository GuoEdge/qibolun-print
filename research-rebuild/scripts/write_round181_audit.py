#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round181: stratified audit of the 616 official-unmatched articles.

Sample: 79 records (12.8% of 616), seed 20260926, covering all 79 non-empty
(length-band x current-topic) cells and all 21 current topics — see
``round181-sample-frame.json``.

The audit answers two separate questions and keeps them separate:

  Q1  Is the *local* print primary topic supported by the article body?
  Q2  Is the article's absence from the official category inventory a mere
      inventory gap, or does it indicate a local classification problem?

The official layer is never fabricated for these articles: every row keeps
``official_layer = native_unassigned_valid``.

Evidence excerpts are extracted **by this script** from the corpus body, so they
are verbatim by construction; the reviewer verdict is recorded separately.  Two
excerpts are stored: the body head and (when a topic anchor term occurs) a
window around the first anchor hit.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "reports/rebuild-20260926/round181"
REVIEW_DATE = "2026-09-26"
REVIEWER = "main-thread+round181-official-unmatched-sample"

ANCHORS = {
    "A01": ["情绪", "焦虑", "自我", "心态", "害怕", "恐惧", "痛苦", "坚持", "迷茫"],
    "A02": ["女性", "男性", "性别", "身体", "女权", "性关系", "外貌"],
    "A03": ["本质", "定义", "证据", "逻辑", "事实", "概念", "论证"],
    "A04": ["学习", "教育", "学历", "能力", "学校", "孩子", "专业"],
    "A05": ["父母", "子女", "家人", "家族", "亲戚", "媳妇", "孩子"],
    "A06": ["朋友", "爱人", "恋人", "恋爱", "婚姻", "友谊", "亲密"],
    "A07": ["管理", "组织", "合作", "职场", "公司", "同事", "执行"],
    "A08": ["市场", "经济", "税", "股市", "商业", "价格", "利润", "财富"],
    "A09": ["疾病", "医疗", "医生", "病人", "传染病", "护理", "临终"],
    "A10": ["法律", "法院", "犯罪", "警察", "司法", "死刑", "立法"],
    "A11": ["信仰", "宗教", "上帝", "神", "价值", "伦理", "道德"],
    "A12": ["战争", "军事", "美国", "中国", "战略", "外交", "冲突"],
    "A13": ["技术", "工程", "制造", "产业", "设备", "芯片", "设计"],
    "A14": ["AI", "人工智能", "机器", "算法", "自动化", "ChatGPT"],
    "A15": ["艺术", "审美", "电影", "文化", "创作", "美", "气场"],
    "A16": ["舆论", "媒体", "宣传", "传播", "话语", "公共"],
    "A17": ["民族", "种族", "身份", "自豪", "族群"],
    "A18": ["动物", "生态", "自然", "进化", "科学", "生物"],
    "A19": ["死亡", "葬礼", "去世", "死", "纪念", "临终"],
    "A20": ["历史", "王朝", "文明", "时代", "古代", "演变"],
    "A00": ["跨域", "材料", "待审"],
}

# id -> (verdict, local_topic_supported, official_absence_reading, correction_suggestion, note)
V = {
    # --- needs_revision: local topic not supported by the body -----------------
    "01cc5e71-1aae-5677-8463-41640aeaa77c": (
        "needs_revision", "no", "inventory_gap",
        "A15 -> A08（副 A12）",
        "正文中心是股价与盈利脱钩、增长叙事与愿景的可信度、中国资产的长期判断，属于市场与投资逻辑；正文没有任何艺术、审美或文化生产内容。local A15 属明显误置。"),
    "a4b0e11a-9cf1-59bc-83b7-d671271eb36e": (
        "needs_revision", "no", "inventory_gap",
        "A16 -> A09（副 A10）",
        "正文是防疫防线设计（交通枢纽落地检疫、行程码认证、常备防疫设施与专业应急部队），全文没有媒体、传播、舆论或公共形象内容；local A16 属明显误置。"),
    "31dcaf05-d756-5ab9-8ee7-9c6191c35104": (
        "needs_revision", "no", "inventory_gap",
        "A02 -> A04（副 A07;A03）",
        "正文讨论“厉害的人”为何办法多：失败没有造成恐惧、避责天堂、无知作为庇护所，属于能力形成与组织避责；全文没有性别、身体或同意的任何内容。local A02 属明显误置。"),
    "26c7ad17-39ab-5728-afa9-a4181110a374": (
        "needs_revision", "no", "inventory_gap",
        "A18 -> A02（副 A10）",
        "题面与正文都在讨论“女性对政治兴趣低是否是生理天性”，并以女皇/女帝与弱者政治学作答，中心是性别秩序与政治能力；全文没有生态、动物或自然科学内容。local A18 属明显误置。"),
    "bb3a6d98-8bc5-5324-b13b-38d9710fb0d4": (
        "needs_revision", "no", "inventory_gap",
        "已由 round172 从 A00 改为 A03（副 A04）",
        "抽样时该行仍为 A00（样本取自修订前的印刷索引）。正文区分“对”与“对错了”，是命题有效性与判断框架的认识论问题；本轮 round172 已改正。"),
    "8e98b07e-b5f1-523b-9fcf-4882ceda59de": (
        "needs_revision", "no", "inventory_gap",
        "已由 round172 从 A00 改为 A11（副 A03）",
        "抽样时该行仍为 A00。正文论证传统与宗教无法被“打死”且会吸收攻击者招数，属于宗教/传统与科学理性关系的规范性论证；本轮 round172 已改正。"),
    "b8654507-6bff-5b2e-a5d5-e963065da83b": (
        "needs_revision", "no", "inventory_gap",
        "已由 round172 从 A00 改为 A11（副 A01;A07）",
        "抽样时该行仍为 A00。作者自述其论述是“选择后者的心理建设、行为准则和伦理框架”，属世俗规范性论证；本轮 round172 已改正。"),
    "02d91221-6cbd-5739-ae03-154992a878a5": (
        "needs_revision", "no", "inventory_gap",
        "已由 round172 从 A00 改为 A03（副 A16;A20;A07）",
        "抽样时该行仍为 A00。正文解剖“宏大叙事”概念、叙事与事实的分野、合作需要共同价值观，属认识论分析；本轮 round172 已改正。"),
    # --- cannot_verify_from_body ---------------------------------------------
    "cdf1315e-9753-550f-8e55-651c06dfa32f": (
        "cannot_verify_from_body", "no", "cannot_assess",
        "维持 A00 + manual_provisional（round165/round172 已判）",
        "正文在“厂”字后截断，仅 10 字。A00 + 待审与 registry 定义一致，不构成新的本地分类问题。"),
    "709c7581-b9fb-5c40-9d0d-bf5f0b3ec31b": (
        "cannot_verify_from_body", "no", "inventory_gap",
        "建议复核：A06 是否应由正文而非题面支撑",
        "正文 18 字“当然是爱和被爱的能力。不接受反驳。”只能支撑“爱与被爱是能力”，无法在 A06（亲密关系）与 A04（能力形成）之间定出唯一主码。属材料不足，不是官方层问题。"),
    "66627550-a9d0-5b2e-af32-c03cfac0786a": (
        "cannot_verify_from_body", "no", "inventory_gap",
        "建议复核：A07 的“服务”入口是否应由该正文支撑",
        "正文 62 字是戏谑回应（“哔嘟哔嘟魅惑光波”），没有可辨认的中心操作；local A07 只能由题面“餐馆老板服务态度”推出，属材料不足。"),
    # --- holds_but_body_short -------------------------------------------------
    "bad58134-0613-5973-843b-2bc93ebb9733": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 25 字是作者对弥留告别的直接表述，A19 由正文支持；但正文极短，专题稳定性依赖题面语境。"),
    "7892dffe-5880-5ff5-9b50-d6e35a827662": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 45 字完成了“利己的野心／利他的野心”的概念区分，A03 由正文支持。"),
    "b9d54197-5ebd-59ee-896f-9c3edb53721d": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 53 字直接回答印钞与通胀的关系，A08 由正文支持。"),
    "ff132074-8175-5372-8c38-7080750951b8": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 55 字直接判断中美脱钩的主动权，A12 由正文支持。"),
    "3ea32315-6621-5490-874c-f67875fbd32e": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 75 字给出“个体越小越不节能”的生物学理由，A18 由正文支持。"),
    "b8b64584-8dbc-56c2-b405-c7daf93e2cc9": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 82 字给出“机器与人的文化差异”判断，A13 由正文支持。"),
    "d56b4f7f-b78d-5812-b784-a89b8027e4e1": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 110 字以“语言 vs 文字”的定义区分作答，A03 由正文支持。"),
    "f5cfadcb-27a0-51bd-af95-922d104f84e4": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 111 字直接否定政治信仰与宗教信仰的二分，A11 由正文支持。"),
    "525ef1d9-b14d-5532-a015-aacbdde26dc0": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 120 字以三组对照句区分民族主义与种族主义，A17 由正文支持。"),
    "f378e3c7-87a0-524c-a6ec-d3231fd3cba2": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 141 字比较仿星器与托卡马克的容错/效率取舍，A13 由正文支持。"),
    "073d820a-ca22-52fe-bc2c-152e5a0d9742": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 192 字以机器形态与杂质稀释作答，A14 由正文支持。"),
    "3b6dc172-30a7-5fa8-a8ee-4aface5842e6": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 196 字给出巨兽可行性的生物学与自卫机制推理，A18 由正文支持。"),
    "13f87a0b-aae3-5dcd-b9e8-295c4862ba6c": (
        "holds_but_body_short", "yes", "inventory_gap", "",
        "正文 208 字以流量数据反驳“喜闻乐见即正义”，A15 由正文支持。"),
    # --- holds_with_boundary_note --------------------------------------------
    "9df58f55-d41c-54a3-a441-167d05798bda": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A15；若强调主体形象管理可考虑 A01",
        "正文把穿搭分基本款／制服／戏服三层并收束到“cosplay 你自己”，属审美与自我呈现；A15 可站住，但 A01（主体感）是可讨论的替代入口。"),
    "5d5b4502-5b35-5392-b79f-dd62408fb0dd": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A17；若强调竞技伦理入口可考虑 A21",
        "正文以职业体育的“干净”定义、阈值博弈与民族自豪感的尺度为中心，A17 由正文支持；由于体育制度与竞技伦理占相当篇幅，A21 是可讨论的副入口。"),
    "e830e716-ff9a-5e35-bcbe-b07193fcfab1": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A06；若强调亲属秩序可考虑 A05",
        "正文由配偶与亲戚住宿费用之争起，收束到为人处事与道义权力；A06（配偶）与 A05（亲属）都在场，取 A06 可接受。"),
    "d1e4b776-aac6-510f-9fa8-d30c1f3b5092": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A12；正文尾部转向人际熟悉度，属结构瑕疵",
        "正文主体是立陶宛案例下的大国影响力与情报依赖，A12 由正文支持；但尾段突然转入“轻狎则必后惊”的人际议题，与前半不同域，属正文结构问题而非分类问题。"),
    "049ac2a7-fd8b-5c5c-b78c-1133cbd4c75e": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A20；若强调人才市场可考虑 A08/A04",
        "正文以 1990-2015 国策阶段与未来二十年的时代轨迹作答，A20（历时演变）可站住；但人才供需本身属劳动市场/教育，A08 或 A04 是可讨论的替代入口。"),
    "16dee6cc-dfa1-57e8-b25d-135a9b3bbae6": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A11（按本轮 R4“世俗论证”入口）",
        "正文以两个情景案例论证对社会责任的愧疚不可抛弃，属规范性人生论证，按 RULE-REVISION R4 归 A11；A05/A07 是可讨论的替代入口。"),
    "a623fb54-aaca-5b8b-9728-92023fa470d7": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A12；前半段属市场结构（A08）",
        "正文前半解释日本西瓜为何长期不降价（对内博弈能力），后半转入台海—日韩地缘格局，A12 覆盖后半的中心；若以“市场失灵”为准则应入 A08。"),
    "b01b85e8-9601-58b4-b734-1bcf558100c6": (
        "holds_with_boundary_note", "yes", "inventory_gap",
        "维持 A12；正文实为物理与工程可行性论证",
        "正文以工质推进的物资量级与收益结构论证星际战争不可行，A12（战争与大国秩序）是注册表内最贴近的入口，但内容主体是量级估算与工程推理，A13 亦可讨论。"),
}

HOLDS = """a878e18a-f50a-50d3-8b66-ab21df943436 66917df2-05fa-51f8-a776-1e5959ebcd2d c4d83310-ebf7-5a0c-b054-265c034f4523
1c5a8886-10e2-548a-911b-9bdb32e87921 6e00a9d7-d4d4-5578-9443-cf54d8b34d1f a762cfb1-7393-508b-950b-3628631c9827
ee657bec-2d6a-5259-b88b-d9391f85310a f082310c-2aa3-5de8-aacd-3239ca103c99 33145356-802e-5f25-92d1-bf644bc4c154
418def6a-d83c-58a9-8055-db2fec4434ed cf89d18d-166b-5af2-a6b3-dad6a6c853b3 c037b709-70ab-5d89-952e-9cdc4ee7f924
d345dfad-efbe-5dd8-ad4d-4bc095c30d26 512c1ba9-4005-5685-bfc6-08e1d35d967c 423cdf0a-6e07-5795-87bf-43bbb0bc6451
aa95c15c-a6fd-5de4-85c7-27f4365a0354 9af3f757-ffb6-5c9e-b461-afdf9ccea949 661b29c0-a41f-589f-9493-51a0719d0afe
670401ad-58ae-5d29-bce3-79f0ff90c037 2afb5f2f-3230-51ec-8201-8bcbec611b85 2702982e-d0ee-5380-99d5-05ba3af76193
04295c92-aeb2-5400-8418-46b6446e00cf bb41d4c7-93b2-5910-923b-5e577b76b8e6 a76431bd-767c-5863-9a1d-52ace5b134f2
9b29490d-e7a4-57a2-8f19-d5c2b9947669 4acda225-d296-57b6-9595-0d85264d0ef2 64038e78-7895-5593-a7ed-2f1274b00855
13a691da-053b-598e-b831-7da9a49fba15 000eeb82-5cac-5e7f-a22b-fb8949aa1b12 b5636f46-9279-5242-a25e-95ce95de0ce0
911abc81-6ebf-58a0-9ac2-96b40f412f94 6e19481e-b83e-5b79-a4a2-db1137fca698 35af9bf7-37bd-5b11-9d13-f314dc5a1ee6
45ad7f8d-f4a2-5975-8750-5b90d8ef2247 953904db-2f8f-5b98-9a8e-87b15a4675ab 1b8ad80d-e7bc-5ffe-88db-0060275b8121
e4da9868-2b4b-5c7e-b689-898ab4e03e53 3701390c-7f2f-56a6-a126-97ba2e892f4f 575a9421-ccab-5ddf-8fb1-0ce68be1c799
115363db-d788-5691-bb9f-3924f0a811d8 ca98070c-112a-5de1-8d8e-7afed106ea9e 3225022a-2d87-588a-9fab-8097493b1ae0
f0e6b60b-5f91-5037-9796-480eeca991b2 17649db4-9574-57a1-b386-d7f3e181d218 d259c0c0-7071-5286-a949-17610195fbc1
becd5793-42a0-508d-9811-ce217f24500d b95e3891-a76b-5252-86ca-12733a306294""".split()

READ_FULL_MAX = 1500


def main() -> int:
    packets = {p["id"]: p for p in json.loads((OUT / "round181-fulltext.json").read_text(encoding="utf-8"))}
    frame = {r["id"]: r for r in csv.DictReader((OUT / "round181-sample-frame.csv").open(encoding="utf-8-sig"))}
    assert set(frame) == set(packets) == set(V) | set(HOLDS), "sample sets differ"

    rows = []
    for aid, f in frame.items():
        p = packets[aid]
        text = p["text"]
        topic = f["primary_print_topic"]
        if aid in HOLDS:
            verdict, supported, absence, suggestion, note = (
                "holds", "yes", "inventory_gap", "",
                "本地主专题与正文中心一致：正文可辨认的中心操作与该 A 码的注册边界相符，未发现本地分类问题。")
        else:
            verdict, supported, absence, suggestion, note = V[aid]
        head = text[:160]
        window = ""
        for kw in ANCHORS.get(topic, []):
            pos = text.find(kw)
            if pos >= 0:
                lo = max(0, pos - 80)
                window = text[lo: lo + 160]
                break
        rows.append({
            "id": aid, "title": p["title"], "source_ordinal": f["source_ordinal"],
            "published_date": f["published_date"], "body_char_count": f["body_char_count"],
            "length_band": f["length_band"], "year_band": f["year_band"],
            "stratum": f["stratum"], "draw": f["draw"],
            "local_primary_topic": topic, "local_topic_supported_by_body": supported,
            "read_coverage": "full_text" if p["body_char_count"] <= READ_FULL_MAX else "head1000+tail500",
            "body_excerpt_head": head, "body_excerpt_topic_window": window,
            "audit_verdict": verdict, "official_layer": "native_unassigned_valid",
            "official_absence_reading": absence, "correction_suggestion": suggestion,
            "audit_note": note, "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE,
        })

    fields = list(rows[0].keys())
    with (OUT / "round181-official-unmatched-audit.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    from collections import Counter
    vc = Counter(r["audit_verdict"] for r in rows)
    pc = Counter(r["local_primary_topic"] for r in rows if r["audit_verdict"] == "needs_revision")
    summary = {
        "round": 181, "frame": 616, "sample": len(rows),
        "sample_ratio": round(len(rows) / 616, 4),
        "seed": 20260926,
        "verdict_counts": dict(vc),
        "local_problem_count": vc["needs_revision"] + vc["cannot_verify_from_body"],
        "local_problem_ratio": round((vc["needs_revision"] + vc["cannot_verify_from_body"]) / len(rows), 4),
        "needs_revision_by_local_topic": dict(pc),
        "official_layer_fabricated": 0,
        "read_coverage_counts": dict(Counter(r["read_coverage"] for r in rows)),
        "output": str(OUT / "round181-official-unmatched-audit.csv"),
    }
    (OUT / "round181-audit-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
