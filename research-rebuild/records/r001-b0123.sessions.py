# -*- coding: utf-8 -*-
"""批次 r001-b0123 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0123.sessions.py            # 写 out/r001-b0123.out.jsonl
  python3 records/r001-b0123.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0123"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0123.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "da098d20": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问“字体字库未来前景怎么样？”（Q001，属提问者）。作者不预测字库市场前景，而是提出一项政策主张：把颜体、柳体、瘦金体等传统字体作为民族文化遗产由国家牵头提取、标准化、免版权，并强制预装于在华销售电子产品；同时以“浸润”论与“技术成本已不成问题”论支撑该主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "政策主张：政府牵头提取标准化传统字体资源并豁免版权，设为法定必备字体、强制预装，违者禁售。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "收益与正当性：收益远超成本；属民族文化遗产，投资推广理所当然，应融入日常生活。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "损失论证：身边罕见传统字体，文化细节流失，长期隔绝伤害文化传承且可能不可逆，审美日本化、香港化、欧美化。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "批评设计界：抄日语设计中的纯汉字部分，因缺少书法浸润而只能走捷径，结果是残缺、落后一等。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "纠正路径：单有书法教育不够，必须从受众端建立“这才是汉字正常的样子”的认知基线，迫使设计方以此为基础，才能建立中国自己的审美体系。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023"], "summary": "文化正统论：中国是汉语言文明永远的核心，其灵魂装进别的容器必是阉割；此事未被重视是重大失误。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "制度主张：基准字形资源是公共事业，只能由中央政府创设、维护与发布；这是文化统一和治理，不能成为商家专利，应列为高优先等级。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036"], "summary": "回应技术成本顾虑：清晰度、webfont流量、存储三项限制已大幅下降甚至早已不是问题，强制推行的技术基础早已成熟。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P037", "P038", "P039"], "summary": "收束：中国已承受不自知的重大损失；技术由不可妥协的市场需求催生，先有需求就不必担心技术。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张：中国应由政府牵头投入预算，对文化遗产级别的字体资源予以提取和高质量标准化，并作为永久的人类公共文化财富豁免一切版权费用。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张把这些字体设为法定必备字体，强制在华销售的所有电子产品系统平台预置安装并提供完全支持，不符合要求者应禁止在中国市场销售。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者判断中文的国际地位、文化市场份额与中文媒体设计水准必定因此获益良多，且收益远远超过完成这项工作的成本。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这是民族文化遗产，投资和推广理所当然；不把这些字体直接放进汉字使用的日常生活体验中是一种很大的损失。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者判断长期把传统字体隔绝在中国人日常生活之外对文化传承存在伤害，时间久了甚至不可逆；并称中国人的汉字审美甚至文化审美已严重日本化、香港化甚至欧美化。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为要纠正此问题单有“书法教育”不够，必须从受众端建立不假思索的认知基线，让公众潜意识锁定传统字形才是汉字正常的样子，从而迫使一切设计方以此为基础思考美感问题。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为汉字基准字形资源是不可交付给单独商家以所谓“市场竞争”自由博弈决定的公共事业，事实上只能由中央政府创设、维护与发布，事关文化正统地位乃至国本、正朔。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为以你的字形为基准者即绝对正统，只要使用汉字，在市场规律约束下就不能不以你所决定的字形为中心，这就是文化意义上的统一和治理。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问表达：如此公器，岂能成为某个商家的“专利”。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述一种被其反驳的顾虑：汉字传统字形的基准化有很高的技术成本。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为字体清晰度、webfont流量与响应成本、存储空间三项技术顾虑已大幅下降甚至早已不是问题，强制推行基准字形的技术基础早已成熟。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为技术是被不可妥协的市场需求催生出来的，先有不可妥协的市场需求，就不必担心没有足够可用的技术。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这件未被重视的事是汉字源头民族的一项重大失误，中国为此已承受不自知的重大损失。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "先提政策主张：政府牵头提取标准化传统字体并免版权（P001—P003）。",
    "给出强制手段：设为法定必备字体、强制预装、违者禁售（P004）。",
    "以收益大于成本与“民族文化遗产”作正当性理由（P005、P006）。",
    "用反问指出身边罕见传统字体的现状（P007）。",
    "论证损失：文化细节流失、传承受伤且可能不可逆、审美他化（P008—P010）。",
    "反驳设计界：抄日语设计的纯汉字部分，因缺少浸润只能走捷径（P011—P016）。",
    "提出纠正路径：不止书法教育，须从受众端建立认知基线（P017—P019）。",
    "预先回应不服气者，并转入文明正统论（P020—P023）。",
    "推出制度结论：基准字形属公共事业，只能中央政府创设维护发布，不可成为商家专利（P024—P028）。",
    "逐条回应技术成本顾虑（P029—P036）。",
    "以“技术由市场需求催生”收束（P038、P039）。"
   ],
   "concept_usage": [
    {"term": "浸润", "meaning": "作者强调的、区别于“教育”的长期生活经验式熏染，需从受众端建立。", "evidence": "P014", "ambiguity": "作者用“注意，不是教育，而是浸润”作区分，但未给出可操作的判定标准。"},
    {"term": "基准字形/基准字体", "meaning": "作为全社会设计基准的传统汉字字形资源，须由国家统一创设发布。", "evidence": "P024", "ambiguity": "具体包含哪些字体、以何标准取舍，正文只给举例未定规则。"},
    {"term": "公器", "meaning": "作者用以指称汉字字形资源，强调其公共属性、不可为商家专利。", "evidence": "P027", "ambiguity": "未界定法律上的权利安排。"},
    {"term": "正统/正朔", "meaning": "文化正统地位与政权正当性象征的政治-文化语汇。", "evidence": "P025", "ambiguity": "属作者修辞性提升，未给出与字形标准的对应关系。"}
   ],
   "examples_and_targets": [
    "颜真卿、王羲之、柳公权、欧阳询、瘦金体、魏碑、小篆、隶书、楷书、行楷、仿宋、黑体、等线、幼圆、康熙字典体——作者列举的字体资源（P003）。",
    "颜体、柳体、真草隶篆——作者用以质问身边可见度的例证（P007）。",
    "日本设计、片假名平假名、欧美设计手法——作者批评的模仿对象（P011、P012、P015、P016）。",
    "视网膜屏、micro LED屏、webfont、64G手机存储——作者用于反驳技术成本顾虑的技术例证（P031、P033、P035）。",
    "初级设计师、“大师”们——作者的反驳对象与训诫对象（P020）。"
   ],
   "conditions": [
    "“不符合要求的，应禁止在中国市场销售”（P004）——强制预装主张的惩罚条件。",
    "“长期把它们隔绝在中国人的日常生活之外……时间久了甚至是不可逆的”（P009）——伤害成立的时间条件。",
    "“如果一家……”式的技术前提：作者称以前或许存在技术限制，现在已不再成为问题（P032、P036）。",
    "“对方只要使用汉字，在市场规律的约束下就不能不以你所决定的字形为中心跳舞”（P026）——正统效应成立的条件。",
    "“先有不可妥协的市场需求，就不必担心没有足够可用的技术”（P039）——技术供给的前提条件。"
   ],
   "rhetoric_and_tone": "政策倡议书兼训诫文。以“应该”“必须”“岂能”“说不过去”“活该”等强断言与反问推进；大量第二人称“你们”直接质问读者（P007、P011、P020）；用“阉割”“尸”“镶金嵌玉”“抱着饭碗要饭”等激烈比喻；把字体问题提升到“国本、正朔”“文化意义上的统一和治理”的高度；技术上则以逐条回应顾虑的方式收敛论证。",
   "unresolved_questions": [
    "本篇含 2 个图片节点（IMG001、IMG002，src 见结构），图片内容未经核验，需人工/多模态复核；正文中未见对这两张图的文字说明。",
    "提问者所问“字体字库未来前景”未获市场角度的直接回答。",
    "“这些字体”的完整清单与取舍标准，正文仅以举例与“等”字带过。",
    "政策主张的成本预算规模、实施机构与法定期限，正文未说明。",
    "强制预装与厂商技术中立、版权豁免的具体法律路径，正文未说明。",
    "版本信息：updated_at（2024-12-20）晚于 published_at（2021-05-18），差异内容未提供。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中国应该由政府牵头投入预算对文化遗产级别的字体资源予以提取和高质量标准化", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "这些字体应该设为法定必备字体", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "不符合要求的，应禁止在中国市场销售。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "必定会因此获益良多，远远超过完成这项工作的成本", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "这是民族文化遗产，这点投资和推广是理所当然的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "不给它们最大的机会直接出现在汉字使用的直接生活体验中，这是一个很大的损失", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "这对文化传承是存在伤害的——时间久了甚至是不可逆的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "中国人的汉字审美甚至文化审美严重地日本化、香港化甚至欧美化了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "单有“书法教育”是不够的，必须要有浸润。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "潜意识里就锁定“这才是汉字正常的样子”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P024", "quote": "其基准字形资源是一个不可以交付给单独商家来通过所谓“市场竞争”来自由博弈决定的公共事业", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "它事实上只能由中央政府来创设、维护与发布。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "对方只要使用汉字，在市场规律的约束下就不能不以你所决定的字形为中心跳舞。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P027", "quote": "如此公器，岂能成为某个商家的“专利”？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "有一种顾虑，说汉字传统字形的基准化有很高的技术成本。", "relation": "context"},
    {"key": "E16", "paragraph_id": "P031", "quote": "这些问题实际上已经不是问题了。", "relation": "contradicts"},
    {"key": "E17", "paragraph_id": "P036", "quote": "强制推行基准字形的技术基础早已成熟。再不动作，说不过去。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P038", "quote": "技术是被不可妥协的市场需求催生出来的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P039", "quote": "先有不可妥协的市场需求，就不必担心没有足够可用的技术。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P037", "quote": "中国为此已经承受了不自知的重大损失，这不应该继续下去。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文字字体设计", "文化政策", "文化传承", "国家标准化"],
   "issue_candidates": ["汉字基准字体标准化", "字体版权与公共文化财富", "电子产品强制预装", "汉字审美他化", "书法浸润与文化认同"],
   "text_function_candidates": ["政策倡议", "批评", "论辩", "答疑"],
   "object_candidates": ["中国政府", "中国设计师群体", "日本设计", "欧美设计", "颜真卿", "王羲之", "柳公权", "欧阳询"],
   "working_keywords": ["基准字体", "法定必备字体", "浸润", "公器", "文化正统", "正朔", "webfont", "micro LED"]
  },
  "notes": "本篇含 2 个图片节点（IMG001、IMG002），图片内容未经核验，需图像核验；已读部分为正文文本。正文中提到“以下图片”式的图文配合未见明确指认，图片作用待复核。"
 },
 "f3fa6e52": {
  "analysis": {
   "question_context": "提问者问“中年人的解压方式是回家前在车里安静坐会，那青年人呢？”（Q001，属提问者，预设青年也应有某种解压方式）。作者不列举青年的解压方式，而是先追问“解压方式”的原理：解压属于明知问题已无可更改、唯一解法办不到而只能等待或承受的绝望处境（如等宣判、等开宝）；作者据此反驳提问前提，认为二三十岁的年轻人尚未绝望、还有力气，本应去消灭压力根源，根本就不应该学“解压”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "先问解压的原理：问题明知、后悔已晚、唯一解法办不到才叫绝望；不能整天绝望，只能让生活有点乐趣，否则会放弃。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "以赌注已下未开宝、庭审已毕等宣判类比“只能等”的时刻，指这种时刻才需要解压，即解压的原理。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "转向年轻人：可以后悔就该悔改；所谓绝望与“没办法”建立在靠不住的前提上；没绝望还有力气，就该消灭压力根源而非学解压。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "以“解压类似医用大麻，是给癌症患者用的”作类比，讥讽未到该处境却来问自己抽什么的人。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018"], "summary": "行动主张：什么造成压力就解决什么，不要用麻醉解决“压力”本身；P018为指向另一知乎回答的链接节点。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "澄清“解决压力根源”也含反思和解除无谓贪欲，但明确不等于“佛系”化；多数人拿食色欲望做促燃剂。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025"], "summary": "理由：应一开始就适应简朴生活，否则无盈余、被奢侈造成的贫穷逼迫，这种压力无法靠解决业务难点消除；被欲望刺激的斗志不足以支撑面对和承认业务问题。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "递进链条：解决业务困难的斗志←确信业务正确←无自欺欺人的疑虑←不害怕←不介意推翻原结论←简朴、有盈余、能帮人而有人情善意。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032", "P033"], "summary": "以“内圣则外王”点题：从根上解决吞吃心力的破洞，问题才能被承认、才能听所有声音；并讥讽对镜喊口号式的自信。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035"], "summary": "收束：解决不了业务困难的根源比业务本身深远；战术的勤奋无法解决战略的懒惰造成的错误。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出“解压”的原理：问题已明知、后悔已晚、解决不了，且恰恰是明知该怎么解决而唯一办法办不到，这才叫绝望。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断不能整天绝望，否则迟早会跳楼跳桥烧炭，其顾虑还在于一大家子此后慢慢被人踩死饿死的处境。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为只能好歹让生活里有点乐趣、有点当时舒坦的东西，否则一直苦一直丧怕是会放弃。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者用赌注已下、买定离手、尚未开宝，以及庭审完毕、陪审团闭门讨论、当事人在外等宣判作类比，指这种只能等的时刻才需要“解压”。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问二三十岁的年轻人：要后悔，可以后悔，为什么不直接悔改？", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者认为年轻人并不知道什么是唯一的解决办法，就算知道其实也不信，因此质问其“绝望”个啥。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断年轻人所谓的“没办法”“走投无路”建立在一些靠不住的前提上，经不起多少质问。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张没绝望就还有力气，就应该继续做有效的事去消灭压力根源，根本就不应该学习什么“解压”。", "evidence": ["E009"]},
    {"claim_id": "C009", "claim_type": "author_reported", "attribution": "unknown", "modality": "questioned", "statement": "作者转述被其批评的问法：癌症患者都有大麻抽，那我抽啥？并以“抽大耳刮子”作答。", "evidence": ["E010", "E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张什么造成压力就去解决什么，不要用麻醉解决“压力”本身。", "evidence": ["E012"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者补充“消灭压力的根源”也包括反思和解除自己无谓的贪欲，但明确这不是指“佛系”化。", "evidence": ["E013", "E014"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者判断若仅为自己的贪欲努力，当努力的痛苦超过对贪欲满足的期待，人很自然会选择“算了我不要了还不行吗”；大部分人都在拿食色欲望做促燃剂。", "evidence": ["E015", "E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张一开始就应学会享受、至少适应简朴生活，以去掉基于享乐欲望奋斗的理由；否则很难有盈余，被奢侈造成的贫穷逼迫，这种压力无法通过解决业务难点消灭。", "evidence": ["E017", "E018"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断被欲望刺激起的斗志总会自我劝解软化，硬软都不够，不足以支撑百折不回面对业务困难，甚至不足以承认自己业务的问题。", "evidence": ["E019", "E020"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出递进链条：解决业务困难的斗志建立在确信业务正确上，确信建立在没有自欺欺人疑虑上，不害怕建立在完全不介意推翻原结论上，而这份从容建立在本就简朴、有盈余、因常有余力帮人而有人情善意的底气上。", "evidence": ["E021", "E022", "E023"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“内圣则外王”概括上述由内而外的次序。", "evidence": ["E024"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为从根上解决吞吃心力和物力的破洞，问题才能先得到承认、才不讳疾忌医，才能听所有声音——并注明不包括梦游者的胡话，也不是一定要听从才叫听。", "evidence": ["E025"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定对镜喊口号式的自信，并反问喊就有用的话镜子和咽喉片哪能卖这么便宜。", "evidence": ["E026", "E027"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：解决不了业务上的具体困难，其根源要比业务本身深远得多；战术的勤奋无法解决战略的懒惰造成的错误。", "evidence": ["E028", "E029"]}
   ],
   "argument_steps": ["先对“解压”下定义：困境是明知问题、后悔已晚、唯一解法办不到，因此绝望（P002）。", "补充自杀风险与家人后果，得出只能让生活有点乐趣的结论（P003、P004）。", "用赌局与庭审等待作类比，把“解压”限定在只能等的时刻，并称这就是解压的原理（P005—P008）。", "转向对话对象（二三十岁的年轻人）：可以悔改、未必真知道唯一解法、也没真信，“没办法”的前提靠不住（P009—P011）。", "推出行动要求：没绝望就该消灭压力根源，不该学解压（P012）。", "以医用大麻作类比并训诫式作答“抽大耳刮子”（P013—P016）。", "给出正面主张：什么造成压力就解决什么，不用麻醉解决压力本身（P017）。", "预判误解，澄清“解决根源”含解除无谓贪欲，但非佛系化（P019—P022）。", "给出理由：应及早适应简朴，否则无盈余、被奢侈造成的贫穷逼迫，斗志会被食欲软化（P023—P025）。", "给出递进因果链至简朴—盈余—人情底气（P026—P029）。", "以“内圣则外王”点题，落到能承认问题、能听所有声音，并讽刺口号式自信（P030—P033）。", "结论：困难的根源比业务本身深远，战术勤奋无法弥补战略懒惰（P034、P035）。"],
   "concept_usage": [
    {"term": "解压", "meaning": "在明知问题无解、只能等待或承受时，用乐趣或麻醉让当时好过一点的做法；作者将其比作给癌症患者用的医用大麻，限定于真正绝望的处境。", "evidence": "P008", "ambiguity": "题面的“解压方式”指日常减压，作者改换了所指，两义在文中未明确区分。"},
    {"term": "绝望", "meaning": "明知唯一解决办法却办不到、已无可更改的状态；作者否认二三十岁提问者处于此状态。", "evidence": "P002", "ambiguity": "作者对“绝望”的判定标准（如何算办不到）未给出可操作界限。"},
    {"term": "贪欲／食色欲望", "meaning": "驱动奋斗的享乐欲望，被作者称为促燃剂，主张反思和解除。", "evidence": "P020", "ambiguity": "作者明确说解除贪欲不等于“佛系”化，但两者界限只在P021举例说明。"},
    {"term": "盈余", "meaning": "简朴生活留下的物质与心力余裕，是敢于推翻原结论、听所有声音的底气来源。", "evidence": "P029", "ambiguity": "未给出盈余的量化标准。"},
    {"term": "内圣则外王", "meaning": "作者用以概括先由内解决破洞、外部问题才可能被承认和解决的次序。", "evidence": "P030", "ambiguity": "作者未展开该词的经典含义，仅作格言式收束。"},
    {"term": "战术的勤奋／战略的懒惰", "meaning": "对举：具体业务上的勤奋不能弥补方向层面的懒惰造成的错误。", "evidence": "P035", "ambiguity": "“战略的懒惰”在本文中未进一步定义。"}
   ],
   "examples_and_targets": ["跳楼跳桥烧炭：作者用以描述长期绝望后果的修辞材料（P003）。", "赌注已下、买定离手、未开宝：类比（P005）。", "庭审完毕、陪审团闭门讨论、等宣判十年或死刑或无罪：类比（P005）。", "医用大麻与癌症患者：类比，用以界定“解压”的适用对象（P013、P014）。", "“抽大耳刮子”：训诫式修辞回答（P016）。", "“赚点钱全换车沟女夜店风光”：作者对奢侈消费的具体举例（P023）。", "镜子与咽喉片的价格：讽刺口号式自信的商业类比（P033）。", "P018“知乎用户：人如何克服自己的懒散习性？”：指向另一知乎回答的链接节点，非作者论证内容。"],
   "conditions": ["解压只在“明知问题、唯一解法办不到、只能等”的处境下才谈得上（P002、P005、P007）。", "如果没绝望、还有力气，就不应学解压而应消灭压力根源（P012）。", "“解压”类似的是给癌症患者用的医用大麻（P013）。", "解除贪欲不等于“佛系”化（P021）。", "能否听得进所有声音，以心里安定、有盈余为前提；不包括梦游者的胡话，也不是一定要听从才叫听（P031）。", "对话对象限定为“二三十岁的年轻人”（P009），题面所问的“中年人”属提问者设定，作者未采用。"],
   "rhetoric_and_tone": "第二人称“你们”“你”直接对话，连续反问（“为啥你不直接悔改？”“你们‘绝望’个啥？”“那我抽啥？”），讥讽与训诫并用（“抽大耳刮子”“镜子和咽喉片哪能卖这么便宜？”），大量类比（赌局、庭审、医用大麻、促燃剂、破洞），结尾以格言式短句收束（“内圣则外王”“战术的勤奋，无法解决战略的懒惰造成的错误”）。结构上是先给定义、再反驳提问前提、最后给出自己的正面主张与因果链。",
   "unresolved_questions": ["正文从“第二种”开始（P005），第一种在正文中未出现，疑为原答案分点被省略或结构合并，影响对完整分类的理解。", "P018为指向另一知乎回答的链接节点，其与上下文的论证关系不明。", "题面问“青年人的解压方式”，作者未正面列举任何青年的具体解压方式，而是质疑问题前提；本记录不把题面预设当作者立场。", "文中“你们”“你”的指称对象（提问者、提问者所属群体或其他对话者）正文未界定。", "作者未说明自身是否处于其描述的“第二种”处境。", "“梦游者的胡话”具体所指不明。", "发布时间2021-05-18与更新时间2023-05-26不一致，语料未说明是否含修订，本记录以当前版本正文为准。"],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "明知道要怎么解决，而这唯一的解决办法办不到，所以才绝望", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "不然迟早要跳楼跳桥烧炭", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "不然一直苦一直丧怕是会放弃", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "赌注已经下了，买定离手了，就是还没开宝", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P008", "quote": "这就是“解压”的原理。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "要后悔，可以后悔，为啥你不直接悔改？", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P010", "quote": "就算知道其实你们也不信，你们“绝望”个啥？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P011", "quote": "都是建立在一些靠不住的前提下的", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "你根本就不应该学习什么“解压”", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P014", "quote": "你跑来问“癌症患者都有大麻抽，那我抽啥？”", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P016", "quote": "抽大耳刮子。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P017", "quote": "什么造成压力，就去解决什么，不要去用麻醉解决“压力”本身。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P020", "quote": "也包括反思和解除自己无谓的贪欲", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P021", "quote": "注意，这不是指“佛系”化。", "relation": "qualifies"},
    {"key": "E015", "paragraph_id": "P021", "quote": "你很自然会选择“算了我不要了还不行吗”", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P022", "quote": "而大部分人都是在拿这种食色欲望在做促燃剂。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P023", "quote": "你一开始就应该学会享受——至少是适应——简朴的生活", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P023", "quote": "这种压力是无法通过解决业务难点消灭的", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P024", "quote": "总是会被“要不少吃点”的自我劝解软化", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P025", "quote": "甚至都不够你鼓足勇气去承认自己业务的问题的", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P026", "quote": "解决业务的困难点的斗志，建立在确信这是正确的业务基础上。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P027", "quote": "建立在没有“我为了害怕而自欺欺人”的疑虑的基础上", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P029", "quote": "反而因为时时有盈余去帮助人，因而有很多人对你有感情、有善意的底气上", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P030", "quote": "内圣则外王。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P031", "quote": "你才不会讳疾忌医", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P032", "quote": "对着镜子喊“我是最聪明的，我一定会成功”", "relation": "contradicts"},
    {"key": "E027", "paragraph_id": "P033", "quote": "喊就有用，镜子和咽喉片哪能卖这么便宜？", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P034", "quote": "其根源要比业务本身深远得多", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P035", "quote": "战术的勤奋，无法解决战略的懒惰造成的错误。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与情绪", "人生经验与建议", "事业与经营", "生活方式"],
   "issue_candidates": ["解压与压力管理", "绝望的判定条件", "青年与中年处境对比", "欲望与简朴生活", "自欺与恐惧", "业务困难的根源"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "经验总结"],
   "object_candidates": ["二三十岁的年轻人", "中年人", "癌症患者", "知乎提问者"],
   "working_keywords": ["解压", "绝望", "唯一解决办法", "医用大麻", "贪欲", "简朴", "盈余", "内圣则外王", "战术的勤奋", "战略的懒惰"]
  },
  "notes": "正文P005以“第二种”开头而未见“第一种”，疑有分点结构缺失或合并；P018为指向另一知乎回答的链接节点（“知乎用户：人如何克服自己的懒散习性？”），非正文论证。发布时间与更新时间不一致（2021-05-18／2023-05-26），语料未标注版本差异，本记录以当前版本正文为准。本篇无图片节点。"
 },
 "718d6642": {
  "analysis": {
   "question_context": "提问者问“如何看待中国的宗教问题？”（Q001，属提问者，无进一步限定）。作者不讨论宗教管理或社会影响层面，而是把中国的宗教问题判定为心态问题与神学／思想不努力的问题：先给三教（基督教、佛教、道教）分别下诊断，再指出“没有神学家、佛学家和道学家”以及未完成政教分离的神学建设这两个要害，并据“不勉强任何人才有真信”这一原则责备中国宗教界思想上的不努力。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总判断：中国的宗教问题主要是固步自封、自轻自贱的心态问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "三教分述：基督教欠缺与西方分支分庭抗礼的平视心态；佛教没有领导世界佛教的自觉；道教似乎只打算寄居在传统文化遗产与华人世界的余绪上。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "对照判断：中国宗教有天资、遗产与世界第一流的思想禀赋，不该是受制于人的短板，反而应成为向外输出文化成就的一部分。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "病因与后果：因受逼迫打击而怨恨执着、只求生存，不做神学哲学道学的真东西，近一个世纪只有“宗教事务”而无思想创见；结果是社会威胁未降，反而催生邪气渊薮、给外部势力操作空间。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "提出第二个要害：中国的宗教没有完成政教分离的神学建设。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "神学论证：真正超然的信仰对人类缺陷应有宽容；正统宗教应以勉强哪怕一个人为最大羞耻；任何人跟随都不应迫不得已；须完全保护一切人基于一切理由不信的自由，这是真信的底线。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018"], "summary": "由上述底线推出“不干政”原则，并反问既然不打算勉强任何人，为何要做可称为“施压”的事。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021"], "summary": "批评与规范：忧愁无压可施、无威可恃的“宗教”不过是窃取美好理念的帮派；正教最基本的自觉是与内部贪念做最坚决的斗争；怀着勉强人的邪念就不应享有自由。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "现状责备：中国宗教尚未自觉自愿遵奉此守则，反而引以为辱、视以为憾、疾以为仇，是基本境界的残缺；作者直言“是你们自己不够资格”，并称该领悟只是及格线。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "反问与因果链：你若是真理何必盘算勉强别人；没有不强迫的信心就根本算不上信；没想清楚→没信心→断不了念头→没有存在资格，故思想上的不努力是一切宗教问题的核心。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P030", "P031", "P032"], "summary": "条件性出路：若心甘情愿放下欲勉强而不得的执念，就获得谁也没理由不接受的存在资格，甚至有资格让自认“主干”“正统”的“源头支派”跪地忏悔。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038"], "summary": "对“源头支派”的贬斥与收束：它们得意的只是财雄势大、人强马壮，“欲勉强而竟可得”；无不必勉强之信心、无不可勉强之自觉，只是不自知的可怜虫；在其面前自卑并求认可令人发指。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断中国的宗教问题主要是一个固步自封、自轻自贱的心态问题。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者分述三教：中国的基督教欠缺与其西方分支分庭抗礼的平视心态，甚至都没有这样的追求；中国的佛教没有领导世界佛教的自觉；中国的道教似乎只打算寄居在中国传统文化那点遗产上，满足于华人世界里的那点余绪。", "evidence": ["E002", "E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国宗教有非常好的天资和遗产、世界第一流的思想禀赋，不该成为中国受制于人的短板，反而应成为中国向外输出文化成就的一部分。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断中国宗教界因自觉受逼迫打击而怨恨执着、注目于蝇营狗苟的“求生存”，不在神学、哲学、道学上做真正有价值的东西，近一个世纪以来只有所谓“宗教事务”而无任何思想创见，完全丧失了对信仰的真诚追求。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为没有神学家、佛学家和道学家，这就是中国宗教的主要问题。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这不但没有使宗教意识形态对社会的实际威胁下降，反而因诸教在思想上的腐化与迷茫化催生无数邪气十足的渊薮，并给外部势力极大操作空间、留下极大隐患。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出核心问题还有第二个要害：中国的宗教没有完成政教分离的神学建设。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为一个价值观真正超然、将生死荣辱置之度外、只求人类平安与幸福的意识形态，拥有对人类缺陷的宽容和理解是题中应有之义。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张一种正统的宗教应以“以自己的现实影响力勉强哪怕一个人”为最大的羞耻。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张任何人跟随都不应有一丝一毫迫不得已；世界上最后一个没有归信的人绝不能因为若不信就会丧失任何一种平等权利或者机会而屈服，其之前的任何一个人也理应如此。", "evidence": ["E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张要充分、完全、彻底地给予并保护一切人基于一切理由不信的自由，那些相信的才有真正的相信可言；这是任何真实信仰无可妥协、无可让步的底线。", "evidence": ["E015", "E016"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把这称为没有任何悬念、没有任何置辩余地的“不干政”原则，并反问：既不打算勉强任何人，为什么还要做可被称为“施压”的事。", "evidence": ["E017", "E018"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断一个处处忧愁自己无压可施、无威可恃、无势可仗的“宗教”，不过是一个窃取了美好理念的帮派，本来就不该有脸去要求生存空间。", "evidence": ["E019"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为宗教由人组成，人有看见自己人多就产生贪念的劣根性，所以任何一个正教最基本、最首要的自觉，就是与自己内部的一切这类贪鬼做最坚决的斗争。", "evidence": ["E020"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张唯其毫不勉强所以可以最大自由；心里怀着抱团勉强人的邪念不放下，就确确实实不应该享有自由。", "evidence": ["E021"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断中国宗教还没有做到自觉自愿将这一条视为天然遵奉的最基本守则，而是不情不愿、不忿不服，引以为辱、视以为憾、疾以为仇，这是最基本的境界的残缺，并直接对之说出“是你们自己不够资格”。", "evidence": ["E022", "E023"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者说明这就是他称中国宗教在神学上思想上不努力为最核心问题的原因，因为这个领悟和信念不过是值得人正眼相看的宗教的及格线。", "evidence": ["E024", "E025"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：你如果是真理，盘算着勉强别人干什么？连不计划使用任何强迫的信心都没有，就根本算不上信，也谈不上“真理必胜”。", "evidence": ["E026", "E027"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出因果链：没把自己该想的事情想清楚，所以没有这份信心；没有信心就断不了这个念头；断不了念头，就天然没有资格冒名顶替地存在。", "evidence": ["E028"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：你们在思想上的不努力，是一切宗教问题的核心。", "evidence": ["E029"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者给出条件性出路：思想上及格（只看是否心甘情愿放下一切欲勉强而不得的执念），就会因放下执念而获得谁也没理由不接受的存在资格。", "evidence": ["E030"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者进一步判断，届时你们会有资格让那些自认为是“主干”“正统”的“源头支派”跪地忏悔。", "evidence": ["E031"]},
    {"claim_id": "C023", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述被批评方的自我认知与得意：它们自认为是“主干”“正统”的“源头支派”，得意于自己现在财雄势大、人强马壮，所以“欲勉强而竟可得”。", "evidence": ["E032"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断它们既没有“不必勉强”的信心，也没有“不可勉强”的自觉，只不过是一群不自知的可怜虫，再亢奋也是扯淡。", "evidence": ["E033", "E034"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者责备中国宗教界：居然在这种要靠附和撒谎来求筹码的可怜虫面前自卑，甚至还要求ta们认可，你们在思想上的不努力令人发指。", "evidence": ["E035"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“所以，我说这是中国宗教的核心问题”收束全文。", "evidence": ["E036"]}
   ],
   "argument_steps": ["总判断先行：中国宗教问题是固步自封、自轻自贱的心态问题（P001）。", "分三教举例诊断，各给一条缺失（P002—P004）。", "对照给出正面估价：有天资、遗产与第一流思想禀赋，应向外输出（P005）。", "归因：因受逼迫而生怨恨执着、只顾求生存，近一世纪只有宗教事务而无思想创见（P006）。", "点名主要问题：没有神学家、佛学家和道学家（P007）。", "指出后果：社会威胁未降，反催生邪气渊薮、给外部势力留操作空间（P008、P009）。", "提出第二要害：未完成政教分离的神学建设（P010）。", "给出神学前提：超然信仰须宽容人类缺陷；勉强人为最大羞耻；跟随不得迫不得已；须保障一切理由不信的自由（P011—P016）。", "由前提推出“不干政”原则，并以反问排除施压的正当性（P017、P018）。", "反驳现状：无压可施却忧愁的“宗教”是窃取理念的帮派；正教须与内部贪念斗争（P019—P021）。", "责备中国宗教界未自觉遵奉此守则、境界残缺，并称其不够资格；指出这只是及格线（P022—P025）。", "以反问与因果链说明没有不强迫的信心就算不上信，故思想不努力是一切问题核心（P026—P029）。", "给出条件性出路与预言：若放下执念即可获存在资格，并令“源头支派”跪地忏悔（P030—P032）。", "贬斥“源头支派”的得意，并责备在其面前自卑求认可者；回到核心结论（P033—P038）。"],
   "concept_usage": [
    {"term": "宗教问题", "meaning": "本文不是指宗教管理或社会冲突，而是指心态上的固步自封、自轻自贱与神学／思想上的不努力。", "evidence": "P001", "ambiguity": "与通常所说“宗教问题”（政策、管理、极端主义）不同，作者未与其区分。"},
    {"term": "政教分离", "meaning": "作者把它作为神学建设问题提出，即宗教须在自身教义上完成“不干政”的根据。", "evidence": "P010", "ambiguity": "作者未讨论制度层面的政教分离安排，只讲神学根据。"},
    {"term": "不干政", "meaning": "由“不勉强任何人才有真信”推出的原则：不施压、不勉强任何个人或群体。", "evidence": "P017", "ambiguity": "作者未列举何种具体行为算“施压”或“干政”。"},
    {"term": "勉强／施压", "meaning": "以现实影响力使人迫不得已地跟随；作者视之为正统宗教的最大羞耻。", "evidence": "P012", "ambiguity": "未给出判定“迫不得已”的操作标准。"},
    {"term": "不信的自由", "meaning": "一切人基于一切理由不信的自由，被作者视为真信与真信仰不可让步的底线。", "evidence": "P015", "ambiguity": "未说明该自由在家庭、社群等非国家场域如何落实。"},
    {"term": "资格／存在资格", "meaning": "由放下勉强执念换得的、谁也没理由不接受的宗教存在正当性；反面是“不够资格”。", "evidence": "P030", "ambiguity": "“资格”的授予者与判定程序未说明。"},
    {"term": "正教／正统", "meaning": "作者用以指符合上述不干政底线的宗教，并以“及格线”作尺度。", "evidence": "P012", "ambiguity": "作者未点名哪些宗教符合，也未给出判定标准。"}
   ],
   "examples_and_targets": ["中国的基督教、中国的佛教、中国的道教：作者并列诊断的对象（P002—P004）。", "神学家、佛学家、道学家：作者指其缺失，用作思想不努力的证据（P007）。", "邪气十足的渊薮、外部势力：作者对后果的判断性表述，未点名具体组织（P008），属需外部核查的事实断言。", "自认为“主干”“正统”的“源头支派”：作者的反驳对象，正文未点名具体教派或机构（P032）。", "“近一个世纪以来”：作者用以界定其思想停滞判断的时间范围（P006）。", "“真理必胜”：作者引述并质疑的口号（P027）。"],
   "conditions": ["P001用“主要是”、P004用“似乎”，作者对三教诊断留有保留语气。", "P022的判断是现状判断（“还没有做到”），非不可改变之断言。", "P030的条件结构：以心甘情愿放下欲勉强而不得的执念为获得存在资格的条件。", "P014以“世界上最后一个没有归信的人”为极限情形设定，用以检验自由是否真实。", "P016把上述底线限定为“任何真实的信仰”的底线，未限定单一宗教。", "P006以“近一个世纪以来”为时间限定。"],
   "rhetoric_and_tone": "训诫与斥责为主，直接以“你／你们”对宗教界说话；反问密集（“否则你的‘信仰’算是个什么东西？”“你如果是真理，你盘算着勉强别人干什么？”“它们只不过在得意……罢了”）；断语与格言式短句（“是你们自己不够资格”“——再亢奋也是扯淡”）；贬称迭出（贪鬼、帮派、可怜虫、渊薮、扯淡）；结构上先总判、再分述三教、再点两处要害、再作神学论证、最后责备并收束回核心结论。",
   "unresolved_questions": ["作者批评的“自认为是‘主干’‘正统’的‘源头支派’”具体指哪些教派、教会或机构，正文未点名，主体不明。", "“邪气十足的渊薮”“外部势力”所指未说明，属需外部核查的事实断言。", "作者未给出判定“正教／正统”或“及格线”的可操作标准，也未点名哪些宗教符合。", "“近一个世纪以来”的起算时间与依据未说明，属需外部核查。", "作者后文举例多以“信仰”“真理”语汇展开，未说明是否主要针对基督教发言，指涉范围有歧义；本记录不替作者补足。", "文中“ta们”所指与“你们”是否同一对象（中国宗教界与“源头支派”的关系）存在歧义。", "平台话题标签是否混入正文：本次阅读包未见话题标签节点，语料未提供该字段，无法判断。", "发布时间2021-05-19与更新时间2025-10-11不一致，语料未说明是否含修订，本记录以当前版本正文为准。"],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "主要是一个固步自封、自轻自贱的心态问题", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "欠缺与其西方分支分庭抗礼的平视心态", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "没有领导世界佛教的自觉", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "只打算寄居在中国传统文化那点遗产上", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "反而应该成为中国向外输出文化成就的一部分", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "只有所谓“宗教事务”，而无任何思想创见", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "完全丧失了对自己信仰的真诚追求", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "没有神学家、佛学家和道学家，这就是中国宗教的主要问题。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "给了外部势力极大的操作空间，留下了极大的隐患", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "就是中国的宗教没有完成政教分离的神学建设", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "拥有对人类缺陷的宽容和理解是显而易见的题中应有之义", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "应以“以自己的现实影响力勉强哪怕一个人”为最大的羞耻", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "任何一个人跟随你，都不应该有一丝一毫迫不得已可言", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "绝不能是因为ta若不信就会丧失任何一种平等权利或者机会而迫不得已要屈服", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "那些相信的才有真正的相信可言", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P016", "quote": "这是任何真实的信仰无可妥协、无可让步的底线。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P017", "quote": "没有任何悬念、没有任何置辩余地的“不干政”原则", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P018", "quote": "你为什么要去做任何可以被称为“施压”的事？", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P019", "quote": "不过是一个窃取了美好理念的帮派，本来就不该有脸去要求生存空间", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P020", "quote": "就是要与自己内部的一切这类贪鬼做最坚决的斗争", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P021", "quote": "唯其毫不勉强，所以可以最大自由。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P022", "quote": "这是最基本的境界的残缺", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P023", "quote": "是你们自己不够资格。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P024", "quote": "这是我说中国的宗教在神学上思想上不努力是其最核心的问题的原因", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P025", "quote": "不过是一个值得人正眼相看的宗教的及格线", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P026", "quote": "你如果是真理，你盘算着勉强别人干什么？", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P027", "quote": "连不计划使用任何强迫的信心都没有，你自己就根本算不上信", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P028", "quote": "你就天然的没有资格冒名顶替的存在", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P029", "quote": "所以，你们在思想上的不努力，是一切宗教问题的核心。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P030", "quote": "你们自然会因为放下了这执念而获得谁也没理由不接受的存在资格", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P032", "quote": "让那些自认为是“主干”“正统”的“源头支派”跪地忏悔", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P033", "quote": "它们只不过在得意自己现在财雄势大、人强马壮", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P035", "quote": "只不过是一群不自知的可怜虫而已", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P036", "quote": "——再亢奋也是扯淡。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P037", "quote": "你们在思想上的不努力令人发指", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P038", "quote": "所以，我说这是中国宗教的核心问题。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与神学", "文化与思想", "政治与宗教关系", "社会批评"],
   "issue_candidates": ["中国宗教的思想停滞", "政教分离的神学根据", "不干政与不信的自由", "宗教的生存资格", "宗教领袖与神学家缺失", "对外来宗教支派的自卑心态"],
   "text_function_candidates": ["答疑", "评论", "批评", "论辩", "训诫"],
   "object_candidates": ["中国的基督教", "中国的佛教", "中国的道教", "中国宗教界", "“源头支派”", "外部势力"],
   "working_keywords": ["固步自封", "自轻自贱", "政教分离", "不干政", "勉强", "施压", "不信的自由", "及格线", "存在资格", "源头支派", "正教", "正统"]
  },
  "notes": "本篇无图片节点。正文中“自认为是‘主干’‘正统’的‘源头支派’”未点名，属主体不明，已记入未决问题；作者对“邪气十足的渊薮”“外部势力”的断言需外部核查，本记录不作事实裁决。发布时间2021-05-19与更新时间2025-10-11不一致，语料未说明版本差异。"
 },
 "7ac9cc0b": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问“自己做饭吃，怎样从极耗时的买菜、择菜、洗菜、切菜、配菜中解脱出来？”（Q001，属提问者）。作者以“时间审计”为方法框架，先把做饭拆成准备配料、清洗擦干主料、形状加工、预处理、慢速加工、烹饪调味、收拾清洗七个环节，再逐环节给出省时办法（买脱水配料与净菜、挑选好洗的菜、提前处理、用现成成品与智能家电、重新设计食谱），并夹入一段关于中国人应掌握毛笔字与菜刀等基本技能的训诫。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009"], "summary": "方法框架：先做时间审计，列出做饭耗时的七个环节，并判断每一环节都花时间、也都可挤时间。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "环节1配料：葱姜蒜可买脱水碎粒（也有汁液版本），对多数家庭味道上已足够替代，但用法有限制。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "环节2清洗擦干：可买超市净菜，关键在选对超市；以三条理由说明无须担心用剩菜做净菜，并给出规模与部位齐全的辨别法；豆类豆制品净菜可放心。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027"], "summary": "仍属清洗环节：多买好洗好做的菜、少买带泥多的叶子菜；批评对“新鲜”的偏执，主张保证卫生即可，理由是浪费的时间就是生命本身。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P028", "P029"], "summary": "补充建议：脱水食材有些很不错，其价值在于另一种食材味道，而不见得只为方便。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031"], "summary": "环节3形状加工：一方面由净菜解决，另一方面自己总要练点功夫。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "训诫性插叙：中国人写不好毛笔字、拿不住菜刀是傲慢的浪费，是“抱着饭碗要饭”；作者为喊“活不下去”设定前提，并提出别人对你“冷漠无情”至少还有这一种可能性。", "role": "context"},
    {"unit_id": "U008", "paragraph_refs": ["P040", "P041", "P042"], "summary": "环节4预处理：没必要每天吃大菜，须提前处理；给出用食品级塑料袋腌制的诀窍及其好处。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P043", "P044", "P045"], "summary": "环节5慢速加工：时间不够就别折腾需要耐心的手段，多做凉拌菜、炒菜；可用智能家电定时与远程启动。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050"], "summary": "环节6烹饪调味：要有计划性先切好放小碟子；多用现成糖色、卤汁；卤蛋卤豆腐可冷泡；冷卤不能卤猪蹄。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P051", "P052", "P053"], "summary": "环节7收拾碗筷：以图片提问碗的共性、是否好洗，并指出有预成型产品可买（两处均以未核验的图片为内容）。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059"], "summary": "收束：列出不花时间的食物，建议重新设计食谱（一凉菜、一外购卤菜、只需再做一个菜），熟练后怕是比方便面还快。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张先做时间审计就能找出自己做饭最花时间精力的环节，并列出七个环节，判断每一环节都花时间、也都可挤时间。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为葱、姜、蒜都可以买脱水碎粒（也有汁液版本），对大多数家庭在味道上已经足够替代。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者提醒使用脱水配料的限制：不能再用油“爆香”，除葱油外都宜主料下锅后再加，干葱只能最后加。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为接买超市净菜没什么大不了，问题是要选对超市——净菜出货量够大、没得剩菜可卖的超市。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断成规模地进剩菜本来就不现实，剩菜的来源只能是店里自己没及时卖完的菜，因此不必一天到晚纠结商家拿剩菜做净菜。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者理由一：店家天天没卖完就不会天天进那么多，剩余量不成规模，而过于小的规模往往不值得再投入人工成本做挽救性加工；挽救性加工很少发生在日常蔬菜这类低值商品上，只有高级水果、海鲜才有意义。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者理由二：剩菜是作为新鲜菜进来的、进价并不比新鲜菜低，商家不如降低冗余量、把剩余百分之五直接丢掉。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者理由三：有些净菜尤其是豆类、豆制品类没有任何顾虑的必要，原理性的干净，拿回去直接下锅即可。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者给出判断标准：若一家店的净菜区规模可与其他生鲜成相当比例，种类又是辣椒丝、土豆丝、蚕豆瓣这类日常蔬菜，而不是寥寥几包，就不必纠结。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出辨别法：腐烂有规律，挽救性加工往往一致缺少特定部位，可看加工品是否什么部位都全（如橙子削成五边形）来判断是挽救性还是加工性。", "evidence": ["E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议多买表面简单连续、采摘运输不易污损的好洗好做的菜（西红柿、蒜苗、西兰花、球白菜、青椒、苦瓜、胡萝卜），少买小白菜、菠菜这些带泥多的叶子菜。", "evidence": ["E014"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断餐饮文化里对“新鲜”的执着有很强偏执倾向，常把新鲜说得差两个小时就会吃死人；新鲜不是不好、田头采摘确实味道好得多，但论营养成分与晚几小时甚至一两天的版本并没有多少至关重要的差异。", "evidence": ["E015", "E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张单从健康角度没有多大必要追求新鲜，只需保证卫生、对“新鲜度”顺其自然，因为浪费的时间直接就是生命本身。", "evidence": ["E017", "E018"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为脱水食材有些很不错、可以考虑，这不见得是为了方便，而整个是另一种食材味道。", "evidence": ["E019", "E020"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为形状加工一方面由净菜解决，另一方面自己总要练点功夫。", "evidence": ["E021"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为身为中国人写不好毛笔字、拿不住菜刀是一种至为傲慢的浪费：文化财富摆在面前，一弯腰就能捡起来，不捡却回头喊困窘、喊抑郁，这是不打折的“抱着饭碗要饭”。", "evidence": ["E022"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言眼前的金子不捡就喊穷、活该穷死，并称这是万事通理。", "evidence": ["E023", "E024"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为一个现代中国人喊“我活不下去了”的前提，是至少已学会做饭做菜、写毛笔字、说中国话这些最基本的技能。", "evidence": ["E025"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张若这些都没学好，至少该学了、用了，还是活不下去再来喊；否则显而易见没有穷尽作为一个中国人最基本的努力空间，没资格喊“活不下去”。", "evidence": ["E026", "E027"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者提出别人对你“冷漠无情”至少还有这一种可能性，主张先排除这种可能性再去嫌别人“无情”。", "evidence": ["E028", "E029"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为预处理都是做大菜的事，有兴趣可以研究，但没必要每天吃大菜；很多预处理本身不怎么花时间只是要等待，最好提前处理、别等吃饭时现整。", "evidence": ["E030"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出诀窍：料酒这类液态腌料腌鱼、排骨等整块食材，可用食品级塑料袋做容器，扎紧袋口隔袋揉捏，可大幅减少腌料用量、提高均匀性，还省得洗碗洗手和让食材氧化。", "evidence": ["E031"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者主张时间不够就最好不要折腾需要耐心的手段、多做凉拌菜与炒菜；并指出智能家电已可预定时和远程启动，可设定程序提前启动加热。", "evidence": ["E032", "E033"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为烹饪调味本来不花时间，很多人却在下锅后才想起切姜末、小米椒、调芡汁；做事要有计划性、先切好放小碟子里，否则耽误时间且锅里火候极易失误。", "evidence": ["E034"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议本来要花时间熬的东西（糖色、卤汁）有现成的卖，多多利用现成成品对加快速度大有好处。", "evidence": ["E035"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出卤鸡蛋不需要一直加热：煮到定型、剥壳后丢进卤汁冷泡，第二天再吃已经是卤蛋，加热只为获得无菌基底，卤豆腐也一样。", "evidence": ["E036"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者限定冷卤的适用范围：不能用冷卤卤猪蹄。", "evidence": ["E037"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者就收拾碗筷环节以图片设问：以下图片有什么共性、它们的碗好洗吗，并指出有预成型的卖。", "evidence": ["E038", "E039"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列出不花时间的食物：蔬菜沙拉没有烹饪时间，卤菜熟食没有烹饪时间，豆腐乳这类不需要时间。", "evidence": ["E040", "E041", "E042"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议重新设计食谱：一餐里一个凉菜、一个外购卤菜，就只需再做一个菜；熟练的话怕是比方便面还快。", "evidence": ["E043", "E044"]}
   ],
   "argument_steps": ["先立方法：做时间审计找出耗时环节（P001）。", "列出七个环节作为审计清单（P002—P008）。", "给出总判断：每环节都花时间、也都可挤时间（P009）。", "环节1：用脱水葱姜蒜或汁液版本替代现切，并给出使用限制（P010—P013）。", "环节2：先破除对净菜的顾虑——选对超市即可；再以三条理由论证剩菜不会成规模地用于净菜；给出规模与部位齐全的辨别法；豆类豆制品无须顾虑（P014—P022）。", "仍属环节2：转入选菜策略并批评对“新鲜”的偏执，以“浪费的时间就是生命”作价值论据（P023—P027）。", "补充脱水食材，指出其味道价值（P028、P029）。", "环节3：净菜加自己练功夫（P030、P031）。", "插入训诫：以毛笔字、菜刀为例主张中国人应先穷尽最基本的努力，才有资格喊困窘或“活不下去”，并据此解释他人“冷漠无情”的一种可能性（P032—P039）。", "环节4：预处理提前做，给出塑料袋腌制诀窍（P040—P042）。", "环节5：时间不够就避开慢速手段，用智能家电定时（P043—P045）。", "环节6：调味要有计划性，用现成成品，卤味可冷泡（P046—P050）。", "环节7：以图片设问碗的清洗，并指出有预成型产品（P051—P053）。", "收束：列出零耗时食物并给出新的食谱结构，断言熟练后比方便面还快（P054—P059）。"],
   "concept_usage": [
    {"term": "时间审计", "meaning": "先测量做饭各环节实际耗时，再逐项压缩的方法框架，是全文的组织方式。", "evidence": "P001", "ambiguity": "作者未说明审计的具体方法或时间尺度。"},
    {"term": "净菜", "meaning": "超市预先清洗切配好的菜；作者关注其出货规模、种类与部位完整性，用以判断来源是否可信。", "evidence": "P015", "ambiguity": "作者未区分不同超市业态或不同加工标准。"},
    {"term": "挽救性加工", "meaning": "商家对将要剩余或不新鲜的食材所做的补救性加工；作者判断其多发生在高级水果、海鲜等高值品类，少见于日常蔬菜。", "evidence": "P018", "ambiguity": "该判断属作者的行业推断，需外部核查。"},
    {"term": "新鲜", "meaning": "作者承认田头采摘味道确实更好，但否认“差两个小时就会吃死人”的偏执，主张卫生优先。", "evidence": "P024", "ambiguity": "作者未给出营养差异的具体数据来源。"},
    {"term": "抱着饭碗要饭", "meaning": "作者用以形容中国人未利用自身文化财富（毛笔字、菜刀功夫）却喊困窘、喊抑郁的比喻。", "evidence": "P032", "ambiguity": "该说法在文中未进一步界定范围。"},
    {"term": "活不下去", "meaning": "作者为这一说法设定前提：须先学会做饭做菜、写毛笔字、说中国话这些最基本技能。", "evidence": "P035", "ambiguity": "“最基本技能”的清单在文中只举例列三项，是否穷尽未说明。"}
   ],
   "examples_and_targets": ["脱水碎粒葱姜蒜、汁液版本：作者建议购买的商品（P011、P012）。", "辣椒丝、土豆丝、蚕豆瓣：作者举的日常蔬菜净菜种类（P019）。", "橙子削成五边形：作者举的辨别挽救性加工的例子（P020）。", "西红柿、蒜苗、西兰花、球白菜、青椒、苦瓜、胡萝卜；小白菜、菠菜：作者举的宜买／宜少买菜例（P023）。", "糖色、卤汁：作者举的现成成品（P048）。", "卤鸡蛋、卤豆腐、猪蹄；樊哙：作者举例与调侃用典（P049、P050）。", "毛笔字、菜刀、青椒炒肉丝、青椒丝：训诫段落中的技能举例（P032、P035、P039）。", "方便面：用作速度比较对象（P059）。", "智能家电：作者举的可用工具（P045）。", "14个图片节点：P052“以下图片有什么共性？它们的碗好洗吗？”与P053“有预成型的卖：”以图片为论据，图片内容未经核验。"],
   "conditions": ["脱水配料的使用限制：不能再用油“爆香”，除葱油外宜主料下锅后再加，干葱只能最后加（P013）。", "净菜可放心的条件：净菜区规模与其他生鲜成相当比例，种类为日常蔬菜而非寥寥几包（P019）。", "辨别挽救性加工的条件：观察是否一致缺少特定部位（P020）。", "对“新鲜”的限定：新鲜不是不好、田头采摘确实味道好得多，只是营养成分差别不大，且须保证卫生（P025、P026）。", "喊“活不下去”的前提：至少学会做饭做菜、写毛笔字、说中国话（P035）；且须已排除“没穷尽最基本努力”这一种可能性（P039）。", "时间不够时不要折腾需要耐心的慢速加工手段（P044）。", "预处理最好提前处理，别等吃饭时现整（P041）。", "冷卤的适用限制：不能用于猪蹄（P050）。", "卤蛋冷泡的适用：煮到定型、剥壳后冷泡，第二天可吃（P049）。"],
   "rhetoric_and_tone": "教程式清单：先列七环节，再按同一编号顺序逐环节给办法，条目化、可操作；第二人称“你”全程指导；夹入训诫与讥讽（“活该穷死你”“抱着饭碗要饭”“切不好青椒丝之前，不要再喊救命”）；口语与调侃（“师傅也是要工钱的好伐”“你毕竟不是樊哙”）；格言式断言（“浪费的时间直接就是生命本身”“这是万事通理”）；部分环节以图片代替文字说明（P052、P053）。",
   "unresolved_questions": ["本篇含14个图片节点（IMG001—IMG014），均未核验；P052、P053直接以图片为内容（“以下图片有什么共性？它们的碗好洗吗？”“有预成型的卖：”），图片未核验使这两处所指不明，需人工／多模态复核。", "正文编号清单中，第2环节内部又出现“其次”（P023）与“第二”（P028）的分层，且图片节点与段落的对应位置不明，层级关系存在歧义。", "P021原文作“这远不不如降低冗余量”，有重复字，疑为原文笔误；本记录按原样引用，不作更正。", "P016—P022对超市剩菜与挽救性加工的判断（如剩余量不会成规模、挽救性加工少见于日常蔬菜）属作者的行业推断，需外部核查。", "P024称“我们的餐饮文化”，其范围（中国或华人世界）未界定。", "作者未说明七个环节的耗时排序依据，未给出时间审计的具体方法。", "发布时间2021-05-19与更新时间2022-10-23不一致，语料未说明是否含修订，本记录以当前版本正文为准。"],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "做一下时间审计，就知道自己做饭最花时间精力的是什么。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P009", "quote": "每一环节都花时间，每一环节也都都可以挤时间。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P011", "quote": "葱、姜、蒜你都是可以买脱水碎粒的。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P013", "quote": "在味道上已经足够替代", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P013", "quote": "不能再用油“爆香”，除了葱油之外都宜主料下锅后再加", "relation": "qualifies"},
    {"key": "E006", "paragraph_id": "P015", "quote": "接买超市净菜没什么大不了", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P016", "quote": "剩菜的来源只能是你店里自己没及时卖完的菜", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P017", "quote": "而过于小的规模往往不值得再投入人工成本去搞挽救性加工", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P018", "quote": "只有在高级水果、海鲜这类品类上才有意义", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P021", "quote": "这远不不如降低冗余量，然后把那剩余的5%直接丢掉", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P022", "quote": "原理性的干净，拿回去直接下锅好了", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P019", "quote": "你就不用纠结那么多", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P020", "quote": "比如橙子削成了五边形", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "少买不好洗不好干的菜，比如小白菜、菠菜这些带泥多的叶子菜", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "常把“新鲜”说得差两个小时就会吃死人一样", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "它和晚了几个小时甚至一两天的版本并没有多少至关重要的差异", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P026", "quote": "你只需要保证卫生，对“新鲜度”顺其自然就好", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P027", "quote": "要知道，浪费的时间直接就是生命本身。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P028", "quote": "脱水食材有些很不错，可以考虑", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P029", "quote": "而整个的是另一种食材味道", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P031", "quote": "另一方面自己总要练点功夫", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P032", "quote": "这是不打折的“抱着饭碗要饭”", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P033", "quote": "你眼前就有金子你不捡，你就喊穷，活该穷死你。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P034", "quote": "这是万事通理。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P035", "quote": "是ta至少学会了做饭做菜、写毛笔字、说中国话这些最基本的技能之后才能说的话", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P036", "quote": "你再来喊活不下去", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P037", "quote": "你没资格喊“活不下去”", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P038", "quote": "至少还有这一种可能性", "relation": "qualifies"},
    {"key": "E029", "paragraph_id": "P039", "quote": "切不好青椒丝之前，不要再喊救命", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P041", "quote": "别等吃饭的时候现整", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P042", "quote": "可以用食品级塑料袋来做容器", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P044", "quote": "多做凉拌菜、炒菜", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P045", "quote": "你可以设定程序让它们提前启动加热", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P047", "quote": "做事要有计划性，先切好放小碟子里", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P048", "quote": "多多利用这些现成的成品，对加快速度大有好处", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P049", "quote": "第二天再吃已经是卤蛋了", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P050", "quote": "当然你不能用冷卤卤猪蹄，你毕竟不是樊哙。", "relation": "qualifies"},
    {"key": "E038", "paragraph_id": "P052", "quote": "以下图片有什么共性？它们的碗好洗吗？", "relation": "supports"},
    {"key": "E039", "paragraph_id": "P053", "quote": "有预成型的卖：", "relation": "supports"},
    {"key": "E040", "paragraph_id": "P055", "quote": "蔬菜沙拉没有烹饪时间，", "relation": "supports"},
    {"key": "E041", "paragraph_id": "P056", "quote": "卤菜熟食没有烹饪时间，", "relation": "supports"},
    {"key": "E042", "paragraph_id": "P057", "quote": "豆腐乳这类，不需要时间。", "relation": "supports"},
    {"key": "E043", "paragraph_id": "P058", "quote": "一餐里面一个凉菜、一个外购卤菜，你就只需要再做一个菜了", "relation": "supports"},
    {"key": "E044", "paragraph_id": "P059", "quote": "你要是熟练，怕是比方便面还快。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["烹饪与家常饮食", "时间管理", "消费与购物选择", "文化批评"],
   "issue_candidates": ["做饭各环节的省时办法", "超市净菜与剩菜顾虑", "对“新鲜”的偏执", "脱水与现成食材", "中国人基本生活技能"],
   "text_function_candidates": ["答疑", "经验总结", "操作指南", "训诫", "批评"],
   "object_candidates": ["提问者", "超市", "商家", "餐饮文化", "现代中国人", "樊哙"],
   "working_keywords": ["时间审计", "净菜", "挽救性加工", "脱水食材", "新鲜", "抱着饭碗要饭", "活不下去", "卤蛋冷泡", "预成型", "智能家电"]
  },
  "notes": "本篇含14个图片节点（IMG001—IMG014），图片内容未经核验，需图像核验；已读部分为正文文本。P052、P053直接以图片为论据（“以下图片有什么共性？它们的碗好洗吗？”“有预成型的卖：”），图片未核验使这两处不能完整理解。P021“这远不不如”有重复字，疑为原文笔误，引用时按原样保留。发布时间2021-05-19与更新时间2022-10-23不一致，语料未说明版本差异。"
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
