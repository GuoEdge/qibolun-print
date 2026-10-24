#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动修正v4新增29篇文章的分册分配"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
INCREMENT = ROOT / "research/online-increment/sooon-increment-20261009-195354.jsonl"
OUTPUT = ROOT / "v4_increment_final_assignment_2026-10-09.jsonl"

# 基于深度阅读的手动分配
MANUAL_ASSIGNMENTS = {
    # 1. 你的金字塔 - 关于旅游如何有意义，建立个人传统
    "f5a15cc2-3654-5b02-93cd-c9eb80640731": {
        "booklet": "B28",  # 消费主义与生活观念
        "reason": "讨论旅游的意义和个人生活习惯的建立，属于生活观念范畴"
    },
    
    # 2. 无可选 - 关于性取向确定的社会压力和现实考量
    "43b01e69-5aca-5c0f-9606-7de33d061afb": {
        "booklet": "B26",  # 性别议题与两性舆论
        "reason": "讨论性取向、社会压力、婚姻和子女问题，属于性别议题"
    },
    
    # 3. 言不灵 - 如何改善口吃
    "aea44bf2-eafa-5bfd-bc90-b857d786ce0f": {
        "booklet": "B17",  # 情志平复与容貌自和
        "reason": "讨论口吃改善方法，属于身心健康和自我调节"
    },
    
    # 4. 道不孤 - 朋友临时带人的社交应对
    "1841ca23-c968-526c-9732-cb0632ddd59b": {
        "booklet": "B15",  # 社交距离与孤立自处
        "reason": "讨论社交应对和朋友关系"
    },
    
    # 5. 家宴 - 儿媳不愿吃家常菜的家庭矛盾
    "1f4c6eee-0645-5484-a2c9-e9ae249b687f": {
        "booklet": "B06",  # 成年子女自立与边界
        "reason": "讨论成年子女回家、与父母的边界问题"
    },
    
    # 6. 智障 - AI解决数学问题对未来数学家的影响
    "3fa5c506-5ba2-5c2e-afb2-bde6bf8d8da0": {
        "booklet": "B29",  # 现代科技与工具反思
        "reason": "讨论AI对人类能力发展的影响"
    },
    
    # 7. 小妖怪 - 自媒体如何做起来
    "7734a82b-635f-57ac-a200-d57abde1ced0": {
        "booklet": "B22",  # 商业竞争与资产投资
        "reason": "讨论自媒体创业和商业策略"
    },
    
    # 8. 求助难 - 为什么很多人不愿求助
    "9526b6a7-4d36-540e-9f95-aa609dadc81c": {
        "booklet": "B15",  # 社交距离与孤立自处
        "reason": "讨论社交中的求助心理障碍"
    },
    
    # 9. 闹天宫 - 孩子在家总是挨骂
    "b45496c4-9bf0-5a66-abd5-b927ccda1bba": {
        "booklet": "B03",  # 言传身教与奖惩边界
        "reason": "讨论管教孩子的方式和边界"
    },
    
    # 10. 硅人 - AI是否有灵魂
    "bc3197a1-db3b-5e07-aebd-4dd239c71823": {
        "booklet": "B29",  # 现代科技与工具反思
        "reason": "讨论AI的伦理和法律地位"
    },
    
    # 11. 痴仙糖醇 - 什么是情绪价值
    "c060a3db-4dcd-59b6-9a07-93c35bcb4667": {
        "booklet": "B32",  # 名相辨析与语言牢笼
        "reason": "辨析'情绪价值'这个概念的真正含义"
    },
    
    # 12. 慧极则辱 - 中层管理者为什么难晋升
    "d30c2add-8d73-5547-bdfd-3af494b73ce7": {
        "booklet": "B20A",  # 职场汇报与权责留痕
        "reason": "讨论职场晋升和管理问题"
    },
    
    # 13. 末犬 - 为什么在成功前一刻搞砸
    "4e5f7a84-dc8c-51e3-9e4d-4bea4a90fe3e": {
        "booklet": "B19",  # 知行精进与克服拖延
        "reason": "讨论自我sabotage和心理障碍"
    },
    
    # 14. 勇字诀 - 对胆小怕事的人的建议
    "a415516b-ef0f-5e2b-b533-b2d8b26d8453": {
        "booklet": "B19",  # 知行精进与克服拖延
        "reason": "提供具体的行动建议克服胆小"
    },
    
    # 15. 团圆节 - 调休凑长假的意义
    "20cf887b-7c98-5868-9a7a-3c400bf8f5d4": {
        "booklet": "B06",  # 成年子女自立与边界
        "reason": "讨论背井离乡的子女与父母团聚"
    },
    
    # 16. 不恶道 - 代露娃向母亲求助被反问
    "2ab7ea5d-aec0-5b2e-9f18-ec4c1fa524ee": {
        "booklet": "B04",  # 亲子沟通与青春叛逆
        "reason": "深度讨论亲子沟通中的情感支持问题"
    },
    
    # 17. 直通天灵 - 开车犯困的应对方法
    "5a6aa784-cddd-5543-885c-3576e1ace333": {
        "booklet": "B18",  # 作息节律与病理常识
        "reason": "讨论疲劳应对和嗅盐的生理作用"
    },
    
    # 18. 教坊司 - 《兰香如故》中入教坊司的残酷
    "afbc352e-24dd-5bf7-8246-d9c5895fe075": {
        "booklet": "B30",  # 文明演进与社会秩序
        "reason": "讨论历史上的等级制度和社会结构"
    },
    
    # 19. 苦征 - 女儿只黏爸爸疏远妈妈
    "bd355e6d-bd3c-5842-bcca-7be88ea7552c": {
        "booklet": "B03",  # 言传身教与奖惩边界
        "reason": "讨论管教方式对亲子关系的影响"
    },
    
    # 20. 两条大道理 - 懂很多道理却过不好一生
    "04bb3a12-15d4-5f80-9801-971f61d6840c": {
        "booklet": "B34",  # 认识局限与心智模型
        "reason": "讨论知识与实践的鸿沟、认知陷阱"
    },
    
    # 21. 在爱中 - 在爱中仍感到孤独
    "efce39be-8add-502e-b6f4-9bdde826b478": {
        "booklet": "B17",  # 情志平复与容貌自和
        "reason": "讨论情感需求和心理孤独感"
    },
    
    # 22. 社会性超英 - 《兰香如故》为何成为爆款
    "2d6c3f61-81fa-5da8-9061-29b3b4305cc6": {
        "booklet": "B23",  # 公共热点与事件剖析
        "reason": "剖析影视作品热点现象"
    },
    
    # 23. 美文人 - 文笔好的人写网文难出圈
    "5af22fba-113d-5d11-83a1-d0e28c63cf48": {
        "booklet": "B01",  # 艺能创作与生活美学
        "reason": "讨论文学创作的方法和读者体验"
    },
    
    # 24. 冲刺马拉松 - 如何评价"让本科生做回本科生"
    "64c2a0d7-0f1f-56ef-820c-163647f5b011": {
        "booklet": "B27",  # 教育体制与社会流动
        "reason": "讨论本科教育和学生焦虑"
    },
    
    # 25. 羊 - 牧羊犬如何指挥羊群
    "658e26f6-dd99-57af-9a3f-23029497570d": {
        "booklet": "B30",  # 文明演进与社会秩序
        "reason": "通过动物行为类比社会秩序机制"
    },
    
    # 26. 必要的你 - 老婆想去月子中心被说没必要
    "88c68d22-f752-5276-9a75-012f1f6f344f": {
        "booklet": "B12",  # 婚姻存续与夫妻日常
        "reason": "讨论夫妻沟通中的语言伤害"
    },
    
    # 27. 并排躺 - 躺平命运也会推着你走吗
    "f52dcbbc-955e-570b-8be5-3baedf45d505": {
        "booklet": "B24",  # 青年心境与躺平反思
        "reason": "讨论躺平心态和命运机遇"
    },
    
    # 28. 就你 - 向内求的真正含义
    "754263b7-a85f-53c4-95fd-e04deb87e827": {
        "booklet": "B32",  # 名相辨析与语言牢笼
        "reason": "辨析'向内求'的概念，用交易成本理论解释"
    },
    
    # 29. 不辩而白 - 面对恶意揣测有必要解释吗
    "fe4d7838-a41e-503a-803e-de486ebb224a": {
        "booklet": "B15",  # 社交距离与孤立自处
        "reason": "讨论网络社交中的应对策略"
    }
}

