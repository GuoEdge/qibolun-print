# -*- coding: utf-8 -*-
"""批次 r001-b0421 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0421.sessions.py            # 写 out/r001-b0421.out.jsonl
  python3 records/r001-b0421.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import autofill_empty_analysis, build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0421"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0421.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "eff96e11": {
  "analysis": {
   "question_context": "提问者问如何看待“如果严格执行劳动法，会有很多企业活不下去，发生大规模裁员”这种说法；作者直接否定该说法，并给出自己的因果解释与延伸论述（劳动者面对的不是裁员，而是绕过劳动法的用工形式，以及社会文化层面的压力）。提问者的说法为被反驳对象，不代表作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "否定该说法；认为真实后果是劳务派遣公司、极小微型企业、平台从业被算作自雇、自愿加班等合法绕过劳动时间限制的形式。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013"], "summary": "劳动焦虑的根源不在资本家压榨，而在中国社会总体价值观逻辑；躺平在物质上可行，但会遭社会道德惩罚与关系压力；这种安排融在汉语里。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "汉语文化中没有歌颂躺平的语料与作品；文艺产品本身也是奋斗者生产出来的。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "亲友关心无法用隐私隔绝；这些社会支柱会变成情绪能量的没收者，最终心灰意冷、恩断义绝。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "该文化机制能把人力资源发挥到极限、免疫消极思想，是祝福也是诅咒（少数人可能撑住考验）。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "以历史强敌与假设（危急关头几十万人躺平则不再说汉语）说明躺平战术在中国难以玩通。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P034", "P035"], "summary": "解决劳动强度问题只有一条路：支持国家开疆拓土、自强不息，夺回定价权与更广阔的就业市场。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P036", "P037", "P038"], "summary": "中国文化设计的快感机制与社会奖励都建立在积极主动发光发热上，因此躺平想开看破超脱都是扯淡。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043"], "summary": "劳动法的目的不是安逸生活而是让工作与生活两头努力；力竭不可避免，区别只在力竭、气竭还是心竭；结尾以反问收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“严格执行劳动法会导致很多企业活不下去、发生大规模裁员”这种说法是不正确的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "真正会出现的后果是大量劳务派遣公司和极小的微型企业，以合法方式突破劳动时间的硬性限制。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作为参考，美国出现了“一个人做三份工，每份都不超时，加起来一天12-16小时”的现象。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "政策会把开网约车、送快递、签约MCN直播、网店在线客服等新业态算作自雇，其与平台约定的服务时间属商业合同交易，不适用劳动法保护。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此外还有大量“自愿加班”“把活带回家里做”的形式。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "造成威胁健康与可持续性的劳动焦虑的根本不是“资本家的残酷压榨”，而是中国社会的总体价值观逻辑。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在房产持有硬成本几乎为零、食物原料与基本信息服务、基本医疗极便宜且储蓄率超高的前提下，安于躺平完全可以做到，门槛并不高。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若真的躺平，基本上会被社会处以道德极刑：配偶/恋人、朋友、父母、亲戚会疏远。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这种安排不是政府的阴谋，也不是资本家的压榨，而是几千年盛衰兴亡、生离死别凝聚出的生存本能。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人能用汉语有效证明“躺平也挺好的”，相关安慰话语很快会循环用尽。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国社会不支持人用隐私隔绝亲友关心；这种关心会成为躺平者的巨大困扰，并把本应提供支持的支柱关系变成情绪能量的没收者。", "evidence": ["E11", "E12"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "不排除有部分人凭运气和能力撑住这种考验，但该文化机制保证中华民族能把人力资源发挥到极限，几乎免疫于一切消极思想。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能把每一分人力从消极厌世思想侵蚀中夺回的“魔法”是最大的祝福之一，而所有祝福同时是诅咒。", "evidence": ["E14", "E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若在最危急关头多上百万甚至几十万人躺平，现在人们说的就不会是汉语。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "别的国家或文明或许能玩通“都躺平让资本家没人用”的战术，但在中国不好说绝对不可能，劝人不要太期待。", "evidence": ["E17"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在中国解决“劳动强度”问题只有一条路：支持国家在经济外交上开疆拓土、内政上追求伟大梦想、军事上自强不息，夺回公平的定价权和远比现在广阔的就业市场。", "evidence": ["E18", "E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国文化设计的快感机制与社会奖励都建立在积极主动发光发热的态度上，所以躺平、想开、看破、悟透、超脱都是扯淡。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "劳动法不是为了让劳动者“安逸生活”，而是让人在努力工作之外还能努力生活。", "evidence": ["E21"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每天力竭不可避免，区别只在带着家人祝福的力竭、受批评惩罚的气竭、或在悔恨羞耻迷茫中耗尽的心竭。", "evidence": ["E22"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：在中国不会出现“严格执行劳动法，企业就会大面积倒闭”的情况。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "先否定提问中的说法（P001）。",
    "给出替代因果：企业会以劳务派遣、极小微型企业、平台从业者算自雇等方式合法绕过工时硬限制（P002、P004），并补充自愿加班、把活带回家（P005）。",
    "举美国一人打三份工的现成例证作为参考（P003）。",
    "转移问题层次：劳动焦虑的真正根源不是资本家压榨，而是中国社会的总体价值观逻辑（P006）。",
    "设立条件性前提：房产硬成本近零、基本生活与医疗便宜、储蓄率高，故躺平在物质上可行（P007）。",
    "以假设推进反证：真躺平会遭道德极刑与社会关系压力（P008—P011）。",
    "把机制追溯到文化与语言：不是阴谋或压榨，而是几千年凝聚的生存本能，并已融进汉语（P012—P013）。",
    "以汉语中缺乏歌颂躺平的语料与作品、文艺产品本身出自奋斗者为理由（P014—P018）。",
    "补充亲友关心无法隔绝、社会支柱反成能量没收者（P019—P022）。",
    "让步与限定：少数人可能撑住，但文化机制保证人力被发挥到极限（P023）。",
    "以历史强敌与被击退后的反扑、以及“再多几十万人躺平就不说汉语”的假设强化论证（P027—P030）。",
    "以反问收束前半段并给出“别的文明或许可行、中国不宜期待”的判断（P031—P033）。",
    "推出唯一行动路径：支持国家向外开拓与自强，夺回定价权与就业市场（P034—P035）。",
    "以中国人的情感反应机制论证躺平不可行（P036—P037）。",
    "最后重新定义劳动法的目的，指出力竭不可避免，只余“怎么竭”的选择，回扣开头（P039—P043）。"
   ],
   "concept_usage": [
    {"term": "三竭（力竭/气竭/心竭）", "meaning": "文章标题所指的三种耗竭结局：为工作与生活两头努力而力竭；因饱受批评惩罚而气竭；把回避努力省下的精力在悔恨、羞耻、迷茫中耗到心竭。", "evidence": "P041", "ambiguity": "标题“三竭”未在正文直接点明，靠 P041 的并列反推"},
    {"term": "躺平", "meaning": "退出积极竞争、缩回个人生活的生活方式；作者认为物质上可行但会招致社会与家庭关系的惩罚。", "evidence": "P007", "ambiguity": "未给出躺平的严格定义或边界"},
    {"term": "劳动法", "meaning": "文中指硬性限制劳动时间的法律保护；作者称其功能不是让人安逸，而是调整工作与生活各占的精力比例。", "evidence": "P039", "ambiguity": "未涉及具体法条与执行机制"},
    {"term": "自雇", "meaning": "平台从业者被算作“自己是老板”，与平台签的服务时间被视为商业合同交易，从而不适用劳动法保护。", "evidence": "P004", "ambiguity": "作者以“政策会将……算为自雇”的预测口吻表述，未给政策依据"},
    {"term": "魔法/祝福/诅咒", "meaning": "把每一分人力从消极厌世思想中夺回的文化机制，被作者称为最大的祝福之一，同时又是诅咒。", "evidence": "P025", "ambiguity": "比喻性用法，未界定机制的具体内容"},
    {"term": "血继限界", "meaning": "借自漫画的用语，指能把一个民族撑四千年的传承能力，作者以此反问读者能否与之对抗。", "evidence": "P030", "ambiguity": "外来借用词，正文未解释"},
    {"term": "道德极刑", "meaning": "社会对躺平者在关系与评价上的全面惩罚（配偶、朋友、父母、亲戚的疏远）。", "evidence": "P008", "ambiguity": "修辞夸张，非制度性概念"}
   ],
   "examples_and_targets": [
    "美国“一个人做三份工、加起来一天12-16小时”的现象——作者引作参考证据（P003）",
    "开网约车、送快递、签约MCN直播、签约网店做在线客服等新业态被算作自雇——作者预测性例证（P004）",
    "“自愿加班”“把活带回家里做”——补充例证（P005）",
    "和尚谈“勇猛精进”、仙人刻苦攒道行历天劫、隐士谈“先天下之忧而忧”——语言与文化例证（P014）",
    "中文电影多是各种版本的《热辣滚烫》，分手歌在炫耀有过恋人或“空灵之作”作者自传是奋斗典范——文艺市场例证（P017、P018）",
    "匈奴、突厥、契丹、蒙古、女真、英法列强、帝国日本——历史强敌例证（P027）",
    "假想反事实：若危急关头多几十万人躺平，读者不会说汉语、不会姓张王李赵而可能姓罗德里格斯，不会有啃老与倾家荡产支持学钢琴学芭蕾的父母，也不会有守在喜马拉雅和热带丛林的边防战士（P029）",
    "秦桧、岳飞、圆明园、霍去病、李白、《云宫迅音》——作者用来测试读者“纯种中国人”情感反应的修辞材料（P036）",
    "菲律宾人、墨西哥人的姓氏罗德里格斯——反事实后果的类比材料（P029）"
   ],
   "conditions": [
    "全篇针对“严格执行劳动法”这一假设情形展开，而非既有事实（P001）",
    "躺平可行性的前提：房产持有硬成本几乎为零、食物原料/基本信息服务/基本医疗极为便宜、储蓄率超高（P007）",
    "躺平的后果以“如果你真的这么做”的假设语气给出（P008）",
    "作者承认“不排除有部分人有足够的运气和能力撑住这种考验”（P023）",
    "历史论证带反事实条件：“如果在最危急的那些关头，再多上一百万甚至几十万人……躺平”（P029）",
    "国别限定：“也许别的国家、别的文明能……但是在中国”（P032）",
    "结论对读者的适用条件：只要看到秦桧就火大、听到云宫迅音就热血沸腾等情感反应成立（P036）",
    "“政策会将新业态算为自雇”为对政策走向的预测，未说明时间与范围（P004）"
   ],
   "rhetoric_and_tone": "第二人称训诫式，语气强烈、断言密集；反复使用反问逼问读者（“所以你懂了吗？”“说得够清楚了吗？”“你能挺多久？”）；大量夸张与比喻（道德极刑、泥鳅洞与鲨鱼、洞穴、结界、魔法、诅咒、血继限界）；穿插英文句子（P009、P018）制造冷峻调侃；以历史悲情与民族存续叙事收拢论证；结尾把“三竭”作为不可逃避的命运收束。",
   "unresolved_questions": [
    "未提供任何数据或机制论证“严格执行劳动法”与企业倒闭、裁员之间的关系，只有替代性断言。",
    "美国“一人三份工、一天12-16小时”为外部事实断言，未给来源，需外部核查。",
    "“政策会将开网约车、送快递、MCN直播、网店客服算为自雇”是对政策走向的预测，正文未给依据。",
    "P004 中“不适用与劳动法保护”的“与”疑为“于”之误，原文如此，未改。",
    "“zf”为拼音缩写，正文未明写其所指词。",
    "brief 末句“并且政策会将开网约车、送快递、签约MCN直播”在 brief 中被截断，正文 P004 为完整表述，二者不完全一致。",
    "标题“三竭”只在 P041 出现对应内容，未见作者对“三竭”的明确定义。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个说法是不正确的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "出现大量的“劳务派遣公司”和极小的微型企业，以合法方式突破劳动时间的硬性限制", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一个人做三份工，每一份都没有超过限时，加起来达到一天12-16小时", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你跟平台签合同约定的服务时间属于商业合同交易，不适用与劳动法保护", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "更不提大量的“自愿加班”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "根本的不是“资本家的残酷压榨”，而是中国社会的总体价值观逻辑", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "完全是可以做到的，至少门槛并不高", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "你基本上会被社会处以道德极刑", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "而是中国这块土地上经过几千年的盛衰兴亡、生离死别凝聚出来的生存本能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "没人能用汉语来有效的向你证明“躺平也挺好的”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "这种关心会成为躺平者巨大的困扰", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "还会成为你情绪能量的没收者", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "但整个文化机制保证了中华民族总是可以把人力资源发挥到极限", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P025", "quote": "能把每一分人力都从种种消极厌世思想的侵蚀中夺回的“魔法”是最大的祝福之一", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "所有的诅咒都同时是祝福，所有的祝福也都同时是诅咒", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P029", "quote": "再多上一百万甚至几十万人因为不管什么原因“躺平”，现在你说的就不是汉语了", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P032", "quote": "但是在中国，不好说绝对不可能，但劝你不要太期待", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P034", "quote": "在中国只有一条路可以走", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P034", "quote": "夺回属于我们的公平的定价权和远比现在广阔得多的就业市场", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P037", "quote": "中国文化给你设计的快感机制、社会奖励，全都建立在你积极主动的发光发热的态度上", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P039", "quote": "劳动法不是为了让你“安逸生活”的，那是为了让你努力的工作之外，还可以努力生活", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P041", "quote": "每天力竭是你无可避免结果，区别只有带着家人的祝福和钦佩力竭，还是饱受批评和惩罚的气竭、还是把回避努力所省下的精力在悔恨、羞耻和迷茫中耗到心竭", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P043", "quote": "所以你明白为什么在中国不会出现“严格执行劳动法，企业就会大面积倒闭”了吧？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["劳动法与社会政策", "用工形式与就业", "社会文化与民族性", "价值观与生活方式"],
   "issue_candidates": ["严格执行劳动法的后果", "劳务派遣与灵活用工/自雇化", "躺平与劳动焦虑", "社会压力与亲友关系", "民族存续与人力资源动员"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "训诫式劝告"],
   "object_candidates": ["中国", "美国", "劳务派遣公司", "微型企业", "网约车/快递/MCN/网店客服平台", "政府（zf）", "资本家", "匈奴/突厥/契丹/蒙古/女真/英法列强/帝国日本"],
   "working_keywords": ["三竭", "力竭", "气竭", "心竭", "躺平", "自了", "劳务派遣", "自雇", "劳动法", "道德极刑", "血继限界", "定价权"]
  },
  "notes": "brief 末句被截断（“…签约MCN直播”），完整表述见正文 P004；正文 P004“不适用与劳动法保护”的“与”疑为“于”之误，照原文保留未改；本篇无图片节点。"
 },
 "394fcf45": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "e7cddc02": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "e652ba78": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


autofill_empty_analysis(BATCH, SKELETON, ANALYSIS)


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
