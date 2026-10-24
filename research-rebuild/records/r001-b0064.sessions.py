# -*- coding: utf-8 -*-
"""批次 r001-b0064 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0064.sessions.py            # 写 out/r001-b0064.out.jsonl
  python3 records/r001-b0064.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0064"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0064.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "cf163892": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何彻底改掉粗心大意的毛病？”，即寻求消除粗心的方法。作者未复述提问者立场，而是直接否定“彻底改掉”这一目标的可达性，并把“粗心”重新解释为人的真实水平（最无所用心状态下的表现），进而把问题从“提升注意力”转向“长期练习形成严谨工作习惯”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "开篇否定“彻底改掉粗心”的目标，并把最无所用心状态下的表现定义为人的真实水平。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "靠提升注意力、临时“蹦起来”达到的水平是假的：不可持续，且多半只是做姿态以免被骂。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "因假努力屡次无效，遂学会“做认真状”，并由姿态衍生出充实感与“我就是这么笨”的自我塑造。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "断言“认真论”贻害无穷；问题的关键是严谨工作习惯经长期练习而习惯成自然，而非“认真”。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "以走路、骑车、游泳为例说明技能靠反复练习，且这些练习并不需要“认真”，只是手熟。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "指出教育体系知识安排过密，基础技巧练习次数被摊薄，练习时间资源远远不足，故责任不在孩子“不认真”。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "把“你不够认真”解释为老师家长下意识的一种“放弃的仪式”，其后果是各方以“就是笨”共同解脱。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021", "P022"], "summary": "让步承认天资有限存在，但在认清这一点后，很多人在实际工作的直接反馈下“突然变聪明”并成为熟练工或骨干。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025"], "summary": "讽刺这批成功者仍把职场新人和子女的问题归为“不认真”，并复述其劝导话语后加以辱骂式否定。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030"], "summary": "金句总结第一点：不认真都能搞定才叫真搞定；需持续观察改进直到找到傻瓜式可靠办法并练到不用多想，方能超越认真焦虑并取得冲锋心态。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P031", "P032", "P033"], "summary": "第二点：让错误变得更直观是找方法的手段，以染色体染色、X光定位弹头为类比，主张把曲线、流程图、实验做出来。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P034", "P035", "P036"], "summary": "第三点：找到路后一直改进到不费吹灰之力、练到习惯成自然，并称其中的乐趣本身足以使人上瘾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的真实水平就是在最粗心大意、无所用心的状态下的水平；该水平高才算真水平高。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "靠“提升注意力”或临时“蹦起来”达到的水平是假的，既不可持续，也多半只是做姿态以免被抓到不认真。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题关键不在“认真”，而在切实有效、严谨的工作习惯经过长期练习后习惯成自然；反复出现的“你不够认真”实为老师家长下意识的一种放弃的仪式。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育大纲对知识安排过于密集，使语言能力、逻辑能力等基础技巧的练习次数被摊平，形成完美技能所需的练习时间资源远远不足，这不是孩子“不认真”。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者不否认世界上存在天资有限问题，但认为在认清这一点的情况下，很多人可以不必是自己所相信的那么笨。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有做到不认真也能搞定并练到不用多想，才能超越“认真焦虑”并获得真正信心。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "找方法的持续手段是让错误变得更直观，例如画曲线、画流程图、做实验，而老师的口水和家长的怒吼不顶用。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "找到路后要一直改进到不费吹灰之力、练到习惯成自然，过程本身有乐趣，无需依赖“认真”。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：“不认真就要出大事”的心态能干什么。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者复述被其讽刺的那批成功者对新人和子女的说法“你们一定要认真哦”。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "先否定提问目标：某种意义上说，你是改不掉的（P001）。",
    "给出替代定义：真实水平=最无所用心状态下的水平（P002-P003）。",
    "否定对立方案：靠提升注意力、蹦起来达到的水平不可持续、多半是做姿态（P004-P005）。",
    "举后果：憋着认真n回没拿到好成绩，却学会“做认真状”，并自我塑造成“就是笨”（P006-P008）。",
    "指出“认真论”贻害无穷，转向真正关键：严谨工作习惯经长期练习习惯成自然（P009-P010）。",
    "类比举证：走路、骑车、游泳靠反复练习而非认真，无他唯手熟尔（P011-P013）。",
    "推进到制度原因：大纲知识密集摊薄基础技巧练习，练习时间资源远不足，责任不在孩子不认真（P014-P016）。",
    "诊断“你不够认真”为家长老师下意识的放弃仪式，后果是各方共同以“笨”解脱（P017-P019）。",
    "让步：存在天资有限问题，但很多人可不必如自己所信的那么笨（P020）。",
    "举职场反例：实际工作的直接反馈使人“突然变聪明”，成为熟练工、骨干甚至企业主（P021-P022）。",
    "讽刺循环：这些人仍以“不认真”看待新人和子女，作者以辱骂式短句否定（P023-P025）。",
    "行动建议一：练到不认真也能搞定，以超越认真焦虑并获得真信心与冲锋心态（P026-P030）。",
    "行动建议二：让错误变得直观有形状、有重量、有硬度、有气味（P031-P033）。",
    "收束：一直改进到不费吹灰之力，过程乐趣本身即足够上瘾（P034-P036）。"
   ],
   "concept_usage": [
    {"term": "真实水平", "meaning": "指人在最粗心大意、脑袋放空、无所用心状态下的表现水平，被作者用作衡量“真水平高”的标准。", "evidence": "P002", "ambiguity": "作者未说明该标准是否适用于一切任务类型，也未给出可操作的测量方式。"},
    {"term": "认真", "meaning": "文中区分了两种：靠提升注意力、蹦起来维持的姿态式“认真”（被判为假），与做认真状的“认真”；作者主张不需要这种认真，而需要习惯成自然的严谨习惯。", "evidence": "P004", "ambiguity": "“认真”一词在文中主要作被批评对象使用，作者未给出正面定义。"},
    {"term": "做认真状", "meaning": "为了不被抓到“不认真的样子挨骂”而表演出的认真姿态，作者称其本身很累且会带来“充实感”。", "evidence": "P006", "ambiguity": "作者未区分表演性姿态与真实投入的边界。"},
    {"term": "认真论", "meaning": "把问题归因为“你不够认真”的说法体系，作者评价其贻害无穷。", "evidence": "P009", "ambiguity": "作者未指明“认真论”的具体主张者是谁。"},
    {"term": "习惯成自然", "meaning": "严谨有效的工作习惯经长期练习后自动化，达到不用想太多都能搞定、不费吹灰之力的状态。", "evidence": "P010", "ambiguity": "未给出达到该状态所需练习量的标准。"},
    {"term": "做认真状的技巧", "meaning": "指熟练表演认真姿态的能力；作者称一旦掌握，学生、父母、老师、教育系统就都可以长出一口气。", "evidence": "P018", "ambiguity": "此处为反讽用法，非作者提倡的技巧。"},
    {"term": "“突然变聪明”", "meaning": "指人走上工作岗位后，在实际工作的直接反馈引导下表现明显改善的现象。", "evidence": "P021", "ambiguity": "作者以引号标记该说法，未说明是否为他人用语。"}
   ],
   "examples_and_targets": [
    "走路、骑自行车、游泳：作者用作类比证据，说明技能靠反复练习而非“认真”（P011-P013）。",
    "爹妈、老师：作为反复要求“认真”并骂人的对象出现在叙事中（P006）。",
    "教育体系大纲与老师、家长群体：作为被批评对象，“你不够认真”被解释为其下意识的放弃仪式（P014、P017）。",
    "染色体染色、手术前X光定位弹头：作为“让错误变得直观”的类比材料（P031）。",
    "“老师和父母没法骂了”“老师和家长的怒吼都是透明的”：作为修辞材料支撑姿态式认真与怒吼无效的判断（P006、P032）。",
    "职场新人、子女、熟练工、老师傅、企业主、业务骨干、精英：作为职场反馈改变表现这一叙述中的角色（P021-P023）。",
    "“你是改不掉的”“认你x的真啊”“废寝忘食好吗？”：口语化、含脏字的修辞表达（P001、P025、P036）。"
   ],
   "conditions": [
    "判断预设了对象处于“最粗心大意／无所用心”的自然状态，而非被要求刻意专注的状态（P002）。",
    "“多半只是空做姿态”带概率限定词，作者未断言所有认真姿态皆为表演（P005）。",
    "教育制度批评限于“现在的教育体系大纲”，具时间限定（P014）。",
    "作者以“我倒不是说世界上不存在天资有限问题”作让步限定，随后结论限于“有很多人可以不必是自己所相信的那么笨”（P020）。",
    "职场变聪明的叙述依赖实际工作有直接反馈（算错题后果具体：东西倒塌、产品报废、客户退货）以及不必持续追赶新知识点、有更多时间反复练习业务这两个条件（P021）。",
    "行动建议以“直到找到傻瓜式的可靠办法”“有足够多的练习”为条件（P027）。",
    "“能信的话你会省下不少看抑郁症的钱”式的收益表述属预测语气（P032 为同类表达，见该段）。"
   ],
   "rhetoric_and_tone": "第二人称“你”直接对话提问者，口语化、训诫与讽刺并用：开篇即下“你是改不掉的”断语，用“脑袋放空、脚踩西瓜皮”“蹦起来”“做认真状”“金句大总结”等俗语与自创说法推进；对“认真论”及职场成功者循环说教持明显批判态度，出现“贻害无穷”“他娘的”“认你x的真啊”等激烈措辞；结尾转温和劝诱（“这是一件极其有乐趣的事情”“废寝忘食好吗？”）。结构上先破后立，末段以编号金句作总结。",
   "unresolved_questions": [
    "P003“脚踩西瓜皮滑到哪里算哪里”与P022“ta们”等表述含大量口语与网络拟音词，未影响定位，但“真实水平”是否可测量正文未说明。",
    "作者称“ta们不必再不停的追赶新知识点”缺少适用范围限定，是否适用于非职场情境未说明。",
    "P014对教育体系大纲“过于密集”的判断为作者断言，涉及现行课程安排的事实，待外部核查，本文未给出依据。",
    "问句“你有很认真的走路、骑车、游泳吗？”（P012）为反问，作者未给出被问者的可能回答，主体为泛指的“你”。",
    "“做认真状”何时由姿态转为真实习惯，正文未给出判据，可能影响对 P010 主张的解释。",
    "P036“废寝忘食好吗？”为反问收尾，未说明其指向是褒扬还是告诫，存在歧义。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "某种意义上说，你是改不掉的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "人的真实水平，就是在最粗心大意的状态下的水平——也就是“无所用心”的那个水平。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "靠“提升注意力”“蹦起来”达到的水平是假的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "第一是不可持续，第二是实际上多半只是“空做姿态以免被抓到不认真的样子挨骂”而已。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "问题的关键不在于“认真”，而在于切实有效的、严谨的工作习惯经过长期的练习，习惯成自然。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P017", "quote": "实际上是老师、家长们因为长期摸不着头脑，进而自然而然的、下意识而做的一种“放弃的仪式”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "现在的教育体系大纲对知识的安排过于密集，导致基础技巧——语言能力、逻辑能力——的练习次数被大量的知识点摊得太平了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "要形成走路、骑车这样的完美效果所需要的练习的时间资源远远不足。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P020", "quote": "我倒不是说世界上不存在天资有限问题，但说句实话，在认识清楚这一点的情况下，有很多人可以不必是自己所相信的那么笨。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P028", "quote": "只有这样你才能超越“认真焦虑”，并且获得真正的信心", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P032", "quote": "把曲线画出来，把流程图画出来，把实验做出来。老师的口水和家长的怒吼都是透明的，不顶用。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P035", "quote": "你根本不需要“认真”，因为这其中的乐趣本身就会让你足够上瘾。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P030", "quote": "“不认真就要出大事”的心态，你能干什么？", "relation": "context"},
    {"key": "E14", "paragraph_id": "P024", "quote": "“你们一定要认真哦。”", "relation": "context"},
    {"key": "E15", "paragraph_id": "P018", "quote": "你势必会学会做认真状", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P007", "quote": "做认真状本身就很累的了，会给人一种“充实感”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["学习与教育", "认知与工作方法", "心理与自我认知"],
   "issue_candidates": ["粗心是否可改", "认真与注意力提升的有效性", "练习次数与技能自动化", "教育大纲知识密度", "归因于“不认真”的家长与教师话语", "错误反馈的可视化"],
   "text_function_candidates": ["答疑", "评论", "经验总结", "批评"],
   "object_candidates": ["提问者", "学生", "父母", "老师", "教育系统", "职场新人", "企业主"],
   "working_keywords": ["粗心", "认真", "真实水平", "无所用心", "做认真状", "习惯成自然", "认真焦虑", "关键路径", "错误可视化"]
  },
  "notes": "提问者问“如何彻底改掉粗心大意的毛病？”，作者未作答该问法，而是否定“改掉”的目标并重设问题，全文属直接答疑式评论。已按原文逐段核对，无图片节点。需注意 brief 为正文前若干句的截断预览，不作为主张依据。文末 P036“废寝忘食好吗？”为反问收尾，语气偏劝导。"
 },
 "c463a9b3": {
  "analysis": {
   "question_context": "提问者（Q001）就“湖南高一新生军训时晕倒身亡，教育局通报系因患热射病已启动调查”这一新闻事件征求看法。提问者未表达明确立场，仅提供事件与调查信息。作者不把该事件当作需要特别评论的个案，而是借机论证军训制度的战略功能，并批评主张取消军训的言论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "把该事件定性为普通意外，引出全国每年大学军训参与规模约800万人的数量前提。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "主张百万分之一级别的严重训练事故率不会导致政策变化，只会带来细则修正，并称2015年已推行军训前强制体检。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "提出军训的根基是义务兵役制这一国策，并称在领土争端彻底解决、国力胜过所有潜在敌人之前该制度不会有重大变化。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012"], "summary": "反驳“学走队列无用”的视角，主张学校操场是有意保留的战时总动员军事用地，并以礼堂、体育课用地需求与城市地价的机会成本作论证。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "反驳“训练内容无用”的看法，主张教官获得的组织大规模新兵训练经验才是关键，中国需要大量有动员兵训练经验的基层军官。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "把每年约一千五百万人的集中军训称为义务兵役制的“开机自检”，并强调该规模卫星可见。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "推测取消制度后操场、人武部、演训关系与储备器材会萎缩废除，进而使中国的总动员能力被外界判断为需18-36个月才能运转。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "以三个月可动员千万具备中学知识兵员为前提，称无国家或国家集团敢与中国常规冲突；并称若总动员需一两年则结论难说，有人会产生大胆想法。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030"], "summary": "主张真正保护日常安全的不是现役部队或核武库，而是对手无法确定打垮两百万部队所需时间，操场上的1500万因而是其噩梦。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032"], "summary": "列举操场人群中可转化的大量兵种与无人机操作者，称之为中国战略安全的绝对保证与底牌。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P033"], "summary": "回到开篇结论：不要抱“军训会晒晕人又不能帮我学会杀人，应该取消”的幻想。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P034", "P035"], "summary": "提出判断“什么可以改变、什么应接受”是一种至关重要的能力，并把该辨识能力低下与受操纵、虚掷生命相联系。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P036", "P037", "P038", "P039"], "summary": "质问读者在断言“军训毫无用处”前做过哪些调查研究，批评其未查未想即抱怨，并警告不改此习惯人生将很痛苦。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该军训致死事件只是普通意外；百万分之一级别的严重训练事故率不会导致太大政策变化，只会导致细则修正，2015年已推行军训前强制体检制度。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "军训的根基是义务兵役制这一国策；义务兵役制不变，军训就绝对不可能被取消。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在彻底解决台湾、南海等领土争端、中国国力胜过所有胆敢觊觎的敌人的总和之前，义务兵役制不可能有重大变化。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学校操场是有意安排保留的、为随时启动义务兵役制进行战时总动员的军事用地，其地价机会成本巨大，故不能只为体育课或集会而保留。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "军训的关键价值在于教官获得“对全新兵员组织大规模训练”的经验；中国需要大量有基本训练动员兵经验的基层军官，否则带兵经验军官队伍无法支撑总动员。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每年约一千五百万人（大学新生八百万，算上高中生接近翻倍）的集中军事训练是义务兵役制的一次“开机自检”，配套人员、机构、场地、器械得到年度检验、测试和更新。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若取消该制度，用不了几年操场会缩小或消失变成综合体育馆、人武部缩编、演训关系淡漠、储备器材与训练基地被弃置废除。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "最重要的是，中国在半年到一年内扩军至三千万高中以上文化程度兵力的动员能力，可能被判断为需要18-36个月才能充分运转，那几乎意味着事实上已丧失总动员能力。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "动员一千万具备几何、代数、三角函数、化学、生物学常识并熟练掌握母语读写的兵员只需三个月，则没有任何国家或国家集团敢于想象与中国陷入常规军事冲突；但若总动员需一年多甚至两年多，结论就难说。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正保护中国人能悠闲刷手机吐槽的不是现役部队，也不是核武器库（至少目前不是），而是对手无法确定打垮两百万部队需要多久，操场上的一千五百万因而是其噩梦与中国的底牌。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不应抱“军训会晒晕人又不能帮我学会杀人，应该取消”的幻想。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判断“什么事情可以改变、值得投入并期待回报，什么事情不能甚至不应该改变、要花精力接受”是一种至关重要的能力；该能力低下轻则招致损失，重则在错误方向虚掷生命。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在开口定论“军训毫无用处”之前应先做调查研究与思考，而批评对象没有去查去想，直接开口抱怨。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "作者转述并反驳的对手看法：学个走队列没有用；军训会晒晕人又不能帮我学会杀人，应该取消。", "evidence": ["E21", "E17"]},
    {"claim_id": "C015", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "hypothetical", "statement": "作者设想敌对方可能产生的想法：“原子弹其实不像麻瓜们想的那么坏……”。", "evidence": ["E22"]}
   ],
   "argument_steps": [
    "以“普通意外”定性事件，并用每年约800万参训人数确立规模前提（P001-P003）。",
    "给出规律判断：百万分之一级事故率不改变政策，只修正细则，且2015年已有强制体检（P004）。",
    "给出制度前提：军训根基是义务兵役制这一国策，故不可能被取消（P005）。",
    "限定条件：在领土争端解决、国力绝对优势达成之前该制度不会重大变化（P006）。",
    "转向认知批评：认为军训无战略意义是观察视角太低（P007）。",
    "以“操场”命名反问切入，先排除足球与体育课、礼堂等解释（P008-P012）。",
    "提出解释：操场是为战时总动员保留的军事用地，并以城市地价的机会成本佐证（P010-P012）。",
    "预判并回应“这点训练没啥大用”的质疑，改从教官经验角度论证其关键性（P013-P016）。",
    "把年度军训定义为义务兵役制的“开机自检”，并强调其卫星可见的规模（P017-P018）。",
    "反向推演：取消制度将导致场地、机构、器材、演训关系萎缩（P019）。",
    "推进后果：总动员能力可能被外界判断为需18-36个月才能运转，等于丧失总动员能力（P020）。",
    "以反问强化：场地与机构没了不能临时凭空产生（P021）。",
    "给出威慑推理：三个月可动员千万有文化兵员则无人敢想常规冲突；若需一两年则结论难说（P022-P024）。",
    "引述设想中的“大胆想法”，即核武器并不那么可怕（P025）。",
    "反转安全归因：真正的保护不是现役部队与核武库，而是对手无法确定的动员时间（P026-P030）。",
    "收束到结论：不要幻想取消军训（P033）。",
    "提升为一般能力要求：辨识什么可改变、什么应接受（P034-P035）。",
    "最后质问读者是否做过调查研究，并警告不改此习惯将痛苦（P036-P039）。"
   ],
   "concept_usage": [
    {"term": "军训", "meaning": "指大学与高中新生参加的集中军事训练；作者视其为义务兵役制的配套检验机制与总动员能力的一部分，而非单纯体育或纪律训练。", "evidence": "P017", "ambiguity": "作者未区分大学军训与高中军训在制度上的差异。"},
    {"term": "义务兵役制", "meaning": "被作者称为军训的根基、关系到国家安全的根本国策，其存废决定军训存废。", "evidence": "P005", "ambiguity": "作者未说明该制度当前的具体法律形式与执行状态，待外部核查。"},
    {"term": "操场", "meaning": "作者解释为有意安排保留、可将全校师生聚集一天一操一周一会的开阔草地，实为随时启动义务兵役制进行战时总动员的军事用地。", "evidence": "P010", "ambiguity": "作者称“普遍称为操场”属对命名习惯的断言，未给出史料依据。"},
    {"term": "开机自检", "meaning": "比喻年度集中军训对义务兵役制配套人员、机构、场地、器械的检验、测试和更新。", "evidence": "P017", "ambiguity": "比喻所指的具体检验指标与结果未说明。"},
    {"term": "总体军事动员能力", "meaning": "文中指在半年到一年之内扩军至三千万高中以上文化程度兵力的能力，被作者称为战略安全的绝对保证。", "evidence": "P020", "ambiguity": "三千万、半年至一年、18-36个月等数字无来源，待外部核查。"},
    {"term": "麻瓜", "meaning": "借自《哈利·波特》的戏称，用于指代把原子弹想得很坏的一般人。", "evidence": "P025", "ambiguity": "引号内话语为作者设想的他人想法，非作者判断。"},
    {"term": "长痛不如短痛", "meaning": "作者用来描述某些国家或集团可能不介意发动一次军事冲突的算计。", "evidence": "P026", "ambiguity": "主体为泛指的“某些国家、某些集团”，未具体指名。"}
   ],
   "examples_and_targets": [
    "湖南高一新生军训晕倒身亡、教育局通报热射病并启动调查：属提问者提供的新闻事件，作者将其定性为普通意外（P001、Q001）。",
    "2015年军训前强制体检制度：作者用以证明事故只带来细则修正的事实断言，需外部核查（P004）。",
    "每年约800万人参加大学军训、集中军训人口一千五百多万（大学新生八百万，算高中生接近翻倍）：作为规模论据的数据（P003、P017）。",
    "操场、综合体育馆、礼堂、城市地价：作为论证军事用地保留与机会成本的证据材料（P010-P012、P019）。",
    "台湾、南海等领土争端：作为义务兵役制不会重大变化的限定条件（P006）。",
    "两百万现役部队、上百条船、几千发导弹、几百枚核弹、北约与周边国家：作为威慑推理中的对手力量材料（P016、P023、P027-P028）。",
    "装甲兵、导弹兵、工程兵、狙击手、飞行员、雷达兵、无人机驾驶员与“吃鸡狂魔”：作为操场人群可转化兵种的例举（P031）。",
    "“原子弹其实不像麻瓜们想的那么坏……”：引号内为作者设想的敌对方想法，非作者观点（P025）。",
    "男足：“就男足那个样”作为否定操场为足球所用的修辞材料（P009）。"
   ],
   "conditions": [
    "“义务兵役制不变，军训就绝对不可能被取消”以制度不变为条件（P005）。",
    "义务兵役制无重大变化以“彻底解决台湾、南海等领土争端，中国的国力胜过所有胆敢觊觎的敌人的总和”为前提（P006）。",
    "操场的军事用地解释依赖中国高校中学多位于城市中、地价高昂这一情形（P012）。",
    "教官经验论依赖“他们中的大部分将来都不会下连队去直接担任军事主官”这一假设（P015）。",
    "P020的动员能力表述使用“可能被判断为”“那几乎意味着”等推测措辞（P020）。",
    "P022的威慑结论以“动员一千万……兵员只需要三个月”为条件；P024明确“但是如果总动员需要一年多甚至两年多才能逐渐运转起来，这个问题的结论就难说了”（P022、P024）。",
    "P026对核武库作用的否定带有“至少目前不是”的时间限定（P026）。",
    "对读者的批评以“在你开口定论……之前”为条件，针对未做调查即抱怨的读者（P036）。"
   ],
   "rhetoric_and_tone": "军事战略评论式论辩，语气强硬、训诫且带挑衅性：以“你们知道吗”“你们想过吗”“我提醒你们”等第二人称反复施压，用“虚头巴脑”“想都不必想”“打个响指”等口语；借“开机自检”“底牌”“噩梦”等比喻构建威慑叙事；P026-P028连用排比式短句模拟对手盘算，P025引述设想中的核武言论以增强紧张感；结尾转为道德劝诫（“多想想吧”）。全文不作个案评价而作制度论证。",
   "unresolved_questions": [
    "文中“2015年就已经推行了军训前强制体检制度”属事实断言，需外部核查（P004）。",
    "800万大学新生参训、一千五百多万集中军训人口、三千万扩军、18-36个月等数字均无来源，待外部核查（P003、P017、P020）。",
    "P006“中国的国力胜过所有胆敢觊觎的敌人的总和”为条件设定，作者未说明判定标准。",
    "P010操场为“军事用地”的解释未给出任何文件或史料依据，属推论，需外部核查。",
    "P018“这一千五百万人头顶上没有屋顶，卫星能看见”指涉何国卫星与何种侦察目的，正文未明说。",
    "P025引号内“原子弹其实不像麻瓜们想的那么坏……”的说话主体，作者仅以“有些人”设想，无法确定具体归属。",
    "提问所涉湖南学生死亡事件的责任与调查结果，作者未评论，正文亦未涉及。",
    "P009“你都知道中国人根本没有那么热爱足球”属作者断言，无数据支撑，待核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "本来这不值得特别评论，只是一个很普通的意外事件。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "百万分之一级别的严重训练事故率不会导致太大的政策变化，只会导致一些细则修正", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "军训的根基是义务兵役制这一项国策。义务兵役制不变，军训就绝对不可能被取消。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "在彻底解决台湾、南海等领土争端，中国的国力胜过所有胆敢觊觎的敌人的总和之前，义务兵役制是不可能有重大变化的", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P010", "quote": "那是一块有意安排保留的为随时启动义务兵役制进行战时总动员的军事用地。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "一个城市几十所甚至上百所中学/大学的操场的地皮值多少钱？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "对于训练你们的教官而言，他们受到的“对全新兵员组织大规模训练”的经验是至关重要的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "中国需要大量有基本的训练动员兵经验的基层军官。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "其实是义务兵役制的一次“开机自检”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "所有与这个制度配套的人员、机构、场地、器械，都会得到一年一度的检验、测试和更新。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "就会有大量的操场缩小甚至消失，变成所谓“综合体育馆”，人武部缩编", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "就可能被判断为“需要18-36个月才能充分运转”——那几乎意味着在事实上已经丧失了总动员能力。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "熟练掌握母语读写的兵员只需要三个月，世界上没有任何国家或国家集团敢于想象与中国陷入常规军事冲突。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "这个问题的结论就难说了——有些人可能会产生一些“大胆的想法”。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P026", "quote": "真正保护住你们能悠闲地刷手机吐槽的，不是现役的部队，也不是我们的核武器库（至少目前不是）。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P030", "quote": "那操场上的1500万会成为它们永远无法醒来的噩梦。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P033", "quote": "不要抱任何“军训会晒晕人又不能帮我学会杀人，应该取消”的幻想。", "relation": "contradicts"},
    {"key": "E18", "paragraph_id": "P035", "quote": "判断“什么事情是可以改变的、是值得花精力和感情去改变并可以期待回报的，什么事情是不能甚至不应该改变的、是要花精力和感情去接受的”是一种至关重要的能力。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P036", "quote": "在你开口定论“军训毫无用处”之前，你下过哪些调查、研究、对比和思考的功夫？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P037", "quote": "但你没有去查、去想，而是直接开口抱怨。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P007", "quote": "很多人意识不到大学、高中军训的战略意义，觉得“学个走队列有什么用”，这是个观察视角太低造成的认知问题。", "relation": "contradicts"},
    {"key": "E22", "paragraph_id": "P025", "quote": "“原子弹其实不像麻瓜们想的那么坏……”", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国防与军事", "教育制度", "公共政策", "社会评论"],
   "issue_candidates": ["军训存废", "军训训练事故与体检制度", "义务兵役制与总动员能力", "学校操场用地性质", "基层军官训练经验", "核威慑与常规冲突"],
   "text_function_candidates": ["评论", "答疑", "论辩", "批评"],
   "object_candidates": ["提问者", "湖南高一新生", "教育局", "大学与高中新生", "军训教官", "中国军队", "北约", "周边国家", "人武部"],
   "working_keywords": ["军训", "义务兵役制", "操场", "总动员", "开机自检", "热射病", "强制体检", "基层军官", "核武器库", "底牌"]
  },
  "notes": "本篇针对新闻事件提问，但作者主要作制度与战略论证，未对个案作评价或表达对死者的态度；提问者字段仅提供事实，无立场可归属。文内数字（800万、一千五百多万、两百万、三千万、18-36个月、2015年强制体检）均无出处，已登记为待外部核查，不得视为已证实事实。P025引号内核武言论为作者设想的他人想法，未归为作者主张。无图片节点。"
 },
 "be47f120": {
  "analysis": {
   "question_context": "提问者（Q001）问“人如何克服自己的懒散习性？”，预设懒散是需要克服的习性。作者不接受该预设，先以“多挨生活的毒打”作答，继而主张懒散是生物本能中健康的低成本生存安排，真正要改的不是懒而是“打麻药”，并给出顺应而非克服的方向。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以“多挨生活的毒打”作简短回答，并声明并非抖机灵开玩笑。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "以非洲狮子为例：它们懒散且要等肚子饿了才有斗志打猎，不饿时驱赶也不去。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "由狮子推到一般判断：幸存主要靠休息而非努力，休息低消耗安全稳妥，能休息就应先休息。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "指出每天被焦虑驱使到处乱试是速死之道；懒散习性写在生物本能底层，而这种安排本身健康。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "行动建议：应接受这一点并顺应安排去追求更好结果，而非负罪或毫无意义地耗尽自己。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "懒散到不该再懒散时，生活主动来毒打，形成挨打记忆并塑造出恰当的焦虑传感器，懒散下限自然调整。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "把“顺应安排”定义为对“我正在被毒打”敏感一点，并以逐级加重的毒打清单说明拖延的后果。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019", "P020"], "summary": "指出问题出在很多人挨了毒打却用上麻药，举上网喷人、抽烟喝酒、六合彩、网络贷、以贩养吸等例，主张停止打麻药。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022"], "summary": "断言别人不是比你勤奋而是比你敏感；以标题句点明要改的不是懒而是打麻药。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P023", "P024", "P025"], "summary": "提出第一个附加问题：这样是否把一切交给生活的毒打，理想与追求是否都没了。", "role": "transition"},
    {"unit_id": "U011", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031"], "summary": "回到狮子：其懒办法能活几十年并非运气，而是饥饿才捕食的频率维持了猎物与狮子的平衡；生活的毒打节奏与本能敏感性由数百万年自然大数据调校。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P032"], "summary": "主张生活负面反馈指向的方向往往是人类智慧无法理解的正确答案，并称这涉及信仰问题。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038"], "summary": "主张目标本身无所谓客观正确，能否坚持取决于对“这个选择充满绝对智慧”的信念强度；相信生活的毒打自有美意比相信自己更易坚持。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "第二个附加好处：因毒打而取得的方向没得怨没得恨，省下怨人的精力。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P043", "P044", "P045", "P046"], "summary": "定义“打麻醉”为与改善处境无关、以净消耗精力资源为代价试图忘记负面感受的措施，并以睡觉不算、通宵游戏算作说明。", "role": "definition"},
    {"unit_id": "U016", "paragraph_refs": ["P047", "P048"], "summary": "判定酗酒、吸毒当然算打麻药，其余情形让读者自行套用。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面对“如何克服懒散”，应多挨生活的毒打；这不是抖机灵开玩笑。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "动物（如狮子）要等肚子饿了才有足够斗志和动力去打猎，不饿时驱赶也不去；幸存主要靠休息而不是“努力”。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "休息是低消耗、安全、稳妥的，“努力”是高消耗、有风险、充满不确定性的，因此能休息就应先休息。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每天被焦虑驱使到处乱摸乱试是速死之道；懒散习性写在生物本能底层，但这种安排本身是健康的。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人应该接受这一安排并顺应它去追求更好的结果，而不是感到负罪、胡作非为乃至毫无意义地耗尽自己。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "懒散到不该再懒散时生活就会主动来毒打，挨打记忆会塑造出恰当的焦虑传感器，懒散下限自然调整。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题出在很多人挨了生活的毒打却用上麻药（上网喷人、抽烟喝酒、六合彩、网络贷、以贩养吸等），以致痛觉丧失。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "要改的根本不是懒，而是打麻药；停止打麻药后就不需要再问“怎么可以改变懒散”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人不是比你勤奋，而是比你敏感。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "狮子能顺利活几十年并非运气，而是饥饿才捕食的频率维持了猎物与狮子的平衡；“生活”不是随随便便毒打你的。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "生活毒打的节奏与本能中的天然敏感性由数百万年乃至上亿年的自然大数据调校，其复杂机制“至少在青少年时期”不可能参详得透。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "生活给人的负面反馈所指向的方向往往是人类智慧无法理解的正确答案；作者称这涉及信仰问题，信不信由读者，但能信会省下不少看抑郁症的钱。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人追求哪个目标、哪个理想无所谓客观正确；是否正确更多甚至决定性地取决于对“这个选择充满着绝对智慧”这一命题的信念坚强程度，不选生活的指向则易因自我否定而崩溃。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何方向都无所谓对错，坚持得住的就是对，坚持不住的就是错；相信“生活的毒打自有美意”远比相信自己英明神武来得容易坚持。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因生活的毒打而取得的努力方向没得怨、没得恨；就凭这一点，躺着都赢了一半。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“打麻醉”指那些与改善危机处境无关、以净消耗精力和资源为代价、试图让你忘记负面感受的措施；睡觉一般不算，为消解考试压力打两通宵游戏则算，酗酒吸毒当然算。", "evidence": ["E22", "E23", "E24"]}
   ],
   "argument_steps": [
    "直接作答：多挨生活的毒打，并排除玩笑（P001-P002）。",
    "以狮子类比：懒散、饿才打猎（P003-P005）。",
    "归纳一般命题：幸存靠休息而非努力，休息低耗安全（P006-P008）。",
    "反面论证：焦虑驱使到处乱试是速死之道（P009）。",
    "给出本能解释：懒散习性写在生物本能底层，且该安排健康（P010-P011）。",
    "给出行动方向：接受并顺应安排，避免负罪与无意义消耗（P012）。",
    "机制说明：毒打→挨打记忆→焦虑传感器→懒散下限调整（P013-P014）。",
    "把“顺应”定义为对“我正在被毒打”敏感一点，并列出毒打逐级升级的清单（P015-P017）。",
    "诊断真正问题：用麻药解决毒打，痛觉丧失（P018-P019）。",
    "收束：停止打麻药，问题不成立；别人只是比你敏感（P020-P022）。",
    "自设第一问：是否把一切交给毒打、理想追求怎么办（P023-P025）。",
    "再用狮子回答：懒办法能存活源于猎物与狮子的平衡，非运气（P026-P028）。",
    "提升为秩序论：毒打节奏由长期自然大数据调校，机制深不可测（P029-P031）。",
    "提出信念论：负面反馈指向正确答案，属信仰问题（P032）。",
    "展开信念论：目标无客观正确，坚持取决于信念强度，故应选更易坚持的“生活指向”（P033-P038）。",
    "补充第二好处：毒打选的方向没得怨（P039-P042）。",
    "自设第二问：什么叫打麻醉，给出定义与判例（P043-P046）。",
    "补充判例：酗酒吸毒算，其余套用（P047-P048）。"
   ],
   "concept_usage": [
    {"term": "懒散（懒散习性）", "meaning": "文中指“有得混就一直混，实在没得混才动一动”的行为模式，作者称其写在生物本能底层、本身健康，而非道德缺陷。", "evidence": "P010", "ambiguity": "作者未区分生物性节能与习得性拖延，二者在文中被合并处理。"},
    {"term": "毒打（生活的毒打）", "meaning": "泛指生活给出的负面反馈与惩罚；作者认为其节奏有内在合理性，并能塑造人的焦虑传感器。", "evidence": "P013", "ambiguity": "作者未界定毒打的具体形式与强度阈值。"},
    {"term": "打麻药（打麻醉）", "meaning": "与改善危机处境无关、以净消耗精力和资源为代价、试图让人忘记负面感受的措施。", "evidence": "P044", "ambiguity": "判据是“净消耗”还是“是否改善处境”，文中两说并见；睡觉为何不算的解释依赖“睡醒更充沛”这一条件。"},
    {"term": "焦虑传感器", "meaning": "由挨打记忆塑造出的、能维持恰当懒散下限的感知机制。", "evidence": "P013", "ambiguity": "该机制是否可主动训练，正文未说明。"},
    {"term": "敏感（比人敏感）", "meaning": "指对生活中的负面反馈察觉更快，作者以此替代“勤奋”作为他人优势的解释。", "evidence": "P021", "ambiguity": "未说明敏感性是否可培养。"},
    {"term": "自然大数据调參", "meaning": "作者用语（原文作“调參”），指数百万年乃至上亿年的自然选择过程调校出毒打节奏与本能敏感性的匹配。", "evidence": "P030", "ambiguity": "“调參”为原文用字，疑为方言或异体写法，未作改动；该比喻非实证表述。"},
    {"term": "绝对智慧", "meaning": "指作者要求读者对“这个选择充满着绝对智慧”这一命题持有的信念内容，用于支撑坚持。", "evidence": "P033", "ambiguity": "作者称此涉及信仰问题，未给出可验证判据。"}
   ],
   "examples_and_targets": [
    "非洲的狮子：全篇核心类比证据，用于说明懒散、饿才捕食、休息为主的生存策略（P003-P005、P026-P028）。",
    "上网喷人、抽烟喝酒、六合彩、网络贷、以贩养吸：作为“打麻药”的具体例举（P019）。",
    "打两通宵游戏转移注意力以消解考试压力：作为“打麻醉”的判例（P046）。",
    "睡觉：作为不算打麻醉的反例（P045）。",
    "酗酒、吸毒：作为当然算打麻醉的判例（P047）。",
    "“连续有几次狮子都是饿了才出去捕食结果运气都不好于是终于饿死了”的假想剧本：作为被否定的假设情景（P027）。",
    "分科时/报志愿时/找工作时/跳槽时/创业时：作为“相信自己英明神武”的时间节点例举（P037）。",
    "抑郁症、网游封号、家破人亡：作为成本后果与修辞材料（P016、P032）。"
   ],
   "conditions": [
    "“幸存主要靠的是休息”以能量消耗与风险对比为条件，作者未限定物种范围（P006）。",
    "P010以“有得混就一直混，实在没得混才动一动”描述人类习性的实际表现条件。",
    "懒散下限的调整依赖“懒散到不该再懒散了”这一临界点出现且生活确实给出毒打（P013）。",
    "毒打的有效性以人未使用麻药、痛觉仍存为前提（P018-P019）。",
    "狮子存活结论以“猎物丰富了”维持捕食频率平衡为条件（P028）。",
    "“至少在青少年时期不可能参详得透”为时间限定（P030）。",
    "信念论以“信不信由你”为条件，作者明确承认其属信仰范围（P032）。",
    "“睡觉不算打麻醉”以“你睡醒了会精力更充沛，会给你应对危机带来更好的条件”为判据（P045）。",
    "“打两通宵游戏算”以“打完这两天你并没有获得更多的资源和精力来应对问题”为判据（P046）。"
   ],
   "rhetoric_and_tone": "答疑式口语短句，第二人称“你”贯穿，语气戏谑而带训诫：以狮子作贯穿全篇的类比，用“毒打”“打麻药”“焦虑传感器”“自然大数据”等比喻构筑解释框架；“家破人亡都不行，改网游封号”“非要把你的道具都扣了你才知道厉害”带调侃与夸张；P022 标题句“要改的根本不是懒，而是打麻药”为结构转折点；对“用麻药”者语气严厉（“痛觉整个都没了”），对读者则作劝服与免责（“信不信由你啦”）。",
   "unresolved_questions": [
    "P030“数百万年乃至于上亿年的自然大数据调參”中的“调參”用字特殊，疑为异体或方言写法，未改动，可能影响解读。",
    "非洲狮子“有时一天睡二十个小时”及“饥饿才捕食”的行为描述属事实断言，需外部核查（P003、P005）。",
    "“打麻药”的判据在文中兼有“是否改善处境”和“是否净消耗”两条，两者在边界情形（如娱乐性运动）上可能冲突，正文未裁决。",
    "“焦虑传感器”“懒散下限”均为比喻性表述，未界定可观测指标。",
    "作者称“能信的话你会省下不少看抑郁症的钱”为预测，无数据支持，需外部核查（P032）。",
    "作者未说明该方案对已形成成瘾行为者是否适用，仅指出麻药是问题所在（P018-P019）。",
    "P033“你不选‘生活的指向’，选‘自己的决定’”中“生活的指向”如何辨识，正文未给出操作标准。",
    "本篇无图片节点，无版本差异记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "多挨生活的毒打。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "它们还真的是要等肚子饿了才有足够的斗志和动力去打猎。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "实际上，幸存主要靠的是休息，不是“努力”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "休息是低消耗的、安全的、稳妥的，“努力”是高消耗的、有风险的、充满不确定性的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "每天被焦虑驱使着到处乱摸乱试，是块石头都翻一下，有枣没枣都戳三杆子，这是速死之道", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "但这种安排本身是健康的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "人应该做的是接受这一点，学会顺应这个安排去追寻更好的结果", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "懒散到不该再懒散了，生活就会主动来毒打你", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "问题出在很多人挨了生活的毒打，却用上麻药解决。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "从上网喷人到抽烟喝酒到六合彩到网络贷到以贩养吸", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "要改的根本不是懒，而是打麻药。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "停止打麻药，弹一下脑崩儿就够了", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "人家根本不是比你勤奋，人家是比你敏感。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P028", "quote": "狮子饿了肚子才去捕食的这个频率维持了猎物与狮子的平衡。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "“生活”不是随随便便毒打你的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P030", "quote": "这里面蕴含着你至少在青少年时期不可能参详得透的深不可测的复杂机制", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P032", "quote": "生活给人的负面反馈所指向的方向，往往是人类的智慧所无法理解的正确答案。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "是否正确更多的——甚至是决定性的——取决于你对于“这个选择充满着绝对智慧”这个命题本身的信念坚强程度。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P036", "quote": "其实任何方向都无所谓对或者错，坚持得住的就是对，坚持不住的就是错。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P037", "quote": "远比相信“分科时 / 报志愿时 / 找工作时 / 跳槽时 / 创业时……的自己英明神武”来得容易坚持。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P042", "quote": "不客气的说，就这一条，你躺着都赢了一半。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P044", "quote": "就是那些与改善危机处境无关，要以净消耗精力和资源为代价，试图让你忘记负面感受的措施。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P045", "quote": "一般来说，睡觉就不算，因为你睡醒了会精力更充沛", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P046", "quote": "为了消解即将考试的压力打两通宵游戏转移注意力就算", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P003", "quote": "你看到非洲的狮子够懒散吧——它们有时一天睡二十个小时，再懒点就直接长眠了。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["行为与习惯", "进化与生物本能", "心理与情绪调节", "人生方法与信念"],
   "issue_candidates": ["懒散是否需克服", "休息与努力的代价比较", "止痛式应对（麻药）与成瘾", "焦虑与敏感性的作用", "目标选择的信念基础", "归因与怨怼"],
   "text_function_candidates": ["答疑", "解释", "经验总结", "劝诫"],
   "object_candidates": ["提问者", "非洲狮子", "猎物", "读者（第二人称“你”）"],
   "working_keywords": ["懒散", "毒打", "打麻药", "焦虑传感器", "敏感", "自然大数据", "绝对智慧", "坚持"]
  },
  "notes": "提问者预设“懒散习性需要克服”，作者明确不接受该预设并把问题改写为“改打麻药”，故本篇含对提问前提的否定，不得把“克服懒散”写成作者主张。P030“调參”为原文用字，未改动、未按常见写法替换。P032、P033 涉信仰表述，作者自己以“信不信由你”标明不可强证，初读不作真伪判断，仅登记为待外部核查。无图片节点。"
 },
 "12b7d5cf": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者（Q001）问“什么是执行力？”，属概念界定类提问。作者不给出抽象定义，而以“推动进度条的神秘力量”作比喻性界定，并把大部分人的问题定位为做事没有进度条，随后补充两种制作进度条的方法及其适用边界。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以“推动进度条的神秘力量”比喻界定执行力，并提出首先要有进度条。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "主张大部分人的问题在于做事没有进度条，并以打游戏有进度条作对照。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "给出第一种方法“工时法”：统计关键路径上必要步骤的工时并折算时间价值，完成后按估计工时而非实际耗时计进度。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "以五步骤0.2/0.25/0.25/1/0.3个工时为例，说明累计进度为10%、22.5%、100%的计算方式。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "回应“估计错误怎么办”：不作处理，实际工时只记录、修正留到下次，反复做多次后才有可靠基线。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "给出第二种方法“当（dang4）值法”：把步骤拆成无瓶颈流水线，按各环节工资摊平得出每步价钱，以价钱代替时间算百分比权重。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "说明当值法更精确、更有参考意义，并称工时法培养技术专家／手艺人、当值法培养管理者／business owner，三者构成三重进阶并指向一番事业。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "处理无法推算进度的事情：这类事最好不是专业而是兴趣娱乐爱好；若是专业则说明能力见识管理能力不够，建议退后一步、自降级别，并称“胜任”的关键标志之一是能算出进度条。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030", "P031"], "summary": "重申允许甚至很大的误差，“算不出来”指误差放宽仍搞不定；此时应借助更专业的人或先进学习阶段，因而这是一个不需要解决的伪问题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "执行力就是传说中推动进度条的神秘力量。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大部分人的问题在于做事没有进度条；打游戏打得飞起很大程度上是因为有进度条。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "工时法按关键路径上必要步骤的估计工时折算时间价值，完成一步即获得该步工时对应的进度，不按实际耗时计算；估计错误不作处理，实际工时只记录，修正留到下次。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当值法把步骤拆成请工人机械完成的流水线、设计环节不要有瓶颈，按各步摊平后的工资价钱代替时间计算百分比权重。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "当值法比单纯的工时法更精确、更有参考意义；工时法培养技术专家／手艺人，当值法培养管理者／business owner，构成三重进阶并最终指向一番事业。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无法用这些办法推算进度的事情最好不要是你的专业，而是你的兴趣、娱乐、爱好。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果做不出哪怕带误差的进度统计手段的事正是你的专业，意味着你的能力、见识、管理能力实际上不够应对这件工作，建议退后一步、自降级别。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“胜任”的关键标志之一是能算得出这个进度条；算不出来不要强干，算得出来再动手。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "允许有误差甚至可以有很大的误差；“算不出来”是指误差打得很宽都搞不定，那么这事最好别强干，必须借助更专业的人或先经历学习阶段。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因此“无法推算进度的事情怎么办”实际上是一个不需要解决的伪问题。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "以比喻给出执行力的通俗界定（P001）。",
    "提出操作前提：先要有进度条（P002）。",
    "诊断现状：大部分人的问题是没有进度条（P003）。",
    "以游戏体验作对照说明进度条的作用（P004）。",
    "引入方法一：工时法，统计关键路径必要步骤工时并按估计工时计进度（P005-P008）。",
    "举例：五步骤工时合计与10%／22.5%／100%的累计算法（P009-P010）。",
    "自设疑问并回答：估计错误不处理，实际工时只记录，修正留到下次；重复多次后才有可靠基线（P011-P014）。",
    "引入方法二：当值法，拆流水线、避免瓶颈、按工资摊平得各步价钱（P015-P019）。",
    "补充判断：某些步骤费时费力但用普工反而便宜，故当值法更精确（P020-P021）。",
    "给出进阶论：工时法等值于技术专家、当值法等值于管理者，三重进阶指向一番事业（P022-P023）。",
    "处理剩余情形：算不出进度的事宜作兴趣而非专业（P024-P025）。",
    "若属专业则判定能力不足，建议自降级别（P026-P027）。",
    "给出判据：胜任的标志之一是算得出进度条（P028）。",
    "限定误差范围并给出出路：借助更专业的人或先学习（P029-P030）。",
    "结论：这是伪问题（P031）。"
   ],
   "concept_usage": [
    {"term": "执行力", "meaning": "文中未作抽象定义，以“推动进度条的神秘力量”作比喻性界定，实际等同于“能把事情按可测进度推进的能力”。", "evidence": "P001", "ambiguity": "比喻未给出可操作定义，作者随后转谈进度条方法。"},
    {"term": "进度条", "meaning": "把一件事的完成程度量化成百分比的机制；文中给出工时法与当值法两种构造方式，并被当作“胜任”的判据。", "evidence": "P002", "ambiguity": "作者未说明进度条是否适用于创作、研究等难以拆步的工作。"},
    {"term": "关键路径", "meaning": "工时法统计工时的对象范围；作者以括号让读者“自己去查一下什么叫关键路径”，未在本文定义。", "evidence": "P007", "ambiguity": "定义外包给读者自行查阅，本文未给界定。"},
    {"term": "时间价值", "meaning": "按工时折算出的每个步骤权重，用于计算累计进度百分比。", "evidence": "P007", "ambiguity": "未说明与真实紧迫度的关系。"},
    {"term": "当（dang4）值法", "meaning": "以流水线各环节工资摊平后的“价钱”代替时间来计算步骤权重的方法；作者标注读音 dang4，疑为“当值”的自定义用法。", "evidence": "P015", "ambiguity": "“当值”一词为作者自造或方言用法，与常见词义不同，需注意歧义。"},
    {"term": "胜任", "meaning": "文中以“能算得出这个进度条”作为其关键标志之一。", "evidence": "P028", "ambiguity": "作者称其为“关键标志之一”，未列出其他标志。"},
    {"term": "伪问题", "meaning": "指“无法推算进度的事情怎么搞进度条”这一提问，作者认为应通过降低级别或求助他人来处理，而非解决。", "evidence": "P031", "ambiguity": "该判断依赖 P025-P030 的建议，非独立论证。"}
   ],
   "examples_and_targets": [
    "打游戏打得飞起：作为“有进度条”的类比证据（P004）。",
    "五个步骤0.2 / 0.25 / 0.25 / 1 / 0.3 个工时及其10%、22.5%、100%的累计进度：作为工时法的计算示例（P009-P010）。",
    "流水线、请工人、发工资、一天做一百件：作为当值法的设想情景（P016-P018）。",
    "容易找到的普工与“要本科生才能安全搞定”的步骤：作为当值法更精确的例证（P020）。",
    "关键路径：以括号要求读者自查，作为外部知识引用（P007）。",
    "兴趣、娱乐、爱好、专业、“吃饭的家伙”：作为无法推算者的分类处置对象（P025-P026）。",
    "IMG001（src=//asset.sooon.ai/p/2020-08/17/cbdef2764a6d63ea3b1a9fa5e45aaae7.jpg）：本篇唯一图片节点，内容未核验，图片可能承载正文之外的补充说明（P032-P034 区段附近）。"
   ],
   "conditions": [
    "工时法的进度计算以“按你完成的步骤本身估计的工时数来算”为条件，不按实际耗时（P008）。",
    "估计错误不作修正，以“要修正也是下次修正”为条件，故需重复多次才有可靠基线（P012-P014）。",
    "当值法以“设计好流水线的环节，不要有瓶颈”为条件（P016）。",
    "当值法比工时法更精确的判断以“有的步骤可能要本科生才能安全搞定”这类差异存在为条件（P020）。",
    "“最好不是你的专业”的处置以该事属兴趣娱乐爱好为条件；若确属专业则触发能力不足的判断（P025-P026）。",
    "“算不出来”的判定带明确限定：允许很大误差，仅当误差打得很宽仍搞不定才算（P029）。",
    "出路限于两条：借助更专业的人，或先经历一个学习阶段（P030）。"
   ],
   "rhetoric_and_tone": "答问式短文，语气务实的指导口吻：以“神秘力量”的调侃开篇，随即转为方法说明；用“凉拌，啥也不办”“自己套用吧”式的口语消解严肃感（P012）；以“再提醒一遍”“建议你”作劝导；对能力不足者不嘲讽而给退让建议（P027、P029）。结构上为“定义—方法一—质疑回应—方法二—边界处理—结论”，编号与括号（如“当（dang4）值法”）带讲稿或教材笔记感。",
   "unresolved_questions": [
    "IMG001 图片未核验：本篇含 1 个图片节点，无读图能力，图片内容（疑为进度条示意或流程图）未经核对，需人工或多模态复核，故本篇状态为 needs_reread。",
    "图片节点在文本中的确切位置为 P031 之后（lexical 记 paragraph 34、image 1），其承载的说明内容无法从正文推定。",
    "“关键路径”在本文被要求读者自查，未给出定义，属外部知识依赖，需核查作者所指是否为项目管理中的同一概念（P007）。",
    "“当（dang4）值法”名称与常见词义不同，作者标注读音但未给出定义来源，存在术语歧义（P015）。",
    "P023“没有进度条 》 有工时进度条 》有当值进度条”中的“》”用法不明，可能表示“优于”或“递进”，影响对三重进阶方向的理解。",
    "“business owner”等英文词混入正文，未作解释，可能属作者原用语。",
    "作者未说明进度条方法在创作、研究等不可拆步工作中的适用性。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "执行力，就是传说中推动进度条的神秘力量。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "大部分人的问题在于做事没有进度条。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "将整个关键路径（自己去查一下什么叫关键路径）上的必要步骤的工时都统计出来，按工时折算出该步骤的“时间价值”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "不是按照你实际花了多久来算，而是按你完成的步骤本身估计的工时数来算。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P016", "quote": "把所有的步骤拆开，想象你有一条流水线，每一个环节你都请了一些工人来机械完成。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P021", "quote": "实际上这个当值法比单纯的工时法更精确，更有参考意义。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P022", "quote": "工时法实际上是在培养自己做一个技术专家，一个手艺人，而当值法是在培养自己做一个管理者，一个business owner。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P025", "quote": "很简单——这类事最好不要是你的专业，而是你的兴趣、娱乐、爱好。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P026", "quote": "那么你要意识到做不出哪怕带着误差的进度统计手段意味着你的能力、见识、管理能力实际上不够应对这件工作。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P027", "quote": "建议你先退后一步，自降级别，不要贪多嚼不烂。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P028", "quote": "“胜任”的关键标志之一就是能算得出这个进度条。算不出来，不要强干，算得出来再动手。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P029", "quote": "“允许你有误差”，甚至可以有很大的误差。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P030", "quote": "你必须借助更专业的人来帮你干，或者你必须先经历一个学习阶段，先摸到眉目再说。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P031", "quote": "所以这实际上是一个不需要解决的伪问题。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "凉拌，啥也不办。你可以把实际花费的工时记录下来，但是算进度还是要按估计工时来算。要修正也是下次修正。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P004", "quote": "你们打游戏打得飞起，很大程度上是因为有进度条。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["工作方法与项目管理", "个人效率", "能力评估"],
   "issue_candidates": ["执行力的界定", "进度量化方法", "工时法与当值法比较", "胜任的判据", "无法量化事务的处置"],
   "text_function_candidates": ["答疑", "解释", "经验总结", "教程式说明"],
   "object_candidates": ["提问者", "读者", "管理者", "business owner", "技术专家", "普工", "本科生"],
   "working_keywords": ["执行力", "进度条", "关键路径", "工时法", "当值法", "时间价值", "瓶颈", "胜任", "伪问题"]
  },
  "notes": "本篇含 1 个图片节点（IMG001，src=//asset.sooon.ai/p/2020-08/17/cbdef2764a6d63ea3b1a9fa5e45aaae7.jpg），图片内容未经核验，需图像核验；已读部分为正文文本，故 status=needs_reread、image_checked=False。图片在 lexical 中的位置为 P031 之后，正文文本在 P031 已收束，图片是否承载额外结论无法从文本推定，不得据上下文补写其内容。另注：brief 为正文前若干句的截断预览（末尾停在“必要步骤”），不作主张依据；标题《执行力》与提问“什么是执行力？”一致，作者以比喻作答而未给学理定义。"
 },
 "8a0542d0": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何发自内心地宽恕一个人？”，即寻求达成内心真实宽恕的路径。作者给出两条要点：先想明白为什么一开始就不该怪对方并为此歉疚，且在想明白之前不放弃；并主张宽恕的唯一办法不是在定罪之后宽免惩罚，而是根本不去定人的罪。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "第一条要点：想明白为什么一开始就不该怪别人，并为自己不公平地责怪对方而歉疚。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "以三次递进强调：想不明白也不放弃，直到想明白为止。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "提出宽恕的唯一办法：不是在定了对方罪之后去宽免惩罚，而是不去定人的罪。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要发自内心宽恕，须想明白为什么一开始就不该怪别人，并为自己不公平的责怪对方而歉疚。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想不明白也不放弃，还想不明白还是不放弃，要想明白为止。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果你真的想要原谅对方，唯一的办法不是在定了对方罪之后去宽免惩罚，而是不去定人的罪。", "evidence": ["E4", "E5"]}
   ],
   "argument_steps": [
    "给出第一条行动要求：想明白不该怪对方并为此歉疚（P001）。",
    "针对想不明白的情形，以连续三次否定式要求排除放弃（P002-P004）。",
    "给出更根本的条件句判断：真宽恕的唯一办法是不去定人的罪，而非定罪后宽免惩罚（P005-P006）。"
   ],
   "concept_usage": [
    {"term": "宽恕（原谅）", "meaning": "文中指发自内心的原谅；作者把它与“定了罪之后去宽免惩罚”区分开，主张真正的宽恕在于取消定罪这一前置步骤。", "evidence": "P005", "ambiguity": "作者未说明“不去定人的罪”与“认为对方无过错”是否为同一件事。"},
    {"term": "不该怪", "meaning": "指一开始就不应把责任归于对方；作者要求读者想明白这一点并由此产生歉疚。", "evidence": "P001", "ambiguity": "作者未论证为何“一开始就不该怪别人”普遍成立，也未给出判断标准。"},
    {"term": "定罪", "meaning": "指对对方作出有罪的判定；作者视之为宽恕的障碍，认为应先取消这一判定。", "evidence": "P006", "ambiguity": "宗教或法律语义是否被借用，正文未说明。"}
   ],
   "examples_and_targets": [
    "本篇未提供人物、事件、机构、数据或历史叙述，全文为针对“你”与“对方”的一般化表述（P001-P006）。",
    "“如果你真的想要原谅对方”为条件句修辞材料，用于限定该办法的适用读者（P005）。"
   ],
   "conditions": [
    "P001以读者能“想明白”为条件，属要求而非已完成事实。",
    "P002-P004以“想不明白”为前提反复要求不放弃，未限定所需时间或方法。",
    "P005明确以“如果你真的想要原谅对方”为条件，即该唯一办法只对该目的成立。",
    "全文未限定对象关系、事件性质或严重程度。"
   ],
   "rhetoric_and_tone": "极简短篇，六段短句，语气如格言或训诫：用“想不明白也不放弃／还想不明白，还是不放弃／想明白为止”的排比递进施压；末两段以“不是……而是……”的对举句式给出核心判断。无调侃、无例子、无第二人称之外的称呼，对读者直接要求。",
   "unresolved_questions": [
    "正文未说明“想明白为什么一开始就不该怪别人”的具体理由或判据，也未处理明显过错方的情形。",
    "“不去定人的罪”与“不认为对方有错”的区别未说明，存在解读歧义。",
    "作者未说明该方法是否适用严重伤害、犯罪等情形。",
    "本篇正文仅 107 字符（P001-P006），brief 中的“如果你真的想要原谅对方，唯一的办法不是在定了对方罪之后去宽免惩罚，”与 P005 重合，属预览而非额外内容。",
    "question 属提问者，其“发自内心”的限定未在正文中被直接回应，正文未讨论“内心真实”如何验证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "想明白为什么一开始就不该怪别人，并且为自己不公平的责怪对方而歉疚。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "想不明白也不放弃。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "还想不明白，还是不放弃。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "如果你真的想要原谅对方，唯一的办法不是在定了对方罪之后去宽免惩罚，", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "而是不去定人的罪。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与人际关系", "伦理与道德"], 
   "issue_candidates": ["宽恕的达成方式", "责怪与归因", "定罪与惩罚的关系"],
   "text_function_candidates": ["答疑", "劝诫", "格言式短答"],
   "object_candidates": ["提问者", "读者（“你”）", "被宽恕的“对方”"],
   "working_keywords": ["宽恕", "原谅", "歉疚", "责怪", "定罪", "宽免惩罚", "不放弃"]
  },
  "notes": "本篇为极短篇（正文 107 字符，6 个段落），无图片节点，无版本差异记录。作者未举例、未论证“一开始就不该怪别人”的理由，属断言式劝诫；不得外补理由。brief 与正文局部重合，为预览性质，未据以补写正文。"
 },
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
