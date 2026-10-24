# -*- coding: utf-8 -*-
"""批次 r001-b0093 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0093.sessions.py            # 写 out/r001-b0093.out.jsonl
  python3 records/r001-b0093.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0093"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0093.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e1153efa": {
  "analysis": {
   "question_context": "提问者要求评价「如果自由不加以限制，一定会导致强者对弱者的剥削」这句话（Q001），该引述句属于提问者，提问者本人未表态。作者没有直接评判这句话，而是从“剥削”这一概念的定性主体入手，追问交易旁观者是否有权作出此类判断。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "把“剥削”界定为交易双方之外的第三方对交易的定性，并追问旁观者是否有权判断。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "作者表态：不承认这种权利的合法性。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "认为起作用的是基于实力的权力而非法理权利，并称这只是动机与强加意志的事实。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "从神学角度提出：既成的集体意志与力量本身即体现某种自然法背书的意愿。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "给出改写式表述：“剥削”只是“不符合旁观者价值观的交易”的缩写和转译。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“剥削”是由交易双方之外的第三方对交易作出的定性。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者留下的待答问题：交易旁观者是否有权利对交易是否合法、是否道德作出判断。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不同意旁观者拥有这种权利的合法性。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "使强大的旁观者得以阻止这些交易的，不是基于法理的权利，而是基于实力的权力。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此事谈不上合理不合理，只是不满的群体有足够动机把自己的集体意志强加于此。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "仅就神学角度而言，这样的集体意志与足够强大的力量本身即体现某种由自然法背书的意愿。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果禁止强大的旁观者将自己的价值观贯彻到对一切交易的监管上，就会发生不符合这些旁观者价值观的交易。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“剥削”只是“不符合旁观者价值观的交易”的缩写和转译。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "P001—P003 先作界定：剥削是交易双方之外的第三方对交易的定性；再以两个连续反问追问旁观者的判断权。",
    "P004 表态：不承认这种权利的合法性。",
    "P005—P006 给出替代解释：起作用的是基于实力的权力，而非法理权利；并称这只是动机与强加意志的事实，谈不上合理不合理。",
    "P007 让步式补充：若从神学角度说，既成的集体意志与力量本身即体现自然法背书的意愿。",
    "P008—P011 重新表述命题：禁止旁观者贯彻其价值观就会产生不符合其价值观的交易，故“剥削”只是后者的缩写和转译；并断言“这是显然成立的”。"
   ],
   "concept_usage": [
    {"term": "剥削", "meaning": "本文中不被当作客观经济事实，而被改写为“不符合旁观者价值观的交易”的缩写与转译。", "evidence": "P010", "ambiguity": "先定义为第三方对交易的定性，后给出改写式定义，两处用法是否同一未说明。"},
    {"term": "旁观者（第三方）", "meaning": "并非买方、也不是卖方、也不承担交易被阻止所造成的买卖双方机会成本，却试图对交易作合法性与道德判断的一方。", "evidence": "P003", "ambiguity": "旁观者的范围与身份未说明。"},
    {"term": "power based on capability", "meaning": "与“基于法理的权利”相对的、基于实力的权力。", "evidence": "P005", "ambiguity": "作者仅以括注给出，未展开定义。"},
    {"term": "自然法", "meaning": "在神学视角下为既成的集体意志与力量作背书的概念。", "evidence": "P007", "ambiguity": "只一句话带过，未说明其内容与来源。"}
   ],
   "examples_and_targets": [
    "「如果自由不加以限制，一定会导致强者对弱者的剥削」——提问者引述、要求评价的命题，是本文的讨论对象，非作者主张。",
    "买方、卖方、交易旁观者——作者论证中的角色设定，非具体人物或事件。"
   ],
   "conditions": [
    "“从神学的角度来说”（该判断被限定在神学视角内）。",
    "“如果禁止强大的旁观者将自己的价值观贯彻到对一切交易的监管上”（改写后的命题以该条件为前提）。",
    "“即使ta并非买方、也不是卖方、也不承担潜在交易被阻止所造成的买卖双方的机会成本”（对旁观者身份的限定）。"
   ],
   "rhetoric_and_tone": "短段自问自答式推进，多处反问（“是否有权利作出这种判断？”“却有某种不可置疑的权利……”）；语气冷静、坦白（“坦白说”），以定义改写收束，末句“这是显然成立的”作断言式结尾。",
   "unresolved_questions": [
    "提问者所引“自由不加以限制→剥削”的命题与作者讨论的“旁观者定性权”是否同一问题，作者未说明。",
    "作者所说“神学的角度”具体指何种神学或自然法学说，本文未说明。",
    "“强大的旁观者”指哪些主体（国家、舆论、国际组织等），本文未说明。",
    "P011“这是显然成立的”指代范围是否仅为P010的改写命题，文本未明说。",
    "图片未核验的事项不适用（本篇无图片节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "它是由交易双方之外的第三方对交易作出的定性", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "交易的旁观者，是否有权利作出这种判断？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "却有某种不可置疑的权利来对交易是否合法、是否道德作出判断？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "坦白说，我不同意这种权利的合法性。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "并不是某种基于法理的权利，而是一种基于实力的权力", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "谈不上什么合理不合理", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这种现状本身就体现了某种由自然法背书的意愿", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P009", "quote": "如果禁止强大的旁观者将自己的价值观贯彻到对一切交易的监管上，当然就会发生不符合这旁观者们价值观的交易。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "“剥削”只是“不符合旁观者价值观的交易”的缩写和转译而已。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "伦理学", "交易与监管"],
   "issue_candidates": ["剥削的定义", "旁观者对交易的判断权", "权力与权利之别", "监管的正当性"],
   "text_function_candidates": ["概念辨析", "质疑", "论辩"],
   "object_candidates": ["交易双方", "交易旁观者"],
   "working_keywords": ["剥削", "旁观者", "power based on capability", "自然法", "交易的定性"]
  },
  "notes": "提问者引述句的立场未归入作者主张；作者未直接评判该引述句真假，而是改写“剥削”的定义。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "e31cc6dc": {
  "analysis": {
   "question_context": "提问者问“普通的男生怎样才能追到漂亮的女生?”（Q001），属提问者的求助式提问，其中“普通人／美女”的区分是提问者的预设。作者不提供追求技巧，而先否定“普通人”这一前提，把问题诊断为观察者丧失兴趣能力、观察分辨率过低。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以三个反问追问“普通人”的所指与标准，拆解提问前提。", "role": "other"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "否认“普通人”存在，把“我是普通人”重述为自己对自己都没兴趣。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "归因：观察者丧失兴趣能力，对他人与自身皆无兴趣，遂把自己划入“大众”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "以视力为喻：看不见便以为一切皆黑，只有极强之光与艳光四射者才算可见。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "反推：视力良好者眼中无人“普通”，“普通”只是数学空间中的抽象理想。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019"], "summary": "结论：真正的问题是视力太差、分辨率太低。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "收束：美女没有动力为看不见的人跳舞，人都去和能看见ta们的人一起。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上根本不存在“普通人”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“我是普通人”的本质是自己对自己也没有了解与看一眼的兴趣。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该问题的根源不在于有没有特殊的点，而在于作为观察者的自己丧失了兴趣的能力。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因丧失兴趣能力而对他人和自己都无兴趣，遂依“都无法引起我的兴趣”这一共同点把自己划入大众，形成大家都是普通人的认知。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是因为自己看不见，所以认定自己和其他看不见的一切一样都是黑色的。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在视力良好的观察者看来，人类没有任何一个谈得上“普通”。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“普通”只是一个抽象的、只在数学空间中存在的理想。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "若一个人所有参数都刚好是全人类的最高频值，ta将成为最特殊的人；作者反问这样“世界上最普通的人”还“普通”吗。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题不是“你普通”，而是“你视力太差，近乎于盲”，观察的分辨率低。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不是色彩斑斓的人少，而是视力好到能看到色彩斑斓的人少。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人都去和能看见ta们的人一起了。", "evidence": ["E11"]}
   ],
   "argument_steps": [
    "P001—P003 以三个反问拆解提问前提：谁是普通人、标准是什么。",
    "P004—P005 否定“普通人”存在，并把“我是普通人”重述为自己对自己都没有兴趣。",
    "P006—P009 归因：观察者丧失了兴趣的能力，遂对他人与自己都无兴趣，并据此把自己划入“大众”。",
    "P010—P012 类比：看不见便以为一切皆黑，只有探照灯、太阳与艳光四射者才算可见。",
    "P013—P016 反推：视力良好者眼中无人“普通”，“普通”只是数学空间中的抽象理想。",
    "P017—P019 结论：真正的问题是视力太差、分辨率太低。",
    "P020—P022 收束：美女没有动力为看不见的人跳舞，人都去和能看见ta们的人一起。"
   ],
   "concept_usage": [
    {"term": "普通人", "meaning": "本文中被否认是实存类别，而是观察者丧失兴趣能力后形成的认知与抽象理想。", "evidence": "P014", "ambiguity": "与提问者所用“普通男生”的日常含义关系未说明。"},
    {"term": "兴趣的能力", "meaning": "能对他人与自己发生真实兴趣、进而分辨差异的观察能力。", "evidence": "P006", "ambiguity": "如何丧失、能否恢复，本文未说明。"},
    {"term": "视力／分辨率", "meaning": "比喻观察他人差异的敏锐程度。", "evidence": "P017", "ambiguity": "比喻与字面视力在同一段中混用。"},
    {"term": "美女", "meaning": "沿用提问者的词，指“艳光四射”的人。", "evidence": "P012", "ambiguity": "作者未重新定义，只在P020再次使用。"}
   ],
   "examples_and_targets": [
    "提问者所说的“普通的男生”“漂亮的女生”——作者的质疑与重述对象，非作者主张。",
    "探照灯和太阳——比喻：只有极强刺激才略有微光可见。",
    "核弹级的能量释放——夸张比喻：需要极高刺激才能让“你”看见、知道、触动。",
    "“爱你太难。”——对提问者的短句回应，语气近似感叹。"
   ],
   "conditions": [
    "“如果我是别人，我对自己也没多了解一分钟、多看一眼的兴趣”（以设身处地的假设界定“普通人”的本质）。",
    "“如果一个人所有的参数都刚好是全人类的最高频值”（反证所用的假设条件）。",
    "“在视力良好的观察者看来”（结论所依赖的观察条件）。",
    "“只有艳光四射的，才算‘不普通’了”（描述视力差者的判定阈值）。"
   ],
   "rhetoric_and_tone": "以三个短反问开篇，整体为训诫式；比喻密集（黑、视力、探照灯、核弹）；多用第二人称“你”直接对提问者说话；“爱你太难。”独立成段，语气由训诫转为感叹，末段复归平静陈述。",
   "unresolved_questions": [
    "作者把“追不到”的问题整体改写为观察者能力问题，但未回答“怎样才能追到”，二者关系未说明。",
    "“兴趣的能力”如何丧失、能否恢复，本文未说明。",
    "“视力太差”的成因与改善办法，本文未说明。",
    "P019“爱你太难”的主语与对象（谁爱谁）未明说。",
    "本篇无图片节点，图片未核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "世界上根本不存在“普通人”，只有自己想起自己都觉得没兴趣的人。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "“如果我是别人，我对自己也没多了解一分钟、多看一眼的兴趣”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "而在于作为观察者的自己丧失了兴趣的能力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "形成了大家都是普通人的认知", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "是因为自己看不见，所以认定自己和其他看不见的一切一样都是黑色的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "根本没有任何一个谈得上“普通”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "“普通”只是一个抽象的、只在数学空间中存在的理想。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "ta将奇妙的成为一个最特殊的人", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "而是你视力太差，近乎于盲。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P021", "quote": "不是色彩斑斓的人少，而是视力好到能看到色彩斑斓的人少。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "人都去和能看见ta们的人一起了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学", "人际关系", "自我认知"],
   "issue_candidates": ["“普通人”的定义", "兴趣能力与观察分辨率", "择偶与吸引力"],
   "text_function_candidates": ["答疑", "驳正前提", "训诫"],
   "object_candidates": ["提问者（普通男生）", "美女", "观察者"],
   "working_keywords": ["普通人", "兴趣的能力", "视力", "分辨率", "爱你太难"]
  },
  "notes": "提问者的“普通男生／漂亮女生”框架未算作作者主张，作者否定该前提。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "de6cd452": {
  "analysis": {
   "question_context": "提问者问“如何打造自己的人设？”（Q001），属提问者的求助式提问，其中把“人设”当作可自行打造之物的预设归提问者。作者不提供操作步骤，而是重新界定人设的要害：不在自身有多引人喜欢和关注，而在关注它的人因“关注”这一行为获得何种评价。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "区分两层：人设要害不在自身吸引力，而在关注者因关注行为获得的评价；多数人只看第一层，决定“成功”的是第二层。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "举例：受欺负的弱者形象提供了让人展现同情心或奋斗心的机会，因而比炫富人设更成功。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "类推到写作、拍摄：不要只想博眼球，还要想喜欢你的人因关注你而获得什么评价。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "以连续反问展开第二层：旁人会因此觉得关注者贪慕虚荣还是不被虚荣所骗、愚蠢还是聪明、喜欢还是不喜欢。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "条件式断言：看得懂这一点就自然出类拔萃。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P013"], "summary": "转向读者一侧：只面向第一层而创作的东西不值得花太多时间。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P014"], "summary": "收束：要打造的不是你自己的人设，而是认同你的人的人设。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人设的要害不在它本身有多引人喜欢和关注，而在关注它的人会因为“关注”这一行为获得何种评价。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多数人只想到第一层，但决定人设是否“成功”的是第二层。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "呈现受欺负的弱者形象，实际提供了让人通过支持ta展现同情心或奋斗心的机会，故比炫富人设更成功。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "写作、拍摄同理：不要只想博人眼球，还要想喜欢你的人因喜欢你、关注你这个行为获得什么评价。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问要求读者核对：旁人会因关注者常看你的东西而觉得ta贪慕虚荣、愚蠢或不喜欢ta，还是相反。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果真看得懂这一点，你自然出类拔萃。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作为读者、观众也应反思：只面向第一层而创作的东西不值得花太多时间。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要打造的不是你自己的人设，而是认同你的人的人设。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "P001—P002 先作区分：人设要害不在自身吸引力，而在关注者因关注行为所获评价。",
    "P003 指出多数人只想到第一层，决定成败的是第二层。",
    "P004—P005 举弱者人设为例：它提供让他人展现同情心或奋斗心的机会，故比炫富人设成功。",
    "P006—P007 类推到写东西、拍东西：要为喜欢你的人所获评价考虑。",
    "P008—P011 用连续反问展开第二层的两个维度（旁人如何评价关注者；关注者本身聪明或愚蠢、带来爱或噩运）。",
    "P012 条件式断言：看懂则出类拔萃。",
    "P013 转向读者、观众的行动建议。",
    "P014 结论：打造的是认同你的人的人设。"
   ],
   "concept_usage": [
    {"term": "人设", "meaning": "本文不指自我形象本身，而指关注者因“关注”这一行为所获评价的载体。", "evidence": "P002", "ambiguity": "未给定义，两层之分由作者设定。"},
    {"term": "第一层／第二层", "meaning": "第一层指人设本身是否引人喜欢和关注；第二层指关注它的人因关注行为获得的评价。", "evidence": "P003", "ambiguity": "“层”的划分标准与判定方法未说明。"},
    {"term": "弱者形象", "meaning": "呈现为很受欺负的形象，其功能是提供让他人通过支持ta展现同情心或奋斗心的机会。", "evidence": "P004", "ambiguity": "作者举为例子，未说明适用范围。"},
    {"term": "认同你的人的人设", "meaning": "收束句中的落点：要打造的不是自己的形象，而是认同你的人群的形象。", "evidence": "P014", "ambiguity": "仅一句结论，未展开操作方法。"}
   ],
   "examples_and_targets": [
    "“很受欺负的弱者形象”与“整天炫耀自己很有钱、富贵逼人的人设”——作者用于对比的两种人设例子。",
    "写东西、拍东西——作者类推的创作场景。",
    "读者、观众——作者在P013转向的劝告对象。",
    "提问者问题“如何打造自己的人设？”——属提问者，非作者主张。"
   ],
   "conditions": [
    "“如果你真的看得懂这一点”（P012 条件式表述，未说明看懂的标准）。",
    "第二层评价的成立依赖“旁人”的观感，作者未给出该判断的适用人群或场景限定（P008—P011）。",
    "适用场景被限定在写作、拍摄等面向他人关注的形象与创作经营（P006）。"
   ],
   "rhetoric_and_tone": "指点式教学口吻，第二人称“你”直接告诫（“不要光想着博人眼球”）；P008—P011 连用四组反问逼读者自检；以“简单来说”收束为一句口诀式结论；语气笃定但未给数据或例证来源。",
   "unresolved_questions": [
    "“第二层”评价的具体判断标准与形成机制，本文未说明。",
    "P005 断言弱者人设“反而会比”炫富人设成功，未给证据或限定条件。",
    "P008—P011 的反问均未给出答案，也未说明“旁人”指哪些人。",
    "P010—P011 中“自己愚蠢／聪明”“带来噩运／带来爱”的对应关系未论证，句式为反问，是否为作者断言存在歧义。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "要害在于关注它的人会因为关注这一行为而获得何种评价", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "决定是否“成功”的，是第二层", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "ta实际上是提供了一种机会，一种通过支持ta而展现同情心或者奋斗心的机会", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "于是ta反而会比整天炫耀自己很有钱、富贵逼人的人设成功。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "还要想着那些喜欢你的人，因为喜欢你、关注你这个行为，获得的是什么样的评价。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "旁人是会因为看到ta们常看你的东西而觉得ta们显然贪慕虚荣", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "如果你真的看得懂这一点，你自然出类拔萃。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "只面向第一层而创作的东西，是不值得你太多时间的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "你要打造的不是你自己的人设，而是认同你的人的人设。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["传播与媒介", "自我呈现与形象经营", "人际吸引"],
   "issue_candidates": ["人设的层次", "关注者所获社会评价", "受众与粉丝心理", "创作动机"],
   "text_function_candidates": ["答疑", "经验总结", "说理劝导"],
   "object_candidates": ["人设经营者", "关注者／受众", "读者与观众"],
   "working_keywords": ["人设", "第一层", "第二层", "关注", "评价", "弱者形象"]
  },
  "notes": "提问者的“如何打造人设”预设未算作作者主张；作者以两层区分与反问作答，未给操作步骤。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "366ab128": {
  "analysis": {
   "question_context": "提问者问“五千年了，除了人类，看到那些生物在进化？”（Q001）。“五千年”的时间尺度与“看到……在进化”的观察期待属提问者的说法。作者不直接回应观察问题，而是列举最近几千年演化最快的几类生物，并反驳“人类是演化最快物种”的印象，转而主张人类恐怕是演化最慢的物种之一。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出最近几千年有几类生物进化最快，第一类是细菌和病毒。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "理由：人类交通手段与环境改造能力的进步，推动新类型细菌和病毒产生。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "第二类：畜养禽畜、农作物和宠物；人类直接参与新品种繁育筛选，是额外的演化动力。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "基因工程几乎改变这些品类的基本演化机制，把演化速度提升数个数量级。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "第三类：为科学目的产生的研究用动物，其“演化速度”相对自然物种近乎“无限快”。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "小结：上述类别的演化速度远非人类自身演化速度所能及。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P010"], "summary": "转折与反驳：人类几乎谈不上明显演化，身高寿命的进步并非基因层面而是发育变化；以四千年前古人为假想例证。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P011", "P012"], "summary": "医学与社会进步削弱了人类所受的筛选力度，而同样的演化动力对动植物反因人类活动被加强。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P013"], "summary": "例证：千万年尺度才能造成的森林衰退或草原沙化，可能因人类不到千年活动突然发生。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P014"], "summary": "结论：人类恐怕不但不是演化最快，反而是演化最慢的物种之一。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P015", "P016"], "summary": "限定与反问：大概只有被刻意保护的活化石物种更慢，人类会用克隆等保证其演化速度为0；若不为零岂不是失败。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最近几千年有几类生物演化最快，其中包括细菌和病毒。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类交通手段与改造环境能力的进步，对新类型细菌和病毒的产生是很强的推动力。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类直接参与畜养禽畜、农作物和宠物的新品种繁育筛选，构成额外的演化动力。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基因工程几乎改变了这几个品类生物的基本演化机制，把演化速度提升了数个数量级，可在一代人有生之年出现肉眼可见的特性变化。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "直接被用于基因工程实验的物种，其“演化速度”相对于自然演化的物种几乎可以说是“无限快”的。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述几类生物的演化速度远非人类自身的演化速度所能及。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人类自己几乎谈不上明显的演化；身高、寿命之类的进步并非基因层面，而是生存条件改变造成的发育变化。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若给一名四千年前的古人现代化的生活条件和医疗条件，ta会成长成与现代人区别极其细微的人，几乎无有效证据可识别其为“古人”。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "医学进步削弱了大规模传染病对基因突变的筛选力度，社会进步削弱了环境变迁、自然灾变对人类的筛选力度。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这两种演化动力对其它动植物并未被削弱，反而因人类的活动被加强。", "evidence": ["E11", "E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "人类——尤其进入文明史的人类——恐怕不但不能算演化速度最快的物种代表，恐怕还是演化最慢的物种之一。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "大概只有将来人类刻意成功保护下来的“活化石物种”（如熊猫、扬子鳄）会比人类演化更慢；人类会排除其演化压力，甚至用克隆等技术保证其演化速度为0。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以反问收尾：若不为零，岂不是就失败了吗。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "P001—P008 列举三类演化最快者（细菌和病毒；畜养禽畜、农作物和宠物；研究用动物），并给出人类活动构成额外演化动力的理由，直至基因工程把速度提升数个数量级。",
    "P009 归纳：这几类的演化速度远非人类自身所能及。",
    "P010 转折反驳：人类几乎谈不上明显演化，身高寿命之变属发育变化而非基因变化；以四千年前古人的假想为例。",
    "P011—P012 补充机制：医学与社会进步削弱人类所受筛选，而同类动力对动植物反被人类活动加强。",
    "P013 举例：千万年尺度的气候变化后果可能因人类不到千年活动突然发生。",
    "P014 结论：人类恐怕是演化最慢的物种之一。",
    "P015—P016 边界与反问：被刻意保护、演化速度被保持为0的活化石物种可能更慢。"
   ],
   "concept_usage": [
    {"term": "演化（进化）", "meaning": "本文指基因层面的物种变化；作者据此把身高、寿命等变化归为发育变化而非演化。", "evidence": "P010", "ambiguity": "标题与提问用“进化”，正文用“演化”，是否同义未说明。"},
    {"term": "演化速度", "meaning": "相对尺度上的变化快慢，用于基因工程物种时可被形容为“无限快”。", "evidence": "P008", "ambiguity": "未给出量化标准或测量方式。"},
    {"term": "筛选力度", "meaning": "大规模传染病对基因突变的筛选，以及环境变迁、自然灾变对物种的筛选。", "evidence": "P011", "ambiguity": "未说明筛选机制的具体内容。"},
    {"term": "活化石物种", "meaning": "人类刻意成功保护下来、被排除一切演化压力（以熊猫、扬子鳄为例）的物种。", "evidence": "P015", "ambiguity": "以例举方式出现，未给定义。"},
    {"term": "发育变化", "meaning": "由生存条件大幅改变造成、非基因层面的个体发育差异。", "evidence": "P010", "ambiguity": "与演化的界线由作者划定，未展开论证。"}
   ],
   "examples_and_targets": [
    "细菌和病毒、畜养禽畜、农作物、宠物、研究用动物——作者列举的类别，属作者证据性分类。",
    "基因工程、克隆技术——作者所说的新手段。",
    "四千年前的古人——作者设定的假想例证。",
    "熊猫、扬子鳄——作者举出的活化石物种例子。",
    "森林衰退、草原沙化——作者举出的环境变化例证。",
    "提问者问句“五千年了，除了人类，看到那些生物在进化？”——属提问者，非作者主张。"
   ],
   "conditions": [
    "“最近几千年”（P001 时间范围限定）。",
    "“如果给予ta现代化的生活条件和医疗条件”（P010 假设条件）。",
    "“直接用于基因工程实验的物种”（P008 对象范围限定）。",
    "“大概只有将来人类刻意成功保护下来的‘活化石物种’”（P015 预测加限定）。",
    "“若不为零”（P016 反问所设条件）。"
   ],
   "rhetoric_and_tone": "科普式列举（1）2）3））与议论文推进结合；以“显然”“事实上”“所以”作断定，用“恐怕”“大概”“几乎可以说”保留不确定；结尾由陈述转为反问（“岂不是就失败了吗？”），带轻微调侃。",
   "unresolved_questions": [
    "提问者问“五千年”尺度，作者答“最近几千年”，两个时间范围是否对应，本文未说明。",
    "P006“提升了好几个数量级”无数据来源，待外部核查。",
    "P010 四千年前古人的假想属推断，作者称“几乎没有任何有效的证据”，但未给出研究依据。",
    "P015 说人类“会”用克隆保证活化石物种演化速度为0，是既有做法还是预测，本文未说明。",
    "P016 反问中“若不为零”所指为何、以何为失败标准，存在歧义。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有几类生物是进化最快的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "这对新类型细菌和病毒的产生是一个很强的推动力", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "人类自己直接参与了新品种的繁育和筛选。这也是一项额外的演化动力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "把它们的演化速度提升了好几个数量级", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "几乎可以说是“无限快”的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "远非人类自身的演化速度所能及", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "事实上，人类自己几乎谈不上什么明显的演化。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "并非基因层面的，而是生存条件的大幅改变所造成的一种发育变化", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "ta会成长成一个与现代人区别极其细微的人", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "削弱了大规模传染病对基因突变的筛选力度", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "倒是因为人类的活动反而被加强了", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "可能因为人类不到一千年的活动就突然发生", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "恐怕还是演化最慢的物种之一", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "保证它们的演化速度保持为0", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "若不为零，岂不是就失败了吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["演化生物学", "科普", "人类活动与环境"],
   "issue_candidates": ["人类是否为进化最快的物种", "人类活动对其它物种演化的推动", "基因工程与演化速度", "演化与发育之别"],
   "text_function_candidates": ["答疑", "科普解释", "反驳常识印象"],
   "object_candidates": ["细菌和病毒", "畜养禽畜与农作物", "宠物", "研究用动物", "人类", "熊猫", "扬子鳄", "四千年前的古人"],
   "working_keywords": ["演化速度", "进化", "细菌和病毒", "基因工程", "活化石物种", "筛选力度", "发育变化"]
  },
  "notes": "提问者的问句属提问者；作者以类别列举与反驳作答。标题与提问用“进化”，正文用“演化”，未说明是否同义。P006 数量级说法与P015 克隆做法待外部核查。本篇无图片节点。"
 },
 "90f589a9": {
  "analysis": {
   "question_context": "提问者问“什么样的老年会很凄惨?”（Q001）。“老年”“凄惨”两个限定词均来自提问者，正文未再出现这两个词。作者不解释原因、不给标准，而以四个并列短语加一句英文列举其答案，落点全在“爱”的失败与孤独死去。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "第一类：以错误的理解定义爱、花真实力气“爱”人却施加实际伤害、最后未获原谅的人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "第二类：明知什么是爱却因软弱和贪婪知而不行，自知不爱人也无人爱自己的人。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "第三类：身边或有许多欠债者、受威胁者围绕，却无人真爱、无人真希望ta活下去的人。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "第四类：没有爱过、因而也无法理解爱的人。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "以英文短句收束：those who die alone。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "晚年凄惨者之一：以错误的理解定义爱、花着真实力气“爱”别人、施加实际伤害而最后没有获得原谅的人。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "晚年凄惨者之一：明知道什么是爱，却因软弱和贪婪终于知而不行，在内心知道自己并不爱人、也知道无人爱自己的人。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "晚年凄惨者之一：即使有欠自己债或在自己威胁之下的人围绕，也没有谁真正爱、没有谁真的希望ta活下去的人。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "晚年凄惨者之一：那些没有爱过，于是也无法理解爱的人。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以英文短句收束的一类：those who die alone（孤独死去的人）。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "P001—P004 以四个并列短语列举晚年凄惨者的类型，分别落在误解爱并造成伤害而未获原谅、知爱而不行、被欠债或受威胁者围绕却无真爱、未曾爱过而无法理解爱。",
    "P005 以英文单句 those who die alone 收束，把落点归为孤独死去。"
   ],
   "concept_usage": [
    {"term": "爱", "meaning": "本文用作衡量晚年处境的尺度，涉及理解爱、真的爱人、被爱、被希望活下去等不同层次。", "evidence": "P002", "ambiguity": "未给定义；四类中“爱的失败”性质不同（认知错误／知而不行／无人真爱／未曾爱过）。"},
    {"term": "知而不行", "meaning": "明知什么是爱，却因软弱和贪婪没有去做。", "evidence": "P002", "ambiguity": "未说明所指行为范围。"},
    {"term": "凄惨", "meaning": "标题与提问用词，正文未出现；正文以四类人的描述间接作答。", "evidence": "P005", "ambiguity": "正文未使用“凄惨”“老年”二词，对应关系需据提问推断。"},
    {"term": "die alone", "meaning": "英文收束句，指孤独死去者。", "evidence": "P005", "ambiguity": "是第五类还是前四类的总结，未说明。"}
   ],
   "examples_and_targets": [
    "四类人的形象描写——作者给出的类型描述，非具体人物或事件。",
    "“欠着自己的债或者在自己威胁之下的人”——作者描述的关系情境。",
    "提问者问题“什么样的老年会很凄惨?”——属提问者，非作者主张。"
   ],
   "conditions": [
    "“也许有着种种欠着自己的债或者在自己威胁之下的人围绕”（P003 以“也许”给出的情形限定）。",
    "“而最后没有获得原谅的人”（P001 以“最后”限定的结果条件）。",
    "“在内心知道自己并不爱人，也知道无人爱自己的人”（P002 对自我认知状态的限定）。",
    "正文未给出时间、地域、人数或年龄阶段的适用范围限定；是否专指“老年”需据提问推断。"
   ],
   "rhetoric_and_tone": "全篇无完整主谓判断句，四个名词性短语以分号排比成清单式判词，末尾改用英文短句收束；语气冷峻、近乎断言，不作解释、不给例证，亦无劝诫或安慰。",
   "unresolved_questions": [
    "正文未出现“老年”“凄惨”字样，四类描写是否专指老年阶段，本文未说明。",
    "四类之间是否互斥、可否重叠，本文未说明。",
    "P005 英文句与前四类的关系（第五类或总括）存在歧义。",
    "“爱”未定义，四类的判定标准并不一致。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "以错误的理解定义着爱，花着真实的力气“爱”着别人，施加着实际的伤害", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "明知道什么是爱，却因着软弱和贪婪，终于知而不行", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "没有谁真正的爱、没有谁真的希望ta活下去的人", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "那些没有爱过，于是也无法理解爱的人；", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "those who die alone.", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理与情感", "人生经验", "通俗心理"],
   "issue_candidates": ["晚年处境的判定", "爱的能力与关系失败", "孤独死", "知行不一"],
   "text_function_candidates": ["答疑", "经验总结与判断"],
   "object_candidates": ["四类被描述者（泛称）", "欠债者或受威胁者（情境角色）"],
   "working_keywords": ["爱", "理解爱", "知而不行", "原谅", "die alone"]
  },
  "notes": "正文为并列短语清单，无展开论证与例证；“老年”仅见于提问，属提问者限定。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "8783122f": {
  "analysis": {
   "question_context": "提问者问“古代谋士为什么有上中下三策，而君主却不选上策?”（Q001），“君主不选上策”这一判断属提问者。作者先声明这不只是“古代君主”的问题（P001），再追问上中下按何排列（P002），给出“上策”的一般机制（扩大时间资源项）与其对信心的要求，继而以中日君臣之道对比说明中国之臣效命的是天道而非君主个人，最后把三策读作群臣理想与试炼的表达，并把该逻辑延伸至现代组织与未来情境。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "指出这不是古代君主独有的问题，并追问上中下三策的排列依据。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "给出“上策”的一般机制：扩大对策需要的时间资源项，使谋略指向底层、根本、必然的要素。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "对比三年治本与三天应付：前者路线池更宽，后者受物理实在约束只能在小范围内选择。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "指出上策的致命问题是太需要信心：治本要扛心理压力、组织张力与自我怀疑；无信念与道德勇气则选不下手。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "在儒家、礼教视野下把道德释为对“天地正气”的信仰，列出所要相信的内容，并称需“虽九死其犹未悔”的信仰才能挺过最黑暗时期。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "反证：信心不足与犹豫徘徊会把可奏效的策略执行成无效，自我实现“果然无效”的预言。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013"], "summary": "提出：臣下建言分上中下三策本身是对君主一种不自觉的试探。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016"], "summary": "对比日本武士道（家臣放弃评价权，本质是“侍道”）与中国“君君，臣臣”的君臣之道。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018"], "summary": "解释“君君，臣臣”：君主达成君主资格，臣子才尽臣子道义；臣对君有基于理想的选择。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "以臣的口吻自述地位：不比你差、不需你赏赐、世代传承；接受三项天意昭示，故甘愿承受随之而来的辛劳、痛苦与危险。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "结论：臣非效命于君主个人或契约誓言，而是效命于自己信服的天道；若判断君主不够格则挂冠而去。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "天命际遇与社会理想原则均与“实力”无必然关联；弱君不妨碍贡献，秩序未崩坏时人臣不会自认理应取而代之。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P033", "P034"], "summary": "由此精英的能力与资源不必耗于零和博弈，可投入公共产品与服务以促进共同理想。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039"], "summary": "三策的真相：上策里有群臣的理想；君主选上策的道德勇气证明其资格；行上策未必幸存，但君既君臣必臣。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046"], "summary": "臣等效死力的排比宣言（鞠躬精粹、茹毛饮雪、抛头颅洒热血、虽九死其犹未悔、死得其所）。", "role": "other"},
    {"unit_id": "U016", "paragraph_refs": ["P047", "P048", "P049"], "summary": "中策是可接受的妥协、选中策证明被效忠资格仍有效；下策完全脱离理想原则、越理非法有悖天道。", "role": "claim"},
    {"unit_id": "U017", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "下策的伦理二义性：既是作为朋友的尽情之举，又是对君主的公平试炼；无知之义不足以为君；选下策则君不君、臣可不臣。", "role": "reason"},
    {"unit_id": "U018", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066"], "summary": "回到现实：该选择栖身之地的逻辑今天仍在运行，仍是最可行的人生策略之一；要记住君君臣臣；并断言其未来普适性。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“上策”的一般机制是扩大对策需要的时间资源项，使谋略指向底层的、根本的、必然的要素，而非表层、即刻、机会性的矛盾。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "允许用三年从根上解决而非三天应付表象危机，前者带来更多策略工具选择空间与宽广得多的路线池。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若限定三天内出效果，各种物理的、实在的约束决定只能在极小范围内选择，而这些选择在综合效应与长远利益上无法与长期策略相比。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上策存在的致命问题在于它太需要信心。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "长期治本之策意味着眼下不愉快的“缓释”过程，要扛心理压力、组织关系的张力与自我怀疑的折磨。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有坚定的信念与足够的道德勇气，上策选不下手。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "道德不是虚无缥缈的事物；在儒家、礼教的视野下，它意味着对“天地正气”的一种信仰。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要敢于相信“天地有正气”、相信邪终不能胜正、以退可以为进、可以徐徐图之、在外可以为安。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "需要“虽九死其犹未悔”的信仰，才能坚定维持正确的行动、把正面效应发挥出来并挺过最黑暗的时期。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若对共同信仰的信心不足、犹豫徘徊，只会把本可奏效的策略执行成无效，从而自我实现“果然无效”的预言。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "臣下建言分上中下三策，本身是对君主一种不自觉的试探。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的君臣之道不同于日本武士道：武士道要求家臣放弃对主君的一切评价权、以主君价值观为绝对价值，其本质是“侍道”而非“臣道”。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“君君，臣臣”意即君主达成君主的资格，臣子才尽臣子的道义；臣对于君有基于理想的选择。", "evidence": ["E13", "E14"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的臣并非实质效命于君主，也非效命于契约、誓言，而是在理性指引下通过效命有道君主的形式与同道形成合力，去效命于自己信服的天道。", "evidence": ["E15"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要君主在可接受的范围内同样为这一理想服务，ta是否更聪明、更强大都不构成问题；作者敬的不是这个人，而是天意与自己认定其未偏离理想的判断。", "evidence": ["E16"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若判断君主不够格，作者将挂冠而去。", "evidence": ["E17"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论天命际遇或社会理想原则，都与“实力”并没有必然的逻辑关联。", "evidence": ["E18"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在秩序没有崩坏的前提下，人臣不会因为自己比君主聪明、强大、富有就认为自己“理应取而代之”。", "evidence": ["E19"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "精英的能力和资源因此不必在比暴力、比诡诈的零和博弈中被反复耗尽，可投入提供公共产品和服务。", "evidence": ["E20", "E21"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上策里有群臣的理想；君主展现真诚的道德勇气而选择上策，仅凭这份勇气就足以证明其有资格享有最大限度的忠诚。", "evidence": ["E22", "E23"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "行上策未必就能幸存，但君既君，臣必臣。", "evidence": ["E24", "E25"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中策之中有群臣可以接受的妥协，选中策证明被效忠的资格仍然有效。", "evidence": ["E26"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "下策往往完全脱离臣的理想原则，是纯粹从“最大获利、最大幸存机会”出发的策略，会带来“额外的策略空间”。", "evidence": ["E27"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "下策其实已经越理非法，有悖天道。", "evidence": ["E28"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提出下策这一行为有伦理上的二义性：既是作为朋友给出自己绝不会选的下策（尽情而非尽忠尽义），又是对君主的一次公平试炼。", "evidence": ["E29", "E30", "E31"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若君主面前根本没有被摆上过不义的选择，则即使选择义也非出于义，而是出于无知；无知之义不足以为君。", "evidence": ["E32", "E33"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "选下策，君则不君，臣亦可不臣。", "evidence": ["E34"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种选择栖身之地的逻辑今天仍在运行，仍是最可行、最有效的人生策略之一；想有所成就终究要以或君或臣的身份加入某个组织。", "evidence": ["E35", "E36", "E37"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "即使生活在火星殖民地里，只要共事者仍是人类乃至拥有人格的外星人、超人工智能，这逻辑同样有效；即使太阳陨落、人类走向星辰大海也没有失效的一天。", "evidence": ["E38", "E39"]}
   ],
   "argument_steps": [
    "P001—P002 由提问者的“古代君主”框架转出，自设两问：这是否只是古代问题、上中下按何排列。",
    "P003—P005 给出上策的一般机制（扩大时间资源项），并以三年／三天的对比与短期约束说明机制如何起作用。",
    "P006—P008 指出该机制的代价：上策太需要信心，治本要扛压力、张力与自我怀疑，无信念与道德勇气则选不下手。",
    "P009—P011 把道德释为对“天地正气”的信仰，列出所要相信的内容，并称需“虽九死其犹未悔”的信仰。",
    "P012 反证：信心不足会自我实现“果然无效”的预言。",
    "P013 提出建言三策本身是对君主不自觉的试探。",
    "P014—P018 以中日君臣之道对比与“君君，臣臣”释义，界定臣对君的选择性。",
    "P019—P024 以臣的口吻自述身份与三项天意昭示，说明其甘愿承受辛劳危险的根据。",
    "P025—P028 结论：臣效命于自己信服的天道，判断君主不够格即挂冠而去。",
    "P029—P032 说明实力与天命际遇、理想原则无必然关联，故强臣弱君不成问题。",
    "P033—P034 推出公共效果：精英能力不必耗于零和博弈，可投入公共产品与服务。",
    "P035—P039 归结三策的真相：上策里有群臣的理想；君选上策的勇气即忠诚的资格；行上策未必幸存而君臣之义已定。",
    "P040—P046 以排比短句展开臣的效死宣言。",
    "P047—P049 说明中策、下策的性质，并断言下策越理非法。",
    "P050—P056 展开下策的二义性（尽情与试炼）及其后果（君不君、臣可不臣）。",
    "P057—P066 回到“不只是古代君主的问题”：该逻辑今日仍运行，并断言其对未来与异类共事者同样有效。"
   ],
   "concept_usage": [
    {"term": "上策", "meaning": "通过扩大对策所需时间资源项，使谋略指向底层、根本、必然要素的策略；其致命问题在于太需要信心。", "evidence": "P003", "ambiguity": "与中策、下策的分界由作者以是否脱离臣的理想原则划定，未给操作标准。"},
    {"term": "君君，臣臣", "meaning": "君主达成君主的资格，臣子才尽臣子的道义；据此臣对君有基于理想的选择。", "evidence": "P017", "ambiguity": "“君主的资格”如何判定未说明。"},
    {"term": "天命／际遇", "meaning": "接受历史赋予君主的既有组织地位（天的敕封）、接受命运安排相遇（天的敕令）、承认君主对天道的可接受服从（我的意志自由）三者共同昭示的结果。", "evidence": "P023", "ambiguity": "三项如何“一起向我昭示”未论证。"},
    {"term": "天道", "meaning": "臣真正效命的对象；只要君主在可接受范围内为同一理想服务，其才干强弱不构成问题。", "evidence": "P025", "ambiguity": "未给出内容与来源。"},
    {"term": "武士道／侍道", "meaning": "要求家臣放弃对主君的一切评价权、以主君价值观为绝对价值的伦理；作者称其本质是“侍道”而非“臣道”。", "evidence": "P014", "ambiguity": "属作者的历史论断，未给史料依据。"},
    {"term": "下策", "meaning": "完全脱离臣的理想原则、纯粹从最大获利与最大幸存机会出发的策略，被作者判为越理非法、有悖天道。", "evidence": "P048", "ambiguity": "与“额外的策略空间”的关系仅以类比说明。"},
    {"term": "实力", "meaning": "与天命际遇、社会理想原则相对，被作者认为与之并无必然的逻辑关联。", "evidence": "P029", "ambiguity": "未界定实力的范围。"}
   ],
   "examples_and_targets": [
    "日本武士道、大名、家臣、侍、天皇、将军、公卿——作者用于对比中国君臣之道的历史叙述，属作者论断，待外部核查。",
    "儒家、礼教、“天地正气”——作者援引的思想资源。",
    "三年治本与三天应付、“缓释”过程——作者的说明与类比材料。",
    "弱君、强臣、理想团体——作者设定的情境。",
    "零和博弈、公共产品和服务、共同理想——作者论述中的概念性场景。",
    "火星殖民地、拥有人格的外星人、超人工智能、太阳陨落——作者用于说明逻辑永恒性的假想情境。",
    "提问者问题（古代谋士上中下三策与君主不选上策）——属提问者，非作者主张。"
   ],
   "conditions": [
    "“如果限定你在三天内出效果”（P005）。",
    "“没有坚定的信念，没有足够的道德勇气”（P008 反面条件）。",
    "“如果对共同信仰的信心不足”（P012）。",
    "“只要这人在可以接受的范围内同样是在为这个理想服务”（P026）。",
    "“在秩序没有崩坏的前提下”（P032）。",
    "“假如这个团体奉行着经典的儒家‘君君臣臣’的逻辑”（P030）。",
    "“如果你面前根本就没有被摆上过这样不义的选择”（P053）。",
    "“行上策，未必就能幸存”（P038 以“未必”限定）。",
    "“即使你已经生活在火星殖民地里，只要与你共事的仍是人类——甚至拥有人格的外星人、超人工智能”（P065）。"
   ],
   "rhetoric_and_tone": "自设两问开篇与回扣（P001—P002、P057）；长段论述与警句短句交替，P040—P046 连用排比短句，另有“君君、臣臣”“君不君、臣不臣”的对句；以第一人称“我”代入臣的立场向“你”（君）直陈，语气庄重、训诫与抒情兼具；结尾以火星殖民地、太阳陨落等夸张假设强调逻辑的永恒性。",
   "unresolved_questions": [
    "作者对日本武士道及“东亚伦理观”称谓之别的历史论断未给依据，待外部核查。",
    "“君君，臣臣”中“君主的资格”判定标准，本文未说明。",
    "“天道”“共同理想”的内容与来源，本文未说明。",
    "P022—P023 三项天意如何共同昭示“天命所归”，本文未论证。",
    "P065—P066 对超人工智能、拥有人格的外星人同样适用的说法属预测，未给依据。",
    "文中给出上、中、下三策的性质，但未给判定某一具体策略属哪一策的操作标准。",
    "P047“资格任然有效”中的“任然”为原文用字，照录不改。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "扩大对策需要的时间资源项，从而使得谋略可以指向底层的、根本的、必然的要素", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "前者自然而然的给了你更多的策略工具的选择空间", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "各种物理的、实在的约束实际上决定了你只能在极小的范围内选择", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "但是这类上策存在的致命问题，在于它太需要信心。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "一个要扛心理压力、扛组织关系的张力、扛自我怀疑的折磨的漫长过程", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "没有坚定的信念，没有足够的道德勇气，上策是选不下手的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "在儒家、在礼教的视野下，这意味着对“天地正气”的一种信仰", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P010", "quote": "要敢于相信“天地有正气”，要相信邪终不能胜正", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "需要这种虽九死其犹未悔的信仰，才能在将忧臣疑的时候坚定的维持住继续推进正确的行动", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "只会将本来可以奏效的策略执行成果然没有效果", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "臣下建言分上中下三策，本身是对君主一种不自觉的试探", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "武士道，本质上是一种“侍道”，本来就不是“臣道”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "意思是君主达成君主的资格，臣子才尽臣子的道义", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "臣对于君，是有基于理想的选择的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "而是在自己的理性指引下，通过效命于有道君主的形式、与其他同道形成合力，去效命于自己信服的天道", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "只要这人在可以接受的范围内同样是在为这个理想服务", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P027", "quote": "我如果判断你不够格，我将挂冠而去。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P029", "quote": "都与“实力”并没有必然的逻辑关联", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P032", "quote": "人臣不会因为自己比君主聪明、强大、富有就认为自己“理应取而代之”", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P033", "quote": "就不必在无穷无尽的比暴力、比诡诈的零和博弈中被反复耗尽", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P034", "quote": "就可以被投入到提供公共产品和服务中去", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P036", "quote": "上策里，有群臣的理想。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "就足以证明你有资格享有最大限度的忠诚", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "不要以为我们不知道，行上策，未必就能幸存。", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P039", "quote": "但君既君，臣必臣。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P047", "quote": "中策之中，有群臣可以接受的妥协。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P048", "quote": "是纯粹从“最大获利、最大幸存机会”而出的策略", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P049", "quote": "但是，这其实已经越理非法，有悖天道。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P050", "quote": "这是因为此时我不再单纯视你为我借以实现理想的载体", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P051", "quote": "这已经不是尽忠、尽义，而是尽情了。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P052", "quote": "第二，这是对你的一次公平的试炼。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P053", "quote": "那么你即使选择了义，也不是出于义，而是出于无知而已", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P054", "quote": "无知之义，不足以为君。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "选下策，君则不君，臣亦可不臣了。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P058", "quote": "这种选择栖身之地的逻辑仍然在运行着", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P059", "quote": "它仍然是最可行、最有效的人生策略之一。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P060", "quote": "你终究要以或君或臣的身份加入某个组织", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P065", "quote": "只要与你共事的仍是人类——甚至拥有人格的外星人、超人工智能——这逻辑都将同样有效。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P066", "quote": "即使太阳陨落，人类已经走向星辰大海，也没有失效的一天。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治伦理", "中国传统思想（儒家、礼教）", "谋略与组织行为", "历史比较"],
   "issue_candidates": ["上中下三策的排列机制", "长期治本与短期应付", "信心与道德勇气", "君臣之道的伦理基础", "臣对君的选择权", "实力与正当性"],
   "text_function_candidates": ["答疑", "论辩", "历史与文化解释", "训诫与抒情"],
   "object_candidates": ["古代谋士", "君主", "臣", "日本武士道与家臣、大名、侍", "儒家、礼教", "现代组织", "火星殖民地、外星人、超人工智能"],
   "working_keywords": ["上策", "中策", "下策", "时间资源项", "天地正气", "君君，臣臣", "天命", "天道", "挂冠而去", "侍道"]
  },
  "notes": "提问者的“君主不选上策”判断属提问者；作者未直接回答该现象的原因，而是先改写“上策”的机制再论君臣伦理。P014 关于日本武士道与“东亚伦理观”称谓的历史论断、P047“任然”等原文用字均照录，历史事实待外部核查。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "041f957b": {
  "analysis": {
   "question_context": "提问者问“如何辨别和远离心理变态等极端人士？”（Q001），“心理变态”这一用词与诊断性预设属提问者，作者未沿用该术语。作者以“比较确切的危险迹象”作答，列出三项迹象（杀生取乐、赞同“正义的虐待”、自认绝对善良且是非观简单），指出后两项合并可复现“马加爵式”的心理结构，并给出不动声色的观察方法与警告。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出存在“比较确切的危险迹象”，并给出一般建议：若不止匹配一条，一般应避免深交与利益、感情纠葛。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "迹象1“杀生取乐”的表现：对打猎特别感兴趣、对象常是随机或法规外的小动物，甚至购活物射杀；以最大痛苦伤害为追求并借“所有权”“非保护动物”辩护。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "迹象2“赞同正义的虐待”：认为某些人受虐罪有应得、某些正义需用更残酷手段惩罚，热衷虐杀与血腥复仇。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "迹象3：确信自己最多有小毛病、基本层面上无可置疑地善良、是非观念绝对正确，尤其表现为认为善恶分别很简单。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "指出2与3单看平常且比例不低，但合并触发即可复现“马加爵式”的心理结构，并让读者自行查证马加爵所为。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "补充：这类人的是非观念非常“随机”，无法自圆其说却仍确信对方有罪，且不承认自己无权据个人是非观攻击他人。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014"], "summary": "由“可以不建私交也正常生活”的时代条件，推出应特别慎重考虑值得建立私交的对象。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016", "P017"], "summary": "给出观察方法：不动声色、不诱导表态、在对方不知情下观察其与第三方互动，并列出三个观察点。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P018", "P019", "P020"], "summary": "以必然性警告收束：将来必与对方发生不公、过犯与不幸的关联，不要自恃善良，届时才知2和3的致命。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有一些比较确切的危险迹象，在结交人的时候要慎重考虑。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这些是极端危险的信号；如果甚至不止匹配一条，一般来说要避免深交，避免利益纠葛、感情羁绊。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迹象1“杀生取乐”：表现为对打猎特别感兴趣，猎杀对象常是随机碰到、计划外、法规外的小动物和鸟类，甚至购买活物圈起来射杀。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此类行为以造成最大痛苦、最大伤害为追求，并用“所有权”“非保护动物”这类理由予以辩护。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迹象2“赞同正义的虐待”：认为某些人遭受虐待是罪有应得、某些正义有必要用更残酷手段实施惩罚，热衷正义的虐杀与刻意血腥的复仇。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迹象3：确信自己最多有小小的无伤大雅的小毛病，在基本层面上是无可置疑的善良之人，有绝对正确的基本是非观念。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迹象3尤其表现为认为善与恶的分别很简单，只在很特殊情况下才难以判断，大多数情况下ta不会判断错误。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "2和3各自看起来都是很平常的属性，比例很不低。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "2和3一旦合起来触发，就能活生生地复现马加爵式的心理结构。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样的人是非观念非常“随机”：无法自圆其说，却不妨碍ta们认定对方无疑有罪。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "ta们不会意识到、更不会认可自己没有权利根据自己的个人是非观念就对别人实施攻击。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个时代真的可以不和任何人建立私交也正常生活，所以要特别慎重考虑值得建立私交的对象。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与人交往前务必不动声色地默默观察这人在相关议题上的言行态度；不要故意设定议题诱导表态，因为对方若有所图，答案没有意义。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要在对方完全不知道你的存在的前提下，默默观察ta与其他第三方的互动表现。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "观察要点：对方如何对待不公和委屈、如何看待报复和惩罚、如何看待不幸事件责任的划分。", "evidence": ["E15"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "将来你必定会给对方不公和委屈、必定会有人觉得该受惩罚的过犯、必定会与对方的某种不幸有关。", "evidence": ["E16"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要在任何意义上认为“我这么善良的人绝对不会做这样的事”。", "evidence": ["E17"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "那时候你会知道2和3有多致命的。", "evidence": ["E18"]}
   ],
   "argument_steps": [
    "P001—P002 立论：存在“比较确切的危险迹象”，并给出“不止匹配一条则避免深交”的一般判据。",
    "P003—P008 逐条列出三项迹象及其表现（杀生取乐；赞同正义的虐待；自认绝对善良且是非观简单）。",
    "P009—P011 指出2与3单看平常且比例不低，但合并触发可复现“马加爵式”的心理结构，并把马加爵具体所为交由读者查证。",
    "P012—P013 补充这类人的是非观念“随机”，且不承认自己无权据个人是非观攻击他人。",
    "P014 由“可不建私交而正常生活”的时代条件推出应慎重选择私交对象。",
    "P015—P017 给出可操作的观察方法（不动声色、不诱导表态、观察第三方互动、三个观察点）。",
    "P018—P020 以必然性警告收束：将来必与对方发生不公与不幸的关联，届时才知2和3的致命。"
   ],
   "concept_usage": [
    {"term": "危险迹象", "meaning": "作者称“比较确切”的、用于筛选结交对象的信号，共列三项：杀生取乐、赞同正义的虐待、自认绝对善良。", "evidence": "P001", "ambiguity": "未给出判定所需的行为门槛或依据。"},
    {"term": "杀生取乐", "meaning": "对打猎特别感兴趣、以造成最大痛苦和伤害为追求，并用所有权或非保护动物等理由辩护的行为模式。", "evidence": "P004", "ambiguity": "未说明与一般狩猎的界线。"},
    {"term": "正义的虐待", "meaning": "认为某些人遭受虐待是罪有应得、某些正义有必要用更残酷手段实施惩罚。", "evidence": "P006", "ambiguity": "术语置于引号内，未说明来源。"},
    {"term": "马加爵式的心理结构", "meaning": "由“赞同正义的虐待”与“自认绝对善良”两项合并触发而可复现的心理结构。", "evidence": "P010", "ambiguity": "未描述该结构的内容与依据，P011 让读者自行查证。"},
    {"term": "是非观念非常“随机”", "meaning": "无法自圆其说，却仍确信对方无疑有罪。", "evidence": "P012", "ambiguity": "“随机”为作者加引号的用法，未给定义。"},
    {"term": "私交", "meaning": "与利益纠葛、感情羁绊并列的深度交往关系。", "evidence": "P002", "ambiguity": "未界定其范围。"}
   ],
   "examples_and_targets": [
    "“打猎”、购买活物圈起来射杀、以“所有权”“非保护动物”辩护——作者举出的行为例证（对应迹象1）。",
    "马加爵——作者举出的案例，用于说明2与3合并的后果；作者未叙述其具体行为，仅让读者自行查证。",
    "“我笨嘴拙舌说不清楚，但别管你说得多头头是道，我都确定你无疑有罪”——作者为这类人拟的自我表述（拟言）。",
    "“这是一个很了不起的时代”——作者的时代判断，用作建议的前提。",
    "提问者问题“如何辨别和远离心理变态等极端人士？”——属提问者，非作者主张。"
   ],
   "conditions": [
    "“如果甚至不止匹配一条，一般来说要避免深交”（P002 条件加一般化限定）。",
    "“2和3一旦合起来触发”（P010 触发条件）。",
    "“在大多数情况下，ta都不会判断错误”（P008 对迹象3的量化限定）。",
    "“在对方完全不知道你的存在的前提下”（P016 观察方法的前提）。",
    "“对方若有所图，其实答案是没有意义的”（P015 对诱导表态无效的限定）。",
    "“将来你必定会给对方不公和委屈”（P018 以必然性表述的预设）。"
   ],
   "rhetoric_and_tone": "清单式列举（1）2）3））加第二人称告诫（“你”“你们”），语气冷峻、警戒性强；用“务必”“不要有任何侥幸”“不要在任何意义上”等命令式；引号内的拟言（“我笨嘴拙舌……”）具讽刺模拟效果；结尾以必然性预言加重紧张感。",
   "unresolved_questions": [
    "作者称迹象“比较确切”，但未给出判定标准、样本或依据，属作者断言。",
    "P010“马加爵式的心理结构”未描述其内容，P011 让读者自行查证，作者未叙述任何事实，相关事实待外部核查。",
    "三项迹象是否穷尽、彼此关系如何，本文未说明。",
    "提问者用词“心理变态”与作者所列迹象的对应关系，本文未说明。",
    "“这是一个很了不起的时代”的判断依据，本文未说明。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有一些比较确切的危险迹象，在结交人的时候要慎重考虑。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "如果甚至不止匹配一条，一般来说要避免深交，避免利益纠葛、感情羁绊。", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P004", "quote": "表现为对“打猎”特别感兴趣，而猎杀的对象常是随机碰到的、计划外、法规外的小动物和鸟类", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "以造成最大痛苦、最大伤害为追求", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "认为某些人遭受虐待是罪有应得，某些正义有必要用更残酷的手段来实施惩罚", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "确信自己最多有小小的无伤大雅的小毛病", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "认为善与恶的分别很简单，只是在某些很特殊的情况下才存在难以判断的现象", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "2和3各自看起来都是很平常的属性", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "但是2和3一旦合起来触发，就能活生生的复现马加爵式的心理结构。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "其实这样的人的是非观念非常“随机”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "而且ta们不会意识到、更不会认可自己没有权利根据自己的个人是非观念就去对别人实施攻击。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "你其实真的可以不和任何人建立私交也正常生活的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "与人交往之前，务必要不动声色的默默观察这人在一系列的相关议题上的言行态度。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "你要在对方完全不知道你的存在的前提下", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "看对方如何对待不公和委屈，看对方如何看待报复和惩罚", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "将来你必定会给对方不公和委屈", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "不要在任何意义上认为“我这么善良的人绝对不会做这样的事”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "那时候你会知道2和3有多致命的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往与识人", "心理与行为", "伦理"],
   "issue_candidates": ["危险人格的识别", "深交对象的筛选", "暴力倾向与自我认知偏差", "观察方法"],
   "text_function_candidates": ["答疑", "经验总结", "告诫清单"],
   "object_candidates": ["心理变态等极端人士（提问者用词）", "马加爵", "打猎者", "潜在的交往对象", "第三方旁观者"],
   "working_keywords": ["危险迹象", "杀生取乐", "正义的虐待", "马加爵式的心理结构", "私交", "不动声色"]
  },
  "notes": "提问者用词“心理变态”未由作者沿用为诊断术语；作者以三项迹象与观察方法作答。马加爵相关事实作者未叙述、要求读者自行查证，属待外部核查项。brief 与正文一致，仅作导航。本篇无图片节点。"
 },
 "533915a4": {
  "analysis": {
   "question_context": "提问者问“我爸不停否认我关于男女平权的观点，并且说我以后在社会上会混不下去，我该怎么办？”（Q001）。父亲的反对立场与“混不下去”的说法、以及女儿主张男女平权的立场，均属提问者转述，作者未对女权主张本身表态。作者先判定这类家常对话多半是“焦虑激荡”，再改写双方真正争执的对象，最后把答复落在“看清自己在对谁说什么、做什么”与讨论的前提规矩上。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "立论：讨论这类问题需要很高的条件；大部分家常对话没有质量与成果可言。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "提出“焦虑激荡”的往复机制：甲的焦虑表达触发乙的恐惧想象，乙的表达又触发甲，逐轮加重。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "以风车巨人、附身魔鬼为喻，说明双方不是在与对方说话，冲突实际发生在各自与自己的心病之间。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "落到本题：父亲反对的是女儿持有主张的姿态，女儿反对的是父亲不认可时“连正眼一看也不肯”的方式。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "提出最重要的能力是随时随地看清自己在对谁说什么、做什么，并称这并非理所当然而近乎“神通”；迈不过门槛者活在误会固结的“习惯”里。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "指多数人努力解决不存在的问题，靠未觉察的副作用维持“现实正威胁着ta生存”的虚假稳态；以求雨仪式作类比。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015"], "summary": "提出讨论的规矩：讨论而要有得本身有规矩——不得其人、不当其时、不在其所，不论其事。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "警告违反规矩的后果（无意义、耗生命、生痛苦、诱发妄念、造成伤害、迈入歧途），并重复口诀要求记住。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020"], "summary": "鼓励式收束：只要在谈论前考虑人、时、所三问，无论标准多幼稚粗糙错误都会获益，并再次重复口诀。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论这类问题需要很高的条件。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大部分家常对话中，对这类问题的讨论都没有质量可言，也没有有意义的成果可言。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这类对话的本质多半只是一群人挤在一起发生了一次“焦虑激荡”。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“焦虑激荡”的机制是：甲的焦虑表达触发乙的恐惧想象，乙的焦虑表达又触发甲的恐惧想象，导致甲加重语气、加大力度再次表达。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "双方是在与寄生在自己心里、却附身在对方身上的魔鬼抱摔；他也不是在对你说话，你也不是在对他说话，冲突实际发生在各自与自己的心病之间。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这位父亲反对的并不是女权的主张，而是女儿持有这种主张的姿态；女儿反对的也不是父亲对自己主张的不认可，而是父亲不认可时“连正眼一看也不肯”的方式。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最重要的事是随时随地都能看清楚自己在对谁说什么、做什么，这不是理所当然的事。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这何止不是理所当然，事实上可以说是一项神通。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "迈不过这个门槛的人几乎可以说一直活在层层叠叠的误会，以及误会固结出的看似坚固、实则布满裂纹、岌岌可危的“习惯”里。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "大多数人都在拼着极大的“努力”解决其实不存在的问题；正是这些行为未被觉察的副作用维持了“现实正威胁着ta生存”的稳态，从而获得奇妙却虚假的控制感、安全感。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如同古人相信漫长隆重的求雨仪式可以召唤龙王下雨，其实只是仪式大概率能熬到自然降雨。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论问题而要有所得，本身就是一件有规矩的事：不得其人、不当其时、不在其所，不论其事。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "否则非但结论没有意义、徒耗生命，还可能更生无谓的痛苦、诱发无明的妄念，造成本可以不发生的伤害，甚至迈入歧途。", "evidence": ["E14", "E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要在开始谈论前考虑是否可论当论之人、可谈当谈之时、可论当论之所，无论标准多么幼稚、粗糙乃至于错误，都会获得没有这意识的人可能一生望尘莫及的益处。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "P001—P002 立论：讨论此类问题需很高条件，家常对话多半无质量、无成果。",
    "P003—P004 给出机制描述“焦虑激荡”：双方的焦虑表达与恐惧想象互相触发、逐轮加重。",
    "P005—P007 以风车巨人、附身魔鬼为喻，说明双方并非在与对方说话，冲突发生在各自与自己的心病之间。",
    "P008 据此改写本题：父亲反对的是女儿持有主张的姿态，女儿反对的是父亲不认可的方式。",
    "P009—P011 提出关键能力要求：随时随地看清自己在对谁说什么、做什么，并称这是一道门槛。",
    "P012—P013 说明多数人解决的是不存在的问题，以求雨仪式为类比。",
    "P014—P015 给出讨论的规矩：不得其人、不当其时、不在其所，不论其事。",
    "P016—P018 警告违规后果并重复口诀要求记住。",
    "P019—P020 以“只要考虑三问即获益”作鼓励式收束，再重复口诀。"
   ],
   "concept_usage": [
    {"term": "焦虑激荡", "meaning": "甲的焦虑表达触发乙的恐惧想象、乙的表达又触发甲的恐惧想象并逐轮加重的往复过程。", "evidence": "P003", "ambiguity": "术语加引号，未说明来源，也未给出适用范围的界限。"},
    {"term": "不得其人、不当其时、不在其所，不论其事", "meaning": "作者提出的讨论前提规矩：人、时、所三者不当则不讨论。", "evidence": "P015", "ambiguity": "三项的判定标准未给出；P019 只说标准即使幼稚粗糙错误也可获益。"},
    {"term": "神通", "meaning": "作者用来形容“随时随地看清自己在对谁说什么、做什么”这一能力。", "evidence": "P010", "ambiguity": "修辞用法，未作宗教或心理学术语定义。"},
    {"term": "心病／魔鬼", "meaning": "比喻双方各自内心的问题，被说成寄生在自己心里、却附身在对方身上。", "evidence": "P006", "ambiguity": "隐喻表述，未给出对应的学理概念。"},
    {"term": "稳态", "meaning": "由未被觉察的副作用维持的“现实正威胁着ta生存”的状态。", "evidence": "P012", "ambiguity": "术语来源与所指机制未说明。"},
    {"term": "女权的主张", "meaning": "仅作为提问者与父亲争执的议题出现，作者未对其内容作评价。", "evidence": "P008", "ambiguity": "作者只论争执的姿态与方式，未说明对该主张的看法。"}
   ],
   "examples_and_targets": [
    "提问者与其父亲的冲突——提问者提供的处境，作者据此改写双方真正争执的对象，属提问者说法。",
    "风车巨人、红着眼睛拿着破枪——作者借用的比喻形象，未点名出处。",
    "古人求雨仪式、龙王、九九八十一天——作者的类比例证。",
    "“他也不是在对你说话，你也不是在对他说话”——作者对提问情境的判断。",
    "女权主张、男女平权——提问者与父亲争论的议题，作者对其本身未表态。"
   ],
   "conditions": [
    "“讨论这类问题，是需要很高的条件的”（P001 前提）。",
    "“大部分家常对话中”（P002 范围限定）。",
    "“其本质多半只是”（P003 以“多半”限定）。",
    "“不得其人、不当其时、不在其所”（P015 前提条件）。",
    "“只要你在开始谈论事情之前考虑：这是不是可论、当论之人……”（P019 条件式承诺）。",
    "“无论你的标准是多么幼稚、粗糙乃至于错误”（P019 让步限定）。"
   ],
   "rhetoric_and_tone": "以比喻和意象说理（风车巨人、附身魔鬼、求雨仪式）；第二人称“你”直接对话提问者；口诀式短语三次重复（P015、P018、P020）以强化记忆；语气训诫而收束处转为鼓励（“你都会获得……益处”）；对争论双方的立场本身不作评判。",
   "unresolved_questions": [
    "作者未给出“我该怎么办”的直接建议，也未讨论女儿应否继续坚持其主张，只给出讨论条件与自我觉察要求。",
    "“很高的条件”具体指哪些条件，本文未列出。",
    "P008 关于父亲与女儿各自真正反对之物的判断，是作者依提问者描述所作的推断，提问者未提供其父原话。",
    "“焦虑激荡”的来源与适用范围，本文未说明。",
    "风车巨人的比喻是否指向《堂吉诃德》，作者未点名。",
    "本篇无图片节点，图片核验事项不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "讨论这类问题，是需要很高的条件的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "大部分家常对话中，对这类问题的讨论都没有质量可言，也没有有意义的成果可言。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "其本质多半只是一群人挤在一起发生了一次“焦虑激荡”。", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P004", "quote": "甲的焦虑表达，触发了乙的恐惧想象", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "你们是在与寄生在自己心里、却附身在对方身上的魔鬼抱摔在一起。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你们的“激烈冲突”，只是形式上发生在你们之间", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这位父亲反对的并不是女权的主张，而是女儿持有这种主张的姿态", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "随时随地都能看清楚自己在对谁说什么、做什么", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "事实上可以说是一项神通", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "一直都活在层层叠叠的误会", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "在解决其实不存在的问题", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "求雨仪式很自然地能大概率熬到自然降雨而已", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "不得其人、不当其时、不在其所，不论其事。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "非但其结论没有意义、徒耗生命", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "甚至由此迈入一段迂回曲折的歧途。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "你都会获得没有这意识的人可能一生都望尘莫及的益处", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["沟通与说理方法", "家庭关系", "通俗心理"],
   "issue_candidates": ["家常争论的无效性", "焦虑激荡", "讨论的前提条件", "女权议题引发的家庭冲突"],
   "text_function_candidates": ["答疑", "说理劝导", "比喻性解释"],
   "object_candidates": ["提问者", "提问者的父亲", "女权主张", "古人求雨（类比）", "龙王（比喻）"],
   "working_keywords": ["焦虑激荡", "不得其人、不当其时、不在其所，不论其事", "心病", "神通", "稳态", "风车巨人"]
  },
  "notes": "提问者转述的父亲立场与“混不下去”之说未归入作者主张；作者对女权主张本身未表态，只论争执姿态与讨论条件。brief 与正文一致，仅作导航。本篇无图片节点。"
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
