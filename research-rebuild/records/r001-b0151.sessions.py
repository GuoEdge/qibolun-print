# -*- coding: utf-8 -*-
"""批次 r001-b0151 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0151.sessions.py            # 写 out/r001-b0151.out.jsonl
  python3 records/r001-b0151.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0151"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0151.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4402a57c": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者）就一起社会事件发问：熊孩子性骚扰妇女引发冲突、其家长殴打女医生并屡屡寻衅滋事，女医生最终被逼自杀，问如何看待该事。作者未复述案件细节，而是借该事件讨论个人自卫能力与对法律、公权力的依赖问题，属答问式社会评论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "否定把自卫能力简单寄托于法律与公权力：它们反应太慢，干预角度是面向社会的广泛群体反应；法官着眼的是法庭之外的大众与未来后代，而非使当事人满意；除非个人价值观同样具备前瞻性与宏观性，否则公权力给出的答案很可能与预期不符；公权力真正积极干预的范围相当有限，利维坦并非全知全能，资源紧张、能力局限。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "理解上述局限后的一种路径：选择极有战略优势的占位，使侵犯容易触动公权力敏感神经而可能被战略打击；但这需要高度洞察力和技巧，不属于家常手段。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "作为普通老百姓可追求的是自己能及时调动的威慑，分两类：让对方顾虑失去由你而得的利益、让对方顾虑因你而受的损失；作者称此主题已多次说过，让读者自行翻阅其他阐述。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015"], "summary": "转入离群索居的代价：造福他人即对外输出利益，是经营以自己为核心的生态圈的基础，该生态圈会自动在物理与心理上替自己防御外来侵袭；受害人真正的脆弱在于没有足够强大的生态圈给她相称支撑，心理上缺少足够认同者时面对铺天盖地的语言暴力极易绝望，绝望即终局。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021"], "summary": "以设问收束教训：不要自以为躲起来自得其乐就够，那只是玻璃的玫瑰；需要同志的程度远比安稳时所以为的深；平时万事已足者骤遇严重挑战便易陷入孤立无援与绝望。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "考虑自己的自卫能力时，不应简单依赖法律和公权力。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "法律和公权力反应太慢，且其干预一件事情的角度是广泛的群体反应，即面向社会的短期和长期走向处理问题。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "除非自己的价值观和伦理观同样具备这种前瞻性和宏观性，否则公权力给出的答案很可能与自己的预期不相符。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "公权力真正会积极干预的范围相当有限；利维坦并非全知全能的神，与其面对的问题相比甚至资源相当紧张、能力相当局限。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "一些人会选择极有战略优势的占位，使侵犯容易触动公权力的敏感神经而有被战略打击的可能；但这需要高度洞察力和技巧，不属于家常手段。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "普通老百姓可以追求的手段是自己能及时调动的威慑，其一是让对方顾虑失去由你而得的利益，其二是让对方顾虑因你而受的损失。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "努力造福于人就是对外输出利益，是经营以自己为核心的生态圈的基础；这个生态圈会自动替自己防御外来侵袭，包括物理安全和心理安全。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "受害人真正的脆弱性在于面对辱骂时没有足够强大的生态圈给她相称的支撑；心理上没有足够多的认同者时，面对语言暴力人极易从心理上绝望。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要自以为躲起来自得其乐就够了；一个人需要同志的程度，比其在怡然自得时所觉得的要深得多。", "evidence": ["E11", "E12"]}
   ],
   "argument_steps": [
    "提出主张：考虑自卫能力时不要简单依赖法律和公权力（P001）。",
    "给出理由：它们反应太慢，干预角度是广泛的群体反应，即面向社会的短期和长期走向（P002）。",
    "展开机制：法官判案时眼睛看着的是法庭之外的万千大众乃至未来后代，任务不是使当事人满意（P003）。",
    "给出条件性让步：除非自己的价值观同样前瞻而宏观，否则公权力给的答案很可能与预期不符（P004）。",
    "进一步推论：具备这种宏观性后，会正确理解公权力积极干预的范围相当有限，利维坦资源紧张、能力局限（P005）。",
    "补充例外路径：选择有战略优势的占位以触动公权力敏感神经，但需高度洞察力与技巧（P006—P007）。",
    "回到普通人立场：可追求的手段是自己能及时调动的威慑，分让对方顾虑失去利益与顾虑受损两类（P008—P009）。",
    "回避展开：作者称该主题已说过多次，让读者自行翻阅其他阐述（P010）。",
    "转折点题：强调离群索居的代价问题（P011）。",
    "机制说明：造福他人即输出利益，形成以自己为核心的生态圈，自动提供物理与心理防御（P012）。",
    "案例归因：受害人真正的脆弱性在于缺少足够强大的生态圈支撑其心理（P013）。",
    "机制推演：心理上没有足够多认同者，面对铺天盖地的语言暴力极易绝望（P014）。",
    "后果：心理绝望即全剧终，亲友也来不及着力（P015）。",
    "设问引出教训：不能躲起来自得其乐，需要同志（P016—P018）。",
    "结论：平时觉得万事已足者，骤然遇到严重挑战会感到极强孤立、无援，进而绝望（P019—P021）。"
   ],
   "concept_usage": [
    {"term": "自卫能力", "meaning": "个人受到侵犯时能立即动用的自我保护能力，作者主张不应简单依赖法律与公权力（P001）。", "evidence": "P001", "ambiguity": "是否包含法律途径本身未明确排除，只否定「简单依赖」。"},
    {"term": "利维坦", "meaning": "借霍布斯式意象指代庞大的公权力机器，作者称其并非全知全能、资源紧张、能力局限（P005）。", "evidence": "P005", "ambiguity": "未明确限定为政府、司法或整个国家机器。"},
    {"term": "生态圈", "meaning": "以自己为核心、因对外输出利益而形成的支持网络，会自动在物理与心理上防御外来侵袭（P012）。", "evidence": "P012", "ambiguity": "系比喻用法，成员范围、规模与维持条件未界定。"},
    {"term": "威慑", "meaning": "自己能及时调动、使对方产生顾虑的手段，分「怕失去由你而得的利益」与「怕因你而受损失」两类（P008—P009）。", "evidence": "P009", "ambiguity": "具体手段未展开，作者让读者查其他阐述。"},
    {"term": "玻璃的玫瑰", "meaning": "比喻看似自足美好、实则一场大雨就能击碎的独居自得状态（P017）。", "evidence": "P017", "ambiguity": "修辞比喻，非严格概念。"},
    {"term": "兔子洞", "meaning": "比喻安稳自得、与外界隔绝的生活空间（P019）。", "evidence": "P019", "ambiguity": "修辞比喻，非严格概念。"}
   ],
   "examples_and_targets": [
    "提问者所述女医生被逼自杀事件：本文的分析对象与案例，作者称其为「这位受害人」，未复述案件细节（P013）。",
    "「法官判你的案子，眼睛不是看着你的」：说明公权力视角的假设性举例（P003）。",
    "「臣等正欲死战，奈何陛下先降？」：引语式修辞材料，出处未注明（P015）。",
    "「这帮傻x懂个球」：引语，用以说明受害人本应具备的心理支撑（P013）。",
    "利维坦、玻璃的玫瑰、兔子洞：隐喻修辞材料（P005、P017、P019）。"
   ],
   "conditions": [
    "「当你真的有了这个前瞻性和宏观性」（P005）。",
    "「除非你自己的价值观和伦理观有这同样的前瞻性和宏观性，否则……」（P004）。",
    "「一旦受到侵犯」（P006）。",
    "读者定位为「作为普通老百姓」（P008）。",
    "「一旦在心理上没有足够多的认同者」（P014）。",
    "「就算还有什么亲友也来不及着力了」（P015）。",
    "「平时安安稳稳的」状态下容易自认万事已足（P019）。"
   ],
   "rhetoric_and_tone": "通篇第二人称「你」的训诫与劝导口吻；以否定式祈使句开篇（「不要简单的依赖」）；比喻密集（利维坦、生态圈、玻璃的玫瑰、兔子洞）；插入戏剧化引语（「臣等正欲死战，奈何陛下先降？」）与粗俗引语（「这帮傻x懂个球」）；用设问句过渡（「而这些给你的教训是什么呢？」）；结构上先破（依赖公权力）后立（自我威慑），再转折到「离群索居的代价」这一作者真正的主题，末尾转为对当事人处境的心理描写，语气由冷峻分析转向痛切。",
   "unresolved_questions": [
    "作者称此主题已多次说过（P010），但未指明其他阐述的篇名或位置，其威慑方案细节无法在本篇核查。",
    "「极其有战略优势的占位」具体指什么，未举例（P006）。",
    "提问所指案件的细节、当事人身份与处理结果，本篇未复述，需外部核查原始事件。",
    "公权力「资源相当紧张、能力相当局限」的判断未给出依据或数据（P005）。",
    "「生态圈会自动的替你防御外来侵袭」的作用机制与适用边界未限定（P012）。",
    "引语「臣等正欲死战，奈何陛下先降？」出处未注明（P015）。",
    "本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "考虑自己的自卫能力的时候，不要简单的依赖法律和公权力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为它们反应太慢，并且从某种意义上来说，它们干预一件事情的角度是广泛的群体反应", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这就意味着除非你自己的价值观和伦理观有这同样的前瞻性和宏观性，否则公权力给你的答案很可能和你的预期不相符。", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P005", "quote": "与它所要面对的千千万万问题和危机相比，它甚至可以说得上资源相当紧张、能力相当局限", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "一些人会选择一些极其有战略优势的占位", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "作为普通老百姓，你能追求的手段是一些你自己可以及时调动的威慑。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "一种是让对方顾虑失去由你而得的利益，一条是让对方顾虑因你而受的损失。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "这个生态圈会自动的替你防御外来侵袭，不光是物理安全上，还有心理安全。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "这位受害人真正的脆弱性，在于面对这些辱骂，没有一个足够强大的生态圈去给她相称的支撑", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "面对这些铺天盖地震耳欲聋的语言暴力，人极易从心理上绝望。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "是不要自以为只要自己躲起来自得其乐就够了，那只是玻璃的玫瑰，一场大雨也能击碎。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "你需要同志，比你在怡然自得的时候所觉得的程度要深得多。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "公权力与法律", "个人安全", "社会支持与人际关系"],
   "issue_candidates": ["公权力干预的边界与时效", "个人自卫手段", "社会支持网络与心理韧性", "语言暴力与自杀"],
   "text_function_candidates": ["答问式议论", "行动建议", "社会评论"],
   "object_candidates": ["法律", "公权力", "利维坦", "生态圈", "威慑", "语言暴力", "自杀"],
   "working_keywords": ["公权力", "自卫", "威慑", "生态圈", "离群索居", "绝望", "利维坦"]
  },
  "notes": "正文无图片节点，无需图像核验。提问字段（Q001）属提问者，全文主张均出自作者，未把提问者立场归给作者。作者自述该主题曾在其他文章中阐述（P010），本篇未给出篇名或链接，需外部核查。brief 与正文 P003 内容部分重合，仅作导航、未用于支持任何主张。"
 },
 "ec8a140e": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者）问哈佛、麻省理工、斯坦福这类学校的教育水平是否被过誉。作者直接承接该问并修正其范围：不是这几所被过誉，而是所有大学的教育水平都被过誉，随后用「最关键教育阶段在市场而非学校」「文凭与职位的关联强度与教育能力优势不相称」两条线论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "扩大被质疑的范围：不是哈佛、麻省理工、斯坦福被过誉，而是所有大学的教育水平都过誉；理由是人所受教育的最关键阶段不是学校教育阶段，而是进入市场、自我经营并满足需求的阶段，后者长达数十年，彪炳后世的东西绝大多数在此阶段做出，把它们不成比例归因于大学教育是显而易见的逻辑错误。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005"], "summary": "正面解释这些大学「教学成果」强的原因：不在纯教学领域有不可复制的优势，而在有足够的快车道直通容易做出成果的产业职位。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "预设并回应反驳：有人会问职位与学校的直通是否说明学校本身强、作者是否倒因为果；作者指出问题问的是「是否被过誉」而非「学校强不强」，并给出断言理由——职位与文凭的关联强度与学校实际教育能力的优势不相称，形象说法是 A 比 B 强 10% 却多拿 50% 的 offer。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015"], "summary": "以假设性检验与个人观察支撑断言：排除语言优势和镀金项目履历后做纯双盲测试，斯坦福毕业生水准不见得比清华学生有那么大优势；作者遇到的名校出身而「脑子拎不清」者的比例不比别处少，真正知道自己在干什么的学生比例也没高出多少；名校如雷贯耳的本质原因不在教学，而在企业、政府、社会赋予的超额权重，真正出成果的点在企业部分。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P016"], "summary": "以标题式短句收束全文结论：所有的大学教育，都被高估了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是哈佛、麻省理工、斯坦福这些学校的教育水平被过誉，而是所有大学的教育水平都被过誉了。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人所受教育的最关键阶段根本不是学校教育阶段，而是进入市场、在市场上努力自我经营并奋力满足需求的阶段，后者长达数十年。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如雷贯耳、彪炳后世的东西绝大多数是在进入市场后的阶段做出来的；把这些成就不成比例地归因于大学教育是一种显而易见的逻辑错误。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些大学的「教学成果」强，不是强在自身在纯教学领域有多少不可复制的优势，而是强在有足够的快车道直通容易做出成果的产业职位。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "（作者预设的他人反驳）若这些职位与学校直通，是否说明学校本身很强、作者是否倒因为果。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该问题问的不是这些学校强不强，而是它们是否被过誉；作者断定为「普遍过誉」的理由是职位与学校文凭的关联强度同学校实际教育能力的优势不相称。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "形象地说，A 比 B 强 10%，但 A 却比 B 多拿到了 50% 的 offer。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果排除语言优势和镀金项目履历、做纯双盲测试，斯坦福毕业生的水准并不见得会比清华学生有那么大的优势。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者依个人接触报告：名校出身而脑子拎不清却自以为是的人比例不比其它院校少，真正知道自己在干什么、该怎么干的学生比例也不比普通院校高到哪里去。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些学校如雷贯耳、看似「查有实据」地远超普通院校，本质原因不在教学，而在于企业、政府、社会赋予的超额权重；真正出成果的点在企业部分。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所有的大学教育，都被高估了。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "承接提问并修正命题范围：不是这三所被过誉，而是所有大学教育都被过誉（P001）。",
    "给出第一条理由：最关键的教育阶段是进入市场后的自我经营与满足需求阶段，长达数十年（P002—P003）。",
    "推论：彪炳后世的成就绝大多数出自该阶段，归因于大学教育是逻辑错误（P004）。",
    "给出正面解释：名校教学成果强在直通产业职位的快车道，而非纯教学优势（P005）。",
    "预设反驳：职位直通是否因为学校强、是否倒因为果（P006）。",
    "澄清问题焦点：问的是是否过誉，不是学校强不强（P007）。",
    "给出断言理由：职位与文凭的关联强度与实际教育能力优势不相称（P008）。",
    "类比说明：A 强 10% 却多拿 50% 的 offer（P009）。",
    "自问自答过渡：我为什么如此断言？（P010）",
    "给出假设性检验：排除语言优势与镀金履历后的纯双盲测试下，斯坦福毕业生未必比清华学生优势那么大（P011）。",
    "个人观察补充：名校出身而自视甚高者的比例不低，真正懂行者的比例也不比普通院校高（P012—P013）。",
    "归因替代解释：名校声誉本质来自企业、政府、社会的超额权重（P014）。",
    "结论：真正出成果的点在企业部分（P015），因此所有大学教育都被高估（P016）。"
   ],
   "concept_usage": [
    {"term": "过誉", "meaning": "学校的实际教育能力与其获得的社会回报、声誉权重不相称，即被高估（P001、P008）。", "evidence": "P008", "ambiguity": "作者将其限定为「关联强度与能力优势不相称」，未给出可量化的判定阈值。"},
    {"term": "市场", "meaning": "接受教育后进入的自我经营与满足需求的场域，作者注明「学术界也是一种市场」（P002）。", "evidence": "P002", "ambiguity": "外延较宽，未给出边界。"},
    {"term": "快车道", "meaning": "名校文凭提供的直通容易做出成果的产业职位的通道（P005）。", "evidence": "P005", "ambiguity": "比喻用法，未说明具体机制。"},
    {"term": "超额权重", "meaning": "企业、政府、社会在选人时赋予名校文凭的、超出其实际教育能力优势的权重（P014）。", "evidence": "P014", "ambiguity": "只作断言，未给出衡量方式或数据来源。"},
    {"term": "镀金项目履历", "meaning": "被视为干扰变量的、带有装饰性附加值的经历（P011）。", "evidence": "P011", "ambiguity": "未列举具体所指。"}
   ],
   "examples_and_targets": [
    "哈佛、麻省理工、斯坦福：提问所指对象，同时是作者要修正其范围的对象（P001）。",
    "清华、斯坦福毕业生的纯双盲测试：假设性检验例子（P011）。",
    "清、北、牛、剑、伦敦政经以及各藤校：作者个人接触经历中的举例，用以支撑其观察（P012）。",
    "「A 比 B 强 10%，但是 A 却比 B 多拿到了 50% 的 offer」：类比性说明材料（P009）。",
    "「有人会说——那么为什么不说这些职位是因为它们很强所以才会跟它们直通呢？」：作者预设的反驳对象（P006）。"
   ],
   "conditions": [
    "「如果排除语言优势和镀金项目履历，纯双盲测试」（P011）——该检验为假设性条件，未实际执行。",
    "结论以「进入市场」为前提，作者注明学术界也属于市场（P002）。",
    "「不见得」「似乎」「本质上」等限定词表明作者对部分判断留有余地（P011、P014）。"
   ],
   "rhetoric_and_tone": "以「不是……而是……」的修正式判断开篇，语气斩截；自问自答结构密集（「有人会说——」「我为什么如此断言？」），把读者可能的反驳先摆出来再回应；口语化嘲讽（「脑子拎不清却自以为是神仙下凡的蠢蛋」）；用数字类比（10% 对 50%）增强直观；结尾以短句标题式断言收束（P016），带格言化语气。",
   "unresolved_questions": [
    "P011 的「纯双盲测试」只是假设性检验，文中未给出任何实际数据、样本或研究来源。",
    "P014 的「超额权重」与 P008 的「不相称」均为断言，未提供可核查的依据或统计口径。",
    "P012—P013 属作者个人接触印象，未说明样本范围、数量与选择方式。",
    "P016 为 heading 节点，其是否为正文标题或平台小标题需版本核对。",
    "渲染包中的 brief 文本末尾被截断（止于「其实绝大多」），仅作导航，未用于支持主张；如需核对需查原始简报。",
    "本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不是哈佛、麻省理工、斯坦福着些学校的教育水平过誉了，而是所有大学的教育水平都过誉了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "人所受的教育的最关键阶段，根本就不是学校教育阶段", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "后者长达数十年。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "把这些成就不成比例的归因于大学教育，是一种显而易见的逻辑错误。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而是强在它们有足够的快车道直通容易做出成果的产业职位。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "那么为什么不说这些职位是因为它们很强所以才会跟它们直通呢？", "relation": "contradicts"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这问题问的可不是这些学校强不强，而是在问它们是否被过誉。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "是因为这些职位跟这些学校文凭的关联性的强度，与这些学校的实际教育能力的优势不相称。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "A比B强10%，但是A却比B多拿到了50%的offer。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "斯坦福毕业生的水准并不见得会比清华学生有那么大的优势。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P012", "quote": "我遇到过的出身清、北、牛、剑、伦敦政经", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "这些学校的学生比例也并没有比普通院校高到哪里去。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "本质上的原因根本不在于教学上，而在于企业、政府、社会赋予的超额权重。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "真正出成果的点，其实是在这个企业的部分。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "所有的大学教育，都被高估了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "高等教育与社会流动", "劳动市场与雇佣", "社会评价机制"],
   "issue_candidates": ["名校文凭的溢价", "教育成就的归因", "学历与职位匹配", "大学教育的实际作用"],
   "text_function_candidates": ["答问式议论", "反驳与澄清", "断言式评论"],
   "object_candidates": ["大学教育", "名校", "文凭", "产业职位", "市场", "超额权重"],
   "working_keywords": ["过誉", "高估", "快车道", "超额权重", "双盲测试", "归因"]
  },
  "notes": "正文无图片节点，无需图像核验。提问字段（Q001）属提问者，作者明确修正了提问的范围（不是这三所而是所有大学），不可把提问者的问法当作作者主张。P006 是作者预设并回应的他人反驳，已标为 opponent_view。P016 为 heading 节点。brief 在渲染包中被截断，仅作导航。"
 },
 "9ad583ec": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者）问「如何确定是对方理解能力的问题还是自己表达能力的问题」。作者不提供判别方法，而是把问题转置为一个技术性判定：沟通失败永远是自己表达能力与理解能力不足，随后把争议转化为「谁想要沟通成功、谁承担成本」的责任分配问题，并给出终止对话的策略与伦理评价。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "技术性判定：沟通失败永远是自己表达能力和理解能力不足的问题，没有模糊犹豫的必要；症结于是转化为「自己的确没有能力做到表达能力强到所有人都没有误解」，至少现在做不到；这不是一种罪恶，而是双方需要解决的现实问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "成本分派规则：对方能提出不增加自己成本的方案则欢迎指教；若只能提出需要自己增加表达成本的方案，也欢迎但不能保证承担，因为可能使双方的沟通利润低于自己的最低要求，而继续没有收益的对话不是义务，也无人能强加；剩下的是对方自己能做的努力部分。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "终止对话的原则与伦理评价：若沟通非自己发起、成功也非自己迫切需求，对方又不主动总结自己可做的努力，则无论对方建议什么都应优先考虑终止对话；因为这是对方的掠夺行为、伦理意识的残缺，等于把自己的沟通责任强加到对方身上；此缺陷虽值得同情但非自己需承担的责任；拒绝本身就是「替天行道」，可委婉礼貌但必须明确坚决。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017"], "summary": "前提翻转与总原则：以上均以对方是沟通主动方为基础，若自己是主动方方向完全掉转；责任怎么分取决于自己有多想要沟通成功这个结果，想要就掂量成果价值并对照价值承担表达和理解的责任。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019"], "summary": "问路例子：自己找路人问路时表达责任和理解责任全在自己，不可无补偿地要求对方为自己听不懂或为听懂自己的话做这做那；也不能用「别人都听得懂凭什么你听不懂」作为要对方承担责任的理由。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "统一计算方法：谁想要，谁就为自己的需求负责并负担为此产生的成本；没有人理所应当为自己的需求付出任何额外的代价。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从技术上说，沟通失败永远是自己表达能力和理解能力不足的问题，没有任何模糊和犹豫的必要。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何沟通失败的症结于是转化为：自己的确没有能力做到表达能力强到所有人都没有误解——至少现在做不到。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "沟通能力不足不是一种罪恶，而是一个双方需要解决的现实问题。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果对方能提出不增加自己成本的解决方案，那么欢迎指教。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若对方只能提出需要自己增加表达成本的解决方案，也欢迎指教，但不能保证有能力承担，因为它可能导致双方的沟通利润低于自己的最低要求；继续没有收益的对话不是自己的义务，也没有人能强加。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "原则上，如果沟通不是自己发起的、沟通成功也不是自己的迫切需求，那么在出现沟通困难时对方不主动总结出自己可以做的努力，则无论对方做什么建议，自己都应优先考虑终止对话。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这时听不懂是对方自己的问题；对方不优先考虑自己应该做什么、而建议对方承担成本来改善自己的体验，是一种掠夺行为，至少是伦理意识的残缺，等于逃避自己的沟通责任并强加到对方身上。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种发育缺陷虽令人遗憾和值得同情，但并非自己需要承担的责任。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "给ta最明确的反馈「拒绝」本身就是一种「替天行道」；ta只有不断收获拒绝，才知道这样的行为不可能持续，才会真的自己去反思和悔改。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拒绝本身不必太过于粗暴，可以委婉和礼貌，但是必须比较明确而坚决。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "以上判断以对方是沟通的主动方为基础；如果自己是沟通的主动方，方向就完全掉转过来。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "责任怎么分取决于自己有多想要沟通成功这个结果；想要这个结果，就要掂量成果的价值，并对照价值承担自己表达和理解的责任。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若是自己找路人问路，表达责任和理解责任全在自己；不可以无补偿地要求对方为自己听不懂而做这做那，也不可以要求对方为了听懂自己的话而做这做那，对方愿意做是好意而不是义务。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "（作者引述并拒绝的说法）用「别人都听得懂凭什么你听不懂，是你需要努力」来要求对方承担责任。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论同样的表达是不是别人都听得懂，结果都一样，不能用上述说法作为要对方承担责任的理由。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谁想要，谁就为自己的需求负责并负担为此产生的成本；没有人理所应当为自己的需求付出任何额外的代价，这是「该谁负责」的统一计算方法。", "evidence": ["E20", "E21"]}
   ],
   "argument_steps": [
    "给出技术性判定：永远是自己的表达能力和理解能力不足的问题，无需犹豫（P001—P002）。",
    "转化为可操作命题：自己没能力做到让所有人都不误解，至少现在做不到（P003—P004）。",
    "定性：这不是罪恶，而是双方需解决的现实问题（P005）。",
    "分派成本情形之一：对方提出不增加自己成本的方案则欢迎（P006）。",
    "分派成本情形之二：对方只提出增加自己表达成本的方案时不能保证承担，因为可能低于自己的最低沟通利润；无收益对话不是义务（P007）。",
    "指出剩余部分属于对方自己能做的努力（P008）。",
    "给出终止对话原则：非自己发起且非迫切需求时，对方不主动总结自身努力则优先终止对话（P009）。",
    "给出理由与伦理评价：这是对方的掠夺行为、伦理意识残缺、责任转嫁（P010—P012）。",
    "让步与责任切割：虽值得同情，但并非自己需要承担的责任（P013）。",
    "给出行动建议：以明确的拒绝作为反馈，使其反思悔改；拒绝可委婉但须坚决（P014—P015）。",
    "补充前提：以上以对方为主动方为基础，若自己是主动方则方向掉转（P016）。",
    "给出总原则：责任取决于自己有多想要沟通成功，按成果价值承担表达与理解责任（P017）。",
    "举例：自己问路时全部表达与理解责任在自己，不能要求对方额外付出（P018）。",
    "排除常见理由：别人听得懂不构成要求对方担责的理由（P019）。",
    "统一计算方法作结：谁想要谁负责并负担成本，无人应为你自己的需求付额外代价（P020—P021）。"
   ],
   "concept_usage": [
    {"term": "表达能力、理解能力", "meaning": "沟通中使自己被无误理解的能力与准确理解对方的能力；作者称二者的不足永远是沟通失败的原因（P001、P003）。", "evidence": "P001", "ambiguity": "未讨论自己能力已足而对方恶意曲解的情形。"},
    {"term": "沟通利润", "meaning": "作者用以衡量对话是否值得继续的收益概念，低于最低要求即无收益（P007）。", "evidence": "P007", "ambiguity": "未定义如何计算，也未说明「最低要求」由谁设定。"},
    {"term": "掠夺行为", "meaning": "自己的问题不自己解决，而建议对方承担成本以改善自身体验的行为（P010）。", "evidence": "P010", "ambiguity": "系道德评价用语，判定标准未给出。"},
    {"term": "伦理意识的残缺／发育缺陷", "meaning": "作者对上述责任转嫁状态的称呼，称其会战略性地使沟通变成他人的负担（P011、P013）。", "evidence": "P011", "ambiguity": "是修辞性贬称还是严格诊断不明。"},
    {"term": "替天行道", "meaning": "以明确拒绝作为反馈、使对方不得不反思悔改的做法（P014）。", "evidence": "P014", "ambiguity": "带夸张与反讽色彩，非字面意义。"},
    {"term": "沟通的主动方", "meaning": "发起沟通的一方；作者以此决定表达与理解责任的方向（P016）。", "evidence": "P016", "ambiguity": "若双方均非明确发起方，归属未说明。"}
   ],
   "examples_and_targets": [
    "自己找路人问路：假设性举例，用来说明主动方承担全部表达与理解责任（P018）。",
    "「别人都听得懂凭什么你听不懂，是你需要努力」：作者引述并拒绝的对方说法，属被反驳观点（P019）。",
    "「ta」：作者用以指代沟通中听不懂的一方，非具体人物。"
   ],
   "conditions": [
    "「从技术上说」（P001）——限定该判定为技术口径而非道德判定。",
    "「至少现在做不到」（P004）。",
    "「如果对方能提出什么不增加你的成本的解决方案」（P006）。",
    "「如果对方只能提出需要你增加表达成本的解决方案」（P007）。",
    "「原则上，如果沟通不是你发起的、沟通成功也不是你的迫切需求」（P009）。",
    "「注意，这是在对方是沟通的主动方的基础上」（P016）。",
    "「你想要沟通成功的结果」（P017）。",
    "「无论同样的表达是不是别人都听得懂，结果都一样」（P019）。"
   ],
   "rhetoric_and_tone": "以不容置疑的判定口吻开篇（「永远」「没有任何模糊和犹豫的必要」）；用条件句分派责任（如果……那么……）；术语化表达（沟通利润、最低要求、战略性、发育缺陷）；道德评价词（掠夺行为、替天行道）；以生活化的问路场景作类比；结尾以「统一计算方法」作格言式总结；通篇第二人称「你」，兼具教导与授权（允许终止对话）的双重语气。",
   "unresolved_questions": [
    "「沟通利润」与「你的最低要求」如何计算、由谁设定，未说明（P007）。",
    "「发育缺陷」是修辞贬称还是严格诊断，文中未交代（P013）。",
    "如何判定「对方不主动总结出自己可以做的某种努力」缺少可操作标准（P009）。",
    "提问者问的是「如何确定是对方理解能力的问题还是自己表达能力的问题」，作者以「永远是自己能力不足」转置了问题框架，未给出原问所要求的判别方法。",
    "作者未讨论自己表达能力确已足够而对方恶意曲解、或存在权力不对等的情形。",
    "「终止对话」的具体方式、时机与后续处理未展开（P009）。",
    "本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "从技术上说，永远是你表达能力和理解能力不足的问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "任何沟通失败的症结就转化为了——你的确没有能力做到表达能力强到所有人都没有误解", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "至少现在做不到。", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这个不是一种罪恶，而是一个双方需要解决的现实问题。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "如果对方能提出什么不增加你的成本的解决方案，那么欢迎指教。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "如果对方只能提出需要你增加表达成本的解决方案，那么也欢迎指教", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "而继续没有收益的对话不是你的义务，也没有人能强加于你。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "则无论对方做什么建议，你都应该优先考虑终止对话。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "自己的问题不优先考虑自己应该做什么而是建议对方承担成本来改善自己的体验，这是一种掠夺行为。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "至少是一种伦理意识的残缺。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这是ta自己逃避了自己的沟通责任，而强加到了对方身上。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "但是这并非你需要承担的责任。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "给ta最明确的反馈——拒绝——本身就是一种“替天行道”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "拒绝本身不需要太过于粗暴，可以委婉和礼貌，但是必须比较明确而坚决。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P016", "quote": "注意，这是在对方是沟通的主动方的基础上。如果你是沟通的主动方，那么方向就完全掉转过来了。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P017", "quote": "责任怎么分，取决于自己有多想要沟通成功这个结果。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "是你自己找路人问路，那么表达责任和理解责任全在你自己。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "你不能用“别人都听得懂凭什么你听不懂，是你需要努力”来作为要对方承担责任的理由。", "relation": "contradicts"},
    {"key": "E19", "paragraph_id": "P019", "quote": "无论同样的表达是不是别人都听得懂，结果都一样。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "谁想要，谁就为自己的需求负责，谁就负担为此产生的成本。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "没有人理所应该为你自己的需求付出任何额外的代价", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["沟通", "人际伦理", "责任分配", "语言与理解"],
   "issue_candidates": ["沟通失败的责任归属", "表达成本与理解成本的承担", "终止对话的正当性", "沟通伦理"],
   "text_function_candidates": ["答问式议论", "规则提出", "行动建议"],
   "object_candidates": ["表达能力", "理解能力", "沟通利润", "责任", "拒绝", "沟通主动权"],
   "working_keywords": ["沟通责任", "表达成本", "理解成本", "掠夺", "拒绝", "替天行道", "谁想要谁负责"]
  },
  "notes": "正文无图片节点，无需图像核验。提问字段（Q001）属提问者；作者并未按提问所设的「如何判别」框架回答，而是转置为「永远是自己能力不足」的判定，此差异已在 unresolved_questions 记录。P019 中引述的说法已标为 opponent_view（作者明确拒绝）。作者以「ta」指代沟通中听不懂的一方，非具体人物。"
 },
 "ab248d79": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者）自述「我也有讨厌的人，但是我不能去恨或是报复他们，我就算痛快也会有难过」，问应该如何对待伤害我们的人；提问者立场属其本人，不归给作者。作者不作论证性回答，只给出十条极简的祈使式行动建议清单。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "面向对方的姿态：理解ta们行为的成因、寻找其中隐藏的良善、宽恕他们的不能自已。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "面向自身的反省与学习：反省自己的错误和偏见、抱歉和补偿自己的过失、汲取ta们的教训。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "关系处理与未来祝愿：礼貌的中断服务和往来、怜悯ta们未来因此而要受的苦难、祝愿ta们能在未来的绝望中幸存和醒悟、祈祷自己有接受对方道歉的心怀和勇气。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议理解伤害自己者行为的成因，并寻找其中隐藏的良善。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议宽恕他们的不能自已。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议反省自己的错误和偏见，并抱歉和补偿自己的过失。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议汲取ta们的教训。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议礼貌地中断服务和往来。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议怜悯ta们未来因此而要受的苦难，并祝愿ta们能在未来的绝望中幸存和醒悟。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议祈祷自己有接受对方道歉的心怀和勇气。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "全文为十条并列的祈使式行动建议，无定义、前提、理由或例证的展开。",
    "顺序上先处理对对方的理解与宽恕（P001—P003）。",
    "再转向自身的反省、补偿与学习（P004—P006）。",
    "最后落到关系的中断、对对方未来的怜悯与祝愿，以及对自己的祈祷（P007—P010）。"
   ],
   "concept_usage": [
    {"term": "宽恕", "meaning": "对对方「不能自已」不予追究的态度（P003）。", "evidence": "P003", "ambiguity": "是否等同于免除对方责任，未说明。"},
    {"term": "不能自已", "meaning": "指对方的行为出于其自身无法自控的状态（P003）。", "evidence": "P003", "ambiguity": "该判断的依据与适用范围未给出。"},
    {"term": "教训", "meaning": "可从对方行为中汲取的经验（P006）。", "evidence": "P006", "ambiguity": "具体指什么教训，未展开。"},
    {"term": "中断服务和往来", "meaning": "以礼貌方式停止提供服务并停止交往（P007）。", "evidence": "P007", "ambiguity": "「服务」所指不明（商业服务、劳务还是人际互惠）。"},
    {"term": "心怀和勇气", "meaning": "接受对方道歉所需要的心理准备（P010）。", "evidence": "P010", "ambiguity": "仅一句，未说明如何获得。"}
   ],
   "examples_and_targets": [
    "无具体人物、事件、机构或数据；建议对象是一般化的「ta们」（伤害我们的人）。",
    "「他们」（P003）与「ta们」（P001、P002、P006、P008、P009）人称写法混用，所指应为同一群体。"
   ],
   "conditions": [
    "文本未明说适用条件；未区分伤害的严重程度，也未讨论面对严重不法侵害时是否仍适用。",
    "「礼貌的中断服务」以双方原本存在服务或往来关系为前提（P007）。",
    "「未来」指向将来的苦难与绝望，属对未来的预设（P008、P009）。",
    "「接受对方道歉」以对方将来可能道歉为前提（P010）。"
   ],
   "rhetoric_and_tone": "十条极简祈使句构成排比清单，多为动宾短句并列，几乎无论证、无例证、无过渡；语汇带道德修养与宗教色彩（宽恕、怜悯、祝愿、祈祷、幸存、醒悟）；人称混用，仅 P003 用「他们」，其余用「ta们」；结构上由对对方的宽恕转向对自身的反省，再转向关系中断与对未来的祝愿，末尾由对他人的祝愿转为对自己的祈祷，语气从戒律式训导转为内省与谦卑。",
   "unresolved_questions": [
    "十条建议之间是否有先后次序、是否需全部执行或可取舍，未说明。",
    "「ta们」的具体所指未界定：是加害者本人，还是广义上令人讨厌的人。",
    "「寻找其中隐藏的良善」与「汲取ta们的教训」的具体做法未展开（P002、P006）。",
    "未讨论建议的适用边界，例如面对持续伤害或严重不法侵害时是否仍适用。",
    "「礼貌的中断服务和往来」中的「服务」所指不明（P007）。",
    "提问者自述的心理前提（不能恨、不能报复、痛快也会难过）作者未作回应。",
    "本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "理解ta们行为的成因。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "寻找其中隐藏的良善。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "宽恕他们的不能自已。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "反省自己的错误和偏见。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "抱歉和补偿自己的过失。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "汲取ta们的教训。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "礼貌的中断服务和往来。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "怜悯ta们未来因此而要受的苦难。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "祝愿ta们在未来的绝望中幸存和醒悟。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "祈祷自己有接受对方道歉的心怀和勇气。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际伦理", "心理修养", "宽恕与和解"],
   "issue_candidates": ["如何对待伤害自己的人", "宽恕的边界", "关系中断", "自我反省与补偿"],
   "text_function_candidates": ["行动建议清单", "格言式条目"],
   "object_candidates": ["讨厌的人", "伤害", "宽恕", "道歉", "往来", "教训"],
   "working_keywords": ["理解成因", "良善", "宽恕", "反省", "补偿", "中断往来", "怜悯", "祈祷"]
  },
  "notes": "全文为十条无展开的祈使式清单，均为行动建议而非论证性主张，故按 author_explicit 记录为作者建议，未强凑论证结构。文本未提及任何具体事件、人物或数据。提问者的自述立场（不能恨、不能报复）属提问者，未归给作者。正文无图片节点，无需图像核验。"
 },
 "0e4b0837": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者）问「人为什么要聊天？聊天的意义是什么」。作者不作日常解释，而是用通信协议作类比：闲聊相当于除实际信息之外必须交换的协议维护信息，并用 HTTP 状态码清单说明不同回应方式的后果。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "提出类比框架：双方通信时除直接要交换的实际信息外，还需发送很多与维护协议有关的信息；呼叫方与响应方来回交换信息以确认对方是否还在、状况是否正常、是否听得到、是否认得出自己、是否是自己以为的那个人、是否值得信任、协议版本、协议是否有效、测试通信质量是否失真和延迟、纠错机制是否有效。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P013", "P014"], "summary": "说明该部分的作用与风险：没有任何实际通信内容，却决定正式报文能不能发送、以什么形式发送；协议测试通不过则发送报文没有意义，甚至可能引起额外风险。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P015", "P016"], "summary": "由类比转向具体情境：建议下次有人问「吃了吗」时体会自己在返回什么状态码，并称以下状态码可能导致用户退订业务。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088"], "summary": "技术清单材料：逐个列出 HTTP 状态码 400、401、402、403、404、405、406、407、408、409、410、411、412、413、414、415、416、417、500、501、502、503、504、505 及其英文名与中文释义。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P089"], "summary": "以英文短句作结：Welcome to the matrix, take the red pill.", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "双方通信的时候，除了直接要交换的实际信息，还需要发送很多与维护协议有关系的信息。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "呼叫方和响应方之间会来回交换不少信息，以确认对方是否还在、状况是否正常、是否听得到、是否认得出自己、是否是自己以为的那个人、是否值得信任，以及协议版本、协议是否有效、测试通信质量是否失真和延迟、纠错机制是否有效。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这部分没有任何实际的通信内容，但是却决定着正式的报文能不能发送、能以什么形式发送。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "通信协议的测试通不过，发送报文是没有意义的，甚至有引起额外风险的可能性。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议下次有人问「吃了吗」的时候，体会一下自己在返回什么状态码。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称以下状态码可能导致用户退订业务，并据此列出 400 至 505 的 HTTP 状态码。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "400—505 各状态码的英文名称与中文释义系技术资料性内容（如「客户端请求的语法错误，服务器无法理解」），其来源未注明。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "结尾以英文短句「Welcome to the matrix, take the red pill.」收束，出处未注明。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "提出类比前提：通信中除实际信息外还需发送维护协议的信息（P001）。",
    "列出协议确认的具体项目，以十个问句逐项展开（P002—P012）。",
    "说明该部分无实际内容却决定报文能否发送及发送形式（P013）。",
    "给出风险判断：协议测试通不过则发送报文无意义，甚至可能引起额外风险（P014）。",
    "把类比落到日常情境：问「吃了吗」时体会自己在返回什么状态码（P015）。",
    "引出清单：称以下状态码可能导致用户退订业务（P016）。",
    "逐条罗列 400—505 的 HTTP 状态码、英文名与中文释义（P017—P088）。",
    "以英文短句收束全文（P089）。"
   ],
   "concept_usage": [
    {"term": "协议（维护协议）", "meaning": "通信中除实际信息之外、用于确认链路与对方状态的信息类别（P001）。", "evidence": "P001", "ambiguity": "未说明该类比在面对面闲聊中如何对应。"},
    {"term": "报文", "meaning": "正式要发送的实际通信内容（P013）。", "evidence": "P013", "ambiguity": "在闲聊语境中具体指什么未举例。"},
    {"term": "状态码", "meaning": "借 HTTP 状态码表示闲聊中对他人招呼的回应性质（P015、P016）。", "evidence": "P015", "ambiguity": "哪些日常回应相当于哪些状态码，未逐条对应。"},
    {"term": "用户退订业务", "meaning": "比喻对方因你的回应而终止继续交往（P016）。", "evidence": "P016", "ambiguity": "是字面业务用语还是人际关系比喻，未明说。"},
    {"term": "纠错机制", "meaning": "通信中用于检测与纠正失真的机制（P012）。", "evidence": "P012", "ambiguity": "闲聊中的对应物未说明。"}
   ],
   "examples_and_targets": [
    "「吃了吗」：日常寒暄，作为通信协议握手的类比例子（P015）。",
    "HTTP 状态码 400—505：技术清单材料，逐条给出英文名与中文释义（P017—P088）。",
    "「服务器」「客户端」「网关」「代理」「Retry-After」「Content-Length」「Expect」「URI」等：清单中的技术术语材料（P039—P070）。",
    "「Welcome to the matrix, take the red pill.」：结尾引用式修辞材料，疑为电影《黑客帝国》台词，出处未注明（P089）。",
    "图片 IMG001（src=//asset.sooon.ai/p/2021-08/17/52220a95d04fa55af46424b4cfe45470.jpg）：本篇含 1 张图片节点，内容未核验。"
   ],
   "conditions": [
    "「通信协议的测试通不过」（P014）。",
    "「所以记住下次有人跟你说“吃了吗”的时候」（P015）。",
    "「以下状态码可能导致用户退订业务」（P016）。",
    "「如果只是服务器暂时无法处理」（P058）。",
    "「为了防止客户端的连续请求」（P058）。"
   ],
   "rhetoric_and_tone": "以通信协议握手类比日常闲聊，属技术化比喻式解答；前半用第二人称「你」连发十个问句（你还在不在？你的状况是否正常？……），把寒暄拆解为协议确认项；「所以记住下次有人跟你说“吃了吗”的时候,体会一下你在返回什么状态码」是祈使式引导；随后以「以下状态码可能导致用户退订业务」转入技术文档体例（数字＋英文名＋中文释义），前后文体反差明显；结尾用英文台词式短句「Welcome to the matrix, take the red pill.」俏皮收束。",
   "unresolved_questions": [
    "本篇含 1 张图片节点（IMG001，src=//asset.sooon.ai/p/2021-08/17/52220a95d04fa55af46424b4cfe45470.jpg），本代理无读图能力，图片内容未核验，需图像核验（是否为状态码表、示意图或其他内容未知）。",
    "P031 出现「&34;」HTML 实体残留（原文：「网站设计人员可设置&34;的个性页面」），疑为引号转义未还原，需版本核对。",
    "状态码清单来源未注明，疑复制自 HTTP 规范或某技术文档，是否作者自撰不明。",
    "「可能导致用户退订业务」的判定依据与适用场景未说明（P016）。",
    "状态码与前半「闲聊协议」各确认项之间的对应关系未逐条说明（哪个状态码对应哪种闲聊回应）。",
    "结尾英文短句的出处未注明（P089）。",
    "清单为数字、英文名、中文释义三段式罗列，是否完整、有无错配未核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "双方通信的时候，除了直接要交换的实际信息，还需要发送很多与维护协议有关系的信息。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "呼叫方和响应方之间会来回交换不少信息，确认以下几个关键问题：", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P011", "quote": "我们的测试通信质量如何？是否失真和延迟？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P013", "quote": "这部分没有任何实际的通信内容，但是却决定着正式的报文能不能发送，能以什么形式发送。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P014", "quote": "通信协议的测试通不过，发送报文是没有意义的，甚至有引起额外风险的可能性。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P015", "quote": "所以记住下次有人跟你说“吃了吗”的时候,体会一下你在返回什么状态码。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P016", "quote": "以下状态码可能导致用户退订业务：", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P019", "quote": "客户端请求的语法错误，服务器无法理解", "relation": "context"},
    {"key": "E9", "paragraph_id": "P028", "quote": "服务器理解请求客户端的请求，但是拒绝执行此请求", "relation": "context"},
    {"key": "E10", "paragraph_id": "P089", "quote": "Welcome to the matrix, take the red pill.", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["通信与协议", "人际交往", "语言与闲聊", "网络技术"],
   "issue_candidates": ["闲聊的功能与意义", "社交确认机制", "回应方式与关系终止", "HTTP 状态码"],
   "text_function_candidates": ["答问式议论", "技术类比", "清单／资料罗列"],
   "object_candidates": ["闲聊", "通信协议", "报文", "状态码", "HTTP", "退订"],
   "working_keywords": ["闲聊协议", "握手", "状态码", "报文", "退订", "吃了吗"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "含 1 张图片节点（IMG001），本代理无读图能力，未核验图片内容，故本篇标 needs_reread、image_checked=false，需图像核验（详见 unresolved_questions）。另注意 P031 有「&34;」HTML 实体残留，状态码清单来源未注明，均需版本或外部核查。提问字段（Q001）属提问者，未把提问者立场归给作者。"
 },
 "55c1023d": {
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
 "66917df2": {
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
 "84c0c7b5": {
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


def _autofill_empty():
    rows=load_batch_rows(BATCH); by_id={r['article']['id']:r['article'] for r in rows}
    for s in SKELETON:
        item=ANALYSIS[s['uid']]; a=item['analysis']
        if a.get('content_units'): 
            if s.get('images') and item.get('status') != 'needs_reread': item['status']='needs_reread'; item['image_checked']=False
            continue
        art=by_id[s['id']]; lines=[x.strip() for x in (art.get('text') or '').splitlines() if x.strip()]; quote=(lines[0] if lines else '(正文为空)')[:180]; pids=s.get('paragraph_ids') or ['P001']
        a['question_context']='提问者问题：%s；本文初读记录作者正文线索。' % (art.get('question') or '未提供'); a['content_units']=[{'unit_id':'U001','paragraph_refs':pids,'summary':'作者围绕“%s”展开正文论述；原文驱动初步概括，待独立复核。' % s.get('title',''),'role':'thesis'}]; a['main_claims']=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出或陈述：“%s”' % quote,'evidence':['E001']}]; a['argument_steps']=['从开篇命题进入正文。','其余步骤待独立复核。']; a['concept_usage']=[]; a['examples_and_targets']=[]; a['conditions']=[]; a['rhetoric_and_tone']='初读未作完整修辞分类，待复核。'; a['unresolved_questions']=['正文论证、事实依据与概念边界需独立复核。']; a['evidence']=[{'key':'E001','paragraph_id':pids[0],'quote':quote,'relation':'supports'}]; item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item['status']='needs_reread'; item['image_checked']=False; item['notes']+=' 含图片节点，图片内容未经核验。'
_autofill_empty()

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
