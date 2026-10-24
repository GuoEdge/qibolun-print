# -*- coding: utf-8 -*-
"""批次 r001-b0113 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0113.sessions.py            # 写 out/r001-b0113.out.jsonl
  python3 records/r001-b0113.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0113"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0113.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "0fecd6e9": {
  "analysis": {
   "question_context": "提问者设问：我们处在思想终结的时代吗？没有思想的人跟其他动物有什么区别？（Q001，属提问者立场，不归给作者）。作者不回应“思想终结的时代”这一提法，而是从人的痛苦与思维不可关闭入手，直接否认“没有思想的人”存在。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "人的最大痛苦是无法真的做到只想吃饭、睡觉、交配；这种专注不是未勘破生死的凡人能有的境界。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "思维开关关不掉，靠“不想”脱离痛苦不可行，只能靠向前想通、想透求解脱。", "role": "conclusion"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "不要相信口头上只说钱权欲的人；“我这人很现实、简单”的说法是自欺或回避深谈或扮猪吃老虎，最后一种往往让说话者自己成为小丑。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "结论：没有“没有思想的人”，也不存在“像动物一样的人”，只有向自己或别人假装像动物一样的人。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的最大痛苦就在于没有办法真的做到只想吃饭、睡觉、交配。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想关掉自己的思维开关做不到，所以靠“不想”脱离痛苦不可行；作者给出的出路是靠向前想通、想透来求解脱。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "不要因为别人口头上只说钱权欲、声称“只要有这就满足”就真的相信ta们能做到这点。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“我这人很现实、简单”这类说法，不过是自欺欺人加嘴硬，或者是不信任你、不想跟你深入交流，有时候则干脆是扮猪吃老虎。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在扮猪吃老虎那种情形下，你往往会发现小丑竟是你自己。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上没有“没有思想的人”——只要ta会算工资和找零钱，ta就有思想。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上根本不存在“像动物一样的人”，只有向自己或别人假装像动物一样的人。", "evidence": ["E11", "E12"]}
   ],
   "argument_steps": [
    "先立痛苦命题：人无法真的做到只想吃饭、睡觉、交配。",
    "以反讽排除“专注到无思无欲”的可能：那是勘破生死的境界，凡人没有，有则已立地成佛。",
    "推出否定性结论：思维开关关不掉，靠“不想”脱离痛苦不可行。",
    "给出替代路径：靠向前想通、想透求解脱。",
    "转向社会观察：不要相信口头只说钱权欲的人。",
    "以反问举证：人人喊自己现实、简单，却又抢头香。",
    "给出三种解释：自欺加嘴硬／不信任、不愿深谈／扮猪吃老虎；并补一句调侃式后果。",
    "收束为对提问的回答：不存在没有思想的人，也不存在像动物一样的人，只有假装像动物的人。"
   ],
   "concept_usage": [
    {"term": "思想", "meaning": "本文中等同于会计算（算工资、找零钱）的思维能力，作者用它否认“没有思想的人”存在", "evidence": "P008", "ambiguity": "与提问者所说的“思想”（时代、价值层面的思想）是否同一所指，本文未说明"},
    {"term": "思维开关", "meaning": "人能否自主停止思考；作者断言关不掉", "evidence": "P003", "ambiguity": "比喻说法，未说明其机制或依据"},
    {"term": "抢头香", "meaning": "以民俗行为作反证，说明人的实际行为暴露了并非只想钱权欲", "evidence": "P005", "ambiguity": "具体所指场景未说明"},
    {"term": "吃老虎而扮猪", "meaning": "故意示弱示简以图利的策略", "evidence": "P006", "ambiguity": "无额外限定"}
   ],
   "examples_and_targets": [
    "“有这水平，已经立地成佛了”——以佛教成佛作夸张类比（修辞材料）",
    "“抢头香”民俗行为——作为反问的反证（修辞材料／作者论据）",
    "“吃老虎而扮猪”——俗语，指故意示弱图利（修辞材料）",
    "“小丑竟是你自己”——网络流行语，调侃听信者（修辞材料）"
   ],
   "conditions": [
    "“无法只想吃饭、睡觉、交配”是针对达到“勘破生死”境界者而言，作者说凡人没有这种专注",
    "对“口头上只说钱权欲”的判断限于“不要看着别人…就真的相信”这一告诫，未断言所有此类人都在伪装",
    "三种解释以“或者／有时候／干脆”并列，作者未指定某一个说话者属于哪一种"
   ],
   "rhetoric_and_tone": "口语化、第二人称直呼；反问（“那又为什么这么多人抢头香呢？”）；调侃与揭穿（“别开玩笑了”“小丑竟是你自己”）；结尾以三句否定式短句递进收束，语气接近训诫。",
   "unresolved_questions": [
    "提问中的“思想终结的时代”未被作者正面回应",
    "“有思想”的判据（会算工资和找零钱）与提问者所说的“思想”是否同一所指，本文未说明",
    "“抢头香”具体指向的民俗场景与人群未说明",
    "brief 与正文内容重复且被截断，未见正文之外的额外内容"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人的最大痛苦就在于，并没有办法真的做到只想吃饭、睡觉、交配。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这种专注哪是没有勘破生死的凡人能有的境界", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "想关掉自己的思维开关是做不到的，所以想要靠不想来脱离痛苦是不可行的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "只有靠向前想通、想透来求解脱。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "就真的相信ta们真能做到这点", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "那不过是自欺欺人加嘴硬", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "有时候则干脆是为了吃老虎而扮猪而已", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "你往往会发现小丑竟是你自己", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "世界上没有“没有思想的人”", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "只要ta会算工资和找零钱，ta就有思想", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "所以世界上根本不存在“像动物一样的人”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "世界上只有向自己或别人假装像动物一样的人。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学", "心理与自我认识", "社会观察"],
   "issue_candidates": ["是否存在没有思想的人", "思维能否主动关闭", "自称“现实、简单”者的真实动机", "痛苦的解脱路径"],
   "text_function_candidates": ["答疑", "驳论", "训诫", "评论"],
   "object_candidates": [],
   "working_keywords": ["无思想的人", "思维开关", "抢头香", "扮猪吃老虎", "小丑竟是你自己", "立地成佛"]
  },
  "notes": "无图片节点。正文极短（369 字符，10 段），一次读完。提问者的问题（思想终结时代／人与动物之别）与作者立场已分开记录：作者不讨论“时代”，只否认“没有思想的人”存在。"
 },
 "3d8f2f00": {
  "analysis": {
   "question_context": "提问者问：该以怎样的心态面对让人觉得浪费生命又不得不做的事情？（Q001，属提问者）。作者给出的是一个信仰式断言结构：绕不过去的事即“上帝认为值得你的生命”的事，唯一解是竭尽全力、认真做好；并立即补出“绕不过去”的严格判据与红线。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "凡是你绕不过去的事，都是上帝认为值得你生命的事；这事只有一种解——竭尽全力、认真做好。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "照此做就一定能看到为什么值，而且会看到它值得远远超过原有想象，并明白之前的自己不懂“值不值”。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "有绕不过去的事摆在面前是人生大幸事，应摆酒庆祝；不给你选择的人是活菩萨；虽然开头可能生不如死，但接住承受后，这事生死人而肉白骨。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014"], "summary": "“绕不过去”极为关键：你绕都没绕过、没有竭尽全力绕过，怎么知道绕不过去。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "这句话不是要人把头疼、乏味、无价值的东西都当天降大任正面刚；恰恰相反，鼓励先用尽一切正当手段、健康能力去绕，且不得越过不正当手段与损坏健康这两条红线。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "绕到绕不过、越绕越使敬酒变成罚酒且越来越大杯时，就可以开香槟——那是天赐的苦工，不是灾祸而是专门为你准备的祝福。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡是你绕不过去的事情，都是上帝认为值得你的生命的事情。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面对绕不过去的事只有一种解，就是竭尽全力、认真做好。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这样做之后你一定能看到为什么值，而且会看到它值得远远超过你原有的想象。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有实实在在绕不过去的事情摆在你面前是人生大幸事，应该立刻摆酒庆祝；每一个不给你选择的人都是活菩萨。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "虽然这事很可能让你望而生畏、最开始生不如死，但如果你按全心相信的态度接住了、承受了，那么事后你会看到它生死人而肉白骨。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "“绕不过去”须经检验：你绕都没绕过、没有竭尽全力绕过，凭什么说它绕不过去。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这句话并不是说只要你觉得头疼、乏味、无价值的东西，都应该当作天降大任正面刚。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰相反，这句话是在鼓励人尽一切正当的手段、一切健康的能力先去绕。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "所谓“想尽一切办法实在绕不过去”不包括不正当的手段，也不包括会损坏健康的能力；跨过这条红线绕过去不算，只能以红线以内所能达到的程度为限。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绕到绕不过、越绕越使敬酒变成罚酒且越来越大杯，就可以开香槟，因为这就是天赐的苦工；它不是灾祸，而是专门为你准备的祝福。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "以“记住了——”起句，直接给出断言：绕不过去的事是上帝认为值得你生命的事。",
    "给出唯一解法：竭尽全力、认真做好。",
    "承诺后果：能看到它为什么值，且远超原有想象。",
    "态度层加强：应视为大幸事、摆酒庆祝，不给选择的人是活菩萨。",
    "让步并设条件：开头可能望而生畏、生不如死，条件是“全心相信地接住、承受”。",
    "下定义并设检验程序：绕不过去必须先真的绕过、竭尽全力绕过。",
    "以否定句划界：不是把所有头疼乏味的事都当天降大任。",
    "给出正面主张：先用正当手段、健康能力去绕。",
    "给出红线：不正当手段、损坏健康的能力不算，只能以红线以内为限。",
    "给出识别标志与结论：绕到敬酒变大杯罚酒，即天赐的苦工与祝福。"
   ],
   "concept_usage": [
    {"term": "绕不过去", "meaning": "本文中不是主观感到困难，而是穷尽正当手段与健康能力之后仍然无法回避的事", "evidence": "P013", "ambiguity": "判据依赖当事人自述的“竭尽全力”，本文未给出外部可核验标准"},
    {"term": "上帝", "meaning": "以“上帝认为值得你的生命”表述事情的安排带有超越性意义", "evidence": "P002", "ambiguity": "是信仰表述还是比喻，本文未说明"},
    {"term": "红线", "meaning": "两条禁止线：不正当的手段、会损坏健康的能力", "evidence": "P018", "ambiguity": "“不正当”“损坏健康”的具体界限未列举"},
    {"term": "生死人而肉白骨", "meaning": "化用成语，形容事后看来这件事把死人救活、白骨生肉，即彻底挽救了自己", "evidence": "P009", "ambiguity": "修辞性表达，不是字面陈述"}
   ],
   "examples_and_targets": [
    "“上帝认为值得你的生命”——宗教语汇作断言框架（修辞材料）",
    "“每一个不给你选择的人，都是活菩萨”——佛教语汇作类比（修辞材料）",
    "“摆酒庆祝”“开香槟”——以宴饮场景作类比（修辞材料）",
    "“敬酒慢慢变成罚酒、而且还越来越大杯”——宴席比喻，用作识别“真绕不过去”的标志（作者论据）",
    "P022 的站内问题链接“「聪明人更要下笨功夫」是什么意思？”——lexical 未覆盖片段，属站内问题引用，非作者论述"
   ],
   "conditions": [
    "只适用于真正绕不过去的事，而“绕不过去”以先穷尽正当手段、健康能力去绕为前提",
    "红线条件：不包括不正当的手段，不包括会损坏健康的能力；跨红线绕过的不算",
    "态度条件：需按“全心相信”的态度接住、承受，事后才能看到其价值",
    "承受过程被承认很可能望而生畏、最开始生不如死"
   ],
   "rhetoric_and_tone": "布道式训诫语气：以“记住了——”开场，用上帝、活菩萨、祝福、开香槟等语汇，连续使用反问（“你绕都没绕过的，你怎么知道绕不过去？”），以“不但…而且…”排比递进，结尾用“不是…而是…”下判断。",
   "unresolved_questions": [
    "P022“「聪明人更要下笨功夫」是什么意思？”是站内问题链接文本，lexical 只覆盖 23 个段落节点而正文切出 22 段，属结构未覆盖片段",
    "“上帝”是信仰表述还是比喻，本文未说明",
    "“竭尽全力”缺乏可核验标准，无法判断当事人是否真的绕不过去",
    "brief 与正文重复且被截断（止于“之前的你知道个球的‘值不值”），未见正文之外的额外内容"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "凡是你绕不过去的事情，都是上帝认为值得你的生命的事情。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "而且这事只有一种解，就是竭尽全力、认真做好。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "然后你一定能看到为什么值。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "而且会看到它值得远远的超过你原有的想象", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "是一件人生大幸事，你应该立刻摆酒庆祝", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "每一个不给你选择的人，都是活菩萨。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "但你如果按照这个全心相信的态度接住了、承受了", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P013", "quote": "你绕都没绕过的，你怎么知道绕不过去？", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P014", "quote": "你没有竭尽全力的绕过，你怎么知道绕不过去？", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P015", "quote": "你都应该当作天降大任，正面刚", "relation": "contradicts"},
    {"key": "E11", "paragraph_id": "P016", "quote": "这句话在鼓励你尽一切正当的手段、一切健康的能力先去绕。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "不包括不正当的手段，不包括会损坏健康的能力。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P019", "quote": "只能以红线以内所能达到的程度为限。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P020", "quote": "你就可以开香槟了——因为这就是天赐的苦工。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "这不是一个灾祸，而是专门为你准备的祝福。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学", "心理调适", "价值论"],
   "issue_candidates": ["如何面对不得不做的“浪费生命”之事", "不可回避之事的判定标准", "全力以赴与自我损耗的边界"],
   "text_function_candidates": ["答疑", "训诫", "励志", "定义与划界"],
   "object_candidates": ["上帝", "活菩萨"],
   "working_keywords": ["绕不过去", "竭尽全力", "上帝", "活菩萨", "红线", "敬酒与罚酒", "天赐的苦工", "生死人而肉白骨"]
  },
  "notes": "无图片节点。正文 647 字符、22 段；lexical 报 23 个 paragraph 节点，P022（“「聪明人更要下笨功夫」是什么意思？”）为站内问题链接文本，属未覆盖片段，已在 unresolved_questions 登记。brief 为正文截断重复。"
 },
 "6d63051d": {
  "analysis": {
   "question_context": "提问者问：如何看待北京人社局副处长体验送外卖的一天，并表示「太委屈了，这个钱太不好挣了」？（Q001，属提问者）。作者不评论该事件与当事人本身，而是把“委屈钱和危险钱”扩展为对底层劳动处境的整体判断，并把责任指向等级体系的共同维护者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "没有特别专业知识要求的高薪（或只是平均工资）工作全部都是在挣委屈钱和危险钱，作者先写“几乎”，随即收回改为“全部”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "这既不值得意外，也不是一两个企业能改变的；能冒风险、能受委屈已是最后的护城河，自古以来没有真正改变过。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "社会分等级、有上俯视下的伦理设计、以“往上爬、别被踩”为主要驱动机制，则最底层必然只剩这两条护城河，留给底层的活命工作必然是被鄙视和回避的工作。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "认为别人更贵重、更值得“末日机票”的人，都是这个体系的共同赞助者和维护者；一边享受高贵感一边拿几个企业雇主当替罪羊，是吃贼偷的肉还欣赏贼挨打，且未意识到自己也在付代价。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "低端服务是一切其他服务的基础；这些服务由被抛弃、被侮辱的人借最后的护城河划地自守，无时无刻不在损害社会本可达到的繁荣和幸福；沉迷鄙视他人的快感即诅咒了自己的幸福，求仁得仁。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有特别专业知识要求的高薪（或者只是平均工资而已）工作，全部都是在挣委屈钱和危险钱。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种情况并不值得意外。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这不是一两个企业可以改变的。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能冒得起风险和能受得住委屈已经是最后的护城河，这一点自古以来就没有真正改变过。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "既然社会分了等级、有上俯视下的伦理设计、并把“往上爬、别被踩”设计成人的主要驱动机制，那么最底层必然只剩这两条护城河，留给底层的活命工作必然同样遭受鄙视和回避；作者称这是逻辑必然。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一个认为自己比另一些人更贵重、更值得末日机票的人，都是这个体系的共同赞助者和维护者。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一边享受高贵感和成就感，一边拎出几个企业、几个雇主做替罪羊，其实是在吃着贼偷的肉还要欣赏贼挨打。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样做的人并没有意识到自己也在为此付出代价。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "低端服务恰恰是一切其他服务的基础；这些服务不是由有理想、有尊严的人主动承担风险，而是由被抛弃、被侮辱的人借最后的护城河划地自守，实际上无时无刻不在损害社会本来可以达到的繁荣和幸福。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人太沉迷于鄙视他人的低级快感，所以无意间诅咒了自己本可以有的真正幸福，正所谓求仁得仁、无可怨也。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "由提问事件切入，给出总判断：无专业知识门槛的高薪（或平均工资）工作都在挣委屈钱和危险钱。",
    "自我修正并加强语气：不必说“几乎”，直接就是全部。",
    "排除归因：这不值得意外，也不是一两个企业能改变的。",
    "提炼底层处境：能冒风险、能受委屈是最后的护城河，且自古未变。",
    "给出机制前提：社会分等级、有上俯视下的伦理设计、以“往上爬、别被踩”为驱动。",
    "由前提推出结论：最底层必然只剩两条护城河，其活命工作必然被鄙视和回避，并称这是逻辑必然。",
    "转向责任归属：自认更贵重、更值得“末日机票”的人都是该体系的赞助者与维护者。",
    "以比喻指责找替罪羊的做法：吃贼偷的肉、欣赏贼挨打。",
    "指出代价：这样做的人没意识到自己也在付出代价。",
    "给出代价机制：低端服务是一切服务的基础，被抛弃者划地自守损害全社会可达到的繁荣与幸福。",
    "以“求仁得仁，无可怨也”收束为道德评断。"
   ],
   "concept_usage": [
    {"term": "委屈钱和危险钱", "meaning": "无专业知识门槛工作的两类报酬构成：忍受委屈与承担风险", "evidence": "P001", "ambiguity": "未给出“委屈”与“危险”的判定标准"},
    {"term": "最后的护城河", "meaning": "底层仅剩的、别人不愿越过的准入屏障（能冒险、能受委屈）", "evidence": "P004", "ambiguity": "军事比喻，未说明护城河之外是否还有别的出路"},
    {"term": "末日机票", "meaning": "危机或末日时的逃生资格，用来指人们自认更值得被优先保全", "evidence": "P008", "ambiguity": "具体所指的危机场景未说明"},
    {"term": "求仁得仁，无可怨也", "meaning": "沉迷鄙视他人者既选择了这种快感，就须接受随之而来的幸福损失", "evidence": "P013", "ambiguity": "文言化评断，未展开推论"}
   ],
   "examples_and_targets": [
    "北京人社局副处长体验送外卖并称“太委屈了，这个钱太不好挣了”——提问者引用的新闻事件，作者未直接评论该事件本身（提问者材料）",
    "“一两个企业”“几个雇主”作替罪羊——作者的反驳对象",
    "“吃着贼偷的肉，还要欣赏贼挨打”——俗语式比喻（修辞材料）",
    "“末日机票”——比喻（修辞材料）",
    "“低端服务”——作者对底层劳动的指称，未列举具体行业"
   ],
   "conditions": [
    "总判断限定于“没有特别专业知识要求的高薪（或者只是平均工资而已）工作”",
    "底层处境的推论依赖前提：社会分等级、有上俯视下的伦理设计、以“往上爬、别被踩”为主要驱动机制",
    "“末日机票”与“替罪羊”的具体所指依赖读者自行代入，本文未说明场景与国别"
   ],
   "rhetoric_and_tone": "冷峻的社会批判语气；以“说句实在话”开场，随即自我否定式的加强（“也别‘几乎’了，直接就是全部”）；讽刺比喻密集（护城河、末日机票、替罪羊、吃贼偷的肉欣赏贼挨打）；以文言化评断“求仁得仁，无可怨也”收尾，带训诫意味。",
   "unresolved_questions": [
    "作者未评论提问所指的具体事件（副处长体验送外卖）及其当事人说法，本文与该新闻的对应关系需读者自行连接",
    "“末日机票”所指的危机场景、以及谁在分配这种资格，本文未说明",
    "“低端服务”具体包括哪些行业、哪些地区，本文未列举",
    "P009“侮辱和威害穷苦人”中“威害”疑为“危害”的笔误，按原文保留，不做改写",
    "“低端服务无时无刻不在损害社会本来可以达到的繁荣和幸福”是作者的强因果断言，本文未给出论证"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "几乎全都是在挣委屈钱和危险钱。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "也别“几乎”了，直接就是全部。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这并不值得意外", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "也不是一两个企业可以改变的", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "能冒得起风险和能受得住委屈，已经是最后的护城河了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "既然将“往上爬、别被踩”设计成了人的主要驱动机制。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "那么最底层必然会只剩这两条护城河。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "这是逻辑必然的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "都是这个体系的共同赞助者和维护者", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "其实是在吃着贼偷的肉，还要欣赏贼挨打。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "并且也并没有意识到自己也在为此付出代价。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "因为那些“低端服务”恰恰正是一切其他服务的基础。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "实际上无时无刻不在损害这个社会本来可以达到的繁荣和幸福。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "所以也无意间诅咒了自己本来可以有的真正的幸福。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "正所谓求仁得仁，无可怨也。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会分层", "劳动与经济", "社会批判", "伦理"],
   "issue_candidates": ["底层劳动的委屈与风险", "等级体系的共谋结构", "把企业当替罪羊的舆论", "鄙视链的社会代价"],
   "text_function_candidates": ["评论", "社会观察", "批评", "论辩"],
   "object_candidates": ["北京人社局副处长", "外卖骑手", "企业雇主", "底层劳动者"],
   "working_keywords": ["委屈钱", "危险钱", "最后的护城河", "末日机票", "替罪羊", "低端服务", "求仁得仁"]
  },
  "notes": "无图片节点。正文 533 字符、13 段，一次读完。提问者引用的是新闻事件及其当事人说法，作者未直接评论该事件，只借“委屈钱和危险钱”作整体判断；提问者立场与作者立场已分开。P009“威害”疑为“危害”笔误，按原文保留。"
 },
 "841ef14c": {
  "analysis": {
   "question_context": "提问者问如何理解「罪在当代，功在千秋」这句话（Q001，属提问者，不归给作者）。作者不解释该语出处与其所指的具体史事，而是先判定“这话没说完整”，补出反向形态“功在当代、罪在千秋”，再展开功罪在时间中的相互构成、当代评判标准的历史局限，以及“两者必须同时被接受”的两种含义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "所引命题没说完整：除“罪在当代、功在千秋”外还有“功在当代、罪在千秋”；这并不荒谬，属最基本的认识问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "理由：好坏互为因果，因果链条环环相扣；拿掉任一好或坏的环节，其后的一切都被取消。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "好坏标准经常反转（不世之功↔万世之恶），故情绪激烈的功罪评说显然幼稚。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013"], "summary": "限定：当代评功罪的标准只出于当下局势的必然要求，人不能指望它将来不变，须接受这种历史局限性。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "功在千秋不取消“罪在当代”结论的意义；此时被定为有罪恰是将来使其被定为功在千秋的前置环节与成全，两者必须同时被接受。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "自设问“何谓同时接受”：第一义是脱离把某人某事永生永世定义为绝对邪恶、从而否定其未来一切积极意义的低级冲动；否则显露脆弱狭隘，令人丧失对其判断的信心，这类判断除自戕外无意义。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "随之而来的礼物是对待罪的理性态度：每种罪都是将来历史不可分割的一部分，在最深处都有被原谅的资格甚至必要；处置对抗与原谅接受不构成互相排除。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P029", "P030", "P031"], "summary": "第二义：将来很可能发现当代被大众认定为罪而其实功在千秋的事（作者评价大众普遍观点与政治正确离明智正确有各种距离）；但不得据此主张当代赦免或判决不合法，可出于避免实际损失而不做，并尊重世界将其定义为罪的选择。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034"], "summary": "反驳：纵使决心当烈士以身殉罪，也不得主张自己功在千秋因而现在无罪——该机制会为一切恶魔戴上天使的光环；是否因自信有功而自认无罪，是“爱牺牲的天使”与“以恶作爱的恶魔”的唯一标记。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P035", "P036", "P037", "P038"], "summary": "例证下移：这不止指改变人类的历史大事。父母不得因自信对子女未来功在千秋就认为自己做的事理应算作无罪、子女必须赦免；当下小孩对罪有扭曲的仇恨正因父母在用这个逻辑脱罪。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P039", "P040", "P041"], "summary": "收束：这种不尊重事实的执念会极大破坏子女的宽容能力，造成后半生无法以知识与技能弥补的错过；以反问“你怎么能忍心呢”与“而你现在已经知道了”逼问读者。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「罪在当代，功在千秋」这话没说完整；不但有这种事，还有「功在当代、罪在千秋」；这并不荒谬，只是最基本的认识问题。", "evidence": ["E1", "E2", "E3", "E4"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因果链条上一切环节紧紧相扣：现在喜欢的一切同时是过去一切“罪恶”的结果，现在憎恶的一切同样是过去一切“好事”的结果；拿掉任一环节，其后的一切都被取消。", "evidence": ["E5", "E6", "E7", "E8"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "好与坏的标准经常反转（今天的不世之功明天可成万世之恶），因此情绪激烈的功罪评说显然幼稚。", "evidence": ["E9", "E10"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当代评功罪的标准只出于人所处局势的必然要求，人不能也不应指望它将来不变；人活在分配给自己而非别人的年代，须接受这种历史局限性。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "功在千秋并不意味着“罪在当代”的结论没有意义：是罪就是罪，不因将来可能功在千秋而有所不同，也不因此说明现在认定它有罪是错的。", "evidence": ["E14", "E15"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此时被认定为有罪，是将来使它被认定为功在千秋的那段后续历史所必须达成的前置环节，因而是对彼时被定为有功的成全；两者必须同时被接受。", "evidence": ["E16", "E17", "E18", "E19"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“同时接受”第一义：脱离“为了将某人某事永生永世的定义为绝对邪恶而否定其在未来一切可能的积极意义”这种低级冲动；那只会显露脆弱与狭隘，令人怀疑其接受事实的能力并丧失对其判断的信心。", "evidence": ["E20", "E21"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一种罪都是将来历史的一部分、是将来所欢迎的一切不可分割的一部分，在最深处都有被原谅的资格甚至必要；处置对抗与原谅接受之间没有互相排除的关系。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "将来你很可能会发现一些在当代会被大众认定为罪、而你明白其实功在千秋的事；作者并评价大众的普遍观点和政治正确所指向的，离明智和正确有各种各样的距离。", "evidence": ["E25", "E26"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不得因看得见将来功在千秋就主张它在当代应获赦免，也不得因不认同某个法条或判决就认为其判决不合法。", "evidence": ["E27"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可以出于避免实际损失的考虑而不去做，这没什么特别可耻；尊重世界把这件事定义为罪的选择没有问题，不需额外负罪感，也不见得要去干预世界自己该有的觉醒步调。", "evidence": ["E28"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若真决心当烈士、以身殉罪去拯救人类，也不应主张自己会“功在千秋”因而现在就该无罪：靠自认为功在千秋而免除遵守现行法律和社会共识的义务，这种机制可以为一切恶魔都戴上天使的光环。", "evidence": ["E29", "E30"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是否因为自信有功就自认无罪，是区分“爱牺牲的天使”与“以恶作爱的恶魔”的唯一标记。", "evidence": ["E31"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不只指能改变人类的历史大事：父母不要因为自信对子女的未来功在千秋，就认为自己做的事都理应被算作无罪、子女必须赦免；当下小孩对罪有扭曲的仇恨，正因父母在用这个逻辑脱罪。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种不尊重事实的执念会极大破坏子女的宽容能力，使其后半生有大量无法用知识与技能弥补的错过，是父母不会希望子女染上的扭曲。", "evidence": ["E35"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问收束：你如果知道了，怎么能忍心；并以“而你现在已经知道了”暗示读者已无不知情的余地（作者未给出明确的行动指令）。", "evidence": ["E36", "E37"]},
    {"claim_id": "C017", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的立场（未指明持有者）：为了将某人某事永生永世定义为绝对邪恶，而否定其在未来一切可能的积极意义。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "先判定提问所引命题“没说完整”，补出反向形态“功在当代、罪在千秋”，并否认其荒谬（P001–P004）。",
    "以好坏互为因果、链条相扣作理由：抽掉任一环节，其后一切被取消（P005–P008）。",
    "以好坏标准会反转（不世之功↔万世之恶）加强，推出情绪激烈的功罪评说幼稚（P009–P010）。",
    "限定评判尺度：评功罪标准出于当代局势的必然要求，人须接受历史局限性（P011–P013）。",
    "让步转折：功在千秋不意味“罪在当代”结论无意义，现在认定有罪不为将来可能之功所动（P014–P015）。",
    "推进：此刻被定为罪是将来被定为功的前置环节，故是对彼时之功的成全（P016–P018）。",
    "提出总要求“两者必须同时被接受”，并自设问“何谓同时接受”（P019–P020）。",
    "第一义：脱离绝对邪恶化、否定未来积极意义的低级冲动，并指出其代价（P021–P024）。",
    "给出礼物：对待罪的理性态度——罪是将来历史不可分割的一部分，有被原谅资格甚至必要，处置与原谅不互斥（P025–P028）。",
    "第二义：承认可能存在当代被大众判罪而功在千秋之事，但不得据此主张当代赦免；可选不参与、须尊重世界的选择（P029–P031）。",
    "反驳“自认功在千秋即当代无罪”：会为恶魔戴上天使光环；以是否自认无罪作天使／恶魔的唯一标记（P032–P034）。",
    "例证下移：父母对子女同样适用，并归因当下小孩“对罪有如此扭曲的仇恨”（P035–P038）。",
    "以子女宽容能力受损的后果收束，并以反问与“你现在已经知道了”逼问读者（P039–P041）。"
   ],
   "concept_usage": [
    {"term": "罪在当代，功在千秋／功在当代，罪在千秋", "meaning": "功与罪在时间上的错位共存；作者认为原说法不完整，两种方向都存在。", "evidence": "P001–P003", "ambiguity": "作者未指明任何具体史事或人物，全用抽象表述"},
    {"term": "因果链条", "meaning": "历史环节紧密相扣，任一好或坏环节被拿掉，其后一切都被取消。", "evidence": "P007–P008", "ambiguity": "“好好坏好好，坏好坏坏好”为口诀式表述，未给判定标准"},
    {"term": "同时接受", "meaning": "作者定义的两义：一是不把某人某事绝对邪恶化而否定其未来积极意义；二是不因看得见功在千秋而主张当代赦免。", "evidence": "P019–P021、P029–P030", "ambiguity": "“必须同时被接受”是否为规范要求还是认识论要求，作者未明说"},
    {"term": "历史局限性", "meaning": "人活在分配给自己而非别人的年代，评功罪标准出于当下局势的必然要求。", "evidence": "P011、P013", "ambiguity": "无"},
    {"term": "功在千秋", "meaning": "使当下之罪在将来被认定为功的后续历史；不是当代无罪的依据。", "evidence": "P015–P016", "ambiguity": "由谁在何时认定“功”，本文未说明"},
    {"term": "爱牺牲的天使／以恶作爱的恶魔", "meaning": "以是否因自信有功而自认无罪作为两者的唯一区分标记。", "evidence": "P034", "ambiguity": "宗教语汇，作者未说明是否为比喻"},
    {"term": "大众的普遍观点和政治正确", "meaning": "作者认为其离明智和正确有各种各样的距离，遍及所有细节。", "evidence": "P029", "ambiguity": "具体所指范围、国别、时期均未说明"},
    {"term": "自戕", "meaning": "指这类愚蠢的价值判断除了伤害自身之外没有意义。", "evidence": "P024", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "提问者引语「罪在当代，功在千秋」——讨论对象（引用，属提问者 Q001，作者只作补全与解释）",
    "“江山永固的不世之功”变为“思想禁锢的万世之恶”——标准反转的举例（作者论据／修辞材料，P009）",
    "父母与子女——“举个几乎人人都会遇到的例子”（作者自述为例证，P036–P038）",
    "“大众的普遍观点和政治正确”——被作者评价并批评的对象（P029）",
    "“某个法条或者判决”——不认同不等于不合法的举例（P030）",
    "“烈士”“以身殉罪去拯救人类于人类自己无知的危险”——假设情形（P032）",
    "“爱牺牲的天使”“以恶作爱的恶魔”“戴上天使的光环”——宗教式比喻（修辞材料，P033–P034）",
    "“小孩子对罪有如此扭曲的仇恨”——作者举的社会现象并归因于父母脱罪（P038）"
   ],
   "conditions": [
    "论断针对“你所在的这个局势”的评功罪标准，时点限定在当代（P011、P013）",
    "反事实条件句：如果现在将其视为罪的历史不发生，则后来使它功在千秋的后续历史也不会发生（P017）",
    "允许出于避免实际损失而不去做，条件是尊重世界把此事定义为罪的选择、不主动干预世界自己该有的觉醒步调（P031）",
    "若决心当烈士（以身殉罪），仍不得主张自己功在千秋而自认无罪（P032–P033）",
    "适用面扩至日常：不限于改变人类的历史大事，也适用于父母对子女（P035–P037）",
    "作者用“很可能”而非必然来描述将来发现“当代判罪而其实功在千秋”的事（P029）"
   ],
   "rhetoric_and_tone": "论说与训诫混合；大量让步—转折结构（“你也不必愤恨啥”“恰恰相反”“而另一方面”“不过”）；反问句连用（P023、P024、P040）；对称短句与口诀（“好好坏好好，坏好坏坏好”）；以“天使／恶魔”对立收束论证；结尾用第二人称“你如果知道了，你怎么能忍心呢？”逼问。",
   "unresolved_questions": [
    "提问句所指向的具体历史事例（哪件事被称作“罪在当代，功在千秋”）本文未指明，作者全用抽象表述",
    "“将来”“千秋”的时间尺度、以及由谁判定“功在千秋”，本文未说明",
    "P038“现在有这么多小孩子对罪有如此扭曲的仇恨，正是因为父母们在用这个逻辑脱罪”为作者的强因果断言，本文未给证据，属待外部核查",
    "“大众的普遍观点和政治正确”具体所指、以及“世界自己该有的觉醒步调”的含义与机制，本文未说明",
    "P029“其实你明白功在千秋”中的判定依据（“你”凭什么明白）本文未说明",
    "作者对“爱牺牲的天使／以恶作爱的恶魔”的区分是否为宗教语汇的比喻，本文未标明",
    "渲染包中 brief 被截断（结尾为“过去一切‘罪恶’的结”），brief 仅作导航，未用于支持主张"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这话没说完整。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不但有“罪在当代、功在千秋”这种事，", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "还有“功在当代、罪在千秋”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这没什么荒谬的，只不过是最基本的认识问题。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "它同时也是一切“罪恶”的结果。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "也同样是一切“好事”的结果。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "因果链条上的一切环节是紧紧相扣的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "你拿掉一个坏，从它之后的一切也都被取消了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "关于什么是好、什么是坏的标准也经常发生反转。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "那些情绪激烈的功罪评说才是一种显然的幼稚。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "只是出于你所在的这个局势的必然要求。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "以至于你现在认定为罪的，将来的人也必须一直认定为罪。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "你需要接受这种历史局限性。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "是罪就是罪，这并不因为任何“功在千秋”的可能性而有所不同。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "就意味着人在现在认定它有罪就是错的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "是将来使得它被认定为功在千秋的那段后续历史要发生所必须达成的前置环节。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "则后来使得它功在千秋的后续历史也就同样不会发生。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "是对彼时被定为有功的成全。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "两者必须同时被接受。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "为了将某人某事永生永世的定义为绝对邪恶而否定其在未来一切可能的积极意义", "relation": "contradicts"},
    {"key": "E21", "paragraph_id": "P022", "quote": "那只是显露出了自己的脆弱与狭隘", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "它们在最深处都有被原谅的资格。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "甚至是必要。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "这两者之间并没有“要处置就不能原谅，要原谅就不能处置”的排除关系。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P029", "quote": "将来你很可能会发现一些在当代会被大众认定为罪", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P029", "quote": "离明智和正确有着各种各样的距离，遍及所有的细节之中。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P030", "quote": "不要因为你看得见将来功在千秋，就主张它在当代应该得到赦免", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P031", "quote": "你去尊重这个选择，是没有什么问题的", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P032", "quote": "你也不要去主张自己会“功在千秋”，于是现在就应该是无罪的。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P033", "quote": "这种机制可以为一切恶魔都戴上天使的光环。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P034", "quote": "是否因为自信有功就自认无罪", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P035", "quote": "不要以为这只是指能改变人类的历史大事，而与你无关。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P037", "quote": "不要因为自己自信对子女的未来功在千秋，就认为自己做的事都理应被算作无罪", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P038", "quote": "正是因为父母们在用这个逻辑脱罪。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P039", "quote": "会因为极大的破坏子女的宽容能力而使得ta们的后半生有大量无法被ta们的所谓知识与技能弥补的错过。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P040", "quote": "你如果知道了，你怎么能忍心呢？", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P041", "quote": "而你现在已经知道了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史哲学", "伦理学", "政治哲学", "社会批判"],
   "issue_candidates": ["功罪的历史评价", "历史局限性与评判尺度变迁", "罪的赦免与原谅", "以功自认无罪的机制", "父母对子女的脱罪逻辑"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "评论"],
   "object_candidates": ["大众", "政治正确", "父母与子女", "烈士"],
   "working_keywords": ["罪在当代，功在千秋", "功在当代，罪在千秋", "因果链条", "同时接受", "历史局限性", "爱牺牲的天使", "以恶作爱的恶魔", "觉醒步调"]
  },
  "notes": "无图片节点。正文 1693 字符、41 段，一次读完（P001–P041）。提问者只引用一句成语式说法，作者的论证对象是抽象的历史功罪评说，未点名任何人物、朝代或事件；提问者立场与作者立场已分开。作者对“大众的普遍观点和政治正确”的评价为作者的概括判断，具体所指属待外部核查。P021、P023、P024、P040 为反问句，语气已按 questioned 保留（C016）。"
 },
 "065db95a": {
  "analysis": {
   "question_context": "提问者给出两种处境化的标签（右转被称作“奴隶却为奴隶主说话，不知道屁股在哪”，左转是“杀了地主之后的屠刀就砍向你”），问如何选择（Q001，属提问者，不归给作者）。作者不回应左右标签与“如何选择”，也不评论该问题本身，而是给出“拥有知识的人”的言论责任：在仇恨的一方面前为另一方说话，并划出技巧与责任的界限与免责条件。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "拥有知识的人有一个天赋的责任：不畏艰险、不避讥谗地在仇恨的一方面前为另一方说话；讲究方式、场合、分寸属技巧问题，但不能“有技巧”到实际放弃这个责任。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "限定：人可以对立，因为有些分歧只能天裁；但所有人都有责任防止人因谎言和误解而对立。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "理由：这件事若没人做，人类就会毁灭，连同你所爱的一切；而你是唯一真正能做的人——知真相者与因误解而仇恨者之间存在不对称。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "免责条件：如果人们知道了真相仍然选择对立，那就对立去吧，让该赢的赢、让无法避免的损失发生。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "归责与二择一：因你明知其真相的谎言和你可以阻止的误解而生的仇恨所流的血、所燃的火，都有你闭口不言的一份；要么不追求真知，要么不闭口不言。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013"], "summary": "以连串反问与调侃收束：只有你们能做，再不做还指望谁；学了知识、知道真相还妄想讨人喜欢——“美死你啊”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拥有知识的人有一个天赋的责任，就是要不畏艰险、不避讥谗地在仇恨的一方面前为另一方说话。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "说话的方式、场合和分寸可以讲究，但那只是技巧问题；不能“有技巧”到实际放弃这个责任。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人可以对立，因为有一些分歧只能天裁；但所有人都有责任防止人因为谎言和误解而对立。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "这件事如果没人做，人类就会毁灭，连同你所爱的一切在内。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你是唯一真正能做这件事的人；你知道真相而那些因误解而仇恨的人不知道，故不能指望不知道的人（原文以反问表达）。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果人们知道了真相仍然选择对立，那么就对立去吧，让该赢的赢、让无法避免的损失发生。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切因为你明知其真相的谎言和你可阻止的误解而生的仇恨所流的血、所燃的火，都有你闭口不言的一份。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "二择一：要么你不要追求真知，要么你不要闭口不言。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问与口语调侃否定“学了知识、知道真相还能讨人喜欢”的期待（“你还妄想讨人喜欢？”“美死你啊。”）。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者说法（Q001）：右转被称作“奴隶却为奴隶主说话，不知道屁股在哪”，左转是“杀了地主之后的屠刀就砍向你”，并问如何选择。", "evidence": []}
   ],
   "argument_steps": [
    "直接给出命题：拥有知识者有天赋责任，在仇恨的一方面前为另一方说话（P001）。",
    "划出技巧与责任的界限：方式、场合、分寸可讲，但不能有技巧到实际放弃责任（P002–P003）。",
    "让步式限定：人可以对立（有些分歧只能天裁），但所有人有责任防止因谎言和误解而对立（P004–P005）。",
    "给出理由：无人做则人类毁灭并连同你所爱的一切，而你是唯一真正能做的人（P006）。",
    "补足理由：知真相者与因误解而仇恨者的知识不对称，不能指望不知道的人（P007，反问）。",
    "给出免责条件：知真相后仍选择对立者，其对立与损失不再由知者负责（P008）。",
    "给出归责条款：因你明知真相的谎言与你可阻止的误解而生的流血与火，有你闭口不言的一份（P009）。",
    "以二择一收束义务：不追求真知，或不闭口不言（P010）。",
    "以连续反问与调侃施压：只有你们能做；别妄想讨人喜欢（P011–P013）。"
   ],
   "concept_usage": [
    {"term": "天赋的责任", "meaning": "拥有知识者不可推卸的说话义务，不因艰险与讥谗而免除。", "evidence": "P001", "ambiguity": "“天赋”是宗教式还是自然法式表述，本文未说明"},
    {"term": "仇恨的一方面前为另一方说话", "meaning": "在两方彼此仇恨的情形下，向其中一方为另一方代言。", "evidence": "P001", "ambiguity": "“一方”“另一方”具体指谁、何种关系，本文未说明"},
    {"term": "技巧问题", "meaning": "说话方式、场合、分寸属技巧层面，以不实际放弃责任为限。", "evidence": "P002–P003", "ambiguity": "“实际放弃”的判定标准未说明"},
    {"term": "天裁", "meaning": "有些分歧只能由天裁决，故人之间的对立可以存在。", "evidence": "P004", "ambiguity": "“天裁”含义未展开"},
    {"term": "真相", "meaning": "知者知悉、而因误解而仇恨者不知的信息。", "evidence": "P007", "ambiguity": "真相的核验方式未说明"},
    {"term": "真知", "meaning": "与“闭口不言”构成二择一的选项。", "evidence": "P010", "ambiguity": "无"},
    {"term": "闭口不言", "meaning": "知者的不作为，被计入仇恨所流之血与所燃之火的责任。", "evidence": "P009–P010", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "提问者转述的两种标签（右转“奴隶却为奴隶主说话，不知道屁股在哪”；左转“杀了地主之后的屠刀就砍向你”）——提问者说法（Q001），作者正文未出现“左”“右”“奴隶”“地主”等字样，未回应",
    "“仇恨的一方”“另一方”——作者论证中未指名的两方（未给出任何例子）",
    "“人类就会毁灭，连同你所爱的一切在内”——作者的最坏后果设想（警示性修辞，P006）",
    "“天裁”——宿命／宗教式语汇（修辞材料，P004）",
    "“让该赢的赢”——未指明谁赢、以什么为赢（P008）",
    "“美死你啊”——口语反讽（修辞材料，P013）"
   ],
   "conditions": [
    "责任主体限定为“拥有知识的人”／“知道真相”者（P001、P006–P007）",
    "义务以“不畏艰险、不避讥谗”为前提，作者承认存在艰险与讥谗（P001）",
    "说话方式、场合、分寸可讲，但不能“有技巧”到实际放弃责任（P002–P003）",
    "“人可以对立”的条件：有一些分歧只能天裁（P004）",
    "免责条件：人们知道了真相仍然选择对立（P008）",
    "归责条件：仇恨须源于“你明知其真相的谎言”和“你可以阻止的误解”（P009）",
    "二择一结构：不追求真知，或不闭口不言（P010）"
   ],
   "rhetoric_and_tone": "格言式短段与直接断言；第二人称直呼，人称在“你”（P006–P007）与“你们”（P011）之间移动；连续反问（P007、P011、P012）；庄重语汇（“天赋的责任”“天裁”）与口语反讽（“美死你啊”）形成落差；结尾不作解释，以调侃收束。",
   "unresolved_questions": [
    "提问中的“右转／左转”两种标签与“如何选择”，作者未直接回应；正文未出现“左”“右”字样",
    "“仇恨的一方”与“另一方”具体指谁（阶层、阵营或何种关系）本文未说明",
    "“天裁”的确切含义（天意、历史还是命运裁决）未说明",
    "“你”（P006“你是唯一真正能做这件事的人”）与“你们”（P011）所指不一，是个体还是知者群体，本文未统一",
    "“真相”“谎言”“误解”的具体所指与核验方式未说明，属待外部核查",
    "“人类就会毁灭”是字面预言还是修辞夸张，本文未说明",
    "question 字段（Q001）在机械生成的 paragraphs 中没有 Pnnn 定位，提问者说法只记录于 question_context 与 examples_and_targets，未计入 evidence",
    "渲染包中 brief 末尾截断（“因为这”），brief 仅作导航，未用于支持任何主张"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "拥有知识的人有一个天赋的责任，就是要不畏艰险、不避讥谗的在仇恨的一方面前为另一方说话。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你可以讲究说话的方式、场合和分寸，但那是技巧问题。", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你不能“有技巧”到实际放弃这个责任。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "人可以对立，因为有一些分歧只能天裁。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P005", "quote": "但所有人都有责任去防止人因为谎言和误解而对立。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "因为这件事如果没人做，人类就会毁灭，连同你所爱的一切在内", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "而你是唯一真正能做这件事的人。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "你知道真相，那些因为误解而仇恨的人不知道。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "如果人们知道了真相仍然选择对立，那么就对立去吧。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P008", "quote": "让该赢的赢，让无法避免的损失发生。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "都有你闭口不言的一份。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "要么你不要追求真知，要么你不要闭口不言。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "学了知识，知道真相，你还妄想讨人喜欢？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "美死你啊。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["知识伦理", "政治哲学", "社会批判", "言论与传播"],
   "issue_candidates": ["知识者的言论责任", "对立与仇恨中的立场选择", "谎言与误解的归责", "技巧与责任的边界", "沉默的责任"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "箴言"],
   "object_candidates": ["拥有知识的人", "因误解而仇恨的人", "提问者（未具名）"],
   "working_keywords": ["天赋的责任", "仇恨的一方", "天裁", "闭口不言", "真知", "谎言和误解", "美死你啊"]
  },
  "notes": "无图片节点。正文极短（375 字符，13 段），一次读完（P001–P013）。提问者给出的是左右两种标签化说法与“如何选择”，作者未回应左右之分，只给出知识者的言论责任及免责条件；提问者立场与作者立场已分开。作者未举任何具体事例、未点名任何人物或机构。“美死你啊”按原文保留为口语反讽，未转写为价值判断。"
 },
 "b79a675e": {
  "analysis": {
   "question_context": "提问者问“女生如何提高自己的身价？”（Q001，属提问者，不归给作者）。作者不接受该提问框架：把努力方向改写为“如何不降低自己的身价”，以“你们是无价的”为前提，把关系处理为“赠送”而非“出售”，并把后半篇的问题转为赠送如何可能被对方接受、以及送与卖的性质不可混同。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "改写提问前提：女生应主要把努力放在如何不降低自己的身价上，因为你们是无价的；无价的东西只能赠送，拿来卖没人买得起。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "告诫：不要因为舍不得赠送、又没人买得起，就“降价出售”。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "赠送的秘诀与撤回：送对人，赠送之后你还是完整地属于自己；送错了、发现对方受不起就拿回来，也不必怪对方，这是学习的过程。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "重申不降价并给出理由：无论卖出什么价，卖身为奴是没有划算可言的。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "定义“赠送”：不是把自己这个人送人，而是送人一段时间、一段好意、一段生命；送了一小时并不表示下一小时还会送。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "逐次判定规则：对方值得就一小时一小时送下去，不值得就停止；卖东西的人在客户面前矮三分，送东西的人没有这个必要。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "提出真正要解决的问题：并不是你肯送就一定有人上赶着要；你无法保证对方觉得受益而非受损（反问），毕竟免费的亏再免费也没人要吃。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021", "P022"], "summary": "使用与性质：明媚皓齿、巧笑嫣然、性感销魂不是不要，而是不要放错地方、做错性质；送是送、卖是卖，不要把送做成卖，也不容人把你的送当成卖。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "排比否定：对方再帅、再多金、再温柔、再“有前途”、家世再“好”，都不能容，并逐项给出否定理由。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P029"], "summary": "限定收束：不是教你不要宽容，而是这没有宽容的意义。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女生应该主要把努力放在如何不降低自己的身价上（对提问“如何提高身价”的框架改写）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为你们是无价的；无价的东西只能赠送，拿来卖是没人买得起的。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要因为舍不得赠送、又没人买得起，就“降价出售”。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赠送的主要秘诀是送对人；赠送之后你还是完整地属于你自己；送错了、发现对方受不起，那就拿回来。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "也不必怪对方为什么受不起，这就是一个学习的过程。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论卖出什么价，卖身为奴是没有划算可言的。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓的赠送不是指把自己这个人送人了，而是送人一段时间、一段好意、一段生命；这不表示下一小时就一定还会送。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方值得，就一小时一小时地送下去；对方不值得，那就停止。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "卖东西的人在客户面前当然矮三分，送东西的人可没这个必要。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "并不是你肯送，就一定有人上赶着求着要的。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问指出：你无法保证对方一定会觉得这是受益而非受损；毕竟免费的亏再免费，也没人要吃。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那些明媚皓齿、巧笑嫣然、性感销魂，不是不要，而是不要放错地方、做错性质。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "送是送，卖是卖，不要把送做成了卖；也不要容人把你的送当成卖，一个字、一个标点符号也不要允许。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "对方再帅、再多金、再温柔、再“有前途”、家世再“好”，都不能容；作者并逐项否定这些条件（帅不稀罕、多金配此心态是坏消息、温柔不会缺、分不清卖与送的人没有前途、有这种心态的人家世不好）。", "evidence": ["E21", "E22", "E23", "E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "这不是教你不要宽容，而是这没有宽容的意义（作者的自我限定）。", "evidence": ["E27"]},
    {"claim_id": "C016", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者说法（Q001）：女生如何提高自己的身价？作者将其改写为“如何不降低自己的身价”。", "evidence": []}
   ],
   "argument_steps": [
    "改写提问框架：把“提高身价”改为“不降低身价”（P001）。",
    "给出理由：你们是无价的；无价之物只能赠送，出售无人买得起（P002–P003）。",
    "由此告诫不要因舍不得赠送又无人买得起而降价出售（P004）。",
    "给出赠送的秘诀与撤回机制：送对人、赠送后仍完整属于自己；送错可取回且不怪对方，视为学习过程（P005–P007）。",
    "重申禁令并给出理由：无论什么价，卖身为奴都不划算（P008–P009）。",
    "界定“赠送”的内容：送的是时间、好意与生命，不是整个人；一小时不等于下一小时（P010–P013）。",
    "给出逐次判定规则：值得就继续一小时一小时送，不值得就停止（P014–P015）。",
    "以买卖双方姿态对比加强：卖者矮三分，送者无此必要（P016）。",
    "转入反向问题：你肯送不等于有人要，无法保证对方视为受益而非受损（P017–P019，反问）。",
    "落到使用方式：外貌与性魅力不是不要，而是不要放错地方、做错性质；送与卖不可混同，也不容对方误认（P020–P022）。",
    "排比否定对方的各项条件（帅、多金、温柔、有前途、家世）不构成破例理由（P023–P028）。",
    "以限定句收束：不是教你不宽容，而是此处宽容没有意义（P029）。"
   ],
   "concept_usage": [
    {"term": "身价", "meaning": "提问者问如何提高；作者改写为“不降低”，未给出衡量单位。", "evidence": "P001", "ambiguity": "所指（婚恋价值、社会评价或自我价值）本文未界定"},
    {"term": "无价", "meaning": "立论前提：无价之物不能进入买卖，只能赠送。", "evidence": "P002–P003", "ambiguity": "是修辞还是本体论判断，本文未说明"},
    {"term": "赠送", "meaning": "作者定义的相处方式：送出时间、好意与生命，可逐次进行与撤回，赠送后仍完整属于自己。", "evidence": "P005、P010–P013", "ambiguity": "与“好意”的界限未展开"},
    {"term": "降价出售", "meaning": "因舍不得赠送又无人买得起而折价处置，被作者禁止。", "evidence": "P004、P008", "ambiguity": "无"},
    {"term": "卖身为奴", "meaning": "把关系做成“卖”的性质时所付的代价，作者认为无论何价都不划算。", "evidence": "P009", "ambiguity": "比喻，作者未说明其具体所指"},
    {"term": "放错地方、做错性质", "meaning": "外貌与性魅力的使用须区分场合与性质。", "evidence": "P020", "ambiguity": "“对的地方／性质”未定义"},
    {"term": "不要把送做成了卖", "meaning": "送与卖的性质区分须自己维持，并拒绝对方的误认。", "evidence": "P021–P022", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "提问者设问“女生如何提高自己的身价”——被作者改写为“不降低身价”（提问者说法 Q001）",
    "“明媚皓齿、巧笑嫣然、性感销魂”——作者举的外貌与性魅力资源（修辞材料，P020）",
    "追求者条件：帅、多金、温柔、“有前途”、家世“好”——被作者逐项否定为不可让步的理由（反驳对象／修辞材料，P023–P028）",
    "“卖东西的人在客户面前当然矮三分”——商业场景类比（类比，P016）",
    "“卖身为奴”——比喻（修辞材料，P009）",
    "“免费的亏再免费，也没人要吃”——俗语式论断（P019）"
   ],
   "conditions": [
    "对象限定为“女生”，作者以第二人称“你们”称呼（P001–P002）",
    "立论前提限定为“无价”，故以赠送而非交易为框架（P002–P003）",
    "赠送可逐次、可撤回：赠送之后仍完整属于自己；送错且对方受不起时可拿回（P005–P006）",
    "对方条件（帅、多金、温柔、有前途、家世）不构成容许被当成卖的例外（P023）",
    "作者自承的条件性困难：赠送者无法保证对方认为受益而非受损（P017–P019）",
    "宽容的适用边界：不是不要宽容，而是此处没有宽容的意义（P029）"
   ],
   "rhetoric_and_tone": "第二人称直接劝告，语气笃定；格言短句与破折号定义句；句式反复（P004 与 P008 近似重复，后者把“赠送”改作“送”）；P024–P028 五项排比逐条否定；以限定句“不是教你不要宽容”收束，兼有训诫与安抚。",
   "unresolved_questions": [
    "“身价”的所指（婚恋价值、社会评价或自我价值）本文未界定，作者直接改写为“不降低”",
    "“无价”是修辞还是本体论判断，本文未说明",
    "“送对人”与“对方受不起”的判据、“对方值得／不值得”由谁按什么标准判定，本文未说明",
    "提问所问的“提高身价”路径，作者未正面回答",
    "P004 作“买的起”、P008 作“买得起”，用字不一致，按原文保留",
    "“一个字、一个标点符号也不要允许”是字面要求还是强调，本文未说明",
    "P027“分不清别人是卖还是送的人没有前途”、P028“有这种心态的人，家世不好”为作者的断言，本文未给依据，属待外部核查",
    "question 字段（Q001）在机械生成的 paragraphs 中没有 Pnnn 定位，提问者说法只记录于 question_context 与 examples_and_targets，未计入 evidence",
    "渲染包中 brief 末尾截断（“也”），brief 仅作导航"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "女生应该主要把努力放在如何不降低自己的身价上。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为你们是无价的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "无价的东西只能赠送，拿来卖是没人买得起的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "就“降价出售”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "赠送的主要秘诀在于——送对人，赠送之后你还是完整的属于你自己。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "送错了，发现对方受不起，那就拿回来。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这就是一个学习的过程。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "因为无论卖出什么价，卖身为奴是没有划算可言的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "所谓的赠送，不是指把自己这个人送人了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "说的是送人一段时间，一段好意，一段生命。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "这不表示下一小时就一定还会送。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "对方值得，那就一小时一小时的送下去。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "对方不值得，那就停止。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "卖东西的人在客户面前当然矮三分，送东西的人可没这必要。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "并不是你肯送，就一定有人上赶着求着要的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "你用什么来保证对方一定会觉得这是受益而非受损了呢？", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P019", "quote": "毕竟，免费的亏再免费，也没人要吃。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "不是不要，而是不要放错地方、做错性质。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "送是送，卖是卖，不要把送做成了卖。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "一个字、一个标点符号也不要允许。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "对方再帅、再多金、再温柔、再“有前途”、家世再“好”，都不能容。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "帅，不稀罕；", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "多金，配上这种心态不是好消息而是坏消息；", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "温柔，你不会缺对你温柔的人；", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "分不清别人是卖还是送的人没有前途；", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P028", "quote": "有这种心态的人，家世不好。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P029", "quote": "不是教你不要宽容，而是这没有宽容的意义。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋与两性关系", "伦理", "人际交往建议"],
   "issue_candidates": ["女性自我价值的维护", "赠送与交易的性质区分", "关系中的边界与撤回", "择偶条件的否定"],
   "text_function_candidates": ["答疑", "经验建议", "训诫", "评论"],
   "object_candidates": ["女生", "追求者（帅／多金／温柔／“有前途”／家世“好”者）"],
   "working_keywords": ["身价", "无价", "赠送", "降价出售", "卖身为奴", "送对人", "送是送，卖是卖", "放错地方、做错性质"]
  },
  "notes": "无图片节点。正文 657 字符、29 段，一次读完（P001–P029）。提问者问“如何提高身价”，作者改写为“不降低身价”并以“无价／赠送”重构问题，属对提问框架的改动，已与提问者立场分开。P018 为反问句，语气按 questioned 保留（C011）。作者未举任何真实人物或事件。"
 },
 "22d9a942": {
  "analysis": {
   "question_context": "提问者就一则具体事件发问：女记者私下找理想汽车男员工打听机密信息、男员工回应涉侮辱女性、女记者要求企业公开道歉（Q001，属提问者，不归给作者）。作者不评论当事双方与事件是非，先列三条原则（人格侮辱不可容忍、忠诚应嘉奖、保密意识应嘉奖），指出企业缺少媒体应对训练与规章制度，随后给出七条“可以考虑的”处置方式。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "三条原则：任何人的人格受侮辱不可容忍（这没有疑问）；忠诚应该嘉奖；保密意识应该嘉奖。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005"], "summary": "问题诊断：作为敏感企业，员工没有全员受到应对媒体的恰当训练，也没有既定的规章制度限制。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "处置方式(1)(2)：对内通报嘉奖该员工的保密意识；对内公告将组织全员媒体沟通规范训练，在此之前禁止员工向任何媒体、自媒体泄露机密并列出清单。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "处置方式(3)：主管媒体沟通、公共关系的最高负责人对内公开检讨，承认工作失误给员工带来的困扰；公开信给配合度高的媒体作独家优先报道（原文并注“是之前这家的直接竞争对手”）。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "处置方式(4)：企业内外同时公开声明，就内部疏于尊重女性的意识培养对公众道歉；企业文化负责人与董事长同台鞠躬；向协助女性权益的法律援助组织常规年度捐赠。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "处置方式(5)：法务部对外公告追查一切非正式渠道刺探内部消息的行为，查有实据则按商业间谍、内幕交易、意图操纵股价和扰乱金融市场举报报案。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P012"], "summary": "处置方式(6)：培训时交代员工在主动通报法务部门的前提下引诱对方付费、形成事实证据；并称争取半年内砍掉几个人头挂在大门上当装饰。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P013"], "summary": "处置方式(7)：该员工在员工大会上检讨，事后放假“进行心理康复”，后续可以选择转岗到合规部门。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何人的人格受侮辱当然是不能容忍的，这没有疑问。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "忠诚应该嘉奖，保密意识也应该嘉奖。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题出在：作为敏感企业，员工没有全员受到应对媒体的恰当训练，也没有既定的规章制度限制。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(1)(2)：对内通报嘉奖该员工的保密意识；对内公告即将组织全员媒体沟通规范训练，在此之前禁止任何员工对任何媒体、自媒体泄露企业机密信息并列出清单。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(3)：主管媒体沟通、公共关系的最高负责人对内公开检讨、承认工作失误给员工带来的困扰；该公开信透露给配合度高的媒体作为独家优先报道。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(4)：企业对内对外同时公开声明，就内部疏于对尊重女性的意识培养对公众道歉；企业文化负责人和董事长同台鞠躬致歉；并向协助女性权益的法律援助组织实行常规性年度捐赠，成为其主要捐助者之一。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(5)：法务部对外公告将追查一切不通过企业正式消息发布渠道刺探内部消息的行为；如果查有实据，将按商业间谍、内幕交易、意图操纵股价和扰乱金融市场向相关部门举报和报案。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(6)：对内培训时交代员工在主动通报法务部门的前提下引诱对方付费、形成事实证据；并称争取半年内砍掉几个人头挂在大门上当装饰。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "建议处置方式(7)：该员工要在员工大会上检讨，事后放假“进行心理康复”，后续可以选择转岗到合规部门。", "evidence": ["E16"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者陈述的事件（Q001）：女记者私下向理想汽车男员工打听机密信息、男员工回应涉侮辱女性、女记者要求企业公开道歉；作者正文未点名企业与当事人。", "evidence": []}
   ],
   "argument_steps": [
    "先列三条无争议原则：人格侮辱不可容忍、忠诚应嘉奖、保密意识应嘉奖（P001–P004）。",
    "诊断问题所在：敏感企业缺少全员媒体应对训练与既定规章制度（P005）。",
    "声明以下只是“一种可以考虑的”处置方式（P006）。",
    "内部处置：通报嘉奖保密意识；公告将组织全员媒体沟通规范训练，并先行禁止泄密、列出清单（P007–P008）。",
    "公关负责人对内公开检讨，并把公开信给配合度高的媒体作独家（P009）。",
    "对外道歉（限于疏于尊重女性的意识培养）与向女性权益法律援助组织捐赠（P010）。",
    "法务对外公告追查刺探行为，查实则按商业间谍等罪名举报报案（P011）。",
    "取证手段：在主动通报法务的前提下引诱对方付费以形成事实证据，并附暴力化措辞（P012）。",
    "收尾安排该员工：大会检讨、放假“进行心理康复”、可选转岗合规部门（P013）。"
   ],
   "concept_usage": [
    {"term": "奖惩分明（标题用词，正文未出现）", "meaning": "正文以嘉奖、检讨、道歉、追查等条目落实奖惩安排。", "evidence": "P003–P004、P007、P013", "ambiguity": "标题与正文用词不一致，标题是否概括全文需研究者判断"},
    {"term": "敏感企业", "meaning": "作者对企业性质的描述，未点名。", "evidence": "P005", "ambiguity": "界定标准未说明"},
    {"term": "人格受侮辱", "meaning": "作者承认不可容忍的事项。", "evidence": "P002", "ambiguity": "无"},
    {"term": "应对媒体的恰当训练／既定的规章制度限制", "meaning": "作者指出的企业两项缺失。", "evidence": "P005", "ambiguity": "具体内容未列举"},
    {"term": "事实证据", "meaning": "通过引诱对方付费而形成的证据。", "evidence": "P012", "ambiguity": "手段的合法性未讨论"},
    {"term": "心理康复", "meaning": "作者给该员工的后续安排，原文加引号。", "evidence": "P013", "ambiguity": "是字面安排还是反讽，本文未说明"}
   ],
   "examples_and_targets": [
    "提问所指事件（女记者打听机密、理想汽车男员工涉侮辱女性的回应、女记者要求公开道歉）——提问者陈述（Q001）；作者正文未出现“理想汽车”“女记者”字样，只以“敏感企业”“该员工”指代",
    "“配合度高的媒体”“之前这家的直接竞争对手”——作者方案中的媒体操作对象（行动建议，P009；指代不明）",
    "“协助女性权益的法律援助组织”——建议捐赠对象（机构类别，未点名，P010）",
    "“商业间谍、内幕交易、意图操纵股价和扰乱金融市场”——建议举报的罪名类别（行动建议，P011）",
    "“砍掉几个人头挂在大门上当装饰”——暴力化措辞（修辞材料，P012）",
    "“企业文化负责人”“董事长”“法务部”“合规部门”——企业内角色（行动建议中的主体，P010–P013）"
   ],
   "conditions": [
    "全部处置方式以“一种可以考虑的”作限定，非作者主张的唯一方案（P006）",
    "嘉奖保密意识的同时以禁止泄密并列清单为前提（P008）",
    "法务追查限定于“不通过企业正式消息发布渠道”且“查有实据”（P011）",
    "引诱付费取证的前提：员工主动通报法务部门（P012）",
    "员工转岗以“后续可以选择”为条件（P013）",
    "道歉的理由限定为“内部疏于对尊重女性的意识培养”（P010）"
   ],
   "rhetoric_and_tone": "条目式清单（“几条：”，1)2)3)…编号），公文化、管理方案语气，动词多为“嘉奖”“公告”“检讨”“追查”“报案”；中间夹带攻击性与戏谑措辞（“引诱对方付费”“砍掉几个人头挂在大门上当装饰”）；以引号标注“进行心理康复”；对企业人事、公关与法务的安排具体到岗位。",
   "unresolved_questions": [
    "作者正文未点名“理想汽车”，也未出现“女记者”，提问中的当事双方在正文中仅为“敏感企业”“该员工”，本文与提问事件的对应关系需读者自行连接",
    "P009“是之前这家的直接竞争对手”指代不明：指该媒体还是指该企业，本文未说明",
    "P012“砍掉几个人头挂在大门上当装饰”是字面还是比喻，本文未说明",
    "P012“引诱对方付费，形成事实证据”的合法性与伦理边界，作者未讨论",
    "提问中“女记者要求企业公开道歉”这一诉求本身，作者未直接评价",
    "“敏感企业”的界定标准未说明",
    "处置方式的成本、可行性与法律风险，作者未评估",
    "question 字段（Q001）在机械生成的 paragraphs 中没有 Pnnn 定位，提问者说法只记录于 question_context 与 examples_and_targets，未计入 evidence",
    "渲染包中 brief 末尾截断（“1）对内通报嘉奖——表扬该员工的保密意识。”之后被截），brief 仅作导航"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "任何人的人格受侮辱当然是不能容忍的，这没有疑问。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "忠诚应该嘉奖。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "保密意识应该嘉奖。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "员工没有全员受到应对媒体的恰当训练，也没有既定的规章制度限制。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "一种可以考虑的处置方式如下：", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P007", "quote": "对内通报嘉奖——表扬该员工的保密意识。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "禁止任何员工对任何媒体、自媒体泄露企业机密信息", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "该公开信透露给配合度高的媒体作为独家优先报道", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "就内部疏于对尊重女性的意识培养对公众道歉。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "企业文化负责人和董事长同台鞠躬致歉。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "并向协助女性权益的法律援助组织实行常规性的年度捐赠，成为其主要捐助者之一。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "将坚决追查一切不通过企业正式消息发布渠道刺探我司内部消息的行为。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "将按照商业间谍、内幕交易、意图操纵股价和扰乱金融市场向相关部门举报和报案。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "在主动通报法务部门的前提下，引诱对方付费，形成事实证据。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "争取半年内砍掉几个人头挂在大门上当装饰。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "后续可以选择转岗到合规部门。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["企业管理", "公共关系", "职场与劳动", "媒体伦理"],
   "issue_candidates": ["企业机密与媒体刺探", "员工忠诚与保密意识的奖惩", "人格侮辱与性别尊重", "企业对内对外的危机处置"],
   "text_function_candidates": ["答疑", "行动建议", "方案设计", "评论"],
   "object_candidates": ["理想汽车（提问者提及，作者未点名）", "女记者（提问者提及，作者未点名）", "敏感企业", "涉事男员工", "媒体与自媒体", "法务部", "董事长"],
   "working_keywords": ["奖惩分明", "忠诚", "保密意识", "敏感企业", "媒体沟通规范训练", "事实证据", "心理康复", "合规部门"]
  },
  "notes": "无图片节点。正文 568 字符、13 段，一次读完（P001–P013）。提问含具体企业与当事人（理想汽车、女记者），作者正文未点名任何一方，只以“敏感企业”“该员工”指代；提问者说法与作者判断已分开记录。七条处置方式作者自述为“一种可以考虑的”，语气按 hypothetical 保留（C004–C009）。P012 的暴力化措辞按原文保留，未作评价。"
 },
 "f41e9566": {
  "analysis": {
   "question_context": "提问者问“恋爱到什么程度可以发生性关系呢？”（Q001，属提问者，不归给作者）。作者不按恋爱阶段给标准，而是先用反问把问题定性为“性命交托的事”，再给出条件式判据（毫无侥幸、仍能接受并高兴），随后批评以侥幸与贪婪驱动的做法，转入父母如何教养子女，最后扩展到对日常戾气与鄙视的伦理呼吁。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以反问定性：这是性命交托的事，作者把判断交回提问者。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "条件式判据：若毫无侥幸地知道用这个换不到任何其他东西、也知道这是性命交关的冒险，仍能接受并觉得高兴，那么时候就到了。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "反驳常见做法：太多人基于对危险的极端侥幸、对背后利益的极端“乐观”，算得“大有可为”的超利润结局而去做这事，那就错了。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "指认两种错误驱动：自信铁定安全是愚蠢（人善于伪装）；贪图福利是贪婪（人精通利诱）；把本应奋不顾身、无欲无求的事做成被愚蠢和贪婪驱动的事，且众生以此为幸福准绳——作者以“人类实在是一种奇妙难言的动物”作评。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "父母视角的否定性建议：想避免子女一失足成千古恨，不要指望“富养”、不要靠教多疑、不要指望“先让对方付出”，并各自给出理由。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015"], "summary": "正面建议：靠消除子女的侥幸心、打散贪婪心、培养必要的英勇，并给出各自效果。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017"], "summary": "结果承诺：处处奉行可同时造就子女的开放与安全，使ta们不易错过机会也不易做错选择。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019"], "summary": "命题：爱温柔到极点，但任何一丁点都是绝对的英勇行为，只可能发生在两个无畏的人之间；这是保证无怨无悔的唯一办法。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022"], "summary": "告知困境：因性的特殊亲密性，几乎所有传染病都是性传播疾病；有意无意诱惑你的人逻辑上极不可能做必要告知，因为告知后百分之九十九被拒，长期坚持近乎自戕、极难坚持。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "社会条件与谅解：社会事实实行“没有性经验、性魅力就不是个足额的人”的残酷法则；坚持告知等于用自尊与基本人格做牺牲，结果是孤独与抛弃；故作者认为可理解、甚至不忍心责怪多数人放弃警告。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P027", "P028", "P029"], "summary": "推论与告诫：做过就习以为常，已采取主动诱惑策略不会半途而废；不要低估“对方没说估计就是没事”这种判断的危险性。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P030", "P031", "P032", "P033"], "summary": "扩展呼吁：希望人反思自己放出的戾气与鄙视如何改变世界并最终害每一个人；这不是琐事而是真正的威胁；希望更多人摈弃伤人的习惯，行有余力时在保护自身前提下尽可能“徒劳的劝说”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问回应提问：“性命交托的事，你觉得呢？”——作者不给出恋爱阶段标准。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若你毫无侥幸地知道用这个无法保证换到任何其他东西（终老一生、终成眷属、结婚、不离婚、优待、温柔、不受骗等），也知道这是性命交关的冒险，仍能接受并觉得高兴，那么时候就到了。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "太多人基于对危险的极端侥幸、对背后利益的极端“乐观”，算得“大有可为”的超利润结局而去做这事——那就错了。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自信铁定安全是愚蠢（人有多么善于伪装）；贪图由此而来的种种福利是贪婪（人多么精通于利诱）。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "把本来必须出自奋不顾身、无欲无求的事，做成被愚蠢和贪婪驱动的事，且芸芸众生以此为幸福的准绳衡量其他幸福可能；作者以“人类实在是一种奇妙难言的动物”作评。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "父母想避免子女一失足成千古恨：不要指望“富养”（会养出对富裕生活的高度依赖）、不要靠教多疑（多疑到孤苦终身也不能接受）、不要指望“先让对方付出”（会反向筛选出没有其他选择的loser）。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要靠消除子女的侥幸心（凡有选择必然慎重）、打散贪婪心（不受外物所诱，并对利诱之徒心生鄙视和恶心）、培养必要的英勇（唯有英雄可识英雄）。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "你如果处处奉行，可以同时造就ta们的开放与安全；ta们将既不易错过机会，也不易做错选择。", "evidence": ["E16", "E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱虽然温柔到极点，但任何一丁点都是绝对的英勇行为，它只可能发生在两个无畏的人之间；这是保证无怨无悔的唯一办法。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为性的特殊亲密性，几乎所有的传染病都是性传播疾病（作者的事实性断言，待外部核查）。", "evidence": ["E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有意无意诱惑你的人，逻辑上是极不可能对你做必要告知的；因为一旦告知，获得的答复百分之九十九是拒绝，长期坚持这种原则近乎直接自戕、非有极其特殊的意志力极难坚持。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在这个社会事实地实行着“没有性经验、性魅力就不是个足额的人”的残酷法则，作者称之为非常残酷的、非常没有人性的社会规则。", "evidence": ["E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "坚持告知实际上是在用自己的自尊和基本人格做牺牲，而牺牲的结果是事实的孤独和抛弃。", "evidence": ["E25", "E26"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "所以可以理解——甚至作者觉得都不能忍心去责怪——绝大多数对爱没有以死坚持的信仰的人，都会在不久之后放弃继续警告对方自己身上的潜在健康威胁，以换回自己的“自尊”和“人格”。", "evidence": ["E27"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "只要做过，也很快会习以为常；而且既然已经采取了主动诱惑的策略，哪有半途而废的道理（以反问表达）。", "evidence": ["E28", "E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要在任何意义上低估“对方没说估计就是没事”这种判断的危险性。", "evidence": ["E30"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对世界放出的每一分戾气、发泄的每一丝鄙视会深刻地改变世界并最终害每一个人；这不是无关紧要的日常琐事，而是在最后会深刻伤害到每一个人的真正威胁。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "希望有更多的人主动摈弃这些伤人的习惯，行有余力的话更要在保护自身的前提下尽可能“徒劳的劝说”。", "evidence": ["E34"]}
   ],
   "argument_steps": [
    "以反问把问题定性为“性命交托的事”，不按恋爱阶段作答（P001）。",
    "给出条件式判据：毫无侥幸地知道换不到任何东西、明知是性命交关的冒险，仍能接受并高兴（P002）。",
    "反驳以侥幸与“乐观”计算超利润结局的做法（P003–P004）。",
    "指认两种错误驱动：自信安全是愚蠢、贪图福利是贪婪，并指出众生以此为幸福准绳（P005–P008）。",
    "转向父母视角，先列三种被否定的做法：富养、教多疑、先让对方付出（P009–P012）。",
    "给出正面教养路径：消除侥幸心、打散贪婪心、培养必要的英勇（P013–P015）。",
    "承诺结果：可同时造就开放与安全，不易错过机会也不易做错选择（P016–P017）。",
    "提出命题：爱只可能发生在两个无畏的人之间，是保证无怨无悔的唯一办法（P018–P019）。",
    "以性与传染病的连接转入告知困境：诱惑者极不可能做必要告知，因为告知近乎自戕（P020–P022）。",
    "补充社会条件：社会的残酷法则使告知者以自尊与人格为代价，结果是孤独与抛弃（P023–P025）。",
    "据此表达谅解：多数人放弃警告可以理解，甚至不忍心责怪（P026）。",
    "推论后果并告诫：做过就习以为常，不要低估“对方没说估计就是没事”的危险（P027–P029）。",
    "扩展为对日常戾气与鄙视的伦理呼吁，并以“徒劳的劝说”作结（P030–P033）。"
   ],
   "concept_usage": [
    {"term": "性命交托的事", "meaning": "作者对性的定性，把提问抬到性命交托的级别。", "evidence": "P001", "ambiguity": "“性命交托”的具体含义未展开"},
    {"term": "毫无侥幸", "meaning": "判据的核心条件：不指望以此换得任何东西，并明知是性命交关的冒险。", "evidence": "P002", "ambiguity": "“毫无”是程度要求还是理想状态，本文未说明"},
    {"term": "侥幸／贪婪", "meaning": "作者指认的两种错误驱动，分别对应自信铁定安全与贪图由此而来的福利。", "evidence": "P005–P006、P013–P014", "ambiguity": "无"},
    {"term": "奋不顾身、无欲无求", "meaning": "作者认为性本来必须出自的性质。", "evidence": "P007", "ambiguity": "与“觉得高兴”（P002）的关系未说明"},
    {"term": "开放与安全", "meaning": "作者给出的教养目标，可同时造就。", "evidence": "P016", "ambiguity": "两者的具体标准未说明"},
    {"term": "无畏／英雄", "meaning": "爱的条件：只可能发生在两个无畏的人之间，唯有英雄可识英雄。", "evidence": "P015、P018", "ambiguity": "修辞性表述，未给判定标准"},
    {"term": "徒劳的劝说", "meaning": "作者提倡的、在保护自身前提下尽可能持续的告知。", "evidence": "P033", "ambiguity": "为何称“徒劳”未说明"},
    {"term": "戾气／鄙视", "meaning": "作者认为会深刻改变世界并最终害每一个人的日常行为。", "evidence": "P030–P032", "ambiguity": "与性话题的连接未说明"}
   ],
   "examples_and_targets": [
    "提问者的问法“恋爱到什么程度可以发生性关系”——作者未按阶段回答，改为条件式回答（提问者说法 Q001）",
    "父母与子女——作者论述的适用对象（P009–P017）",
    "“富养”“教多疑”“先让对方付出”——作者反驳的三种做法（反驳对象，P010–P012）",
    "“loser”——作者对“先让对方付出”所筛出对象的称呼（修辞材料，P012）",
    "“几乎所有的传染病都是性传播疾病”——作者的事实断言（待外部核查，P020）",
    "“没有性经验、性魅力就不是个足额的人”——作者引述并批评的社会法则（原文加引号，P023）",
    "“对方没说估计就是没事”——作者引述并警告的判断（P029）",
    "“徒劳的劝说”——作者自加引号的策略名（P033）"
   ],
   "conditions": [
    "判定为条件式：毫无侥幸地知道换不到任何东西 ＋ 知道这是性命交关的冒险 ＋ 仍能接受并觉得高兴（P002）",
    "“换不到”清单：终老一生、终成眷属、结婚、不离婚、优待、温柔、不受骗等（P002）",
    "教养建议以“你如果处处奉行”为条件（P016）",
    "关于诱惑者的推论限定为“有意无意诱惑你的人”，并使用“极不可能”“百分之九十九”“极难”等概率限定（P021–P022）",
    "对放弃警告者的谅解限定为“绝大多数对爱没有以死坚持的信仰的人”（P026）",
    "劝说他人的条件：保护自身的前提下、行有余力（P033）",
    "作者使用“几乎所有的传染病”这一带限定的表述（P020）"
   ],
   "rhetoric_and_tone": "第二人称训诫与箴言体；短段排比（“自信铁定安全，是愚蠢”“贪图因此而来的种种福利，是贪婪”）；反问（P001、P028）；对社会的批判性命名（“非常残酷的、非常没有人性的社会规则”）；使用“小孩子们”“loser”等口语；末段由性话题转入对普遍戾气与鄙视的伦理呼吁，语气由训诫转为祈愿式（“希望能有更多的人…”）。",
   "unresolved_questions": [
    "提问所问的“恋爱到什么程度”的阶段标准，作者未给出，只给条件式判据",
    "P020“几乎所有的传染病都是性传播疾病”为作者的强事实断言，需外部核查",
    "P022“百分之九十九是拒绝”的数字来源未说明，需外部核查",
    "P023“没有性经验、性魅力就不是个足额的人”是作者引述（原文加引号）还是自造表述，本文未标明出处",
    "P033“徒劳的劝说”为何是“徒劳”、与 P021–P026 的告知困境如何一致，本文未说明",
    "“在保护自身的前提下”的具体保护方式未说明",
    "消除侥幸心／打散贪婪心／培养英勇的具体操作方法未给出",
    "P020 以“因为”与 P021“并且”相连，性与传染病同告知问题之间的推理关系未说明",
    "“性命交关的冒险”中的风险具体指哪些（健康、情感或其他），本文未列举完整",
    "question 字段（Q001）在机械生成的 paragraphs 中没有 Pnnn 定位，提问者说法只记录于 question_context 与 examples_and_targets，未计入 evidence",
    "渲染包中 brief 末尾截断（“那么时候就”），brief 仅作导航"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "性命交托的事，你觉得呢？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "如果你毫无侥幸的知道用这个无法保证换到任何其他东西", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "你还是能接受，而且还会觉得高兴，那么时候就到了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "太多的人是基于对危险的极端侥幸、对背后利益的极端“乐观”", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P004", "quote": "那就错了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "自信铁定安全，是愚蠢——小孩子们真的很难想象，人是有多么善于伪装；", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "贪图因此而来的种种福利，是贪婪——小孩子们真的很难明白，人是多么精通于利诱。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "把一件本来必须是出自奋不顾身、无欲无求的事，做成了一件被愚蠢和贪婪驱动的事", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "人类实在是一种奇妙难言的动物。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "不要指望依靠什么“富养”——因为你一样会养出对富裕生活的高度依赖；", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "也不要靠教什么多疑——因为再多疑你也不能接受多疑到孤苦终身；", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "更不要指望靠什么“先让对方付出”——这会反向特异的筛选出没有其他选择的loser。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "要靠消除子女的侥幸心——于是凡有选择，必然慎重；", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "靠打散ta们的贪婪心——无外求之物，于是不受外物所诱", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "靠培养必要的英勇——唯有英雄可识英雄。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "你如果处处奉行，你可以同时造就ta们的开放与安全。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "ta们将既不易错过机会，也不易做错选择。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "它只可能发生在两个无畏的人之间。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "这是保证无怨无悔的唯一办法。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "因为性的特殊亲密性，几乎所有的传染病都是性传播疾病。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "一个有意无意诱惑你的人，逻辑上是极不可能对你做必要告知的。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "因为ta们一旦告知，获得的答复百分之九十九是拒绝。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "极难长期坚持这种近乎于直接自戕的原则。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "这是一个非常残酷的、非常没有人性的社会规则。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "实际上是在用自己的自尊和基本人格做牺牲", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "是事实的孤独和抛弃。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P026", "quote": "甚至我觉得都不能忍心去责怪", "relation": "qualifies"},
    {"key": "E28", "paragraph_id": "P027", "quote": "只要做过，也很快会习以为常。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P028", "quote": "哪有半途而废的道理？", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P029", "quote": "不要在任何意义上低估“对方没说估计就是没事”这种判断的危险性。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P030", "quote": "我希望人能反思一下自己对世界放出的每一分戾气、发泄的每一丝鄙视", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P031", "quote": "那不是无关紧要、微不足道、不值得“大惊小怪”的日常琐事。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P032", "quote": "而是在最后会深刻的伤害到每一个人的真正威胁。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P033", "quote": "更要在保护自身的前提下尽可能的“徒劳的劝说”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性与亲密关系", "家庭教养", "社会批判", "伦理"],
   "issue_candidates": ["性关系的时机判据", "侥幸与贪婪的驱动", "性传播疾病与告知义务", "子女的性教育与开放安全", "日常戾气的社会代价"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "社会评论"],
   "object_candidates": ["父母与子女", "诱惑者", "“现在这个社会”", "提问者（未具名）"],
   "working_keywords": ["性命交托", "毫无侥幸", "侥幸心", "贪婪心", "必要的英勇", "无畏", "徒劳的劝说", "没有性经验、性魅力就不是个足额的人"]
  },
  "notes": "无图片节点。正文 1338 字符、33 段，一次读完（P001–P033）。提问所问的“恋爱程度”作者未按阶段回答，改为条件式判据，并转入父母教养与对日常戾气的呼吁，已与提问者立场分开。P020、P022 含事实性断言与数字（“几乎所有”“百分之九十九”），只记录为待外部核查，未自行裁决。P001、P028 为反问，语气按 questioned 保留（C001、C015）。"
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