# 册信息映射
BOOKLET_INFO = {
    "B01": {"name": "艺能创作与生活美学", "volume": "V8"},
    "B03": {"name": "言传身教与奖惩边界", "volume": "V1"},
    "B04": {"name": "亲子沟通与青春叛逆", "volume": "V1"},
    "B06": {"name": "成年子女自立与边界", "volume": "V1"},
    "B12": {"name": "婚姻存续与夫妻日常", "volume": "V2"},
    "B15": {"name": "社交距离与孤立自处", "volume": "V3"},
    "B17": {"name": "情志平复与容貌自和", "volume": "V4"},
    "B18": {"name": "作息节律与病理常识", "volume": "V4"},
    "B19": {"name": "知行精进与克服拖延", "volume": "V4"},
    "B20A": {"name": "职场汇报与权责留痕", "volume": "V5"},
    "B22": {"name": "商业竞争与资产投资", "volume": "V5"},
    "B23": {"name": "公共热点与事件剖析", "volume": "V6"},
    "B24": {"name": "青年心境与躺平反思", "volume": "V6"},
    "B26": {"name": "性别议题与两性舆论", "volume": "V6"},
    "B27": {"name": "教育体制与社会流动", "volume": "V6"},
    "B28": {"name": "消费主义与生活观念", "volume": "V6"},
    "B29": {"name": "现代科技与工具反思", "volume": "V6"},
    "B30": {"name": "文明演进与社会秩序", "volume": "V6"},
    "B32": {"name": "名相辨析与语言牢笼", "volume": "V7"},
    "B34": {"name": "认识局限与心智模型", "volume": "V7"}
}

