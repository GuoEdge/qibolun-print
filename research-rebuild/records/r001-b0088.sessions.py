# -*- coding: utf-8 -*-
"""批次 r001-b0088 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0088.sessions.py            # 写 out/r001-b0088.out.jsonl
  python3 records/r001-b0088.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0088"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0088.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4791bcbd": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么口红色号不用六位十六进制来标？提问者的预设是色号本可用六位十六进制这种简洁编码表示，期待一个技术性解释。作者不解释行业惯例，也不接受该预设，而是列举色号还需表达光泽度、防水性、保湿性、金属感、覆盖力、附着力、香型等多项属性，反问“六位哪够”，并以“Jon Snow，you know nothing.”“加强学习。”调侃并训诫提问者；其立场是六位十六进制远不足以承载口红色号的信息量，属提问者认知不足。全文仅四句，brief 与正文一致。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002"],"summary":"口红色号除颜色外还要表达光泽、防水、保湿、金属感、覆盖力、附着力和香型等属性。","role":"claim"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"六位十六进制编码不足以表达口红产品的多维属性。","evidence":["E1"]}],
   "argument_steps":["列举颜色之外的属性。","以‘六位哪够’否定单一颜色编码的充分性。"],"concept_usage":[{"term":"色号","meaning":"需要同时承载颜色及产品质感、性能等属性的标识","evidence":"P001"}],"examples_and_targets":["光泽度、防水性、保湿性、金属感、覆盖力、附着力、香型。"],"conditions":["若色号只表达颜色，六位编码才可能足够；作者讨论的是完整产品标识。"],"rhetoric_and_tone":"极短、反问和调侃，带有训诫色彩。","unresolved_questions":["未说明行业色号实际编码规则。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"人家还有光泽度，防水性、保湿性、金属感、覆盖力、附着力、香型","relation":"supports"}] 
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
 "eb8d27c4": {
  "analysis": {
   "question_context": "提问者（Q001）问：有修养的人应该如何表达他的愤怒？提问者假定愤怒可以被“表达”，并关心其修养化的方式。作者不讨论情绪宣泄技术，而是把“有修养”界定为给人最大的 benefit of doubt、在契约模糊地带向对自己更严苛的方向作收敛解释，并把这种人的愤怒描述为递进的三句话（“哦？”“你确信要这样吗？”“祝你人生好运”）与两次机会（先给机会解释，再给机会撤销），仍不撤回则“接下去就必有改变”。立场区分：作者未否定提问，而是以“不勉强”为边界，说明有修养者的愤怒主要以信号、抽身与撤销担保的方式显现；其真正损失不是资源，而是每多一个纯良的人转过脸就离魔鬼更近一层，并把对这类信号的敏感列为父母家教的责任。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060","P061"],"summary":"有修养意味着给最大善意推定；愤怒以‘哦？’、‘你确信要这样吗？’和‘祝你人生好运’递进，分别给解释、撤销和最后告别机会，超过限度仍不撤回则契约改变。","role":"argument"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"有修养的人在模糊地带向对自己更严苛的方向解释，并尽量不以情绪强迫他人。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"‘哦？’是需要解释的信号，‘你确信要这样吗？’是撤销机会；仍不撤回则意愿落定并带来新的契约状态。","evidence":["E2","E3"]}],
   "argument_steps":["定义修养为最大善意推定。","解释三句递进信号及其机会。","说明不撤回后的关系与资源后果。","把对微弱信号的敏感延伸到家教。"],"concept_usage":[{"term":"不勉强","meaning":"不以明显情绪和压力迫使对方违背本心","evidence":"P033"},{"term":"哦？","meaning":"越过灰色地带后要求解释的低强度警告","evidence":"P007"}],"examples_and_targets":["契约模糊地带、关系担保、父母对子女的家教。"],"conditions":["对方若认真解释或撤回，关系尚有缓冲；不撤回则必须适应新契约。"],"rhetoric_and_tone":"冷峻、递进式训诫，夹有威胁、反讽和极端后果描写。","unresolved_questions":["文章把社会关系后果作强烈推演，未给外部案例。"],"evidence":[{"key":"E1","paragraph_id":"P005","quote":"有修养，意味着会给人最大的benefit of doubt。","relation":"supports"},{"key":"E2","paragraph_id":"P007","quote":"‘哦？’就是你需要解释的信号。","relation":"supports"},{"key":"E3","paragraph_id":"P037","quote":"因为你的意愿已经落定，它必须得到尊重。","relation":"supports"}]
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
 "024252b1": {
  "analysis": {
   "question_context": "提问者（Q001）问：怎么做个有修养的人？提问者要的是修养的养成方法。作者先摆出流行看法（有修养最重要的是仁爱、克己复礼、温柔），随即反驳，主张有修养最快的捷径是高傲、是不屑于去做某些事，并把“不做”分为不敢做、不能做、不该做、不忍做、不屑做五类，逐一说明前四类都会被处境推翻，只有“不屑做”最刚硬，因为它依靠人根深蒂固的傲慢。作者进而称这种人的“谦虚”与“仁爱”很大程度上只是不屑于欺负人、不屑于损人利己，客观上已有肉眼可见的修养和自我要求即为大福利，故不必追究动机（拈花指背后是否小无相功）；末段转向真正的问题是虚荣。立场区分：提问者求修养之法，作者给的是对“有修养”的动机重述与流行理解的翻转。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012"],"summary":"作者把修养的捷径定义为不屑于做某些事，区分不敢、不能、不该、不忍和不屑，认为不屑做最刚硬并能客观形成修养。","role":"claim"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"有修养最快的捷径是高傲和不屑于做猥琐、损人利己之事。","evidence":["E1","E2"]}],"argument_steps":["先列出仁爱、克己复礼、温柔的常见理解。","把不做分为五种动机并比较其稳定性。","将谦虚仁爱解释为对欺负人和损人利己的不屑。","以虚荣指出真正问题。"],"concept_usage":[{"term":"不屑做","meaning":"对猥琐和蝇营狗苟有根深蒂固的憎恶，不因压力而选择","evidence":"P006"}],"examples_and_targets":["不敢做、不能做、不该做、不忍做、不屑做；损人利己。"],"conditions":["不屑做的稳定性取决于是否被逼到生死与蝇营狗苟之间。"],"rhetoric_and_tone":"反转常识、尖锐反讽、格言化。","unresolved_questions":["未给出培养不屑动机的具体实践方法。"],"evidence":[{"key":"E1","paragraph_id":"P002","quote":"有修养最快的捷径是高傲，是不屑于去做某些事。","relation":"supports"},{"key":"E2","paragraph_id":"P008","quote":"这些人的‘仁爱’，很大程度上是因为不屑于损人利己。","relation":"supports"}]
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
 "c364b908": {
  "analysis": {
   "question_context": "提问者（Q001）问：觉得自己特别虚荣怎么办？提问者自认虚荣、求解决办法。作者不直接给对策，而是提出一个自查指标——话语中“我”字的使用密度，并给出解释链条：功利主义社会把功成名就当作人生价值的绝对标准，使每个人心中被装上“价值炸弹”，青少年无法直接面对市场与自然，只能靠他人的鉴定性意见安抚自己，于是把“我是否会成功”在实践上做成“我是否可以争取到足够多的人赞同我会成功”，成为一场不自知的选举，而“我”正是标准的选举关键词。作者主张真正该面对的是“客观的审视”与客观规律，与客观规律打交道多的人（广义上的手艺人）会发现“我”字多余，因而建议养成对使用“我”字的敏感性，末句以“如无必要，勿增我字”作结。立场区分：作者把提问者的“虚荣”重新定位为焦虑与竞选心态的语言症状，给出语言层面的自查与转移，而非安慰或道德训诫。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039"],"summary":"用‘我’字密度作为虚荣和焦虑的自查线索，批评依赖他人认可的选举式成功观，主张回到市场、自然和客观规律，以实践减少自我中心表达。","role":"argument"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"焦虑越强，语言中的‘我’越多；‘我’字密度可作为成熟度和焦虑程度的参考指标。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"他人点赞不能代替客观规律的检验，实践型手艺人会发现‘我’字是多余的。","evidence":["E2","E3"]}],"argument_steps":["提出‘我’字密度指标。","把虚荣追溯到功利社会、价值焦虑和认可投票。","列举市场、飞机、树、桥和纪录作为客观检验。","以减少不必要的‘我’字作为建议。"],"concept_usage":[{"term":"客观的审视","meaning":"产品、工程、自然结果等不依赖个人好感的现实检验","evidence":"P019"}],"examples_and_targets":["产品市场、飞机飞行、树结果、桥是否垮、运动纪录、实验报告和手艺人。"],"conditions":["‘我’字密度只是自查参考，不是诊断。"],"rhetoric_and_tone":"分析、讽刺和格言并用，反复设问。","unresolved_questions":["文章未区分正常自我陈述与虚荣性表达。"],"evidence":[{"key":"E1","paragraph_id":"P003","quote":"越焦虑的人，所说的话里‘我’字越多。","relation":"supports"},{"key":"E2","paragraph_id":"P025","quote":"更多的是在和客观规律对话、在受客观规律检验。","relation":"supports"},{"key":"E3","paragraph_id":"P038","quote":"没有‘我’，虚荣自散。","relation":"supports"}]
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
 "acb72aeb": {
  "analysis": {
   "question_context": "提问者（Q001）问：自己知道自己控制欲强应该怎么改变？提问者已接受“控制欲强”这一自我诊断并求改变方法。作者不接受该框架：先指出“大众心理学”的吊诡误区是把“症状”当成“诊断”“病因”，举抑郁症、多动症、PTSD、下肢功能障碍、电脑花屏等例，说明这类命名只是把不规范描述翻译为规范描述，尚未包含任何结论；再以亲子场景为例，说明在拽者（父母）视角其“控制欲”已是极力放松后的底线，半步不能再退，故真正的问题不是父母“控制欲”太强，而是他们想不清楚底线在哪里，这是信仰级的“缺少乐观的预期”问题，且在不改变超越理性的信仰级预设的前提下无解，因为击溃这份乐观的正是理性本身。文末以“悲观的人如何能变得乐观？”及一条带“⚠lexical未覆盖片段”标记的标题句收束，正文疑似在此中断。立场区分：提问者的自诊被作者判为不成立，作者把问题转置到乐观预期与信仰预设上。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020"],"summary":"反对把症状名称当作诊断和病因，指出‘控制欲强’只是规范化命名，尚未包含结论。","role":"rebuttal"},{"unit_id":"U002","paragraph_refs":["P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039"],"summary":"以父母阻止孩子翻阳台为例，说明控制行为存在视角差异；作者将根本问题转为缺少乐观预期和信仰级预设。","role":"example"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"‘控制欲强’等标签只是症状的规范命名，不等于诊断或病因。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"亲子控制冲突的根本问题是底线和乐观预期，而非单纯控制欲强弱；改变信仰级预设前问题无解。","evidence":["E3"]}],"argument_steps":["列举把症状当诊断的常见说法。","用蓝屏和下肢障碍类比命名不等于解释。","分析亲子场景的双方视角。","把问题推进到乐观预期和理性限制。"],"concept_usage":[{"term":"症状","meaning":"对表面表现的非规范描述","evidence":"P001"},{"term":"控制欲强","meaning":"一个可能描述行为的标签，不足以推出病因或结论","evidence":"P020"}],"examples_and_targets":["抑郁症、多动症、PTSD、蓝屏、父母拽孩子离开阳台。"],"conditions":["同一控制行为在被保护者和执行者视角下评价不同。"],"rhetoric_and_tone":"拆解心理学标签，使用讽刺、类比和亲子场景。","unresolved_questions":["文章未给出可操作的改变方案。","末尾含未覆盖的追加问题。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"误认为‘症状’就是‘诊断’，就是‘病因’","relation":"supports"},{"key":"E2","paragraph_id":"P018","quote":"在这一步可以说根本还没有任何的诊断可言","relation":"supports"},{"key":"E3","paragraph_id":"P030","quote":"真正的问题并不是父母们的‘控制欲’太强，而是ta们想不清楚底线在哪里。","relation":"supports"}]
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
 "1a04670d": {
  "analysis": {
   "question_context": "提问者（Q001）设问：如果社会没有道德和责任感，再好的科技、再远的道路，有什么用吗？这是提问者的忧虑性判断。作者不承接该忧虑，直接判为“不必要的担心”：理由是文化再负面也会像凭空出现突变种一样自动生出天赋异禀的人重新唤起人群中的神性；人类文化是绝妙的培养基，过于“邪恶”时会成为仁人志士出人头地的土壤，过于“正义”时又会成为“邪恶”生根发芽的温床，这种阴阳交换常使正义与邪恶的定义倒转，使人难辨新天使与改头换面的老魔鬼；社会存在自我更新机制并不断自我平衡，该机制至今没有失效过。作者最终把判断交还给读者的“信”：你若相信便是新天使浴火重生、不必忧心，你若不信便是第六天魔王毁灭一切——“Whatever you say goes. 尽在你一念之间.”，并以反问“真正的问题是，你为什么宁肯相信是后者？”作结。立场区分：提问者担忧道德崩溃使科技与道路失去意义，作者认为该担忧不必要，并把焦点移到读者选择相信哪一边。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013"],"summary":"作者认为文化会在过度邪恶或过度正义时产生反向平衡机制，筛选出重新唤起凝聚力的人，因此不必预先断定道德将彻底消失。","role":"claim"}],"main_claims":[{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"predicted","statement":"社会文化具有自我更新和阴阳逆转机制，会筛选出修复整体凝聚力的人；是否相信决定了对未来的判断。","evidence":["E1","E2"]}],"argument_steps":["否定对无道德社会的担心。","说明邪恶与正义过度都会孕育反向力量。","把天使或魔鬼的判断转为认识论问题。","将结论落在信任或不信任这种机制。"],"concept_usage":[{"term":"阴阳逆转","meaning":"过度正负文化条件相互孕育反向力量的机制","evidence":"P003"}],"examples_and_targets":["天使、魔鬼、仁人志士、第六天魔王。"],"conditions":["结论依赖对社会自我更新机制的信任。"],"rhetoric_and_tone":"寓言化、二元对照、带宗教隐喻。","unresolved_questions":["未提供‘机制至今没有失效’的历史证据。"],"evidence":[{"key":"E1","paragraph_id":"P005","quote":"社会存在着一种自我更新机制，会不断地自我平衡","relation":"supports"},{"key":"E2","paragraph_id":"P009","quote":"根本不必忧心‘人类彻底失去道德感’","relation":"supports"}]
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
 "336acd26": {
  "analysis": {
   "question_context": "提问者（Q001）问：怎样做到“不抱怨”？作者先为抱怨正名并界定：抱怨是自己承担了不该承担的、觉得不公平，尤其是承担了别人本该承担的；随即以第一人称代抱怨者抒发郁愤（“我连说也不能说一句吗？”“你们把我当作畜生吗？！！！”），指出若只想避免抱怨的负效应，就该去学“巧抱怨”而非“不抱怨”。接着给出组织论根据：分工设计总不完美，责权利交接处必有交叠与脱节，抱怨因此有根有据；但若无人把这些断裂弥合、安抚，产品线就会断裂、组织就会灭亡，故组织必须靠不抱怨的人吃掉这个亏，这类愿意承担不公平责任的人是组织的脊梁与命脉。作者进一步把“勇于任事，甘冒风险，受责无怨”界定为爱（“受责无怨”却一定是），并称不求回报、给予不配受的人是其本质要求。文末正面作答：第一，开口之前先反省清楚这是不是抱怨；并区分抱怨（为榨取抚慰、认可和补偿，本质是一种“暴力撒娇”、负面的亲密表达）、批评（不涉及批评者自身获利）与报复（自觉抱怨得不到爱的回应而索取心理安慰，已丧失理智），建议对抱怨中可认可的部分给予清晰明确的认可、对不可认可的部分温和拒绝。正文在 P076 处中断（“但这其实是人生中对于‘抱怨可以获得本该获得的宽慰’已经屡试屡败，”），未完。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021"],"summary":"作者先把抱怨定义为承担不该承担之事后的不公平感和痛苦表达，再区分抱怨、抵抗与巧妙表达。","role":"definition"},{"unit_id":"U002","paragraph_refs":["P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060","P061","P062","P063"],"summary":"组织分工必有交叠脱节，抱怨有时有根有据；作者认为承担无人认领责任且受责无怨的人是组织和关系的脊梁，并把这种无怨承担定义为爱。","role":"conclusion"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"抱怨是已经承担不公平之后对痛苦和不该承担之事的表达，不等于事前抵抗。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"组织无法完美设计，需要有人承担无人认领的责任；勇于任事、受责无怨才构成作者所说的爱。","evidence":["E2","E3"]}],"argument_steps":["定义抱怨并区分巧抱怨。","说明组织分工产生抱怨的结构原因。","筛选真正无怨承担者与投机者。","把无怨受责从组织扩展到亲子和伴侣关系。"],"concept_usage":[{"term":"巧抱怨","meaning":"正确表达负面情绪并避免抱怨负效应","evidence":"P019"},{"term":"受责无怨","meaning":"承担风险和责任后接受惩罚而不以委屈申辩","evidence":"P053"}],"examples_and_targets":["家庭、作坊、国家、社会、文明等组织；分工交叠和责任脱节。"],"conditions":["无怨承担不是无条件正确，需经过失败、惩罚和长期无怨的试炼。"],"rhetoric_and_tone":"强烈控诉与组织伦理论证交替，后段转为定义式抒情。","unresolved_questions":["作者没有给出避免被剥削的边界。","‘爱’的定义是作者在文中的研究对象，不应外推为普遍规范。"],"evidence":[{"key":"E1","paragraph_id":"P002","quote":"是指自己承担了自己不该承担的，觉得不公平。","relation":"supports"},{"key":"E2","paragraph_id":"P035","quote":"所有的组织——小到两个人的小家庭、小作坊，大到国家、社会、文明，愿意承担不公平的责任的成员，都是组织存在的根基所在。","relation":"supports"},{"key":"E3","paragraph_id":"P053","quote":"‘勇于任事’不见得是爱，‘甘冒风险’也不见得是爱，‘受责无怨’却一定是。","relation":"supports"}]
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
