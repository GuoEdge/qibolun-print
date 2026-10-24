# -*- coding: utf-8 -*-
"""批次 r001-b0051 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0051.sessions.py            # 写 out/r001-b0051.out.jsonl
  python3 records/r001-b0051.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0051"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0051.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "c34ca81a": {
  "analysis": {
   "question_context": "提问者问「人类知道世界的终极真理后会疯掉吗?」（Q001，属提问者，仅见提问字段，正文段落不含该句）。作者没有沿用「知道之后疯掉」的预设，而把它改写为「人类会在知道终极真理之前疯掉」（P001），全文围绕这个改写分两层论证：先论语言与概念无法支撑对真理的完全描述，再论即便拥有完全描述也无法验证；随后重新定义「终极真理」，推出它非人类所能承受，末段把决策重述为赌注。篇末标「（未完，待续）」（P097）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "对提问的总回答：人会在知道终极真理之前疯掉。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "以幼儿园小朋友学会写E=MC^2为假设情形，论仅掌握记法而无概念理解不算掌握。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "追问「掌握M」的过关标准；定义会引入新概念，层层分解不可能无限，出现循环自指与互为注释，整个描述系统近似「概念乌托邦」。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "以查身份证为比喻：概念互相交叉担保却无凭证，「道德」「正义」被点名为无证的担保者。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019"], "summary": "第一层论证收束，转入第二层。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022"], "summary": "假设语言问题已被解决、人真的拥有并理解真理的完全描述，追问如何确认这是真货。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "以「最完美操作系统的全部源代码」为思想实验，连续反问：测试样例、单元测试、横向比较、bug与特性、代价、恒久稳定、穷举出错、意外结果，以及「一切的答案不是42」。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P036", "P037", "P038"], "summary": "无法验证完美性就不能宣布其为终极完美；应先证实再宣布。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "给出「终极真理」定义及其真理性、终极性两个鉴定条件。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "由两条件推出：运用它需无穷算力，等于要求全知全能；人类不可能承受，超载表现为存储与运算的「无限卡顿」。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062"], "summary": "提出「减配命题」：拿掉完整性要求，只要求对一件前提非常确切的事百分之百准确预测；作者先让步答「可以」。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "以三米自由落体说明「确切的事情」与「正确的预测」都不成立、近似被无视；局部终极真理组合越多越不可靠，中长期预测近乎无效。", "role": "reason"},
    {"unit_id": "U013", "paragraph_refs": ["P071", "P072", "P073", "P074", "P075", "P076", "P077"], "summary": "以「3是1的3倍」为例：数学命题的必然性来自它存在于被创造的私有世界，共识不能反向约束现实世界。", "role": "example"},
    {"unit_id": "U014", "paragraph_refs": ["P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087"], "summary": "回到原点：终极真理不可知晓、不可讲述、无力验证；追问决策依据是什么，承认会随时落空，远期预测不可靠。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096"], "summary": "决策实为赌注；把赌注加冕为真理会产生信念互斥与除异己的后果，被指为人类一切苦难的根源。", "role": "conclusion"},
    {"unit_id": "U016", "paragraph_refs": ["P097"], "summary": "篇末标注「（未完，待续）」。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类会在知道终极真理之前疯掉（对提问预设的改写式回答）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "在作者自设的假设下：若幼儿园小朋友不能理解公式中的符号，仅掌握E=MC^2的记法没有意义。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "概念定义的层层分解不可能是无限的，因为人类语言容量有限；分解过程中会出现大量循环自指、互为注释。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "整个看似精妙的描述系统近乎一个「概念乌托邦」：概念互相交叉担保，却大多来历不明、拿不出凭证。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "「会背M的定义就是过关条件」这一判断被作者明确否弃（未点名的一般做法）。", "evidence": ["E3"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在假设语言问题已解决、人真的拥有并理解真理的完全描述之后，仍无法确认手里的是否真货。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以一连串反问指出：无法验证答案的完美性就不能宣布其为「终极完美」，应当证实之后才能宣布。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「终极真理」被定义为对事物及事物之间关系的最终正确理解，含真理性与终极性两个鉴定条件。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按此定义，终极真理显然不是为人类准备的概念。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果终极真理存在且其定义不打折扣，则运用它需要无穷算力，等于要求运用者全知且全能；人类不可能全知全能，故承受不起。", "evidence": ["E16", "E17", "E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即便拿掉完整性要求、只要求对一件前提非常确切的事作百分百准确预测，仍然有问题：所谓「确切的事情」与「正确的预测」都不成立，只是差异与精度要求被忽略。", "evidence": ["E20", "E21", "E23", "E24"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "局部终极真理的微小误差在组合与重复中累积，组合越多越不值得信任；人生与命运所涉近似真理数量惊人，其中长期预测近乎完全无效。", "evidence": ["E25", "E26"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们之所以觉得那些算真理，更大原因是考虑它们时人在考试或实验室里，是教育期导致的错觉效应。", "evidence": ["E27"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "「3是1的3倍」在被创造的私有世界里是终极真理，却不因此在现实世界同样是终极真理；私有世界的共识不能反向约束现实世界。", "evidence": ["E28", "E29"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "终极真理既不可能知晓、不可能讲述、无能力验证，连一个碎片也无力抓住。", "evidence": ["E30"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何具体的远期预测都不可靠；只要人还是有限的人而不是无限的上帝，技术与算力的发展都无法改变这一点。", "evidence": ["E31", "E32"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在没有终极真理可依靠的情况下，人的决策实质是赌注——最聪明、最有胜算、最值得一搏的赌注。", "evidence": ["E34"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们因害怕面对「我的决策全是赌注」而把所信之物宣布为终极真理，副作用是信念之间出现唯我独尊、你死我活的互斥性。", "evidence": ["E35", "E36"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "承认自己的选择只是赌注，就不会认为对方必错，也不会简单认为对方对自己的否定有绝对效力。", "evidence": ["E37"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若因无法忍受自己的选择只是赌注而将其加冕为真理，则凡不肯认错的异见者都被视为威胁，作者说「我必先除之而后安枕」，并称这是人类一切苦难的根源。", "evidence": ["E38", "E39"]},
    {"claim_id": "C021", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问法是「人类知道世界的终极真理后会疯掉吗?」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []},
    {"claim_id": "C022", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "篇末只以「赌注」回答「我们做出决策所依靠的东西是什么」，其是否充分、后续如何展开，本篇止于「（未完，待续）」（P097 仅 7 字，不满足短引长度，故本条不附短引）。", "evidence": []}
   ],
   "argument_steps": [
    "开篇改写提问：从「知道终极真理之后疯掉」改为「知道终极真理之前疯掉」。",
    "以幼儿园小朋友学会写E=MC^2的假设，区分记法与理解。",
    "追问「掌握M」的达标标准，推出定义链会循环自指，并受语言容量限制。",
    "以查身份证比喻概念互相担保却无凭证；称此为「论证一」。",
    "第二层：假设语言问题已解决、已获得真理的完全描述，追问如何验证真伪。",
    "以「最完美操作系统的全部源代码」思想实验列举验证难题（测试、基准、bug与特性、代价、稳定性、穷举、意外结果）。",
    "小结：不能验证就不能宣布，应先证实。",
    "正式定义终极真理：真理性＋终极性两条鉴定标准。",
    "由定义推出运用它需无穷算力→须全知全能→人类承受不起；超载表现为「无限卡顿」。",
    "让步：提出减配命题，只要求对确切事情100%预测，作者先承认「那当然可以」。",
    "以三米自由落体反驳「确切的事情」与「正确预测」，指出近似被有意无意无视。",
    "推论：误差组合累积，局部终极真理越多越不可信，中长期预测近乎无效。",
    "以「3是1的3倍」说明数学命题的必然性只在其被创造的私有世界内成立。",
    "回到原点：终极真理不可得；追问决策依据，自答会随时落空、远期预测不可靠。",
    "结论：决策是赌注；把赌注加冕为真理会导致信念互斥与除异己，作者称之为人类一切苦难的根源。"
   ],
   "concept_usage": [
    {"term": "终极真理", "meaning": "对事物及事物之间关系的最终正确理解，须满足真理性与终极性两个鉴定条件。", "evidence": "P041/P043/P045/P047", "ambiguity": "同篇内又出现「完整的终极真理」「局部终极真理」「减配命题」，术语范围随论证层次被作者自行收放。"},
    {"term": "真理性", "meaning": "能对任意久远未来下一刻作出正确判断，并能逆向对任意久远过去某一刻作出完全正确描述。", "evidence": "P043/P044", "ambiguity": "以「任意久远」为条件，未讨论可操作边界。"},
    {"term": "终极性", "meaning": "预测与倒推若与现实不符，必是运算者之错，绝不产生「这个版本还需要修改」的必要性。", "evidence": "P045/P046", "ambiguity": "等同「不可修改」，作者未说明它与真理性如何分别核验。"},
    {"term": "概念乌托邦", "meaning": "比喻：整个描述系统由来历不明、互相交叉担保的近亲概念构成，缺少可追溯凭证。", "evidence": "P010/P011", "ambiguity": "比喻性用语，未指明是否特指某一学说或某一学派。"},
    {"term": "全知／全能", "meaning": "知道一切事物的状态即全知；能做不必验算即绝对无误的运算即全能。", "evidence": "P052/P053", "ambiguity": "作者以「本质上」限定全能。"},
    {"term": "局部终极真理", "meaning": "被拿掉完整性要求、只对某类确切事情作百分之百预测的「真理」。", "evidence": "P060/P061/P068", "ambiguity": "作者先让步承认「那当然可以」（P062），随后又指其组合不可靠（P068）。"},
    {"term": "赌注", "meaning": "在没有任何终极真理碎片可依靠时，决策的实质。", "evidence": "P088/P089/P090", "ambiguity": "未说明不同赌注之间如何比较胜算。"}
   ],
   "examples_and_targets": [
    "幼儿园小朋友学写E=MC^2（P003–P005）：作者自设假设例证，用来说明记法不等于理解。",
    "查身份证／暂住证／介绍信场景（P011–P015）：作者比喻；「康德康八爷」介绍信、「道德」「正义」被点名为无证担保者，属修辞与讽刺对象，非外部事实主张。",
    "「最完美的操作系统的全部源代码」硬盘（P024）：作者思想实验。",
    "「一切的答案不是42」（P035）：文化典故式修辞，出处本篇未说明，待外部核查。",
    "特朗普（P038）、老格瓦拉（P014）：修辞材料。",
    "三米高处自由落体小球（P061、P065–P066）：作者例证，用月球与太阳引力、地球潮汐说明误差不可避免。",
    "「3是1的3倍」（P071–P076）：作者思想实验，用私有世界／平行世界论证数学命题必然性的范围。",
    "高考物理满分（P021）：类比。",
    "程序员（P023）：修辞性铺垫。"
   ],
   "conditions": [
    "「如果这位小朋友不能理解M、C、E、^甚至2是什么」——记法无意义的前提（P005）。",
    "「假设，在大脑安装了某种神秘的强大插件之后，语言的问题解决了」——第二层论证的假设前提（P020）。",
    "「如果它存在，则运用它去顺推也罢、倒推也罢，需要的算力是无穷的」（P051）。",
    "「如果我们一丝一毫也不打折的遵从其定义」——推出必须全知全能的附加条件（P053）。",
    "「假设我们把终极真理的『完整性要求』从终极的含义里拿掉」——减配命题的假设（P060）。",
    "「只要这种预测的正确率能达到100%」——让步时设定的合格线（P061）。",
    "「只要人还是有限的人而不是无限的上帝」——远期预测不可靠无法改变的条件（P087）。",
    "「我若因为无法忍受我的选择只是赌注……而加冕它为真理」——P095 后果推论的条件。"
   ],
   "rhetoric_and_tone": "口语化、粗俗比喻与密集反问并用；以「你」「我们」直接称呼读者，兼有调侃（程序员、特朗普、老格瓦拉）、拟人化讽刺（概念互相递烟担保）与夸张（地球还没炸就该宰牛还神）。结构上按「论证一」「第二层」「减配命题」分层，严肃定义（P039–P047）夹在戏谑段落之间；结尾由戏谑转为断言式的沉重（P096）。",
   "unresolved_questions": [
    "本篇以「（未完，待续）」结束（P097），后续论证未在本篇出现；「我们做出决策所依靠的东西是什么」只以「赌注」作答，作者未说明该回答是否充分。",
    "提问者问「会疯掉吗」，作者改答「会在知道终极真理之前疯掉」；「疯掉」的确切含义（字面精神失常还是比喻）本文未界定。",
    "P035「一切的答案不是42」为外部文化指涉，出处与含义需外部核查。",
    "「人类语言的容量是有限的」（P008）未给依据或量化，属待外部核查的事实断言。",
    "「概念乌托邦」是否指特定他人学说，本文未点名。",
    "「局部终极真理」在 P062 被承认、在 P068 被削弱，作者未正面调和两处语气。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人类会在知道终极真理之前疯掉。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "那么仅仅掌握这个公式的记法是没有意义的", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "认为“会背M的定义”就是过关条件", "relation": "contradicts"},
    {"key": "E4", "paragraph_id": "P008", "quote": "这种层层分解显然不可能是无限的，因为我们人类的语言的容量是有限的", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "我们很快会发现有大量的循环自指，互为注释", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "几乎完全是一个“概念乌托邦”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "一个有身份证的都没有，全部都是暂住证", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P020", "quote": "你真的拥有了真理的完全描述", "relation": "context"},
    {"key": "E9", "paragraph_id": "P024", "quote": "这就是最完美的操作系统的全部源代码，一字不多，一字不少，一字不错", "relation": "context"},
    {"key": "E10", "paragraph_id": "P036", "quote": "如果你无法验证答案的完美性，你怎么确定你所拿到的答案是“终极完美”的呢？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P037", "quote": "难道不该是证实了之后才能宣布吗？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P041", "quote": "对事物及事物之间的关系的最终正确理解", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P043", "quote": "第一，依据这一理解可以对任意久远的未来下一刻作出正确的判断", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P045", "quote": "只要还有任何合理的需要修改这一理解的必要性浮现，这个理解就并不能称其为终极的", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P050", "quote": "它显然不是为人类准备的概念。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P051", "quote": "如果它存在，则运用它去顺推也罢、倒推也罢，需要的算力是无穷的", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P052", "quote": "知道一切事物的状态，即为全知", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P053", "quote": "则唯一能有效理解和运用它的事物就必然要全知且全能", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P054", "quote": "我们人类显然不可能全知，也没有全能", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P060", "quote": "假设我们把终极真理的“完整性要求”从终极的含义里拿掉呢？", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P061", "quote": "只要这种预测的正确率能达到100%，我们就将其称其为一条终极真理", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P065", "quote": "你从来就没有真正的从绝对准确的三米高处释放小球", "relation": "contradicts"},
    {"key": "E24", "paragraph_id": "P066", "quote": "那事情并不确定，只是因为你忽略了每一次之间的差异", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P068", "quote": "组合、重复得越多，越不值得信任。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P069", "quote": "那他们的组合所形成的中长期预测近乎于是完全无效的", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P070", "quote": "这不过是教育期所导致的错觉效应罢了。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P074", "quote": "你的意愿不改，这一命题在那个世界里当然就是终极真理。", "relation": "qualifies"},
    {"key": "E29", "paragraph_id": "P076", "quote": "但我们的共识并不能反向的对这个现实世界发生约束。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P079", "quote": "既不可能知晓、也不可能讲述、也无能力验证", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P086", "quote": "因此任何具体的远期预测都是不可靠的。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P087", "quote": "只要人还是有限的人而不是无限的上帝，就永远无法改变。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P090", "quote": "最聪明、最有胜算、最值得一搏的赌注而已。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P091", "quote": "人们害怕面对“我的决策全是赌注”这一事实", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P092", "quote": "不同的信念之间出现了唯我独尊，你死我活的互斥性。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P093", "quote": "我却不会认为你的必错", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P095", "quote": "我必先除之而后安枕。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P096", "quote": "这就是人类一切苦难的根源。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["哲学认识论", "科学哲学", "真理理论", "决策与风险"],
   "issue_candidates": ["终极真理是否可能", "概念定义的循环与无穷倒退", "验证与证实问题", "预测误差累积", "信念冲突与互斥"],
   "text_function_candidates": ["答疑", "论辩", "思辨随笔", "系列长文（未完待续）"],
   "object_candidates": ["康德", "特朗普", "格瓦拉", "《银河系漫游指南》的42", "程序员", "人类／上帝"],
   "working_keywords": ["终极真理", "真理性", "终极性", "概念乌托邦", "局部终极真理", "减配命题", "全知", "全能", "赌注"]
  },
  "notes": "brief 与正文前五段（P001–P005，含分隔线）几乎逐字重复，仅作导航，未据 brief 支持任何主张。提问字段（Q001）不在本记录 paragraphs 中，故提问者主张 C021 无段落短引。P002 为分隔线「——————」，已按结构原样保留在 structure 中，未单列内容单元。P062「那当然可以啊。」（7 字）、P089「是赌注而已。」（6 字）、P097「（未完，待续）」（7 字）三段短于 10 字，未单列 evidence 短引；相关让步（P062）与结尾标记（P097）已在 C011、C022 的 statement 中说明。E38 短引含句末句号以凑足 10 字。全文无图片节点。"
 },
 "09ac8a44": {
  "analysis": {
   "question_context": "提问者问「用力顶住要倒的架子，为什么我没有做功却非常累？」（Q001，属提问者；「我没有做功」是提问者的前提，未自动归给作者）。作者用一整篇比喻解释肌肉如何维持用力：肌节内的肌球蛋白不断拽动很滑的肌动蛋白，从而在长度不变的情况下持续做功并持续耗能（P005–P011）。作者既没有使用「等长收缩」这类术语，也没有解释「累」的主观感受机制。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "交代结构层次：肌肉—肌纤维—肌节；肌节收缩由肌球蛋白与肌动蛋白合作完成。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "把肌节比作橡胶火车车厢（更像涨鼓鼓的长气球），肌动蛋白是两根涂油的绳子，肌球蛋白是背靠背拽绳的两人。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "绳子很滑：想拽住不动就会滑出去，只有不停往怀里拽才能动态维持拉力；一停手绳子就往外滑。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "车厢保持缩短长度不变，是因为肌球蛋白一直在对肌动蛋白做功，靠动能转化为摩擦热能维持拉力；作者断言「功做在这了」。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "拽绳动作靠消耗ATP产生的化学能，整个过程是化学能向热能的转化以维持运动上的平衡态。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011"], "summary": "结论：虽无宏观运动状态变化，却存在微观能量转移；并非看起来静止就没有能量转移。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P012"], "summary": "分隔线「———」。", "role": "other"},
    {"unit_id": "U008", "paragraph_refs": ["P013"], "summary": "元评论：本篇以纯文字完成说明，作者自称「无图说明成就达成」。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "肌肉由肌肉纤维构成，肌肉纤维由大量肌节首尾相接连成；肌肉收缩主要依靠每一个肌节的收缩。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "肌节的收缩由肌球蛋白和肌动蛋白合作完成。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者用比喻说明结构：肌节像橡胶火车车厢（更像长气球），肌动蛋白是两根涂油的绳子，肌球蛋白像背靠背腰捆在一起拽绳的两个人。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绳子很滑，想拽住不动就会滑出去，只有不停往怀里拽才能动态维持对绳子的拉拽力；一停手绳子立刻往外滑。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "车厢维持在缩短后的长度不变，是因为肌球蛋白一直在对肌动蛋白做功，靠动能转化成摩擦热能维持拉力。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "肌球蛋白拽绳靠消耗三磷酸腺苷（ATP）产生的化学能；总体上这是靠化学能对热能的转化来维持运动上的平衡态的过程。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "并非看起来静止不动就没有能量转移：没有宏观运动状态变化，但仍存在微观上的能量转移。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者以「功做在这了」回应提问者「没有做功」的前提，指持续维持拉力的位置正是做功之处。", "evidence": ["E7", "E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本篇是作者自述的「无图说明」——不配图完成解释。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者的前提是「用力顶住要倒的架子却没有做功却非常累」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "先给结构：肌肉→肌纤维→肌节；肌节收缩由肌球蛋白与肌动蛋白合作。",
    "用火车车厢／长气球＋涂油绳子＋两人拽绳的比喻把分子过程具象化。",
    "强调绳子滑：拽住不动会滑出去，必须不停往怀里拽才能动态维持拉力。",
    "在外人看来车厢只是变短后维持不变，内部却必须持续拽绳。",
    "断言此处一直在做功，靠动能转化为摩擦热能维持拉力——即「功做在这了」。",
    "补充能量来源：ATP产生的化学能，整体是化学能→热能的转化以维持运动上的平衡态。",
    "结论：没有宏观运动变化不等于没有能量转移，微观上存在能量转移。",
    "以分隔线和「无图说明成就达成」收尾。"
   ],
   "concept_usage": [
    {"term": "肌节", "meaning": "肌肉收缩的基本单位，大量肌节首尾相接连成肌肉纤维。", "evidence": "P001/P002", "ambiguity": "未给出尺度或结构细节。"},
    {"term": "做功", "meaning": "本文指维持拉力时持续进行的能量转化（动能→摩擦热能；ATP化学能→热能），不要求宏观位移。", "evidence": "P007/P008/P009", "ambiguity": "作者未给出物理学的功定义，也未处理「没有位移是否做功」这一提法本身。"},
    {"term": "动态的维持", "meaning": "长度不变的状态必须靠不停拽动才能保持，一停就滑回。", "evidence": "P005/P006", "ambiguity": "未命名对应的生理学状态。"},
    {"term": "运动上的平衡态", "meaning": "靠化学能对热能的转化所维持的、宏观不变化的状态。", "evidence": "P009", "ambiguity": "「平衡态」在此为描述性用法，未定义。"}
   ],
   "examples_and_targets": [
    "橡胶火车车厢／涨鼓鼓的长气球（P003）：作者自设比喻。",
    "你和朋友背靠背腰捆在一起拽两根涂油绳子（P003–P006）：同一比喻的展开，含「列车长喊一声快拉」（P004）。",
    "三磷酸腺苷（ATP）（P009）：作者作为能量来源的陈述，属事实断言，未被外部核验。",
    "「无图说明」成就达成，撒花！（P013）：元叙事，说明本篇未配图。"
   ],
   "conditions": [
    "「只有不停的往怀里拽，才能动态的维持对这根绳子的拉拽力」（P005）——维持拉力的必要条件。",
    "「你们要是一停手，绳子立马从手里往外滑」（P006）——停止做功的后果。"
   ],
   "rhetoric_and_tone": "科普口吻，第二人称「你」把读者代入车厢情境；大量口语与拟人（「该死的绳子」「苦不堪言」「列车长喊一声」），用比喻代替配图；结尾以「成就达成，撒花！」自嘲式收束。",
   "unresolved_questions": [
    "提问者问「为什么会非常累」，作者只解释了持续做功与持续耗能，未说明疲劳感本身的产生机制。",
    "作者没有使用任何术语为「用力顶住不动」这一状态命名。",
    "肌球蛋白／肌动蛋白／ATP等属作者的事实陈述，本篇未给文献或数据，如需核准需外部核查。",
    "P012 分隔线与 P013 的元评论与题目关系，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你的肌肉是由无数根肌肉纤维构成，肌肉纤维则是由大量的肌节首尾相接连成", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "而肌节的收缩，由肌球蛋白和肌动蛋白来合作完成。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你可以把肌节想象成一个橡胶做成的火车车厢", "relation": "context"},
    {"key": "E4", "paragraph_id": "P003", "quote": "而肌球蛋白就好像你和你的朋友背靠背腰捆在一起站在车厢中间", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "只有不停的往怀里拽，才能动态的维持对这根绳子的拉拽力。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你们要是一停手，绳子立马从手里往外滑。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "是因为你们（肌球蛋白）一直在对这两根滑溜溜的绳子（肌动蛋白）做功", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "靠着你们身体的动能转化成双手摩擦绳子的热能，维持住了那个拉力", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "靠的是消耗三磷酸腺苷（ATP）而产生的化学能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "这是一个靠着化学能对热能的转化来维持一种运动上的平衡态的过程", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "尽管看起来没有发生宏观的运动状态的变化，但是却存在微观上的能量转移。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "并不是看起来静止不动，就没有能量转移的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "“无图说明”成就达成，撒花！", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生理学", "生物物理", "科普"],
   "issue_candidates": ["静力性用力为何仍耗能", "肌肉收缩的分子机制", "做功与能量转化"],
   "text_function_candidates": ["答疑", "科普解释", "打比方讲解"],
   "object_candidates": ["肌节", "肌球蛋白", "肌动蛋白", "三磷酸腺苷（ATP）", "肌肉纤维"],
   "working_keywords": ["肌节", "肌球蛋白", "肌动蛋白", "ATP", "动态的维持", "做功", "微观上的能量转移", "运动上的平衡态"]
  },
  "notes": "brief 与正文前两段重复且末尾被截断（止于「肌动蛋白是两根分别系在车厢两头的涂了油的绳子」），仅作导航。提问者的前提「我没有做功」（Q001）未归给作者；作者的回应见 P007–P008。正文的 P001 段落文本在记录中完整，无截断。本篇无图片节点，但 P013 为「无图说明」元评论，已单列。P012 为分隔线「———」。"
 },
 "8ea0b86e": {
  "analysis": {
   "question_context": "提问者描述自己的玩法（买弓箭、把鸡围起来射死、独自找没人的地方玩），问「我道德吗？」（Q001，属提问者）。作者没有直接回答是或否，而是先确立一套道德判据：道德不取决于个人观点而取决于认同者的客观可持续性，道德律是客观的、被决定的，人只能去参悟（P001–P025）；随后把提问情境改写为一个可判断的问题——赞赏或认可【杀生取乐】的群体是否更有竞争力（P028），并说答案决定应然，但本篇未给出该答案。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "道德与不道德不取决于任何单个人的个人观点，而取决于认同者的客观可持续性。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "以违约谋生为假设例证：合作者受损、人们绕着走、活不下去；若公司全员同意则成本高、无竞争力、破产。写书、呼喊权利、百万人点赞都无用。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "道德不能依靠共识来定义；决定道德的最终权柄不在人类手中，全民公决也不行。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "假设全体投票一致同意「故意违约不应被视为道德问题」并贯彻，结果会是集体灭亡。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "人只能根据客观事实、自然规律思考道德观；猜中才有机会活下去，没猜中倒霉几率更大，属缓刑期；劝其早日醒悟没有选择道德观的自由。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "以万有引力类比：没有权利相信它不存在；思想自由指没有人类有权说你不对话，不等于自然界无权否决；自然界有绝对的惩罚权。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "道德律是绝对的、不以人的观点为转移；人的立场只是参悟，不是选择或决定。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019", "P020"], "summary": "反驳「你有你的道德，我有我的道德」：该说法逻辑上不成立，通顺版本是「你有你的道德观」；可拥有的是道德观，不是道德律。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "道德律是自然（或造物主）的所有物；如光如何传播一般不由你的观点决定；猜对是绝对义务。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P025", "P026", "P027"], "summary": "确立探讨道德问题的前提，并回到提问。", "role": "transition"},
    {"unit_id": "U011", "paragraph_refs": ["P028", "P029", "P030"], "summary": "把情境改写为竞争力问题：认可【杀生取乐】的群体是否更有竞争力、能否以更低合作成本出产更优质产品；答案对应然有决定作用，与点赞数量无关。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P031", "P032", "P033"], "summary": "若答案为否，点赞者无论多少都只是同在死缓判决里的狱友；决定道德律者不为人数所动。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道德与不道德并不取决于任何单个人的个人观点，而取决于认同者的客观可持续性。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以违约为谋生策略会导致合作者蒙受损失，进而使人们绕着此人走，最终使其活不下去。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果公司全体成员都同意该做法，会出现大量内部合作上的无效成本，产品成本与售价过高、失去竞争力，最后整个公司破产。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "写书论证该法则为什么道德、呼喊「我有权利选择自己的道德观」、拉上百万人在网上点赞，都没有实际意义。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "道德并不是可以依靠共识来定义的事物。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "决定道德的最终权柄根本不在人类手中，哪怕是全体人类全民公决也不行。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果全体投票一致同意「故意违约不应被视为道德问题」并且真的去贯彻，结果会是集体灭亡。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人只能根据客观事实、自然规律去思考自己的道德观。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "猜中结果才「有权」保留自己的猜测（有机会按猜测活下去）；没猜中则客观上倒霉几率更大，作者称之为缓刑期。", "evidence": ["E8", "E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人其实没有自己选择道德观的自由；若一直高喊相反说法执迷不悟，最后命运会亲自来教他做人。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "以万有引力为类比：人没有权利相信该定律不存在，一次没摔死不表示主张对，这不属于「思想自由」的覆盖范围。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "思想自由是指没有什么人类有权利说你不对，而不是说自然界（含社会在内的广义自然界）没资格否决你。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然界有无限的、绝对的、不容任何质疑的权利，随时随地以祂高兴的方式惩罚人。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道德律是绝对的，是不以人的观点为转移的。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对于道德唯一可选的立场是去参悟，而不是去选择、去决定；道德律已经被决定，人只需探索被决定的版本是什么。", "evidence": ["E15", "E16"]},
    {"claim_id": "C016", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "「你有你的道德，我有我的道德」被作者称为愚蠢的口误，认为它在逻辑上不成立（未点名的流行说法）。", "evidence": ["E17"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该句的逻辑通顺版本是「你有你的道德观（对客观道德的观点），我有我的道德观」。", "evidence": ["E18"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人有权拥有的是关于那个客观事实的观点，而不是那个客观事实；道德观可以拥有，道德律不可以。", "evidence": ["E19"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道德律是自然（或造物主）的所有物。", "evidence": ["E20"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以光如何传播作类比：人对它有观点，与它实际如何传播无关；光不会因人不那样猜就按人的主张来传播。", "evidence": ["E21", "E22"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「猜对」对人是一种绝对义务。", "evidence": ["E23"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「道德是绝对的、客观的、不受我决定的，我的任务是去认识它、发现它」是探讨一切道德问题的前提。", "evidence": ["E24"]},
    {"claim_id": "C023", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者把提问情境改写为问题：一个赞赏或认可【杀生取乐】的群体有更强的竞争力吗？这有利于ta们以更低的合作成本出产更优质的服务和产品吗？", "evidence": ["E25"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是这个（竞争力）答案决定了这样做到底是不是道德的（应然的），而不是由有多少人给你点赞决定。", "evidence": ["E26", "E27"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果那答案是否，则所有给你点赞的人，无论有多少，只是与你同在死缓判决里的狱友。", "evidence": ["E28"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "决定道德律的那一位心硬如铁，多少人头摆在眼前也不会眨眼。", "evidence": ["E30"]},
    {"claim_id": "C027", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「我想买个弓箭，买几只鸡，把它们围一起，用箭射死它们，我只自己找个没人地方玩，我道德吗？」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "先立判据：道德取决于认同者的客观可持续性，而非个人观点。",
    "以违约谋生为例，推出合作者受损→被绕开→活不下去的结果链。",
    "把例证放大到公司全体同意的情形，推出内部成本升高、竞争力丧失、破产。",
    "否定写书论证、宣称权利与网络点赞的作用。",
    "断言道德不能由共识定义，决定权柄不在人类手中（全民公决也不行）。",
    "假设全体投票同意「违约不是道德问题」并贯彻，推出集体灭亡。",
    "提出人只能依客观事实与自然规律思考道德观；区分猜中（缓刑期）与没猜中（倒霉几率更大）。",
    "劝告对方醒悟没有选择道德观的自由。",
    "以万有引力与思想自由的边界说明自然界具有否决权，且其权利绝对。",
    "正面命题：道德律绝对、不以人的观点为转移，人只能参悟。",
    "反驳「你有你的道德，我有我的道德」，改述为「道德观」并区分道德观与道德律。",
    "以光如何传播作类比，得出「猜对是绝对义务」。",
    "确立前提后回到提问，把情境改写为竞争力问题，并称答案决定应然、与点赞数无关。",
    "结论：若答案为否，点赞者只是同在死缓判决里的狱友；决定者不为人数所动。"
   ],
   "concept_usage": [
    {"term": "道德／道德观／道德律", "meaning": "道德（律）是客观的、已被决定的、自然（或造物主）的所有物；道德观是个人对客观道德的观点，是人可以拥有的东西。", "evidence": "P019/P020/P021", "ambiguity": "作者对「道德」与「道德律」常混用；P015 用「道德律」，P001 用「道德」。"},
    {"term": "客观可持续性", "meaning": "判定道德与不道德的依据，指认同者能否在客观上持续存续。", "evidence": "P001/P002/P003", "ambiguity": "未给出界定方式或测量标准。"},
    {"term": "思想自由", "meaning": "指没有什么人类有权利说你不对；不等于自然界没有资格否决你。", "evidence": "P013", "ambiguity": "作者自注「自然界」为包括社会在内的广义自然界。"},
    {"term": "缓刑期／死缓判决", "meaning": "比喻：未猜中者只是暂时未受罚，判决已在，倒霉几率更大。", "evidence": "P010/P031", "ambiguity": "比喻性用法，未对应任何制度或机制。"},
    {"term": "应然的", "meaning": "与「这样做到底是不是道德的」对应，由竞争力答案决定。", "evidence": "P029", "ambiguity": "作者未展开实然与应然的关系。"},
    {"term": "那一位", "meaning": "指决定道德律者；P021 写作「自然（或造物主）」。", "evidence": "P021/P033", "ambiguity": "主体未明确指定为神、自然或别的存在。"}
   ],
   "examples_and_targets": [
    "「某人认为违约是重要的谋生策略」（P002）：作者自设假设例证。",
    "公司全体成员同意违约做法→破产（P003）：作者推演例证。",
    "「写一本一千多万字的书」「大呼『我有权利选择自己的道德观』」「拉着一百多万人在网上给你点赞」（P004）：作者讽刺的做法，未点名具体人或事件，待外部核查是否指涉特定争论。",
    "万有引力定律（P012）：类比。",
    "光是如何传播的（P022–P023）：类比。",
    "赞赏或认可【杀生取乐】的群体（P028）：与提问情境对应的例证。",
    "「你有你的道德，我有我的道德」（P018）：被反驳的说法。"
   ],
   "conditions": [
    "「如果是一个公司里的全体成员都同意这个做法」（P003）。",
    "「如果我们全体投票一致同意……并且我们也去贯彻它」（P007）。",
    "「你猜中了结果」／「你要是没猜中」（P009／P010）——两种结果分支。",
    "「你要是一直高喊这种废话执迷不悟」（P011）。",
    "「一次没摔死不表示你的主张是对的」（P012）。",
    "「站在这个前提下看待这个问题」（P025–P026）——讨论提问情境的前提。",
    "「如果那答案是否」（P031）。"
   ],
   "rhetoric_and_tone": "训诫式第二人称与密集反问（「看懂了吗？」「看懂没有？」各出现一次）；断言式短句成段，法律隐喻（缓刑期、死缓判决、绝对义务）；拟人与夸张（自然界「抡圆了抽你」、「那一位心硬如铁」）；对论辩对手语气粗直（「愚蠢的口误」「废话」）。",
   "unresolved_questions": [
    "作者未对提问者的具体行为直接给出「道德／不道德」的结论，只给出判据与「答案决定应然」的框架；P028 提出的竞争力问题，本篇没有给出答案。",
    "「客观可持续性」如何界定与测量，本文未说明。",
    "「决定道德律的那一位」主体不明确：P021 写「自然（或造物主）」，P033 只写「那一位」。",
    "P004 的「一千多万字的书」「一百多万人点赞」是否指涉特定事件或人物，未点名，待外部核查。",
    "brief 与正文前四段重复且末尾被截断（止于「如果是一个公司里的全体成员都同意这个做法，这会出」），仅作导航。",
    "本篇无图片节点。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "而取决于认同者的客观可持续性", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "接着会导致人们不能不绕着ta走，接着会导致ta活不下去", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "于是它生产出的产品成本太高，对外的售价太高，没有竞争力。最后整个公司会破产。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "拉着一百多万人在网上给你点赞也没有实际意义", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "道德并不是可以依靠共识来定义的事物", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "因为决定道德的最终权柄根本不在人类手中——哪怕是全体人类全民公决也不行", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "并且我们也去贯彻它，我们就会集体灭亡", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "人只能根据客观事实、自然规律去思考自己的道德观", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你就会客观的有更大的倒霉几率。这算缓刑期。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "你最好早点醒悟你其实没有自己选择道德观的自由", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这就像你没有权利相信万有引力定律不存在", "relation": "context"},
    {"key": "E12", "paragraph_id": "P013", "quote": "思想自由，是指没有什么人类有权利说你不对", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "自然界有无限的、绝对的、不容任何质疑的权利", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "道德律是绝对的，是不以人的观点为转移的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "人对于道德唯一可选的立场是去参悟，而不是去选择、去决定。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "它已经被决定了，你只是需要去探索被决定的版本到底是什么。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "这句话一开始就是一种愚蠢的口误，本身甚至在逻辑上不成立", "relation": "contradicts"},
    {"key": "E18", "paragraph_id": "P019", "quote": "这句话的逻辑通顺版本是“你有你的道德观（对客观道德的观点），我有我的道德观”", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "道德观才是你可以拥有的东西，道德律不是", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "道德律是自然（或造物主）的所有物。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "这就好像你可以对“光是如何传播的”有你的观点", "relation": "context"},
    {"key": "E22", "paragraph_id": "P023", "quote": "光并不会因为你不那样猜就按照你的主张来传播", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "“猜对”对你是一种绝对义务", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P025", "quote": "这是探讨一切道德问题的前提", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P028", "quote": "一个赞赏或者认可【杀生取乐】的群体有更强的竞争力吗？", "relation": "context"},
    {"key": "E26", "paragraph_id": "P029", "quote": "是这个答案决定了这样做到底是不是道德的（应然的）", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P030", "quote": "而不是由有多少人给你点赞决定。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P031", "quote": "只是与你同在死缓判决里的狱友", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P033", "quote": "决定道德律的那一位心硬如铁，多少人头摆在眼前也不会眨眼。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／道德哲学", "社会规范理论", "演化与竞争视角"],
   "issue_candidates": ["道德的客观性", "道德能否由共识定义", "思想自由的边界", "动物伦理／杀生取乐", "道德观与道德律的区分"],
   "text_function_candidates": ["答疑", "论辩", "训诫式说理"],
   "object_candidates": ["提问者（射鸡玩家）", "违约者", "公司", "自然界／造物主", "点赞的网民"],
   "working_keywords": ["客观可持续性", "道德律", "道德观", "思想自由", "广义自然界", "缓刑期", "死缓判决", "杀生取乐", "应然的"]
  },
  "notes": "brief 与正文前四段重复且末尾被截断（止于「如果是一个公司里的全体成员都同意这个做法，这会出」），仅作导航。P028 的【杀生取乐】方括号为原文格式，引文逐字保留。P032「无论多少，都一样。」仅 9 字，短于 10 字，未单列 evidence 短引；该句内容已并入 C025 的 statement，其证据由 P031 承担。本篇无图片节点。作者的「杀生取乐」为提问情境的中性改写，未直接给出该行为道德与否的结论；我未替作者补结论。"
 },
 "e7de7c32": {
  "analysis": {
   "question_context": "提问者问「这个世界真的是纯粹的唯物主义吗？」（Q001，属提问者）。作者没有直接回答，而是用一个测试样本——圆周率——连续设问：它是否客观存在、在人类出现之前与灭亡之后是否存在、是否依赖人类主观意识、其他文明是否会得到不同的圆周率（P002–P008）。全篇基本是问题链，只有两处断言（P003、P009），末段以「圆周率是不是一种『物』」收束，未给出作者的结论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "邀请读者回答一个问题。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "问圆周率是否客观存在；断言世界上没有任何圆形的物体，圆规画的圆、地球、水波纹、月球轨道都不是真正的圆形。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "追问在人类还在树上吃果子的时代或人类灭亡之后圆周率是否存在，是否依赖人类主观意识才存在。", "role": "other"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "假设人类灭绝一亿多年后老鼠进化成新人类，它们是否会得到不一样的圆周率；或数值相同而存在于另一文明的集体意识中，是否只是「与死者一模一样的新小孩」。", "role": "other"},
    {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "追问圆周率的存在性到底是客观的还是主观的。", "role": "other"},
    {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "断言圆周率没有自己的质量、动量和位置。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P010"], "summary": "追问圆周率是不是一种「物」。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上没有任何圆形的物体：圆规画的圆、地球、水波纹、月球轨道都不是真正的圆形。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "圆周率没有自己的质量、动量和位置。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者提出待答问题：圆周率是否客观存在。", "evidence": ["E3", "E10"]},
    {"claim_id": "C004", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者追问：在人类还在树上吃果子的时代，或在人类灭亡之后，圆周率是否存在；它是否实际上不存在、是依赖人类的主观意识才存在着。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "open_question", "attribution": "author", "modality": "hypothetical", "statement": "作者假设：若第一代人类灭绝一亿多年后老鼠进化成新人类，它们是否会发现一个和我们不一样的圆周率；或者数值完全一样、但存在于另一个文明的集体意识之中，它是否只是「一个与死者一模一样的新小孩」。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者追问：圆周率的存在性到底是客观的，还是主观的。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以「圆周率是不是一种『物』」收束全篇，未给出自己的答案。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「这个世界真的是纯粹的唯物主义吗？」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "以邀请读者作答开篇。",
    "把「唯物主义」之争落到一个样本上：圆周率是否客观存在。",
    "断言没有真正的圆形物体，切断「从实物抽象出来」的直觉路径。",
    "追问人类出现之前与灭亡之后圆周率是否存在。",
    "追问它是否依赖人类主观意识。",
    "假设新人类（老鼠进化）与另一文明的集体意识，追问圆周率的同一性。",
    "再次追问存在性是客观还是主观。",
    "断言圆周率没有质量、动量和位置。",
    "以「它是不是一种『物』」收尾，全篇不给结论。"
   ],
   "concept_usage": [
    {"term": "圆周率", "meaning": "本文中被用作测试「客观存在」的抽象对象样本；作者设想不同文明可能得到不同或相同的圆周率。", "evidence": "P002/P004/P006/P007", "ambiguity": "作者始终以问题形式使用，未表明自己认为它客观存在与否。"},
    {"term": "客观／主观（存在性）", "meaning": "用来追问圆周率的存在归于哪一侧。", "evidence": "P002/P005/P008", "ambiguity": "作者未界定「客观存在」的判据。"},
    {"term": "物", "meaning": "在 P009–P010 的语境中，是否具有质量、动量和位置被用作判别「物」的相关属性。", "evidence": "P009/P010", "ambiguity": "作者未明确给出「物」的定义，仅以问题收束。"},
    {"term": "唯物主义", "meaning": "仅出现在提问字段（Q001），本篇正文未使用、未界定该词。", "evidence": "Q001（提问字段，非正文段落）", "ambiguity": "正文没有回应或使用提问中的这一术语，二者关系需研究者判断。"}
   ],
   "examples_and_targets": [
    "圆规画的圆、地球、水波纹、月球轨道（P003）：作者列举并断言都不是真正的圆形。",
    "人类还在树上吃果子的时代、人类终于灭亡之后（P004）：假设性时间场景。",
    "第一代人类灭绝一亿多年以后，老鼠们进化成新人类（P006）：假设情形。",
    "「一个与死者一模一样的新小孩」、另一文明的集体意识（P007）：作者类比/假设，未展开。"
   ],
   "conditions": [
    "「在人类还在树上吃果子的时代，或者在人类终于灭亡之后」（P004）。",
    "「假设第一代人类灭绝一亿多年以后，老鼠们进化成了新人类」（P006）。",
    "「即使数值和我们完全一样，但是因为这个圆周率存在于另一个文明的集体意识之中」（P007）。"
   ],
   "rhetoric_and_tone": "全篇设问体，除两处「显然」断言外几乎不含陈述句；以「来，回答一下这个问题——」直接邀请读者，用连续追问把问题推向概念边界，不给答案，也不表明作者立场。",
   "unresolved_questions": [
    "正文没有给出作者对「世界是否纯粹唯物主义」以及「圆周率是否客观存在」的结论；本篇以问题收束。",
    "「唯物主义」只在提问字段出现，正文未界定或使用该词。",
    "P007「与死者一模一样的新小孩」这一类比的确切含义（同一性还是复制）本篇未展开。",
    "「客观存在」的判据（如无质量、动量、位置是否足以否定其为「物」）本篇未说明。",
    "brief 与正文前五段重复且末尾被截断（止于「它是否实际上是不存在的？是依赖着我们人类」），仅作导航。",
    "本篇无图片节点。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "注意，世界上没有任何圆形的物体", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P009", "quote": "显然，圆周率是没有自己的质量、动量和位置的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "圆周率是否客观存在？", "relation": "context"},
    {"key": "E4", "paragraph_id": "P004", "quote": "在人类还在树上吃果子的时代，或者在人类终于灭亡之后，圆周率是否存在？", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "是依赖着我们人类的主观意识才存在着？", "relation": "context"},
    {"key": "E6", "paragraph_id": "P006", "quote": "它们是否会发现一个新的圆周率，和我们不一样？", "relation": "context"},
    {"key": "E7", "paragraph_id": "P007", "quote": "它只是一个与死者一模一样的新小孩？", "relation": "context"},
    {"key": "E8", "paragraph_id": "P008", "quote": "圆周率的存在性，到底是客观的，还是主观的？", "relation": "context"},
    {"key": "E9", "paragraph_id": "P010", "quote": "那么圆周率是不是一种“物”？", "relation": "context"},
    {"key": "E10", "paragraph_id": "P001", "quote": "来，回答一下这个问题——", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["哲学本体论", "数学哲学", "唯物论／观念论之争"],
   "issue_candidates": ["抽象对象的客观存在性", "数学对象是否依赖人类意识", "何为『物』", "跨文明数学同一性"],
   "text_function_candidates": ["设问／引导思考", "答疑（未给答案）", "苏格拉底式追问"],
   "object_candidates": ["圆周率", "圆规画的圆", "地球", "水波纹", "月球轨道", "老鼠进化成的新人类", "另一文明"],
   "working_keywords": ["圆周率", "客观存在", "主观意识", "集体意识", "唯物主义", "物", "质量", "动量", "位置"]
  },
  "notes": "brief 与正文前五段重复且末尾被截断（止于「它是否实际上是不存在的？是依赖着我们人类」），仅作导航，未据以补写正文。本篇正文没有作者结论，全部记为问题型主张（open_question），未把提问者的「唯物主义」问题写成作者立场。无图片节点。"
 },
 "2956f665": {
  "analysis": {
   "question_context": "提问者问「如何看待人大代表蒋胜男建议民法典草案删除离婚冷静期?」（Q001，属提问者；其中的人大代表与建议内容均只见于提问字段）。作者支持删除离婚冷静期，并进一步主张增设结婚冷静期与婚姻法告知程序（P001），理由是冲动结婚的社会成本更大、离婚冷静期挽回不了冲动结婚造成的失败婚姻（P002）；随后提出对强制调解、首轮驳回等司法实践的再审视、对智库课题的呼吁，并给出告知程序的具体设计，最后把家庭质量与航空发动机材料、国家竞争和民族复兴联系起来（P013–P020）。正文未再提及蒋胜男其人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "主张：不仅应删除离婚冷静期，还应增设结婚冷静期与婚姻法告知程序。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "理由：冲动结婚的社会成本绝对更大；离婚冷静期挽回不了冲动结婚造成的失败婚姻，如禁止公司破产或禁止呕吐。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "语义不清的过渡句：结婚冷静期可避免资源错配、「至少帮民政局多省四张纸」。", "role": "other"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005"], "summary": "主张重新审视强制调解与首轮普遍驳回离婚诉讼的实践，呼吁对智库下达立场中立、结论开放的课题研究，核算损耗对总体福利的影响及政策是否把社会强行固定在低能稳态。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "判断：现代中国在这一方面的执念缺少理性基础，更像源于老一辈无法接受社会伦理过快改变。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "婚姻法告知程序的设计：题库开放的单题考试，提前十天预约，未过可三天后重考且资格无限，完全正确为合格，双方通过即冷静期终点。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "预期收益：确保申请者准确认识婚姻法会节省无知带来的社会成本，可拯救儿童、节约治安与教育成本。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P013", "P014"], "summary": "判断：中国最大的问题是人与人之间基本伦理关系质量不高；若把家庭、企业视为社会基本构建，个人伦理认识的成熟程度就是钢的品质。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "以航空发动机为类比：技术迭代之外更根本的是材料问题；若不提高家庭这一基本零件的质检标准，甚至用离婚冷静期、首轮驳回掩盖或拖延其自我优化，中国成为优越文明发动机会有跨越不过去的天花板。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P019", "P020"], "summary": "结论：这「小小的不便」会明显提升家庭构件的抗压与工作性能，是与民族复兴、构建人类命运共同体有根本联系的极重大事，重要性不在科技争胜之下。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P021"], "summary": "平台话题标签「女性相关答集」，与正文论述无关，lexical 未覆盖该片段。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不仅应该删除离婚冷静期，还应该增设结婚冷静期以及婚姻法告知程序。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "比起冲动离婚，冲动结婚的社会成本绝对的更大。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "离婚冷静期根本挽回不了冲动结婚造成的失败婚姻，其作用如同靠禁止公司破产来避免投资人亏损、用禁止呕吐来增强营养吸收。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者提出待研究的问题：这种政策选择究竟是提高了稳定性，还是通过付出能量把社会强行固定在低能稳态、妨碍其走向更好的稳态。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "目前的强制调解、事实上的首轮普遍驳回离婚诉讼的法律实践，也要重新严肃审视其必要性。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质问耗费大量司法资源程序性阻碍公民解除婚姻关系的收益「确切的在哪里」，并呼吁对智库下达严肃的课题研究任务。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "需要的是立场中立、结论开放的严谨再研究，而不是「再给咱找点不要改的理由」的研究。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "现代中国在这一方面的执念缺少理性基础，更像是因为老一辈无法接受社会伦理的过快改变的结果。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "婚姻法告知程序应设计为题库开放的单题考试：提前十天预约，未过可三天后重考、重考资格无限、合格标准是完全正确，申请双方均通过即结婚冷静期的终点。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "确保婚姻申请者对婚姻法、婚姻的法律责任和法定权利有起码准确的认识，会大大节省因这种无知带来的社会成本。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者估计此举可拯救因父母不负责任的婚姻而陷入人生极大困境的儿童，并节约治安、教育上的社会成本。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国最大的问题是人与人之间的基本伦理关系质量不高。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "「中国最大的问题在于科技受制于人」被作者表述为「很多人认为」的看法，并以「事实上」引出自己的相反判断（未点名的流行观点）。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果把家庭、企业视为社会的基本构建，那么每个人的伦理认识的成熟程度就是钢的品质。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "中国的竞争困难在很大程度上恰恰类似航空发动机问题：不理解技术确实需要多年构思、试制和检测的迭代。", "evidence": ["E17"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "更根本的是材料问题：缺少耐高温、耐疲劳、耐损耗的材料，使构建最有效率的设计本身有难以逾越的困难。", "evidence": ["E18"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果不提高家庭这种基本零件的质检标准、任由其保持低质状态，甚至用离婚冷静期、首轮驳回掩盖或拖延其质量的自我优化，中国想要成为与其规模相衬的优越文明发动机会有跨越不过去的天花板。", "evidence": ["E19"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这一点小小的「不便」对提高家庭这一基本构件的抗压性能和工作性能会有明显提升作用。", "evidence": ["E20"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这看似家长里短的小事，实则是与中国民族复兴和构建人类命运共同体的基本目标有根本联系的极重大事。", "evidence": ["E21"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "其重要性绝不在科技争胜之下，甚至恐怕正是科技竞争最终取胜的重要前提条件之一。", "evidence": ["E22"]},
    {"claim_id": "C021", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「如何看待人大代表蒋胜男建议民法典草案删除离婚冷静期?」（Q001，仅见于提问字段；作者正文未提及蒋胜男其人，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "开门见山加码：不只删离婚冷静期，还要增设结婚冷静期与婚姻法告知程序。",
    "给出理由：冲动结婚成本更大，离婚冷静期救不了它，并用禁止破产、禁止呕吐两个类比贬斥该手段。",
    "（P003 过渡句语义不清，仅以「至少帮民政局多省四张纸」带过。）",
    "把批评扩展到强制调解与首轮驳回的司法实践，呼吁中立、结论开放的课题研究。",
    "判断这种执念缺少理性基础，归因于老一辈对社会伦理快速改变的抗拒。",
    "给出婚姻法告知程序的具体设计（单题题库考试、十天预约、三天后重考、完全正确为合格）。",
    "预期收益：减少无知造成的社会成本，拯救儿童并节约治安、教育成本。",
    "把议题提升：中国最大的问题是人际基本伦理关系质量不高，家庭是基本构建，伦理成熟度是钢的品质。",
    "以航空发动机类比：技术迭代之外，材料（家庭质量）是更根本的瓶颈。",
    "结论：提高家庭质检标准是重大事，关乎民族复兴与科技竞争胜负。"
   ],
   "concept_usage": [
    {"term": "离婚冷静期／结婚冷静期", "meaning": "前者是提问所指的现行安排，作者主张删除；后者是作者主张新增的、以婚姻法考试为终点的程序。", "evidence": "P001/P009/P010", "ambiguity": "结婚冷静期的具体时长除「提前十天预约」外未说明。"},
    {"term": "婚姻法告知程序", "meaning": "作者设计的一项题库开放的考试，只有一道题，双方通过即完成。", "evidence": "P007/P008/P009/P010", "ambiguity": "题库由谁维护、考试如何组织未说明。"},
    {"term": "低能稳态", "meaning": "作者用语：通过付出能量把社会强行固定住的状态，与「更好的稳态」相对。", "evidence": "P005", "ambiguity": "借用物理比喻，未给出界定标准。"},
    {"term": "钢的品质／材料问题", "meaning": "比喻：个人伦理认识的成熟程度之于社会，如同钢材品质之于航空发动机。", "evidence": "P014/P015/P016/P017", "ambiguity": "类比中「材料」同时指国民伦理素质与实体材料，含义在比喻与字面之间滑动。"},
    {"term": "基本零件／基本构件", "meaning": "指家庭；作者主张对其设立「质检标准」。", "evidence": "P018/P019", "ambiguity": "「质检标准」具体所指（教育、法律还是考试）未说明。"}
   ],
   "examples_and_targets": [
    "靠禁止公司破产来避免投资人亏损、用禁止呕吐来增强营养吸收（P002）：作者类比，用以贬斥离婚冷静期。",
    "「至少帮民政局多省四张纸」（P003）：口语化论据，所指不明。",
    "强制调解、首轮普遍驳回离婚诉讼（P004）：作者要求重新审视的现行实践。",
    "「再给咱找点不要改的理由」的研究（P005）：作者讽刺的研究取向。",
    "航空发动机（P015–P017）：作者类比，用技术迭代与材料问题说明瓶颈。",
    "「离婚冷静期、首轮驳回」作为掩盖或拖延家庭质量自我优化的手段（P018）：作者判断。",
    "中国民族复兴、构建人类命运共同体（P019）：作者引用的官方话语，用于拔高议题。",
    "人大代表蒋胜男及其建议（Q001）：只见于提问字段，作者正文未提及。"
   ],
   "conditions": [
    "「比起冲动离婚」（P002）——成本比较的前提。",
    "「如果没有考过，可以在三天后重考」（P009）——考试程序的分支条件。",
    "「如果把家庭、企业视为社会的基本构建」（P014）——类比的假设前提。",
    "「不理解技术是一回事」（P015）——作者对技术迭代难度的让步。",
    "「如果不提高家庭这种基本零件的质检标准」（P018）——预测性后果的条件。",
    "「只要……」（本篇未见）；作者多用「会」「将会」表述预测（P011、P018、P019）。"
   ],
   "rhetoric_and_tone": "政策评论体，判断句短促而绝对（「绝对的更大」「根本挽回不了」）；以禁止破产、禁止呕吐、航空发动机材料等类比贬斥或说明；带明确倡议（对智库下达课题、增设告知程序）；后半由具体政策转入国家竞争与民族复兴的宏大话语（P019–P020），语气近似训诫与呼吁并存。",
   "unresolved_questions": [
    "P021「女性相关答集」是平台话题标签，混入正文末尾，与全文论述无关；structure 已记录该处 lexical 未覆盖（1 处 divergence），需人工确认是否应剔除。",
    "P003 语句疑残缺、语义不清（「结婚冷静期对降低连这个加上不必要的社会资源错配一起避免」），作者原意未能确定。",
    "提问中提到的人大代表蒋胜男及其建议的具体内容，作者正文未提及、未评价，只就离婚冷静期政策本身作答。",
    "「至少帮民政局多省四张纸」的具体所指（表格数量还是其他）本文未说明。",
    "P004「这笔帐的收益确切的在哪里」为反问，作者未提供数据；对智库下达课题属倡议，可行性未讨论。",
    "P019–P020 把家庭质检标准与民族复兴、科技竞争胜负相关联，为预测性判断，本文未给论证细节。",
    "brief 与正文前两段重复且末尾被截断（止于「结婚冷静期对降低连这个加上不必要的社会资源错配一起避」），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "何止应该删除离婚冷静期，还应该增设结婚冷静期以及婚姻法告知程序。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "比起冲动离婚，冲动结婚的社会成本绝对的更大", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "离婚冷静期根本挽回不了冲动结婚造成的失败婚姻", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "这如同靠禁止公司破产来避免投资人亏损，用禁止呕吐来增强营养吸收", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "还是事实上通过付出能量强行固定在低能稳态，妨碍了我们的社会走向一个更好的稳态", "relation": "context"},
    {"key": "E6", "paragraph_id": "P004", "quote": "目前的强制调解、事实的首轮普遍驳回离婚诉讼的法律实践也要重新严肃的审视它的必要性", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "需要立场中立、结论开放的严谨的再研究", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "更像是因为老一辈无法接受社会伦理的过快改变的结果", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P007", "quote": "婚姻法告知程序的基本形式是一项题库开放的考试。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "重考资格无限，合格标准是完全正确。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "申请双方均通过考试，即结婚冷静期的终点。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "会大大的节省因为这种无知带来的社会成本", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "不知可以拯救多少因父母不负责任的婚姻而陷入人生极大困境的儿童", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "事实上中国最大的问题，是人与人之间的基本伦理关系质量不高。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "很多人认为中国最大的问题在于科技受制于人之类", "relation": "contradicts"},
    {"key": "E16", "paragraph_id": "P014", "quote": "每个人的伦理认识的成熟程度就是钢的品质", "relation": "context"},
    {"key": "E17", "paragraph_id": "P015", "quote": "中国的竞争困难，在很大程度上恰恰类似航空发动机问题", "relation": "context"},
    {"key": "E18", "paragraph_id": "P017", "quote": "是缺少耐高温、耐疲劳、耐损耗的材料", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "中国想要成为一部与其规模相衬的性能优越的人类文明发动机会有其跨越不过去的天花板", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "对于提高家庭这一基本构件的抗压性能和工作性能会有明显的提升作用", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "实则是与中国民族复兴和构建人类命运共同体的基本目标有根本联系的极重大事", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "甚至它恐怕正是科技竞争最终取胜的重要前提条件之一。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共政策", "婚姻家庭法", "社会伦理", "国家竞争力论述"],
   "issue_candidates": ["离婚冷静期存废", "结婚冷静期与婚姻法告知程序", "强制调解与首轮驳回", "家庭质量与社会成本", "科技竞争与材料/人才瓶颈"],
   "text_function_candidates": ["政策评论", "论辩", "行动建议／倡议"],
   "object_candidates": ["离婚冷静期", "民政局", "智库", "人大代表蒋胜男（仅见提问）", "家庭", "航空发动机", "中国"],
   "working_keywords": ["离婚冷静期", "结婚冷静期", "婚姻法告知程序", "低能稳态", "社会资源错配", "钢的品质", "材料问题", "人类命运共同体"]
  },
  "notes": "P021「女性相关答集」为平台话题标签混入正文（structure.text_lexical_divergence 记 1 处，lexical 未覆盖），与本文论述无关，已在 unresolved_questions 登记；该段仅 6 字，未作为 evidence 短引（不满足 10–60 字要求）。P003 语句疑残缺，未据以提出主张。提问字段中的人大代表蒋胜男未归给作者。brief 与正文前两段重复且被截断，仅作导航。本篇无图片节点。"
 },
 "cc24d577": {
  "analysis": {
   "question_context": "提问者说「我发现我对宇宙很感兴趣，我该从哪里初学呢？」（Q001，属提问者）。作者的回答是一份极简推荐：给出一部纪录片的英文名，说自己推荐，并进一步主张每个人都应该看、它应属现代人必备基础常识（P001–P005）。全文没有解释为什么推荐，也没有提供观看渠道或背景信息。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "推荐一套纪录片并给出片名《How does the universe work》，称其很适合小白扫盲。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "由对提问者的推荐扩展为对所有人的推荐：每个人都应该看看，这应是每个现代人必备基础常识的一部分。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有这么一套非常好的纪录片，很适合小白扫盲。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "推荐提问者观看《How does the universe work》这套纪录片。", "evidence": ["E1", "E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "事实上，每个人都应该看看这套纪录片。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这（纪录片内容）应该是每个现代人都必备的基础常识的一部分。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「我发现我对宇宙很感兴趣，我该从哪里初学呢？」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "直接给出推荐对象：一套非常好的纪录片，适合小白扫盲。",
    "给出片名《How does the universe work》。",
    "对提问者发出观看建议。",
    "把建议扩大到所有人：每个人都应该看看。",
    "以「应该是每个现代人都必备的基础常识的一部分」收尾，未给理由。"
   ],
   "concept_usage": [
    {"term": "小白", "meaning": "指零基础或初学者；作者以此界定适用受众。", "evidence": "P001", "ambiguity": "未说明门槛具体在哪里。"},
    {"term": "扫盲", "meaning": "补足基础知识；作者用它说明该纪录片的功能。", "evidence": "P001", "ambiguity": "未说明覆盖哪些知识。"},
    {"term": "基础常识", "meaning": "作者认为每个现代人都必备的知识的一部分。", "evidence": "P005", "ambiguity": "作者以「应该是」限定，未列出范围。"}
   ],
   "examples_and_targets": [
    "纪录片《How does the universe work》（P002）：作者的推荐对象；本篇未给中文名、出品方、年份、集数或观看渠道，片名准确性待外部核查。"
   ],
   "conditions": [
    "本文未给出明确条件；受众以「小白」（P001）与「每个现代人」（P004–P005）界定，未设其他前提。"
   ],
   "rhetoric_and_tone": "极简推荐体，五句话成篇；语气平实而肯定，用「事实上」「应该」加强推荐力度；不含论证、数据或限定说明。",
   "unresolved_questions": [
    "纪录片的中文名、出品方、年份、集数与观看渠道本篇均未说明；片名是否为官方准确名称待外部核查。",
    "「每个人都应该看看」「每个现代人都必备的基础常识」的理由未展开。",
    "brief 与正文五段几乎逐字相同（含被截断的观感），仅是正文的回显，不能单独支持主张。",
    "本篇无图片节点。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有这么一套非常好的纪录片，很适合小白扫盲。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "《How does the universe work》", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "事实上，每个人都应该看看。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这应该是每个现代人都必备的基础常识的一部分。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["科普", "天文学入门"],
   "issue_candidates": ["宇宙学入门途径", "科普纪录片的推荐", "基础常识的范围"],
   "text_function_candidates": ["答疑", "资源推荐"],
   "object_candidates": ["纪录片《How does the universe work》", "提问者", "现代人"],
   "working_keywords": ["How does the universe work", "纪录片", "小白", "扫盲", "基础常识"]
  },
  "notes": "brief 与正文五段几乎完全相同且末尾截断（止于「这应该是每个现代人都必备的基础常识的一部分。」），仅作导航。P003「推荐你看看。」仅 5 字，不满足 10–60 字的短引要求，故未单列 evidence；推荐意图由 P001「有这么一套非常好的纪录片」与 P002 片名共同支持。无图片节点。"
 },
 "f5a5535f": {
  "analysis": {
   "question_context": "提问者问「如何完成经由逻辑思维产生的决策?」（Q001，属提问者）。作者把它转成一套机制解释：逻辑思维对决策的执行提供两种力——推力（来自对危机与后果的清醒自知，属恐惧驱动）与拉力（来自对愿景的好奇，属愿景驱动）（P002–P020）；随后把「完成决策的最大关键」归为扎扎实实的规划能力，并提出觉知、逻辑、创造性思维三根支柱（P021–P033），最后以两台引擎及其机身材料作结（P034–P037）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "回应提问：逻辑思维对决策的执行有两种力，推力与拉力。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "界定需求与决策：需求是广义的危机感，决策本质是应对该危机的方案。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "思维越严谨、投入智力资源越多，越看得清危机与后果，这份没有侥幸的自知形成推力；团队领导常因此最有危机感与执行力。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "反向解释：一般人决策执行不下去，多因智力投入太少，决策与危机的关联半透明（如「我要好好学习」只来自道听途说），因此欠缺推力；作者声明不谈这是谁的错。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "界定拉力：对决策跃跃欲试的好奇心；投入的调查研究与计划越多，指向的愿景越真切，从而对执行产生拉力。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P021"], "summary": "总纲：完成决策的最大关键是扎实的规划能力；充分的觉知、严谨的逻辑、创造性的思维艺术是三根支柱。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023"], "summary": "第一根支柱：充分的觉知使计划不成为无本之木；若不能分辨事实与欲望恐惧催生的幻觉，决策就建立在流沙之上，执行会耗在自欺欺人上。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026"], "summary": "第二根支柱：严谨的逻辑保证推力，如工程师对桥墩尺寸的不敢侥幸；计算模糊则会「等垮了再说」。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "第三根支柱：创造新的思维艺术是决策的复活节彩蛋；全按老套路完成只重复已知经验，失掉智慧增长这一最大回报；加入新实验性要素可把人从时间的流沙中拉出，使结果只在赚经验与两者兼得之间。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "总结：推力即恐惧驱动，拉力即愿景驱动；两台引擎都工作就不必担心决策不被执行，其机身材料是疏而不漏的逻辑思维。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "逻辑思维对于决策的执行有两种力，一种推力，一种拉力。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "决策往往应对一种需求，而需求是一种广义的危机感；即使追求欲望的满足，决策也是为了应对「此欲望不能得满足」的危机。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "决策的本质就是为了应对这种危机而作出的方案。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "思维的严谨性、洞察力越高、投入的智力资源越多，越能看清危机是什么及其紧迫与危险，也越能看到决策的有效性、时效性和各阶段失败的后果。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想得越深入周密，对决策要害性的了解越没有侥幸；这份没有侥幸的自知会形成推动决策执行的推力。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "团队里的领导常常是最有危机感和执行力的人，原因之一是他对整个计划有最透彻的了解，对失误与延误的后果看得越清楚、越难自欺欺人。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一般人的决策执行不下去，一个极大原因是投入的智力资源太少，使决策与追求／危机之间的关联模糊、半透明；这常因策略与目标的关联是从别人那里道听途说、随大流随来的。", "evidence": ["E8", "E9", "E37"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以「我要好好学习，这样将来人生才能顺利」为例：若不追问什么样的学习导致什么样的顺利、哪些不学会死翘翘，就说明决策与危机的联系是半透明的。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明不谈这是谁的错，但既然智力投入如此，该决策就欠缺这份推力。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拉力是一份对决策跃跃欲试的好奇心：投入大量智力资源做深入调查研究和缜密计划后，能相当清晰地看到决策指向的愿景；投入越多愿景越真切，并对执行产生拉力。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "完成决策的最大关键是一份扎扎实实的规划能力；充分的内观外照的觉知、严谨的、经验的逻辑、和创造性的思维艺术是决策将来能被顺利执行的三根支柱。", "evidence": ["E17", "E18"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "充分的觉知保证一切不是无本之木；若对「什么是事实、什么是欲望和恐惧催生的幻觉」没有清晰分辨能力，一切决策都建立在流沙之上，执行时精力会用在自欺欺人、回避真相上。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "严谨的逻辑保证了推力：逻辑严谨则对后果没有侥幸，如同计算严谨的工程师不会觉得哪根桥墩没必要。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果计算是模糊的，自然就是「等垮了再说」，并以游戏式心态作比（关羽今天就能满级、服务器要掉随机宝箱）。", "evidence": ["E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "创造新的思维艺术是决策里的复活节彩蛋；如果决策里全是老套路，其实没有「成功」可言，因为完成只是在重复一种已知经验。", "evidence": ["E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "沿完全重复的固有套路完成一件事、拿到交付物，可以挣工资养活自己再活一段时间，但失掉了花去生命最应该得到的回报——智慧的增长。", "evidence": ["E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "智慧的增长才是人生幸福的最大保障，它甚至可以救赎计划本身的失败。", "evidence": ["E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "只要加入一点新的实验性要素，就会获得把人从时间的流沙里拉出来的力量。", "evidence": ["E29"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个力量如此重要，乃至于计划本身的成败得失与它相比亦为次要：也许损失金钱，但获得重新擦亮和拓宽的视野、新工具和对未来更强的信心。", "evidence": ["E30", "E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论金钱上是赚是亏，拿到实验的结果就不可能真的亏本；结局只在赚经验和既赚经验也赚收益之间，要么赢，要么赢得更多。", "evidence": ["E32"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被推力推着走是恐惧驱动，被拉力拉着走是愿景驱动。", "evidence": ["E33", "E34"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "两台引擎都在工作，就不必担心决策不会被执行。", "evidence": ["E35"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这两台引擎的机身材料，就是天网恢恢、疏而不漏的逻辑思维。", "evidence": ["E36"]},
    {"claim_id": "C024", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「如何完成经由逻辑思维产生的决策?」（Q001，仅见于提问字段，本篇段落不含该句，故无段落短引）。", "evidence": []}
   ],
   "argument_steps": [
    "先给总框架：逻辑思维对决策执行提供推力与拉力。",
    "定义需求为广义的危机感，把决策定义为应对该危机的方案。",
    "论证推力来源：智力投入越多→越看清危机与后果→没有侥幸的自知→推力；以团队领导为例。",
    "反向论证：智力投入太少使决策与危机的关联半透明（好好学习式决策、我听老爸说），故欠缺推力；声明不谈是谁的错。",
    "定义拉力来源：对决策的好奇心与愿景——投入越多，愿景越真切，拉力越强。",
    "给出总纲：最大关键是规划能力，三根支柱为觉知、逻辑、创造性思维艺术。",
    "论觉知：计划要基于事实而非欲望与恐惧催生的幻觉，否则决策建立在流沙之上。",
    "论逻辑：逻辑严谨则对后果没有侥幸（桥墩例），计算模糊则等垮了再说（游戏例）。",
    "论创造性：老套路只是重复已知经验，失掉智慧增长；加入新实验性要素可从时间的流沙中被拉出。",
    "结论：推力＝恐惧驱动，拉力＝愿景驱动，双引擎皆运转则决策必被执行，其材料是逻辑思维。"
   ],
   "concept_usage": [
    {"term": "推力／拉力", "meaning": "逻辑思维对决策执行的两种作用力：推力来自对危机与后果的清醒自知，拉力来自对愿景的跃跃欲试的好奇心。", "evidence": "P002/P006/P020/P034/P035/P036", "ambiguity": "两力若冲突或只具其一如何取舍，本文未说明。"},
    {"term": "需求／危机感", "meaning": "需求被定义为一种广义的危机感；决策是应对「欲望不能得满足」这类危机的方案。", "evidence": "P003/P004", "ambiguity": "把一切需求归为危机感，作者未处理例外情形。"},
    {"term": "半透明", "meaning": "描述决策与追求／危机之间关联模糊、未被打透的状态。", "evidence": "P008/P014/P015", "ambiguity": "作者以「这就是那个『半透明』」回指，未给出判定标准。"},
    {"term": "内观外照的觉知", "meaning": "第一根支柱：分辨事实与欲望、恐惧催生的幻觉，使计划基于曾经做到过什么、有什么、相信什么，而非基于以为什么、希望什么。", "evidence": "P021/P022", "ambiguity": "术语本身未定义，仅靠对比句说明。"},
    {"term": "三根支柱", "meaning": "充分的内观外照的觉知、严谨的、经验的逻辑、创造性的思维艺术。", "evidence": "P021", "ambiguity": "「经验的逻辑」确切含义未展开。"},
    {"term": "复活节彩蛋", "meaning": "比喻：决策中创造新的思维艺术所带来的额外回报。", "evidence": "P027", "ambiguity": "比喻性用语，未说明如何识别或度量。"},
    {"term": "时间的流沙", "meaning": "比喻：重复老套路时视野逐步阴暗、逐渐沉没的状态；新实验性要素可把人从中拉出。", "evidence": "P030/P031", "ambiguity": "比喻性用法。"},
    {"term": "引擎／机身材料", "meaning": "以推力与拉力为两台引擎，以逻辑思维为机身材料。", "evidence": "P036/P037", "ambiguity": "比喻性用法，未与技术概念对应。"}
   ],
   "examples_and_targets": [
    "「我要好好学习，这样将来人生才能顺利」（P009–P015）：作者例证，用来说明决策与危机的关联半透明；「我听老爸说」（P015）为引语式例证。",
    "团队里的领导（P007）：作者举例说明危机感与执行力的来源。",
    "桥墩、六级风、天气预报（P024）：作者类比，用工程师的不敢侥幸说明严谨逻辑带来推力。",
    "关羽满级、服务器掉随机宝箱（P025）：游戏式类比，说明计算模糊时的心态。",
    "「对着风扇假装超人」「花大量的时间哭泣」（P022）、「执行个空气啊」（P023、P026）：口语化修辞。",
    "时间的流沙（P030–P031）、复活节彩蛋（P027）、引擎与机身材料（P036–P037）：作者比喻。"
   ],
   "conditions": [
    "「即使你是在追求一种欲望的满足」（P003）。",
    "「你如果对此没有清晰的分辨能力」（P022）——决策沦为流沙之上的条件。",
    "「如果这个计算是模糊的」（P025）。",
    "「如果你的决策里全是老套路」（P027）。",
    "「只要加入一点新的实验性要素」（P031）。",
    "「无论金钱上是赚是亏」（P033）。",
    "「两台引擎都在工作」（P036）。"
   ],
   "rhetoric_and_tone": "第二人称「你」贯穿，像面对面指导与训诫，兼有鼓励；口语与网络化表达（「执行个空气啊」「关羽今天就能满级」「复活节彩蛋」）；比喻密集（半透明、流沙、桥墩、引擎与机身材料）；结尾以格言式短句收束（P034–P037）。",
   "unresolved_questions": [
    "作者把提问的「如何完成」转成推力／拉力与三根支柱的解释框架，但未给出可操作的步骤、顺序或验证办法。",
    "推力与拉力若互相冲突或只具备其一时应如何处理，本文未说明。",
    "桥墩与游戏两个例子均为类比，未附数据、研究或来源，相关事实断言需外部核查。",
    "「内观外照」「经验的逻辑」等表述未在文中定义，仅靠对比句说明。",
    "P030 起叙述人称从「你」转为「我」（「我其实在渐渐沉入时间的流沙」），是否为作者自述经验，本文未说明。",
    "brief 与正文前三段重复且末尾被截断（止于「你的决策的本质就是」），仅作导航。",
    "本篇无图片节点。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "逻辑思维对于决策的执行有两种力，一种推力，一种拉力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "需求，是一种广义的危机感。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "决策也是为了应对“此欲望不能得满足”的危机", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你的决策的本质就是为了应对这种危机而作出的方案。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你就越能看清楚危机是什么、它有多紧迫、它有多危险", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这份没有侥幸的自知，就会形成一种推动决策执行的推力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这也是为什么一个团队里的领导常常是最有危机感和执行力的人的原因之一", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "一个极大的原因就是投入的智力资源太少", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "对于自己目前所采取的策略和追求的目标之间的关联是从别人那里道听途说来的，随大流随来的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "比如，“我要好好学习，这样将来人生才能顺利”", "relation": "context"},
    {"key": "E11", "paragraph_id": "P012", "quote": "学哪些不学会死翘翘，哪些学了没啥意义？", "relation": "context"},
    {"key": "E12", "paragraph_id": "P015", "quote": "你对这个决策投入的全部智力资源，只是“我听老爸说”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "只是既然是这样，你的决策就欠缺这份推力。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "是一份对决策的跃跃欲试的好奇心。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "你投入的资源越多，那个愿景也就越真切。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "这个愿景就会对你的决策的执行产生拉力。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "完成决策的最大关键，就是一份扎扎实实的规划能力。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "和创造性的思维艺术是这决策将来能被顺利执行的三根支柱。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "充分的觉知，保证了一切不是无本之木。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "你一切的决策都不过是建立在流沙之上。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "总是在对着风扇假装超人", "relation": "context"},
    {"key": "E22", "paragraph_id": "P024", "quote": "严谨的逻辑保证了那个推力。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "这就跟计算严谨的工程师绝对不会觉得哪根桥墩没必要一样。", "relation": "context"},
    {"key": "E24", "paragraph_id": "P025", "quote": "如果这个计算是模糊的，那自然是等垮了再说吧。", "relation": "contradicts"},
    {"key": "E25", "paragraph_id": "P027", "quote": "创造新的思维艺术是决策里的复活节彩蛋。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P027", "quote": "其实你的决策是没有“成功”可言的", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P028", "quote": "但却失掉了花去生命最应该得到的回报——智慧的增长。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P029", "quote": "后者才是人生幸福的最大保障，它甚至可以救赎计划本身的失败。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P031", "quote": "我就会获得把我从时间的流沙里拉出来的力量", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P032", "quote": "乃至于计划本身的成败得失与它相比其实亦为次要。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P032", "quote": "但我获得了重新擦亮和拓宽的视野，有了新的工具和对未来更强的信心", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P033", "quote": "要么赢，要么赢得更多。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P034", "quote": "被推力推着走，是恐惧驱动。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P035", "quote": "被拉力拉着走，是愿景驱动。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P036", "quote": "两台引擎都在工作，你就不必担心你的决策不会被执行。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P037", "quote": "就是天网恢恢、疏而不漏的逻辑思维。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P023", "quote": "那还有个空气的执行啊。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["决策心理学", "行动理论与执行力", "自我管理／方法论"],
   "issue_candidates": ["决策执行不力的原因", "恐惧驱动与愿景驱动", "规划能力与三根支柱", "经验重复与创新回报", "自欺与觉知"],
   "text_function_candidates": ["答疑", "经验总结", "劝导／训诫", "方法论阐述"],
   "object_candidates": ["提问者", "团队领导", "工程师与桥墩", "决策者本人（我）"],
   "working_keywords": ["推力", "拉力", "广义的危机感", "半透明", "内观外照的觉知", "三根支柱", "复活节彩蛋", "时间的流沙", "恐惧驱动", "愿景驱动"]
  },
  "notes": "brief 与正文前三段重复且末尾被截断（止于「你的决策的本质就是」），仅作导航。P023、P026 的「执行个空气啊」类口语否定保留在正文引用中；P026 仅 6 字未作短引，P023 已作 E37。提问字段的提问者立场未归给作者。无图片节点。"
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
