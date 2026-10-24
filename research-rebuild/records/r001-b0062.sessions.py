# -*- coding: utf-8 -*-
"""批次 r001-b0062 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0062.sessions.py            # 写 out/r001-b0062.out.jsonl
  python3 records/r001-b0062.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0062"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0062.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "2d39cbec": {
  "analysis": {
   "question_context": "提问者问“为何近年来世界集体右转?”（Q001），预设世界正在集体右转；作者在正文首句即否定该前提，改以“左转但人对‘左得到位’的评价标准提升更快”解释该印象。提问者的前提属提问者，不计入作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总判断：世界一直左转；“右转”印象来自评价标准提升快于左转速度。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "逐项检视被称“右转”的诉求（进口与移民、反歧视、全球化、环保），指出内容均为放缓或延缓加码。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "以船舵比喻总括实际诉求位置：扳回四分之一左舵，而非右舵。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "反问谁有能力扳向右舵，断言其后果近乎毁灭性，并以朝鲜为例。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "极左/半左/微左都属左派；声势不等于政策真的右转。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P016"], "summary": "“全球右转”是恐惧感呼唤出的媒体制造的“观点热卖品”。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "以川普为唯一例外，并以假设语气预测其任满四年的“好处”。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界没有在右转，而是一直在左转。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“右转”错觉的成因是人对“左得到位”的评价标准提升得更快，快到左转速度跟不上。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被指为右转者实际要求的是降低出口／降低进口增长速度、限制新移民流入速度并提高放行门槛，而非降低进口或驱逐移民。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在反歧视政策上，他们是要求延缓或暂停进一步加强，而非取消这些政策。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他们多数是要求放缓全球化，而非反对全球化。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他们是要求减缓在环保策略上进一步加码，而非反对加强环保。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实际主张是把“左满舵”往回扳一扳，连直行都不算，只是扳回四分之一左舵。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者反问谁有能力、胆量与资本扳成右舵，并断言真扳成右舵在经济、政治、文化上几乎都是毁灭性的。", "evidence": ["E8", "E9"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "连朝鲜也很难说是右舵状态，其实在左舵，只是左得谨小慎微。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极左、半左和微左都是左派，不能因为半左和微左有了声势就认定是右转。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这种声势会让真正右翼的声音自以为春天到了而传出，但并没有影响政策到真的右转的能量。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“全球右转”更多是人们恐惧感呼唤出来的、媒体制造的观点热卖品，可换点击率和转发率。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "目前唯一的例外可以说是川普。", "evidence": ["E14"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "若川普真的任满四年，也有一个“好处”——可作为“强行右转会怎么死”的活例子。", "evidence": ["E15"]},
    {"claim_id": "C015", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者反问：到底谁真的在往过了中线的右舵上扳？", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "先给出与提问前提相反的总判断：世界一直在左转（P001）。",
    "用“评价标准提升更快”解释“右转”印象的来源（P002）。",
    "逐项检视被指为右转的诉求，指出其内容是放缓、延缓或限制加码，而非逆转（P003-P008）。",
    "以船舵刻度比喻总括实际诉求位置（四分之一左舵）（P009）。",
    "反问谁有能力扳向右舵，并断言强行右转的毁灭性后果（P010-P011）。",
    "举朝鲜为例，说明连威权体制也难称右舵（P012）；再次反问到底谁在扳向右舵（P013）。",
    "区分极左/半左/微左，指出声势不等于政策右转（P014-P015）。",
    "把“全球右转”归因于恐惧感与媒体制造（P016）。",
    "点出川普为唯一例外，并以假设语气给出预测式判断（P017-P019）。"
   ],
   "concept_usage": [
    {"term": "左／右（舵位比喻）", "meaning": "以船舵位置比喻政治方向，含“左满舵—四分之一左舵—直行—右舵”的连续刻度；左＝现行方向，右＝方向逆转。", "evidence": "P009", "ambiguity": "未给出判定左/右的具体政策刻度，比喻与政策判准之间的对应不完全明确。"},
    {"term": "右转", "meaning": "指政策方向真正逆转；作者认为该词被误用于只是放缓的情形。", "evidence": "P001", "ambiguity": "与“声势”“声音传出”相区分，作者强调后者不构成右转。"},
    {"term": "左得到位", "meaning": "衡量左转程度是否足够的评价标准，作者称其提升速度快于实际左转速度。", "evidence": "P002", "ambiguity": "未说明该标准由谁持有、如何测量。"},
    {"term": "极左／半左／微左", "meaning": "作者对左派内部的强度分类，三者均归为左派。", "evidence": "P014", "ambiguity": "未给出三类的划分依据。"}
   ],
   "examples_and_targets": [
    "川普：作者举为“目前唯一的例外”，并称其为“二愣子”（P017-P019，作者例证＋戏谑称呼）。",
    "朝鲜：作者以“连……都很难说”作例，称其其实在左舵（P012，作者例证）。",
    "“全球右转”的媒体观点热卖品：被作者归因为恐惧感的产物（P016，被批评对象）。",
    "进口／移民难民、反歧视政策、全球化、环保：被逐项检视为“放缓”而非“逆转”的诉求清单（P004-P008，作者检视对象）。"
   ],
   "conditions": [
    "论断针对“现在被称为‘右转’的这一派”的实际诉求内容（P003-P009）。",
    "对川普的判断带限定语“目前唯一的例外可以说是”，并以“要是他真的愣四年”为假设条件（P017、P019）。",
    "对朝鲜使用“很难说”，保留不确定性（P012）。",
    "“在经济上、政治上、文化上都几乎是毁灭性的”为对强行右转后果的断言，含“几乎”限定（P011）。"
   ],
   "rhetoric_and_tone": "连续反问构成主体（P003、P005-P008、P010、P011、P013）；贯穿船舵比喻；对川普用“二愣子”的戏谑称呼与“先看他还能愣几天”的调侃；结尾以反讽式“也有好处”作结。",
   "unresolved_questions": [
    "提问者“世界集体右转”与作者“一直在左转”是相反的事实判断，文中未给出数据或指标，需外部核查。",
    "未给出判定“左舵/右舵”的具体政策刻度与测量方法（P009）。",
    "对川普任满四年的预测未给出依据，仅以“先看他还能愣几天”带过（P018-P019）。",
    "“媒体制造的观点热卖品”未举具体媒体或案例（P016）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "世界没有在右转，而是一直在左转。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "人对“左得到位”的评价标准提升得更快", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "其实只是要降低出口 / 降低进口增长的速度", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "他们是在要求延缓或者暂停进一步加强这些政策。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "他们多数是在要求放缓全球化。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "他们是在要求减缓在环保策略上进一步加码。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "而是要把左满舵往回扳一扳", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "去扳成右舵，哪怕是四分之一右舵？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "在经济上、政治上、文化上都几乎是毁灭性的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "连朝鲜都很难说现在是右舵状态", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "你不能因为半左和微左有了声势，就认定是右转。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "但这并没有影响政策到真的右转的能量。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P016", "quote": "其实更多的是人们的恐惧感呼唤出来的媒体制造的观点热卖品", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "目前唯一的例外可以说就是川普这二愣子。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P019", "quote": "可以拿来做一个“强行右转会怎么死”的活例子。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "到底谁真的在往过了中线的右舵上扳？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治评论", "国际政治", "政治光谱/左右翼"],
   "issue_candidates": ["全球是否集体右转", "左转与右转的判定标准", "移民与进口政策", "反歧视政策与全球化", "环保政策加码", "媒体与恐惧情绪"],
   "text_function_candidates": ["答疑", "论辩", "评论"],
   "object_candidates": ["川普", "朝鲜", "媒体", "被称右转的政治派别"],
   "working_keywords": ["左转", "右转", "左满舵", "四分之一左舵", "极左/半左/微左", "观点热卖品"]
  },
  "notes": "无图片节点；正文19段全部读完。提问者的“世界集体右转”前提与作者判断相反，已按归属区分。文中三种结果式预测与川普段落带假设/限定语气，未按断言处理。"
 },
 "65a6161c": {
  "analysis": {
   "question_context": "提问者问如何评价文章《小县城的中年粉红：在混吃等死中研究世界局势》（Q001），即请求对被评文章作出评价。作者未逐句评价原文，而是用连续追问把被评文章的隐含替代方案逼出来，并论证普通人关心世界局势的正当性。被评文章的具体论据未随本文给出。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"], "summary": "以替换组合的连续追问（去掉粉红／去掉研究局势／迁移或升级小县城等），追问批评者想改成什么更好的状态。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P008"], "summary": "提出标准：要先有更好的可选方案，才能批评眼下方案不行。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "论证当代普通人持有资产或经营时，关心世界局势是题中应有之义，并列出与经营成本的直接关联。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "反问并量化：国际局势与个人身家的关系比同事、表哥、老同学更亲近。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "判定“国际局势与老百姓无关”之说已过时，并以“女人读什么书”的类比指出嘲讽本身构成反讽。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要有一个更好的可选方案，才能批评眼下的方案不行，否则与“嫌直线距离太长”无异。", "evidence": ["E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在现在这个时代，即使普通人只要买点指数基金、有一点固定资产或有个小局面，关心世界局势就是题中应有之义。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "国际局势与进货成本、销售预期、银行利率、物价涨跌有直接而敏感的关系；水平如何另论，但关心本身无可惊讶。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者反问：国际局势一天可影响你百分之几甚至更多的身家，为什么还要说它跟小老百姓没关系。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“国际局势与老百姓无关”的说法早已过时，这是对21世纪现代化国家社会成员提出自然经济、农业时代的要求。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把关心世界局势当作可笑之事，犹如一本正经嘲讽“女人读什么书”，该嘲讽本身即构成反讽。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "先以替换组合的追问，要求批评者说明想把现状改成什么（P001-P007）。",
    "提出批评得以成立的前提：必须先有更好的可选方案（P008）。",
    "转向正面论证：当代普通人持有资产或小生意，故关心世界局势是题中应有之义（P009）。",
    "列出与进货成本、销售预期、银行利率、物价涨跌的直接关联（P010）。",
    "反问“为什么还要说没关系”，并以影响身家的比例说明关系之近（P011-P012）。",
    "判定该说法是对21世纪现代化国家成员的自然经济式要求，已过时（P013）。",
    "以“女人读什么书”的类比收束，指出嘲讽本身构成反讽（P014）。"
   ],
   "concept_usage": [
    {"term": "粉红", "meaning": "沿用被评文章的标签，作者只在组合替换中拆解它，未自行定义。", "evidence": "P001", "ambiguity": "本文未界定“粉红”具体所指，含义依赖被评文章。"},
    {"term": "题中应有之义", "meaning": "指基于财产与经营关系而产生的合理关切，而非多余之举。", "evidence": "P009", "ambiguity": "作者以“只要买点指数基金或者有一点固定资产、有个小局面”为条件加以限定。"},
    {"term": "混吃等死", "meaning": "来自被评文章的组合标签，作者将其作为可替换项之一处理。", "evidence": "P002", "ambiguity": "作者未评价该标签是否成立。"},
    {"term": "反讽", "meaning": "指嘲讽者的嘲讽反过来暴露嘲讽者自身。", "evidence": "P014", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "被评文章《小县城的中年粉红：在混吃等死中研究世界局势》：本文的评价对象（P001）。",
    "指数基金、固定资产、小局面：作者举的普通人财产形态（P009，作者例证）。",
    "进货成本、销售预期、银行利率、物价涨跌：作者举的经营关联项（P010，作者例证）。",
    "把小县城中年集体迁移到大城市、把小县城统统升级为大城市：作者假设的不可行方案（P005，修辞材料）。",
    "“女人读什么书”：作者类比（P014，类比材料）。"
   ],
   "conditions": [
    "论证以“在现在这个时代”为时间条件（P009）。",
    "以“即使是一个普通人，只要买点指数基金或者有一点固定资产、有个小局面”为条件（P009）。",
    "“水平如何另论”承认关心水平参差，但不影响关心的正当性（P010）。",
    "过时判断以“21世纪的现代化国家”为社会条件（P013）。"
   ],
   "rhetoric_and_tone": "通篇以反问和列举式追问推进（P001-P007、P011）；口语化反诘（“呀”“好吗”）；以“犹如……一本正经的嘲讽”作类比讽刺；结尾用“反讽”下判断，带训诫意味。",
   "unresolved_questions": [
    "被评文章原文未随本文给出，“粉红”“混吃等死”等标签的具体含义依赖该文，本文未界定（P001）。",
    "P008 以“第二，”开头，但正文未见“第一，”；结构上疑有缺失或平台切分（P008），需核对语料完整性。",
    "“一天就影响到你百分之几（甚至可能百分之十几、几十）的身家”为无来源的估计，需外部核查（P012）。",
    "迁移小县城人口、升级小县城等替代方案由作者假设提出，是否属被评文章主张不明（P005）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "那把“小县城、粉红、混吃等死、研究世界局势”这一组合改成一个什么组合呢？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P008", "quote": "要有一个更好的可选方案，才能批评眼下的方案不行啊", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P009", "quote": "即使是一个普通人，只要买点指数基金或者有一点固定资产、有个小局面，关心世界局势难道不是题中应有之义吗", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "这本来就是与进货成本、销售预期、银行利率、物价涨跌……有直接而敏感的关系的事情。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "为什么还要说国际局势跟小老百姓没关系？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "这是在对一个21世纪的现代化国家的社会成员提出自然经济、农业时代的要求。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "犹如在一本正经的嘲讽“女人读什么书”——这个嘲讽本身就构成了反讽。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "怕是比你跟你同事、表哥、老同学的关系还要亲近好吗。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P005", "quote": "总不能自己出钱把小县城中年都集体迁移到大城市", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会评论", "社会心态", "经济生活与信息关切"],
   "issue_candidates": ["小县城中年群体标签", "普通人是否应关心国际局势", "财产与全球化信息的关联", "对他人生活方式的嘲讽"],
   "text_function_candidates": ["答疑", "评论", "论辩"],
   "object_candidates": ["小县城中年人", "被评文章及其作者", "普通人投资者/经营者"],
   "working_keywords": ["粉红", "混吃等死", "题中应有之义", "反讽", "小县城"]
  },
  "notes": "无图片节点；正文14段全部读完。提问为“如何评价某文”，作者未逐句评点，而是以追问与正面论证回应，已按作者主张记录。P008 出现“第二，”而正文未见“第一，”，已在未决问题登记。"
 },
 "7d9d6244": {
  "analysis": {
   "question_context": "提问者问：为何中国人往往能一眼识别出美国出生的华裔（ABC）（Q001）。作者未直接回答识别线索，而是提出一个关于面相成因的假说：语言（发音方式与表情要求）是同一人种在不同文化环境中总体面貌发育差异的根本原因，并把该假说自评为可供研究的选题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出核心假说：语言是同一人种面貌发育差异的根本原因。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "以日本老人与中国、韩国、蒙古族、苗族老人的面相差异，以及嘴角下撇的观察为例支持假说。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "把假说推到说英语与说汉语的华人，并加“营养水平相当”的条件。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "自评这是有趣的选题，可拿去研究。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者一直怀疑：语言才是对不同文化环境的同一人种造成总体面貌发育差异的根本原因。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "日本老人与中国、韩国、蒙古族、苗族老人的面相差异，很可能是各自语言的发音方式和表情要求塑造出来的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "例如日本老人嘴角下撇的情况似乎比中国老人多得多。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在营养水平相当的情况下，说英语的华人与说汉语的华人的面相差异，根子很可能也在于语言。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自评这是一个比较有趣的选题，可以拿去研究。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "以“我一直怀疑”提出语言塑造面貌发育的假说（P001）。",
    "举东亚诸群体与日本老人的面相差异作为观察支持（P002）。",
    "给出更具体的观察项：日本老人嘴角下撇多于中国老人（P003）。",
    "把同一假说用于说英语与说汉语的华人，并加“营养水平相当”的条件以排除营养因素（P004）。",
    "自评为有趣选题，交给他人去玩（P005-P006）。"
   ],
   "concept_usage": [
    {"term": "语言", "meaning": "在本文指具体的发音方式和表情要求，被设为塑造面貌发育的原因。", "evidence": "P002", "ambiguity": "未说明语言通过何种生理机制影响面貌发育。"},
    {"term": "面相", "meaning": "指总体面貌发育所呈现的差异。", "evidence": "P001", "ambiguity": "未说明如何测量面相差异。"},
    {"term": "根本原因／根子", "meaning": "作者用“怀疑”“很可能”限定，表示尚未确证的因果假设。", "evidence": "P001", "ambiguity": "语气为推测而非断言。"}
   ],
   "examples_and_targets": [
    "日本老人与中国老人、韩国老人、蒙古族老人、苗族老人：作者观察例证（P002）。",
    "日本老人嘴角下撇：作者观察例（P003）。",
    "说英语的华人与说汉语的华人：作者例证，并加营养条件（P004）。",
    "提问中的 ABC 识别问题：构成语境，正文未直接回答（Q001）。"
   ],
   "conditions": [
    "“在营养水平相当的情况下”为排除营养因素的条件（P004）。",
    "通篇以“很可能”“似乎”“怀疑”等限定词表达不确定性（P001-P003）。",
    "未说明样本规模、地区、年代与统计方法等经验条件。"
   ],
   "rhetoric_and_tone": "探询式、假说式语气（“我一直怀疑”“很可能”）；口语化收尾“这是个比较有趣的选题，拿去玩”，把自身定位为选题建议而非结论。",
   "unresolved_questions": [
    "提问（为何能一眼识别 ABC）未在正文得到直接回答，正文转而讨论面相成因（Q001）。",
    "“日本人嘴角下撇多于中国老人”属未给来源的观察，需外部核查（P003）。",
    "未说明如何排除遗传、饮食、气候等竞争解释（P002-P004）。",
    "未给出可检验的机制与数据，假说停留在猜测层面（P001）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我一直怀疑，其实语言才是对不同文化环境的同一人种造成总体面貌发育差异的根本原因。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "很可能是因为各自语言的具体发音方式和表情要求所塑造出来的", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "比如日本老人的嘴角下撇的情况似乎就比中国老人多得多。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "在营养水平相当的情况下——很可能根子也是在这里。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这是个比较有趣的选题", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "拿去玩。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言与文化", "体质人类学/面相", "族群差异观察"],
   "issue_candidates": ["ABC 的面相识别", "语言发音对面部发育的影响", "跨文化同人种面貌差异"],
   "text_function_candidates": ["答疑（实为提出选题）", "假说提出"],
   "object_candidates": ["日本人", "中国人", "韩国人", "蒙古族", "苗族", "美国出生的华裔（ABC）", "说英语的华人"],
   "working_keywords": ["语言", "面相", "发音方式", "表情要求", "ABC"]
  },
  "notes": "无图片节点；正文6段全部读完。全文为假说与选题建议，未回答提问中的识别线索；关键判断均带“怀疑/很可能/似乎”限定，已按 qualified 记录，未升格为断言。"
 },
 "69744eb2": {
  "analysis": {
   "question_context": "提问者问对“韩国政府收回父母惩戒权”怎么看（Q001）。作者不讨论韩国立法的具体内容，而先否定提问与事件的表述框架本身，进而断言父母惩戒权超出现有人类社会形态的干预能力，任何政府立法剥夺都会失败或代价不可承受。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "否定问题框架：把此事定义为“政府收回父母惩戒权”本身就是错误。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P004"], "summary": "核心判断与理由：父母惩戒权非现有人类社会形态所能干预；剥夺等同抢走他人子女。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "预测立法剥夺的三种结果。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "让步式限定：至多可对致残、致死、失学等显著客观后果做极肤浅干预。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "反事实条件：除非改变人类生育形态，否则不要妄想收回惩戒权。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009", "P010"], "summary": "结论：政府既无资格给也无资格收回；此为天赋天然权利，剥夺须买单而机构买不起。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把这件事定义为“政府收回父母惩戒权”本身就是一种错误。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母的惩戒权是目前的人类社会形态没有能力干预的东西。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "任何政府若立法剥夺父母惩戒权，只会有三种结果：因根本不实施而丧失司法信用、因强行实施的社会成本而破产，或两者同时发生。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本质上这与抢走他人的子女没有两样。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "顶破天也只能基于极其显著的后果做极其肤浅的干预，例如追究致残、致死、失学这类显著而客观的后果。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "除非改变人类的生育形态（如由政府机构孵化捐赠生殖细胞或公民基因库克隆、禁止自然受孕），否则永远不要妄想“收回父母的惩戒权”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这本来就不是政府有资格“给”的东西，更不是政府有资格“收回”的东西。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是天赋的天然权利，想剥夺就要买单；由人类组成的机构在数学上没有可能买得起这个单。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "光使用“收回父母的惩戒权”这个词汇都是荒唐可笑的。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "先否定提问所预设的“政府收回”框架（P001）。",
    "断言父母惩戒权超出目前人类社会形态的干预能力（P002）。",
    "以“要么……要么……要么”预测立法剥夺的三种结果（P003）。",
    "给出理由：剥夺等同于抢走他人子女（P004）。",
    "让步式限定可干预范围：仅限致残、致死、失学等显著客观后果（P005）。",
    "提出反事实前提：除非改变人类生育形态（P006-P007）。",
    "断言政府既无资格给也无资格收回（P008）。",
    "断言其为天赋的天然权利，剥夺须买单且机构在数学上买不起（P009）。",
    "以对用词本身的否定评价收束（P010）。"
   ],
   "concept_usage": [
    {"term": "父母惩戒权", "meaning": "作者视为天赋的天然权利，不由政府授予，超出目前人类社会形态的干预能力。", "evidence": "P002", "ambiguity": "未界定惩戒权的范围与限度，也未给出“天赋”的依据来源。"},
    {"term": "收回", "meaning": "作者认为该词不适用于此项权利，因为政府从未有资格给出。", "evidence": "P008", "ambiguity": "无。"},
    {"term": "买单", "meaning": "比喻剥夺该权利须承担的全部社会成本。", "evidence": "P009", "ambiguity": "未说明成本如何计量，“数学上没有可能”为未展开的强断言。"},
    {"term": "极其显著的后果", "meaning": "作者给出的可干预门槛，如致残、致死、失学。", "evidence": "P005", "ambiguity": "未说明由谁认定、依何程序认定。"}
   ],
   "examples_and_targets": [
    "韩国政府收回父母惩戒权：提问所指事件，作者否定其表述框架而非讨论立法细节（P001）。",
    "致残、致死、失学：作者举的可干预后果例（P005）。",
    "捐赠生殖细胞在政府机构孵化、公民基因库克隆、禁止自然受孕生育：作者假设的反事实方案（P006）。",
    "“由人类组成的机构”：作者的一般化对象（P009）。"
   ],
   "conditions": [
    "以“目前的人类社会形态”为时间/形态条件（P002）。",
    "三种结果以“哪个政府想要立法剥夺父母的惩戒权”为条件（P003）。",
    "“顶破天，也只能……”限定干预上限（P005）。",
    "“除非你改变人类的生育形态……否则永远不要妄想”构成反事实条件（P006-P007）。"
   ],
   "rhetoric_and_tone": "强断言与绝对化措辞（“永远不要妄想”“数学上没有可能”“荒唐可笑”）；“要么……要么……要么”三段排比预测；反事实设想；结尾一句短评收束，带训诫口吻。",
   "unresolved_questions": [
    "韩国相关立法的具体内容与实施情况未在文中说明，需外部核查（Q001、P001）。",
    "“数学上没有可能买得起这个单”未给出计算或论证，属强断言（P009）。",
    "“天赋的天然权利”未说明依据来源（P009）。",
    "“极其显著的后果”未说明认定主体与程序（P005）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个事情被定义为“政府收回父母惩戒权”本身就是一种错误。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "父母的惩戒权是目前的人类社会形态没有能力干预的东西。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "要么因为根本不实施而丧失司法信用；要么因为强行实施造成的社会成本而破产", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "因为本质上这和抢走他人的子女没有两样。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "也只能基于极其显著的后果做极其肤浅的干预", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "除非你改变人类的生育形态", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P007", "quote": "否则永远不要妄想什么“收回父母的惩戒权”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "因为这本来就不是政府有资格“给”的东西，更不是政府有资格“收回”的东西。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "这是天赋的天然权利，想剥夺，就要买单。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "光使用这个词汇都是荒唐可笑的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学/权利理论", "家庭与法律", "社会评论"],
   "issue_candidates": ["父母惩戒权是否可由政府收回", "国家对家庭干预的边界", "儿童保护与显著后果干预"],
   "text_function_candidates": ["答疑", "论辩", "评论"],
   "object_candidates": ["韩国政府", "父母", "子女", "政府机构"],
   "working_keywords": ["父母惩戒权", "收回", "天赋的天然权利", "买单", "显著而客观的后果"]
  },
  "notes": "无图片节点；正文10段全部读完。作者未讨论韩国立法细节，而是否定事件与提问的表述框架，已按此记录归属；三种结果为预测性断言，仍按作者主张记录并保留 predicted 语气。"
 },
 "7cdfab67": {
  "analysis": {
   "question_context": "提问者问如何看待马前卒的“社会化抚养”主张（Q001）。作者以分点论辩的方式提出反对：先列三条理由（抑制思想多样性、对落后者不公正、其顺序对应有期限的紧迫社会困境），在“补充一条”中再论“有限而积极的社会化抚养”仍属潜在灾难，最后给出谦抑原则式的行动边界。正文未点名马前卒，评论对象为“社会化抚养”这一主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "第一点：社会化抚养从根上抑制思想多样性；以无限克隆单一品种、香蕉濒危作类比。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "第二点：对“落后者”无法交代的不公正；单一评价体系必有相对失败者，只能靠多维化解决而社会化抚养给不出足够维度。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "斯巴达例证：只培养战士、掉队者被自然淘汰；反问能否提供足够多的“系”与重选机会。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "第三点：该顺序必然对应紧迫而明确的社会困境（以色列、普鲁士、苏联），而紧迫性有期限，到期后陷入惯性危机。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "邮轮比喻：须撞冰山有痛感才转舵；平时慢速、危机时全马力、危机后政府离开舵轮与油门以重建信用。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "小结：社会化抚养属“前进四”级措施，对无存亡危机的巨型国家危险；只能作失败后的补充，不可作进取性策略。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "补充一条：转述“只搞有限社会化抚养＋政府积极检查家庭”的设想，并称之为用有限化救赎该概念。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "论证：正因效益巨大才绝不可行，因直接受益者是判定实体本身，它将实际拥有拆开家庭、猎取“人力资源”的权力。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "以反问揭示标准无法固定（金牌数量够、禁卫军够强、好帮手够多、红线够合理），重申收益巨大故危险且绝不可行。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032"], "summary": "行动边界：必须绝对遵循谦抑原则，民不举官不究，发动端不在政府，举报人不得受益；否则后果严重。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“社会化抚养”会从根上抑制社会成员的思想多样性。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“优选优育”去除“令人不快”的生物多样性，如同认为某品种优秀就无限克隆；并类比香蕉濒临灭绝的单一化风险。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会化抚养对“落后者”存在无法交代的不公正：单一评价体系下必有大部分人成为相对失败者，该问题只能由评价体系多维化解决，而社会化抚养不可能提供足够的维度。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "斯巴达人就是社会化抚养，因为他们只要战士，战士教育中的掉队者被“自然淘汰”也不可惜。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者反问：你能提供多少个系、给人多少次重选机会？在“次要专业”里“成功”的学生是否真的拥有了一个维度？", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“从第一个不行到最后一个不行”的顺序必然对应一种紧迫而明确的社会困境，如以色列要求生存、普鲁士谋求德意志统一、苏联要快速工业化。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种紧迫性和明确性有期限；一旦到期或挑战转变，原有人力投资造就的最精锐成果在新问题前并不适用，某些方向又缺精英，将陷入巨大的惯性危机。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "问题转向须靠老体系不断出问题、直到形成足够共识才能纳入议程，到那时连稍微在碰撞前抓住最近栏杆的机会都没有了。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类社会如冰海中的巨型邮轮，必须撞上冰山、有了足够痛感才真正开始转舵；即使右满舵也只能眼睁睁看着剩余碰撞进程展开，顶多少挨最后百分之十。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "邮轮式策略应是平时慢速行进，撞上什么而有痛感时因非全速故损失可管理，此时再全马力躲开碰撞。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "危机解除后应回到慢速行驶状态，政府要离开舵轮和油门，珍惜并重建信用以备下一次危机干预。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“社会化抚养”绝对是“前进四”级别的措施，对一个并非处在明确存亡危机的巨型国家而言是类似“蒙着眼睛在冰海上全速狂奔”的危险行为。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "社会化抚养绝非明智的选择。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会化抚养只能作为家庭抚养失败后不得已的补充，不可以作为一种进取性的策略。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述一种主张：只搞有限的社会化抚养，只抚养父母显然不合格、家庭显然失败者，并由政府积极、周期性地检查家庭是否成功，一旦判定失败即将其子女纳入社会化抚养。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种设想是想用有限化救赎“社会化抚养”这个概念。", "evidence": ["E17"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者表示毫不怀疑这样会有巨大的综合效益。", "evidence": ["E19"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰因为会存在巨大的综合效益，它才万万不可行。", "evidence": ["E20"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为效益的直接受益者是作出判定的实体本身；该判定者将在实践层面事实上拥有拆开任何目标家庭、猎取它所钟意的“人力资源”的权力。", "evidence": ["E21"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判定标准无法固定：提高失败家庭的标准即可多取优秀苗子，因此“金牌数量够了”“禁卫军够强”“好帮手够多”“失败家庭的红线够合理”都没有确定答案。", "evidence": ["E22", "E23"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰是“收益巨大”，所以才危险，且绝对不可行。", "evidence": ["E24"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会化抚养必须绝对遵循谦抑原则：民不举、官不究，发动端绝不能放在政府一方，举报人绝不能以任何方式受益。", "evidence": ["E25"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "否则天下生民恐无噍类矣（作者对后果的严重预警）。", "evidence": ["E26"]}
   ],
   "argument_steps": [
    "先立第一点：社会化抚养抑制思想多样性，并以克隆单一品种、香蕉单一化风险作类比（P001-P003）。",
    "立第二点：对“落后者”不公正，评价体系须多维化而社会化抚养给不出维度（P004-P005）。",
    "举斯巴达为实例，说明只培养战士时掉队者被淘汰，并反问能否提供多个“系”与重选机会（P006-P008）。",
    "立第三点：该顺序对应紧迫而明确的社会困境，并举以色列、普鲁士、苏联（P009）。",
    "论证紧迫性有期限，到期后旧精锐不适用新问题，陷入惯性危机（P010-P011）。",
    "以冰海邮轮比喻说明转向滞后与损失不可避免，进而给出平时慢速、危机全马力、危机后退出舵轮的行动模式（P012-P014）。",
    "小结：社会化抚养属“前进四”级措施，绝非明智，只能是失败后的补充而非进取策略（P015-P017）。",
    "“补充一条”：转述有限社会化抚养的设想，指出其为用有限化救赎概念（P018-P021）。",
    "承认其综合效益巨大，随后论证正因效益大、受益者为判定实体本身，才绝对不可行（P022-P024）。",
    "以模拟判定者口吻与连续反问说明标准无法固定（P025-P029）。",
    "重申收益巨大故危险且绝对不可行，并给出谦抑原则的行动边界与后果预警（P030-P032）。"
   ],
   "concept_usage": [
    {"term": "社会化抚养", "meaning": "由社会（政府）承担抚养的主张；作者区分“进取性策略”“家庭抚养失败后的补充”与“有限而积极的社会化抚养”三种用法。", "evidence": "P017", "ambiguity": "正文未点名马前卒，也未给出该主张的完整定义，讨论对象以“社会化抚养”一词为准。"},
    {"term": "思想多样性／生物多样性", "meaning": "以品种克隆、香蕉单一化的生物多样性风险比喻思想同质化。", "evidence": "P002", "ambiguity": "思想多样性与生物多样性之间的类比未被论证。"},
    {"term": "谦抑原则", "meaning": "作者主张的行动边界：民不举、官不究，发动端不在政府，举报人不得受益。", "evidence": "P031", "ambiguity": "未说明该原则的适用范围是否仅限社会化抚养。"},
    {"term": "前进四", "meaning": "借用来指最高强度的加速措施；作者称社会化抚养属于该级别。", "evidence": "P015", "ambiguity": "文中未解释该词来源与确切含义。"},
    {"term": "自然淘汰", "meaning": "引号使用，指斯巴达式教育中对不合格者的淘汰。", "evidence": "P006", "ambiguity": "引号表明作者在转述该逻辑而非认同。"}
   ],
   "examples_and_targets": [
    "马前卒的社会化抚养主张：提问所指的评论对象，正文未点名（Q001）。",
    "香蕉濒临灭绝、一场感冒亏掉底裤：作者类比材料（P003）。",
    "斯巴达人、战士教育、二十公里负重跑：作者例证（P006）。",
    "数学学校、文学系战地记者、音乐系吹号：作者假设的替代“系”（P007）。",
    "以色列要求生存、普鲁士谋求德意志统一、苏联快速工业化：作者例证（P009）。",
    "冰海巨型邮轮、撞冰山、右满舵、70%碰撞进程：作者比喻与估计（P012）。",
    "奥运金牌、禁卫军、好帮手、家庭调查的调查员：作者模拟判定者动机的设想（P025-P026）。"
   ],
   "conditions": [
    "第三点以“必然对应了一种紧迫而明确的社会困境”为前提，并强调这种紧迫性与明确性“是有期限的”（P009-P010）。",
    "对“一个并非处在明确的存亡危机的巨型国家”这一前提作判断（P015）。",
    "“补充一条”整段限定在“有限而积极的社会化抚养”这一变体（P019-P020）。",
    "作者自陈不怀疑其综合效益，否定理由落在风险与权力归属而非效益（P022-P023）。",
    "结尾以“必须绝对遵循谦抑原则”为行动条件，并以“否则”给出后果（P031-P032）。"
   ],
   "rhetoric_and_tone": "分点编号推进（第一/第二/第三/补充一条/第四）；密集反问（P008、P027、P028、P029）；以第一人称模拟判定者口吻的反讽段落（P025-P026）；多重比喻（克隆品种、香蕉、邮轮、前进四）；结尾用文言句式加重语气。",
   "unresolved_questions": [
    "正文未点名“马前卒”，评论对象是否与提问所指的主张完全一致，需核对原主张（Q001）。",
    "“前进四”未在文中说明来源（疑为科幻作品用语），需外部核查（P015）。",
    "斯巴达、以色列、普鲁士、苏联的历史叙述未给依据，需外部核查（P006、P009）。",
    "“70%碰撞进程”“少挨最后的百分之十”为比喻中的估计，无数据来源（P012）。",
    "正文嵌入英文词“power”未加解释（P024）。",
    "P018“补充一条：”后接第四点，编号体例与前三点的“第一/第二/第三”不完全一致，属作者自述的结构安排（P018-P019）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "第一，“社会化抚养”会从根上抑制社会成员的思想多样性。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "用优选优育去除“令人不快”的生物多样性", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一场感冒，亏掉底裤：香蕉濒临灭绝，我们以后还有香蕉吃吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "第二，社会化抚养对“落后者”存在无法交代的不公正。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而“社会化抚养”不可能提供足够的维度。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "斯巴达人就是社会化抚养，因为他们拿定了主意只要战士。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "但你能提供多少个系呢？你能给人多少次重选的机会呢？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "这个从第一个不行到最后一个不行的顺序必然对应了一种紧迫而明确的社会困境", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你会发现你原有的巨大的人力投资造就的最精锐的成果在新的问题面前并不适用", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "到那时你连稍微在碰撞前抓住最近的栏杆的机会其实都没有了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这时的人类社会就像一艘在冰海里行驶的巨型邮轮", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "只能是平时就慢速行进", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "政府就要离开舵轮和油门，珍惜和重建自己的信用，以便用作下一次危机干预。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "“社会化抚养”绝对是属于“前进四”级别的措施", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "绝非明智的选择。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "社会化抚养只能作为家庭抚养失败后不得已的补充，不可以作为一种进取性的策略。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "这个是想用有限化救赎社会化抚养这个概念。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "只抚养那些父母显然不合格的，家庭显然失败的", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "我毫不怀疑这样会有巨大的综合效益。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "但恰恰是因为这样会存在巨大的综合效益，它才万万不可行！", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "这个判定者将在实践层面上事实的拥有拆开任何目标家庭，猎取它所钟意的“人力资源”的power。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "我就提高失败家庭的标准，多弄点优秀的好苗子来。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P028", "quote": "所以什么叫“失败家庭的红线够合理”？", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P030", "quote": "恰恰是“收益巨大”，所以才危险，且绝对不可行。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P031", "quote": "社会化抚养必须绝对遵循谦抑原则，民不举、官不究，发动端绝不能放在政府一方，且举报人绝不能以任何方式受益。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P032", "quote": "否则天下生民恐无噍类矣。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P018", "quote": "补充一条：", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会政策评论", "教育与社会化", "政治哲学/国家权力边界"],
   "issue_candidates": ["社会化抚养的可行性", "思想多样性与单一评价体系", "紧迫社会困境与人力投资惯性", "政府干预家庭的权力风险", "谦抑原则"],
   "text_function_candidates": ["答疑", "论辩", "批评", "政策评论"],
   "object_candidates": ["马前卒（提问所指，正文未点名）", "斯巴达人", "以色列", "普鲁士", "苏联", "政府", "家庭", "判定者/调查员"],
   "working_keywords": ["社会化抚养", "思想多样性", "评价体系多维化", "自然淘汰", "前进四", "谦抑原则", "民不举、官不究", "人力资源"]
  },
  "notes": "无图片节点；正文32段（含1个 heading 段落 P032）全部读完。C015 为作者转述他人（“很多人想说”）的设想，已标 author_reported／attribution=unknown，未归为作者主张；C023 为文言式后果预警，保留 predicted 语气。"
 },
 "de0e5722": {
  "analysis": {
   "question_context": "提问者问如何看待刘银川穿越无人区失踪（Q001）。作者未评论该事件本身，而是针对流行的极限运动逻辑表态：以设定极限目标来证明自己强大的做法不成立，并区分了基于公共福利的冒险与出于私利的冒险，进而给出“不阻止但停止追捧”的行动建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "表态：不赞成现在流行的极限运动基本逻辑——设定极限目标以证明自己强大。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "提出“基于勇气”的条件：为公共福利、危险不可回避地冒生命危险。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "判定出于“证明自己”“征服快感”“人生意义”或包装过的私利者，有多勇敢就有多贪婪。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "区分责怪对象：不怪不明白的年轻人，怪鼓吹“酷炫”“牛x”“偶像”的世界；以角斗士作比。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "提出判准：只有为了他人，人才有迎着风险逆行的正当性；荣耀仅属于为他人而战的人。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011"], "summary": "行动建议：停止追捧与鼓吹，但不必阻止；并给出夸张式收尾。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不赞成现在流行的一种极限运动的基本逻辑——设定一个极限的目标，用来证明自己的强大。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若为救人或其他建设性理想（架桥、堵涌口、救战友、筹善款直播）而不得不挑战极限，为创造公共福利冒生命危险且危险不可回避，这件事才真的是基于勇气。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若是为了“证明自己”“征服的快感”“寻找人生的意义”或用美好说法包装的私利，那么有多“勇敢”就有多贪婪。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "归根到底，这只是惊人的贪婪。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不责怪这样做的年轻人（因为ta们并不明白），而责怪鼓吹“酷炫”“牛x”“偶像”的世界。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "角斗士没有勇气，亦无荣耀，只是欲望的奴隶和人言的囚徒。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有为了他人，人才有迎着风险逆行的正当性。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "荣耀属于——而且仅仅只属于——为他人而战的人。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应停止跟风追捧那些仅为自我满足而行的冒险行为；不必阻止（那的确是人的自由），但要停止追捧和鼓吹，不抢购角斗场的门票，不崇拜角斗士。", "evidence": ["E11", "E12"]}
   ],
   "argument_steps": [
    "先表态不赞成流行极限运动的基本逻辑（P001）。",
    "给出“基于勇气”的判准及条件：为公共福利且危险不可回避（P002）。",
    "反向列举出于自我证明或包装过的私利的动机，判为贪婪（P003-P004）。",
    "修正责怪对象：不怪年轻人，怪鼓吹的世界；以角斗士作比（P005-P006）。",
    "提出正当性与荣耀的判准：为他人（P007-P008）。",
    "给出行动建议：不阻止但停止追捧与鼓吹（P009-P010）。",
    "以夸张口语作结（P011）。"
   ],
   "concept_usage": [
    {"term": "勇气", "meaning": "仅指为公共福利、危险不可回避地冒险；出于自我证明的冒险不算勇气。", "evidence": "P002", "ambiguity": "作者未界定“建设性的理想”与“公共的福利”的判准。"},
    {"term": "贪婪", "meaning": "作者对以冒险求自我满足者的定性，与“勇敢”构成反比关系。", "evidence": "P003", "ambiguity": "未说明贪婪与正当私利的界线。"},
    {"term": "角斗士", "meaning": "比喻被欲望和他人言论驱使、并无勇气与荣耀的冒险者。", "evidence": "P006", "ambiguity": "比喻是否涵盖所有商业化的极限运动，未说明。"},
    {"term": "人言的囚徒", "meaning": "指被他人评价与喝彩所支配。", "evidence": "P006", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "刘银川穿越无人区失踪：提问所指事件，正文未提及（Q001）。",
    "在峡谷之间架桥、堵住将溃的涌口、从绝望的包围中拯救战友、为筹集善款而直播挑战：作者举的正当冒险例（P002）。",
    "角斗士、角斗场的门票：作者比喻材料（P006、P010）。",
    "鼓吹“酷炫”“牛x”“偶像”的世界：作者的主要批评对象（P005）。"
   ],
   "conditions": [
    "“如果你为了救人或者为了别的什么建设性的理想不得不挑战某种极限”为条件（P002）。",
    "“且这危险的确是不能不直面、无法回避的”为附加条件（P002）。",
    "“如果你是为了‘证明自己’……”构成反向假设条件（P003）。",
    "“不必阻止，因为那的确是人的自由”划出不干预的边界（P009）。"
   ],
   "rhetoric_and_tone": "道德训诫语气；第二人称“你”呼告；勇气/贪婪的二元对照；“ta们”的性别中立写法；结尾“如果是你的崽子，打断ta的狗腿”为夸张戏谑，不宜按字面主张处理。",
   "unresolved_questions": [
    "刘银川事件的时间、经过与结论未在正文说明，需外部核查（Q001）。",
    "正文未点名刘银川，也未讨论该事件本身（Q001、P001-P011）。",
    "“建设性的理想”“公共的福利”的具体判准未给出，正当与不正当冒险的边界仍不明确（P002）。",
    "末句“打断ta的狗腿”属夸张修辞，是否为字面行动建议存疑（P011）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我很不赞成现在流行的一种极限运动的基本逻辑", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "设定一个极限的目标，用来证明自己的强大", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "是为了创造某种公共的福利而冒生命的危险", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "那么这件事你才真的是基于勇气。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "那么你有多“勇敢”，你就有多贪婪。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "归根到底，这只是惊人的贪婪。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "我不责怪这样做的年轻人，因为ta们并不明白，我责怪鼓吹“酷炫”“牛x”“偶像”的世界。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "角斗士没有勇气，亦无荣耀，只是欲望的奴隶和人言的囚徒。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "只有为了ta人，人才有迎着风险逆行的正当性。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "荣耀属于——而且仅仅只属于——为ta人而战的人。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "但你要停止追捧和鼓吹。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "不要抢购角斗场的门票，不要崇拜角斗士。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "如果是你的崽子，打断ta的狗腿。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理/价值评论", "极限运动与社会风气", "公共评论"],
   "issue_candidates": ["冒生命危险的正当性", "自我证明式冒险", "对冒险者的追捧与鼓吹责任"],
   "text_function_candidates": ["答疑", "评论", "训诫"],
   "object_candidates": ["刘银川（提问所指，正文未提及）", "年轻人", "角斗士", "鼓吹酷炫牛x偶像的世界"],
   "working_keywords": ["极限运动", "勇气", "贪婪", "公共的福利", "角斗士", "自我满足"]
  },
  "notes": "无图片节点；正文11段全部读完。正文未涉及刘银川事件本身，作者讨论的是一般化的极限运动逻辑；末段夸张表述已在未决问题中标注，不作为字面主张。"
 },
 "4c8d70b4": {
  "analysis": {
   "question_context": "提问者问“政治是什么？”（Q001），请求给出定义。作者以一副对句作答，把“政治”拆为“政”与“治”两个环节，全文仅19字，无展开论证、举例或条件说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以对句分别定义“政”（对应然的博弈）与“治”（对结果的实践），合为对“政治”的拆解式定义。", "role": "definition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“政”是对应然的博弈。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“治”是对结果的实践。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“政治”在本文中被拆为两个环节：对“应然”的博弈（政）与对“结果”的实践（治）。", "evidence": ["E1", "E2"]}
   ],
   "argument_steps": [
    "以对句形式先给出“政”的定义（P001）。",
    "再给出“治”的定义（P002），二者并置构成对“政治”的拆分式回答；本文未作进一步论证或举例。"
   ],
   "concept_usage": [
    {"term": "政", "meaning": "对“应然”的博弈，即围绕应然之事的角力。", "evidence": "P001", "ambiguity": "未说明博弈的主体、场域与规则。"},
    {"term": "治", "meaning": "对“结果”的实践，即面向结果的行事。", "evidence": "P002", "ambiguity": "未说明实践的主体与范围。"},
    {"term": "应然", "meaning": "与“结果”相对的一侧，指应当如何的层面。", "evidence": "P001", "ambiguity": "未说明应然的判定依据。"},
    {"term": "政治", "meaning": "由“政”与“治”两环节合成的概念，本文未再给出统一界说。", "evidence": "P001", "ambiguity": "两环节的关系（先后、并列或循环）未说明。"}
   ],
   "examples_and_targets": [
    "本文未给出任何例子、人物、事件、机构或数据。"
   ],
   "conditions": [
    "本文未说明该定义的适用对象、场景、时间或条件，亦无限定词。"
   ],
   "rhetoric_and_tone": "极简对句（格言体），文言式判断句，两句字数与结构对仗；无展开、无修辞性反问，语气为下定义式的平静陈述。",
   "unresolved_questions": [
    "全文仅19字，未说明“应然”的判定主体、“博弈”的场域与“实践”的范围，定义的具体所指不确定（P001-P002）。",
    "未说明该定义与通行政治学定义的关系，也未给出理由或例证（P001-P002）。",
    "“政”与“治”的关系（时间先后、手段与目的、并列还是循环）未说明（P001-P002）。",
    "是否有后续补充或展开未知（正文两段即止）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "对应然的博弈为政，", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "对结果的实践为治。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治理论/概念界定"],
   "issue_candidates": ["政治的定义", "政与治的区分", "应然与结果"],
   "text_function_candidates": ["答疑", "定义"],
   "object_candidates": ["unknown（文中无具体对象）"],
   "working_keywords": ["政", "治", "应然", "实践", "博弈"]
  },
  "notes": "无图片节点；正文仅2段共19字，已全部读完。全文为对句定义，无展开论证与例证；未决问题登记了定义所指的不确定性，未据标题或提问补写含义。"
 },
 "aa50fc78": {
  "analysis": {
   "question_context": "提问者问如何确定你真正想做的事情到底是什么（Q001）。作者不直接给识别方法，而是先剖析“标准奋斗模型”（选定目标—延迟享受—忍受痛苦）为何制造出这个折磨人的问题，指出换事业而不换模型无法解决，再把问题来源追溯到民族长征叙事经父母传导的精神副效应，最后给出两层替代策略，并声明正文未完待续。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "描述“标准的奋斗模型”及其要害：若最终目标不给过程快感反馈，人就会持续怀疑痛苦能否兑换终极满足。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "模型的脆弱性：万一选错则忍受纯属无谓损失；且既有成功也抵消不了“确实可能失败”的阴影。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "父母人为塑造“延迟享受”体验（布置困难＋末尾赏赐）并自认是教育；作者判定这不能解决问题，反使怀疑与自我厌恶加剧、能量耗竭、进展停滞的循环。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "以“是不是我真正想做的”作为将放弃合法化的出口；作者称答案不重要，不换模型只会重来，错的是模式而非那件事。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030"], "summary": "追溯模型来源为民族长征叙事的副效应；声明民族长征本身不是错的模型，但只适用于当时情境而非现在的普通人；不责怪父母。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "替代策略第一层：从价值观层面重新考虑一生追求的价值，属慢方子，通常须三四十岁有阅历后才能做。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043"], "summary": "第二层：学习欣赏和享受困难本身，建立更强健的快感机制与对“可用的困难”的鉴赏力，从而不再问“适不适合我”。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P044", "P045", "P046"], "summary": "结论：把问题转化为“哪些事情值得拼死一做”和“如何最深最好地享受正确的困难”，此处才是痛苦的出路；文末注明未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述“标准的奋斗模型”：选择一个自己喜欢的事情，牢记初心，把路上困难看作获取最后欢愉必须忍受的代价，延迟享受、不断奋斗直到如愿以偿。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该模型的要害在于：若选定的最终目标未在过程中给予足够快感反馈，人就会一直怀疑现在忍受的痛苦将来能否兑换成终极满足。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "万一所选的路不是注定该做、适合做、有真实前途或能做成的事，那么忍受痛苦与延迟享受最后会转化为纯粹无谓的损失。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "模型更脆弱之处：即使曾有过具体成功经验，只要也同样失败过，成功就抵消不了“确实也有可能会失败”的阴影。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多父母通过人为操纵培养子女“延迟享受可以获得更大快乐”的体验（布置困难、末尾赏赐冰激凌玩具枪与迪斯尼之旅），并多多少少深信这就是“教育”。", "evidence": ["E6", "E35"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明：这个教育本质的问题不是本文主题，另作讨论。", "evidence": ["E29"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这种人为安排不能解决问题：它抑制不了折磨人的自我怀疑，反而增加怀疑的威力，在游移不定之上额外加上下意识生出的自我厌恶。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "怀疑消耗能量，自我咒骂与自我辩解再放大数倍消耗；能量耗尽则事情事实上没有令人鼓舞的进展，而没有进展又刺激出更深的怀疑与对自我怀疑的痛恨。", "evidence": ["E9", "E36"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人于是转向另一个可将放弃合法化的出口——“我是不是不适合做这个”；只有事情本身是错的，其动摇和“贪图享乐”才不可耻。", "evidence": ["E10", "E31"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这个问题的答案并不重要：换了另一个事业而模型没变，只争取到半年左右喘息期，一切将会卷土重来，下下次甚至半年都没有。", "evidence": ["E11", "E12", "E37"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "你不可能通过“找到真正想做的事情”来解决这个问题。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为错的根本就不是它，它只是一个错误模式的耗材。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "它只是慌乱父母被大叙事无意中传染的一种精神副效应——因为这些父母成长时，中国正处在卧薪尝胆、百年生聚的民族长征状态。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明不是在说民族长征本身是错误的模型：对亿万人口、救亡图存目标明确的民族而言，延迟享受、追求幸存的目标是清晰、现实、无臆测的。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "该模型的问题在于：它对民族以及同样面临亡国灭种危机的民族成员成立，但并不适用于现在的普通人。", "evidence": ["E17"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在每天都有新战事、大屠杀、大饥荒的时代，为不被屠杀奴役而延迟享受没什么好犹疑（除非生活在繁华而远离战火的大都市）；但在和平年代，为一个上市后不知能否被接受的新产品、不知能开多久的企业、不知会否被结构性淘汰的职位忍受痛苦，是另一回事。", "evidence": ["E40", "E18"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以也不要责怪父母——责怪的能量本身也是损失。", "evidence": ["E19"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "替代策略有两层；第一层是从自己的价值观层面重新考虑一生追求的价值应该是什么。", "evidence": ["E33"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "第一层是慢方子：这其实是三四十岁有足够阅历之后才有能力真正去做的事情；在这之前人将不可避免按照被环境写入的价值观行事。", "evidence": ["E20", "E38"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二层技术性地说是学习欣赏和享受困难本身：不要与快感为敌，但要建立起更强健的快感机制。", "evidence": ["E21", "E22"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要像用“闻过则喜”击败对批评的恐惧那样建立对“困难”的新感情：先学会鉴别何谓可用、何谓不可用的困难，再对“可用的困难”建立新的鉴赏机制。", "evidence": ["E39", "E23"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要害是培养识别哪些酸、苦、辣有毒、哪些不但无毒而且有益的能力，然后对有益者不是忍受而是学会品鉴和欣赏。", "evidence": ["E24"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这才真的将人解放出来：并无所谓“什么事情是你真正想做的”这种概念，而是世界上有一些幸运的困难，任何一种都值得好好品尝。", "evidence": ["E25"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "人遗憾的将是人生有限，没机会把它们都尝遍，某些东西只能浅尝辄止。", "evidence": ["E32"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“如何知道我真正想做的是什么”这个无答案的问题，只有转化为“哪些事情是值得拼死一做的”和“如何最深最好的享受正确的困难”，才会有想要的答案。", "evidence": ["E26"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里才是驱使你问这问题的痛苦的出路。", "evidence": ["E27"]},
    {"claim_id": "C027", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者自问：要害在于不走这个模型，替代的策略是什么？", "evidence": ["E30"]}
   ],
   "argument_steps": [
    "先转述“标准的奋斗模型”的构成（P001）。",
    "指出其要害：过程缺乏快感反馈即产生“能否兑换终极满足”的怀疑（P002-P003）。",
    "列出模型的脆弱性：选错即无谓损失；成功经验抵消不了失败的阴影（P004-P006）。",
    "描述父母人为塑造延迟享受体验的做法与自认的“教育”（P007-P009）。",
    "声明教育本质问题不属本文主题，收窄论域（P010-P011）。",
    "回答“能不能解决问题”：不能，反使怀疑加剧并叠加自我厌恶，形成能量耗竭与进展停滞的循环（P012-P015）。",
    "指出“我是不是不适合／不是我真正想做的”是放弃合法化的出口（P016-P018）。",
    "论证答案不重要：不换模型只得到约半年喘息，一切将重来；错的是模式而非那件事（P019-P024）。",
    "追溯来源为民族长征叙事经慌乱父母传导的精神副效应，并限定该模型对民族曾经成立、对现在普通人不适用；不责怪父母（P025-P030）。",
    "给出替代策略第一层：价值观层面的重新考虑，并说明其为慢方子（P031-P034）。",
    "给出第二层：学习欣赏困难本身、鉴别可用与不可用的困难、建立对有益之苦的鉴赏力（P035-P043）。",
    "结论：问题须转化为“值得拼死一做的”与“如何享受正确的困难”，此处才是出路（P044-P045）。"
   ],
   "concept_usage": [
    {"term": "标准的奋斗模型／模型", "meaning": "指“设定最终目标—延迟享受—忍受痛苦—期待终极满足”的策略；作者称其为错误模式。", "evidence": "P001", "ambiguity": "“模型”在文中兼指策略与心态模式，未给出严格界定。"},
    {"term": "真正想做的事", "meaning": "作者认为该概念并无所谓，是一个无答案的问题，被用作放弃的合法化出口。", "evidence": "P042", "ambiguity": "作者既否定该概念，又主张把它转化为“值得拼死一做的”，两者的关系未细说。"},
    {"term": "快感机制", "meaning": "指人对快感的获取与感受结构，作者主张不应与之敌对而应使其更强健。", "evidence": "P036", "ambiguity": "未说明该机制如何训练。"},
    {"term": "可用的困难／不可用的困难", "meaning": "作者主张需先鉴别困难是否有益，再对可用者建立鉴赏机制。", "evidence": "P038", "ambiguity": "未给出鉴别标准的具体判据。"},
    {"term": "正确的困难", "meaning": "值得拼死一做、应最深最好地享受的困难。", "evidence": "P044", "ambiguity": "与“可用的困难”是否同义未说明。"},
    {"term": "民族长征", "meaning": "指中国救亡图存、百年生聚的历史状态，作者称其目标对当时情境清晰而现实。", "evidence": "P025", "ambiguity": "未给出史料依据，属作者的历史叙述。"},
    {"term": "耗材", "meaning": "指某件具体事业只是错误模式的消耗品，本身并非错误所在。", "evidence": "P024", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "冰激凌、玩具枪、迪斯尼之旅：父母赏赐的举例（P008，作者例证）。",
    "上市后不知会不会被市场接受的新产品、不知能开多久的企业、不知会否被结构性淘汰的职位：和平年代的举例（P029，作者例证）。",
    "每天都有新战事、隔三差五出现大屠杀、大饥荒的时代：作为对照的历史情境（P028，作者叙述）。",
    "“闻过则喜”：成语类比（P037，类比材料）。",
    "咖啡、麻辣火锅、蘸醋吃饺子与蛋糕、果汁：味觉类比（P040，类比材料）。",
    "辣椒、咖啡：承接类比的举例（P041，修辞材料）。",
    "父母：被作者明确列为不责怪的对象（P030）。"
   ],
   "conditions": [
    "对模型的批评以“如果你选择的这个‘最终目标’没有在过程中给予你足够的快感反馈”为条件（P002）。",
    "“万一我所选择的路不是我注定该做的事 / 适合我做的事 / 有真实前途的事 / 能做成的事”为假设条件（P004）。",
    "民族长征模型的适用边界：对民族及面临亡国灭种危机的成员成立，不适用于现在的普通人（P026-P027）。",
    "第一层策略的时间条件：“三四十岁有足够阅历之后才有能力真正去做”；此前“将不可避免的按照自己被环境写入的价值观行事（这在很大程度上取决于父母的教育）”（P034）。",
    "结尾注明“（未完，待续）”，本文论述未完结（P046）。"
   ],
   "rhetoric_and_tone": "第二人称“你”贯穿的分析—劝解语气；密集设问与自问自答（P003、P006、P011、P016、P018、P023、P031）；口语插注“（废话，人又不是傻瓜，眼睁睁的怀疑怎么强行否定？）”（P012）；以酸、苦、辣、咖啡、火锅等味觉比喻作结；文末以括号注明未完待续。",
   "unresolved_questions": [
    "文末注明“（未完，待续）”（P046），本文论述未完结，后续内容不在本记录范围内。",
    "第一层“从自己的价值观层面重新考虑”未给出具体方法，作者自承是慢方子、须三四十岁后才可做（P033-P034）。",
    "“民族长征”作为精神状态来源的论断未给史料或传导机制说明，属需外部核查的历史叙述（P025-P026）。",
    "“可用的困难”的鉴别标准未说明如何得出（P038）。",
    "作者既否定“真正想做的事”这一概念，又主张把问题转化为“值得拼死一做的”，两者关系存在解释空间（P042、P044）。",
    "P010-P011 声明教育本质问题另谈，本文未展开（P010）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "标准的奋斗模型是这样的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "延迟享受、不断奋斗，直到如愿以偿，赢取最后的胜利。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "你就会一直在想——我现在忍受的痛苦真的在将来可以兑换成终极满足吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "岂不是最后会转化为纯粹无谓的损失吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "只要它也同样失败过，那么这些成功也抵消不了它“确实也有可能会失败”的阴影。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "赏赐ta做梦也想不到的冰激凌、玩具枪和迪斯尼之旅", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "不能，这抑制不了这种折磨人的自我怀疑的产生", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "只会反而增加这些怀疑的威力", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "这些能量耗尽了，事情在事实上就的确没有令人鼓舞的进展。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "人就要转向另一个可以将放弃合法化的出口", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "其实这个问题的答案并不重要。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "你只不过争取到了半年左右的喘息期而已。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "你不可能通过“找到真正想做的事情”来解决这个问题。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "因为错的根本就不是它，它只是一个错误模式的耗材。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "它只是自己生养时也对人生的总体策略并无通透思考的慌乱的父母们被大叙事所无意中传染的一种精神副效应", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "我不是在说民族长征本身是错误的模型", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P027", "quote": "但却并不适用于现在的普通人。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P029", "quote": "这是另一回事。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P030", "quote": "所以也不要去责怪父母——责怪的能量本身也是损失。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "但这是一个慢方子", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P035", "quote": "是学习欣赏和享受困难本身。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P036", "quote": "也就是不要与快感为敌，但要建立起更强健的快感机制。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "首先学会鉴别何谓可用的困难、何谓不可用的困难的鉴定方法", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P039", "quote": "你的要害是要培养出“识别哪些酸、苦、辣是有毒的，哪些不但无毒而且有益”的能力", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P042", "quote": "并无所谓“什么事情是你真正想做的”这种概念", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P044", "quote": "只有转化为“哪些事情是值得拼死一做的”，和“如何最深最好的享受正确的困难”，才会有你想要的答案。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P045", "quote": "这里才是驱使你问这问题的痛苦的出路。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P046", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E29", "paragraph_id": "P010", "quote": "不过这个教育本质的问题，不是这里的主题，我们另外再谈。", "relation": "context"},
    {"key": "E30", "paragraph_id": "P031", "quote": "要害在于不走这个模型，替代的策略是什么？", "relation": "context"},
    {"key": "E31", "paragraph_id": "P017", "quote": "只有事情本身是错的，我的动摇和“贪图享乐”才不会是可耻的。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P043", "quote": "你遗憾的将是人生有限", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P033", "quote": "第一层，是从自己的价值观层面重新考虑自己一生追求的价值应该是什么。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P012", "quote": "（废话，人又不是傻瓜，眼睁睁的怀疑怎么强行否定？）", "relation": "context"},
    {"key": "E35", "paragraph_id": "P009", "quote": "ta们或多或少的深信，这就是“教育”。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P015", "quote": "而事情没有进展，本身又刺激出更深的怀疑和对自我怀疑的痛恨。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P021", "quote": "一切将会卷土重来。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P034", "quote": "这其实是三四十岁有足够阅历之后才有能力真正去做的事情。", "relation": "qualifies"},
    {"key": "E39", "paragraph_id": "P037", "quote": "你要像用“闻过则喜”来击败对批评的恐惧那样，建立起对“困难”的新的感情。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P028", "quote": "在每天都有新战事、隔三差五出现大屠杀、大饥荒的时代", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与人生策略", "教育/家庭教育", "社会心态史", "价值观评论"],
   "issue_candidates": ["如何确定真正想做的事", "延迟享受模型的问题", "父母的延迟满足训练", "自我怀疑与放弃的合法化", "民族叙事对个体心态的影响", "对困难的鉴赏力"],
   "text_function_candidates": ["答疑", "解释", "评论", "经验总结"],
   "object_candidates": ["父母", "子女", "中国（民族长征时期）", "普通人", "企业/新产品/职位"],
   "working_keywords": ["标准奋斗模型", "延迟享受", "真正想做的事", "快感机制", "可用的困难", "正确的困难", "民族长征", "耗材"]
  },
  "notes": "无图片节点；正文46段全部读完（末段为括号注“（未完，待续）”，作者自述未完结，已在未决问题登记）。C001 为作者转述的流行模型，标 author_reported／attribution=unknown；C014 为作者对可能误读的自我澄清（否定式），按原语气记录。"
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