def main():
    # 加载增量文章
    articles = {}
    with INCREMENT.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                article = json.loads(line)
                articles[article["id"]] = article
    
    # 生成最终分配
    final_assignments = []
    for article_id, assignment in MANUAL_ASSIGNMENTS.items():
        article = articles[article_id]
        booklet_code = assignment["booklet"]
        booklet_info = BOOKLET_INFO[booklet_code]
        
        final_assignments.append({
            "article_id": article_id,
            "title": article["title"],
            "url": article["url"],
            "text_len": len(article.get("text", "")),
            "published_at": article["publishedAt"],
            "booklet_code": booklet_code,
            "booklet_name": booklet_info["name"],
            "volume_code": booklet_info["volume"],
            "assignment_reason": assignment["reason"]
        })
    
    # 写入最终分配
    with OUTPUT.open("w", encoding="utf-8") as f:
        for item in final_assignments:
            f.write(json.dumps(item, ensure_ascii=False, separators=(',', ':')) + "\n")
    
    print(f"✓ 最终分配已写入：{OUTPUT}")
    
    # 统计
    from collections import Counter
    volume_counter = Counter(item["volume_code"] for item in final_assignments)
    booklet_counter = Counter(item["booklet_code"] for item in final_assignments)
    
    print(f"\n分卷统计:")
    for vol in sorted(volume_counter.keys()):
        print(f"  {vol}: {volume_counter[vol]}篇")
    
    print(f"\n分册统计:")
    for booklet in sorted(booklet_counter.keys()):
        info = BOOKLET_INFO[booklet]
        print(f"  {booklet} {info['name']}: {booklet_counter[booklet]}篇")
    
    print(f"\n共29篇文章，分配至{len(booklet_counter)}个册")

if __name__ == "__main__":
    main()
