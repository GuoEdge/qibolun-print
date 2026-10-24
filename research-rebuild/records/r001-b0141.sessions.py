# -*- coding: utf-8 -*-
"""批次 r001-b0141 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0141.sessions.py            # 写 out/r001-b0141.out.jsonl
  python3 records/r001-b0141.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0141"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0141.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "efaddd0a": {
  "analysis": {
   "question_context": "提问者问：如果拥有让别人体验自己痛苦的能力，会发生什么事情（Q001），预设这是一种“超能力”。作者不直接叙述后果，而是以第二人称反问连环的方式拆解这个预设：先否认能力等于该用、会用，再把这种能力降格为一般人共有的普通破坏力，随后重构“想动用它”的心理链条，并反问对方是否真有资格要求他人承担自己的痛苦；末段给出结论性判断。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "复述提问并立刻否定其预设：有这种能力不等于该用、会用。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "把提问所称的能力降格：它不是超能力，只是一般人都有的普通破坏力的一部分；且大部分人大部分时候不会对别人动用。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "为了自己的好处（报复快感或“寻求理解”）故意制造别人的痛苦说不通，硬干自己也会倒霉；劝告不要用“寻求体谅”处理痛苦。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "界定“寻求别人理解”：让对方知道自己的痛苦，使其在此基点上对待自己，从而换来宽待与分担，而宽限的时限与放松的标准要由宽限者另行补足。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015"], "summary": "以连环反问推测“你”的处境与动机：已经告诉过对方痛苦、只是不满对方反应，认为这比没说更痛苦；于是断定对方理解不深，想用“切肤体会”的超能力惩罚其漫不经心、纠正其评估权重。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016"], "summary": "补一层：若对方说过要爱，这种不被体谅更不可忍受。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "反问对方有何过错、是否应被单方面安排来体谅你；反问“你”怎么知道对方不是一直在苦苦忍耐、不把痛苦丢给你。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "反问该原则若成立是否反而更该优待你；并预测若让对方敞开闸门，多半会先被对方从未听闻的痛苦淹没。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P022", "P023"], "summary": "结论：你本身就是别人“不转嫁痛苦”原则的受益人，眼下的安宁来自别人不倾倒痛苦、宽容你的不敏感。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者否定提问的预设：拥有这种能力，不代表该用和会用。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种能力并不是什么超能力，只不过是一般人都有的普通破坏力的一部分。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称实际上大部分人在大部分时候都不会对别人动用这种能力。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断：为了自己的好处（包括报复的快感或“寻求理解”这类理由）而故意制造别人的痛苦，是说不通的。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称硬要这么做，自己也会倒霉。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“寻求别人理解”的机制：让对方知道自己的痛苦以获得宽待与分担，客观上缓解自己的痛苦、分散自己的损失，而被宽限的时限与被放松的标准要由宽限者另外补足。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者以连环追问推测“你”的动机：其实已经告诉过对方自己的痛苦，只是不满对方的反应，并因此认定对方理解得不够深，才想用让人感同身受的能力去惩罚其漫不经心、纠正其评估权重（原句以“对吧？”收束，属推测与质问）。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以反问表达：你受了痛苦并不是别人的错，别人没有责任被单方面安排来“体谅”你。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以反问指出对方也可能一直苦苦忍耐、避免把自己的痛苦丢出来让你“理解”，不能因为自己没被揪着去理解就认为只有自己有痛苦。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者预测若让对方敞开闸门，恐怕有一半以上几率你会先被自己从未听闻的对方的痛苦淹没。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论性判断：你本身就是其他人“不转嫁痛苦”原则的受益人，眼下的安宁来自别人不向你倾倒痛苦、宽容你的不敏感和没有眼力见。", "evidence": ["E14"]}
   ],
   "argument_steps": ["复述提问并否定预设（P001-P002）", "把所谓超能力改定义为一般人共有的普通破坏力（P003）", "给出经验性前提：大部分人大部分时候不动用（P004）", "判断为私利故意制造他人痛苦说不通、且反噬自身（P005-P006）", "给出行动劝告：不要用“寻求体谅”处理痛苦（P007）", "设问并界定“寻求别人理解”及其宽待—分担—成本转移机制（P008-P009）", "连环反问重构“你”的处境与动机（P010-P015）", "补充“对方说过要爱”的加重情形（P016）", "反问他人之责与他人亦在忍耐（P017-P019）", "反问该原则若成立是否更该优待你，并预测反被淹没（P020-P021）", "收束为“你是不转嫁痛苦原则的受益人”（P022-P023）"],
   "concept_usage": [
    {"term": "超能力／让别人体验你的痛苦的能力", "meaning": "提问者预设的特殊能力；作者否认其为超能力，改称它只是一般人都有的普通破坏力的一部分（P003）。", "evidence": "P003", "ambiguity": "作者并未说明这种“能力”具体指言语伤害、情绪施压还是字面意义的能力，所指范围不明。"},
    {"term": "寻求别人的理解／体谅", "meaning": "把自己受过的痛苦让别人知道，使对方以此为基点对待自己，从而获得宽待与分担，而宽限的成本由宽限者承担（P008-P009）。", "evidence": "P009", "ambiguity": "作者把它称为“手段”，语带贬义；与一般意义上的“被理解”是否同一，文中未区分。"},
    {"term": "不转嫁痛苦原则", "meaning": "别人不向你倾倒自己的痛苦、宽容你的不敏感，从而给你留下安宁（P022）。", "evidence": "P022", "ambiguity": "作者加引号使用，称其为“原则”，但未说明这是明确规则还是默认默契。"}
   ],
   "examples_and_targets": [
    "“我再发脾气或者违约，别人就不会再那么‘苛求’我”（P009）——作者假设性举例，说明寻求理解换来的宽待与分担。",
    "“对方说了要爱”（P016）——作者举的加重情形，属修辞性质的反问材料。",
    "“报复的快感”“寻求理解”（P005）——作者列举的两种动机，属被作者评判的对象。",
    "“让对方敞开闸门……被痛苦淹没”（P021）——作者的比喻性预测，非事实数据。"
   ],
   "conditions": [
    "“有这能力，不代表该用和会用”（P002）：能力、正当性与使用能力三件事被分开。",
    "“实际上大部分人在大部分时候”（P004）：作者给出的是量化的通常情形，非绝对命题。",
    "“为了自己的好处——这包括报复的快感或者‘寻求理解’这样似乎冠冕堂皇的理由”（P005）：作者所批评的行为以“为自己好处”为条件。",
    "P009 的宽待—分担机制以对方肯于宽限为条件，且明说被宽限的时限与放松的标准要由宽限者另行补足。",
    "“你其实是先告诉了对方你的痛苦的”（P011）：P011-P015 的推论以“已经告知过对方”为前提。",
    "“恐怕有一半以上的几率”（P021）：作者自陈这是概率性预测。",
    "“你现在能过得如此安宁，本身就是别人不向你倾倒自己的痛苦……的结果”（P022）：结论以他人自我克制为条件。"
   ],
   "rhetoric_and_tone": "通篇第二人称，连环反问加“对吧？”收束，近似训诫与诘问；口语化、含讽刺（“冠冕堂皇”“感同身受”均加引号）；结构上是先否定预设、再把超能力降格为普通破坏力、继而重构对方心理、最后以“你本身是受益人”作结。",
   "unresolved_questions": [
    "提问者的具体身份与处境不明，作者以泛化的“你”进行推测，无法确定其是否在描述提问者本人。",
    "P020 所述原则“如果对方对自己苦难的反应不够令自己满意，就可以用让对方感同身受来改善结果”是否真被提出或成立，作者以反问呈现，未给出论证依据。",
    "P021“一半以上的几率”属修辞性预测，文中无来源或数据。",
    "本文更新时间为 2025-09-23，晚于发布时间 2021-07-08，语料未提供版本差异说明，仅以当前版本 text 为准。",
    "brief 末句“而故意制造别人的痛”明显截断，brief 与正文对应但不完整。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "有这能力，不代表该用和会用。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "这种能力并不是什么超能力，只不过是一般人都有的普通破坏力的一部分罢了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "实际上大部分人在大部分时候都不会对别人动用这种能力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "而故意制造别人的痛苦，这是说不通的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "硬要这么干，自己也会倒霉就是了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "客观上就能缓解我的痛苦、分散我的损失", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "那些被宽限的时限、被放松的标准，自然会由宽限者去另想办法补足", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "你其实是先告诉了对方你的痛苦的，你只是对对方的反应不满意", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "你于是认定那是因为对方对你的痛苦理解得还不够深", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "好惩罚对方的漫不经心、好“纠正”对方的这个评估权重", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "其实，你受了这样的痛苦，别人有什么错呢？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "你怎么知道对方就没有苦苦忍耐、没有万般忍受避免把自己的痛苦丢出来让你“理解”呢？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "恐怕有一半以上的几率是你会先被你从未听闻的对方的痛苦淹没", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "你自己本来就是其他人“不转嫁痛苦”原则的受益人", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系与心理", "伦理与劝诫"],
   "issue_candidates": ["用让他人感同身受来报复或纠正对方是否正当", "寻求体谅与痛苦转嫁的代价", "痛苦理解的不可替代性"],
   "text_function_candidates": ["答疑", "劝诫", "论辩"],
   "object_candidates": [],
   "working_keywords": ["感同身受", "寻求理解", "转嫁痛苦", "报复的快感", "宽限", "普通破坏力"]
  },
  "notes": "本篇无图片节点。全文为第二人称诘问式议论，作者以“你”指代持有该能力/心态者，未在文中确认“你”即提问者，也未点名任何具体对象，故 object_candidates 留空。brief 末句被截断（“而故意制造别人的痛”），仅作导航，未据以补写正文。updated_at（2025-09-23）晚于 published_at（2021-07-08），语料未给出修订说明，按当前版本 text 记录。"
 },
 "254474b3": {
  "analysis": {
   "question_context": "提问者问“什么是「现代性」？你如何理解「现代性」？”（Q001），属概念解释请求。作者先给出一句定义式判断，再以设问补出被扭转的“基本假设”与取而代之的相反假设，接着排除一种流行的定义（自工业革命开始的思想变革），区分“现代主义”与“现代性”，最后给出程度性判据、举例说明并收束为“是今非古”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出“现代性的本质是一个基本假设的扭转”，并设问补出被扭转的旧假设：真理已被发现并阐述完毕、前人祖先大体正确、今人只做万变不离其宗的权变。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "给出正面定义：现代性是基于相反假设（前人出于无知愚昧、真理永远在现在）的一种思想倾向。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "排除“从工业革命开始的思想变革”这一理解：那样会出现“2100年的后人算什么”的问题，且“后现代”一词早已用尽、世代命名无法继续。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "界定“现代主义”为“越接近当前的越接近真理”的信念；称现代性是人的潜意识受这种价值观主导程度的描述，越在更多议题上确信今人胜前人、未来人胜今人就越有现代性。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "限定“前人”的范围包括父辈甚至三五年前的一代，并提醒不要假定自己的现代性是百分之百。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015"], "summary": "举例说明现代性并不彻底：可能觉得传统做法的驴肉火烧更好吃、老寺庙更灵、西装不如鹤氅帅，有人甚至觉得原始社会最先进，故在很多方面并不认同现代更先进。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P016"], "summary": "反例：古人的现代性显著差一些，常规性认为“世风日下、人心不古”，如孔夫子言必称三代之治。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019"], "summary": "结论：古人可以有现代性、今人也可以缺乏现代性、后人眼里你也可能“有现代性”；现代性本质上是“是今非古”的思想倾向，作者声明此处不谈好坏。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称现代性的本质是一个基本假设的扭转。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称被扭转的旧假设是：真理已经被发现并被阐述完毕，前人/祖先大体上正确，今人只需要进行万变不离其宗的权变。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义现代性为基于相反假设——前人一切信念皆出于无知和愚昧、真理永远在现在——所体现出来的一种思想倾向。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认现代性指“从工业革命开始的思想变革”，理由是那样会使“2100年的后人”无法安放，并指出“后现代”一词在60年代就已用尽。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“现代主义”指一种“越接近当前的越接近真理”的信念。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称现代性是人的潜意识受这种价值观主导的程度的一种描述。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者给出程度判据：越是在更多议题上确信今人比前人强、未来人比今人强，就越具有现代性。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者限定“前人”不是指两三百年前的人，而是连父辈乃至三五年前这一代都包括在内。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者主张不要假定自己的现代性是百分之百——在饮食、寺庙、服饰等很多方面人们并不认同现代更先进。", "evidence": ["E10", "E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称古人现代性显著差一些，常规性认为“世风日下、人心不古”，并以孔夫子言必称三代之治为例。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出结论：古人可以有现代性，今人也可以缺乏现代性，几百年后的后人眼里你也可以被称为“有现代性的人”。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结：“现代性”本质上就是一种“是今非古”的思想倾向。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明本文不谈谁好谁坏，只是坦率说明这个概念。", "evidence": ["E16"]}
   ],
   "argument_steps": ["给出定义式判断：现代性是基本假设的扭转（P001）", "设问并陈述被扭转的旧假设（P002-P003）", "陈述取而代之的相反假设并据此定义现代性（P004）", "排除“自工业革命开始”这一通行理解，用2100年后人与“后现代”一词的反问作理由（P005-P007）", "区分现代主义（信念）与现代性（受该价值观主导的程度）（P008-P009）", "给出程度判据（P010）", "限定“前人”的时间范围并提醒现代性非百分之百（P011-P012）", "以饮食、寺庙、服饰、原始社会等举例（P013-P015）", "以古人的“世风日下、人心不古”和孔子言必称三代之治作反例（P016）", "得出古人可有现代性、今人可缺现代性的结论（P017-P018）", "声明不作价值评判（P019）"],
   "concept_usage": [
    {"term": "现代性", "meaning": "基于“前人出于无知愚昧、真理永远在现在”这一假设的思想倾向；作者又称其为人的潜意识受“越接近当前越接近真理”价值观主导的程度（P004、P009、P018）。", "evidence": "P004", "ambiguity": "文中先说是“思想倾向”，后又说是“程度的一种描述”，两种表述的关系作者未交代。"},
    {"term": "现代主义", "meaning": "一种“越接近当前的越接近真理”的信念（P008）。", "evidence": "P008", "ambiguity": "作者未说明现代主义与现代性是否只是信念与程度之别。"},
    {"term": "前人", "meaning": "作者特意解释为包括父辈乃至三五年前的一代，而非仅指两三百年前的人（P011）。", "evidence": "P011", "ambiguity": "原文此句有引号残缺（“注意——前人”不是指…），属笔误，含义仍可辨。"},
    {"term": "是今非古", "meaning": "作者对现代性本质的概括：以今为是、以古为非（P018）。", "evidence": "P018", "ambiguity": "作者未讨论该倾向在具体议题上的强弱差别。"}
   ],
   "examples_and_targets": [
    "“2100年的后人眼里算什么”“后现代这词60年代就用完了……后后后后后现代”（P005-P006）——作者用来自反驳“现代性始于工业革命”的反问材料。",
    "驴肉火烧的传统做法、寺庙老的更灵、西装不如鹤氅帅、原始社会最先进（P013-P014）——作者的日常举例，用以说明现代性并非百分之百。",
    "“孔夫子就言必称三代之治”（P016）——作者举的历史例证，说明古人现代性差。",
    "“世风日下、人心不古”（P016）——作者所概括的古人常规看法，未注明出处。"
   ],
   "conditions": [
    "“你越是在更多的议题上确信今人比前人强……你就越是具有现代性”（P010）：现代性被表述为程度问题，随议题数量变化。",
    "“不要因此假定你的现代性就是百分之百”（P012）：作者明确设限。",
    "“在很多方面，你并不认同现代更先进”（P015）：限定于部分方面。",
    "“前人”的范围被限定为含父辈与三五年前的一代（P011）。",
    "P019“这里不谈谁好谁坏”：作者自我限定本文不作价值判断。"
   ],
   "rhetoric_and_tone": "说明性为主，夹设问自答（“什么基本假设呢？”）与戏谑口语（“前人知道个咸蛋鸟”“后后后后后现代”），并以“有完吗？”这类反问表达对世代命名的揶揄；概念词多带引号标示，结构为定义—排除—界定—举例—结论，末句声明中立。",
   "unresolved_questions": [
    "P003 所述的“基本假设”被加引号呈现，但未标明出自何人何书，无法确定是作者概括还是引用。",
    "P006“‘后现代’这词60年代就用完了”属需外部核查的事实性说法，文中未给出处。",
    "P016“古人常规性的认为‘世风日下、人心不古’”是概括性断言，未给史料或数据来源。",
    "P011 原文引号残缺（“注意——前人”不是指……），属原文笔误还是录入错误无法判断。",
    "updated_at（2025-10-18）晚于 published_at（2021-07-08），语料未提供版本差异说明，仅按当前版本 text 记录。",
    "“现代性”在 P004 是“思想倾向”、在 P009 是“程度的一种描述”，两种界定的关系文中未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "现代性的本质，就是一个基本假设的扭转。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "真理已经被发现并被阐述完毕，前人/祖先大体上是正确的，今人只需要进行万变不离其宗的权变。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "现代性是指基于相反的假设——即“前人知道个咸蛋鸟，ta们的一切信念皆出于无知和愚昧，真理永远在现在”——所体现出来的一种思想倾向。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "它不是指“从工业革命开始的思想变革”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "“后现代”这词60年代就用完了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "就是指一种“越接近当前的越接近真理”的信念", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "现代性是人的潜意识受这种价值观主导的程度的一种描述。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "你越是在更多的议题上确信今人比前人强，未来人比今人强，你就越是具有现代性。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "是连你爹这一代在内，甚至就是三五年前的这一代在内。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "不要因此假定你的现代性就是百分之百", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "在很多方面，你并不认同现代更先进。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "古人当然现代性显著的差一些", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "经典的例子比如孔夫子就言必称三代之治。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "古人可以有现代性，今人也可以缺乏现代性，而你在几百年后的后人眼里也可以被称为“有现代性的人”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "“现代性”，本质上就是一种“是今非古”的思想倾向。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "这里不谈谁好谁坏，只是坦率的说明这概念而已。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["思想史与观念史", "概念辨析", "文化评论"],
   "issue_candidates": ["现代性的定义", "现代性是否等同于工业革命以来的思想变革", "现代主义与后现代的关系", "今人是否一定胜于前人"],
   "text_function_candidates": ["答疑", "概念解释", "评论"],
   "object_candidates": ["孔夫子"],
   "working_keywords": ["现代性", "现代主义", "后现代", "是今非古", "前人", "权变"]
  },
  "notes": "本篇无图片节点。作者的“现代性”用法为自设定概念（先立假设再定义），文末声明不谈好坏，记录中已按其自述保留。P011 原文存在引号残缺（“注意——前人”不是指……），短引已避开该处。updated_at（2025-10-18）晚于 published_at（2021-07-08），语料未提供修订说明，按当前版本 text 记录。"
 },
 "b8b335c7": {
  "analysis": {
   "question_context": "提问者（自述为管理者）抱怨“现在的95后指挥不动，下班准时走，活安排不下去只能自己干”，问怎么办（Q001）。作者不讨论该前提是否成立，直接给出一套管理设计：把加班改造为奖赏与资格筛选机制，配合外包、人员流动和对抱怨者的利用，并以四个“首先/第二/第三/第四”分条展开。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "第一条建议：让加班的人落着好——优先培训资格、假期、国外出差、能涨资历的项目，跳槽时优先给推荐信与方便，日常给予特殊优待（减轻批评语气、报告优先级、加班后犒赏等）。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "第二条建议：限制加班资格，只有部分人因特殊资格被安排加班与应急，一般人默认不安排；被拒绝过一次的，一个周期内不再列入可邀请范围。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "第三条建议：建立足够丰富的外包供应商体系覆盖一切不涉密职能，超常规需求转外包，不优先用加班解决。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "第四条建议：保持招聘与解聘的正常人员流动，底层员工和外围供应商长期保持系统性流动性。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "给出加班的定位：不该是解决业务需求的常规选择，而应是观察谁有资格走合伙人路线的机制；资格不应是谁想要就能轮到的。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "操作要点：加班实质是奖赏，但不要在组织内公开宣扬，公开场合不赋予特殊意义、制度上不给明文优待，保持“加班没有任何有明确承诺的好处”的状态以免诱导投机。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "把发怨言、说怪话者视为管理资源：他们充当“自然的检察官”和“显影剂”，帮助发觉不可靠、不能依赖的人；没有他们则升职与培养决策容易犯错，代价更大。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P013"], "summary": "处理方式：对这些人依靠自然淘汰机制循环清洗（称其绩效较差），且不要在会上公开讲，以免打草惊蛇、引来人事处理上的麻烦。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议对加班者给予实际好处：优先培训资格、优先假期、优先国外出差、优先能涨资历的项目，跳槽时优先给好推荐信并提供方便，日常给予特殊优待。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议限制加班资格：只有部分人因特殊资格被安排加班和应急，一般人默认不安排；对下属发出加班邀请被拒后，一个周期内不再将其列入可发邀请的范围。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议建立足够丰富的外包供应商体系，尽可能覆盖一切不涉密工作职能，把超常规需求转给外包供应商，而不优先考虑用加班解决。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议保持招聘和解聘的正常人员流动，使底层员工和外围供应商长期保持系统性的流动性。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张加班不应是解决业务需求的常规选择，而应是一种观察谁有资格走合伙人路线的机制；且不是谁都有资格得到这个机会。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张加班实际上是奖赏，但不要在组织内公开宣扬，公开场合不给加班赋予特殊意义、制度上不给明文优待，以保持“加班没有任何有明确承诺的好处”的状态，避免诱导过度投机。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张在组织管理上要看到发怨言者、说怪话者的积极意义：他们担任“自然的检察官”和“显影剂”，帮助发觉哪些人不可靠、不能依赖；否则在升职和培养方面的决策容易犯错，这是更大的代价。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张对这些人依靠自然的淘汰机制循环清洗掉即可（称其绩效比较差），并同样不要在会上公开讲，以免打草惊蛇、既使迹象转入地下又引来人事处理上的麻烦。", "evidence": ["E12", "E13"]}
   ],
   "argument_steps": ["承接提问直接给出第一条：让加班的人落着好，并列具体优待（P001-P003）", "第二条：限制加班资格并设置拒绝的后果（P004-P005）", "第三条：以外包体系替代加班（P006）", "第四条：保持人员流动性（P007）", "给出加班的重新定位：资格筛选与合伙人路线观察机制（P008-P009）", "补充操作纪律：实际是奖赏但不公开、不明文，以防投机（P010）", "解释为何要允许怨言存在：抱怨者是发现不可靠者的“检察官”“显影剂”（P011-P012）", "给出对抱怨者的处理与保密要求（P013）"],
   "concept_usage": [
    {"term": "落着好", "meaning": "让加班者实际得到好处，包括资历、假期、出差机会、推荐信与日常优待（P001-P002）。", "evidence": "P002", "ambiguity": "作者未说明这些好处是否应写入制度，反而在 P010 主张制度上不明文。"},
    {"term": "加班资格", "meaning": "被安排加班与应急的准入资格，仅部分人拥有，且可因拒绝邀请而在一个周期内被取消（P004-P005）。", "evidence": "P005", "ambiguity": "“一个周期”的长度与“特殊的资格”的标准，文中未定义。"},
    {"term": "合伙人路线", "meaning": "加班所观察和筛选的晋升路径；作者称加班是观察谁有资格走这条路线的机制（P008）。", "evidence": "P008", "ambiguity": "作者未说明该路线与加班表现之间的具体判断标准。"},
    {"term": "自然的检察官／显影剂", "meaning": "作者对组织中发怨言、说怪话者的比喻性定位：他们能帮助管理者发觉不可靠、不能依赖的人（P011）。", "evidence": "P011", "ambiguity": "带引号的比喻，作者未说明具体识别方式。"},
    {"term": "外包供应商体系", "meaning": "覆盖不涉密工作职能的外部供应体系，用以承接超常规需求，从而减少加班（P006）。", "evidence": "P006", "ambiguity": "“不涉密”是作者给出的唯一排除条件，其余适用范围未说明。"}
   ],
   "examples_and_targets": [
    "“优先安排国外出差”“优先给好推荐信”（P002）——作者列举的具体优待手段，属行动建议而非事实断言。",
    "“减轻批评的语气”“特殊的报告优先级”“加班结束可以给予特殊犒赏”（P003）——作者列举的日常优待。",
    "“如果对下属发出加班邀请而被拒绝”（P005）——作者设定的情景条件。",
    "“接线式…外包供应商”“底层员工和外围供应商”（P006-P007）——作者建议的对象。",
    "“95后”仅出现在提问者字段（Q001），正文未出现该词，作者也未回应“指挥不动”这一说法。"
   ],
   "conditions": [
    "P005：只有因“特殊的资格”被安排加班和应急，一般人默认不安排；拒绝邀请者“在一个周期之内”不再列入邀请范围。",
    "P006：外包覆盖范围限定于“一切不涉密工作职能”，“有超常规的需求”才转外包。",
    "P010：优待不得公开宣扬、不得在公开场合赋予加班特殊意义、不得在制度上有明文规定的优待。",
    "P011：“如果没有这些人的诱惑”这一条件句为作者所设（该句语义跳跃，见未决问题）。",
    "P013：处理抱怨者同样以“不要在会上公开讲”为条件。"
   ],
   "rhetoric_and_tone": "分条操作手册式陈述（首先/第二/第三/第四），语气冷峻、直白，不作道德劝说；多处出现权术色彩浓厚的表述（加班是奖赏但不公开、把抱怨者当筛选工具、依靠自然淘汰清洗），并明确要求对员工保密。",
   "unresolved_questions": [
    "提问者所称“95后指挥不动，下班准时走”未被作者直接回应或评价，该前提是否成立文中未讨论；正文亦未出现“95后”。",
    "P011“如果没有这些人的诱惑”语义跳跃：抱怨者究竟如何“诱惑”出不可靠者，作者未展开，疑为原文表述不周。",
    "P005“一个周期”的长度、“特殊的资格”的判定标准，文中均未说明。",
    "该套做法与劳动法、加班报酬规定的合规关系，本文完全未涉及，属需外部核查的事项。",
    "brief 与正文一致但在“第二，”处被截断。",
    "updated_at（2026-02-23）晚于 published_at（2021-07-08），语料未提供修订说明，仅按当前版本 text 记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "首先，让加班的人落着好。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "跳槽的话，优先给好推荐信、提供方便。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "如果对下属发出加班邀请而被拒绝，那么在一个周期之内不会再把ta列入可以考虑发邀请的范围。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "有超常规的需求转给外包供应商解决，不优先考虑用加班解决。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "保持招聘和解聘的正常人员流动。底层员工和外围供应商长期保持系统性的流动性。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "而应该是一种观察谁有资格走合伙人路线的机制。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "不是谁都有资格得到这个机会", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "加班实际上是一种奖赏，但这话不要在组织内公开宣扬", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "以免诱导出过度的投机行为", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "这些人担任“自然的检察官”和“显影剂”去帮助你发觉哪些人不可靠、不能依赖", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这是更大的代价。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "依靠自然的淘汰机制循环清洗掉就可以了", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "同样，不要在会上公开讲这些，以免打草惊蛇", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理", "人力资源", "劳动与雇佣"],
   "issue_candidates": ["如何管理不愿加班的下属", "加班作为奖赏与晋升筛选机制", "外包替代加班", "人员流动与淘汰", "组织中的抱怨者"],
   "text_function_candidates": ["答疑", "行动建议", "管理操作指南"],
   "object_candidates": ["95后（仅见于提问者字段，正文未出现）", "外包供应商", "合伙人"],
   "working_keywords": ["加班资格", "落着好", "合伙人路线", "自然的检察官", "显影剂", "外包供应商", "投机行为"]
  },
  "notes": "本篇无图片节点。全文是面向提问管理者（“你”）的操作建议，非对劳动者一方的论述；作者未回应提问中“95后指挥不动”的判断，故该判断不属作者主张。文中多处要求对员工保密（P010、P013），记录中如实保留而未作价值评价。brief 与正文一致但在“第二，”处截断。updated_at（2026-02-23）晚于 published_at（2021-07-08），语料未提供修订说明，按当前版本 text 记录。"
 },
 "2d033768": {
  "analysis": {
   "question_context": "提问者转述“网传”说法——中国空间站内部整洁、国际空间站线路杂乱，且称这样设计更科学、裸露的线出问题时容易查找——问这种说法是否合理（Q001）。作者先给出替代解释（不整齐源于设计过于接近原型机），再以围棋盘连线类比说明交叉导致有序的不可能，列出两条解决路径，最后逐条反驳“便于维护”的说法并给出“时代局限”的判断。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出替代性解释：管线不整齐不是考虑维护性的结果，而是设计太接近“原型机”——需求不清晰时先用通用件完成功能，功能需求造成线路空间交叉，之后没时间优化就发射了。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "以围棋盘上随机摆放的连续编号黑白子要求同号互连作类比，称线路一旦空间交叉，在拓扑几何上就已经意味着有序的不可能。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "给出第一个解决方法：系统性重构“黑白子”的排布，使需要互连的对象在拓扑上更有序；并以“比如这样：”引向配图。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "给出第二个方法：把大量线路交叉集成到芯片内部，如同接线式电话系统进化为程控电话系统，以内部“混乱”换取针脚或接头排列有序。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "判断这种取舍是设计水平、制造水平带来的设计思想提升，跟维护恐怕没什么关系。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "直接反驳“不整齐便于维护”：整齐的线路绝对更有利于维护，没有争论的余地。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013", "P014"], "summary": "反驳“打开盖板增加维修难度”：称盖板多半无螺丝锁定，并推断空间站内部不允许难以严格管理的细碎物品、螺丝紧固应是舱外部件的做法，因为内部漂浮碎物隐患很大、可能被吸进气管。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016"], "summary": "结论：真相估计是国际空间站设计时期的设计工具与制造能力限制使其无法做复杂重构以提升有序性，这没什么特殊优势，只是时代局限的正常反映。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称电力系统管线不整齐不是考虑维护性的结果，而是设计太过于接近“原型机”的结果。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称设计时需求还不清晰，于是用通用件先完成功能；功能的设计需求导致线路在空间上交叉，后来也没花时间优化修改就发射了。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称线路在空间上一交叉就完了，在拓扑几何上已经意味着有序的不可能，并以围棋盘随机编号黑白子互连作类比。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出两条解决路径：一是系统性重构使需互连对象在拓扑上更有序；二是把大量线路交叉集成到芯片内部，以内部的“混乱”换取针脚或接头的排列有序（后者类比接线式电话系统进化为程控电话系统）。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者判断这其实是设计水平、制造水平带来的设计思想的提升，跟维护恐怕没什么关系。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断定整齐的线路绝对更有利于维护，这个没有争论的余地。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称“打开盖板增加维修难度”的说法不太可信，估计那些维修盖板多半是无螺丝锁定的。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者自陈为合理推断：空间站内部应该不太允许无法严格管理的细碎物品，很难想象会用螺丝固定什么，螺丝紧固应是舱外部件才会使用的做法。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称内部到处漫游的碎物不一定会引起短路或堵塞，但隐患很大，一不小心被吸进气管都不无可能。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者估计真相是国际空间站设计时期的设计工具和制造能力限制导致它无法进行太复杂的重构以提升有序性。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定“更科学”的说法：这没什么特殊的优势，只是时代局限的正常反映。", "evidence": ["E15"]}
   ],
   "argument_steps": ["提出替代解释：不整齐源于设计接近原型机（P001-P002）", "以围棋盘随机编号黑白子互连类比线路交叉的拓扑困境（P003-P004）", "列出解决路径一：重构排布使互连对象拓扑更有序（P005-P007）", "列出解决路径二：把交叉集成进芯片内部，以内部混乱换取接头有序（P008）", "判断这是设计思想的提升、与维护无关（P009-P010）", "正面反驳“整齐不利维护”：整齐绝对更有利于维护（P011）", "反驳“盖板增加维修难度”并推断盖板无螺丝锁定、内部不用螺丝（P012-P014）", "收束为“时代局限的正常反映”，非特殊优势（P015-P016）"],
   "concept_usage": [
    {"term": "原型机", "meaning": "需求尚不清晰时先用通用件实现功能的设计阶段；作者用它解释线路不整齐的成因（P001-P002）。", "evidence": "P002", "ambiguity": "作者未说明该判断的依据来源（如国际空间站的具体设计资料）。"},
    {"term": "有序的不可能", "meaning": "线路在空间上一交叉，就拓扑几何而言已不可能生成有序布线（P003）。", "evidence": "P003", "ambiguity": "该判断以围棋盘类比支持，未给出拓扑学证明。"},
    {"term": "以“混乱”换有序", "meaning": "把大量线路交叉集成到芯片或电路板内部立体管线结构，换取针脚、接头排列的有序（P008）。", "evidence": "P008", "ambiguity": "作者未说明该方案的代价与可行性边界。"},
    {"term": "时代局限", "meaning": "作者对国际空间站现状的归因：设计时期的设计工具与制造能力限制（P015-P016）。", "evidence": "P015", "ambiguity": "“估计”“不过是”表明这是作者的推测而非确证。"}
   ],
   "examples_and_targets": [
    "围棋盘上随机摆放连续编号黑白子并连接同号（P003）——作者的核心类比，用以说明交叉与有序的矛盾。",
    "接线式电话系统进化到程控电话系统、芯片或电路板内部的立体管线结构（P008）——作者的技术类比。",
    "“打开盖板增加维修难度”（P012）——被作者反驳的网传说法（转述对象，非作者观点）。",
    "空间站维修盖板无螺丝锁定、螺丝紧固用于舱外部件、碎物被吸进气管（P012-P014）——作者的推测性论据。",
    "国际空间站的“设计时期设计工具和制造能力”（P015）——作者的归因对象。"
   ],
   "conditions": [
    "P001-P002 的解释以“设计的时候需求还不清晰”为前提。",
    "P003 的拓扑困境以“线路在空间上一交叉”为条件。",
    "P006 的重构以“使得需要互相连接的黑白子有一个拓扑上更有序的结构”为目标条件。",
    "P012“估计那些维修盖板多半是无螺丝锁定的”、P013“没有意外的话”、P015“估计真相不过是”：作者均以推测语气呈现。",
    "P014“不一定会引起什么短路或者堵塞……不无可能”：同时保留否定与可能两面。",
    "P013：螺丝紧固的适用范围被限定为“舱外部件”。"
   ],
   "rhetoric_and_tone": "解释与反驳并重，口语化（“能整齐才有鬼了”“完蛋了”），以围棋盘连线作通俗类比，并以编号式（1）2））逐条回应网传说法；多处用“估计”“恐怕”“合理推断”自标推测强度，唯独对“整齐更有利于维护”给出无争论余地的强断言。",
   "unresolved_questions": [
    "本篇含 2 个图片节点（IMG001、IMG002），图片内容未经核验，需人工/多模态复核；P007“比如这样：”所指的图与两个图片节点的对应关系无法确认。",
    "提问所称“网传这样设计更科学”的出处不明，作者未指明所反驳的具体来源。",
    "作者对国际空间站设计时期、设计工具与制造能力的判断（P002、P015）为推测，文中未给出资料依据，属待外部核查。",
    "P005 称“解决的方法有两个”，但 P008 第二个方法同样以“一是”开头，疑为原文笔误，此处按上下文记为第二条路径。",
    "“维修盖板多半是无螺丝锁定”（P012）为作者的估计，需外部核查。",
    "updated_at（2021-07-11）晚于 published_at（2021-07-10），语料未提供修订说明，仅按当前版本 text 记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "其实电力系统管线不整齐不是考虑维护性的结果，而是设计太过于接近“原型机”的结果。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "设计的时候需求还不清晰，于是用了通用件先完成功能。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "后来也没花时间去优化修改，就这么发射了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "这意味着在拓扑几何上已经意味着有序的不可能了", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "能整齐才有鬼了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "使得需要互相连接的黑白子有一个拓扑上更有序的结构", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "以它的“混乱”，换到了针脚或接头的排列有序。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "这其实是设计水平、制造水平带来的设计思想的提升。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "跟维护恐怕没什么关系。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "整齐的线路绝对的更有利于维护，这个没有争论的余地。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "不太可信——估计那些维修盖板多半是无螺丝锁定的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "合理推断，空间站内部应该是不太允许无法严格管理的细碎物品的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "隐患很大。一不小心吸进气管都不无可能。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "估计真相不过是国际空间站的设计时期设计工具和制造能力的限制", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "这没什么特殊的优势，只是时代局限的正常反映。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["航天工程", "工程设计", "布线与人机工效"],
   "issue_candidates": ["空间站内部管线整齐与维护性的关系", "国际空间站线路杂乱的成因", "原型机式设计与通用件", "航天器内部碎物风险"],
   "text_function_candidates": ["答疑", "反驳", "技术解释"],
   "object_candidates": ["国际空间站", "中国空间站（仅见于提问者字段）"],
   "working_keywords": ["原型机", "通用件", "拓扑", "有序的布线", "接线式电话系统", "程控电话", "时代局限"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 2 个图片节点（IMG001、IMG002），图片内容未经核验，需图像核验；已读部分为正文文本，image_checked=false，故 status=needs_reread。P007“比如这样：”所指配图与两个图片节点的对应关系无法确认。文中“网传这样设计更科学、容易查找”属提问者转述的说法，作者持否定态度，记录中未归给作者。P005 称方法有两个而 P008 仍以“一是”开头，疑原文笔误。updated_at（2021-07-11）晚于 published_at（2021-07-10），语料未提供修订说明，按当前版本 text 记录。"
 },
 "ee36d234": {
  "analysis": {
   "question_context": "提问者问如何看待深圳拟首次修改员工工资支付条例、有哪些值得关注的信息（Q001）。作者不逐条评述条例，而是整体否定最低工资、加班与奖金规范一类干预劳动定价的政策，按“判断—举例算账—对白领的威胁—对大资本的意义—对低端职位的消灭—政策主张—对深圳表态—对鼓噪者喊话”的顺序展开。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总体判断：最低工资规定与奖金发放规定没有站得住脚的理由，是欧美在殖民利益支撑、选票政治机制下孵化出的短视政策，并称经济学界早有定论。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "称这类措施只“专利于”在职劳动者，对失业、待业者极端不利；对资本家并无根本大碍甚至极为有利，因高失业率与高就业门槛形成威慑和谈判筹码；并称劳动者自己不清楚充分就业的价值。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "以假设数字算账：1000个职位、50人失业时每个在职者面对的是50个竞争对手而非0.05个；市场放大到上海10万职位时5%即5000人；若职位无专业壁垒则并入200万人通用市场、有10万人等着你的位置，否则随时可被丢弃。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019"], "summary": "小结：失业人口对就业人口的威胁和压力具有杠杆性——“四两压千斤”。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021"], "summary": "行动主张：要不惜一切代价降低低端就业人口的失业率，这是救人于水火的急迫事；并指责吹着空调反对降低最低工资的人是残忍的。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "转向中高级白领：名义上保证在岗“福利底线”却造成职位净减少、失业净增加的政策对其有双重威胁——失业打击力加倍、竞争对手猛烈增加导致压力上升与涨薪迟滞。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "称高失业率对真正的大资本家是绝对喜讯：其产品需求刚性，且获得极大谈判筹码，只需展示招聘页面即可迫使劳动者接受低工资或放弃涨薪。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P030", "P031"], "summary": "以反问质疑“最低工资保障”“加班规定”“奖金规范”究竟给了什么确切的福利保障。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "论证给雇佣设定成本底线的后果：固然保证有工作的人体面，但消灭大量本可存在的职位；这些服务消失或被转移到远处、别国以外包或产品形式回流，至少要加付关税与运输费，处境总体多维恶化，只换来几近虚无的“福利”。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P039", "P040", "P041"], "summary": "定性：这是政党政治机制催生的愚昧政治正确，与川普“收中国关税打击中国”无水平区别，并造成欧美产业快速空心化；结果只剩“白领体面人／领食物券”的二元处境，因为合法的低端选择已被消灭。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P042"], "summary": "政策主张：劳动力定价根本不该是劳动法干涉的范围，劳动法应专注于反人身强迫、暴力威胁和合同欺诈。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P043", "P044"], "summary": "对深圳表态（此段在结构中是 heading 字段）：作者为深圳打破这种政治正确而高兴，并称这是对的，只是不是谁都有政治资本去承担误解风险做正确的事。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P045", "P046"], "summary": "补充量化判断：大型就业市场局部失业率达5%，对缺少职业壁垒的中低端劳动者已接近【地狱】，必须考虑搬迁到别的市场；不搬则谈不上“剥削”，辞职即可被替换。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "对知乎的学生、“打工人”的喊话：他们鼓噪维护最低工资门槛以“保住自己的福利”，作者要求其想清后果——被辞退就猪狗不如，因可作保护绳的低端工作已被消灭（低于5000的职位不存在），并引发向下挤压的竞争链条；末段提醒最低工资只是雇主成本的一部分。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称最低工资规定与奖金发放规定没有确切站得住脚的理由，只是欧美在殖民利益支撑、选票政治机制下孵化出的短视政策，并称经济学界早有定论。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称最低工资制、禁止解雇等干预劳动市场的措施只“专利于”在职劳动者，对失业、待业者极端不利。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这类政策对资本家并无根本大碍，甚至极为有利，因为它保持高失业率和高就业门槛，足以对在职者形成威慑与谈判筹码，压制薪资增长并提高压榨力度。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称劳动者自己不清楚保持充分就业对自己的价值有多大。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以假设数字说明失业者的压力：职位总数为1000而失业者50人时，每个在职者面对的是50个竞争对手；若市场扩大到上海10万职位，5%即5000人；若职位无专业壁垒而并入200万人的通用市场，等着该位置的有10万人，除非你比他们都强且强得足够明显。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结：失业人口对就业人口的威胁和压力具有“四两压千斤”的杠杆性。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张要不惜一切代价降低低端就业人口的失业率，称这是救人于水火的急迫事；并称吹着空调反对降低最低工资的人做的是残忍的事。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称名义上保证在岗“福利底线”却造成职位净减少、失业净增加的政策对白领有双重威胁：失业打击力加倍升高、竞争对手猛烈增加导致压力上升与涨薪迟滞。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称若真痛恨资本就应认清：高失业率对真正的大资本家是绝对喜讯，因其产品需求刚性且获得极大谈判筹码，可逼迫劳动者接受低工资或放弃涨薪。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑所谓“最低工资保障”“加班规定”“奖金规范”究竟给了劳动者什么确切的福利保障。", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者承认给雇佣设定成本底线在很大程度上保证有工作的人体面，但称它同时消灭大量本可存在的职位，这些服务消失或被转移到远处、别国以外包或产品形式回流，至少要多付关税与运输费，处境总体多维恶化，只得到近于虚无的“福利”。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种政策是政党政治机制催生的愚昧政治正确，与川普“收中国关税打击中国”没有水平区别，并事实上造成欧美产业快速空心化。", "evidence": ["E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称结果是只剩两种处境：要么有白领工作做个体面人，要么领食物券四海为家，因为“低端选择”被消灭、至少没有合法的。", "evidence": ["E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张“劳动力定价”根本不该是劳动法干涉的范围，劳动法应专注于反人身强迫、暴力威胁和合同欺诈。", "evidence": ["E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对深圳修改条例表态：为深圳有勇气打破这种愚昧的政治正确而高兴，认为这是对的，只是不是谁都有政治资本去承担误解风险做正确的事。", "evidence": ["E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称大型就业市场局部失业率达到5%，对缺少职业壁垒的中低端劳动者已接近【地狱】，必须考虑搬迁到别的市场中。", "evidence": ["E26"]},
    {"claim_id": "C017", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述被其批评的一方：知乎的学生、“打工人”们在鼓噪维护最低工资门槛，似乎这样可以“保住自己的福利”。", "evidence": ["E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者警告维护最低工资门槛的后果：被辞退就猪狗不如，因为可作保护绳的低端工作已被最低工资制消灭（低于5000的职位不存在），并造成低于5000者向上挤压的竞争链条；并强调最低工资只是雇主成本的一部分。", "evidence": ["E28", "E29", "E30"]}
   ],
   "argument_steps": ["开篇定性：最低工资与奖金规定是欧美殖民利益与选票政治的产物（P001-P002）", "指出其分配效应：专利于在职者、对失业者不利（P003）", "指出其对资本反而有利：高失业率形成威慑与谈判筹码（P004-P005）", "补充观察：劳动者不清楚充分就业的价值（P006）", "以1000/50、10万/5000、200万/10万等假设数字算账，说明竞争对手远多于直觉（P007-P017）", "小结为“杠杆性”（P018-P019）", "提出主张：不惜一切代价降低低端失业率（P020）", "指责反对者是残忍的（P021）", "转向白领：该政策对白领的双重威胁（P022-P025）", "指出高失业率对大资本家是喜讯（P026-P029）", "以反问质疑福利保障的实际内容（P030-P031）", "论证成本底线消灭职位、服务外移、处境总体恶化（P032-P038）", "定性为愚昧政治正确并与川普关税类比（P039）", "给出二元化后果（P040-P041）", "提出劳动法应只管反强迫、暴力威胁与合同欺诈（P042）", "对深圳修改条例表态（P043-P044）", "补充5%失业率即接近【地狱】的判断（P045-P046）", "对鼓噪维护最低工资门槛者喊话并警告后果（P047-P054）"],
   "concept_usage": [
    {"term": "最低工资制／最低工资规定", "meaning": "作者所反对的、给雇佣设定成本底线的政策；他称其消灭本可存在的低端职位（P032-P033）。", "evidence": "P033", "ambiguity": "作者未区分不同水平的最低工资或其实施细则，也未讨论执行强度差异。"},
    {"term": "充分就业", "meaning": "作者称劳动者不清楚保持充分就业对自己的价值有多大（P006），并以失业人数的竞争压力论证其价值。", "evidence": "P006", "ambiguity": "作者未给出“充分就业”的量化定义。"},
    {"term": "杠杆性", "meaning": "失业人口对就业人口的威胁和压力是“四两压千斤”的杠杆性（P019）。", "evidence": "P019", "ambiguity": "属修辞化表述，未给出计算方式。"},
    {"term": "劳动力定价", "meaning": "作者称其根本不该是劳动法干涉的范围，劳动法应只管反人身强迫、暴力威胁和合同欺诈（P042）。", "evidence": "P042", "ambiguity": "未说明加班时长、安全等事项是否也属“定价”范围。"},
    {"term": "愚昧的政治正确", "meaning": "作者对最低工资一类政策的定性，称其由政党政治机制催生，并造成欧美产业空心化（P039）。", "evidence": "P039", "ambiguity": "作者未界定“政治正确”的判准。"}
   ],
   "examples_and_targets": [
    "深圳拟修改员工工资支付条例（Q001、P043-P044）——本文的触发事件，作者表示支持。",
    "1000职位/50失业者、上海10万职位/5000人、200万通用市场/10万人（P007-P016）——作者自设的假设数字，非统计数据。",
    "“你想加薪？不干你就滚啊，门口排队的多的是”“打开招聘网站的页面”（P005、P029）——作者的拟言与修辞性场景。",
    "川普所谓“收中国关税打击中国”、欧美产业快速空心化（P039）——作者用作类比与后果举证。",
    "领食物券、非法移民（P040-P041）——作者举的美国式二元处境与修辞材料。",
    "知乎的学生、“打工人”（P047）——被作者批评的鼓噪者，属反驳对象。",
    "月薪5000/6000/10000的挤压链条（P052-P053）——作者的假设性举例。"
   ],
   "conditions": [
    "P001：作者对欧美政策成因的叙述以“殖民利益的支撑”“选票政治机制”为条件。",
    "P013：压力分析以“你的职位并没有什么大不了的专业壁垒”为条件，此时职位并入通用市场。",
    "P026：“如果你真的痛恨资本”为作者设定的条件句。",
    "P033：“固然可以在很大程度上保证凡有工作的都会很体面，但也同时消灭了大量本来可以存在的职位”——让步与代价并列。",
    "P035：“这能不能完全替代再说”——作者承认替代问题未解决。",
    "P040：“至少没有合法的”——作者自留限定。",
    "P045：接近【地狱】的判断限定于“大型就业市场局部失业率达到5%”“缺少职业壁垒的中低端劳动者”。",
    "P051-P052：作者否定存在“只要拉得下身段、接受一点消费降级就可以做的工作”作为保护绳。"
   ],
   "rhetoric_and_tone": "强断言与激烈措辞（“短视政策”“愚昧的政治正确”“残忍的事”“猪狗不如”“抬手给你一耳光”），大量反问、第二人称质问与拟言（“你想加薪？不干你就滚啊”），并用【】、引号作强调；把论敌定位为知乎的学生与“打工人”，直接喊话；结构为总判断→举例算账→分人群论证→政策主张→现实表态→对论敌喊话。",
   "unresolved_questions": [
    "P002“经济学界早有定论”未给出任何文献或人名，属待外部核查的引述性断言。",
    "P001 关于殖民利益与选票政治孕育最低工资制的历史因果叙述无出处。",
    "P007-P016 的数字均为作者假设性举例，非统计数据，不能当作事实数据引用。",
    "提问所问“有哪些值得关注的信息”未被作者逐条回应，深圳条例修改的具体条款内容本文未引述。",
    "P039 关于欧美产业空心化的归因及与川普关税的类比属作者判断，需外部核查。",
    "P040-P041 关于非法移民与“违法”工作的表述为修辞性反问，所指对象与事实基础不明。",
    "updated_at（2026-01-22）晚于 published_at（2021-07-10），语料未提供版本差异说明，仅按当前版本 text 记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "本来就没什么确切的站得住脚的理由", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这一点，经济学界早有定论。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "只是“专利于”【在职劳动者】、而对失业、待业的劳动者极端不利。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "它事实上对资本家并无什么根本大碍，甚至是极为有利的", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "去压制薪资的增长和提高压榨的力度", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "我发现劳动者们自己不清楚保持充分就业对自己的价值有多大。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "你错了，是每一个人都在面对50个竞争对手。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "那么你的职位就得合并到一个通用市场里去", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "你最好比10万人都强，并且强得足够明显", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "是有杠杆性的——四两压千斤的杠杆性", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P020", "quote": "要不惜一切代价降低低端就业人口的失业率", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P021", "quote": "你做的其实是一件残忍的事。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "但却会造成职位净减少、失业净增加的政策是对你有利的", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "又使得你的竞争对手猛烈的增加，直接造成你的压力增加和涨薪迟滞。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "高失业率对真正的大资本家是绝对喜讯", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P028", "quote": "却有了极大的谈判筹码逼迫你自愿接受低工资或者放弃涨薪诉求", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P030", "quote": "到底给了你什么确切的福利保障呢？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "但也同时消灭了大量本来可以存在的职位。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P034", "quote": "要么就会被转移到远处、别的国家，被以产品或者外包的形式封装起来", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P036", "quote": "你事实上的处境总体恶化了。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P039", "quote": "它实际上是一种政党政治机制催生出来的愚昧的政治正确", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P040", "quote": "因为“低端选择”不存在，被消灭了——至少没有合法的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P042", "quote": "“劳动力定价”根本就不该是劳动法该干涉的范围", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P043", "quote": "我很高兴深圳有这个勇气打破这愚昧的政治正确。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P044", "quote": "只是不是谁都有这个政治资本去面对这种误解的风险去做正确的事。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P045", "quote": "就已经是接近【地狱】，必须要考虑搬迁到别的市场中去了", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P048", "quote": "要维护最低工资门槛，似乎这可以“保住自己的福利”。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P050", "quote": "那意味着“你一被辞退，就会猪狗不如”。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P052", "quote": "因为这样的工作被你鼓吹的最低工资制消灭了。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P054", "quote": "最低工资只是雇主成本的一部分", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["劳动经济学", "公共政策", "劳动法与工资支付"],
   "issue_candidates": ["最低工资的就业效应", "失业对在职劳动者的竞争压力", "深圳修改员工工资支付条例", "劳动法应否干预劳动力定价", "欧美产业空心化的成因"],
   "text_function_candidates": ["评论", "论辩", "政策评论"],
   "object_candidates": ["深圳", "欧美", "川普", "知乎学生与“打工人”", "非法移民"],
   "working_keywords": ["最低工资", "在职劳动者", "失业率", "杠杆性", "劳动力定价", "政治正确", "通用市场", "福利底线"]
  },
  "notes": "本篇无图片节点。P043 在结构中是 heading 字段（lexical 统计 heading:1），内容仍是作者表态，已按正文纳入内容单元。文中“网传式”他人主张（知乎学生与“打工人”维护最低工资门槛）已标为 opponent_view，未归给作者。P007-P016、P052-P053 的数字均为作者假设性举例，记录中已标明非统计数据。文中 P002“经济学界早有定论”、P039 空心化归因属待外部核查项。updated_at（2026-01-22）晚于 published_at（2021-07-10），语料未提供修订说明，按当前版本 text 记录。"
 },
 "b1d5e392": {
  "analysis": {
   "question_context": "提问者问“天使数字真的可信吗？”（Q001），要求判定一类说法的可信度。作者不直接判定天使数字的真假，而把问题转为“可信的标准定在哪里、由谁定”：先否认存在一套科学式的通用可信标准，承认科学方法的典范地位但指出人无法只靠这一级别的判定生活；再以“对方是不是真的爱你”为例说明证据总是不足、现实层面事实的标准是软的、须由自己决定；最后用两个反问（标准定在此处会让多少其他事情因此变得可信、会让多少恶人跃跃欲试与爱你的人恐慌）给出权衡要求，并声明未否定什么、尺度只能自己掌握。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "先立判断：所谓“可信的标准”并不科学严谨；科学上判断可信度确有一套严谨方法、堪称很好的典范，但人不可能仅仅只靠这个级别的判定来生活。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "以“你的女友/男友是不是真的爱你”为例：把能列举的证据列全、按科学标准衡量仍是不足，最多只能确定到“伪装的可能性不大”；人总要在某个节点把依据还没足到科学知识程度的事情当作事实来规划生活。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P008"], "summary": "给出结论性表述：在现实层面上事实的标准是软的，你可以自己决定。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "提出真正的关键问题：不是依据是否充分到不可辩驳，而是把“可信”的标准定在这里会导致多少其他事情因此变得可信；并落到天使数字上追问是否接受同等证据级别的其他东西也都可信。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "另一个角度：公开宣布自己相信一件事及其逻辑与依据，等于在别人眼里标定“这个证据水平、逻辑水平就足以让你相信”，这会让心怀恶念的人跃跃欲试、让爱你的人产生恐慌，作者要求把这一点想好。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "自我限定与收束：这里并没有否定什么东西，只是说明如何掌握这个尺度；而尺度只能由你自己掌握。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“可信的标准”并不是什么科学严谨的东西。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者承认科学上判断一件事的可信度有一套严谨的体系方法，虽不能说完美无缺，但确实可以说是一个很好的典范。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称遗憾的是人不可能仅仅只靠这个级别的判定来生活。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“你的女友/男友是不是真的爱你”为例：把能列举的证据都列出并按科学标准衡量，会发现证据是不足的，最多只能确定到“我觉得是伪装的可能性不大”这一步。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人总要在某个节点决定把某种依据还没足到科学知识这个程度的事情当作事实来规划自己的生活。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称在现实层面上事实的标准是软的，你可以自己决定。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为关键不是一件事的依据是否充分到了不可辩驳的程度，而是如果把“可信”的标准定在这里，会导致多少其他的事情因此变得可信。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者对天使数字话题作条件式追问：如果“天使数字”这种证据强度的东西可以视为可信，那么你是否能接受同等证据级别的其他东西也都可信（原句为反问，作者未直接判定天使数字本身真假）。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称如果你宣布你相信一件事以及你相信的逻辑与依据，在别人眼里就等于这个证据水平、这个逻辑水平的东西就足以让你相信，这会让多少心怀恶念的人跃跃欲试、让多少爱你的人产生恐慌。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者要求读者“这个你要想好”，并声明这里并没有否定什么东西，只是客观告诉读者如何掌握这个尺度而已。", "evidence": ["E11", "E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称尺度只能由你自己掌握。", "evidence": ["E13"]}
   ],
   "argument_steps": ["先否定存在科学严谨的通用“可信的标准”（P001）", "承认科学判断可信度的方法虽不完美但是很好的典范（P002）", "指出人不可能只靠这一级别的判定生活（P003）", "以“对方是不是真的爱你”为例：按科学标准证据不足，最多只能到“伪装可能性不大”（P004-P006）", "提出人总要在某节点把依据未足科学程度的事当作事实来生活（P007）", "推出结论：现实层面事实的标准是软的、可自己决定（P008）", "给出真正的判据：把标准定在此处会导致多少其他事情因此可信（P009）", "落到天使数字：追问同等证据级别的其他东西是否也都可信（P010）", "补另一角度：公开信念等于向他人标定自己的证据与逻辑门槛，会引来恶念者、惊动爱你的人（P011-P012）", "自我限定：并未否定什么，只说如何掌握尺度（P013）", "收束：尺度只能自己掌握（P014）"],
   "concept_usage": [
    {"term": "可信的标准", "meaning": "作者称其并不是什么科学严谨的东西，在现实层面是软的、可由个人自行决定（P001、P008）。", "evidence": "P001", "ambiguity": "作者一面称其不科学严谨，一面称科学方法为很好的典范，两者的适用边界文中未展开。"},
    {"term": "科学（标准／知识）", "meaning": "判断一件事可信度的严谨体系方法与典范，作者称人不可能只靠这一级别的判定生活（P002、P003、P007）。", "evidence": "P002", "ambiguity": "“证据还没足到科学知识这个程度”中的门槛，文中未给出界定。"},
    {"term": "事实的标准是软的", "meaning": "作者对现实层面事实判定的描述：标准不硬、可以自己决定（P008）。", "evidence": "P008", "ambiguity": "作者未说明“软”的程度与是否有不可逾越的底线。"},
    {"term": "尺度", "meaning": "可信标准的宽严程度，作者称只能由个人自己掌握（P013、P014）。", "evidence": "P014", "ambiguity": "作者未给出掌握尺度的具体方法或判准。"},
    {"term": "天使数字", "meaning": "提问者引入的判定对象；作者只把它当作“这种证据强度”的例子作一致性追问，未判定其真假（P010）。", "evidence": "P010", "ambiguity": "作者在 P013 明言“并没有否定什么东西”，故本文对该对象的真假未表态。"}
   ],
   "examples_and_targets": [
    "“你的女友/男友是不是真的爱你”（P004-P006）——作者举的重要命题例子，用来说明科学标准下证据不足。",
    "“谁说不可能是装得很逼真而已？”（P006）——作者设想并代拟的反驳，属修辞性反问。",
    "“天使数字”（P010，源自 Q001）——提问者所问对象，被作者用作同等证据强度的追问案例。",
    "“心怀恶念的人”“爱你的人”（P011）——作者设想的受影响者，属修辞性论据，未给例证。"
   ],
   "conditions": [
    "P007“你总要在某个节点决定……”：以“某种依据还没足到科学知识这个程度”为前提条件。",
    "P009“如果你把‘可信’的标准定在这里”：作者的核心判据以标准位置可自选为条件。",
    "P010“如果‘天使数字’这种证据强度的东西可以视为可信”：条件句，作者只追问其一致性后果。",
    "P011“如果你宣布你相信一件事情和你相信的逻辑与依据”：条件句，谈的是公开信念在他人眼中形成的信号效应。",
    "P013 声明“这里并没有否定什么东西”：作者自我限定本文不作真假判定。",
    "P014“尺度只能由你自己掌握”：结论不含统一标准，交由个人掌握。"
   ],
   "rhetoric_and_tone": "说明兼劝告；通篇第二人称，连续反问（“重要不重要？”“会导致多少其他的事情因此变得可信？”“会让多少爱你的人产生恐慌？”），以“举个例子——”引入日常例证，用“遗憾的是”“最多最多”“这个你要想好”等口语化措辞调节语气；结构为先破通用标准、再举例、再给判据、末段自我限定并把尺度交回读者，语气克制而不作断言。",
   "unresolved_questions": [
    "提问者所问“天使数字”是否可信，作者未作真假判定（P013 明言并没有否定什么），只给出衡量尺度的方法，故对 Q001 的直接答案在正文中缺位。",
    "P013“并没有否定什么东西”与 P002 对科学方法“很好的典范”的评价之间关系如何，作者未展开。",
    "“天使数字”所主张的具体内容与证据类型语料未提供，作者所说的“这种证据强度”具体对应什么无法确定。",
    "P011 关于“心怀恶念的人跃跃欲试”“爱你的人产生恐慌”的后果判断属作者断言，文中无例证或依据，需外部核查。",
    "brief 止于举例一句，未覆盖 P005 之后的内容，仅作导航，未据以补写正文。",
    "updated_at（2025-10-25）晚于 published_at（2021-07-11），语料未提供修订说明，按当前版本 text 记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“可信的标准”并不是什么科学严谨的东西。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "科学上判断一件事的可信度自然是有一套严谨的体系方法", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "但遗憾的是，人不可能仅仅只靠这个级别的判定来生活。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你会发现这证据是不足的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "你最多最多也只能确定到“我觉得是伪装的可能性不大”这一步。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你总要在某个节点决定把某种依据还没足到科学知识这个程度的事情当作事实来规划你的生活。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "在现实层面上事实的标准是软的，你可以自己决定。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "如果你把“可信”的标准定在这里，会导致多少其他的事情因此变得可信？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "那么你是否能接受同等证据级别的其他东西也都可信？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "会让多少心怀恶念的人跃跃欲试，会让多少爱你的人产生恐慌？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这个你要想好。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "这里并没有否定什么东西，只是客观的告诉你如何掌握这个尺度而已。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "尺度只能由你自己掌握。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论与判断", "科学方法与日常决策", "心理与生活"],
   "issue_candidates": ["可信标准是否必须有科学依据", "证据不足时能否当作事实生活", "天使数字一类说法的可信性", "公开信念对他人判断的影响"],
   "text_function_candidates": ["答疑", "劝告", "概念辨析"],
   "object_candidates": ["天使数字（提问者所问对象）"],
   "working_keywords": ["可信的标准", "证据不足", "事实的标准是软的", "尺度", "天使数字", "科学标准"]
  },
  "notes": "本篇无图片节点。提问者所问为“天使数字真的可信吗”，作者未直接判定其真假，并在 P013 声明“并没有否定什么东西”，记录中未把否定态度归给作者；Q001 与 P010 中的“天使数字”均属提问者引入的话题。brief 未覆盖 P005 之后内容，仅作导航。P011 的后果断言无依据，已列入待外部核查。updated_at（2025-10-25）晚于 published_at（2021-07-11），语料未提供修订说明，按当前版本 text 记录。"
 },
 "2ee824b2": {
  "analysis": {
   "question_context": "提问者问为什么日餐在国际上的地位比中餐高（Q001）。作者不比较两种菜系的口味或技艺，而把问题归到消费心理与国家实力上：人势利而鸡贼、都想尝体面人/有钱人/稀奇人吃的东西，品牌营造的本质是“与君同饮庆功酒”，因此这基本上是国力问题、人均富裕程度问题，而不是味觉审美问题；末段以中国名义GDP压倒美国、远超日本、令欧盟大部分国家发抖的假设情形预测中餐高端品牌的诞生。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出人性前提：人类非常势利而且鸡贼，大家都想尝尝体面人/有钱人/稀奇人吃的是什么，并以拟言方式道出“ta们吃的东西一定跟ta们的成功有关系，俺们也尝尝这成功药”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "进一步贬抑：人类在吃上的境界没比原始部落高太多，恒定的与“吃鹿鞭可壮阳”的总体思想水平保持一致。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "给出对品牌营造的判断：各种大气的品牌营造，说穿了中心思想是在高唱“与君同饮庆功酒”这一本质。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "给出对提问的回答：所以基本上这是国力问题、人均富裕程度问题，而不是味觉审美问题。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "以条件性预测收尾：等中国名义GDP压倒美国、把日本远远甩在身后、让欧盟大部分国家瑟瑟发抖时，中餐自然会诞生“道家菜”“佛门菜”“礼菜”的品牌，高雅到欧洲人捂紧荷包不敢大声说话。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人类是非常势利而且鸡贼的，大家都想尝尝体面人/有钱人/稀奇人到底吃的是啥。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者以拟言方式转述一种普遍心态（未指明出处）：“ta们吃的东西一定跟ta们的成功有关系，俺们也尝尝这成功药”，即把成功者的饮食当作与成功相连之物来模仿。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称大体上人类在吃上没有比原始部落的境界高太多，恒定的与“吃鹿鞭可壮阳”的总体思想水平保持一致。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称各种大气的品牌营造，说穿了中心思想是在高唱“与君同饮庆功酒”这一本质。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断菜系的国际地位基本上是一个国力问题、人均富裕程度问题，而不是一个味觉审美问题。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测等中国的名义GDP压倒美国、把日本远远甩在身后、让欧盟大部分国家瑟瑟发抖的时候，中餐自然会诞生一些“道家菜”“佛门菜”“礼菜”的品牌，高雅到欧洲人捂紧荷包不敢大声说话。", "evidence": ["E6"]}
   ],
   "argument_steps": ["立人性前提：人势利而鸡贼，想尝体面人/有钱人/稀奇人吃的东西（P001）", "以拟言道出“成功药”心态：成功者吃的必与成功有关（P002）", "贬抑性类比：人类在吃上的境界与原始部落、“吃鹿鞭可壮阳”同一水平（P003）", "揭示品牌营造的中心思想是“与君同饮庆功酒”（P004）", "给出结论：这是国力与人均富裕程度问题，不是味觉审美问题（P005）", "以中国GDP压倒美日欧的条件句预测中餐高端品牌的诞生（P006）"],
   "concept_usage": [
    {"term": "势利而且鸡贼", "meaning": "作者对人的整体判断：想尝体面人/有钱人/稀奇人吃的东西（P001）。", "evidence": "P001", "ambiguity": "属无范围限定的整体性人性断言，作者未给出依据。"},
    {"term": "成功药", "meaning": "作者拟言中的比喻，指把成功者所吃之物当作与成功相连、值得一尝的东西（P002）。", "evidence": "P002", "ambiguity": "引号内为拟言（含“俺们”），不代表作者自述立场。"},
    {"term": "品牌营造", "meaning": "作者称其中心思想是在高唱“与君同饮庆功酒”（P004）。", "evidence": "P004", "ambiguity": "文中未举出任何具体品牌或菜系为例。"},
    {"term": "国力问题／人均富裕程度问题", "meaning": "作者对菜系国际地位的归因，与“味觉审美问题”相对立（P005）。", "evidence": "P005", "ambiguity": "作者未给出衡量国力、富裕程度与菜系地位关系的依据或数据。"},
    {"term": "道家菜／佛门菜／礼菜", "meaning": "作者预测中餐未来会诞生的一类高端品牌（P006）。", "evidence": "P006", "ambiguity": "三种名称在文中未作任何解释，所指内容与形成机制不明。"}
   ],
   "examples_and_targets": [
    "“吃鹿鞭可壮阳”（P003）——作者使用的类比，用以贬抑人类在饮食上的观念水平。",
    "“与君同饮庆功酒”（P004）——作者引用的熟语式表达，用作对品牌营造中心思想的概括。",
    "中国名义GDP压倒美国、把日本远远甩在身后、让欧盟大部分国家瑟瑟发抖（P006）——作者的假设性预测条件，非既成事实。",
    "“道家菜”“佛门菜”“礼菜”“欧洲人捂紧荷包”（P006）——作者的预测性设想与修辞材料。",
    "日餐与中餐的国际地位（Q001）——提问者提出的比较对象；正文仅在 P006 的预测句中一带而过地出现“日本”，未对日餐作具体分析。"
   ],
   "conditions": [
    "P001-P002 的人性判断是全文论证的起点，未加范围限定（“人类是非常势利而且鸡贼的”）。",
    "P005 的结论以前四段的人性判断与品牌本质为前提（“所以基本上……”）。",
    "P006 的预测明确以“等中国的名义GDP压倒美国，把日本远远甩在身后，让欧盟大部分国家瑟瑟发抖的时候”为条件，属未来条件句。",
    "全文未讨论菜品口味、食材与烹饪技艺等味觉层面，作者明言这不是味觉审美问题（P005）。"
   ],
   "rhetoric_and_tone": "调侃与讽刺口吻（“势利而且鸡贼”“俺们”“成功药”“瑟瑟发抖”“捂紧荷包不敢大声说话”），用引号内的第一人称拟言刻画消费心态，以原始部落和“吃鹿鞭可壮阳”作贬抑性类比，并在末段转入豪言式预测；结构为立人性前提→揭示品牌本质→一句话给出归因→以国力条件作预测收尾，全篇无数据与案例，属短评式论断。",
   "unresolved_questions": [
    "提问者所问的日餐与中餐地位比较，正文未作具体分析，作者只给出国力/富裕程度的归因框架；“日本”仅出现于 P006 的预测句，故对 Q001 的直接回答需读者自行套用该框架。",
    "P001、P003 关于人性与“原始部落境界”的判断为整体性断言，文中无依据或数据，需外部核查。",
    "P006 的预测为条件性设想，其中“压倒”“远远甩在身后”的判准与时点文中未给出。",
    "“道家菜”“佛门菜”“礼菜”三种品牌在文中未作任何说明，具体所指不明。",
    "brief 末句被截断（止于“各种大气的品牌营造，说穿了中心思想是”），仅作导航，未据以补写正文。",
    "updated_at（2026-06-12）晚于 published_at（2021-07-11），语料未提供修订说明，按当前版本 text 记录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人类是非常势利而且鸡贼的，大家都想尝尝体面人/有钱人/稀奇人到底吃的是啥。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“ta们吃的东西一定跟ta们的成功有关系，俺们也尝尝这成功药。”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "大体上人类在吃上没有比原始部落的境界高太多", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "说穿了中心思想是在高唱“与君同饮庆功酒”这一本质。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "所以基本上这是一个国力问题、人均富裕程度问题，而不是一个味觉审美问题。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "中餐自然会诞生一些“道家菜”“佛门菜”“礼菜”的品牌", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["饮食文化", "消费心理", "国家实力与文化地位"],
   "issue_candidates": ["日餐与中餐国际地位差异的成因", "饮食消费中的身份模仿", "国家实力与文化品牌的关系"],
   "text_function_candidates": ["答疑", "评论", "讽刺短评"],
   "object_candidates": ["中餐", "日餐（仅见于提问者字段）", "美国", "日本", "欧盟"],
   "working_keywords": ["成功药", "势利", "品牌营造", "国力", "人均富裕程度", "庆功酒", "道家菜"]
  },
  "notes": "本篇无图片节点。提问者所问“日餐为何地位高于中餐”在正文中未获具体分析，作者只给出国力/人均富裕程度的归因框架与未来预测，“日本”仅出现于 P006 预测句；记录中未把日餐相关的判断补写为作者主张。P002 引号内文字为作者拟言转述的普遍心态（含“俺们”），未指明出处，故按 author_reported + attribution=unknown 记录，未归为作者自述立场。brief 末句被截断，仅作导航。updated_at（2026-06-12）晚于 published_at（2021-07-11），语料未提供修订说明，按当前版本 text 记录。"
 },
 "8d1ecb37": {
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
        if a.get('content_units'): continue
        art=by_id[s['id']]; q=(next((x.strip() for x in (art.get('text') or '').splitlines() if x.strip()),'(正文为空)'))[:180]; p=s.get('paragraph_ids') or ['P001']
        a['question_context']='提问者问题：%s；本文初读记录作者正文线索。'%(art.get('question') or '未提供'); a['content_units']=[{'unit_id':'U001','paragraph_refs':p,'summary':'围绕“%s”的原文驱动初步概括，待独立复核。'%s.get('title',''),'role':'thesis'}]; a['main_claims']=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出：“%s”'%q,'evidence':['E001']}]; a['argument_steps']=['从开篇命题进入正文。','其余步骤待独立复核。']; a['concept_usage']=[]; a['examples_and_targets']=[]; a['conditions']=[]; a['rhetoric_and_tone']='初读未作完整修辞分类，待复核。'; a['unresolved_questions']=['论证、事实依据与概念边界需复核。']; a['evidence']=[{'key':'E001','paragraph_id':p[0],'quote':q,'relation':'supports'}]; item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item['status']='needs_reread'; item['image_checked']=False; item['notes']+=' 含图片节点，图片未经核验。'
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
