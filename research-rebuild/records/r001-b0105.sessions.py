# -*- coding: utf-8 -*-
"""批次 r001-b0105 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0105.sessions.py            # 写 out/r001-b0105.out.jsonl
  python3 records/r001-b0105.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0105"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0105.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f4ee69e7": {
  "analysis": {
   "question_context": "提问者问：为什么中国人很少宣传夏商周是奴隶制（Q001）。作者不直接回答宣传问题，而是自设一组系数与数值，推算青铜时代一个国家能否长期稳定地依赖奴隶劳动自我供养，并据此质疑上古是否遍地“奴隶制国家”。提问归属提问者，作者立场为质疑“夏商周=奴隶制国家”的默认说法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005","P006","P007","P008"], "summary": "先要求读者考虑几个前提问题，并依次自设食物盈余系数F、待遇倍增系数Q=3、无效人口系数N=40%、武力优势系数W=以一敌十、国防武力占比D=1/4，再宣布要算这些数据的含义。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019"], "summary": "以总人口10万、无效人口40%代入，列出P+S=6、S/10=0.75P，解出武士约7100人、奴隶约5.29万人，并追加妇孺占比与待遇倍数等假设。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P020","P021","P022","P023","P024","P025","P026","P027"], "summary": "由推算提出两个反问：奴隶占一半时奴隶主能否压住舍生忘死的造反；一半人口用石木器与原始低产作物能否产出供另一半脱产的剩余物资。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P028","P029","P030","P031","P032"], "summary": "给出经典奴隶制国家的两个条件：武力高出原始武器两个世代以上，以及一人生产盈余足以养活按几倍口粮计算的压倒性统治阶级；并称两条件未满足前国家不可能既完全依赖奴隶劳动又稳定存在。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P033","P034","P035"], "summary": "承认古代有蓄奴现象，但反问上古是否遍地“奴隶制国家”，并把争点压缩为“一打几？一养几？”。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047"], "summary": "按1养1继续推演监工比例与镇压难度，指出生产力越原始、武力领先越小，非奴隶劳动阶层占比就越高，并追问奴隶比例低到多少还能称为“奴隶制国家”。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P048","P049","P050","P051","P052","P053","P054","P055","P056","P057"], "summary": "以铁器之前没有规模性青铜农具、青铜只用于礼器兵器等、水利受数学与行政能力制约、小麦推广到汉代中晚期未完成、两汉主要作物仍是粟为例，论证春秋以前农业与武力条件没有重大变化，商代夏代偏离的可能性更小。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P058"], "summary": "以一段学术论文摘要（黄河流域史前至两汉小麦种植与推广研究）作为外部材料，交代小麦在黄河流域的推广分期与面食技术条件。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "经典意义上的奴隶制国家需要奴隶主掌握的武力高出原始武器两个世代以上，并且一人生产盈余足以养活压倒性数量的统治阶级成员。", "evidence": ["E8","E9"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在“面对原始武装以一当三”和“一人劳动可养活一人以上”两个条件满足之前，一个国家不可能同时做到完全依赖奴隶劳动自我供养并保持稳定存在。", "evidence": ["E10"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "按作者推算，奴隶占人口一半时，奴隶主未必有把握镇压舍生忘死的奴隶造反。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "一半人口的奴隶用石木器与原始低产作物劳作，其剩余物资比例天然不可能是一比一，只能是一比三以上，因此养活另一半脱产者存疑。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代确实存在蓄奴现象，但作者反问上古是否遍地都是“奴隶制国家”。", "evidence": ["E11","E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生产力越原始、武力领先幅度越小，非奴隶的劳动阶层占总人口的比例必然越高。", "evidence": ["E13"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "除非对石木器劳动效率、原始水利与作物效率或青铜冷兵器皮甲的武力水平有重大误解，春秋之前的国家不太可能大幅偏离作者描述的情形，商代夏代偏离的可能性更小。", "evidence": ["E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "铁器发明之前没有有规模的青铜农具，青铜几乎仅用于礼器、兵器、建筑构件和盛器这类无需耐磨的用途。", "evidence": ["E15","E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作物品种优化速度很慢：小麦的推广到汉代中晚期都没有完成，直到两汉主要作物都是粟，小麦要到唐代中后期才与粟取得对等地位。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "所引论文摘要称：小麦种植经漫长发展最终取代粟成为北方地区首要栽培作物，龙山时代最早出现后长期不受重视，从西汉晚期开始才大范围推广。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者追问：奴隶比例低到什么水平还可以称为“奴隶制国家”。", "evidence": []}
   ],
   "argument_steps": [
    "开头把“奴隶制国家”拆成可计算的问题，并声明要自设若干系数（F、Q、N、W、D）",
    "用一组具体假设（Q=3、N=40%、W=以一敌十、D=1/4、T=10万）算出武士约7100人、奴隶约5.29万人",
    "由此提出镇压能力与生产力两个反问，指出两个问题解决不了则国家无法长期稳定依赖奴隶",
    "给出经典奴隶制国家的两项条件（武力代差、生产盈余），并称“数学和逻辑不允许”",
    "让步：承认古代有蓄奴现象，但把争点定为“一打几、一养几”，并追问奴隶比例下限",
    "进一步以1养1推演监工比例，得出生产力越原始则非奴隶劳动阶层占比越高的推论",
    "以农具、水利、育种三方面的技术停滞（青铜农具、粟与小麦推广）佐证春秋以前不满足条件",
    "引用学术摘要作为作物推广史的外部材料，未展开论证收尾"
   ],
   "concept_usage": [
    {"term": "奴隶制国家", "meaning": "作者指能长期稳定地完全依赖奴隶劳动自我供养、并有能力镇压与对外扩张的国家形态；作者强调这是一个可被量化条件检验的判断，不是有蓄奴就算。", "evidence": "P027", "ambiguity": "作者未给出“奴隶比例低到多少仍可称为奴隶制国家”的界限，只在P046—P047提出该问。"},
    {"term": "食物盈余系数F／待遇倍增系数Q／无效人口系数N／武力优势系数W／国防武力占比D", "meaning": "作者自设的五个分析参数，用于把“一国能否靠奴隶供养”转成算术题。", "evidence": "P002", "ambiguity": "各系数的取值均为作者假设（Q=3、N=40%、W=以一敌十、D=1/4），文中未给数据出处。"},
    {"term": "无效人口", "meaning": "既不从事生产也不从事镇压的社会成员，如老人、儿童、大贵族、艺术家、诗人、祭司等。", "evidence": "P004", "ambiguity": "把艺术家、诗人、祭司与老弱并列为“无效”，是作者本文的用法。"},
    {"term": "一打几？一养几？", "meaning": "作者对争论焦点的压缩提法：武力上一对几能压制、经济上一人养活几人。", "evidence": "P035", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "美国南北战争之前的白人农场主拥有火枪、黑人奴隶基本只有草叉——作者举为“武力代差”的例证（P028）",
    "井田制是否真的存在？（P051）——作者引作“春秋时期农业有多艰难”的延伸阅读链接，该段被渲染标注为lexical未覆盖片段",
    "青铜农具成本高于石质农具而效能没有好多少、青铜只用于礼器兵器等——作者的技术论据（P052、P053）",
    "水利需要高度发达数学与行政能力、大量富余劳动力——作者以“没有蛋哪有鸡”说明其不可得（P054）",
    "小麦推广分期与面食技术（转磨、筛粉、发酵）——引自学术论文摘要（P058）"
   ],
   "conditions": [
    "限定在“青铜时代”与“使用石头和木棍劳动”“原始水利、原始作物”的条件下（P002、P048）",
    "所设数值均为假设：F未定，Q假设为3且作者称“这真的很低了”，N假设为40%且称“很乐观了”，W假设为一敌十，D假设为1/4（P003、P004、P006、P007）",
    "考虑外敌入侵时需抽调1/4武士上前线，且奴隶主不会人人上前线（P011、P022）",
    "明确前提条件为“面对原始武装以一当三”和“一人劳动可养活一人以上”（P031）",
    "用“除非……否则”句式限定结论：除非对劳动效率与武力水平有重大误解（P048）"
   ],
   "rhetoric_and_tone": "以设问与反问推进（“看明白这两个问题了吗？”“请回答这两个问题”），把论战压缩成算术题；语气自信、带嘲弄与训诫色彩（“数学和逻辑不允许”），使用口语化第三人称“ta”，并用编号问题分点。",
   "unresolved_questions": [
    "作者自设的全套参数（F、Q=3、N=40%、W=以一敌十、D=1/4）没有给出史料或统计出处，属假设性推演，需外部核查其代表性",
    "P051“井田制是否真的存在？”被渲染标注为“lexical未覆盖片段”，正文与lexical结构不完全一致，该链接内容未核验",
    "P058为学术论文摘要，正文只附篇名《黄河流域史前至两汉小麦种植与推广研究》，未给作者、刊物与链接，需外部核查",
    "P018“假设奴隶主们可以以一当九，也就是武力倍增系数是10”与P006“以一敌十”在表述上存在数字不一致，作者未解释",
    "作者没有回答提问者所问的“为什么中国人很少宣传夏商周是奴隶制”，只从条件上质疑该说法的前提",
    "“无效人口”把艺术家、诗人、祭司计入不事生产者，其比例假设（40%）是否适用于具体古国，文中未说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "一个奴隶，在青铜时代，能生产出几倍于ta自己份额的口粮？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "我们把这个倍数设为“待遇倍增系数”Q，我们假设是3", "relation": "context"},
    {"key": "E3", "paragraph_id": "P004", "quote": "我们假设为40%，这很乐观了。", "relation": "context"},
    {"key": "E4", "paragraph_id": "P006", "quote": "我们假设为以一敌十吧。", "relation": "context"},
    {"key": "E5", "paragraph_id": "P014", "quote": "可以求得 P = 6 / 8.5 = 0.71", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P023", "quote": "奴隶主们能不能有把握压得住？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P026", "quote": "只能是一比三以上", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P028", "quote": "需要奴隶主们掌握的武力高出原始武器两个世代以上", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P029", "quote": "足够养活能压倒性的战胜ta自己的数量的统治阶级成员", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P031", "quote": "一个国家不可能同时做到既完全依赖奴隶劳动自我供养，又保持稳定存在", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P033", "quote": "古代有没有蓄奴现象？那当然有。", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P034", "quote": "是不是遍地“奴隶制国家”？", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P045", "quote": "非奴隶的劳动阶层占比就要越高", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P048", "quote": "除非我们对使用石头和木棍劳动的效率以及使用原始水利、原始作物的效率，或者使用青铜冷兵器和皮甲的武力水平有什么重大误解", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P052", "quote": "铁器发明之前，是没有有规模的青铜农具的", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P053", "quote": "青铜几乎仅被用于礼器、兵器、建筑构件和盛器这类无需耐磨的用途", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P055", "quote": "光一个小麦的推广，就到了汉代中晚期都没有完成", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P058", "quote": "小麦种植经过漫长的发展,最终取代粟成为北方地区的首要栽培作物", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史", "先秦史", "社会经济史", "农业史"],
   "issue_candidates": ["夏商周社会性质", "奴隶制国家的判定条件", "青铜时代生产力与武力水平", "井田制与先秦农业技术"],
   "text_function_candidates": ["论辩", "推演/估算", "答疑", "引用材料"],
   "object_candidates": ["夏", "商", "春秋", "美国南北战争前的南方", "黄河流域"],
   "working_keywords": ["奴隶制国家", "食物盈余系数", "待遇倍增系数", "无效人口系数", "武力优势系数", "国防武力占比", "井田制", "青铜农具", "粟", "小麦"]
  },
  "notes": "本篇无图片节点，故无图像缺口。P051（“井田制是否真的存在？”）被渲染标注为“lexical未覆盖片段”，正文与lexical结构不一致，已记入unresolved_questions。P058为quote字段的学术摘要，已按引用材料（quoted_or_cited/cited_source）处理，未计入作者主张。全文参数为作者自设假设，未提供史料出处。"
 },
 "bb09d50d": {
  "analysis": {
   "question_context": "提问者问：“你为什么不接受有过外国男朋友的女生？”（Q001，属提问者立场）。作者没有正面回答该择偶理由，而是以第二人称“你”推演：一旦公开表达这种把女性当“水果”挑拣的态度，说话者自己会落入由“好水果”掌握定价权的卖方市场。作者本人是否持有“不接受”的立场，本文未明说，故不归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002"], "summary": "先承认“不接受有过外国男朋友的女生”本属个人自由，乍看也像是避免“淘金女”或“低质女”的有效策略，随后宣告要推演接下来的剧情。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003","P004","P005","P006","P007"], "summary": "推演第一层：“优质女”不能接受对“劣质女”的嘲讽，绝大多数女性都不能接受以挑水果的心态对任何女性评头论足；能接受的“极少数”是自认“好水果”、理应卖好价钱的那些。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008","P009","P010","P011"], "summary": "推论：这些话一说出口且为人所知，说话者就只剩“好水果”可选；同时持相同观点、同样看不出后果的“同伴”很多，作者以“反女权”风气炽烈为旁证。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012","P013","P014","P015","P016"], "summary": "结果：说话者要与大量同观点的“朋友”一起在“好水果”面前被挑选，形成定价权完全在“好水果”手上的卖方市场；唯一反转条件是同观点者人数比“好水果”少一半，而作者称这种数学可能性从未在宇宙历史上出现过。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P017"], "summary": "以一句英文作结，点出“又一重诗意反讽”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“不接受有过外国男朋友的女生”本来是一种个人自由，乍看也像是避免“淘金女”或“低质女”的有效策略。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绝大多数女性归根到底都不能接受他人以挑水果的心态对任何女性评头论足。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能接受这种态度的“极少数”，是自认为“好水果”、理应卖出好价钱的那些人。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这些话一旦说出口并为人所知，说话者就只剩下那些“好水果”可选。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "持相同观点且同样看不出这些话后果的“同伴”很多，作者以“反女权”风气炽烈为旁证。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "说话者将与大量赞同其观点的“朋友”一起在“好水果”面前被挑选，形成定价权完全在“好水果”手上的卖方市场。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "该局面唯一的反转条件是持此观点者的人数比“好水果”少一半。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认上述人数反转的可能性，称这种数学上的可能性从未在这个宇宙的历史上出现过。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "让步：承认这种拒绝本属个人自由，乍看是避免“淘金女/低质女”的有效策略",
    "以第二人称“你”预告要推演“接下来的剧情”",
    "前提一：“优质女”不能接受对“劣质女”的冷嘲热讽；“绝大多数女性”不能接受以挑水果心态评头论足",
    "界定例外：自认“好水果”、理应卖好价钱的是“极少数”",
    "推论一：这些话公开后，说话者只剩“好水果”可选",
    "前提二：同观点且看不出后果的“同伴”很多，以“反女权”风气炽烈为旁证",
    "推论二：说话者与同观点者一起被“好水果”挑选，形成卖方市场，定价权在“好水果”手上",
    "给出唯一反转条件（同观点者少于“好水果”一半），随即否认其可能性",
    "以英文短句作反讽收束"
   ],
   "concept_usage": [
    {"term": "挑水果", "meaning": "作者用来指把女性按条件分等挑拣、评头论足的心态；“好水果”指自认条件好、理应被出高价的女性。", "evidence": "P006", "ambiguity": "“优质女/劣质女/好水果”均为加引号的标签，作者未给判定标准。"},
    {"term": "卖方市场", "meaning": "作者指选择权与定价权集中在被挑选方（“好水果”）手中的局面。", "evidence": "P015", "ambiguity": "借经济学词用于婚恋择偶语境，非严格定义。"},
    {"term": "庞加莱重现", "meaning": "作者借以夸张表示某情形连极小概率的复现都不可能。", "evidence": "P016", "ambiguity": "属修辞性借用，不是物理学论证。"}
   ],
   "examples_and_targets": [
    "“淘金女”“低质女”——作者转述该拒绝立场的预设对象，属被讨论的话术（P001）",
    "“优质女”“劣质女”——作者加引号使用并作为推演对象的标签（P004）",
    "“好水果”——作者对被挑选方中自认条件优越者的比喻性称呼（P007、P009）",
    "“反女权”的风气炽烈——作者举为同观点“同伴”很多的社会旁证（P011）",
    "庞加莱重现——作者用来说明该数学可能性从未出现的修辞性类比（P016）"
   ],
   "conditions": [
    "推演前提是说话者把这种挑拣态度“一说出口，而且为人所知”（P009）",
    "作者点明的唯一反转条件：持此观点者人数比“好水果”少一半（P015）",
    "推演对象是持该观点的“你”与“好水果”之间的择偶局面（P014、P015）"
   ],
   "rhetoric_and_tone": "第二人称“你”的对话式反讽推演；通篇用“水果”隐喻（挑水果、“好水果”、卖个好价钱），语气讥讽、调侃，以“首先”“于是”“同时”“结果”分段推进，结尾用英文短句“Yet another poetic irony.”收束。",
   "unresolved_questions": [
    "提问者问“你为什么不接受有过外国男朋友的女生”，作者未正面回答择偶理由，也未说明自己是否持有该拒绝立场",
    "“优质女”“劣质女”“好水果”均无判定标准，“绝大多数女性”的判断也没有依据或来源",
    "“反女权”风气被引为旁证，但未给出来源、范围或时间",
    "结尾英文短句未附中文，其所指的反讽对象（说话者还是局面本身）未明说"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这本来是一种个人自由，乍看起来似乎也是一种“避免淘金女”或者“避免低质女”的有效策略。", "relation": "qualifies"},
    {"key": "E2", "paragraph_id": "P006", "quote": "绝大多数女性，追根到底都是不能接受你对任何女性用挑水果的心态评头论足的", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "是自认为是“好水果”，理应卖出个好价钱的那些", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "你就只剩下那些“好水果”可选了", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "和你观点一样而且一样看不出这些话的后果的“同伴”多的很", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P015", "quote": "这是一个如此完美的卖方市场，定价权永远的、完全的在“好水果”们的手上", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "除非哪天这样观点的兄弟们比“好水果”们人数还少个一半", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P016", "quote": "因为它就没在这个宇宙的历史上出现过", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋择偶", "性别议题", "社会心态"],
   "issue_candidates": ["择偶标准的公开表达及其后果", "婚恋议价权", "反女权风气"],
   "text_function_candidates": ["反讽推演", "驳论", "答疑", "寓言式评论"],
   "object_candidates": ["挑水果隐喻", "优质女/劣质女", "好水果", "反女权"],
   "working_keywords": ["挑水果", "好水果", "卖方市场", "定价权", "反女权", "个人自由", "庞加莱重现"]
  },
  "notes": "本篇无图片节点，故无图像缺口。全文为第二人称反讽推演，作者未明确表态自己是否持有“不接受有过外国男朋友的女生”的立场，已在 question_context 与 unresolved_questions 中标出。文中无引用出处、无数据来源，引号内标签为作者的转述性用法。"
 },
 "ae30c818": {
  "analysis": {
   "question_context": "提问者问：如何看待 H&M 在「禁用新疆棉花」一事后，疑似遭淘宝等多个电商平台下架？（Q001，属提问者）。作者不评论下架事件本身，而是从产业格局立论：服装与时尚是中国挑战下西方地位最危险的行业，中国已是世界服装产业压倒性霸主，时尚霸权的根基是经济与军事崇拜而非美学，H&M 此举暴露其决策层缺乏远见。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005"], "summary": "判断中国挑战下最危险的是服装与时尚行业；中国已是世界服装产业压倒性霸主（生产与消费），唯一欠缺的是品牌，而设计能力与第一梯队并无不可跨越的鸿沟，真正缺的是国家作为“根品牌”给“时尚”子品牌的授信。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006","P007","P008","P009"], "summary": "预测中美GDP领先地位交换后第一个遭毁灭性冲击的西方优势产业是时尚业，理由是时尚建立在文化崇拜之上，而文化崇拜的决定性基础是经济崇拜与军事崇拜；基础崩溃则时尚霸权支柱连环倒塌，且时尚业在中国面前已无多少技术护城河。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010","P011","P012"], "summary": "对 H&M 一类快时尚企业提出忠告：活过下一个二十年的关键是提前看懂巨变并站在正确一边，站错位置则投资与努力无意义；H&M 的致命处不在犯错，而在错误暴露其决策层丧失基本远见和嗅觉。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P013","P014"], "summary": "反驳担忧：即使西方时尚品牌全部撤出中国，也不会给中国消费者带来无法弥补的实质损失；若因越红线被列入制裁名单，它们会因质量、产量和成本崩溃而自我毁灭。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P015"], "summary": "以格言收束：世界原谅愚蠢，但对待傲慢极尽残忍。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在中国挑战面前地位最危险的行业就是服装行业和时尚行业。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国早已是世界服装产业的压倒性霸主，生产与消费都有压倒性优势，唯一尚欠缺的不过是品牌。", "evidence": ["E2","E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即使就品牌而言，经改开四十年市场洗礼与世界第一等规模的全产业链实践，中国的设计能力与第一梯队也并没有不可跨越的鸿沟。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正缺的甚至不是品牌本身，而是国家作为“根品牌”给“时尚”这个子品牌的授信。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "第一个会因为中美GDP领先地位的交换而面对毁灭性冲击的西方优势产业就是时尚行业。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "时尚建立在文化崇拜之上，而文化崇拜在某种决定性的意义上并非建立在美学价值上，而是建立在经济崇拜和军事崇拜之上。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说直白些，“美”在本质上就是“力的表现”（客气说法是美学本身有高度的政治性）。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "基础崩溃后支撑“时尚霸权”的支柱会连环倒塌，而时尚行业在中国面前早已谈不上多少技术护城河。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "类似 H&M 的快时尚企业想活过下一个二十年，关键是提前看懂这一巨变并提前站在正确一边；在历史潮流上站错位置，任何投资和努力都无意义。", "evidence": ["E10","E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "H&M 此次的致命处不在犯错本身，而在于该错误揭示出其决策层丧失了基本的远见和嗅觉。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "即使把西方时尚品牌加在一起全部撤出中国，也无法给中国消费者带来任何实质上无法弥补的损失。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若因某些行为明确超出红线而被中国列入制裁名单，这些企业会因质量、产量和成本的崩溃而迅速招致自身毁灭。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界常常原谅愚蠢，但对待傲慢总是极尽残忍。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "直接判断：在中国挑战面前最危险的是服装行业和时尚行业",
    "事实前提：中国是世界服装产业的压倒性霸主，只缺品牌；设计能力与第一梯队无不可跨越的鸿沟",
    "进一步界定缺口：真正缺的是国家作为“根品牌”对“时尚”子品牌的授信",
    "预测：中美GDP领先地位交换后，时尚业是第一个遭毁灭性冲击的西方优势产业",
    "理由：时尚建立在文化崇拜之上，文化崇拜的基础是经济崇拜与军事崇拜；“美”本质是“力的表现”",
    "推论：基础崩溃使时尚霸权支柱连环倒塌，且时尚业在中国面前已无技术护城河",
    "忠告：快时尚企业要活过下一个二十年，须提前看懂巨变并站在正确一边",
    "评价 H&M：致命处在暴露决策层丧失远见与嗅觉",
    "反驳担忧：西方品牌全部撤出也不会造成无法弥补的损失；若被制裁会自我毁灭",
    "格言式收束"
   ],
   "concept_usage": [
    {"term": "根品牌", "meaning": "作者用语：国家作为整体为“时尚”这一子品牌提供的信用背书（授信）。", "evidence": "P005", "ambiguity": "非既有术语，作者未说明如何取得或衡量。"},
    {"term": "文化崇拜／经济崇拜／军事崇拜", "meaning": "作者认为文化崇拜的决定性基础是经济与军事崇拜，而非美学价值本身。", "evidence": "P007", "ambiguity": "未给论证或经验依据。"},
    {"term": "时尚霸权", "meaning": "作者指西方在时尚领域的主导地位，其支柱是文化崇拜。", "evidence": "P009", "ambiguity": "未界定霸权的具体范围与判据。"},
    {"term": "技术护城河", "meaning": "作者借商业用语指行业的技术壁垒；称时尚行业在中国面前已谈不上多少。", "evidence": "P009", "ambiguity": "未给技术或成本数据。"}
   ],
   "examples_and_targets": [
    "H&M——被评论的具体对象，作者称其行为为“蠢行”并评其决策层丧失远见（P010、P012）",
    "中美GDP领先地位的交换——作者设为时尚业受冲击的前提事件（P006）",
    "西方时尚品牌全部撤出中国——作者设定的假设情境（P013）",
    "被中国列入制裁名单——作者设定的假设情境（P014）",
    "改开四十年、世界第一等规模的全产业链实践——作者用作中国设计能力的经验依据（P004）"
   ],
   "conditions": [
    "前提事件：中美GDP领先地位的交换（P006）",
    "假设情境：“即使把西方的时尚品牌加在一起，全部撤出中国”（P013）",
    "条件句：“如果因为某些行为明确的超出了红线而被中国列入制裁名单”（P014）",
    "限定语：文化崇拜“在某种决定性的意义上”不是建立在美学价值上（P007）"
   ],
   "rhetoric_and_tone": "短段落层层递进的产业—品牌—授信—文化崇拜推演；语气自信、带训诫与轻蔑（“致命处”“蠢行”“无意义”）；用“说得客气一点／说得直白一点”作对照表述，以对偶格言收束。",
   "unresolved_questions": [
    "提问者问的是 H&M 疑似被电商平台下架，作者完全没有评论下架事件本身，也未提供相关事实",
    "“中国早已是世界服装产业的压倒性霸主”“设计能力与第一梯队没有不可跨越的鸿沟”均无数据或出处",
    "“中美GDP领先地位的交换”没有时间表与判据",
    "“国家作为‘根品牌’给‘时尚’子品牌的授信”是作者自造提法，未定义如何取得或衡量",
    "作者称被制裁企业会因质量、产量和成本崩溃而毁灭，未说明机制与时限"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "其实在中国挑战面前地位最危险的行业就是服装行业和时尚行业。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "中国早已是世界服装产业的压倒性霸主，无论是生产还是消费，都拥有压倒性的优势。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "唯一尚有所欠缺的，不过是品牌而已。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "中国的设计能力与第一梯队其实也并没有不可跨越的鸿沟", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而是国家作为“根品牌”给“时尚”这个子品牌的授信", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "第一个会因为中美GDP领先地位的交换而面对毁灭性冲击的西方优势产业，就是时尚行业。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "文化崇拜在某种决定性的意义上并不是建立在美学价值上的，而是建立在经济崇拜和军事崇拜之上的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "“美”在本质上就是“力的表现”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "支撑“时尚霸权”的支柱会发生连环倒塌", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "想要活过下一个二十年的关键，就是提前看懂这个巨变的必然来临并且提前站在正确的一边", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "在这种历史潮流问题上站错位置，任何投资和努力都是无意义的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "而是这个错误揭示出其决策层丧失了基本的远见和嗅觉", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "也无法真的给中国消费者带来任何实质上无法弥补的损失", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "只怕它们瞬间就会因为质量、产量和成本的崩溃而招致自身的毁灭", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "世界常常原谅愚蠢，但是对待傲慢，总是极尽残忍。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系", "中美关系", "服装产业", "时尚产业", "商业评论"],
   "issue_candidates": ["禁用新疆棉花与品牌声明", "中国服装产业链地位", "时尚霸权的文化基础", "快时尚企业的战略选择"],
   "text_function_candidates": ["时评", "产业分析", "预测", "训诫"],
   "object_candidates": ["H&M", "服装行业", "时尚行业", "根品牌", "中美GDP"],
   "working_keywords": ["时尚霸权", "文化崇拜", "经济崇拜", "军事崇拜", "根品牌", "技术护城河", "快时尚", "新疆棉花"]
  },
  "notes": "本篇无图片节点，故无图像缺口。提问问的是 H&M 疑似被电商平台下架，作者未讨论该事件本身，属行业立论式回应，已记入 unresolved_questions。文中行业地位、GDP 交换与制裁后果等判断均无数据出处。"
 },
 "dc23c975": {
  "analysis": {
   "question_context": "提问者问：如何看待3月24日特斯拉美国官网宣布支持使用BTC付款？（Q001，属提问者）。作者不评价特斯拉或行情，而是质疑比特币“去中心化”这一最大神话，以三连反问扩大“中心化”的外延，并断言掌握印钞机的国家可以轻而易举完成“持有中心化”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002"], "summary": "给出判断：比特币最大的神话属性是“去中心化”，随即反问它是否真的去中心化。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003","P004"], "summary": "连续反问：中心化是否只有“发行机构中心化”一种；生产中心化、持有中心化是否也是一种中心化。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "点出要害：掌握着印钞机的国家可以轻而易举的完成持有中心化。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "比特币最大的神话属性是去中心化。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑比特币是否真的实现了去中心化。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：中心化并不只有“发行机构中心化”这一种。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：生产中心化、持有中心化同样是一种中心化。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "掌握着印钞机的国家可以轻而易举的完成持有中心化。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "先给判断：比特币最大的神话属性是“去中心化”",
    "第一问：它真的去中心化了吗",
    "第二问：中心化是否只有“发行机构中心化”一种（扩大中心化的外延）",
    "第三问：生产中心化、持有中心化是否也是一种中心化",
    "点出要害：掌握印钞机的国家可以轻而易举完成持有中心化，未展开论证即收束"
   ],
   "concept_usage": [
    {"term": "去中心化", "meaning": "作者称其为比特币最大的“神话属性”，即不受单一中心控制；并以反问质疑其成立。", "evidence": "P001", "ambiguity": "作者未给出判定去中心化的标准。"},
    {"term": "持有中心化", "meaning": "作者提出的中心化类型之一，指持有集中于少数主体，并称掌握印钞机的国家可轻易达成。", "evidence": "P005", "ambiguity": "未给数据、门槛或机制。"},
    {"term": "生产中心化", "meaning": "作者列举的另一种中心化，指生产（挖矿）环节的集中；文中只有一句反问。", "evidence": "P004", "ambiguity": "未展开解释。"},
    {"term": "发行机构中心化", "meaning": "作者作为对照提出的传统中心化形式，即由发行机构集中发行。", "evidence": "P003", "ambiguity": "未说明它与生产/持有中心化的关系。"}
   ],
   "examples_and_targets": [
    "比特币——被质疑的对象，其“去中心化”被作者称为最大的神话属性（P001）",
    "掌握着印钞机的国家——作者指出的可完成“持有中心化”的主体（P005）",
    "特斯拉支持BTC付款（Q001）——属提问者的提问背景，作者正文完全未涉及"
   ],
   "conditions": [
    "作者的核心质疑均以反问形式提出，未给出成立条件或判定标准（P002—P004）",
    "“掌握着印钞机的国家可以轻而易举的完成持有中心化”未说明在何种制度、市场或时间条件下（P005）"
   ],
   "rhetoric_and_tone": "全文由一句判断加三连反问构成，短促、质问式；“记住这个要害”带训诫与提示口吻；称去中心化为“神话属性”含讽刺意味，未展开论证即收束。",
   "unresolved_questions": [
    "作者没有回答提问者所问的“如何看待特斯拉支持BTC付款”，全文未提特斯拉或该事件",
    "“它真的去中心化了吗”没有给出正面结论或判定标准",
    "“掌握着印钞机的国家可以轻而易举的完成持有中心化”未给机制、数据或实例",
    "“生产中心化”在文中只有一句反问，未展开",
    "正文极短（111字、5段），除判断与反问外没有论证过程"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "说句实话，比特币最大的神话属性是去中心化。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它真的去中心化了吗？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "中心化只有“发行机构中心化”这一种中心化吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "生产中心化、持有中心化，就不是一种中心化吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "掌握着印钞机的国家可以轻而易举的完成持有中心化", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["加密货币", "金融", "货币制度"],
   "issue_candidates": ["比特币去中心化神话", "中心化的类型", "国家对货币的控制"],
   "text_function_candidates": ["质疑", "短评", "设问"],
   "object_candidates": ["比特币", "去中心化", "持有中心化", "生产中心化", "印钞机"],
   "working_keywords": ["比特币", "去中心化", "中心化", "持有中心化", "生产中心化", "发行机构", "印钞机"]
  },
  "notes": "本篇无图片节点，故无图像缺口。正文仅5段111字，brief 与正文 P001—P005 完全重复，未用于支持任何主张。作者未回应提问的特斯拉付款事件，核心质疑均为反问且无展开，已在 unresolved_questions 记明。"
 },
 "deb200e0": {
  "analysis": {
   "question_context": "提问者问：如何看待 Nike、优衣库、GAP、Zara 等品牌均在境外官网发布「禁用新疆棉花」的声明？（Q001，属提问者）。作者针对“很多人担忧国际巨头集体弃用新疆棉花会造成巨大影响、乃至代表欧洲态度”的悲观情绪，主张欧美企业没有本钱抛开中国服装产业链，并预测它们会假装禁止而实际继续利用中国产能。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004"], "summary": "指出很多人担忧国际巨头集体弃用新疆棉花会造成巨大影响、乃至代表欧洲态度；作者表示不这么悲观，理由之一是欧美企业没有本钱抛开中国的服装产业链。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005","P006"], "summary": "引用海关口径的2020年纺织品服装出口统计（含美国、欧盟、日本市场份额），并称中国份额接近一半，且该口径未计入香港出口与中企在孟加拉、越南、巴基斯坦等国的出口额，那些厂也是中国的投资、机械、管理技术与原料配件。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007","P008","P009"], "summary": "中国纺织服装产业链在量产成衣领域已形成领先（甚至垄断）优势；离开中国的面料、做工与低成本，欧美设计师要失去发挥空间或品牌品质并面对利润损失；以服装业竞争残酷的反问强调代价。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010","P011","P012","P013"], "summary": "竞争对手会借“违禁面料”的巧妙设计“教你做人”；禁令只会把游戏变成大家假装禁止、实际比谁更会“合法违规”；更能利用中国产能的同行能要它们的命，真不用者不配活着。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P014","P015","P016","P017","P018"], "summary": "跨国企业连童工、奴工都用，“验厂”只是行礼如仪与事后解释的表演；它们面对利润装傻并有全套法律文件证明无辜，承诺都有合法方案保证不影响其实际行为，可以完全合法地抛弃承诺，其主导的司法体系以此为中心原则。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P019","P020","P021","P022","P023","P024"], "summary": "资本主义（尤其抛弃道德责任、以货币本位利润为追求者）是逆道德的竞争；它们从未抛弃更低成本、更可靠产能与更大市场；反其道而行是以退为进欺骗更天真的同类，“一起涨价”“一起不买”都是为了搞死真听信者。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P025","P026","P027"], "summary": "至于欧洲的态度，真正合作之前经“试要更高价—被迎头痛击”的过程，有利于形成真诚长久的友谊，以“不打不相识”等俗语作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述：很多人担忧这些“国际巨头”集体“弃用新疆棉花”会造成“巨大影响”，乃至认为这“代表欧洲的态度”，并为此忧心忡忡。", "evidence": ["E1","E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者明确表示自己不像那些人一样悲观。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧美这些企业其实没有本钱抛开中国的服装产业链。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "所引海关统计称：2020年全国纺织品服装出口2912.2亿美元、同比增长9.6%，接近历史最好水平；2020年1—11月中国占美国纺织品服装进口市场比重提高5.1个百分点至39.6%。", "evidence": ["E5","E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国在相关进口市场中接近一半份额，且该口径未计入香港出口额与中企在孟加拉、越南、巴基斯坦等国的出口额——那些厂也是中国的投资、纺织机械、管理技术和原料配件。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在量产成衣领域，中国纺织服装产业链已形成领先优势——如果不是垄断优势的话。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "离开中国先进纺织技术提供的面料、做工和低成本，欧美设计师不是失去发挥空间，就是失去品牌品质，还要面对利润损失。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问强调服装行业竞争残酷，容不下更贵的价格、更差的品质和更累赘繁琐的设计。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "竞争对手会借“违禁面料”的巧妙设计“教你做人”；禁令只会把游戏变成大家假装禁止、实际比谁更会“合法违规”；更能实际利用中国产能的同行就能要它们的命。", "evidence": ["E11","E12","E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "跨国企业连童工、奴工都用，所谓“验厂”只不过是行礼如仪、事后用来解释“验过了奈何ta们太狡猾”的表演。", "evidence": ["E14","E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "跨国企业面对利润可以装傻并有全套法律文件证明自己无辜，其任何承诺都有完全合法的系统方案保证不影响实际行为，因而能完全合法地抛弃承诺——其主导的司法体系以此为中心原则建立。", "evidence": ["E16","E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "资本主义——尤其抛弃道德责任、完全以货币本位利润为追求者——在任何意义上都是逆道德的竞争。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称它们从未做到抛弃更低的成本、更可靠的产能与更大的市场（原文作“从来没有做到过抛弃过”，存在双重否定歧义）。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "它们看似反其道而行，实为以退为进地欺骗更天真的同类：“我们一起涨价”是要搞死真听信去涨价者，“我们一起不买”是为了搞死真不偷买者。", "evidence": ["E20","E21","E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "就欧洲的态度，在真正达成合作之前经过“试试能不能要到更高价—被迎头痛击”的过程，有利于形成真诚、长久的友谊。", "evidence": ["E23","E24"]}
   ],
   "argument_steps": [
    "先摆出被转述的担忧：国际巨头集体弃用新疆棉花会造成巨大影响、代表欧洲态度",
    "表态：作者不这么悲观，理由是没有本钱抛开中国服装产业链",
    "引海关统计快讯：2020年出口接近历史最好水平，中国在美欧日市场份额上升（美国39.6%）",
    "补充口径限定：未计入香港出口与中企在第三国的出口，那些厂也是中国的投资、机械、管理技术与原料配件",
    "强化前提：量产成衣领域中国已形成领先（甚至垄断）优势；离开中国面料、做工与低成本将失去设计空间、品质与利润",
    "以服装业竞争残酷的反问说明代价",
    "推演连锁反应：竞争对手借“违禁面料”借口、禁令变成比谁更会“合法违规”的新游戏、更能利用中国产能者胜出",
    "举证跨国企业行为：童工奴工、“验厂”表演、法律文件与承诺的合法抛弃、司法体系以利润为中心",
    "上升判断：资本主义是逆道德的竞争，从未放弃更低成本、更可靠产能与更大市场",
    "解释其“反其道而行”为以退为进的欺骗：“一起涨价”“一起不买”意在搞死真听信者",
    "转到欧洲态度：先“试要更高价—被迎头痛击”有利于形成真诚长久的友谊，以“不打不相识”收束"
   ],
   "concept_usage": [
    {"term": "国际巨头", "meaning": "作者加引号统称集体声明弃用新疆棉花的耐克、优衣库、GAP、Zara 等跨国品牌企业。", "evidence": "P001", "ambiguity": "正文未逐一点名，只以引号统称。"},
    {"term": "违禁面料／违禁原料", "meaning": "作者指跨国企业口中被禁止使用的原料（如新疆棉），并称其“大家都心知肚明子虚乌有”。", "evidence": "P010", "ambiguity": "作者以引号使用，未说明认定标准。"},
    {"term": "验厂", "meaning": "作者指跨国企业对供应链的合规审核，称其只不过是行礼如仪与事后解释的表演。", "evidence": "P015", "ambiguity": "未给具体案例或证据。"},
    {"term": "合法违规", "meaning": "作者加引号的提法：名义禁止之下，各家企业实际比谁更会利用规则继续使用中国产能。", "evidence": "P011", "ambiguity": "作者自造表述，未界定合法与违规的边界。"}
   ],
   "examples_and_targets": [
    "Nike、优衣库、GAP、Zara（Q001）——提问者列举的品牌，作者正文以“国际巨头”统称，未逐一点名核对",
    "海关总署统计快讯、中国纺织国际产能合作企业联盟——被引数据与其标注出处（P005）",
    "美国、欧盟、日本市场的中方纺织品服装进口占比——作者用作中国产业链地位的证据（P005）",
    "孟加拉、越南、巴基斯坦等国开办的中国企业、香港出口额——作者说明统计口径外的中国产能（P006）",
    "童工、奴工——作者在“验厂”议题上的举证（P014）",
    "CIA——作者以“跨国企业的情报能力怕不比CIA还要专业”作夸张类比（P014）",
    "“我们一起涨价”“我们一起不买”——作者举为以退为进、诱使同类上当的话术（P022、P023）",
    "欧洲的态度——作者回应的另一项外界担忧（P025）"
   ],
   "conditions": [
    "全部立论以“它们其实没有本钱抛开中国的服装产业链”为前提（P004）",
    "关于欧洲态度的判断以“在真正达成合作之前”为条件（P025）",
    "对“合法违规”的推演以禁令被公开宣示而缺乏可核查执行为背景（P010—P012）",
    "中国份额的说明以“这种口径里一般都还没有计入香港的出口额，也没有计入在孟加拉、越南、巴基斯坦等国开办的中国企业的出口额”为限定（P006）"
   ],
   "rhetoric_and_tone": "口语化、戏谑而自信的驳论；大量反问与第二人称“你／你们”，用“千年的狐狸”“耿直少年”“教你做人”“要你的命”“不配活着”等俚俗夸张表述，把商业竞争写成算计博弈；对“验厂”“承诺”用讽刺性引号，结尾用“不打不相识”“杀千刀”等市井俗语调侃，带训诫与看破世情的语气。",
   "unresolved_questions": [
    "P005 所引2020年海关统计数据的口径、发布日期与“接近一半来自中国”的对应关系需外部核查",
    "P005 标注出处为“中国纺织国际产能合作企业联盟”，但内容含海关总署快讯与美国、欧盟、日本官方数据，转引层级不明",
    "提问者所称“禁用新疆棉花”声明的具体内容与主体，正文未逐一点名核对",
    "“跨国企业连童工、奴工都用”“验厂只是表演”等为概括性断言，未给案例或证据",
    "P020“它们从来没有做到过抛弃过更低的成本和更可靠的产能”含双重否定，语义存在歧义",
    "欧洲态度是否“代表”这些企业的立场，作者未直接回应提问者的这一层担忧",
    "P013“那你真的不配活着”与P027“要不是个小没良心杀千刀的”的指代对象（企业、同行还是读者）需结合语境判断"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我发现很多人在担忧这么多“国际巨头”集体“弃用新疆棉花”，会造成“巨大影响”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "乃至于“代表欧洲的态度”，感到忧心忡忡。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "其实我倒没这么悲观。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不是看不起欧美这些企业，它们其实没有本钱抛开中国的服装产业链。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "2020年1-12月全国纺织品服装出口2912.2亿美元（该口径不含94章褥垫、睡袋及其他寝具），同比增长9.6%", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "中国占美纺织品服装进口市场比重较2019年提高了5.1个百分点至39.6%", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "那些厂也是中国的投资、中国的纺织机械、中国的管理技术、中国的原料配件", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "中国纺织服装产业链已经形成了领先优势——如果不是垄断优势的话", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "离开了中国的先进纺织技术所提供的面料、做工和低成本", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "谁能容你以比别人贵的价格、比别人差的品质，提供比别人累赘繁琐的设计？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "你的那些会通过巧妙的设计，假扮善意第三人“受骗上当”“不小心”使用了“违禁面料”的竞争对手自然会教你做人。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "实际上在比谁更会“合法违规”的新游戏而已", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "ta比你更能实际利用中国的产能，ta就能要你的命。你还真以为那些同行真的就不用了啊？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "ta们连童工、奴工都用", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "所谓“验厂”只不过是行礼如仪，只是事后用来解释“我们都验过了奈何ta们太狡猾”的表演而已。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "它们面对利润可以装起一切的傻，而且会有全套的法律文件证明自己是真的傻，完全无辜。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "它们可以完全无辜的、完全合法的抛弃自己的一切承诺", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "在任何意义上都是逆道德的竞争", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "它们从来没有做到过抛弃过更低的成本和更可靠的产能，更不用提更大的市场。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "都是在以退为进的首先想要欺骗更天真一些的同类", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "其实是要搞死那几个真听信了去涨价的", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "其实是为了搞死那几个真的就不偷买了的", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "有利于形成“真诚的、长久的友谊”", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "老话说得好——不打不相识。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际贸易", "中美关系", "服装产业", "供应链", "资本主义批判"],
   "issue_candidates": ["禁用新疆棉花", "跨国企业对中国供应链的依赖", "统计口径与市场份额", "企业承诺与合规表演", "欧洲态度"],
   "text_function_candidates": ["驳论", "时评", "产业分析", "讽刺"],
   "object_candidates": ["国际巨头", "新疆棉花", "中国服装产业链", "海关总署", "美国/欧盟/日本市场", "验厂", "欧洲"],
   "working_keywords": ["新疆棉花", "违禁面料", "合法违规", "验厂", "童工奴工", "以退为进", "不打不相识", "海关统计"]
  },
  "notes": "本篇无图片节点，故无图像缺口。P005 为 quote 字段的转引材料（海关统计快讯数据），按 quoted_or_cited/cited_source 处理；其标注出处为“中国纺织国际产能合作企业联盟”，转引层级与数据时效需外部核查。P001—P002 为作者转述“很多人”的担忧，按 author_reported/unknown 处理，并另记作者本人判断，未归给提问者或作者。P020 的双重否定歧义已记入 unresolved_questions。"
 },
 "5fc52502": {
  "analysis": {
   "question_context": "提问者问：如何看待中伊签署25年全面合作协议？（Q001，属提问者）。作者认为很多人对该协议的意义看得过于理想，主张其“目前来说”主要是中伊双方用来向美国施压的共享筹码，暂不成其为“反美大计划”，执行到什么程度要看美国接下去怎么走。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002"], "summary": "指出很多人把协议意义看得过于理想，其表现是认为协议既然签了，就可以按“将被理想的执行”来看待后果。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003","P004"], "summary": "给出作者判断：协议目前的主要意义仍是中伊向美国施压的共享筹码，暂不成其为“反美大计划”；对双方而言，手持协议等于向美国喊话“你希望我执行到什么程度，就看你要怎么做”。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005","P006"], "summary": "分两种情形推演：美国不上道则积极执行；美国上道则可消极执行，但若再逼人太甚则由消极转积极。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007","P008"], "summary": "限定：美国只需对任一方做出实质让步即可导致协议被消极执行，但让步也只能把协议的最高目标转换成最低目标；两个千年古国也不会因美国让步就一点都不执行。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P009","P010"], "summary": "结论：执行到什么程度要看美国接下去怎么走；即使只是改变美国棋路并达到最低目标，已是很大的进步。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多人对这份协议的意义看得过于理想了。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述这种理想化的表现：认为协议既然签了，就可以按照“将被理想的执行”来看待其后果。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "客观来说，该协议目前的主要意义仍应是中伊双方用来向美国施压的共享筹码，暂时还不成其为“反美大计划”。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对双方而言，手持这份协议等于向美国喊出“这份协议你希望我执行到什么程度，就看你要怎么做”（作者拟想的喊话）。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "美国如果“不上道”，中伊这边就会积极执行协议。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "美国如果“上道”，中伊这边也可以消极执行，但美国别得意忘形——什么时候又逼人太甚，就什么时候消极转积极。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "美国只需对协议双方中的任何一方做出实质让步，都可以导致协议被消极执行；但即使让步，也不过是把协议的最高目标转换成最低目标。", "evidence": ["E7","E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作为两个千年古国，中伊不会短视到因为美国的让步就一点都不执行。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "协议虽然签了，但到底执行到什么程度还是要看美国接下去怎么走。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即使只是因此改变了美国的棋路，外加达到协议约定的最低目标，都已经是很大的进步了。", "evidence": ["E11"]}
   ],
   "argument_steps": [
    "指出很多人把协议意义看得过于理想，其表现是认定协议会“被理想的执行”",
    "给出判断：协议目前主要是中伊向美国施压的共享筹码，暂不成其为“反美大计划”",
    "以一句拟想的喊话界定协议性质：执行到什么程度取决于美国怎么做",
    "分两种情形推演：美国不上道则积极执行；美国上道则可消极执行，再逼人太甚则由消极转积极",
    "限定：美国对任一方实质让步即可导致协议被消极执行，但让步也只把最高目标换成最低目标",
    "补充：两个千年古国不会因美国让步就一点都不执行",
    "结论：执行程度要看美国接下去怎么走",
    "收尾：即使只改变美国棋路并达到最低目标，已是很大的进步"
   ],
   "concept_usage": [
    {"term": "共享筹码", "meaning": "作者指中伊双方共同持有、用来向美国施压的谈判筹码，而非既定的共同行动计划。", "evidence": "P003", "ambiguity": "未说明筹码的具体交换内容。"},
    {"term": "“反美大计划”", "meaning": "作者加引号指被理想化的解读，即把协议看作中伊联合反美的宏大计划；作者称暂时还不成其为该计划。", "evidence": "P003", "ambiguity": "何谓“大计划”未界定。"},
    {"term": "积极执行／消极执行", "meaning": "作者用来描述协议执行程度的两种取向，随美国态度而调整。", "evidence": "P005", "ambiguity": "未说明具体措施与判定标准。"},
    {"term": "最高目标／最低目标", "meaning": "作者指协议目标存在高低两档；美国即使让步也只能把最高目标转换成最低目标。", "evidence": "P007", "ambiguity": "文中未列出目标内容。"}
   ],
   "examples_and_targets": [
    "美国——协议施压与让步的对象，作者推演中的关键第三方（P004—P010）",
    "中伊双方——协议签署方，作者以“我这边”“两个千年古国”指称（P005、P006、P008）",
    "“这份协议你希望我执行到什么程度，就看你要怎么做”——作者拟想的对美喊话，属修辞性拟言（P004）"
   ],
   "conditions": [
    "情形一：美国“不上道”→积极执行（P005）",
    "情形二：美国“上道”→可以消极执行；若再逼人太甚→消极转积极（P006）",
    "触发条件：美国对协议双方中的任何一方做出实质让步→协议可被消极执行（P007）",
    "限定：两个千年古国不会因美国让步就一点都不执行（P008）",
    "全部判断限定为“目前来说”“暂时”（P003）"
   ],
   "rhetoric_and_tone": "以“我感觉很多人……”开头作降温式评论；用“你如果不上道／你如果上道”“你啥时候又逼人太甚，我啥时候消极转积极”等口语化条件句拟想对美喊话；语气冷静、务实并带调侃，人称上把中伊写成“我这边”（拟言），最后以有限度的肯定作结。",
   "unresolved_questions": [
    "协议的具体条款、期限与约定目标（最高目标、最低目标分别指什么）正文完全未列",
    "P004—P006 中“我这边”是作者代协议双方拟想的喊话，作者本人立场与协议方立场未作区分说明",
    "“积极执行”“消极执行”的具体措施与判定标准未说明，也未给实例",
    "“美国上道／不上道”的判断标准未给出",
    "提问者问“如何看待”该协议，作者未评价协议条款或签署本身，只推演执行程度",
    "正文未给任何消息来源或依据，全部为作者推断"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我感觉很多人对这个协议的意义看得过于理想了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "就是认为这个协议既然签了，就可以按照“将被理想的执行”来看待其后果了", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这个协议目前来说主要意义仍然应该是中伊双方用来向美国施压的共享筹码，而暂时还不成其为“反美大计划”", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这份协议你希望我执行到什么程度，就看你要怎么做", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你如果不上道，那么我这边就会积极执行，到时候你别后悔。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你啥时候又逼人太甚，我啥时候消极转积极", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "美国只需要对协议双方中的任何一方做出实质让步，都可以导致这份协议被消极执行", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "即使做出实质让步，也不过是将协议的最高目标转换成最低目标罢了", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P008", "quote": "自然也不会短视到因为美国的让步就一点都不执行", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "到底执行到什么程度还是要看美国接下去怎么走", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "即使只是因此而改变了美国的棋路，外加达到了协议约定的最低目标，都已经是很大的进步了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系", "中东研究", "中美关系", "外交战略"],
   "issue_candidates": ["中伊25年合作协议的性质", "协议执行程度与对美博弈", "制裁与让步的互动"],
   "text_function_candidates": ["时评", "降温式评论", "情形推演", "预测"],
   "object_candidates": ["中伊25年协议", "美国", "共享筹码", "反美大计划"],
   "working_keywords": ["中伊协议", "共享筹码", "反美大计划", "积极执行", "消极执行", "实质让步", "最高目标", "最低目标"]
  },
  "notes": "本篇无图片节点，故无图像缺口。作者未评价协议条款本身，也未回应提问者“如何看待”的全部层面，只推演执行程度对美国的依赖；P004—P006 的“我这边”为代协议双方拟想的喊话，非作者自称，已在 unresolved_questions 记明。正文无来源标注与日期信息（除元数据）。"
 },
 "4f24deca": {
  "analysis": {
   "question_context":"提问者问狗不理停业及老字号品牌困局。作者不从市场经营技巧回答，而是把品牌定义为守护者和家族长期信仰、信用与牺牲的对象。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010"],"summary":"品牌要靠家族前赴后继的虔诚守护；若把品牌只当赚钱工具，经营困难时就容易掺水造假。","role":"thesis"},{"unit_id":"U002","paragraph_refs":["P011","P012","P013","P014","P015","P016","P017"],"summary":"品牌被提升为超越个体生命的对象，守护者应在家族延续失败时交给合适继承者。","role":"definition"},{"unit_id":"U003","paragraph_refs":["P018","P019","P020","P021"],"summary":"作者区分信仰与管理、营销，批评只靠金钱和故事塑造品牌，最终以狗不理被营销派接手为反面结论。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"真正的品牌需要守护者把品牌发扬光大置于个人赚钱和生存之上，并长期保持信用。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"品牌问题根本上是信仰问题，而不是经营或营销技巧问题。","evidence":["E3"]}],
   "argument_steps":["将品牌守护定义为家族式信仰（P001-P003）。","以掺水造假和产品瑕疵说明逐利逻辑如何破坏信用（P004-P010）。","把品牌提升为超生命并要求传承（P011-P017）。","批评堆钱、讲故事和营销派，收束到狗不理案例（P018-P021）。"],
   "concept_usage":[{"term":"品牌","meaning":"由长期守护、信用、牺牲和传承构成的超越个体生命的对象。","evidence":"P011-P018","ambiguity":"作者未讨论现代公司制、股权和职业经理人如何承担这种守护。"},{"term":"信仰","meaning":"在顺逆境中仍不叛逃、不以短期生存交换品牌质量的坚持。","evidence":"P019-P021","ambiguity":"标准高度道德化，缺少可操作判定。"}],
   "examples_and_targets":["狗不理、乐视、锤子作为品牌失败或营销化的例子（P020-P021）。"],
   "conditions":["产品瑕疵发生在家族仍有健康成员和可节省资源时，作者认为不可原谅（P006-P010）。","品牌守护者需要有可继承、可传承的长期承诺（P014-P018）。"],
   "rhetoric_and_tone":"宣言式、道德化和宗教隐喻浓厚，使用绝对化判断、反问和格言式排比。","unresolved_questions":["作者没有具体分析狗不理停业的经营、产品、消费者或制度原因。","‘信仰’如何与现代企业治理、资本和员工关系兼容，正文未说明。"],
    "evidence":[{"key":"E1","paragraph_id":"P001","quote":"需要一个家族前赴后继的、宗教性的虔诚付出","relation":"supports"},{"key":"E2","paragraph_id":"P004","quote":"如果你认为品牌只是你赚钱的工具","relation":"supports"},{"key":"E3","paragraph_id":"P018","quote":"品牌问题，从根本上不是一个经营问题，而是一个信仰问题","relation":"supports"}]},
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；作者采用高度规范性的品牌定义，未对狗不理停业事实作外部核验。"
 }
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')
    args = ap.parse_args()
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row['article']
        uid = UID_BY_ID[art['id']]
        if uid not in ANALYSIS:
            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))
        p = ANALYSIS[uid]
        records.append(build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', '')))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
