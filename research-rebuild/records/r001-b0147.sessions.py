# -*- coding: utf-8 -*-
"""批次 r001-b0147 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0147.sessions.py            # 写 out/r001-b0147.out.jsonl
  python3 records/r001-b0147.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0147"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0147.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "01008cb7": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么性教育在中国的普及如此困难？”。作者没有按提问者的前提罗列困难成因，而是质疑“普及”是否真是教育应追求的目标，并反驳把“性教育遇阻”等同于教育失败的流行说法。提问者只提出问题、未表明立场，不得归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "中国大众的教育观受公立学校体制塑造：教育须与权威、普及挂钩，须产出可评职称、可换社会高看的“结果”，否则不算教育。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "“教育没落/教育艰难”“性教育遇阻”“白学了”等结论正是在这种语境下形成；作者判定其基于扭曲观念，属误判。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "教育的根本是改变人的行为而非改变其在体制中的评分；只要行为改变，无论有无文凭都算教育发生了影响。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "教育成功所需的影响人数不是百万、上亿，只要有一个受教者形成应用习惯并再教他人即算及格。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "教育成功以传承持续的长度而非认同者人数的宽度衡量；只要传承不断，消散的局面迟早再迎春天。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021"], "summary": "教育者应关心所教内容能否扩大学习者的生存优势与自由、是否有便于他人转授的总结资料；做到即使只教一人也算成功。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "人类教育本身没有“普及性”诉求，那是统治的诉求；教育一向走因材施教、树立典型、榜样扩散的路线，争取传递系数不低于1。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P026"], "summary": "按上述标准，性教育谈不上“受阻”，除性教育家自身出于傲慢的绝望外，并无东西阻止其追求目标。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国大众语境中的“教育”必须与权威、普及挂钩，并产出能评职称、换得社会高看的“结果”，否则不能算数。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“教育没落”“教育艰难”以及“性教育遇阻”“白学了”等说法都是在这种扭曲观念下形成的结论，实为误判。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育的根本是改变人的行为，而不是改变人在体制中的评分；行为改变本身即教育发生了影响。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育成功不靠人数多寡：只要有一个受教者形成应用习惯、会再去教别人，就已经及格。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育成功用传承的长度而非认同者的宽度来衡量。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类的教育本身没有“普及性”诉求，有普及性诉求的是统治。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类教育几百万年来奉行的是因材施教、树立典型、再借榜样力量自然扩散引发效仿的路线。", "evidence": ["E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育者真正要关心的是所教之物能否扩大学习者的生存优势与自由，以及是否有足够好的总结和资料方便他人转授。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按传承标准看，性教育根本谈不上“受阻”；除性教育家自身出于傲慢的绝望外，没有东西阻止其追求该目标。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "事实性前提：中国人的教育观念受公立学校教育影响，教育须进学校设课程、有学位才算（P001—P002）。",
    "举例佐证：社会培训班不被当作教育；跟父辈做木匠、学琴、学相声、自学绘画编程，被心里认为“没有受过教育”（P003—P004）。",
    "提炼大众语境的判据：教育与权威、普及挂钩，并须形成可评职称、可获额外高看的结果（P005）。",
    "列出由该判据推出的结论：教育没落、教育艰难、性教育遇阻、白学了（P006—P007）。",
    "反驳：这些结论是基于扭曲观念的误判（P008）。",
    "给出替代定义：教育的根本是改变行为而非改变体制中的评分，行为改变即影响发生（P009—P010）。",
    "以反问设问成功所需的规模，自答：一人肯薪火相传即及格（P011—P014）。",
    "提出衡量尺度：用长度而不是宽度衡量（P015—P016）。",
    "远景推论：传承不断，则局面消散后迟早再迎春天（P017—P018）。",
    "行动建议：教育者应关心生存优势与自由、以及便于转授的资料；做到即成功，不止一人则极其成功（P019—P021）。",
    "一般化前提：人类教育本无普及性诉求，普及性诉求属于统治（P022—P023）。",
    "历史路线与成就标准：因材施教、树立典型、自然扩散，争取传递系数不低于1（P024—P025）。",
    "结论：按该标准，性教育谈不上“受阻”，阻碍只来自性教育家自身的傲慢与绝望（P026）。"
   ],
   "concept_usage": [
    {"term": "教育", "meaning": "大众语境中指与权威、普及挂钩并能产出可评职称结果的体制化过程；作者随后将其重定义为“改变人的行为”。", "evidence": "P005", "ambiguity": "同一词在大众用法与作者定义之间含义冲突，作者未逐一说明两者关系。"},
    {"term": "及格", "meaning": "教育成功的最低门槛——有一个受教者肯薪火相传。", "evidence": "P013", "ambiguity": "“及格”只在作者自设标准下成立，未给出可操作的判定方式。"},
    {"term": "长度/宽度", "meaning": "长度指愿意代代相传者传承的久暂，宽度指认同者的人数。", "evidence": "P016", "ambiguity": "未说明长度如何计量、是否与影响质量有关。"},
    {"term": "普及性", "meaning": "覆盖面意义上的推广诉求；作者认为这属于统治而非教育。", "evidence": "P022", "ambiguity": "“统治（无贬义）”的界定及其与教育的关系未展开。"},
    {"term": "评职称", "meaning": "不只指体制内升迁，也指在社会交往中获得额外高看。", "evidence": "P005", "ambiguity": "作者以引号标示其为大众语汇，未给出精确所指范围。"},
    {"term": "薪火相传", "meaning": "受教者形成应用习惯并再去教别人（子女、朋友也算）。", "evidence": "P014", "ambiguity": "与 P025“传递系数不低于1”的关系未说明。"}
   ],
   "examples_and_targets": [
    "社会上办的种种培训班、认证培训——例证，用来说明它们在大众观念里不算教育（P003）。",
    "跟着老爹做木匠活、跟老师学小提琴或相声、自学绘画与编程——例证，说明非学校路径会被默认为“没有受过教育”（P004）。",
    "“性教育老师找不到体制内工作”“接受性教育不能获得更高的社会评价”——被作者反驳的流行说法（反驳对象，P007）。",
    "“教育没落”“教育艰难”——被作者判定为特定语境下结论的说法（反驳对象，P006）。",
    "性教育家——被批评对象：作者称其绝望出于自身傲慢（P026）。"
   ],
   "conditions": [
    "论述范围限定在“中国的大众语境里”（P005）。",
    "若影响“还是顺应你的目的的”，才谈得上成功（P010）。",
    "成功的最低条件：有一个人会形成应用的习惯、会再去教别人（P014）。",
    "只要传承没有断，局面消散后迟早又会迎来下一个春天（P018）。",
    "视角限定为“作为一个教育者”应关心什么（P019）。",
    "“哪怕你只教了一个人”“如果这样的人不止一个”分别对应成功与极其成功的程度（P020—P021）。"
   ],
   "rhetoric_and_tone": "论辩与定义重构为主：先描述大众观念，再判定其为“扭曲观念”，随后用“改变行为”“及格”“长度而非宽度”重设判据。多用反问（“并且这一成功需要的影响人数是多少呢？”）与自问自答（P011—P013）推进；以“薪火相传”“春天”“评职称”作比喻；第二人称“你”拉近距离并带训诫口吻，结尾以“傲慢而生出的绝望”对性教育家作尖锐批评。",
   "unresolved_questions": [
    "提问者问性教育在中国普及困难的原因，作者实际质疑了“普及”是否为教育应追求的目标，未逐条回应困难成因。",
    "“统治（无贬义）”的普及性诉求与教育的关系未展开论证。",
    "“传递系数不低于1”未给出定义、测量方式或反例条件。",
    "在作者标准下性教育者具体应如何做（教什么、如何组织转授资料），正文未给出可操作步骤。",
    "“教育没落”“教育艰难”被指为误判，但未区分其中可能存在的非观念性原因。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P005", "quote": "必须要与权威、普及挂上钩", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "中国人对教育的观念极大地受到了公立学校教育的影响", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "很多所谓“教育没落”，“教育艰难”都是在这个语境下形成的结论。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "实际上这不过是一种基于扭曲观念的误判。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "教育的根本是改变人的行为，而不是改变人在“体制”中的评分。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "改变了人的行为，无论形不形成任何文凭，都叫做教育发生了影响。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "而是只要有一个人肯薪火相传就及格了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "有一个人会形成应用的习惯，会再去教别人", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "它是用长度，而不是宽度来衡量的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "不是靠认同它的人的人数的多寡来衡量的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "人类的教育根本就没有“普及性”这个诉求。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "有普及性诉求的是统治（无贬义）。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "一向奉行的是因材施教，树立典型", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "真正要关心的是你所教的东西能不能扩大所学的人的生存优势和自由", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "它根本就谈不上“受阻”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "性教育", "社会评价"],
   "issue_candidates": ["教育成功的标准", "普及性是否属于教育诉求", "性教育遇阻的归因"],
   "text_function_candidates": ["论辩", "概念重构", "劝诫"],
   "object_candidates": ["教育", "性教育", "公立学校体制", "社会评价"],
   "working_keywords": ["教育的及格线", "改变行为", "薪火相传", "长度而非宽度", "普及性", "评职称", "性教育遇阻"]
  },
  "notes": "正文无图片，全文已读（26 段）。提问字段 Q001 属提问者，仅作语境；正文未直接回答“普及为何困难”，而是质疑“普及”这一前提。published_at 2021-07-31、updated_at 2025-01-22，语料对应更新后版本，未见版本对照材料。"
 },
 "4cd7ff75": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何才能坦然地面对自己因为抑郁症而荒废的五六年时间？”。提问者自述那五六年是“荒废”，这一前提被作者明确否定；作者以“抑郁症犹如精神性自体免疫病”的类比与对“赢了”的界定，主张那几年是提前面对拆弹工作。提问者的自述框架不得归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "抑郁症犹如精神性自体免疫病：平时驱动人“奋斗”“努力”的因素（心理优越感、权力感、控制感、感官享乐、意识形态快感等）一旦遇上过敏原便反噬自身。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "内在问题已成定局者只有两条路：运气好到不遇上过敏原，或遇上后挺住并在反复发作中形成适应、达成脱敏。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "按中国乃至世界现状，多数人有来自物质主义的内在极大脆弱性，这是普遍焦虑的根源；未发作只因未遇足够大的打击，而寿命延长与节奏加快使不受重击的概率越来越小，属大概率事件。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "毕业、失恋/离婚、落选、意外疾病、失业等关口几乎无人全躲过，衰老、失亲也是必修课。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "若三十岁前得抑郁症、挺住、五六年稳定住并最后赢了，则完成了重大人生功课，并未落后反而领先；“赢了”指引擎换掉、获得逻辑性免疫与强化的抗打击结构。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "没经过这一关的人的成就建立在炸弹上；所以不是耽误五六年，而是提前十几年面对拆弹工作，真正的问题是有没有做好拆弹，并须区分拆弹与救灾。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "很多人的“治疗”只是打扫现场、救治伤员、修复建筑而没有排雷，寄托于“下次不会这么倒霉”的幻想；作者断言这次只是点额头，下一次才是耳光，排雷最重要。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "若做好排雷工作，不但没落后反而跑在别人前面十几年；现在就得了抑郁症是幸运而不是不幸。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抑郁症本质上犹如一种精神性的自体免疫病：平时驱动人奋斗努力的因素在遇上过敏原后会转而攻击自己。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对内在问题已成定局的人只有两条路：运气好不遇上过敏原，或遇上后挺住并在反复发作中形成适应、达成脱敏。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按中国乃至世界的现状，大部分人都存在来自物质主义的内在极大脆弱性，这是普遍焦虑的根源；一般人没有发作只是因为还没遇上足够大的打击。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "由于寿命大幅延长和社会运转节奏提升，几十年里数以千计关键事件中一次都不受沉重打击的概率越来越小，已属大概率事件。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人生几大关口几乎无人能全部躲过，衰老、失亲也是必修课。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若三十岁之前得抑郁症、挺住了、经过五六年稳定住并且最后赢了，那就是完成了一项重大人生功课，不但没有落后反而领先。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“赢了”指不但坚持过去而且引擎换掉了：能提供动力，并能逻辑性地免疫于这些打击，具备大大强化的抗打击结构。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有经过这一关的人，其成就严格说不算建立在沙滩上，而是建立在一颗炸弹上。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问主的经历并不是“耽误五六年时间”，而是提前了十几年面对拆弹工作。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人所谓的“治疗”只是在打扫现场、救治伤员、修复建筑而没有排雷；必须把拆弹和救灾区分清楚。", "evidence": ["E14", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把希望寄托于“下次不会这么倒霉”的人错了：和下次相比，这次只是轻轻点一下额头，下一次才是耳光。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "排雷才是最重要的工作；若做好了排雷工作，不但没有落后五六年，反而跑在别人前面十几年。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在就得了抑郁症是一种幸运，而不是不幸。", "evidence": ["E18"]}
   ],
   "argument_steps": [
    "定义/类比：把抑郁症比作精神性自体免疫病，驱动机制在遇过敏原时反噬自身（P001）。",
    "举例说明反噬：心理优越感在大赛场遇天才或利维坦即转为自卑；以金钱享乐为依靠者见赚钱前景悲观即受打击（P002—P003）。",
    "前提：内在问题已成定局者只有“不遇过敏原”或“遇上后脱敏”两条路（P004）。",
    "现实判断：物质主义造成的内在脆弱性普遍存在，是普遍焦虑的根源；未发作只因打击不够大（P005）。",
    "概率推论：寿命延长与节奏提升使不受重击的概率越来越小，属大概率事件（P006—P007）。",
    "例证列举：毕业、失恋/离婚、落选、意外疾病、失业，以及衰老、失亲（P008—P009）。",
    "条件性结论：三十岁前得病且挺住、稳定、赢了，则完成重大功课、反而领先（P010—P011）。",
    "界定“赢了”：引擎换掉，逻辑性免疫于打击，抗打击结构强化，并以三个“不但…而且…”说明态度转变（P012—P013）。",
    "对比：未过关者的成就是建立在炸弹上（P014）。",
    "重新定性：不是耽误五六年，而是提前十几年面对拆弹；真问题是拆弹做得好不好，且要区分拆弹与救灾（P015—P016）。",
    "反驳流行的“治疗”：只救灾不排雷，寄托于“下次不会这么倒霉”的幻想（P017）。",
    "断言后果：这次只是点额头，下一次才是耳光；排雷才是最重要的工作（P018—P020）。",
    "结论：做好排雷则领先十几年，现在就患病是幸运而非不幸（P021—P022）。"
   ],
   "concept_usage": [
    {"term": "精神性的自体免疫病", "meaning": "对抑郁症的类比：本该驱动自己的内在机制反过来攻击自己。", "evidence": "P001", "ambiguity": "作者写明“犹如”，是类比而非医学诊断，正文未提供医学依据。"},
    {"term": "过敏原", "meaning": "触发反噬的外部打击，如很大的赛场、比自己强的天才或利维坦、赚钱前景悲观。", "evidence": "P002", "ambiguity": "未给出完整清单或判定标准。"},
    {"term": "脱敏", "meaning": "在反复发作中渐渐形成适应。", "evidence": "P004", "ambiguity": "与“排雷”“换引擎”的关系未说明。"},
    {"term": "赢了", "meaning": "不但坚持过去，而且引擎换掉，能逻辑性免疫于打击并具备强化的抗打击结构。", "evidence": "P012", "ambiguity": "判定标准由作者自设，无外部可核指标。"},
    {"term": "拆弹/排雷", "meaning": "处理内在致病结构本身，而非只处理其造成的后果。", "evidence": "P016", "ambiguity": "与“救灾”的具体界线由作者一句划定，未给操作定义。"},
    {"term": "救灾", "meaning": "打扫现场、救治伤员、修复建筑等只处理后果的治疗方式。", "evidence": "P017", "ambiguity": "未说明现实中如何区分二者。"},
    {"term": "引擎换掉", "meaning": "动力来源被替换，从而不再依赖原先脆弱的内在驱动。", "evidence": "P012", "ambiguity": "隐喻，未说明换成何种动力。"}
   ],
   "examples_and_targets": [
    "心理优越感在很大的赛场、见识让自己腿软的天才或利维坦时转化为自卑感——例证（P002）。",
    "以钱带来的享乐为最大依靠者，看到赚钱前景悲观即受负面打击——例证（P002）。",
    "毕业、失恋/离婚、落选、意外疾病、失业——列举式例证（P008）。",
    "衰老、失亲——列举式例证，称其为必修课（P009）。",
    "把“治疗”当作打扫现场、救治伤员、修复建筑的人——被反驳对象（P017）。",
    "“下次不会这么倒霉”的幻想——被反驳对象（P017）。",
    "提问者自述“因为抑郁症而荒废的五六年时间”——提问者说法，被作者否定（Q001/P015）。"
   ],
   "conditions": [
    "讨论对象限定为“这些内在问题已成定局的人”（P004）。",
    "现实前提：来自物质主义的、内在的极大脆弱性普遍存在（P005）。",
    "概率条件：人类寿命大幅延长与社会运转节奏大幅提升（P006）。",
    "若三十岁之前得病、挺住、经五六年稳定住并最后赢了，才谈得上领先（P010—P011）。",
    "若做好了排雷工作，才会跑在别人前面十几年（P021）。",
    "须区分拆弹与救灾，否则“治疗”可能只停留在救灾（P016—P017）。"
   ],
   "rhetoric_and_tone": "第二人称直接对话与断言式劝慰（“我实实在在的告诉你”），全篇以医学与拆弹隐喻贯穿：自体免疫病、过敏原、反噬、脱敏、炸弹、拆弹、排雷、救灾、换引擎。P013 用三个“不但…而且…”排比铺陈转变后的态度；以短句断喝制造节奏（“等等。”“排雷才是最重要的工作。”“下一次才是耳光。”）；末句以“幸运，而不是不幸”正面翻转提问者的“荒废”前提，带强烈训诫与打气色彩。",
   "unresolved_questions": [
    "“精神性的自体免疫病”是类比而非医学论断，需外部核查（脑科学/精神病学）后才能作为事实使用。",
    "“五六年稳定住”与“赢了”的具体判定标准、时间界线，正文未说明。",
    "“拆弹/排雷”与“救灾”的操作性区别、如何判断自己是否已完成排雷，正文未给出。",
    "提问者的具体处境与治疗史未交代，正文只作一般化回应。",
    "“最好”的路径若两条都没走通（既没躲过也未能脱敏）会怎样，正文未讨论。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "抑郁症本质上犹如一种精神性的自体免疫病", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它会立刻转化为自卑感，对你自己发起反噬", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "要么遇上了、挺住了，并在反复发作中渐渐形成适应、达成脱敏。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "大部分人都存在着来自物质主义的、内在的极大脆弱性", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "概率越来越小了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "换句话来说，这是一个大概率事件。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "几乎无人能全部躲过。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "更不必提还有衰老、失亲这几节必修课。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "如果你是三十岁之前就得了抑郁症，而且挺住了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "事实上反而是领先了", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "就是不但坚持过去了，而且你的引擎换掉了", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "事实上是建立在一颗炸弹上。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "你是提前了十几年面对拆弹工作。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "仅仅不过是在打扫现场、救治伤员、修复建筑，没有排雷", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "你要把拆弹和救灾区分清楚", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "和下次相比，这次只是轻轻点点你的额头而已。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "排雷才是最重要的工作。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "你是跑在了别人前面十几年。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "你现在就得了抑郁症是一种幸运，而不是不幸。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理健康", "抑郁症", "人生阶段"],
   "issue_candidates": ["患病经历是否等于荒废时间", "治疗的层次（排雷与救灾）", "抗打击结构的形成"],
   "text_function_candidates": ["劝慰", "论辩", "概念重构"],
   "object_candidates": ["抑郁症", "治疗", "人生关口", "物质主义"],
   "working_keywords": ["自体免疫病", "过敏原", "脱敏", "拆弹", "排雷", "救灾", "换引擎", "耽误五六年"]
  },
  "notes": "正文无图片，全文已读（22 段）。提问字段 Q001 属提问者，“荒废五六年”是提问者自述而非作者判断，作者明确否定该表述。文中医学类比为作者自创，未经外部核查。published_at 2021-08-01、updated_at 2025-10-12，语料对应更新后版本。"
 },
 "525ef1d9": {
  "analysis": {
   "question_context": "提问者（Q001）问“民族主义和种族主义的区别在哪里？”。作者以三组对照口号回答二者的区别，全篇为作者判断，未引用任何来源；提问者只提问、未表立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以口号对照二者的自我定位：民族主义说“我们不比任何人差”，种族主义说“我们比任何人都强”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "以“独立/孤立”对照二者的对外姿态：民族主义说“我们可以独立”，种族主义说“我们可以孤立”。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "以对他人的关系对照：民族主义说“我们不依赖其他人”，种族主义说“我们不需要其他人”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "以“自己体会一下”收束，把从三组对照中得出结论的工作交给读者。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民族主义的口号是“我们不比任何人差”，种族主义的口号是“我们比任何人都强”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民族主义者说“我们可以独立”，种族主义者说“我们可以孤立”。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民族主义者说“我们不依赖其他人”，种族主义者说“我们不需要其他人”。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不再解释，而要求读者凭这三组对照“自己体会一下”二者的区别。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "以“口号”为对照维度：不比任何人差 / 比任何人都强（P001—P002）。",
    "以“独立/孤立”为对照维度（P003—P004）。",
    "以“不依赖/不需要”为对照维度（P005—P006）。",
    "不作论证与定义，直接要求读者自己体会（P007）。"
   ],
   "concept_usage": [
    {"term": "民族主义", "meaning": "本文只用三句口号刻画它：不比任何人差、可以独立、不依赖其他人。", "evidence": "P001", "ambiguity": "无定义、无出处、无例证，与学界通行含义的关系不明。"},
    {"term": "种族主义", "meaning": "本文只用三句口号刻画它：比任何人都强、可以孤立、不需要其他人。", "evidence": "P002", "ambiguity": "同上；与民族主义是否重叠、是否互斥均未说明。"},
    {"term": "独立/孤立", "meaning": "独立指可以不依附他人；孤立指可以不需要他人。", "evidence": "P003", "ambiguity": "二者差别留给读者体会，作者未界定。"},
    {"term": "不依赖/不需要", "meaning": "不依赖指实际关系上的不依附；不需要指需求层面的不必要。", "evidence": "P005", "ambiguity": "缺少现实判据，无法据以区分具体立场。"}
   ],
   "examples_and_targets": [
    "全篇无具体人物、事件、机构或数据；三组口号是唯一的对照材料，作者未注明其为引用还是自拟（P001—P006）。",
    "“自己体会一下”把读者设为结论的得出者（修辞安排，P007）。"
   ],
   "conditions": [
    "对照仅停留在“口号/说法”层面（P001—P006），未限定国家、时期或适用范围。",
    "全文无条件句、无程度限定词，也无例外说明。"
   ],
   "rhetoric_and_tone": "极简格言体与对照法：三组“A说…B说…”平行句，逐字替换关键词（不比任何人差/比任何人都强、独立/孤立、不依赖/不需要），不加论证；末句“自己体会一下”以口语化祈使收束，带留白与轻微调侃意味，读来像让读者自行对号入座。",
   "unresolved_questions": [
    "三组口号是否引自具体人物或文本，正文未注明出处，需外部核查。",
    "“民族主义”“种族主义”均未定义，与通行学术定义的关系不明。",
    "二者是否互斥、能否并存，正文未说明。",
    "无例证、无适用条件，无法判断结论的适用范围与强度。",
    "提问者问“区别在哪里”，作者只给出对照口号，未给出区分判据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "民族主义的口号是“我们不比任何人差”", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "种族主义的口号是“我们比任何人都强”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "民族主义者说“我们可以独立”", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "种族主义者说“我们可以孤立”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "民族主义者说，“我们不依赖其他人”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "种族主义者说，“我们不需要其他人”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "自己体会一下。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["民族主义", "种族主义", "政治观念"],
   "issue_candidates": ["民族主义与种族主义的区分", "独立与孤立的差别", "依赖与需要的差别"],
   "text_function_candidates": ["格言体", "对照", "留白"],
   "object_candidates": ["民族主义", "种族主义", "口号"],
   "working_keywords": ["不比任何人差", "比任何人都强", "独立", "孤立", "不依赖", "不需要"]
  },
  "notes": "极短篇（正文 120 字，7 段），无图片，全文已读。三组对照口号未注明出处，属需外部核查的事实性引用；正文无定义、无例证、无适用条件。published_at 与 updated_at 均为 2021-08-01，无版本差异迹象。"
 },
 "deb01db8": {
  "analysis": {
   "question_context": "提问者问印度食物是否脏、是否会导致腹泻。作者把问题拆为香料刺激、个体菌群适应、制作工艺与文化偏见四层，否认腹泻必然等于食物本身脏。",
   "content_units": [{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008"],"summary":"香料气味强烈且对多数动物有毒，人类食用的是低剂量刺激。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P009","P010","P011","P012","P013","P014","P015","P016","P017"],"summary":"消化反应被解释为菌群适应差异，初次接触某些香料可能腹泻，反复接触后可能减轻。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060"],"summary":"作者将印度旅行者腹泻归因于新菌群和饮食接触，而非笼统的印度食物肮脏，并以制作工艺和文化本位批评收束。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"外地人到印度腹泻可能来自首次接触当地常见香料及菌群适应不足，不等于印度食物整体脏。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"食物卫生判断不能把文化不适感直接当作食物本身有问题。","evidence":["E3"]}],
   "argument_steps":["先说明香料的刺激和毒性背景（P001-P008）。","再用菌群适应解释初次食用后的消化反应（P009-P017）。","最后比较卫生标准、制作工艺和文化偏见，否认印度菜因外观或接触方式而天然不卫生（P018-P062）。"],
   "concept_usage":[{"term":"卫生","meaning":"作者区分医学上明确的致病风险与文化上的恶心感。","evidence":"P041-P046","ambiguity":"医学事实和菜系总体安全性的判断未给出外部资料。"}],
   "examples_and_targets":["印度香料、当地菌群和旅行者腹泻（P009-P031）。","生食、腌制、发酵食品与印度菜制作方式的比较（P047-P058）。"],
   "conditions":["首次接触当地香料或菌群适应不足时（P018-P031）。","讨论卫生时须区分设计风险与执行问题（P041-P046）。"],
   "rhetoric_and_tone":"以反问、自问自答和跨菜系比较推进，语气鲜明，夹有对文化本位偏见的讽刺。",
   "unresolved_questions":["关于香料毒性、菌群传播和菜系安全性的事实断言需外部核查。","图片节点未核验，不能据图片补充结论。"],
   "evidence":[{"key":"E1","paragraph_id":"P008","quote":"人类也只能微量食用","relation":"supports"},{"key":"E2","paragraph_id":"P031","quote":"但这并不是因为“印度食物脏”","relation":"supports"},{"key":"E3","paragraph_id":"P046","quote":"都和食物本身是否洁净无关，是人自己的偏见问题","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "status":"needs_reread","full_text_checked":True,"image_checked":False,"notes":"正文已读；3 个图片节点尚未核验，故保留 needs_reread。香料、菌群与卫生安全相关事实断言待外部核查。"
 },
 "fb5d39a5": {
  "analysis": {
   "question_context":"提问者问为何很多人感觉越来越穷。作者区分客观财富、负债能力与主观穷感，反驳用居民负债率直接证明普遍变穷。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011"],"summary":"负债统计只覆盖正规贷款，能借且银行敢贷本身不直接等于变穷。","role":"rebuttal"},{"unit_id":"U002","paragraph_refs":["P012","P013","P014","P015","P016","P017","P018","P019","P020"],"summary":"用资产、负债和月度现金流的对照区分客观净额与主观压力。","role":"example"},{"unit_id":"U003","paragraph_refs":["P021","P022","P023"],"summary":"作者把结论概括为中国人未必越来越穷，而是越来越有穷感。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"居民负债率上升不能单独证明老百姓越来越穷，因为正规负债同时反映借款意愿和银行放贷意愿。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"客观净资产与日常还贷压力可以分离，主观穷感不等于客观财富减少。","evidence":["E3"]}],
   "argument_steps":["限定负债统计范围（P001-P011）。","以两种资产负债结构比较穷与穷感（P012-P020）。","收束为穷感增强而非必然财富下降（P021-P023）。"],
   "concept_usage":[{"term":"穷感","meaning":"面对持续还款和现金流压力时的主观贫困体验。","evidence":"P021-P023","ambiguity":"未区分收入、资产价格和生活成本变化。"}],"examples_and_targets":["50万余额租房与负债200万、拥有250万房产的对照（P012-P020）。"],"conditions":["讨论正规银行个人贷款时（P003-P011）。"],"rhetoric_and_tone":"以反问、数字对照和口语化讽刺推进。","unresolved_questions":["关于银行盈利、居民资产升值和负债结构的事实判断待外部核查。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"用“负债率越来越高”来证实“老百姓越来越穷”是不可靠的","relation":"supports"},{"key":"E2","paragraph_id":"P011","quote":"居民负债率高，其实反过来说明的是居民因为种种原因而敢于负债了","relation":"supports"},{"key":"E3","paragraph_id":"P021","quote":"中国人不是越来越穷了，而是越来越有穷感了","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；关于宏观经济、银行风险和资产升值的事实断言待外部核查。"
 },
 "38718990": {
  "analysis": {
   "question_context":"提问者描述母亲拒绝心理医生并寻求处理办法。作者把干预重点放在父母自身的改变，而非只把未成年子女送医。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"作者主张父母应先检视自身，因为子女会形成对父母的适应态。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P005","P006","P007","P008","P009","P010","P011","P012","P013"],"summary":"以不断寻找新的按钮比喻持续求助和修正父母自身。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P014","P015","P016","P017","P018","P019","P020","P021","P022"],"summary":"将教育效果归因于父母保持‘仍未找到正确方法’的信念，并总结应修正父母而非只修正子女。","role":"conclusion"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"未成年子女出现心理障碍时，父母应把自身改变作为优先干预对象。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"持续承认自己可能仍未找到方法，比寻找一个固定的正确按钮更重要。","evidence":["E3"]}],"argument_steps":["提出父母先求助的原则（P001-P004）。","用按钮比喻说明持续寻找专业帮助（P005-P013）。","以信念和自我修正收束（P014-P022）。"],"concept_usage":[{"term":"适应态","meaning":"子女对父母行为和环境形成的适应性反应。","evidence":"P003-P004","ambiguity":"未给出心理学定义或边界。"}],"examples_and_targets":["把父母求医比作寻找未按到的按钮（P005-P013）。"],"conditions":["论述对象是未成年子女及其父母（P001）。"],"rhetoric_and_tone":"训诫式、反复反问并以极端绝对语气强化责任归因。","unresolved_questions":["‘父母改变即可使子女好转’的心理学断言需谨慎外部核查，不能替代临床诊疗。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"不要给子女找医生，而要给你自己找医生","relation":"supports"},{"key":"E2","paragraph_id":"P003","quote":"你是什么样，子女会自动发展成对你的适应态","relation":"supports"},{"key":"E3","paragraph_id":"P014","quote":"一定是我没有找到正确的方法","relation":"supports"}]},
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；作者的心理与教育因果断言不替代专业诊疗意见，需独立核查。"
 },
 "0d2f3f3d": {
  "analysis": {
   "question_context":"提问者问老板在公司祷告并让‘圣徒’传教是否可以报警。作者优先讨论举报者的职业风险、技能独立性和后续就业，而未直接裁定法律问题。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"建议先辞职并建立再就业能力，再考虑举报，以降低被变相辞退的风险。","role":"action_advice"},{"unit_id":"U002","paragraph_refs":["P005","P006","P007","P008","P009","P010"],"summary":"把企业意识形态现象放进低端密集型行业的管理与动员逻辑中。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P011","P012","P013"],"summary":"指出举报记录可能影响再就业，因此应准备足以证明自身价值的理由。","role":"conclusion"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"举报前应先取得辞职和再就业的充分自由，以降低企业反制风险。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"仅依靠服从换取工作保障的人，在不同企业中可能重复遭遇意识形态管理。","evidence":["E3"]}],"argument_steps":["先给出辞职后举报建议（P001-P004）。","解释企业意识形态与行业竞争力（P005-P010）。","分析举报记录对就业的潜在影响（P011-P017）。"],"concept_usage":[{"term":"自由选择雇主","meaning":"具备知识技能和再就业选项，不被单一雇主反制。","evidence":"P004","ambiguity":"没有给出具体技能或法律标准。"}],"examples_and_targets":["基督教、佛教、道教、国学等企业意识形态（P005-P007）。"],"conditions":["建议限定在举报可能导致职业报复或再就业障碍的情形（P001-P017）。"],"rhetoric_and_tone":"现实主义、风险规避式建议，带有职业训诫口吻。","unresolved_questions":["公司祷告和传教是否违法、是否构成劳动权益侵害，正文未作法律分析。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"建议你先辞职，再举报","relation":"supports"},{"key":"E2","paragraph_id":"P004","quote":"获得自由选择雇主的充分优势","relation":"supports"},{"key":"E3","paragraph_id":"P011","quote":"你重新找的企业多半换汤不换药","relation":"supports"}]},
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；法律问题未被直接回答，需另行咨询劳动法或监管渠道。"
 },
 "187c3d69": {
  "analysis": {
   "question_context":"提问者问如何停止心理反刍带来的折磨。作者不把痛苦和反刍完全视为被动折磨，而是指出其中可能包含自我意义感和优越感的奖赏。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006"],"summary":"作者把痛苦描述为能提供深刻感、自我存在感和审判世界的心理收益。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P007","P008","P009"],"summary":"指出提问只要求停止折磨而非停止反刍本身，据此认为问题中已有享受线索。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P010"],"summary":"给出结论：停止反刍须先承认自己正在享受。","role":"conclusion"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"反刍痛苦可能同时提供深刻感、优越感和自我存在感等心理收益。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"停止反刍的起点是承认自己在享受其中某些收益。","evidence":["E2"]}],"argument_steps":["列举痛苦反刍的心理奖赏（P001-P006）。","从‘停止折磨’与‘停止反刍’的措辞差异推断动机（P007-P009）。","以承认享受作行为建议（P010）。"],"concept_usage":[{"term":"反刍痛苦","meaning":"反复咀嚼痛苦并从中获得意义或优越感，同时伴随恐慌和自我怀疑。","evidence":"P001-P006","ambiguity":"未区分临床意义上的反刍、创伤反应和一般沉思。"}],"examples_and_targets":["把反刍痛苦比作辣味牛肉干越嚼越香（P006）。"],"conditions":["作者讨论的是提问者自述的心理反刍，而非临床诊断（P001-P010）。"],"rhetoric_and_tone":"挑衅式揭示、讽刺和反转，结尾极度简短。","unresolved_questions":["若提问者存在抑郁、焦虑或自伤风险，正文未提供安全干预或求助建议。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"人最大的毒品是痛苦本身","relation":"supports"},{"key":"E2","paragraph_id":"P010","quote":"从承认“我在享受”开始","relation":"supports"}]},
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；本文未提供临床心理干预建议，涉及持续痛苦或安全风险时需专业求助。"
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
