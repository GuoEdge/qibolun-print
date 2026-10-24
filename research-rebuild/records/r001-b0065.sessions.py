# -*- coding: utf-8 -*-
"""批次 r001-b0065 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0065.sessions.py            # 写 out/r001-b0065.out.jsonl
  python3 records/r001-b0065.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0065"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0065.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6dfd5709": {
  "analysis": {
   "question_context": "知乎提问（问题字段，属提问者）问“国内很多家庭不够整洁，深层次原因是什么？”。作者以答案形式回应，开头即以“不会用闲鱼。”作答，随后把“家庭不够整洁”转译为囤积者对“拥有—损失”的算式问题、有限储存空间的配置问题与二手循环策略问题，并在末段给出闲鱼交易的操作规则。提问者的立场未在问题中展开，不得与作者主张混同。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开门作答：“不会用闲鱼。”", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "指出囤积者的心理算式（不扔＝拥有与收益，扔掉＝损失），并否定靠美感、情绪说服丢东西的做法。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "提出必须解决该算式，办法是把帐算清楚。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "以二十立方米储存空间为假设，说明容量即可物理拥有的财富总和、席位有限、闲置物资形成“死空间”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "以“财产是外延／物质机体”的说法要求持续更新优化、善用席位并及时纠正。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "限定：“囤积”本身不是错，前提是依照上述原则；只获取而不整理管理更新是自我放弃甚至毒害。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "主张重品质添置并靠循环回收降成本，以二手手机换代为例，称同类策略可用于几乎所有耐用品。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "循环更新会改变物资配置：重视经典性、卖出可能反赚、好物影响命运。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "以反问要求在购买前面向闲鱼定价；称真正付出的是买卖差价，二手售价本质是使用押金，并举奔驰G。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029"], "summary": "第二条：注重使用方法、养成爱惜习惯，并因此加深对物品的理解。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037"], "summary": "反驳“这样生活太累了吧”：称其真傻，主张享受建立在对细节的理解与关注上，不懂者只得虚荣感；称物品知识是宝藏，不懂者难被认为有产品触觉。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "第三条：获得对人的洞察力，识货关系形成“接力圈”，圈内可低成本共享物资。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048"], "summary": "第四条：眼力门槛提高、理解加深而自然节俭，物件可能成为传世文物并对继承人有价值。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P049", "P050", "P051"], "summary": "结论：真正的“囤积”是不断循环和精炼直至不朽；做到则不太需要“断舍离”而自然整洁。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057", "P058"], "summary": "闲鱼周转最佳实践：到手即挂、挂“卖掉也划算”的价格、手拍照片、照片必备六类展示、标题挂关键词、明文交易规则。", "role": "action_advice"},
    {"unit_id": "U016", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063", "P064"], "summary": "交易规则条款：只接受直接拍下不私聊、自动降价不接受还价、不提供售后、芝麻信用门槛（选填）、包邮范围。", "role": "action_advice"},
    {"unit_id": "U017", "paragraph_refs": ["P065", "P066", "P067", "P068"], "summary": "发布后定期闹钟更新价格与擦亮；拉黑违规者，给顺利交易的买家发红包加好友，积累低交易成本买家名单。", "role": "action_advice"},
    {"unit_id": "U018", "paragraph_refs": ["P069", "P070"], "summary": "结论：机械执行规则会使东西迟早卖出并越来越好卖，并有机会获得自己的物资生态圈。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "囤积的人主要把“不扔”当作仍然拥有这些东西，视之为拥有和收益，而把扔掉视为损失。", "evidence": ["E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "用美感因素、情绪因素去说服这些人（或自己）丢东西是不现实的，因为对很多人而言美感和情绪不值钱。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要解决这个问题必须先解决该算式，即把帐算清楚；摆不平这个算式一切都是枉然。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "在假设储存空间为二十立方米、且不换更大房子的前提下，该容量代表可物理拥有的财富总和；闲置物资占用的是“死空间”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "直接财产是人的外延；囤积无用之物等于“身体”坏死一部分，应持续更新、优化“物质机体”。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“囤积”本身不是错，前提是充分依照上述更新、整理、管理原则；只获取而不整理、不管理、不更新是自我放弃甚至毒害。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "添置时应拣负担得起的最好的东西并珍惜对待，同时用循环回收降低成本。", "evidence": ["E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以自己买手机为例：通过二手渠道买上一代顶配、新品发售前换代，一年手机支出约千把块（买卖差价）而一直用顶配；同类策略可用于几乎所有耐用品。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果选购得当，很多东西到卖出时甚至可以反过来赚一些钱，非电子类物品有较大机会做到。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "买入之前就该知道这东西卖不卖得出去、大概什么价，因为真正付出的是买入与卖出两个价格之间的差额，二手售价本质上只是使用押金。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "很多人认为这种讲究物品知识的生活方式“太累”。（他人看法，非作者主张）", "evidence": ["E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定上述“太累”的看法（“这是真傻”），主张生活的享受建立在对生活大量细节的理解与关注里，不了解的人享受不到真正美好处、只是虚荣感，并称这类人恰是闲鱼玩家的主要利润来源之一。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "被人发现不懂这些物品门道，你大概率不会被认为是有足够敏锐产品触觉的人。", "evidence": ["E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有了这些经验就会拥有额外对人的洞察力，通过交易更易看出同类，识货关系会形成“接力圈”，圈内可以相当低成本共享物资。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "有了这些经验与思路，能打动你的东西门槛会变高，你会自然而然“节俭”——东西越来越少却件件是好东西，有些甚至对继承人有价值、可成为传世之物。", "evidence": ["E28", "E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的“囤积”不是买进来堆着，而是不断循环和精炼直至不朽；做到这几条就不太需要“断舍离”而会自然整洁。", "evidence": ["E30", "E31"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "闲鱼周转的操作要点：有换代打算的东西到手（或不久）就挂出、挂“此时卖掉也觉得划算”的价格、用手拍照片并关闭地理信息、照片尽可能含六类展示。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "交易规则应明文写清：只接受直接拍下不提供私聊、自动不定期降价且不接受还价、不提供售后、可设芝麻信用“极好”门槛（选填）、限定包邮范围。", "evidence": ["E35", "E36", "E37", "E38"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "发布后设定期闹钟、稳定更新价格与一键擦亮即可；凡不遵守明文规则者一概拉黑，凡顺利交易过的买家完成后发红包加好友，以积累低交易成本的买家名单，作者称该名单本身就是最核心的标的之一。", "evidence": ["E39", "E40", "E41", "E42"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "只需机械执行这套交易规则，东西自然或迟或早会卖出去，以后越来越好卖，并有机会获得属于自己的物资生态圈。", "evidence": ["E43", "E44"]}
   ],
   "argument_steps": [
    "以一句话答案“不会用闲鱼”正面回应提问，随后展开。",
    "先把问题定义为囤积者的得失算式：不扔＝拥有和收益，扔掉＝损失（P002）。",
    "排除一条路径：以美感、情绪说服丢东西不现实（P003）。",
    "提出解法：算清这笔帐（P004-P005）。",
    "建立量化前提：储存容量＝可拥有财富总和，席位有限，闲置物资＝死空间（P006-P008）。",
    "以“财产是外延／物质机体”作类比，推出应持续更新优化并纠正不合条件的情况（P009-P013）。",
    "让步与限定：囤积本身不是错，前提是按原则整理管理（P014）。",
    "给出正向做法：挑负担得起的最好的、珍惜使用、循环回收降成本（P015）。",
    "以手机换代为例证，并推广到几乎所有耐用品（P016-P018）。",
    "推出四项后果：重视经典性可能反赚（P019-P023）、注重使用方法（P028-P029）、获得对人的洞察力与接力圈（P038-P042）、自然节俭而成传世之物（P043-P048）。",
    "用反问处理“卖不出去”的抱怨：买入时就该面向闲鱼定价，售价即押金（P024-P027）。",
    "反驳“这样生活太累”的流行看法，并以“不懂则无产品触觉”加重（P030-P037）。",
    "回到结论：真正的囤积是循环与精炼，做到就无需断舍离（P049-P051）。",
    "转入操作层：给出闲鱼挂牌、照片、标题、交易规则与售后维护的完整清单（P052-P068）。",
    "预测执行效果：迟早卖出、越来越好卖、形成自己的物资生态圈（P069-P070）。"
   ],
   "concept_usage": [
    {"term": "公式", "meaning": "作者把“不扔＝拥有和收益、扔掉＝损失”的得失心理称作需要“摆平”的公式，未给出数学定义。", "evidence": "P004", "ambiguity": "为口语化隐喻，具体变量与算法本文未说明。"},
    {"term": "席位", "meaning": "有限储存空间中被物品占用的位置。", "evidence": "P008", "ambiguity": "与“二十立方米”假设绑定，未说明实际家庭如何换算。"},
    {"term": "死空间", "meaning": "被不准备再使用的物资占用的储存空间。", "evidence": "P008", "ambiguity": "未给判定“不再使用”的时间标准。"},
    {"term": "外延／物质机体", "meaning": "把个人财产与物资视为身体的延伸，因此需要更新与维护。", "evidence": "P009", "ambiguity": "作者自称“在哲学意义上说”，未指明所属学说。"},
    {"term": "循环更新／持续更新和优化", "meaning": "买入—使用—卖出的物资周转策略，用以降低成本并保持配置最优。", "evidence": "P018", "ambiguity": "未说明适用频率与失败情形。"},
    {"term": "押金", "meaning": "二手售价被解释为使用押金，真正成本是买入价与卖出价之间的差额。", "evidence": "P026", "ambiguity": "以“付得起押金”为前提，未讨论价格波动风险。"},
    {"term": "同类／接力圈／物资生态圈", "meaning": "由识货关系连接起来的买卖双方网络，可低成本共享物资。", "evidence": "P040", "ambiguity": "“同类”的判定标准与圈子边界本文未说明。"},
    {"term": "断舍离", "meaning": "流行的舍弃物品主张；作者称做到上述几条就不太需要它。", "evidence": "P050", "ambiguity": "作者未正面定义该词。"}
   ],
   "examples_and_targets": [
    "二手手机换代的具体做法与成本（作者自述经验，例证，P016-P017）。",
    "奔驰G：用以说明付得起押金时贵物也不贵（类比，P027）。",
    "观音土：比喻只囤不用“塞得胀鼓鼓，却一点不顶饿”（比喻，P014）。",
    "“一头二十一立方米的野兽”：把财产说成鳞甲、毛发和爪牙（比喻，P009）。",
    "闲鱼平台上的引流贴、标准广告照与手拍照片（平台经验，P055）。",
    "闲鱼玩家：被作者称为最大利润来源之一（对某类人的判断，P034）。",
    "被反驳对象：认为“这样生活太累了吧”的很多人（P030）；抱怨东西在闲鱼卖不出去的很多人（P024）。",
    "品牌故事、市场传奇与物品知识（作者称其为宝藏，P035）。",
    "继承人与传世文物、传家宝（长期保有与传承的例子，P046-P047、P053）。",
    "芝麻信用“极好”、顺丰陆运、罗列过远省份（交易规则中的平台与物流条件，P063-P064）。"
   ],
   "conditions": [
    "“在你不换更大的房子的前提下，这个空间就这么大了”（P007）。",
    "储存空间“假设这个空间总共是二十立方米”为举例假设（P007）。",
    "“囤积”本身不是错，前提是充分依照上述原则（P014）。",
    "“如果你选购得当”才有卖出反赚的机会（P021）。",
    "“在你付得起押金的情况下，奔驰G也并不贵”（P027）。",
    "“如果你觉得这个‘累’，这真的是可惜了”——针对不接受该生活方式者的条件句（P037）。",
    "交易规则中的可选与例外：芝麻信用门槛“这一条选填”，贵重物品可用第二种写法（P063）；“中国境内除（罗列过远省份）外均包邮顺丰（陆运）”（P064）。",
    "挂牌前提：不是打算变成传家宝的、有升级换代打算的东西（P054）。",
    "适用对象为“很多人／你”的泛称读者，未限定收入、城市或家庭规模。"
   ],
   "rhetoric_and_tone": "第二人称“你”贯穿全文，训诫与劝说并用，语气笃定直白（“说实话，这是真傻”）。大量反问（“你在购买的时候有面向闲鱼购买吗？”“你岂能不慎重选择，爱惜使用？”“否则怎么叫爱惜呢？”）。以比喻和夸张说理（二十一立方米的野兽、观音土、死空间）。用“第一／第二／第三／第四”和“a）b）”分条推进，并用括号插入补充与调侃（P034）。后三分之一从论说转为操作清单，直接抄录挂牌规则、交易规则原文，含“一概拉黑”等强硬措辞；第三人称复数写作“ta们”。",
   "unresolved_questions": [
    "提问问“国内很多家庭不够整洁，深层次原因是什么”，作者只以“不会用闲鱼”与物资配置视角作答，是否穷尽或回应了“国内”与“深层次”未说明。",
    "“公式”“摆平”等说法未给出明确定义或推导过程。",
    "手机例证中的“千把块”为作者个人经验，未给数据来源与时间段。",
    "“非电子类的物品有很大的机会可以做到这样的效果”（P021）所指概率与条件不明。",
    "作者身份与经验背景（如是否为长期闲鱼玩家）本文未交代。",
    "结构上 P053 与 P054-P058、P059 与 P060-P064、P066 与 P067-P068 文本重叠（列表容器与子项），系 lexical 结构对齐结果，非作者重复写作，解读时需注意。",
    "P053 内的“物品”后接“标题挂上&34;关键词”在结构切分处被截断，P057 含“&34;”转义残留，原文此处字符可疑，待核。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不会用闲鱼。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "囤积的人主要是觉得东西不扔总是拥有着这些东西，是一种拥有和收益，而扔掉总是一种损失。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你要因为美感因素、情绪因素去说服这些人（或者自己）丢东西，这是不现实的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你要解决这个问题，首先就要解决这个公式，摆平不了这个公式，一切都是枉然。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "那就是把帐算清楚。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "在你不换更大的房子的前提下，这个空间就这么大了", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这些物资所占用的空间就是“死空间”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你的直接财产是你的外延", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "囤积无用之物，就是你的“身体”坏死了一部分。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "你理所应当不断的更新、持续优化你的“物质机体”，力求磨砺到最佳状态。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "“囤积”本身不是错，前提是要充分依照上述原则。", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P014", "quote": "只获取，不整理，不管理，不更新，这其实是自我放弃，甚至是毒害", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "你要拣你负担得起的最好的添置，然后珍惜的对待，而用循环回收来降低成本。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "不必购买最新版的手机，而是通过二手渠道在最新版发布之后购买上一代的九九新的、箱说齐全的、在保的顶配机型", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "一年用在手机上的钱大概也就千把块（只是买入卖出的差价），但是一直用的是顶配", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "同类的策略你可以用在几乎所有的耐用品上，这就是所谓的“持续更新和优化”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "如果你选购得当，很多东西甚至到卖出时可以反过来赚一些钱", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "你真正付出的实际上是这两个价格之间的差额，而二手售价本质上只是你的使用押金。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P027", "quote": "在你付得起押金的情况下，奔驰G也并不贵", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "很多人认为“这样生活太累了吧”。", "relation": "context"},
    {"key": "E21", "paragraph_id": "P031", "quote": "说实话，这是真傻。", "relation": "contradicts"},
    {"key": "E22", "paragraph_id": "P032", "quote": "生活的享受要建立在对生活的大量细节里的理解和关注里。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "事实上这些人也恰恰是闲鱼玩家最大的利润来源之一", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P036", "quote": "被人发现你不懂得这些东西里面的道道，你大概率也不会被认为是一个有足够敏锐的产品触觉的人", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "你有了这些经验，你就会拥有额外的对人的洞察力。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P040", "quote": "会借着这同样的“识货”关系形成一个“接力圈”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "在这个圈子里，可以以相当低的成本共享物资。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P044", "quote": "东西越来越少，但却件件都是好东西。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P047", "quote": "这支笔，除了是只好笔，还因为是你的笔，最后对你的继承人是有价值的。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P049", "quote": "真正的“囤积”不是买进来堆着，而是不断的循环和精炼，直至不朽。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P050", "quote": "你根本不太需要所谓“断舍离”，而且自然而然会整洁起来", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P054", "quote": "在到手的同时（或者不久）就挂上去。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P055", "quote": "挂出时用手拍照片（注意关闭地理信息）。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "物品照片必须尽可能包含以下几条：原理展示、功能正常展示、光泽效果展示、缺损情况展示、规格详情展示", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P058", "quote": "交易规则清晰明确的给定以下几条：", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P060", "quote": "本人工作繁忙，不提供私聊语言沟通，只接受直接拍下。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P061", "quote": "本货品将自动不定期降价。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P063", "quote": "只接受芝麻信用“极好”评级的买家（这一条选填）", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P065", "quote": "建议你稳定的更新价格和一键擦亮宝贝", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P067", "quote": "凡是不遵守这些明文规则的，一概拉黑。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P068", "quote": "凡是顺利交易过的买家，交易完成后都发红包，加闲鱼好友。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P068", "quote": "实际上这个名单本身就是你要“买到”的最核心的标的之一。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P069", "quote": "你只需要机械的执行这个交易规则，自然或迟或早东西都会卖出去。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P070", "quote": "而且你有机会获得一个属于你的物资生态圈。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["消费与二手交易", "家庭物资管理与整理", "个人理财与成本核算", "生活方式论说"],
   "issue_candidates": ["囤积与家庭不整洁的成因", "断舍离／美感劝说的局限", "使用成本＝买卖差价／押金", "物品知识与身份认同", "闲鱼交易规则与买家筛选", "物资循环与传承"],
   "text_function_candidates": ["答疑", "经验总结", "操作指南", "论辩与反驳", "训诫式劝说"],
   "object_candidates": ["闲鱼（二手平台）", "奔驰G", "芝麻信用", "顺丰", "中国境内", "知乎提问者", "继承人与传家宝"],
   "working_keywords": ["循环买卖", "循环更新", "持续更新和优化", "死空间", "席位", "物质机体", "外延", "使用押金", "接力圈", "物资生态圈", "传世文物", "断舍离", "引流贴", "一键擦亮", "ta们"]
  },
  "notes": "正文 3361 字（P001-P070）已全文读完，本篇无图片节点（图片清单为空），故 status=read、full_text_checked=true。结构提示：P053/P059/P066 为 list 容器且其文本与子项 P054-P058/P060-P064/P067-P068 重叠，属生成器按 lexical 对齐的结果，不是作者重复书写。P057 含“&34;”转义残留、P053 中“物品”处文本被结构切分截断，已在 unresolved_questions 登记。提问字段属提问者，正文中“很多人认为”“ta们”等他人说法已与被反驳观点分开标注。"
 },
 "e9a92f51": {
  "analysis": {
   "question_context": "知乎提问（问题字段，属提问者）问“女性怎样不算「幼稚」？”。作者以极短段落作答：先给出一个字面回答“不怕。”，随即反讽地铺陈社会期待女性所“怕”的清单，进而追问“到底什么是幼稚”并给出定义，最后把幼稚归结为缺少“真实的勇气”，并限定“说不怕，不是叫你啥都不怕”。正文未给出可操作清单，而是给出机制分析与定义；提问本身属提问者，不得当作作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开门作答“不怕。”，并给出判断：女性的“幼态”绝大多数是在展现一种“怕”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "以“你应该怕……”排比代拟社会对女性的一长串惧怕要求，末尾以省略号收束。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "怕全了就有“女人味”；“ta们”鉴定后觉得“还嫩着”并把这种幼稚当优点甚至卖点；不怕则贴不上标签，说不怕又会被说“你太幼稚了”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P023"], "summary": "以“Poetic irony。”评述上述处境。", "role": "other"},
    {"unit_id": "U005", "paragraph_refs": ["P024", "P025", "P026"], "summary": "转入定义：幼稚是对思考成熟度的不认可；并限定评价者未必对，可能基于不成熟的评价体系，甚至只是对结论不同意就认定思考过程不成熟。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "说明何种信号招致幼稚评价：早期心智的“默认配置”、反其道而行之的第二阶段预设状态，直到人们不能再假设你因受教育或反叛教育才采取立场时才摆脱。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P031", "P032"], "summary": "仍处幼稚状态者的决定出于教育与纸面计算，脆弱、经受不起期待和信任、无法当真；咬牙赌咒也无大用。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P033", "P034", "P035", "P036"], "summary": "归结：幼稚是指缺少真实的勇气——不是基于乡愿的、让身经百战的人也觉得值得一赌的、安静的明智的勇气。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P037", "P038", "P039"], "summary": "结尾限定：“说不怕”不是叫你啥都不怕，啥都不怕只能是装的，不学那些中二男。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "女性的“幼态”绝大多数都是在展现一种“怕”。", "evidence": ["E2"]},
    {"claim_id": "C002", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者以排比代拟／引述社会（“ta们”）要求女性具备的惧怕清单：蟑螂老鼠蛇、脏、危险、长痘痘、晒黑、撞衫、数学、计算机、开车、没人追、嫁不出去、离婚、老。此清单属被引述的他人期待，非作者主张。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你把上述都怕全了，就充满了“女人味”。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "“ta们”一一鉴定完毕、得到满意答复后会在心里说“这个还嫩着”；在“ta们”而言这种幼稚是优点甚至卖点。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你这也不怕那也不怕，这个（幼稚）标签就贴不下去了。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们不会说你“太成熟”，而会说“你完全没有女人味，你不怕找不到老公吗？”；你若说不怕，他们就说“你太幼稚了”。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“Poetic irony”评价上述对待。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "幼稚是一种对思考成熟度的不认可。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这不意味着评价者自己一定对：评价者可能基于不成熟的评价体系；甚至不必涉及思考成熟度，只是对结论不同意，就足以据结论认定思考过程必定不成熟。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的心智发育有阶段，早期思维方式有“默认配置”；若你的每种判断与表达都显示仍处该状态，别人就会认定你幼稚。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若你意识到问题并一切反其道而行之，仍会被认为幼稚，因为这只不过是第二阶段的预设状态。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有到了人们不能再假设你采取某个立场只是因为你受到某种教育或试图反叛某种教育时，你才会摆脱这个评价。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "仍在幼稚状态的人的决定出于教育和纸面计算，因此脆弱、经受不起期待和信任、无法当真；他们缺对未知的敬畏，也没做好面对出乎意料风险的准备。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使咬牙切齿、赌咒发誓，实践起来也没大用；当黑暗降临，这些勇气和决心顶不过一柱香。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "归根到底，幼稚是指缺少真实的勇气——不是基于乡愿的、让身经百战的人也觉得值得一赌的、安静的、明智的勇气。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "“说不怕”不是叫你啥都不怕；啥都不怕只能是装的；不学那些中二男。", "evidence": ["E22", "E23", "E24"]}
   ],
   "argument_steps": [
    "先给字面答案“不怕。”，再给出命题：女性的“幼态”多数是在展现“怕”（P001-P002）。",
    "用“你应该怕……”的排比代拟社会期待，陈列女性被要求惧怕的对象，并以省略号示意未尽（P003-P016）。",
    "指出该期待的兑现方式：怕全了＝“女人味”，并被“ta们”鉴定为“还嫩着”、当作优点与卖点（P017-P019）。",
    "指出两难：不怕则标签贴不上，说不怕又会被说“你太幼稚了”，作者评之为 Poetic irony（P020-P023）。",
    "提出问题“到底什么是幼稚？”，给出定义：对思考成熟度的不认可（P024-P025）。",
    "限定该定义：评价者未必对，甚至可能只凭对结论的不同意就判定思考不成熟（P026）。",
    "追问何种信号招致该评价，给出阶段论解释：默认配置→反向仍是第二阶段预设→直到不再被假设受某种教育支配才摆脱（P027-P030）。",
    "补充理由：幼稚状态的决定出于教育与纸面计算，脆弱不可当真，缺对未知的敬畏与风险准备；决心顶不过一柱香（P031-P032）。",
    "归结为定义性结论：幼稚是指缺少真实的勇气，并对“真实的勇气”给出三个限定（非乡愿、让身经百战者觉得值得一赌、安静明智）（P033-P036）。",
    "结尾反转限定：不怕不是啥都不怕，啥都不怕只能是装的（P037-P039）。"
   ],
   "concept_usage": [
    {"term": "幼态", "meaning": "女性表现出的幼稚姿态；作者称其绝大多数是在展现一种“怕”。", "evidence": "P002", "ambiguity": "与后文“幼稚”的定义是否同一，本文未明确。"},
    {"term": "怕／不怕", "meaning": "既指被要求具备的具体畏惧（清单），也指作者主张应去除的畏惧状态；开篇以“不怕”作答。", "evidence": "P001", "ambiguity": "两义在同一词上并用，靠上下文区分。"},
    {"term": "女人味", "meaning": "加引号的他人评价标准，与“怕全了”挂钩。", "evidence": "P017", "ambiguity": "作者未给定义，属引述他人用语。"},
    {"term": "ta们", "meaning": "作鉴定与评价的他人群体（评价者）。", "evidence": "P018", "ambiguity": "具体身份（男性／社会舆论／长辈）未指明。"},
    {"term": "幼稚", "meaning": "先定义为“对思考成熟度的不认可”，后归结为“缺少真实的勇气”。", "evidence": "P025", "ambiguity": "两个定义的关系与判据本文未打通。"},
    {"term": "默认配置／预设状态／阶段", "meaning": "心智发育阶段说中的早期思维方式与第二阶段的反向反应。", "evidence": "P028", "ambiguity": "未给出阶段划分依据或出处。"},
    {"term": "乡愿", "meaning": "作者用以排除的勇气类型（不是真实的勇气）。", "evidence": "P034", "ambiguity": "未给定义。"},
    {"term": "真实的勇气", "meaning": "让身经百战的人也觉得值得一赌的、安静的、明智的勇气。", "evidence": "P033", "ambiguity": "仅以三个修饰语刻画，未给判据。"},
    {"term": "中二男", "meaning": "网络语，指装作啥都不怕的人，作者表示不学。", "evidence": "P039", "ambiguity": "属修辞用语，非严格概念。"}
   ],
   "examples_and_targets": [
    "惧怕清单（蟑螂／老鼠／蛇、脏、危险、长痘痘、晒黑、撞衫、数学、计算机、开车、没人追、嫁不出去、离婚、老）：作者代拟／引述的社会期待，含反讽，不是作者主张（P003-P015）。",
    "“ta们”的鉴定场景与心中评语“嗯，这个还嫩着”：他者评价的转述（P018）。",
    "被引述的他人话语：“你这太成熟了”“你完全没有女人味，你不怕找不到老公吗？”“你太幼稚了”（P021-P022）。",
    "“Poetic irony。”：作者插入的英文评语（P023）。",
    "“一柱香”：比喻时间极短的修辞材料（P032）。",
    "“中二男”：网络俗语，用于结尾的调侃与划界（P039）。",
    "被质疑对象：以结论判定思考过程不成熟的评价者（P026）。"
   ],
   "conditions": [
    "“绝大多数”这一限定语（P002）。",
    "“如果你每一种判断、每一种表达都显示出你仍然处在这个默认配置状态”（P028）。",
    "“如果你意识到了这个问题，开始一切反其道而行之”（P029）。",
    "“只有到了人们不能再假设你采取某个立场只是因为你受到了某种教育或者试图反叛某种教育时”（P030）。",
    "“即使你咬牙切齿，赌咒发誓”（P032）。",
    "“说不怕，不是叫你啥都不怕”（P037）。",
    "适用对象：提问与正文多处指向“女性／女人味”，但 P028-P036 以泛称“人／你”展开；是否只适用于女性，本文未说明。"
   ],
   "rhetoric_and_tone": "句式极短、分段极碎，靠排比与重复推进（连续十余段“你应该怕……”）。主要手法是反讽：先把社会期待罗列成清单，再点出“你都怕全了，你就充满了‘女人味’”，并以“Poetic irony。”作评。大量引号引述他人话语，第二人称“你”直接对读者说话，间或用“咱”拉近。插入英文短句与网络语“中二男”。结构上先答后驳再定义，结尾用短句反转限定，带训诫与调侃语气。",
   "unresolved_questions": [
    "“ta们”具体指谁（男性、社会舆论、长辈或其他）本文未说明。",
    "心智“阶段／默认配置／第二阶段的预设状态”未给出依据、出处或阶段数目。",
    "“真实的勇气”与“乡愿”“装的”之间如何区分，本文未给判据。",
    "提问问“女性怎样不算幼稚”，正文先答“不怕”又限定“不是叫你啥都不怕”，未给出可操作的判定标准。",
    "正文后半以泛称“人／你”论述，与提问限定的女性范围是否一致未说明。",
    "本篇无图片节点，未见平台话题标签混入正文；正文与结构（lexical）无分歧报告。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不怕。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "女性的“幼态”，绝大多数都是在展现一种“怕”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你应该怕蟑螂 / 老鼠 / 蛇，", "relation": "context"},
    {"key": "E4", "paragraph_id": "P017", "quote": "你都怕全了，你就充满了“女人味”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P018", "quote": "ta们一一鉴定完毕，都得到了满意的答复，就会在心里说“嗯，这个还嫩着”。", "relation": "context"},
    {"key": "E6", "paragraph_id": "P019", "quote": "在ta们而言，这种幼稚是一种优点，甚至是卖点。", "relation": "context"},
    {"key": "E7", "paragraph_id": "P020", "quote": "你这也不怕那也不怕，这个标签就贴不下去了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P021", "quote": "而是会跟你说“你完全没有女人味，你不怕找不到老公吗？”", "relation": "context"},
    {"key": "E9", "paragraph_id": "P022", "quote": "你要说不怕，他们会说“你太幼稚了”。", "relation": "context"},
    {"key": "E10", "paragraph_id": "P023", "quote": "Poetic irony。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P025", "quote": "幼稚是一种对思考成熟度的不认可。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P026", "quote": "这并不意味着评价者自己就一定是对的", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P026", "quote": "只是对结论不同意，就已经足够ta根据结论认定思考过程必定不成熟了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P028", "quote": "如果你每一种判断、每一种表达都显示出你仍然处在这个默认配置状态，别人就会认定你幼稚。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "你还是会被认为幼稚——因为这只不过是第二阶段的预设状态。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P030", "quote": "只有到了人们不能再假设你采取某个立场只是因为你受到了某种教育或者试图反叛某种教育时，你才会摆脱这个评价。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P031", "quote": "ta们的决定是脆弱的，是经受不起期待和信任的，是无法当真的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P032", "quote": "当黑暗降临，这些勇气和决心顶不过一柱香。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P033", "quote": "其实归根到底，幼稚是指缺少真实的勇气——", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P035", "quote": "让身经百战的人也觉得值得一赌的、", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P036", "quote": "安静的、明智的勇气。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "说不怕，不是叫你啥都不怕。", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P038", "quote": "啥都不怕只能是装的，", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P039", "quote": "咱不学那些中二男。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与社会期待", "心智成熟与评价机制", "标签与语言批评"],
   "issue_candidates": ["“幼稚”评价的成因与机制", "女性“幼态”“女人味”的社会建构", "勇气与成熟的定义", "评价者自身是否成熟"],
   "text_function_candidates": ["答疑", "评论与批评", "定义辨析", "反讽式论辩"],
   "object_candidates": ["女性", "“ta们”（未指明的评价者）", "中二男", "知乎提问者"],
   "working_keywords": ["幼态", "怕", "不怕", "女人味", "幼稚", "思考成熟度", "默认配置", "预设状态", "乡愿", "真实的勇气", "中二男", "Poetic irony"]
  },
  "notes": "正文 893 字（P001-P039）已全文读完，本篇无图片节点，故 status=read、full_text_checked=true。“你应该怕……”清单与“ta们”的看法、他人话语均属引述或代拟的他人期待，已在 main_claims 中标为 quoted_or_cited／对应 attribution，不归给作者；提问字段属提问者。文末“说不怕，不是叫你啥都不怕”是对开篇答案的自我限定，已作为 qualification 保留。"
 },
 "85aecfc3": {
  "analysis": {
   "question_context": "知乎提问（问题字段，属提问者）问“同学计划完成一个毕设展上毁坏在场所有毕设的行为艺术，是否应该劝说他放弃？”。作者未直接回答“是否劝说”，也未评价该计划本身，而是给出两个可供提问者采用的替代方案（联合同学做“追着打”的行为艺术；在各作品前装摄像头录下破坏的慢动作）并分别拟定作品名。提问者所述计划属提问者说法，作者未予确认或反驳。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "建议联合其他同学一起完成一个“追着打”的行为艺术，并提出可命名为《群像 • 破坏着破坏着的破坏者的破坏者》。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "另一方案：在每个作品前都装上摄像头、录下破坏的慢动作，命名为《被凝视的毁灭者》。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者建议提问者联合其他同学一起完成一个“追着打”的行为艺术，并提出可命名为《群像 • 破坏着破坏着的破坏者的破坏者》。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出另一可选方案：在每个作品前都装上摄像头，录下破坏的慢动作，命名为《被凝视的毁灭者》。", "evidence": ["E3", "E4"]}
   ],
   "argument_steps": [
    "作者未回答“是否应该劝说他放弃”，也未论证该计划是否可行或应否阻止（全文未涉及）。",
    "直接给出可选方案一：联合其他同学做一个“追着打”的行为艺术，并用破折号引出拟定的作品名（P001-P003）。",
    "给出可选方案二：在每个作品前装摄像头录下破坏的慢动作，并拟定作品名（P004-P005）。"
   ],
   "concept_usage": [
    {"term": "行为艺术", "meaning": "作者把提问者所述的破坏计划当作可用行为艺术回应的场景，未给定义。", "evidence": "P001", "ambiguity": "未说明何种行为可算行为艺术。"},
    {"term": "追着打的行为艺术", "meaning": "作者提议的反制形式，具体做法与是否字面暴力未说明。", "evidence": "P001", "ambiguity": "是字面暴力还是比喻，本文未交代。"},
    {"term": "破坏者", "meaning": "以书名号标题层层嵌套的方式命名（破坏着破坏着的破坏者的破坏者）。", "evidence": "P003", "ambiguity": "标题的所指层次未作解释。"},
    {"term": "被凝视的毁灭者", "meaning": "以摄像头记录破坏者所形成的凝视关系的命名。", "evidence": "P005", "ambiguity": "作者未展开该命名的用意。"}
   ],
   "examples_and_targets": [
    "《群像 • 破坏着破坏着的破坏者的破坏者》：作者拟定的作品名（修辞材料，P003）。",
    "《被凝视的毁灭者》：作者拟定的作品名（修辞材料，P005）。",
    "“摄像头”“慢动作”：方案中的具体手段（行动建议的组成部分，P004）。",
    "回应对象：提问者所述“同学计划毁坏在场所有毕设”的计划（提问者说法，作者未评价）。"
   ],
   "conditions": [
    "两个方案均以“你可以……”“又或者……”提出，是可选建议而非要求。",
    "未说明方案的可行性、成本、是否会被视为报复或导致冲突升级、是否涉及校规或法律责任。",
    "“其他同学”“每个作品前”的范围与数量未明确。",
    "正文未涉及该计划是否已实施或是否已被劝阻。"
   ],
   "rhetoric_and_tone": "全文极简（90 字），不回答是非问，而以两个反制性方案回应提问，带戏谑与反讽意味。用破折号引出拟名，用书名号呈现两个层层嵌套的作品标题；“追着打”“被凝视的毁灭者”等措辞带有以暴制暴式的玩笑色彩，作者未说明是否当真，也未给任何论证或评价。",
   "unresolved_questions": [
    "作者未明确回答“是否应该劝说他放弃”这一是非问题。",
    "两个方案的可行性、后果与是否认真未说明；“追着打”是字面还是比喻不明。",
    "未提及提问者同学的计划是否已被劝阻、是否涉及校规或法律后果。",
    "正文仅 90 字，无图片节点；是否存在其他补充内容（如评论区）本文未说明。",
    "“同学计划毁坏在场所有毕设”属提问者说法，未获作者确认，不得当作已核实事实。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你可以联合其他同学一起完成一个追着打的行为艺术——", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "《群像 • 破坏着破坏着的破坏者的破坏者》", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "又或者，在每个作品前都装上摄像头，录下破坏的慢动作：", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "《被凝视的毁灭者》", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术（行为艺术／毕业设计展）", "校园冲突与回应策略"],
   "issue_candidates": ["破坏性行为艺术如何应对", "以创作反制破坏", "凝视与记录", "是否劝阻同学"],
   "text_function_candidates": ["答疑（未直接回答）", "建议与调侃", "反讽"],
   "object_candidates": ["提问者的同学", "毕设展", "其他同学", "摄像头"],
   "working_keywords": ["行为艺术", "追着打", "群像", "破坏者", "被凝视的毁灭者", "摄像头", "慢动作", "毕设展"]
  },
  "notes": "正文 90 字（P001-P005）已全文读完，本篇无图片节点，故 status=read、full_text_checked=true。本篇为极短答／调侃式建议：作者未直接回答“是否劝说他放弃”，只给出两个替代方案；提问者所述事实与作者主张已分开标注，作者未对该计划作任何评价或事实确认。"
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
