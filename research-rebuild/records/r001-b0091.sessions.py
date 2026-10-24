# -*- coding: utf-8 -*-
"""批次 r001-b0091 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0091.sessions.py            # 写 out/r001-b0091.out.jsonl
  python3 records/r001-b0091.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0091"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0091.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6699eaa6": {
  "analysis": {
   "question_context": "提问者问“如何看待‘天赋者应有特权’这种论题？”（Q001，属提问者，不是作者立场）。作者不接受“应有”这一规范提问框架，改写为实然判断：天赋者已经握有无法剥夺的特权；随后指出与特权相随的“特责”与诅咒。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "改换框架：不谈“应有”，天赋者确实握有与能力绑定、无法被剥夺的实际特权。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "提出“特责”：有天赋者招致先发制人的敌意，对抗额外恶意是天然代价。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009"], "summary": "解释激烈矛盾何以易发：什么都懂意味着行为被读作故意，同一行为在有能力与无能力者身上得到双重评价。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "限定：多数人的天赋解决不了随之而来的诅咒；和氏璧之喻说明天赋不能挡刀。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "作者给出的抵御方式：以爱吸引爱、以爱成全爱结成逃城；否则被施加“不爱就要死无葬身之地”的诅咒。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017"], "summary": "对比：无天赋者所受惦记更温和，高价值目标面对的则量身定制；故天赋者在意的是恶意而非特权。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019"], "summary": "几乎只有年幼二代近乎净享特权，但其庇护者终会倒下，届时才见福祸真章。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "结论：世上并无免费之物，故不必羡慕。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不必谈“应有”：天赋者确实被安排了实际拥有、无法剥夺的特权，它与能力绑定，别人根本剥夺不了。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "天赋者除特权外还有“特责”：会被视为威胁而遭先发制人，对抗由此而来的额外恶意是天然代价。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因天赋者“什么都懂”，其不作为只能被解释为残忍冷漠，故极易发生激烈矛盾（没钱／有钱、没能力／有能力皆然）。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "大部分人被赋予的天赋并不能解决因那份天赋而来的诅咒；旁人看到特权，当事人却如履薄冰、步步惊心。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "天赋带来的诅咒靠智力、体力或美貌无能为力，只能靠以爱吸引爱、以爱成全爱结成的逃城抵御和庇护。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这份诅咒对没有那份天赋的人要温和、宽容得多；针对“高价值目标”的技术则是量身定制、连钩带刺、见血封喉。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "客观说，特权真正的“净享受”者几乎只能是年幼的二代们；但庇护的长辈迟早倒下，特权是幸福源泉还是诅咒届时才见真章。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世上并无免费之物，所以不必羡慕天赋者的特权。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "先否定提问的“应有”框架，改判为实然：天赋者已有无法剥夺的特权（P001、P002）。",
    "以“料事如神／攻守莫测”为例，说明能力本身就是 power 与 privilege，与能力绑定故不可剥夺（P002）。",
    "转折提出“特责”：天赋招来先发制人的恶意，并引“既不能为我江东所用，必为我江东之患，请即杀之”佐证（P003）。",
    "自问“何以见得会极易发生激烈矛盾”，答以“你什么都懂，那么你干什么就都是故意的”（P004、P005）。",
    "用成对反例展开双重标准：不懂人心则无可责怪，什么都懂则他人难过即被读作残忍；没钱／有钱、没能力／有能力同理（P006—P009）。",
    "限定：多数人的天赋解决不了这份诅咒，当事人如履薄冰（P010）。",
    "以和氏璧为喻：有好处，但匹夫无罪、怀璧其罪，挡不了刀（P011）。",
    "给出抵御方式：以爱吸引爱、以爱成全爱结成的逃城；否则被施加“不理解爱、不实践爱、不追求爱就要死无葬身之地”的诅咒（P012）。",
    "对比：无天赋者所受惦记远小于“有特权的人”所受觊觎，后者面对量身定制的手段（P013、P014）。",
    "推论：特权很快被习以为常，真正占据注意力的是明处与暗处的恶意（P015、P016）。",
    "指认能解决这威胁的东西反而不允许人安享特权（P017）。",
    "收窄到净享受者几乎只能是年幼二代，并指出庇护伞终会倒下，福祸届时才见真章（P018、P019）。",
    "以“世上并无免费之物”收束，落到“何必羡慕，不必羡慕”（P020、P021）。"
   ],
   "concept_usage": [
    {"term": "特权", "meaning": "本文指由天赋直接带来、与能力绑定因而无法被他人剥夺的实际行动力（power／privilege），不是规范意义上的“应有”", "evidence": "P002", "ambiguity": "与“二代”享有的家世型特权混用，未作区分"},
    {"term": "特责", "meaning": "因拥有天赋而被他人视为威胁所招来的额外恶意，以及自行承担对抗代价的责任", "evidence": "P003", "ambiguity": "作者自造词，未给出可操作边界"},
    {"term": "诅咒", "meaning": "天赋附带、靠天赋本身无法解除的代价；作者称被赐予天赋者同时被施加“不爱就要死无葬身之地”的诅咒", "evidence": "P012", "ambiguity": "施与者与判定方式本文未说明"},
    {"term": "逃城", "meaning": "以爱吸引爱、以爱成全爱所结成的关系性庇护", "evidence": "P012", "ambiguity": "典故来源与具体构成未说明"},
    {"term": "韭菜", "meaning": "被通用技术大规模收割的普通对象，用来与被觊觎的高价值目标对照", "evidence": "P013", "ambiguity": "修辞性用词，作者未将其定义为分析概念"}
   ],
   "examples_and_targets": [
    "料事如神、攻守莫测者（作者例证，说明天赋即 power）",
    "“既不能为我江东所用，必为我江东之患，请即杀之”（作者引语，未注明出处，用作先发制人的例证）",
    "不懂人心而未察觉他人难过者（作者反例，与“什么都懂”对照）",
    "没钱／有钱、没能力／有能力者（作者成对反例，说明双重标准）",
    "和氏璧、匹夫无罪怀璧其罪（作者比喻与引语）",
    "割韭菜（作者提及的流行说法，用作对照）",
    "马云、任正非（作者以反问提及，作为“有特权者未必开心”的修辞材料）",
    "年幼的二代及其父母长辈（作者对净享受者及其庇护者的指认）"
   ],
   "conditions": [
    "“大部分人”被赋予的天赋不足以解决诅咒，作者未把话说成全称（P010）",
    "诅咒对“没有那份天赋的人”更温和、更宽容（P013）",
    "针对高价值目标的技术是量身定制，与针对韭菜靠大数据的方式不同（P014）",
    "“客观说”与“几乎只能是”限定了净享受者的范围（P018）",
    "庇护的长辈“迟早”要倒下，福祸判定被推到那个时点（P019）"
   ],
   "rhetoric_and_tone": "训诫兼论辩。第二人称“你”直接说理，成对短句排比（“你没钱……你有钱……”“你没能力……你有能力……”）；引文言与四字句（“匹夫无罪，怀璧其罪”）制造古雅感；以“和氏璧”“逃城”“韭菜”“高价值目标”作比喻；以“你真觉得马云现在开心吗？任正非现在快乐吗？”反问收束；末句“何必羡慕，不必羡慕”为劝诫式重复。",
   "unresolved_questions": [
    "“天赋”的定义、种类与外延本文未说明（仅举到智力、体力、美貌）",
    "“逃城”的出处与所指（是否宗教典故）本文未说明",
    "引文“既不能为我江东所用，必为我江东之患，请即杀之”未注明出处，待外部核查",
    "“二代”的范围未界定；马云、任正非两处为反问，未提供可核查的事实依据",
    "“能解决这威胁的东西，其实是不允许你安享特权的”一句中“东西”的具体所指作者未明说"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "天赋者的确被安排了特权——实际就有的、无法剥夺的特权", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这本身就是power，是privilege，这跟你的能力已经绑在一起了", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "ta们除了有特权，也有“特责”", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "对抗这种由此而来的额外的恶意就成了一份天然的代价", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你什么都懂，那么你干什么就都是故意的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "那么我难过而你没有做任何事就只能解释为残忍和冷漠", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "大部分人被赋予的天赋并不能解决因那份天赋而来的诅咒", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P010", "quote": "ta们却如如履薄冰、步步惊心", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "只能靠以爱吸引爱、以爱成全爱所结成的逃城抵御和庇护", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "这个诅咒对没有那份天赋的人要温和得多，宽容得多", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P014", "quote": "针对这些“高价值目标”的技术则是量身定制、连钩带刺、见血封喉的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "特权真正的“净享受”者几乎只能是那些早年可以食其利却暂时不必忧其事的年幼的二代们", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P019", "quote": "才到了真正见真章的时候", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P020", "quote": "世上并无免费之物", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "所以，何必羡慕，不必羡慕", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理", "社会心理", "人生哲学"],
   "issue_candidates": ["天赋与特权的关系", "天赋者的代价与额外恶意", "爱与救赎", "是否应当羡慕特权者"],
   "text_function_candidates": ["答疑", "论辩", "劝诫"],
   "object_candidates": ["天赋者", "马云", "任正非", "二代", "韭菜", "和氏璧"],
   "working_keywords": ["特权", "特责", "诅咒", "逃城", "怀璧其罪", "净享受者"]
  },
  "notes": "无图片节点。正文 21 段、1266 字符，一次读完。提问者的“应有”框架与作者的实然重述已区分，未把提问立场归给作者。引文“既不能为我江东所用……”未注明出处，登记为待外部核查；马云、任正非两处为反问式修辞，未提供可核查事实。"
 },
 "2a406215": {
  "analysis": {
   "question_context": "提问者问“如何看待湖南益阳养老院疑似以预订床位为名诈骗，老人一生积蓄化为乌有，选择跳桥结束生命一事？”（Q001，属提问者）。作者不评论该事件的事实与责任，而是抽出一般命题：养老是性命相托，解决手段必须与问题体量对称，须提前二三十年经营可托付的关系。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总纲：解决问题须正确估计问题体量，终身幸福类事项的手段必有对称复杂度与劳动量；不可有侥幸，侥幸即自弃。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "定义：养老本质是性命相托，超出商业合同、民事委托级社会契约所能支撑，不能靠第三方监督的交易逃避经营功夫。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "行动要求：至少提前二十年经营关系，在小十至二十岁的人中物色培养可性命相托、可接受其“停止救护”决定的对象。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "反驳常见预设：子女多半缺席最后二十年且缺少送终准备与训练，故难以担当。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "要求毫无侥幸：见证人从无到有需漫长准备（物色、筛选、观察、教育、交托），是心灵的生养过程，无法用钱替代，应视为人生必做大事。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "主张除骨肉子女外还该从灵里再生子女，后者才真正消解对去处的忧虑。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018"], "summary": "效果：这份功夫能帮助人从对衰老和死亡的恐惧中解脱，并从根上影响面对一切问题的心态。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尝试解决问题时，对问题体量的正确估计是关键；事关终身幸福的重大事项，其解决手段势必会有对称的复杂度和劳动量。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对这类事项不要有任何侥幸，侥幸即自弃。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“养老”本质上就是性命相托，不是商业合同、民事委托这种级别的社会契约所能支撑的，也不能指望靠有“强有力的第三方监督”的交易逃避这份经营功夫。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能送你终老的人，至少要提前二十年经营关系，在小你十至二十岁左右的人中间物色和培养，且对象要能甘于接受其“停止救护”的决定。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "很多人误以为子女显然可以担当，但子女基本上在最后二十年多半缺席你的生活，且往往缺少送终的准备和训练；不少人是由空有“法定资格”却早已疏离、无训练、无交托的子女稀里糊涂甚至痛苦地了结的。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "终末见证人的从无到有需要漫长的准备过程（物色、筛选、观察、教育、交托），这是一个心灵的生养过程，无法用一笔钱来替代。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "物色且视如己出地奖掖和培育值得一搏的后辈青年，本来应该是每个人视为人生必做的大事之一；除了从骨头中生了子女，还该从灵里再生子女，后者才真正消解对去处的忧虑。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这份功夫做得踏实，能极大帮助人从对衰老和死亡的恐惧与不安中解脱，并从根上消解焦虑、深刻影响面对一切问题的心态。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "先立总纲：解决问题要对问题体量有正确估计，终身幸福类事项的解决手段必有对称的复杂度与劳动量（P001）。",
    "下断语：对这类事项不要有任何侥幸，侥幸即自弃（P002）。",
    "给出养老的性质定义：本质是性命相托，超出商业合同与民事委托所能支撑（P003、P004）。",
    "由此排除捷径：不能指望靠巧妙的、有第三方监督的交易来逃避经营功夫（P004）。",
    "给出时间与对象要求：至少从临终倒推提前二十年，在小十至二十岁的人中物色培养（P005、P006）。",
    "反驳“子女显然可以担当”的预设：子女多半缺席、缺准备、缺训练（P007、P008）。",
    "重申不可侥幸，说明准备过程的内容与性质：物色、筛选、观察、教育、交托，是心灵的生养过程（P009—P011）。",
    "排除金钱替代（P012）。",
    "上升为人生必做大事之一，并提出“从灵里再生子女”（P013、P014）。",
    "指出其效果：真正消解对去处的忧虑，帮助人从对衰老与死亡的恐惧中解脱（P015—P017）。",
    "以抒情句“你所踏足处，如有春风，胜境清凉”收束（P018）。"
   ],
   "concept_usage": [
    {"term": "体量", "meaning": "问题所涉的复杂度与劳动量的规模，作者认为解决手段必须与之对称", "evidence": "P001", "ambiguity": "未给出估量体量的标准"},
    {"term": "性命相托", "meaning": "把生命终末（含“停止救护”的决定）交托给对方的关系", "evidence": "P003", "ambiguity": "未说明其法律或伦理形式"},
    {"term": "自弃", "meaning": "本文特指对养老等重大事项抱有侥幸", "evidence": "P002", "ambiguity": "与作者另文《自弃》中“机会未抓住”的定义不同，本文未展开"},
    {"term": "从灵里再生子女", "meaning": "非血缘的、心灵层面的后辈关系（视如己出地培育后辈青年）", "evidence": "P014", "ambiguity": "宗教语汇，具体所指与做法未说明"},
    {"term": "停止救护", "meaning": "临终时由受托者作出的放弃抢救决定", "evidence": "P006", "ambiguity": "决定的主体、依据与程序未说明"}
   ],
   "examples_and_targets": [
    "湖南益阳养老院疑似以预订床位为名诈骗、老人跳桥一事（提问者给定的情境；作者未评论其事实，仅作普遍论述）",
    "结婚、生子、养老（作者列举的终身幸福类重大事项）",
    "商业合同、民事委托与“强有力的第三方监督”的交易（作者反驳的解决路径）",
    "小你十至二十岁左右的后辈青年（作者指定的物色与培养对象）",
    "子女、“法定资格”（作者反驳的常见预设）",
    "空有“法定资格”而疏离、无训练、无交托的子女（作者的负面例证）"
   ],
   "conditions": [
    "“类似结婚、生子、养老……等等事关终身幸福的重大事项”限定适用范围（P001）",
    "“至少要从终日倒推提前二十年”给出时间下限（P005）",
    "“小你十至二十岁左右”给出年龄差范围（P006）",
    "“子女们基本上”“多半”为通常性限定，不是全称判断（P007）",
    "对象须“可以甘于接受其‘停止救护’的决定”（P006）",
    "“这份功夫做得踏实”是取得解脱效果的前提（P016）"
   ],
   "rhetoric_and_tone": "训诫体，且刻意不回应具体新闻事件。以“你必须对这个不可抛弃的工作毫无侥幸——”作断喝；用“你从骨头中生了子女之外，还该要从灵里再生子女”的对偶句式与宗教语汇；以“你所踏足处，如有春风，胜境清凉”作抒情的抒情式收束；全文用第二人称“你”对读者说话。",
   "unresolved_questions": [
    "提问所涉湖南益阳养老院诈骗与老人跳桥的事实，作者既未核实也未评论，不能据本文认定其对事件的判断",
    "“从灵里再生子女”的具体含义与做法本文未说明",
    "“停止救护”由谁决定、依据何在，本文未说明",
    "P019 混入两条平台链接式提问（“你心目中完美的养老院是什么样的？”“50 多位老人众筹买房……曲终人散”），属 lexical 未覆盖片段，需人工判断是否计入正文",
    "“至少提前二十年”与“小十至二十岁”的依据本文未说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "对问题体量的正确估计是一个关键的问题", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "其解决手段势必会有对称的复杂度和劳动量", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "对这些不要有任何侥幸，侥幸即自弃", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "本质上就是性命相托", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "不是商业合同、民事委托这种级别的社会契约所能支撑的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "不能指望可以靠巧妙的、有“强有力的第三方监督”的交易来逃避这份经营的功夫", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "至少要从终日倒推提前二十年开始经营关系", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "就要开始在小你十至二十岁左右的人中间物色和培养", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "子女们基本上在最后的二十年其实多半是缺席你的生活的", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P008", "quote": "不知有多少人是被空有“法定资格”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "这其实是一个心灵的生养过程", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "这个过程，是无法用一笔钱来替代的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "其实本来应该是每一个人都应该视为人生必做的大事之一", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "还该要从灵里再生子女", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "实际上是后者将真正消解你对去处的忧虑", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "能极大的帮助你从对衰老和死亡的恐惧和不安中解脱", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["养老", "临终关怀", "家庭伦理", "人生规划"],
   "issue_candidates": ["养老诈骗事件的一般化反思", "养老关系的性质", "子女能否承担送终", "提前经营可托付关系", "对衰老与死亡的恐惧"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "经验总结"],
   "object_candidates": ["湖南益阳养老院", "老人", "子女", "后辈青年", "养老院"],
   "working_keywords": ["性命相托", "体量", "侥幸", "自弃", "停止救护", "从灵里再生子女"]
  },
  "notes": "无图片节点。正文 19 段、885 字符，一次读完。作者未评论提问所指的湖南益阳事件，只作普遍论述；提问者立场未归给作者。P019 出现与正文无关的平台链接式提问（“你心目中完美的养老院是什么样的？”等），属 lexical 未覆盖片段，已在 unresolved_questions 登记，判断是否计入正文需人工复核。"
 },
 "77880b8f": {
  "analysis": {
   "question_context": "提问者问“什么是自弃？”（Q001，属提问者）。作者给出自己的定义：有机会帮助到更多的人而没抓住即自弃；随即校准该定义按“一生助人总量的期望值”计算，再讨论该原则的两个复杂性，并把论证从道德劝诫转向“世界实际上是这样设计的”这一功利性说法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "定义：有一个机会可以帮助到更多的人，你没抓住，这就叫自弃。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "校准定义：“帮助更多的人”按一生助人总量的期望值计算，故健康、锻炼、理财同属此类；能让你更健康的事没做、奢侈浪费、撒胡椒面同样违背原则。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "复杂性一：期望值本身是极其复杂的计算，你可能在算法中做手脚为背道而驰的行为背书。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "复杂性二：以保持最大期望为由不断推迟实际输出会陷入悖论，来年算法仍得“不给”，总期望升高而无人受益，意外死亡后总期望变成空气。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013"], "summary": "未决：怎么解决这两个问题本身就是重大的人生家庭作业。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "转折：不要把这看成“道德高调”——世界实际是这样设计的；不可因他人背道而驰得利就以为法则不灵。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018"], "summary": "功利论证：想内心宁静地做举足轻重的人、手握财富而保住人格健全，这是唯一的办法；不遵循到骨髓里形同“先挥刀自宫，再猛练神功”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020"], "summary": "结论：看似热火朝天其实败局已定，不成功尚可无疾而终，成功则死无葬身之地；反问还有比这更大的自弃么。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自弃的定义是：有一个机会可以帮助到更多的人，你没抓住。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个“帮助更多的人”不按当时那件事本身计算，而按“一生助人总量的期望值”计算。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因此努力学习、积极锻炼、合理理财同样属于“帮助更多人”的事务；能让你更健康的事没做、奢侈浪费无谓耗散财富、把个人资产简单撒胡椒面，都违背这个原则。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个原则事实上深刻而复杂：其一是“一生助人总量期望值”本身是极其复杂的计算，你无法确知自己不是在算法中做手脚，为背道而驰的行为背书。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "其二是若一直以“保持最大期望”为由不断推迟实际输出，会陷入悖论：明年再跑算法仍得“不给”，总期望不断升高而事实上没有人在受益，一旦意外死亡则“总期望”变成空气。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "怎么解决这两个问题，本身就是重大的人生家庭作业（作者未给出解法）。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要把这单纯看成“道德高调”：世界实际上是这样设计的，不要因为很多人背道而驰、赚得盆满钵满，就以为这只是“时灵时不灵，也许对我不灵”的法则。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预言：等着看，一个逃脱的都不会有。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想要内心宁静地做一个举足轻重的人、想要手握能移山倒海的财富而保住人格健全，遵循这个原则是唯一的办法；不遵循到骨髓里，哪怕从最世俗功利的立场看，也形同“先挥刀自宫，再猛练神功”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不遵循者看似练得热火朝天，其实从一开始就败局已定：不“成功”还可以混个骂骂咧咧、无疾而终，“成功”了立刻死无葬身之地。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问收束：还有比这更大的自弃么？（作者以此判定前述失败大于其所定义的“自弃”）", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "以两句格言给出定义：有机会帮助到更多的人而没抓住，就是自弃（P001、P002）。",
    "校准口径：“帮助更多的人”按一生助人总量的期望值计算，而非按当时那件事本身（P003）。",
    "推广外延：学习、锻炼、理财同属此类事务；健康机会未取、奢侈浪费、撒胡椒面皆违背原则（P004、P005）。",
    "承认原则复杂（P006、P007），并给出第一重复杂性：期望值计算极复杂，人可能在算法中为自己做手脚（P008）。",
    "给出第二重复杂性：以最大化期望为由推迟实际输出导致悖论，期望升高而无人受益，死亡使其归零（P009—P012）。",
    "不下解法，只说这两个问题是重大的人生家庭作业（P013）。",
    "转折：这不是道德高调，而是世界的实际设计；他人的得利不能证明法则失效（P014、P015）。",
    "以预言加固：一个逃脱的都不会有（P016）。",
    "给出功利理由：唯有如此才能既举足轻重又保住人格健全（P017）。",
    "用武侠式比喻说明不遵循者自毁根基，并以反问收束（P018—P020）。"
   ],
   "concept_usage": [
    {"term": "自弃", "meaning": "本文定义为有机会帮助到更多的人而没有抓住；判断口径是一生助人总量的期望值", "evidence": "P002", "ambiguity": "与“懒惰”“不义”等相邻概念的边界未讨论"},
    {"term": "一生助人总量的期望值", "meaning": "衡量是否自弃的计算口径，把单次行为折算进一生的总账", "evidence": "P003", "ambiguity": "如何计算、由谁计算、能否核实均未说明"},
    {"term": "算法", "meaning": "指对上述期望值的计算过程；作者警告人可能在其中做手脚自我背书", "evidence": "P008", "ambiguity": "具体所指的计算方式未说明"},
    {"term": "撒胡椒面", "meaning": "把个人资产简单分散地捐出，作者视其为违背原则的做法", "evidence": "P005", "ambiguity": "为何违背原则，作者未展开论证"},
    {"term": "先挥刀自宫，再猛练神功", "meaning": "戏仿武侠的比喻，指不遵循该原则去追求成功等于先毁掉根基", "evidence": "P018", "ambiguity": "比喻的对应关系作者未逐项说明"}
   ],
   "examples_and_targets": [
    "“有一个机会可以帮助到更多的人，你没抓住”（作者的假设性情境）",
    "努力学习、积极锻炼、合理理财（作者列举的同属“帮助更多人”的事务）",
    "奢侈浪费、无谓耗散上帝交给你的财富（作者的反例）",
    "把个人资产拿出去撒胡椒面（作者的反例）",
    "“我现在本来可以给你一百……明年我就有一百二可以给你”的不作为悖论（作者设想的自辩）",
    "意外死亡、账号和密码没人知道（作者用于说明总期望归零的设想）",
    "背道而驰、赚得满盆满钵、踌躇满志者（作者提及并警告的对象）",
    "“时灵时不灵，也许对我不灵”的法则观（作者反驳的说法）",
    "先挥刀自宫，再猛练神功（作者借用的武侠式比喻）"
   ],
   "conditions": [
    "“帮助更多的人”按一生总量的期望值计算，不按当时那件事本身计算（P003）",
    "“如果有一件事情可以让你更健康，你没做”为例示的条件句（P005）",
    "“如果一直以‘保持最大期望’为理由，不断的推迟实际的输出”是悖论成立的条件（P009）",
    "“不要看到似乎很多人背道而驰……就以为……”为对读者的限定（P015）",
    "“不遵循到骨髓里”是从世俗功利立场看也失败的前提（P018）",
    "“你想要内心宁静的做一个举足轻重的人，想要手握能移山倒海的财富而保住人格健全”是适用该结论的目标条件（P017）"
   ],
   "rhetoric_and_tone": "格言体开头（“有一个机会可以帮助到更多的人，你没抓住。”／“这就叫自弃。”），第二人称训诫与反诘并用；用“撒胡椒面”“先挥刀自宫，再猛练神功”等俗语与戏仿武侠的比喻；以“等着看，一个逃脱的都不会有”作预言式警告；末句“还有比这更大的自弃么？”是反问而非论证。",
   "unresolved_questions": [
    "“上帝交给你的财富”一语所属的宗教框架本文未展开",
    "“算法”具体指何种计算方式、如何避免自我欺骗，本文未说明",
    "作者提出两个复杂性问题后只说“本身就是重大的人生家庭作业”，未给出解法",
    "“等着看，一个逃脱的都不会有”是预测性断言，无可核查证据",
    "“自弃”与道德意义的“恶”“懒惰”如何区分，本文未讨论"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有一个机会可以帮助到更多的人，你没抓住", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这就叫自弃", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "而是按照“一生助人总量的期望值”计算的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "努力学习、积极锻炼、合理理财……同样属于“帮助更多人”的事务", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "奢侈浪费，无谓耗散上帝交给你的财富，也是违背了这个原则", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "你如何知道自己不是在悄没声的在算法中做手脚，用来背书你其实背道而驰的行为？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "不断的推迟实际的输出，你会陷入悖论", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "总期望的确是在不断升高，但是事实上没有人在受益", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "“总期望”变成了空气", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "本身就是重大的人生家庭作业", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "绝对不要单纯的把这看成什么“道德高调”", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "世界实际上是这样设计的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "等着看，一个逃脱的都不会有", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "这是唯一的办法", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "也形同“先挥刀自宫，再猛练神功”", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "其实从一开始就败局已定", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "还有比这更大的自弃么？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "人生哲学", "宗教伦理", "财富观"],
   "issue_candidates": ["自弃的定义", "一生助人总量期望值", "以期望最大化为由的不作为", "道德高调与功利理由"],
   "text_function_candidates": ["答疑", "定义", "训诫", "论辩"],
   "object_candidates": ["上帝", "背道而驰者", "举足轻重的人"],
   "working_keywords": ["自弃", "一生助人总量的期望值", "算法", "撒胡椒面", "先挥刀自宫，再猛练神功"]
  },
  "notes": "无图片节点。正文 20 段、789 字符，一次读完。提问者只问定义，作者的答案含定义、两重复杂性检讨与功利性论证三层；对“这两个问题怎么解决”明确未给答案，已登记在 unresolved_questions。“上帝”“世界是这样设计的”属作者未展开的宗教/目的论说法，按原文保留，未作外部解释。"
 },
 "61d69484": {
  "analysis": {
   "question_context": "提问者问“中国女权发展面临的最大挑战是什么？”（Q001）。作者给出自己的答案：缺少更深入的研究和阐述；随后自评现状为“自发大于自觉”的应激式反击，并以第二人称“你们”向女权阵营追问“要什么”与“新的女德”。提问者只提供问题，未提出被作者回应的具体立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "判断：最大挑战是缺少更深入的研究和阐述；现状是自发大于自觉、由痛苦和刺激驱动战术的应激式反击，相对于上一时代立法层面的进步相当微不足道。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "承认进展：社交媒体使势单力孤的个人较易获得舆论声援，女性经济能力提高使商业机构开始顾虑或经营立场，扩大了女性说“不”的权力。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "指出局限：仅仅说“不”不能解决问题；公众号与大V几乎只是在帮你说“不”，未被回答的是“要什么”。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "不能以“破”代“立”：收集所有“不要”不等于宣布了你要什么。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "主张：说出自己要什么更难，但确定、主张、追求自己想要的才是权利真正实质与主动的部分；接受“这是你自己想要的”约束是头戴王冠必承之重。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P013"], "summary": "判定：现在的女权运动对这一部分的努力明显缺失。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015"], "summary": "追问新女德：反对旧女德可以，但新的女德是什么？若把一切探讨女性应当如何者都视为敌人，结果只会是探讨者全在你们之外。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "论证新女德的必然性：共同行为规范的探讨必然存在；整体性群体必有共同行动纲领，纲领必逻辑引出组织自己的德行；故新女德绕不过去。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022"], "summary": "警告：只说不的实践把旗帜实践成“追求为所欲为的power”，这是被人类历史证明的死路，是一面海盗旗。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P023"], "summary": "文末标记：未完，待续。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国女权发展面临的最大挑战在于缺少更深入的研究和阐述。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在中国的女权处在自发大于自觉、由痛苦和刺激驱动战术的应激式反击阶段。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与上一个时代在立法上取得的进步相比，眼下的进展相当微不足道。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "重要进展是社交媒体使个人较易获得舆论声援、女性经济能力提高使商业机构开始顾虑或经营其女权立场，无形中扩大了女性的实际权力——说“不”的权力。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "仅仅说“不”并不能解决问题；各种公众号、大V几乎都只是在帮你说“不”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能单纯通过“破”来替代“立”；把所有的“不要”收集总结起来，不能等同于已经宣布了你要什么。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说出自己要什么比只说“不”难得多，但确定、主张、追求自己想要的，仍是权利真正实质的、真正主动的、与自我价值实质相关的部分。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因这些而接受“这是你自己想要的”的约束，是头戴王冠必承之重。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在的女权运动对“说出并追求自己要什么”这一部分的努力是明显缺失的。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：反对旧的女德可以，但新的女德是什么？还是说不再应该有任何意义上的女德可言？任何人在任何意义上探讨女性应当如何，都是“尝试从思想上禁锢我们的自由”的敌人吗？（作者未给出答案）", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果认同上述观点，会陷入尴尬困境：这不会导致“不会再有任何女德的探讨存在”，而只会导致“探讨它们的全是你们之外的人”。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关于共同行为规范（本文即指女德）的探讨必然存在；任何真正想作为整体去争取共同目标的群体都必然有共同行动纲领，纲领不可能只包含“不要”“反对”，还须包含反对之外的目标，而目标必定逻辑地引出组织成员的共同行为规范。", "evidence": ["E14", "E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女性要真正团结、真正被看作一个整体、成为必须被一切其它实体行动时纳入考虑的要素，新的女德是一个绕不过去的问题。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "竖起“我想要这个”的大旗才能聚拢“我也想要这个”的同志；“我们想要这个”的共识势必产生“我们应当／不应如何”的共识。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在“对想要什么避而不谈，仅仅只说不”的实践之下，无论是否意识到、是否赞成，这面旗帜在很大程度上已被实践成“我们要尽可能的追求为所欲为的power”。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "追求为所欲为的power是被几百万年人类历史证明过的死路——至今没有任何一个组织在死亡之前实现了这个目标；这是一面海盗旗。", "evidence": ["E19", "E20"]}
   ],
   "argument_steps": [
    "先答挑战：缺少更深入的研究和阐述（P001）。",
    "给出对现状的阶段判断：自发大于自觉、应激式反击，与上一时代立法成就相比微不足道（P002、P003）。",
    "承认已有的进展：社交媒体声援与商业机构立场的调整扩大了女性说“不”的权力（P004）。",
    "转折指出局限：仅仅说“不”不能解决问题，公众号与大V只是帮你说“不”（P005—P008）。",
    "给出“破”不能代“立”的理由（P009），并以“你要什么？”直接发问（P010）。",
    "提出正面主张：主张自己要什么才是权利的实质部分，并须承担“这是你自己想要的”约束（P011、P012）。",
    "判定现有运动在这一部分明显缺失（P013）。",
    "转向女德问题，连环追问新女德是什么，并指出全盘否定的实际后果（P014、P015）。",
    "以群体行动纲领的必然性论证新女德的不可避免（P016—P018）。",
    "以旗帜与共识的关系强化（P019）。",
    "警告现实实践已使旗帜变成“为所欲为的power”，并断言这是死路（P020—P022）。",
    "文末标注未完待续（P023）。"
   ],
   "concept_usage": [
    {"term": "power", "meaning": "本文中与“权利”相对的实际支配力；作者把只说“不”的权力／力量称为女性实际扩大的 power，并把“为所欲为的power”判为死路", "evidence": "P004", "ambiguity": "原文夹用英文，作者未给出明确定义，与“权利”的关系未系统区分"},
    {"term": "女德", "meaning": "本文指女性群体的共同行为规范（组织自己的德行），相对于旧的、被反对的女德而言", "evidence": "P017", "ambiguity": "作者未给出新女德的具体内容，只主张它绕不过去"},
    {"term": "自发大于自觉", "meaning": "对现状的阶段判断：行动由痛苦和刺激驱动，缺少自觉的纲领与研究", "evidence": "P002", "ambiguity": "作者未给出判定自觉／自发的标准"},
    {"term": "破／立", "meaning": "反对与否定为“破”，提出并追求自己要什么为“立”", "evidence": "P009", "ambiguity": "未说明“立”的具体形式"},
    {"term": "海盗旗", "meaning": "比喻把组织目标堕落为寻求一切否决权的路线", "evidence": "P022", "ambiguity": "比喻与历史教训的对应关系未逐项说明"}
   ],
   "examples_and_targets": [
    "中国女权（作者的论述对象）",
    "解放后妇女权利在立法上相对解放前的进步（作者用作对照的“上一个时代”成就）",
    "社交媒体（作者举出的重要进展条件）",
    "各种公众号、大V（作者批评其只帮读者说“不”）",
    "婆媳关系（作者举的“说了不，然后呢”的例子）",
    "旧的女德（作者承认可以反对的对象）",
    "新的女德（作者主张绕不过去但未给出内容）",
    "“这是你自己想要的”（作者指出主张自己要什么之后会遭遇的约束）",
    "寻求一切否决权（作者引述并认可的历史教训）",
    "几百万年的人类历史（作者援引的论证依据）"
   ],
   "conditions": [
    "判断限于“现在中国的女权”（P001、P002）",
    "“如果你们认同这个观点”引出全盘否定女德探讨的后果（P015）",
    "“任何真正想要作为一个整体去争取共同目标的群体”限定共同行动纲领命题的适用范围（P017）",
    "“在‘对想要什么避而不谈，仅仅只说不’这种实践之下”限定旗帜被实践成 power 的条件（P020）",
    "“无论你是否主动的意识到、是否赞成”为无条件让步式限定（P020）",
    "本文结尾自标“（未完，待续）”，属未完成文本（P023）"
   ],
   "rhetoric_and_tone": "论辩兼训诫。以第二人称复数“你们”直接对女权阵营说话，连续追问（“然后‘是’是什么呢？”“你要什么？”“新的女德是什么？”）；用“头戴王冠必承之重”“海盗旗”“死路”等比喻与重词；对公众号、大V的批评带讥诮；结尾“（未完，待续）”表明文本未完成。",
   "unresolved_questions": [
    "本文为系列未完篇（P023“未完，待续”），关于新女德的具体内容等后续论述缺失",
    "作者主张“新女德”绕不过去，但未给出其内容或形成方式",
    "“上一个时代”具体指哪一时段，作者未精确界定",
    "P022 引述的历史教训未注明出处，待外部核查",
    "P021 的“几百万年的人类历史”属概括性断言，未给出依据",
    "提问者所言“最大挑战”是提问者的设问框架，作者只给出自己的答案，未与其他候选挑战比较"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "最大的挑战在于缺少更深入的研究和阐述", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "自发大于自觉的，由痛苦和刺激驱动战术的应激式的反击的阶段", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "相当微不足道", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "通过社交媒体获得舆论的声援", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "说“不”的权力", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "仅仅说“不”并不能解决问题", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "ta们几乎都只是在帮你说“不”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你不能单纯的通过“破”来替代“立”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "这仍然是权利真正实质的部分", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "这是头戴王冠必承之重", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "而现在的女权运动对这一部分的努力是明显缺失的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "但是新的女德是什么？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "而只会导致“探讨它们的全是你们之外的人”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "关于共同行为规范（在这里即指女德）的探讨是必然存在的", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "都必然有一个共同行动纲领", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "新的女德是一个绕不过去的问题", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "你才能聚拢“我也想要这个”的同志", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "已经被实践成了“我们要尽可能的追求为所欲为的power”", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "至今没有任何一个组织在死亡之前实现了这个目标", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "这是一面海盗旗", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别议题", "社会运动", "伦理学", "组织理论"],
   "issue_candidates": ["中国女权发展的最大挑战", "只说“不”的局限", "新女德与共同行为规范", "组织共同行动纲领"],
   "text_function_candidates": ["答疑", "论辩", "批评", "训诫"],
   "object_candidates": ["中国女权运动", "公众号", "大V", "女性", "婆媳关系"],
   "working_keywords": ["女权", "power", "女德", "破与立", "共同行动纲领", "海盗旗", "否决权"]
  },
  "notes": "无图片节点。正文 23 段、1376 字符，一次读完；P023 为“（未完，待续）”，属未完成系列文本，后续论述缺失已登记。作者以“你们”称呼女权阵营，本记录区分了提问者设问（最大挑战是什么）与作者自答；批评对象（公众号、大V、“敌人”式排他做法）未被误归为作者主张。"
 },
 "42e026e0": {
  "analysis": {
   "question_context": "提问者问“你会选择原谅伤害过你的人吗？”（Q001，属提问者，其框架是“选择”）。作者不接受“选择”框架，改判为义务：原谅不是一种选择，而是生而为人的义务，是一种不容不选择的选择。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开场预告：下面的话也许匪夷所思、现在接受不了，建议先记住、将来慢慢验证。", "role": "qualification"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "核心主张：原谅是义务；不能原谅者必在灵魂上受得不偿失的伤害、损失本可得到的幸福，甚至以人生相殉。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "自设反驳性提问：若一律必须原谅，公平和正义怎么办；作者点明这是要害。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "张三赊面例：即使全额收款也是有爱；张三未付后仍继续赊、或降低赊欠额度，这就是原谅。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "同一例界分：索债但不再往来是不原谅；索债外加惩罚是报复。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025"], "summary": "辨析第三种“原谅”：全免债务、当一切没发生，不是宽宏大量而是纵容和溺害，只勾出贪求、依赖与逢迎，是慢性毒药。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030"], "summary": "定义与调和：原谅指不报复；不抹去是为公平，不追索是为宽容，故原谅不破坏公平正义。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "答疑：不索性抹去，是为了给对方留下自我治愈、原谅自己的机会。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040"], "summary": "回应“免人的债”之疑：定意绝不追索时债已免；记住未还之债是能量消耗与最后祭献，能力有限故终会忘记，债彻底免去。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "原谅的时点：不在对方亏欠时，而在开口赊账、已定意如此之时；原谅在爱中预定，爱是原谅而非供养。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P048", "P049", "P050", "P051"], "summary": "对做不到者的第一条：死守不报复的红线，做不到归做不到但不可故意不做；与对方配不配无关，是人对自己的信用。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057"], "summary": "第二条：反思为何轻视“一切可能的辜负”；爱之难难在被辜负的痛苦，低估辜负的爱是伪劣假冒之物，超过限度责任在自己。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P058", "P059", "P060", "P061", "P062", "P063", "P064"], "summary": "第三条：宽容自己，在错误中学会正确的自我估计；不怕错误，只怕“错误的错误”；越红线仍须向对方道歉。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P065", "P066"], "summary": "结语：贯穿一生如此行事者，将来必被人称遇见你为其一生最大幸运；努力原谅一切是人的义务。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原谅不是一种选择，而是生而为人的义务；其根据是人性的诅咒，故是一种不容不选择的选择。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论理由多正当、遭遇多值得同情，不能原谅者最后一定在灵魂上受到得不偿失的伤害，并损失本来可以得到的幸福，甚至可能以人生相殉。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者自设疑难：如果一律都必须原谅，公平和正义要怎么办？并称这正是原谅这件事的要害所在。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以张三赊面为例界分：继续赊账或降低赊欠额度（不追索）就是原谅；索债而断绝往来是不原谅；索债之外再加惩罚是报复。", "evidence": ["E6", "E7", "E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全免债务、让对方当一切没发生，不叫原谅而叫纵容和溺害，不配称为“爱”；它勾起的不是爱而是贪求、依赖与逢迎，是味道极相似的慢性毒药。", "evidence": ["E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原谅不破坏公平与正义，也不允许为贪图原谅带来的“爱”而损害公平正义；不抹去是为公平，不追索是为宽容。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不抹去、留着账等对方来还，是为了给对方机会原谅自己；治愈伤害最好的途径是对方记得这账而自己也终于还上。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "定意“绝不追索”时就已经免了人的债；而为对方保留痊愈机会记住未还之债要消耗能量，因人的能力不是无限的，之后就会忘记、债也彻底免了。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原谅发生在开口赊账、提前定意如此之时，而非对方亏欠之时；原谅是爱中预定的，是爱的预表，爱不是供养、爱是原谅。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对被辜负极深而做不到者，第一条是死死守住不报复的红线；做不到只能是尽力而为后的失误，绝不应是自己故意不做。", "evidence": ["E22", "E23"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "守红线与对方配不配这样的优待无关，理由是“人要对自己有信用”——说好是爱，那就要是爱。", "evidence": ["E24", "E25"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二条是反思自己为何如此轻视“一切可能的辜负”；爱之难不在付出而在被辜负的痛苦，低估辜负的爱不过是伪劣的假冒之物，超过限度责任就在自己头上。", "evidence": ["E26", "E27", "E28"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三条是宽容自己：在错误的自我估计中学会正确的自我估计，只要不自欺、不作弊，因能力不足造成的痛苦结果是“正确的错误”，并通向将来最终伟大的正确。", "evidence": ["E29", "E30", "E31"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "宽容自己意味着原谅自己，但原谅的红线仍在：若失控越过了红线，就要向对方抱歉，因为这是你欠自己、未被自己免除的债。", "evidence": ["E32", "E33"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "若真切的这样行事并能贯穿一生，将来必会有人回首一生时称遇见你为ta一生中最大的幸运、永不相忘；努力原谅一切是人的义务。", "evidence": ["E34", "E35"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者预告这些说法听众也许觉得匪夷所思、现在也接受不了，建议先记住、将来再慢慢验证。", "evidence": ["E36"]},
    {"claim_id": "C017", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "questioned", "statement": "文中引述“免人的债，如同你免了我的债”这一表述并据此追问：若一直记着账，岂不是没有所谓“免人的债”了；引文出处文中未注明。", "evidence": ["E37"]}
   ],
   "argument_steps": [
    "先给接受度提示：说法也许难以接受，建议先记住将来验证（P001）。",
    "以提问者的“选择”框架为反衬，直接下定义式判断：原谅是义务而非选择（P002）。",
    "给出义务的根据：不原谅必在灵魂上受伤、损失幸福乃至以人生相殉，故原谅是“不容不选择的选择”（P003、P004、P005）。",
    "自设反驳：一律原谅则公平正义何在；随即点明这是要害（P006、P007）。",
    "用张三赊面例展开：先说明赊账本身已是爱（不要利息、不要抵押、承担全部风险）（P008、P009）。",
    "张三未付款后，列出两类回应（继续赊／降低额度）并判定为原谅（P010—P013）。",
    "再列索债后断绝往来（不原谅）与索债外加惩罚（报复），完成四类行为的界分（P014—P018）。",
    "反驳第三种“原谅”（全免不追索）：那不是宽宏大量，而是纵容和溺害，勾出贪求与逢迎，是慢性毒药（P019—P025）。",
    "归纳定义：原谅是指不报复（P026）。",
    "调和公平正义：不抹去为公平，不追索为宽容，故二者不冲突（P027—P030）。",
    "追问为何不索性抹去，答以留账是为给对方自愈与自我原谅的机会（P031—P034）。",
    "引“免人的债”之问，答以定意不追索即已免债，且人能力有限终会忘记，债彻底免去（P035—P040）。",
    "追问原谅发生的时点，判定在预先定意赊账之时，并提出“原谅即爱的预表”（P041—P047）。",
    "对做不到者给出三条：死守不报复红线（P048—P051）；反思对辜负的低估（P052—P057）；宽容自己并守住红线（P058—P064）。",
    "以承诺式结语收束，重申原谅是人的义务（P065、P066）。"
   ],
   "concept_usage": [
    {"term": "原谅", "meaning": "本文界定为“不报复”，进一步展开为“不追索”：保留债务与公平，但克制追索与报复（P026、P029、P030）。", "evidence": "P026", "ambiguity": "作者同时否定了日常把“全免债务、当没发生”称为原谅的用法，故该词在本文属窄化定义"},
    {"term": "不原谅", "meaning": "索回欠款但断绝关系，即免除责任之外仍保留关系上的排斥（P014、P016）。", "evidence": "P016", "ambiguity": "与“报复”“原谅”的边界靠是否附加惩罚来区分，作者未给出更细判准"},
    {"term": "报复", "meaning": "在索债之外附加惩罚、羞辱或持续威胁（P017、P018）。", "evidence": "P018", "ambiguity": "作者后文以“红线”称之，但未逐项界定哪些行为越线"},
    {"term": "纵容和溺害", "meaning": "指全免债务、宣告一切没发生以求“虚假的爱”，作者判定其不配称爱（P021、P022）。", "evidence": "P021", "ambiguity": "作者强调“即使加上溺”也不配称爱，语气强于一般用法"},
    {"term": "公平与正义", "meaning": "靠“不抹去”（债务与责任仍被记住）保全；原谅不得为贪图爱而损害之（P027、P030）。", "evidence": "P030", "ambiguity": "未说明债的清算由谁执行"},
    {"term": "宽容", "meaning": "本文限定为“不追索”，与公平（不抹去）分工并存（P028、P029、P030）。", "evidence": "P029", "ambiguity": "作者明确把宽容与抹去债务区分开"},
    {"term": "爱", "meaning": "爱不是供养而是原谅；爱是对可能的一切辜负的、预先许诺的和最后赠予的原谅（P046、P047）。", "evidence": "P047", "ambiguity": "文中“爱”带明显神学语汇色彩，但未点明宗教立场"},
    {"term": "红线", "meaning": "指不可逾越的不报复界限；可以“做不到”，但不可故意不做（P049、P063）。", "evidence": "P049", "ambiguity": "红线内容文中以“不报复”概括，未给出操作判准"},
    {"term": "正确的错误", "meaning": "没有自欺、没有作弊、尽力相爱而因能力不足造成的痛苦结果（P059）。", "evidence": "P059", "ambiguity": "与“错误的错误”的对照标准依赖作者后文“最终伟大的正确”，所指未说明"},
    {"term": "免人的债", "meaning": "作者引用的说法，用于说明“定意不追索”即已完成免除（P035、P036）。", "evidence": "P035", "ambiguity": "引文出处未注明"}
   ],
   "examples_and_targets": [
    "张三赊面（P008—P021）：作者自设的假设例证，张三为假设人物，非真实事件；用于界分原谅／不原谅／报复／纵容。",
    "“免人的债，如同你免了我的债”（P035）：作者引述的表述，来源未注明，属引用材料，待外部核查。",
    "“摘星掬月、鞠躬尽瘁”（P045）：修辞材料，用以说明爱可以只是举手之劳。",
    "“我实实在在的告诉你们”（P065）：带宗教语感的宣告式修辞。",
    "反驳对象：把“全免债务、当一切没发生”当成宽宏大量与爱的流行理解（P019—P024），属作者在本文反驳的观点，非作者主张。"
   ],
   "conditions": [
    "“无论人有多正当的理由、有多值得人同情的遭遇”——条件推到极端，结论仍成立（P003）。",
    "即使全额收款也仍算有爱，前提是没有利息、没有抵押、承受全部风险（P009）。",
    "宽容以不抹去为前提：不追索但账仍记得（P030）。",
    "不抹去是为给对方机会，其成立依赖对方终会来还（P032、P034）。",
    "免除债务的效果附条件：须“定意绝不追索”；而且记住未还之债受“能力不是无限的”限制（P036、P037、P039）。",
    "对做不到者的要求以“尽管困难，尽管有时失控”为限定，允许失误但不允许故意不做（P049）。",
    "“你有几次机会以‘无知’自辩，但超过一定的限度”——责任转移有界限（P056）。",
    "结语承诺以“如果你们真切的这样行事，而能贯穿一生”为条件（P065）。"
   ],
   "rhetoric_and_tone": "训诫与布道式语气为主：第二人称“你们”直接称呼读者，开场先承认听者可能接受不了，再以宣告句下判（“这就是原谅”“这就是不原谅”“这就是报复”）；大量反问设问（“看懂了吗？”“是为公平和正义要怎么办？”“是为了怕爱会亏本吗？”），以张三赊面的分镜头式假设场景与斜杠并列的惩罚清单（“我要揍你一顿 / 再见你一次打你一次”）制造具体感，兼用“实实在在的告诉你们”“不容不选择的选择”等强断言与祝福式收尾；对“第三种原谅”用词转冷，判为纵容、溺害、慢性毒药。",
   "unresolved_questions": [
    "“免人的债，如同你免了我的债”未注明出处，其经文来源与语境需外部核查（P035）。",
    "“以人生相殉”（P004）具体所指未说明。",
    "“最终伟大的正确”（P060）与其孕育分娩的比喻所指主体未说明，是否为神学框架文中未点明。",
    "不报复“红线”的越线判准未给出：哪些行为算红线内、哪些算越线，文中未列举（P049、P063）。",
    "公平靠“不抹去”保全，但谁来追索、何时清算，文中未说明（P030、P034）。",
    "本篇 updated_at 为 2026-07-05、晚于 2021-01-27 发表时间，是否存在平台侧修订或版本差异，无法从本记录判断。",
    "开头“你们”所指读者群（是否特定群体）未说明，属称呼上的不确定性（P001、P006）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "原谅，不是一种选择，而是一种生而为人的义务。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "宣告了原谅是一种义务，一种不容不选择的选择", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "到最后都一定会在灵魂上受到得不偿失的伤害", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "甚至可能以人生相殉。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "如果一律都必须原谅，那么公平和正义要怎么办？", "relation": "context"},
    {"key": "E6", "paragraph_id": "P011", "quote": "只要你补齐面钱，我还可以继续这样赊给你", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "这就是原谅。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "你还我钱，还上以后再也不要出现了", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "plus，我要罚你多还利息", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P021", "quote": "这不叫原谅，这叫作纵容和溺害", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P023", "quote": "勾起来的并不是爱，而是贪求、是出于软弱和贪婪的依赖", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P027", "quote": "原谅并不破坏公平与正义", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P030", "quote": "不抹去，是为公平；不追索，是为宽容。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P032", "quote": "不抹去，等着你来还，是为了给你机会原谅你自己。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P034", "quote": "治愈最好的途径，就是对方记得这账，而自己也终于还上了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P036", "quote": "当你定意“绝不追索”的时候，你已经免了人的债了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P037", "quote": "是要消耗能量的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P040", "quote": "之后，你就会忘记。ta的债也就彻底免了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P043", "quote": "提前已经想好这一切的一切，已经定意要如此", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P044", "quote": "原谅是爱中预定的，原谅即爱的预表。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P047", "quote": "爱不是供养，爱是原谅。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P049", "quote": "死死的守住不报复的红线", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P049", "quote": "做不到归做不到，做归做。", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P050", "quote": "这是因为人要对自己有信用。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P051", "quote": "说好是爱，那就要是爱。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P052", "quote": "反思自己为什么如此轻视“一切可能的辜负”", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P054", "quote": "难不是难在付出，而是难在被辜负的痛苦。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P057", "quote": "低估辜负的爱，不过是伪劣的假冒之物而已。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P058", "quote": "你总要在错误的自我估计中学会正确的自我估计。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P059", "quote": "是错误，但是正确的错误。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P061", "quote": "你们不要怕错误，你们要怕的是错误的错误。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P063", "quote": "宽容自己，当然意味着原谅自己。但是你们要记清楚，原谅的红线何在。", "relation": "qualifies"},
    {"key": "E33", "paragraph_id": "P064", "quote": "因为这是你欠你自己的，未被你自己免除的债。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P065", "quote": "称遇见你为ta一生中最大的幸运，永不相忘。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P066", "quote": "努力原谅一切，是人作为人的义务。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P001", "quote": "但建议先记住了，将来再慢慢验证。", "relation": "qualifies"},
    {"key": "E37", "paragraph_id": "P035", "quote": "“免人的债，如同你免了我的债”怎么办呢？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理道德", "宗教／神学语汇（赦免、债、祭献、预表）", "人际与亲密关系", "心理与自我修复"],
   "issue_candidates": ["原谅是否为义务", "公平正义与宽容的界限", "报复与纵容的界线", "被辜负后的自我治愈", "道德红线与自我信用"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "训诫／劝谕", "经验总结"],
   "object_candidates": ["张三（作者自设的假设人物）", "受伤害者", "辜负他人者", "神（作为修辞与神学参照，未明确指认）"],
   "working_keywords": ["原谅", "不追索", "不报复", "宽容", "公平与正义", "纵容和溺害", "红线", "爱", "免人的债", "正确的错误", "预表"]
  },
  "notes": "无图片节点。正文 66 段、2339 字符，一次读完。提问者设问“你会选择原谅伤害过你的人吗？”（Q001）已与作者立场区分：作者否定“选择”框架，主张原谅是义务（P002）。张三为作者自设的假设例证，非真实人物，未当作事实断言。P035 引述“免人的债，如同你免了我的债”未注明出处，已登记待外部核查，未据此推断作者宗教立场。反驳对象（把全免债务当宽宏大量的流行理解，P019—P024）标为被反驳观点，未归给作者。updated_at（2026-07-05）晚于 published_at（2021-01-27），版本差异无法判断，已登记于未决问题。"
 },
 "2993d264": {
  "analysis": {
   "question_context": "提问者问：如何看待某媒体发文号召年轻人到制造业去，去工厂是否会发展成未来就业的趋势？（Q001，属提问者；“某媒体”未具名）。作者没有直接评述该媒体或回答“是否成为趋势”，而是对号召做规范性改写：年轻人应该到“先进制造业”去，并指出要先搞清楚什么是工业4.0。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "改写号召：不谈笼统的“制造业”，年轻人应该到先进制造业去，并先搞清楚什么是工业4.0。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "断言智能制造前途光明；以特斯拉、丰田不会只需一家、中国起码千家起步估计需求规模。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "理由：各领域与技术革命突破性成果结合都可能产生颠覆性新产品，且产品面向全球制造、须在发布会前后保密期内完成产能爬坡。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "推论：大厂秘密组建新产线将越来越常见，熟手只能从现有智能产线上找，而其去留能决定上亿订单归属。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "需求量以“论千论万”计，未来研发、管理和维护需求是职业蓝海之一，也是很好的创业方向。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "以特斯拉学生招聘页面链接收尾，作为行动指引。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把号召改写为：年轻人应该到“先进制造业”去，而不是笼统的制造业；并应先搞清楚什么是工业4.0。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "智能制造前途非常光明；特斯拉和丰田这类企业地球上绝对不会只需要一家，单中国起码也要千家起步。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "道理很简单：任何领域和新通信技术、新能源技术、新生物技术这类技术革命中的突破性成果结合，都可能产生颠覆性的新产品。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类产品总是面向全球制造，制造要求常常是在发布会前后两三个月的保密期内就要完成产能爬坡。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "这会让“某大厂在疯狂寻找智能制造工程师秘密组建新产线”这种场景在下一个十年里成为越来越常见的现象。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类人只能到特斯拉、丰田、ABB、大疆等现有智能产线上找参加过此类项目的熟手。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问指出：这些熟手能决定下一个总需求量上亿的产品的订单是否落在你家，其待遇应当如何（作者用反问表达而未直接给出结论）。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "等着整个换代的产品数量极多，以“论千论万”计。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "未来庞大的研发、管理和维护需求是将来的职业蓝海之一，而且是很好的创业方向。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "以“修改一下就好”开场，先改写提问中的号召（P001）。",
    "给出改写后的规范判断：应到先进制造业去，并先搞清楚工业4.0（P002、P003）。",
    "断言智能制造前途光明，用特斯拉、丰田与“千家起步”给出规模预期（P004、P005）。",
    "给出“道理”：技术革命突破性成果与各领域结合产生颠覆性新产品（P006）。",
    "补充制造业特征：面向全球制造，须在保密期内完成产能爬坡（P007）。",
    "由此推出现象预测：大厂秘密组建新产线将越来越常见（P008）。",
    "追问人才来源：只能从现有智能产线的熟手中找（P009）。",
    "以反问抬升该岗位的分量——其决定上亿订单归属，故待遇问题随之而来（P010）。",
    "再以“论千论万”的换代需求说明总量（P011、P012）。",
    "结论：研发、管理和维护需求构成职业蓝海与创业方向（P013）。",
    "附招聘链接作行动指引（P014）。"
   ],
   "concept_usage": [
    {"term": "先进制造业", "meaning": "作者用以替换提问中笼统的“制造业”，指与工业4.0、智能制造相关的那部分制造业（P002、P003）。", "evidence": "P002", "ambiguity": "作者未给出界定标准，只要求读者“搞清楚什么是工业4.0”"},
    {"term": "工业4.0", "meaning": "作者要求先搞清楚的术语，但在本文未作任何解释（P003）。", "evidence": "P003", "ambiguity": "全文未定义，属未说明的关键概念"},
    {"term": "智能制造", "meaning": "与特斯拉、丰田、ABB、大疆的“智能产线”相关联的制造形态（P004、P008、P009）。", "evidence": "P004", "ambiguity": "与工业4.0、先进制造业的关系文中未说明"},
    {"term": "产能爬坡", "meaning": "在发布会前后两三个月的保密期内就要完成的量产准备（P007）。", "evidence": "P007", "ambiguity": "未说明难度来自工艺、供应链还是人力"},
    {"term": "熟手", "meaning": "参加过此类项目、在现有智能产线上工作过的人（P009）。", "evidence": "P009", "ambiguity": "无"},
    {"term": "职业蓝海", "meaning": "作者对未来研发、管理和维护需求所构成的就业空间的称呼（P013）。", "evidence": "P013", "ambiguity": "未给出时间尺度与规模测算"}
   ],
   "examples_and_targets": [
    "特斯拉、丰田（P004、P009）：作为智能制造需求规模的例证，属作者证据／类比；ABB、大疆（P009）同列为人才来源企业。",
    "“某大厂在疯狂寻找智能制造工程师秘密组建新产线”（P008）：作者引述式设想的未来场景，非已发生事件。",
    "新通信技术、新能源技术、新生物技术（P006）：作为技术革命突破性成果的类别举例。",
    "https://www.tesla.cn/careers/students（P014）：作者给出的外部招聘链接，页面内容未核验。",
    "提问者提到的“某媒体发文号召”（Q001）：提问者转述，作者未评述该媒体，也未引用其原文。"
   ],
   "conditions": [
    "“任何领域……结合，都可能产生颠覆性的新产品”——以“可能”表述，属可能性而非必然（P006）。",
    "“制造要求常常是……”——以“常常”限定，非全称（P007）。",
    "现象预测限定在“下一个十年里”（P008）。",
    "规模估计“单中国起码也要千家起步”为作者的估计，未给出测算依据（P005）。",
    "岗位重要性依赖“下一个总需求量上亿的产品”这一前提（P010）。",
    "先进制造业的范围以“搞清楚什么是工业4.0”为前置条件（P003）。"
   ],
   "rhetoric_and_tone": "短答、逐条分行，句间跳跃大。以“修改一下就好——”的改写姿态回应提问者的号召，语气直接、断言式（“前途非常光明”“绝对不会只需要一家”）；连续使用反问推进（“这些人能去哪里找？”“你觉得ta们待遇应该如何？”“人类有多少产品要等着整个换代？”），以极简答句“论千论万”作强调；结尾直接给出招聘链接，属行动指引而非论证。",
   "unresolved_questions": [
    "“工业4.0”被要求搞清楚但全文未定义（P003）。",
    "“单中国起码也要千家起步”的测算依据未说明（P005）。",
    "提问者所称“某媒体”未具名，作者亦未评述该媒体原文，无法核对其号召的具体表述（Q001）。",
    "P014 仅为一个特斯拉招聘页链接，链接内容未打开核验，待外部核查。",
    "正文末段为裸链接，且渲染包标出“lexical未覆盖片段”，需确认该链接是否属作者正文还是平台附加内容。",
    "本文 updated_at（2025-10-01）晚于 published_at（2021-01-27），是否存在平台侧修订无法从本记录判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "年轻人应该到先进制造业去。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "搞清楚什么是工业4.0。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "智能制造前途非常光明。特斯拉和丰田地球上绝对不会只需要一家。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "单中国起码也要千家起步。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "都可能产生颠覆性的新产品", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P007", "quote": "制造要求常常是在发布会前后两三个月的保密期内就要完成产能爬坡", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这种场景在下一个十年里成为越来越常见的现象", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "当然是去现在特斯拉、丰田、ABB、大疆……之类的智能产线上找参加过这类项目的熟手", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你觉得ta们待遇应该如何？", "relation": "context"},
    {"key": "E10", "paragraph_id": "P011", "quote": "人类有多少产品要等着整个换代？", "relation": "context"},
    {"key": "E11", "paragraph_id": "P012", "quote": "论千论万。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "未来庞大的研发、管理和维护需求是将来的职业蓝海之一，而且是很好的创业方向。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业经济与制造业", "就业与职业发展", "技术与产业升级（工业4.0、智能制造）"],
   "issue_candidates": ["年轻人是否应进入制造业", "先进制造业与普通工厂岗位的区别", "智能制造人才稀缺与待遇", "职业蓝海与创业方向"],
   "text_function_candidates": ["答疑（短答）", "评论", "预测", "行动建议"],
   "object_candidates": ["特斯拉", "丰田", "ABB", "大疆", "某媒体（提问者提及，未具名）", "年轻人", "某大厂（作者设想场景）", "中国"],
   "working_keywords": ["先进制造业", "工业4.0", "智能制造", "产能爬坡", "智能产线", "熟手", "职业蓝海", "千家起步"]
  },
  "notes": "无图片节点。正文 14 段、430 字符，一次读完，属短答。提问者为“某媒体号召”与“是否成为趋势”（Q001），作者未评述该媒体，而是改写为“应该到先进制造业去”的规范判断，二者已区分。文中企业的规模表述（特斯拉、丰田、千家起步）为作者估计与例证，未当作已证实的外部事实。P014 为裸链接（特斯拉学生招聘页），页面内容未核验，已登记待外部核查。正文末尾存在平台相关链接/未覆盖片段，渲染包以“⚠lexical未覆盖片段”标出，已登记于未决问题。"
 },
 "70573ee8": {
  "status": "needs_reread",
  "full_text_checked": False,
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问：核弹爆炸时，会有一个合适的距离把披萨烤熟吗？（Q001，属提问者）。作者先做物理换算与问题转译，再给出带条件的乐观回答，并以一个几何摆放设想收尾。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "换算与转译：核弹光辐射不到三秒、含火球热辐射也只十几秒，故问题等价于能否靠提高火力把需烤二十分钟的披萨在十几秒内烤熟。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "限定：答案取决于“披萨”薄到什么程度还叫披萨、熟到什么样子可以叫做熟。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "回答“很乐观”：果木窑炉几十秒、炉温400摄氏度即可烤熟，不构成数量级差异，只是口感可能不好。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "设想方案：沿螺旋渐开线摆放一圈由耐温玻璃保护的披萨饼，其中应有一段口感尚可。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "核弹的光辐射释放只有不到三秒，算上高温火球的热辐射也只能维持十几秒。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "该提问实质上等价于另一个问题：可不可以靠提高火力，把一个需要烤二十分钟的披萨在十几秒内烤熟。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "能否烤熟取决于定义边界：披萨薄到什么程度还叫披萨，以及熟到什么样子可以叫做熟。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "答案是“很乐观”：果木窑炉只需几十秒就能烤熟披萨、炉温400摄氏度，故不是数量级的差异，大概只是口感不见得好。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "设想：可沿螺旋渐开线摆放一圈由耐温玻璃保护的披萨饼，其中应有一段的口感尚可。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "先给出核爆热辐射的持续时间（光辐射不到三秒，加火球热辐射十几秒）（P001）。",
    "把原问题转译为“能否靠提高火力把二十分钟的披萨在十几秒内烤熟”（P002）。",
    "指出答案取决于“披萨”与“熟”的边界定义（P003）。",
    "以果木窑炉几十秒、400摄氏度作为对照，判定“很乐观”，并说明差异不在数量级、只在口感（P004、P005）。",
    "以一个几何摆放设想（螺旋渐开线、耐温玻璃）给出可行的幽默方案（P006）。"
   ],
   "concept_usage": [
    {"term": "光辐射／热辐射", "meaning": "作者用以计算核爆可用加热时间的物理量；光辐射不到三秒，含火球热辐射共十几秒（P001）。", "evidence": "P001", "ambiguity": "未说明距离、当量与遮挡条件"},
    {"term": "火力", "meaning": "提高加热功率的通俗说法，问题被化为“火力能否在更短时间内烤熟”（P002）。", "evidence": "P002", "ambiguity": "未换算为具体热流密度"},
    {"term": "披萨（薄到什么程度还叫披萨）", "meaning": "作者把“披萨”的边界当作判定答案的前提之一（P003）。", "evidence": "P003", "ambiguity": "未给出厚度阈值"},
    {"term": "熟（熟到什么样子可以叫做熟）", "meaning": "作者把“熟”的标准当作另一前提，与口感区分（P003、P005）。", "evidence": "P003", "ambiguity": "未给出熟度判准"},
    {"term": "数量级的差异", "meaning": "作者用果木窑炉几十秒与十几秒的比较，判定两者不在数量级上（P005）。", "evidence": "P005", "ambiguity": "无"},
    {"term": "螺旋渐开线", "meaning": "设想中披萨的摆放几何，用来让一圈披萨落在不同受热强度上（P006）。", "evidence": "P006", "ambiguity": "未说明为何选此曲线"}
   ],
   "examples_and_targets": [
    "果木窑炉（P004）：作者用作温度与时间的类比／对照证据（几十秒、400摄氏度）。",
    "400摄氏度与“几十秒”（P004）：作者给出的数据，待外部核查。",
    "耐温玻璃（P006）：设想中的保护材料，非既有事实。",
    "IMG001（asset.sooon.ai 图片节点）：未核验，内容不明，需图像复核。"
   ],
   "conditions": [
    "时间前提：光辐射只有不到三秒、含火球热辐射只能维持十几秒（P001）。",
    "“能不能熟”以“披萨薄到什么程度还叫披萨，以及熟到什么样子可以叫做熟”为条件（P003）。",
    "结论以果木窑炉几十秒、400摄氏度为参照，属类比而非核爆条件下的实测（P004）。",
    "口感判断用“大概只是口感不见得好罢了”的推测语气（P005）。",
    "方案中“其中应有一段的口感尚可”为推测，未论证（P006）。"
   ],
   "rhetoric_and_tone": "简短冷静的估算式科普口吻，兼带调侃：先做“这实际上是在问这样一个问题”的概念转译，答案加引号写作“很乐观”；以“大概”“应有一段”保留不确定；结尾用螺旋渐开线、耐温玻璃等具体细节制造一本正经的幽默画面。",
   "unresolved_questions": [
    "IMG001 图片未核验：子代理无读图能力，图片内容（是示意图还是成品图）不明，需人工或多模态复核。",
    "“果木窑炉只需要几十秒就能烤熟披萨，炉温400摄氏度”为作者给出的数据，待外部核查（P004）。",
    "“披萨”的厚度阈值与“熟”的判定标准文中未给出（P003）。",
    "未说明提问所涉的距离、当量、遮挡与爆高条件，故结论的适用范围不明（P001、P002）。",
    "螺旋渐开线摆放与耐温玻璃方案在核爆环境下的可行性未论证（P006）。",
    "本篇 updated_at（2026-01-22）晚于 published_at（2021-01-27），是否存在平台侧修订无法从本记录判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "核弹的光辐射释放只有不到三秒", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "也只能维持十几秒", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "可不可以通过提高火力把一个需要烤二十分钟的披萨在十几秒内烤熟？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "这取决于披萨薄到什么程度还叫披萨，以及熟到什么样子可以叫做熟。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P004", "quote": "果木窑炉只需要几十秒就能烤熟披萨，炉温400摄氏度", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "这不是数量级的差异，大概只是口感不见得好罢了。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P006", "quote": "可以沿螺旋渐开线摆放一圈由耐温玻璃保护的披萨饼，其中应有一段的口感尚可。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["核武器效应／热辐射", "食品科学与烹饪", "科普问答与估算"],
   "issue_candidates": ["核爆热辐射持续时间", "极端热源下能否烤熟食物", "“披萨”与“熟”的定义边界"],
   "text_function_candidates": ["科普答疑", "问题转译", "估算", "设想／幽默推演"],
   "object_candidates": ["核弹（光辐射、火球）", "披萨", "果木窑炉", "耐温玻璃", "IMG001 图片"],
   "working_keywords": ["光辐射", "热辐射", "火球", "十几秒", "火力", "果木窑炉", "400摄氏度", "螺旋渐开线", "耐温玻璃", "数量级"]
  },
  "notes": "本篇含 1 个图片节点（IMG001，src=//asset.sooon.ai/2021-01/27/bac625373507e9780d0fce0db1f00aae.jpg），图片内容未经核验，子代理无读图能力，故 status=needs_reread、image_checked=false，full_text_checked 记为 false（正文 6 段 213 字符已读完，但图片未核）。未根据图片标题或上下文补写任何图片内容。图片未核验，需人工或多模态复核（见 unresolved_questions）。"
 },
 "ce505c6b": {
  "analysis": {
   "question_context": "提问者问：如何安全的离开有暴力倾向且偏执型人格的男朋友？（Q001，属提问者，其框架是“如何做到绝对安全”）。作者否定该框架本身——不存在“绝对安全”的办法——并把问题改写为：先下定离开的决心，再谈如何把最坏情况的概率降到最低。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接否定：没有“绝对安全”的办法；法律、公安、家人、朋友的保护能解决一些问题但仍谈不上绝对安全。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "困难加剧的条件（家人关系不好、缺少肯挡在危险前的朋友）；并澄清防护与求助不是不要做，而是它们代替不了离开的决心。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "理由：没有决心会使帮助者承担大得多且完全不公平的责任、甚至被指责“挑拨离间”；有洞察力的人看得出来，于是更得不到帮助、被锁死在困境里。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "核心要求：决心第一重要，要在根本没办法的时候就【先有】决心。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "解释家暴、压迫、奴役何以常贯穿一生：摆脱它是冒生死风险的决定，权衡之下“再忍忍吧”，且行动只要不是瞬间完成、多给两三天就又滑回去。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "要求抛弃“万全之策”的幻想；先下“最坏也做”的决心，再去降低最坏情况概率；概率不可能为零，故须做完全心理准备，这一关绕不过去。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "责任归属：这不是不同情不理解，但这仍是你自己命运里须自己完全承担的责任；应在提问之前先下决心。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "改写提问：正确的问法是“决心要离开有暴力倾向男友，如何尽可能保证安全？”，只有这样才能有靠谱答案。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025"], "summary": "收束：死里逃生一回才懂保持自由要如何防患于未然、防微杜渐；警惕“小霸道”背后藏着的獠牙；祝愿逃出生天并知警醒。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P026"], "summary": "正文末段混入另一条与本文主题无关的问题标题行（“该怎么拒绝自己不喜欢的好男生？把伤害降到最低？”），疑为平台相关问答链接。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不存在“绝对安全”的离开办法；借助法律、公安、家人、朋友的保护可以解决一些问题，但仍然谈不上“绝对安全”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在家暴情境下，如果家人关系不好、也没有肯挺身挡在危险之间的朋友，安全离开就更困难。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里没有easy way out；上面的防护不是不要做、帮助不是不要寻求，而是它们代替不了“你宁可直面威胁也要离开的决心”。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若当事人没有决心，帮她的人会承担大得多（更不用说完全不公平）的责任，甚至在其反复后被指责“挑拨离间”；而有能力帮你的人往往看得出这种危险，于是当事人更难得到必要帮助、更被锁死在困境里。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "决心第一重要，要在根本没办法的时候就【先有】决心。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家暴、压迫、奴役常可贯穿一生，是因为摆脱这种关系涉及要不要冒生死风险的重大决定：拿“已经证明受得住的痛苦”去换可能致残、丧命的风险很难换得过去，于是“再忍忍吧”；而行动只要不是瞬间完成，多给两三天就又滑回去了。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要抛弃“有一种绝妙的万全之策”的幻想：必须先下定“无论如何，就算是发生最坏的结果，我也要这么做”的决心，然后才能谋划把最坏情况发生概率降到最低。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最坏情况的概率不可能下降到零，故仍需要做完全的心理准备，这一关绕不过去，必须先过这一关再考虑别的路线。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不是不同情、不理解，但这仍然是你自己命运里需要你自己完全承担的责任；你要在问这个问题之前先下定决心，然后再来问问题。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个问题正确的问法应该是“决心要离开有暴力倾向男友，如何尽可能保证安全？”；只有这样问才会有靠谱的答案，才是人类可以试一试回答的问题。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "人只有这么死里逃生一回，才会真正明白想要保持自由需要怎样的防患于未然和防微杜渐。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提醒：一些看似亲热的玩笑话、一些让不懂的人倍觉“温馨”的“小霸道”，背后藏着可怕的獠牙。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "开门即以“很遗憾”否定提问框架：没有“绝对安全”的办法（P001）。",
    "退一步承认外部保护的作用，但仍判定其达不到“绝对安全”（P002）。",
    "指出更困难的条件：家人关系不好、没有肯挡在危险之间的朋友（P003）。",
    "澄清立场：不是不要防护、不要求助，而是它们代替不了离开的决心（P004）。",
    "给出理由：没有决心会让帮助者承担不公平责任并可能被指责“挑拨离间”，有洞察力的人看得出，于是更得不到帮助，被锁死在困境里（P005、P006）。",
    "点明要求：决心第一重要，要在毫无办法时先有决心（P007）。",
    "自设问题解释普遍性：摆脱暴虐关系是冒生死风险的决定，权衡后倾向“再忍忍吧”，且行动只要不瞬间完成就会滑回去（P008—P011）。",
    "要求抛弃“万全之策”的幻想（P012、P013）。",
    "给出正确次序：先下最坏也做的决心，再谋划降低概率（P014）。",
    "补充限定：概率不可能为零，故须做完全心理准备，这一关绕不过去（P015—P018）。",
    "明确责任归属并提出改问：这是你自己须完全承担的责任，应在提问之前先下决心（P019、P020）。",
    "给出改写后的问题形式，并说明只有这样问才有靠谱答案（P021、P022）。",
    "以经验之谈与祝愿收束：死里逃生一回才懂防微杜渐，警惕“小霸道”下的獠牙，愿其逃出生天并知警醒（P023—P025）。"
   ],
   "concept_usage": [
    {"term": "绝对安全", "meaning": "提问者预设的目标，作者明确否定其可达，并指出外部保护只能解决“一些问题”（P001、P002）。", "evidence": "P001", "ambiguity": "作者未给出可接受的残余风险水平"},
    {"term": "决心", "meaning": "本文的核心要求：宁可直面威胁也要离开的意志，且要先于一切方案存在（P004、P007、P014）。", "evidence": "P007", "ambiguity": "如何取得决心，文中只以“先有”强调，未给方法"},
    {"term": "easy way out", "meaning": "作者用英文短语指省力出路，明确判定此处没有（P004）。", "evidence": "P004", "ambiguity": "无"},
    {"term": "再忍忍吧", "meaning": "作者引述受害者权衡后的典型心态（P010）。", "evidence": "P010", "ambiguity": "属作者概括，未给出经验依据"},
    {"term": "万全之策", "meaning": "作者要求抛弃的幻想，即能让人不必作出最艰难决定的方案（P013）。", "evidence": "P013", "ambiguity": "无"},
    {"term": "小霸道", "meaning": "作者指关系中看似亲热、被外人觉得“温馨”的控制性言行（P024）。", "evidence": "P024", "ambiguity": "未给出识别标准"}
   ],
   "examples_and_targets": [
    "法律、公安、家人、朋友的保护（P002）：作者承认其部分作用的求助与防护途径，未展开具体做法。",
    "“决心动摇了，飞速跳回去了，还要为了乞讨对方的原谅指责帮ta的人‘挑拨离间’”（P005）：作者描述的反覆情形，属概括性叙述，非特定个案。",
    "家暴、压迫、奴役（P008、P009）：作者用以说明暴虐关系何以长期持续的类比性列举。",
    "“杯弓蛇影、草木皆兵的后半生”（P009）、“背后藏着可怕的獠牙”（P024）：修辞材料。",
    "P026“该怎么拒绝自己不喜欢的好男生？把伤害降到最低？”：与本文主题无关的问题标题行混入正文末段，疑为平台相关问答链接，非作者论述。"
   ],
   "conditions": [
    "“尤其是如果家人关系不好、也没有肯挺身挡在你和危险之间的……朋友”——困难程度随支持条件变化（P003）。",
    "防护与求助的作用被限定为“可以解决一些问题”，不等于安全（P002）。",
    "滑回去的条件是“只要这个动作不是那么瞬间就能完成，只要多给两三天”（P011）。",
    "次序条件：必须先下决心，然后才能谋划降低最坏情况概率（P014）。",
    "概率条件：无论想多少办法，概率都不会是零（P015）。",
    "“人只有这么死里逃生一回，才会真正的明白”——作者以“只有……才”限定该认识的取得方式（P023）。"
   ],
   "rhetoric_and_tone": "直接、急切、训诫式。第二人称“你／你们”贯穿全篇，以“很遗憾”开场先否定问题；短句独立成段强调（“看清楚，必须。”“不是不同情你，也不是不理解你”）；自设问句并作答（“为什么家暴、压迫、奴役常常可以贯穿人的一生？”）；用【先有】方括号加着重；以“杯弓蛇影、草木皆兵”“獠牙”等尖锐比喻形容处境与“小霸道”；批评受害者的犹疑但明确表示不是不同情，结尾转为祝愿（“希望你这次能逃出生天”）。",
   "unresolved_questions": [
    "P026 混入与本文主题无关的问题标题行（“该怎么拒绝自己不喜欢的好男生？把伤害降到最低？”），疑为平台相关问答链接混入正文，需与原文/平台核对；本记录未据其推断任何作者主张。",
    "作者提到法律、公安、家人、朋友的保护，但未给出任何具体求助渠道或操作步骤（P002、P004）。",
    "“对方之所以有能力，很大程度上就来自于这种洞察力”（P005）为作者的概括性判断，未给出依据，待外部核查。",
    "“决心”如何取得、在无法下决心时怎么办，文中只以“先有”强调，未给方法（P007）。",
    "安全离开的具体方案（报警、庇护、搬迁、证据保存等）作者明确未展开，属本文未说明。",
    "本篇 updated_at（2021-05-15）晚于 published_at（2021-01-28），是否存在平台侧修订无法从本记录判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "没有什么“绝对安全”的办法。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "借助法律、公安、家人、朋友的保护，可以解决一些问题，但是仍然谈不上“绝对安全”。", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P003", "quote": "也没有肯挺身挡在你和危险之间的那种事前奋不顾身、事后也无怨无悔的朋友", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P004", "quote": "它们代替不了你宁可直面威胁也要离开的决心。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而这样的危险，真有能力帮你的人往往是看得出来的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "更加得不到必要的帮助，更加被锁死在这种困境里面。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "决心第一重要，要在根本没办法的时候，就【先有】决心。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "其实是一个涉及到要不要冒生死风险的重大决定", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "拿“已经证明受得住的痛苦”，去换可能致残、丧命的风险", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "只要多给两三天，就又滑回去了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "抛弃会有“一种绝妙的万全之策”可以帮助你不必作出最艰难的决定的幻想。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "你要先下定“无论如何，就算是发生最坏的结果，我也要这么做”的决心", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "无论你想多少办法，概率都不会是零。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "你就还是需要做完全的心理准备——你绕不过去。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "这仍然是你自己的命运里需要你自己来完全承担的责任。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "你要在问这个问题之前，下定决心，然后再来问问题。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "这个问题正确的问法应该是“决心要离开有暴力倾向男友，如何尽可能保证安全？”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "只有这样问，才会有靠谱的答案", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "才会真正的明白想要保持自由是要怎么样的防患于未然和防微杜渐。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "一些让不懂的人倍觉“温馨”的“小霸道”，背后藏着可怕的獠牙。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系暴力与人身安全", "心理与决策（决心、风险权衡）", "法律与社会求助途径", "人生建议／训诫"],
   "issue_candidates": ["如何离开有暴力倾向的伴侣", "是否存在“绝对安全”的方案", "外部帮助与当事人决心的关系", "受害者反覆与责任归属", "控制性言行的识别"],
   "text_function_candidates": ["答疑", "训诫／劝谕", "问题改写", "风险提示", "经验总结"],
   "object_candidates": ["提问者（女性当事人）", "有暴力倾向且偏执型人格的男朋友", "法律", "公安", "家人", "朋友", "帮ta的人"],
   "working_keywords": ["绝对安全", "决心", "easy way out", "再忍忍吧", "万全之策", "防患于未然", "防微杜渐", "小霸道", "挑拨离间"]
  },
  "notes": "无图片节点。正文 26 段、1111 字符，一次读完。提问者的“如何做到绝对安全”框架（Q001）已被作者否定，本记录未把提问框架当成作者主张；作者的回答核心是“决心第一”并改写问法（P007、P021）。P026 为与本文主题无关的问答标题行混入正文末段，疑为平台相关问答链接，已在未决问题登记，未据其推断作者主张。作者提及法律、公安等求助途径但未展开，属本文未说明，未代为补全。updated_at（2021-05-15）与 published_at（2021-01-28）不同，版本差异无法判断。"
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
