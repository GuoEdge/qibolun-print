# -*- coding: utf-8 -*-
"""批次 r001-b0043 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0043.sessions.py            # 写 out/r001-b0043.out.jsonl
  python3 records/r001-b0043.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0043"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0043.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "0d8ddd57": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何辨认身边的聪明人？”。作者先追问“人们为什么要识别聪明人”，答以“愚蠢是罪恶的最好温床”，并区分“相对的聪明”与“绝对的聪明”（P001-P007）；给出“绝对聪明”的定义与最简识别法，指出该方法可用时“这人身边已经没有位置了”，于是产生“提前看出尚未被发掘的绝对聪明人”的需求（P008-P012）；批评由该需求召唤出的“相对聪明”标准（以与马云等成功者相像为判据）错在“何谓成功”（P013-P036）；最后给出两条可观察线索（承担义务而不回避不消沉、对双赢的偏执性执着）与“遇之于微时”的占位策略（P037-P068），并以“永远在收藏和栽种的才是真·聪明人”反转收尾（P069-P079）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"], "summary": "审题：人们要识别聪明人，是因为愚蠢是罪恶的最好温床；聪明人的恶可以处理，愚蠢人的恶静止、绝对、无法处理；提问者真正想问的是“绝对聪明”而非“相对聪明”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012"], "summary": "界定“绝对聪明”为“在各种风险挑战下大概率还能保持正输出”“和ta达成正面协议就大概率不会吃亏”的能力；最简识别法是查过往成绩，但该方法可用时对方身边已无位置，于是产生“提前识别”的需求。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "描述由该需求召唤出的“相对聪明”概念：以“素质论”“能力论”为依据，认为与已被证明绝对聪明者（如马云）相像的人最可能发迹，属赌马式思路。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "指出该思路“思路对、执行错”：错在“何谓成功”——把成功等同于有名有钱有权，就把“成功者的前体”偷换成“有名有钱有权者的前体”；以少年洛克菲勒为例说明模仿者极大概率失败、下注成愚蠢行为。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "举证与澄清：杂志上侃侃而谈者只是幸存者，埋骨道旁者看不见；从身边采样可见绝大多数人（包括“名门之后”）都不会在名权利上多成功；有钱有权有势者只是拥有帮助人的条件，作者绝不说他们一定是坏人，但其中很大一部分并非要找的聪明人。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043"], "summary": "给出寻找路径：擅长某事的人一定是做得最多的人；做得最多或出于不做不行、或出于真的喜欢；要找的是自认有拉人出水义务的人或喜欢拉人出水的人。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "第一种线索：承担很大义务而不回避、不消沉（如无意听说其家属重病而不离不弃）；“无意听说”意味着没有到处鼓吹，举重若轻是很大的智慧证明；靠忍或自我欺骗都做不到，只能靠反复想通一系列问题；这种人看似没浮出水面是因为脚上套着大铅球，其向上的力量是“绝对聪明人”最核心的资格证明，即使一时未解开，稳住不恶化也往往逐渐好转，因而是最有性价比的收藏对象。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063"], "summary": "第二类线索：不是被迫担责，而是对双赢有信心，偏执地执着于“怎么可能让参与者吃没同意的亏”；底色是骄傲，若看错则先吸收损失让别人至少保本；表现即“临难毋苟免”，由此积累经验技术、高几率办成事，也更容易得到帮助，形成正反馈——这类人是“大浮筒”。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068"], "summary": "占位策略：这类人需“遇之于微时”，要趁其还笨拙时抢先占位；信号是在可有可无、推卸了谁也无法指责的地方观察其是否推卸责任；若能让其获得“责任承担得起”的真实体验，就可能护住“临难毋苟免”的种子。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079"], "summary": "反转收尾：真有油水的“绝对聪明人”是自己栽种出来的；作者提示还漏了极重要的一类，答案就藏在上面几段里——永远瞪大眼睛在收藏和随时在栽种的，才是真·聪明人（“It takes one to know one.”）。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人们要识别聪明人，是因为愚蠢是罪恶的最好温床。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分：聪明人的恶可以处理和互动，愚蠢人的恶是静止的、绝对的、无法处理的；人们往往已从无法排除的“蠢恶人”身上体会到这种痛苦。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为提问者真正想问的不是“某人是否相对聪明”，而是“某人是不是绝对聪明”，并称审题的习惯很重要。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“绝对聪明”界定为一种“在各种风险的挑战下大概率还能保持正输出”的能力、一种“和ta达成正面协议就大概率不会吃亏”的能力。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为最简单的识别办法是查看对方过往成绩，但谁都知道这一条，所以当这个方法可用时“这人身边已经没有位置了”，于是产生提前识别尚未被发掘者的强烈需求。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述由该需求召唤出的“相对聪明”概念：人们相信相对更聪明的人最有可能将来发迹，以便提前下注盈利。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出这套标准的形成机制：马云被认定为绝对聪明的代表，与马云相像的要素于是被定义为相对聪明的标准；这是赌马式思路，把“最聪明的人”等同于与已被证明绝对聪明者最相像的人。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这套思路错在“何谓成功”：把成功视为有名、有钱、有权，就悄悄把“成功者的前体”偷换成“有名有钱有权者的前体”。", "evidence": ["E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言当前的“有名／有钱／有权者的前体”自身并没有很大概率在下一个时代、在所处的环境里发育成“有名／有钱／有权者”。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者以少年洛克菲勒为例预测：重复其行为模式（如超大胆投机）极大概率不会成为新时代的洛克菲勒，而是成为死在投机市场里的失败者；在疑似者身上下注也极大概率输掉，这概率远大于50%，以至下注成了愚蠢行为。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这个低概率是事实：能在杂志上侃侃而谈“照ta的方法做就成了ta”的人只是万千赌徒中的幸存者，埋骨道旁者看不见；从身边采样可见即使出身上流社会比例也不大，绝大多数人包括“名门之后”都不会在名权利上多成功。", "evidence": ["E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者澄清并限定：有钱、有权、有势者仅仅拥有帮助人的条件，可能滑不溜手、踢落攀附者或设钩诱吃靠近的人；作者绝不是说他们一定是坏人，但其中很大一部分并非开篇所说能解决问题的聪明人。", "evidence": ["E22", "E23"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出寻找路径：任何事情擅长它的人一定是做得最多的人；做得最多或因为不做不行、或因为真的喜欢；要找的是自认即使不喜欢也承担拉人出水义务的人，或出于某种原因喜欢拉人出水的人，只有这两种人才有那种“绝对聪明”。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出第一种可观察特征：承担很大的义务而不回避、也不消沉（如无意听说其家属重病而不离不弃）；“无意听说”说明没有到处鼓吹，能举重若轻是很大的智慧证明，靠忍或否认事实、美化幻想都骗不过自己，只能靠反复想通“为什么是我”等一系列问题。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种人看似没浮出水面是因为脚上套着大铅球；扛铅球练出的向上力量是“绝对聪明人”最核心的资格证明；即使铅球一时未解开，只要能稳住不恶化，往往因经验和心力积累而逐渐好转。", "evidence": ["E30", "E31"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张这种人是“最值得、也最有性价比的收藏对象”，结合自己的资源稍加帮助、引导、结善缘，将来有惊喜回报的几率不小。", "evidence": ["E32"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述第二类绝对聪明人：不是被迫担责，而是对双赢有信心，偏执地执着于“怎么可能让参与者吃没同意的亏”；底色是骄傲，自信能做出真正净盈利，若看错则先吸收损失让别人至少保本。", "evidence": ["E33", "E34"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“临难毋苟免”概括这类人在规则不周全、责任不明时不把责任视为与己无关；并称只有这样的人才有足够多的“难”和对付难的经验技术，从而高几率办成事、让各方至少不吃亏，也因低风险高收益而更容易得到帮助，形成正反馈，“这类人都是大浮筒”。", "evidence": ["E35", "E36", "E37", "E38"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出占位策略：这类人需“遇之于微时”，要趁其还笨拙、还不知道将来多强时抢先占位；信号是在可有可无、推卸了谁也无法指责的地方观察其是否推卸责任。", "evidence": ["E39", "E40"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以“如果作为相关人”为条件提出：让其在别处悄悄获得“责任是可以承担得起的”真实体验，这些体验将护住“临难毋苟免”的种子，可能种出将来能救你的梧桐木。", "evidence": ["E41"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者最后反转：真有油水的“绝对聪明人”是自己栽种出来的；还漏了极重要的一类，就藏在上面几段话里——永远瞪大眼睛在收藏和随时在栽种的，才是真·聪明人（“It takes one to know one.”）。", "evidence": ["E42", "E43", "E44"]}
   ],
   "argument_steps": [
    "审题：先问“为什么要识别聪明人”，答以“愚蠢是罪恶的最好温床”（P001、P002）。",
    "区分：聪明人的恶可处理，愚蠢人的恶无法处理；提问者真正要的是“绝对聪明”（P003-P007）。",
    "定义“绝对聪明”＝在各种风险下大概率保持正输出、与其达成正面协议大概率不吃亏（P009）。",
    "指出最简识别法（查过往成绩）的时效困境：可用时身边已无位置，于是产生提前识别需求（P010-P012）。",
    "描述由此产生的“相对聪明”标准：与已被证明绝对聪明者（马云）相像（P013-P019）。",
    "转折：思路对、执行错——错在“何谓成功”，成功被等同于名、钱、权，于是偷换了“前体”（P022-P028）。",
    "以少年洛克菲勒说明模仿与下注的失败概率远大于50%（P029-P031）。",
    "举证：幸存者偏差、身边采样、名门之后亦难成功（P032、P033）。",
    "澄清与限定：名权利者只是拥有帮助人的条件，未必是坏人，也多半不是要找的人（P035、P036）。",
    "给出线索：擅长者做得最多；动机两类；要找承担拉人出水义务者或喜欢拉人出水者（P037-P043）。",
    "第一类特征：重负下不回避不消沉、举重若轻、靠想通一系列问题撑住；是套着铅球的潜力者，最值得收藏（P044-P053）。",
    "第二类特征：对双赢偏执、临难毋苟免、正反馈积累成“大浮筒”（P054-P063）。",
    "策略：遇之于微时，观察其在无人指责处是否推卸责任，并给其“责任可承担”的体验（P064-P068）。",
    "反转收尾：真有油水者是自己栽种的；永远在收藏与栽种的才是真·聪明人（P069-P079）。"
   ],
   "concept_usage": [
    {"term": "绝对聪明／相对聪明", "meaning": "绝对聪明指在各种风险下大概率保持正输出、与其达成正面协议大概率不吃亏的能力；相对聪明指与已被证明绝对聪明者相像的素质与能力标签。", "evidence": "P009", "ambiguity": "“大概率”“正输出”的判据与时间尺度本文未给出。"},
    {"term": "浮筒／游泳圈／气球／铅球", "meaning": "比喻体系：能救自己出困境的人是浮筒、游泳圈、气球；拖累或压制人的负担是铅球、大铁球。", "evidence": "P004", "ambiguity": "为贯穿全篇的比喻，未给出与所描述能力的严格对应。"},
    {"term": "赌马式思路", "meaning": "作者对“相对聪明”标准的概括：像预测赛马一样，看尚未出发的马与过往冠军马有多相像。", "evidence": "P018", "ambiguity": "未说明该思路在何种条件下可能有效。"},
    {"term": "成功者的前体／有名有钱有权者的前体", "meaning": "作者用来揭示概念偷换：把“会成功的人”替换成“有名、有钱、有权者所具有的特征”。", "evidence": "P026", "ambiguity": "“前体”的判定标准本文未给出。"},
    {"term": "收藏／占位／栽种", "meaning": "作者把结交潜在聪明人比作收藏、抢先占位与栽种，主张对其“稍加帮助、稍加引导、结点善缘”。", "evidence": "P053", "ambiguity": "把人际关系工具化表述，是否为作者真实主张及其限度本文未说明。"},
    {"term": "临难毋苟免", "meaning": "作者引用的说法，指在规则不周全、责任不明时不把责任视为与己无关。", "evidence": "P058", "ambiguity": "未给出出处与适用边界。"},
    {"term": "大浮筒", "meaning": "作者对第二类绝对聪明人的称呼，指其能在关键时刻救人。", "evidence": "P063", "ambiguity": "为比喻说法。"},
    {"term": "真·聪明人", "meaning": "作者结尾所指：永远瞪大眼睛在收藏和随时在栽种的人。", "evidence": "P078", "ambiguity": "是玩笑式反转还是实质主张，本文未明说。"}
   ],
   "examples_and_targets": [
    "马云：作者举例（被视为绝对聪明的代表，其相似要素成为相对聪明标准）（P016、P017）。",
    "少年洛克菲勒／新洛克菲勒：作者举例（超大胆投机；迷信模仿者多死在投机市场）（P029、P030）。",
    "杂志上侃侃而谈的成功者：作者举例，指幸存者偏差（P032）。",
    "“名门之后”、出身上流社会者：作者举例说明成功比例不大（P032、P033）。",
    "有钱、有权、有势的人：作者评论对象，称其只是拥有帮助人的条件（P035、P036）。",
    "家属或配偶有重病的同事、朋友：作者举例说明第一种线索（P046）。",
    "大铅球、气球、游泳圈、浮筒、梧桐木、金字塔：作者的比喻材料（P003、P004、P034、P050、P068）。",
    "提问者的“如何辨认身边的聪明人”：提问者语境（Q001），作者改写为“绝对聪明”的问题。"
   ],
   "conditions": [
    "P007 以“审题的习惯多重要”提示问题被改写。",
    "P009 用“大概率”限定能力判据，非必然性。",
    "P023 以“如果成功（绝对聪明）即聪明（相对聪明）的结果”为假设前提，给出两条可选逻辑路线。",
    "P026 以“当你把成功视为有名、有钱、有权的时候”为条件，指出概念偷换。",
    "P027 把判断限定在“下一个时代、在你所处的环境里”。",
    "P036 用“我当然绝不是说……但……”作让步与限定。",
    "P046 以“比如”引出例证；P047 以“无意听说”为条件说明对方未自我宣扬。",
    "P051 以“即使一时没有解开”为让步条件，说明未来乐观性的前提是稳住不恶化。",
    "P056 以“如果我看错了，没有做到净盈利”为条件，说明先吸收损失的做法。",
    "P064 以“你需要遇之于微时”提出时机条件。",
    "P066 把观察场景限定在“可有可无的、看似无关紧要的、想推卸谁也无法指责的地方”。",
    "P068 以“如果作为相关人……那么……”为条件，说明栽种策略的预期效果（“可能种出”）。"
   ],
   "rhetoric_and_tone": "长篇指导体，设问自答与戏谑提示交替（“对吧？”“魔鬼笑了。”“错在哪里了？”“你漏了极大的一类。”“你想到没有？”）；以铅球／气球／游泳圈／浮筒／赌马／种子／梧桐木构成比喻体系；对读者第二人称指导，语气笃定、时而调侃，结尾以英文格言反转。",
   "unresolved_questions": [
    "P032“这概率远远的大过50%”与“你可以去简单调查一下”未给出数据来源、调查方法与样本界定，需外部核查。",
    "以马云、少年洛克菲勒为例属作者举例，其可比性与时代条件本文未论证。",
    "“收藏对象”“占位”“栽种”把人际关系工具化，是否为作者真实主张及其限度，本文未说明。",
    "结尾“真·聪明人”是玩笑式反转还是实质结论，本文未明说。",
    "提问所问“如何辨认身边的聪明人”被作者改写为“绝对聪明”的问题，二者的对应关系需研究者判断。",
    "P034“金字塔是尖的”为类比；P048 列举的一连串人生问题未给出答案。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "要准确的回答这个问题，要先想清楚——人们为什么要识别聪明人？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为愚蠢是罪恶的最好温床。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "聪明人的恶，是可以处理和互动的；愚蠢人的恶，是一种静止的、绝对的、无法处理的恶。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "而是“这个球是不是比水轻”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "ta们想问的，不是如何看出某人是否相对的聪明，而是想学会看清楚某人是不是绝对的聪明。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你们看，审题的习惯多重要。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "就是指一种“在各种风险的挑战下大概率还能保持正输出”的能力", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "这个要识别，最简单的办法就是直接查看这人的过往成绩，看跟ta打交道的人是不是都没有吃亏。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "但故事就是从这里开始的——谁都知道这一条，所以当这个方法可用的时候，这人身边已经没有位置了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "所以，“怎么在为时已晚之前、提前就看出谁是尚未被发掘的绝对聪明人”就成了顺理成章的强烈需求。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "是这个强烈需求召唤出了基于“素质论”“能力论”的相对聪明概念。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "人们相信相对更聪明的人最有可能在将来发迹，这样“我就可以提前下注，指望盈利了”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "可能成为马云的人，一定是和马云很像的人。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "马云被认定为了绝对聪明的代表，于是和马云很像的那些要素，就会被定义为相对聪明的标准。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "因此，最聪明的人，一定是和那些被证明了绝对聪明的人最相像的人。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "当你把成功视为有名、有钱、有权的时候，你无意间把“成功者的前体”悄无声息地偷换成了“有名有钱有权者的前体”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "当前的“有名 / 有钱 / 有权者的前体”自身并没有很大的概率在下一个时代、在你所处的环境里发育成“有名/有钱/有权者”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P029", "quote": "你去重复少年洛克菲勒的行为模式——比如超大胆的投机——极大的概率你不会成为新时代的洛克菲勒，而是成为无数迷信“与洛克菲勒一样就可以成为新洛克菲勒”而死在人生投机市场里的失败者。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "这概率远远的大过50%，以至于下注成了一种愚蠢的行为。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "能在杂志上侃侃而谈“我非常喜欢ta，我就照着ta的方法做，然后我果然就成了ta”的人，只是万千赌徒中的幸存者。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "绝大多数人——包括“名门之后”——都不会在名、权、利上有多成功。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "其实，所谓“有钱、有权、有势的人”，仅仅只是拥有帮助人的条件而已", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "我当然绝不是说有钱、有权、有势之人就一定是坏人，但ta们之中的很大一部分并非我们在一开头所提的那种你想要寻找的、能解决问题的聪明人。", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P039", "quote": "1）任何事情，擅长它的人一定是做得最多的人。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P040", "quote": "2）做得最多的人往往出于两类理由，要么是因为某种原因导致ta不做不行，要么是ta自己真的喜欢这么做。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "你要找的聪明人或者是那种认为自己即使不喜欢，也承担着拉人出水的义务的人；或者是出于某种原因喜欢拉人出水的人。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P045", "quote": "第一种，承担着很大的义务而不回避，也不消沉。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P047", "quote": "还能管理住自己的情绪，举重若轻，这是非常大的智慧证明。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P048", "quote": "只有一条路，就是靠想清楚为什么是我、为什么我应该面对、我可以如何面对、我这样做的意义是什么、人生的意义是什么、别人有什么责任、社会有什么责任……一系列的问题。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P050", "quote": "这人通过扛铅球练出来的那种不动如山的向上的力量，是“绝对聪明人”最核心的资格证明。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P051", "quote": "因为无论是什么问题，只要能稳住不恶化，就往往能因为经验和心力的积累而逐渐好转。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P053", "quote": "这种人是最值得、也最有性价比的收藏对象。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P055", "quote": "这是一种对“怎么可能让参与者吃没同意的亏”的偏执性的执着。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "如果我看错了，没有做到净盈利，那么我一定先吸收损失，让别人至少保本", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P057", "quote": "如果是因为约定规则不周全造成的出现事故后责任不明，这种人不会将这种责任理所当然的视为与己无关。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P058", "quote": "即所谓的“临难毋苟免”。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P059", "quote": "只有“临难毋苟免”的人，才会有足够多的“难”，也才会有对付这些“难”的经验和技术。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P060", "quote": "因为这是一种低风险但是却大概率可能有高收益的投资，谁会不愿意？", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P063", "quote": "显而易见，这类人都是大浮筒。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P064", "quote": "这类人真正的问题是你需要遇之于微时", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P066", "quote": "占位的信号，就是在一些可有可无的、看似无关紧要的、想推卸谁也无法指责的地方，观察这人是不是会推卸责任。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P068", "quote": "这些体验将会护住这颗“临难毋苟免”的种子，可能种出一棵将来能救你的梧桐木来。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P070", "quote": "真有油水的“绝对聪明人”，是你自己栽种出来的。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P078", "quote": "永远瞪大眼睛在收藏和随时在栽种的，才是真·聪明人。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P079", "quote": "It takes one to know one.", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["识人与判断", "成功学批判", "风险与决策"],
   "issue_candidates": ["如何辨认聪明人", "绝对聪明与相对聪明之别", "以成功者特征预测成功的谬误", "人脉经营与占位策略"],
   "text_function_candidates": ["答疑", "论辩", "经验总结", "指导"],
   "object_candidates": ["马云", "少年洛克菲勒", "有钱有权有势者", "名门之后", "承担重病家属责任者"],
   "working_keywords": ["绝对聪明", "相对聪明", "浮筒", "铅球", "赌马式思路", "成功者的前体", "临难毋苟免", "大浮筒", "遇之于微时", "真·聪明人"]
  },
  "notes": "正文无图片节点。brief 为正文语句摘录，仅作导航。作者把提问的“如何辨认聪明人”改写为“如何辨认绝对聪明人”，并给出识别线索与占位建议；结尾反转指“真·聪明人”是收藏与栽种者本人。"
 },
 "709c7581": {
  "analysis": {
   "question_context": "提问者（Q001）问“人最重要的能力是什么？”。作者只给出一句断言式回答——“当然是爱和被爱的能力”，并附一句“不接受反驳”，全文共两段，未展开界定、论证或例证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者答“人最重要的能力是爱和被爱的能力”，并声明不接受反驳。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人最重要的能力是爱和被爱的能力。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明不接受反驳，即拒绝就此展开辩论。", "evidence": ["E2"]}
   ],
   "argument_steps": [
    "直接给出答案：爱和被爱的能力（P001）。",
    "以“不接受反驳”封住讨论（P002）。"
   ],
   "concept_usage": [
    {"term": "爱和被爱的能力", "meaning": "本文只作为“人最重要的能力”的答案出现，未作任何界定。", "evidence": "P001", "ambiguity": "“爱”与“被爱”的所指、以及何以称为“能力”，本文均未说明。"}
   ],
   "examples_and_targets": [
    "无具体例证、人物或数据；全文仅两句。",
    "提问者的“人最重要的能力是什么”：提问者语境（Q001），作者以一句话作答。"
   ],
   "conditions": [
    "本文未说明任何条件、限定或适用范围。"
   ],
   "rhetoric_and_tone": "极简断言体：用“当然”加强确信，用“不接受反驳”作戏谑式封口，未作论证；整篇仅两句话，带调侃意味。",
   "unresolved_questions": [
    "“爱和被爱的能力”的具体含义、与提问“最重要的能力”的衡量标准，本文均未说明。",
    "“不接受反驳”是玩笑还是对讨论的严肃拒绝，本文未说明。",
    "本篇无图片节点，正文文本已完整阅读（共2段）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当然是爱和被爱的能力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不接受反驳。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生观念", "情感与能力"],
   "issue_candidates": ["人最重要的能力", "爱与情感的价值"],
   "text_function_candidates": ["答疑（一句话作答）", "断言"],
   "object_candidates": [],
   "working_keywords": ["爱和被爱的能力", "不接受反驳"]
  },
  "notes": "正文无图片节点，仅2段18字。brief 为正文原文，与正文一致；作者未展开论证。"
 },
 "fffcc0f7": {
  "analysis": {
   "question_context": "提问者（Q001）问“有没有一种液体可以使哺乳动物在里面呼吸？”。作者把实现条件拆成四关（血氧交换效率、溶剂对人体内环境的安全性、呼吸动力、由液转气的路径障碍），逐关说明难度（P001-P014），综合判断“不太现实”，并据此评论科幻作品中的液体培养皿、液体抗高G力设定与 EVA（P015-P022）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "提出要闯过四关；第一关（微观血氧交换效率）有希望，是最容易的一关，前提是某液体有足够载氧量、能与空气匹敌且无碍交换过程。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "第二关（溶剂安全性）难：肺与呼吸道是湿润、高透过性的粘膜，流动性好的小分子几乎都能渗透；按“长时间呼吸”的题设等于连续静脉注射；能大量进入内环境、长期存在且无毒的物质目前看几乎只有水（生理盐水）。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "第三关（呼吸动力）：自主呼吸肌不强健，驱动空气绰绰有余但驱动密度大得多的液体很困难，须借助呼吸机类外部动力（类似“灌进去、抽出来”）；否则呼吸肌群疲劳、代谢废物积累、酸痛抽搐、呼吸紊乱，最终致命。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "第四关（路径障碍）：由液转气会有半液半气状态，肺泡不会自我吞吐，液体长期潴留；液体含氧被耗尽、二氧化碳饱和，除非其能在体温下自然捕获氧气并释放二氧化碳且能力与空气相当，否则成为乏氧液体与阻隔；若不能快速排除，人就要靠仅露出几分之一交换面积的肺泡呼吸，危险甚至窒息而死；除非上ECMO长期替代肺（周期以天计，前提是液体无毒）。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017"], "summary": "综合判断：液体呼吸不太现实；科幻电影里“装满营养液的人体培养皿”没有呼吸管就不靠谱；临床上液体悬浮的主要意义是大面积烧伤患者不宜与床接触时的休养，这种情况没必要连呼吸都替代（“泡归泡，为什么不配根氧气管呢？”）。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "对科幻作品的评论：泡在液体里对支撑人体对抗高G力勉强有一点积极作用；但《环太平洋》式动作投射机制下动作迟缓、没有实际意义，姿势修正速度跟不上失衡节奏；并追问 EVA 为何不用无线传输，以玩笑归因（庵野国贼不相信日本能搞好5G）与“必须天诛之”收尾。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“液体呼吸”的实现条件拆成四关：血氧交换效率、溶剂对人体内环境的安全性、呼吸动力、呼吸模式转换时的路径障碍。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者认为第一关是有希望的、也是最容易的一关，并以假设条件给出：某液体有足够载氧量、能与空气匹敌且无碍于交换过程。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为第二关难：肺和呼吸道是湿润、高透过性的粘膜结构，几乎所有流动性好的小分子都能渗透，按“长时间呼吸”的题设等于连续静脉注射；能大量进入人体内环境、长期存在且无毒的物质目前看几乎只有水（生理盐水）。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为第三关是呼吸动力：人体自主呼吸肌不强健，驱动液体须借助呼吸机一类外部动力，效果类似“灌进去、抽出来”；否则呼吸肌群会疲劳到代谢废物积累、剧烈酸痛甚至自主抽搐、呼吸紊乱，最终还是致命的。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为第四关是由液转气时的半液半气状态：液体在肺泡中潴留、含氧被耗尽而二氧化碳饱和，除非该液体在体温下从空气捕获氧气与释放二氧化碳的能力强到与空气本身相当，否则会变成乏氧液体并成为肺泡与空气之间的阻隔。", "evidence": ["E11", "E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者指出若不能足够快排除这些液体，人就要依赖仅露出几分之一交换面积的肺泡呼吸一段时间，这很危险，甚至能导致窒息而死；除非上ECMO先把肺替代很长时间，长到能等肺把剩余液体吸收掉。", "evidence": ["E13", "E14"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者综合判断液体呼吸不太现实，并称科幻电影里“装满营养液的人体培养皿”若没有配一根呼吸管就根本不靠谱。", "evidence": ["E15", "E16"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为临床上液体悬浮的主要可能意义是让大面积烧伤这类不宜与床接触的患者以更温柔的方式休养，这种情况没有必要连呼吸都替代掉（“泡归泡，为什么不配根氧气管呢？”）。", "evidence": ["E17"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为对科幻作品而言，泡在液体里勉强可以对支撑人体对抗高G力起到一点积极作用；但《环太平洋》那样的动作投射机制下动作会很迟缓、没有实际意义，姿势修正速度跟不上失衡节奏，铁定会摔跟头摔死。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者就 EVA 提问：既然是神经联通意识同步机制，为什么不搞无线传输、要把人装在机身上扛高G力；并以玩笑归因（庵野国贼根本不相信日本能在毁灭之前搞好5G）和“必须天诛之”作结。", "evidence": ["E20", "E21", "E22"]}
   ],
   "argument_steps": [
    "判定问题复杂，提出四关框架（P001、P002）。",
    "第一关：血氧交换效率有希望、最容易（P003、P004）。",
    "第二关：粘膜高透过性使溶剂等于被持续注入体内，无毒且可长期大量存在的物质几乎只有生理盐水（P005-P007）。",
    "第三关：呼吸肌动力不足以驱动液体，需外部设备，否则肌肉疲劳、代谢废物积累、呼吸紊乱乃至致命（P008、P009）。",
    "第四关：由液转气的半液半气阶段会形成乏氧液体与阻隔，除非液体本身换气能力与空气相当（P010-P012）。",
    "补充风险：不能快速排液就要靠极小交换面积呼吸，危险甚至窒息；除非长期上ECMO（P013、P014）。",
    "结论：不太现实；科幻培养皿须配呼吸管（P015、P016）。",
    "临床意义澄清：液体悬浮用于大面积烧伤休养，不必替代呼吸（P017）。",
    "科幻评论：抗高G力作用有限，《环太平洋》机制下反而有害（P018、P019）。",
    "以 EVA 提问与动漫吐槽收尾（P020-P022）。"
   ],
   "concept_usage": [
    {"term": "血氧交换效率", "meaning": "第一关所指：液体在微观层面载氧并与血液交换的能力。", "evidence": "P003", "ambiguity": "未给出定量门槛。"},
    {"term": "高透过性的粘膜结构", "meaning": "作者用来解释溶剂会被呼吸道吸收，因而第二关难。", "evidence": "P006", "ambiguity": "为定性的生理描述，未给出具体通透率。"},
    {"term": "呼吸动力", "meaning": "第三关所指：呼吸肌驱动液体进出肺部的能力，需外部设备补充。", "evidence": "P009", "ambiguity": "未给出所需压力或流量数值。"},
    {"term": "ECMO", "meaning": "体外膜肺氧合，作者作为极端替代方案提及。", "evidence": "P014", "ambiguity": "正文未展开其原理与代价。"},
    {"term": "G力", "meaning": "加速度载荷；作者用它评价科幻作品中液体浸泡的作用。", "evidence": "P018", "ambiguity": "未给出量化分析。"},
    {"term": "液体悬浮", "meaning": "临床语境下用液体让患者悬浮休养的方式，作者称其有烧伤场景的意义。", "evidence": "P017", "ambiguity": "作者未提供临床依据或案例。"}
   ],
   "examples_and_targets": [
    "“装满营养液的人体培养皿”：作者评论的科幻电影设定（P016）。",
    "氧气管：作者提出的替代方案（P017）。",
    "ECMO：作者举出的替代肺的方案（P014）。",
    "《环太平洋》：作者评论的科幻作品及其动作投射机制（P019）。",
    "EVA、庵野（庵野国贼）：作者评论对象与调侃（P020、P021）。",
    "5G：作者玩笑式归因的对象（P021）。",
    "“灌进去、抽出来”：作者对液体呼吸设备工作方式的类比（P009）。",
    "生理盐水：作者举出的唯一符合条件（无毒、可长期大量存在）的物质（P007）。"
   ],
   "conditions": [
    "P004 以“假设某个液体有足够的载氧量，能与空气匹敌，而且无碍于交换过程”为条件，称第一关有希望。",
    "P007 以“考虑到‘长时间呼吸’这个题设”为前提，把溶剂问题等同于持续静脉注射。",
    "P012 以“除非这种液体在体温状态下有足够的从空气中自然捕获氧气和释放二氧化碳的能力……”为条件。",
    "P013 以“如果你不能足够快的把它们排除”为条件，指出窒息风险。",
    "P014 以“除非你上ECMO……前提还是这个液体对人体无毒”为条件，并追问“这意义何在呢”。",
    "P016 以“如果没有配一根呼吸管”为条件，称培养皿不靠谱。",
    "P017 指出临床场景中“没有必要连呼吸都替代掉”。",
    "P018 用“算是勉强可以……起到一点积极作用”作限定。"
   ],
   "rhetoric_and_tone": "科普式分关论证（第一关至第四关），用口语类比（“灌进去、抽出来”“泡归泡”）；结尾突然转入动漫吐槽与玩笑威胁（“庵野国贼根本不相信日本能在毁灭之前搞好5G！”“必须天诛之！”），语气从严谨转为戏谑，属修辞而非论证。",
   "unresolved_questions": [
    "正文未提及现实中被研究过的具体液体（全氟化碳等），只说“几乎只有水——还得是生理盐水”，该判断的依据与时间范围未给出，需外部核查。",
    "“四关”是否为全部障碍、其排序依据本文未说明。",
    "P019 对《环太平洋》动作投射机制、P020 对 EVA 设定的描述是否准确，需外部核查；作者对作品设定的理解不属本文论证。",
    "“庵野国贼”所指（庵野秀明？）正文未点名，需研究者判断；该句为调侃。",
    "ECMO 替代肺“周期只怕要以天来计”为作者估计，未给出依据。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个问题其实蛮复杂的。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "要做到这一点，要闯过四关：", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这一关是有希望的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这是最容易的一关。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "因为肺和整个呼吸道显然不是塑料做的，而是非常湿润和高透过性的粘膜结构，这意味着几乎所有流动性好的小分子都是可以渗透过去的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这就跟拿这个溶剂连续不断做静脉注射没什么本质区别。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "而能大量进入人体内环境，而且长期存在，并且不具有毒性的物质，目前看几乎只有水——还得是生理盐水。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "人体自主呼吸的肌肉并不是很强健，并不能造成很大的呼吸动力。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "这意味着如果要以液体来呼吸，这个液体也必须借助呼吸机一类的设备来提供外部动力。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "很快呼吸肌群就会疲劳到积累过多代谢废物，发生剧烈酸痛甚至自主抽搐，导致呼吸紊乱。最终还是致命的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "由液转气的过程中，会有一个半液半气的呼吸状态。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "除非这种液体在体温状态下有足够的从空气中自然捕获氧气和释放二氧化碳的能力，强到能与空气本身的交换能力相当，否则这些液体一定会变成乏氧液体，并且变成肺泡与空气之间的阻隔。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "这时候如果你不能足够快的把它们排除，人就要依赖仅露出几分之一交换面积的肺泡呼吸一段时间。这很危险，甚至能导致窒息而死。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "除非你上ECMO，先把肺替代很长时间，长到能等肺把剩余的液体干脆吸收掉", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P015", "quote": "所以综合起来说，这个是不太现实的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "换言之，科幻电影里的那种“装满营养液的人体培养皿”，如果没有配一根呼吸管，是根本不靠谱的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "这种情况是没有必要连呼吸都替代掉的。泡归泡，为什么不配根氧气管呢？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "对科幻作品，泡在液体里算是勉强可以对支撑人体对抗高G力起到一点积极作用。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "泡在液体里动作会很迟缓，没有实际意义——铁定会摔跟头摔死，因为姿势修正速度跟不上失衡的节奏。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "而在EVA里面，你是神经联通意识同步机制，为什么不搞无线传输，要把人装在机身上去扛高G力？因为网络延迟太大？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "真相是，庵野国贼根本不相信日本能在毁灭之前搞好5G！", "relation": "context"},
    {"key": "E22", "paragraph_id": "P022", "quote": "必须天诛之！", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生理学／医学", "科幻设定评析", "流体与呼吸力学"],
   "issue_candidates": ["液体呼吸的可行性", "呼吸道通透性与溶剂毒性", "呼吸动力与设备依赖", "科幻作品中的液体浸泡设定"],
   "text_function_candidates": ["答疑", "科普解释", "评论", "调侃"],
   "object_candidates": ["哺乳动物", "肺与呼吸道", "ECMO", "《环太平洋》", "EVA", "庵野（未点名全名）"],
   "working_keywords": ["液相呼吸", "血氧交换", "载氧量", "生理盐水", "呼吸动力", "ECMO", "高G力", "营养液", "5G"]
  },
  "notes": "正文无图片节点。brief 为正文语句摘录，仅作导航。正文前段为四关分析，末两段转入动漫调侃（庵野国贼、必须天诛之），属修辞语气，已如实记录。"
 },
 "75830681": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎么评价「入关学」？”。作者直接否定其特别性与合理性（P001、P002），转而预测中美将长期两强并立、亦敌亦友，并认为“入关”既不符合中国利益、也不应该做（P003-P010）；随后给出“成熟”的标准，断言若真把“入关”作为战略目标则尚未起步已注定失败（P011-P015）；作者真正忧虑的是“入关立威”这一美式帝国梦在中国有很多拥趸，认为这不是爱国而是以国为器，注定失望乃至惨败（P016-P025）；最后把“入关学”评为“不太健康但饱受欢迎的儿童玩具”（P026-P028）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总评：入关学本身没什么特别，只是历史俄狄浦斯情结的东方对称物，戏剧性还不如“杀父娶母”；其若干假设在全球化的现代都不成立。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "中美关系预测：将长期两强并立、瓜葛纠缠、亦敌亦友，非少数政治人物或党派所能对抗；“分久必合、合久必分”的“狗血青春剧”阶段大概持续上百年，直到彼此越来越像、难以分出彼此为止；现在是第二轮闹且中国眼看占上风。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "反驳“入关”的必要性：深刻伤害美国甚至威胁其安全不符合中国利益，美国也会认识到破坏中国稳定不符合美国利益；这不是能不能做到，而是就算能做到也不应该这样做。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "给出“成熟”的标准：明白世界不是都和自己一样就最好、不是杀死“恶龙”就天下大吉，懂得不为已甚、适可而止、君子之争、克己复礼。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "断言中国若真把“入关”作为战略目标则尚未起步已注定失败——不是没机会“入关”，而是入了“关”恐无百年之运；中国是永恒之国，不太可能为几十年的耀武扬威选择祸根深种的霸道。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018"], "summary": "指出真正忧虑：入关立威的霸道愿景实质是美式帝国梦，拥护者是在期待中国成为新的美国——不是基于中国文化传统期待“天下为公、世界大同”的中国梦，而是基于美国文化心理希望中国实现“宝刀屠龙，号令天下”的美国梦。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "论断该倾向对中国、美国乃至世界都是极大的不祥；这不是爱国，而是以国为器追求自我满足、置天下苍生于不顾；因本质上出于欲念而非爱，最终不可能得到真正广泛支持，注定失望且有极大可能带来深刻惨败。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "反问与归结：如果觉得今天美国狼狈不堪令人扬眉吐气，何以要梦想中国取而代之；鼓吹称霸是唯一扬眉吐气之道，唯一值得原谅的理由只能是幼稚；希望中国永不做称霸这种蠢事。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P026", "P027", "P028"], "summary": "总评收束：入关学是一种不太健康但饱受欢迎的儿童玩具、将来长大后会羞于提起的荒唐往事；“最好就是如此”，否则就不是天佑中华或天佑美利坚的问题，而是愿天佑人类了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“入关学”的观点本身没什么特别，只是一种历史俄狄浦斯情结的东方对称物，论戏剧性和观赏性还比不上“杀父娶母”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“入关学”本身没有啥合理性，因为它的若干假设在全球化的现代都是不成立的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测中美将来会长期两强并立、瓜葛纠缠、亦敌亦友，这不是少数政治人物或党派的能力所能对抗的，甚至两国民众自己也不可能对抗。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者把中美关系描述为“分久必合、合久必分”的活冤家，并预测这个“离了想和、合了想离的狗血青春剧阶段”大概会持续上百年，直到两边人民难以分出彼此为止。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这一轮闹中中国眼看要占上风，所以“bumpy了一点，习惯了就好了”。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张深刻伤害美国甚至威胁美国安全并不符合中国利益，美国也会认识到破坏中国稳定绝不符合美国利益；这不是能不能做到的问题，而是就算能做到也不应该这样做。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出“成熟”的含义：明白世界不是都和自己一样就最好、不是把“恶龙”杀死就会天下大吉，懂得不为已甚、适可而止、君子之争、克己复礼。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者断言中国若真把“入关”作为战略目标则尚未起步已注定失败——不是说没机会“入关”，而是入了“关”恐无百年之运。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国是永恒之国，从其文化传承上讲不太可能为了几十年的耀武扬威去选择祸根深种的霸道。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者真正忧虑的是“入关立威”的霸道愿景——实质是美式帝国梦——在中国有如此多的拥趸；拥护者是在期待中国成为一个新的美国。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分中国梦与美国梦：拥护者不是基于中国文化传统期待“天下为公、世界大同”的中国梦，而是基于美国的文化心理希望中国实现“宝刀屠龙，号令天下，莫敢不从”的美国梦。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者断言这种倾向太强，对中国、美国乃至世界都是极大的不祥；这不是爱国，而是以国为器追求自我满足、置天下苍生于不顾。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为这想法本质上出于欲念而非爱，最终不可能得到真正的广泛支持、注定失望，而且有极大可能带来深刻的惨败。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：如果觉得今天的美国狼狈不堪令世人扬眉吐气，那么何以要梦想中国应该取其而代之？逻辑何在？", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为鼓吹称霸是唯一扬眉吐气之道，唯一值得原谅的理由只能是幼稚；并表示希望中国永不做称霸这种蠢事。", "evidence": ["E22", "E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者总结“入关学”只是一种不太健康但饱受欢迎的儿童玩具、将来长大后会羞于对人提起的荒唐往事；否则就不是“天佑中华”“天佑美利坚”的问题，而是愿天佑人类了。", "evidence": ["E24", "E25"]}
   ],
   "argument_steps": [
    "总评：入关学无特别之处、无合理性，其假设在全球化现代不成立（P001、P002）。",
    "给出中美关系预测：长期两强并立、亦敌亦友、上百年“狗血青春剧”（P003-P007）。",
    "反驳“入关”的必要性：伤害美国不符合中国利益，也不应该这样做（P008-P010）。",
    "界定“成熟”：不为已甚、适可而止、君子之争、克己复礼（P011、P012）。",
    "断言以“入关”为战略目标尚未起步已注定失败，入了关也无百年之运；中国是永恒之国（P013-P015）。",
    "指出真正忧虑：入关立威愿景是美式帝国梦，拥护者期待中国成为新美国（P016-P018）。",
    "论断该倾向对中美与世界都不祥；非爱国，而是以国为器；因出于欲念而注定失望乃至惨败（P019-P021）。",
    "反问与归结：鼓吹称霸唯一值得原谅的理由只能是幼稚；希望中国永不做这种蠢事（P022-P025）。",
    "总评收束：入关学是儿童玩具；否则只能愿天佑人类（P026-P028）。"
   ],
   "concept_usage": [
    {"term": "入关学", "meaning": "本文的评论对象，作者称其观点无特别之处、若干假设在全球化现代不成立；正文未介绍其具体主张与提出者。", "evidence": "P001", "ambiguity": "“入关学”的具体内容与代表人物本文未说明。"},
    {"term": "历史俄狄浦斯情结的东方对称物", "meaning": "作者对“入关学”的概括性比喻，指其戏剧结构。", "evidence": "P001", "ambiguity": "作者未展开该比喻的对应关系。"},
    {"term": "霸道", "meaning": "作者用来指“入关立威”式、以武力和耀武扬威为路径的选择，称其祸根深种。", "evidence": "P015", "ambiguity": "未与“王道”对举定义，也未给出判定标准。"},
    {"term": "中国梦／美国梦", "meaning": "作者区分：中国梦是“天下为公、世界大同”，美国梦是“宝刀屠龙，号令天下，莫敢不从”。", "evidence": "P018", "ambiguity": "两处引语的出处本文未标注；作者对两种“梦”的界定未展开。"},
    {"term": "成熟", "meaning": "本文中指懂得不为已甚、适可而止、君子之争、克己复礼。", "evidence": "P011", "ambiguity": "未说明判断成熟与否的标准。"},
    {"term": "以国为器", "meaning": "作者用来批评把国家当作满足自我欲望的工具。", "evidence": "P020", "ambiguity": "未给出具体所指对象。"},
    {"term": "永恒之国", "meaning": "作者对中国的称呼，用来说明其不太可能选择短视的霸道。", "evidence": "P015", "ambiguity": "未给出依据。"}
   ],
   "examples_and_targets": [
    "“入关学”及其拥护者：作者的主要评论与批评对象（P001、P002、P016、P017）。",
    "“杀父娶母”：作者引自希腊神话/戏剧的类比材料（P001）。",
    "“分久必合、合久必分”：作者引用的俗语，用于描述中美关系（P004）。",
    "“恶龙”：作者比喻（P011）。",
    "“天下为公、世界大同”：作者引语，指中国梦（P018）。",
    "“宝刀屠龙，号令天下，莫敢不从”：作者引语，指美国梦（P018）。",
    "“天佑中华”“天佑美利坚”：作者引语式收尾（P028）。",
    "bumpy：作者插入的英文词（P007）。",
    "“儿童玩具”：作者比喻（P026）。"
   ],
   "conditions": [
    "P002 以“因为它的若干假设在全球化的现代都是不成立的”给出否定理由。",
    "P005、P006 以“直到……为止”给出该阶段持续的终点条件。",
    "P007 以“现在这是第二轮闹”限定当下处境。",
    "P010 以“这并不是能不能做到的问题，而是就算能做到、也不应该这样做的问题”区分可行性与正当性。",
    "P014 以“不是说它没机会‘入关’，而是说它入了‘关’恐无百年之运”区分机会与后果。",
    "P022 以“如果你觉得今天的美国狼狈不堪令世人扬眉吐气”为假设前提反问。",
    "P024 以“唯一值得原谅的理由只能是幼稚”作限定式判断。",
    "P026 用“不太健康但饱受欢迎”作双重限定。"
   ],
   "rhetoric_and_tone": "评论兼论辩，语带讥讽与戏谑（“狗血戏码”“狗血青春剧”“儿童玩具”“荒唐往事”），使用历史与文学典故、俗语与金庸式引语；设问反问并用（“入什么关？关在哪？”“逻辑何在？”），结尾以“愿天佑人类”作庄重收束；夹入英文词（bumpy）。",
   "unresolved_questions": [
    "正文未介绍“入关学”的提出者、具体主张与流行背景，需外部核查。",
    "“历史俄狄浦斯情结的东方对称物”的含义与依据本文未展开。",
    "“这几十年的耀武扬威”“第二轮闹”等时间指涉未明确。",
    "“大概会持续上百年”为作者估计，依据未给出。",
    "“天下为公、世界大同”“宝刀屠龙，号令天下，莫敢不从”等引语出处本文未标注，需外部核查。",
    "作者称“中国是永恒之国”“不太可能……”为概括性历史判断，本文未提供论证。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“入关学”的观点本身没什么特别的，只是一种历史俄狄浦斯情结的东方对称物。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它本身没有啥合理性，因为它的若干假设在全球化的现代都是不成立的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "中美将来会长期两强并立，瓜葛纠缠，亦敌亦友。这不是以少数政治人物、少数党派的能力所能对抗的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "中美关系在可见的将来只能是“分久必合、合久必分”的活冤家。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这个离了想和，合了想离的狗血青春剧阶段大概会持续上百年。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "直到美国不断的变得更像中国，而中国不断的变得更像美国，直到两边的人民已经难以分得出彼此", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "现在这是第二轮闹，而且是第一回中国眼看要占上风，所以bumpy了一点，习惯了就好了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "真的深刻的伤害美国甚至威胁到美国的安全并不符合中国的利益", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "这并不是能不能做到的问题，而是就算能做到、也不应该这样做的问题。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "成熟，意味着明白世界不是都和自己一样就最好，明白不是把“恶龙”杀死就会天下大吉，意味着懂得不为已甚，适可而止。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "意味着懂得何谓君子之争，克己复礼。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "中国如果真的把“入关“作为战略目标，则尚未起步，已经注定失败了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "不是说它没机会“入关”，而是说它入了“关”恐无百年之运。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "中国是永恒之国，从它自己一向的文化传承上讲，不太可能为了这么几十年的耀武扬威去选择祸根深种的霸道。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "我真正忧虑的是这个“入关立威”的霸道之愿景——这实质上是一个美式的帝国梦——在中国有如此多的拥趸。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "其实拥护这个愿景的人，是在期待中国成为一个新的美国。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "他们不是在基于中国的文化传统期待中国实现中国梦，那个“天下为公、世界大同”的梦，而是在基于美国的文化心理，希望中国实现一个美国梦", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "这样的倾向太强，对于中国、对于美国，乃至于对于世界都是极大的不祥。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "这并不是爱国，而是以国为器追求自我满足，置天下苍生于不顾。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "也正因为这想法本质上不是出于爱，而是出于欲念，最终是不可能得到真正的广泛支持，最终注定会失望，而且有极大的可能会带来深刻的惨败。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "如果你觉得今天的美国狼狈不堪令世人扬眉吐气，那么何以要梦想中国应该取其而代之？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "鼓吹称霸是唯一扬眉吐气之道，唯一值得原谅的理由只能是幼稚。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "希望中国永不做称霸这种蠢事。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "所谓“入关学”，只是一种不太健康但饱受欢迎的儿童玩具——那种你将来长大了会羞于对人提起的荒唐往事。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "不然就不是“天佑中华”“天佑美利坚”的问题了，是愿天佑人类了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系", "政治评论", "战略文化"],
   "issue_candidates": ["「入关学」的评价", "中美关系的走向", "称霸与帝国梦的批评", "中国梦与美国梦之别"],
   "text_function_candidates": ["答疑", "评论", "批评", "论辩"],
   "object_candidates": ["入关学及其拥护者", "中国", "美国", "中美两国人民"],
   "working_keywords": ["入关学", "入关立威", "霸道", "两强并立", "分久必合、合久必分", "中国梦", "美国梦", "以国为器", "成熟", "儿童玩具"]
  },
  "notes": "正文无图片节点。P013 原文中“入关“使用了两个前引号（原文如此），已逐字保留。brief 为正文语句摘录，仅作导航。"
 },
 "01ed2146": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么网络上有这么多人反对给每人直接发几千块钱，却支持信贷放水的提议？”，即请作者解释这一舆论现象。作者没有分析网络舆论或反对者的心理，而是直接给出自己的政策主张：反对“全民发现金”，改为向每个公民批准低息“专项贷款”并与社会信用体系挂钩（P001-P009）；随后论证该方案在中国因公共服务全民所有而操作成本低（P010-P014），并解释资本主义国家为何更可能选择直接发钱（P015、P016）；最后说明中国的“公民信用贷”额度可更高、且能积累信用数据、兑现制度优势，因而本质上“是赚的”（P017-P026）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出主张：反对“每个人发几千块”，更好的政策是给每个人批准一定的低息专项贷款额度，并把全民个人贷与社会信用体系挂钩。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "界定方案细节：专项贷款经申请直接划给指定公共服务账户；不需物质抵押、仅凭公民身份领取；违约会影响将来享受一切社会服务且不还清不能合法移民；无力偿还者可以承担社会服务抵偿；利息非零、不低于一般消费贷，但第一年免息。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "说明设计理由：这样有需要者会主动申请、不易滥用，既避免大量操作成本，也避免无成本资金冲击供求信号造成资源错配与无效率；将来可对教育等类别豁免利息。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "给出中国可行的制度前提：中国所有的重要公共服务几乎都是全民所有，“吃了中国的，你还是拉在中国的地里”，操作成本上简单易行。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "对照资本主义国家：他们也想到该方案，但法理原则上执行成本很大（无数公司须申请、鉴定、登记进入名单，手续复杂、时效几乎不现实）；该成本中国已以“国企欠缺效率”的方式买过单，而它们临时买单买不起（每人先摊掉几百美金会计与审计成本），因此对它们来说每人发几千块更现实，是“能做的最不坏的选择”。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "说明中国方案的规模空间：额度可随社会信用完美程度提高到十万、二十万甚至五十万，利息相应提高，甚至可无上限；理由是供应端在全民所有体系内，且要还本付息，不是风险不可控或亏本买卖；如期还款可以再借。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023"], "summary": "主张该措施能启动大量公民的金融信用积累，这些信用数据是远胜货币本身的真实财富，可支撑人民币扩张；有坚实基础的扩张会促进经济繁荣，而非“空卡路里”式通胀与局部失衡；本质上“是赚的”。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026"], "summary": "进一步主张：该措施将深刻改变公民社会的伦理关系、更全面兑现全民所有制的制度优势；宣布本身对人类都有震撼，从争夺舆论正当性看也“花得够本”；眼光放远可成为长期制度，本质上是扩大了的学贷；并重申因有更好选择而反对“全民发现金”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为每个人发几千块不是什么好政策，主张更好的政策是给每个人批准一定的低息专项贷款额度，并把全民个人贷与社会信用体系挂钩。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“专项贷款”：钱经申请直接划给指定的公共服务账户（水电煤气、登记房租、暖气、网络、公交、公立教育、统一基本食品供应等），不需物质抵押，仅凭公民身份即可领取。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出违约后果：有违约记录会影响将来享受一切社会服务，并且不还清不能合法移民；无力偿还者可以由承担一定社会服务来抵偿。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出利息安排：利息不是零、也不会特别显著低于一般消费贷，但可以第一年免息；将来可对某些类别的消费（如教育）豁免利息。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这样设计可使有需要的人主动申请、不易滥用，既避免大量操作成本，也避免无成本资金冲击供求信号导致市场资源错配和无效率。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为该方案在中国可行，是因为中国的重要公共服务几乎都是全民所有，“吃了中国的，你还是拉在中国的地里”，操作成本上简单易行。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为资本主义国家也想到该方案，但从法理原则上执行成本很大：无数公司须先申请、鉴定与登记进入可选供应商名单，手续复杂、时效几乎不现实。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出该成本对中国一样存在，只是中国从一开始就以“国企欠缺效率”的方式买过单；资本主义国家临时买单根本买不起，按此发救济每人先摊掉几百美金会计与审计成本。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断对这类国家来说每人发几千块更现实：姿态上可接受、经济上恶果不彰、心理上可延缓动乱，至少把领导层对动乱的责任降到可承受程度；这不是理想选择，而是“能做的最不坏的选择”。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者主张中国的“公民信用贷”额度可随社会信用完美程度一口气提高到十万、二十万甚至五十万，利息也相应提高，甚至可以是无上限的。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出理由：供应端掌握在全民所有体系之中，且款项不但要还、还有利息，所以这不是风险不可控、不可持续的措施，也不是亏本买卖，上限可远高于几千块、一次性这些限制；如期还款还可以再借。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者主张该措施能启动大量公民的金融信用积累，这些信用数据是远胜货币本身的真实财富，仅依靠它们人民币都会得到进一步扩张的坚实基础；有坚实基础的扩张会促进经济进一步繁荣，而不是“空卡路里”式地造成通胀和局部失衡。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断该措施本质上是赚的、赚得还不少，赚的不只是账面上的金钱；它将深刻改变公民社会的伦理关系、更深更全面地兑现全民所有制的制度优势。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为一旦宣布，对人类都是一种会触发深刻反思的震撼，哪怕仅从争夺舆论正当性出发这几千亿也花得够本（何况要还、有利息）；眼光辽阔一些，它可成为长期制度，本质上是一种扩大了的学贷。", "evidence": ["E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结：因为有更好的选择存在，所以反对“全民发现金”。", "evidence": ["E25"]}
   ],
   "argument_steps": [
    "提出主张：反对全民发现金，改行低息专项贷款并与社会信用体系挂钩（P001、P002）。",
    "界定方案：直接划入指定公共服务账户、凭公民身份领取、违约影响社会服务与移民、可以社会服务抵偿、第一年免息（P003-P007）。",
    "说明设计理由：主动申请、防止滥用、避免操作成本与无成本资金对供求信号的冲击（P008）。",
    "补充可豁免利息的类别（教育）（P009）。",
    "中国可行的制度前提：重要公共服务几乎全民所有，操作成本低（P010、P011）。",
    "对照资本主义国家：法理与登记成本高，临时买单买不起，故其选择发钱是“最不坏的选择”（P012-P016）。",
    "中国方案的规模空间：额度可提高到十万、二十万、五十万甚至无上限，因供应端全民所有且要还本付息（P017-P020）。",
    "收益论证：启动信用数据积累、支撑人民币扩张、促进繁荣而非通胀与失衡；本质上“是赚的”（P021-P023）。",
    "政治与制度收益：改变伦理关系、兑现全民所有制优势、争夺舆论正当性、可成为长期制度（扩大了的学贷）（P024、P025）。",
    "结论：因有更好选择而反对“全民发现金”（P026）。"
   ],
   "concept_usage": [
    {"term": "专项贷款／公民信用贷", "meaning": "作者提出的政策工具：低息、需申请、直接支付给指定公共服务账户，并与社会信用体系挂钩的个人贷款。", "evidence": "P002", "ambiguity": "额度、利率、期限的具体决定机制本文未给出。"},
    {"term": "社会信用体系", "meaning": "作者主张与之挂钩的信用制度，违约记录会影响享受一切社会服务并影响合法移民。", "evidence": "P005", "ambiguity": "该体系的现行范围与法理依据本文未说明。"},
    {"term": "全民所有", "meaning": "作者称中国重要公共服务几乎都是全民所有，因而供应端掌握在体系内、操作成本低。", "evidence": "P010", "ambiguity": "未说明“全民所有”在具体服务上的覆盖与例外。"},
    {"term": "空卡路里", "meaning": "作者用来形容无坚实基础的货币扩张：只造成通胀和局部失衡，不促进繁荣。", "evidence": "P022", "ambiguity": "为比喻说法，未给出量化判据。"},
    {"term": "供求信号", "meaning": "作者认为无成本资金会冲击价格信号，导致市场资源错配与无效率。", "evidence": "P008", "ambiguity": "未说明该机制在何种规模下成立。"},
    {"term": "舆论正当性", "meaning": "作者称仅从争夺舆论正当性出发，这笔支出“也花得够本”。", "evidence": "P024", "ambiguity": "未说明衡量方式。"},
    {"term": "学贷", "meaning": "作者把该长期制度类比为“扩大了的学贷”。", "evidence": "P025", "ambiguity": "类比的具体对应关系未展开。"}
   ],
   "examples_and_targets": [
    "水、电、煤气、经登记的房屋租金、暖气、网络、公交、公立教育、统一基本食品供应服务：作者列举的指定公共服务账户（P003）。",
    "资本主义国家：作者的对照对象，称其更可能选择发钱（P012、P015）。",
    "“国企欠缺效率”：作者引述的说法，用来指中国已付出的制度成本（P013）。",
    "几百美金会计与审计成本：作者对资本主义国家执行该方案成本的估计（P014）。",
    "“吃了中国的，你还是拉在中国的地里”：作者的口语比喻（P010）。",
    "几千亿：作者对宣布该措施所涉规模的估计（P024）。",
    "学贷：作者的类比（P025）。"
   ],
   "conditions": [
    "P001 以“不是什么好政策”作否定判断，P026 以“因为有更好的选择存在，所以……”给出理由。",
    "P005 以“如果有违约记录”为条件说明后果。",
    "P007 用“不是零，也并不会特别显著的低”与“但是可以第一年免息”作双重限定。",
    "P008 以“这样……自然会……也不容易……”说明预期效果。",
    "P010 以“之所以这样建议，是因为……”给出制度前提。",
    "P012 以“考虑到为了保证基本公平”为前提说明手续必然复杂。",
    "P017 以“可以根据社会信用的完美程度”为条件设定额度。",
    "P019 以“因为首先……而且不是给了不用还”给出上限可放宽的理由。",
    "P024 用“一旦宣布”假定该措施落地；P025 用“如果眼光辽阔一些”作前瞻。",
    "P016 用“绝不是……而是……”强调这是“最不坏的选择”。"
   ],
   "rhetoric_and_tone": "政策建议体，条列式给出设计细节与理由，夹杂口语比喻（“吃了中国的，你还是拉在中国的地里”）与对资本主义国家的讥讽（“哪家企业不想登记？凭什么不给登记？”）；结尾直接给出反对结论；使用“空卡路里”“最不坏的选择”等自造或引号式表述。",
   "unresolved_questions": [
    "提问问“为什么有这么多人反对发钱却支持信贷放水”，正文未分析网络舆论或反对者的心理，而是给出自己的替代方案，问答对应关系需研究者判断。",
    "“几千亿”“几百美金”等数字为作者估计，依据未给出，需外部核查。",
    "“社会信用体系”“不还清不能合法移民”“无力偿还者以社会服务抵偿”等设想的法律与制度可行性本文未说明，需外部核查。",
    "“人民币都会得到进一步扩张的坚实基础”等货币论断本文未给出论证。",
    "“资本主义国家”的范围与所指未明确。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "每个人发几千块不是什么好政策。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "更好的政策是给每个人批准一定的低息专项贷款额度，并将这种全民个人贷与社会信用体系挂钩。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "所谓专项贷款，是指这笔钱会经由申请直接划给指定的公共服务账户", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不需要任何物质抵押，仅凭公民身份就可以领取。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "如果有违约记录，会影响到将来享受一切社会服务，并且不还清不能合法移民。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "无力偿还者，可以由承担一定社会服务来抵偿。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "利息不是零，也并不会特别显著的低于一般消费贷，但是可以第一年免息。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "在将来可以对某些类别的消费豁免贷款利息——比如用于教育的部分。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "无成本的资金一定会冲击供求信号，导致市场资源的错配和无效率。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "之所以这样建议，是因为中国在这方面有特殊的制度特性——中国所有的重要公共服务几乎都是全民所有的。吃了中国的，你还是拉在中国的地里。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "这就在操作成本上一下变得简单易行了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "资本主义国家自然也想到了这个方案，但是它们从法理原则上要执行这个方案就有很大的成本", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "只是中国从一开始就以“国企欠缺效率”的方式买过单了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "而资本主义国家临时想用，临时买单是根本买不起的", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "所以，对它们来说，每人发个几千块更现实。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "这绝不是因为这对他们是理想的选择，而是因为这对它们是能做的最不坏的选择。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "这种“公民信用贷”的额度可以根据社会信用的完美程度一口气提高到十万、二十万、甚至五十万的等级", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "甚至可以是无上限的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "因为首先供应端就掌握在全民所有体系之中，而且不是给了不用还，而是不但要还、还有利息的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "这些信用数据本身是远胜货币本身的真实财富", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "它会促进经济活动的进一步繁荣而不是所谓空卡路里单纯的造成通胀和局部失衡。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "换句话说——这个措施本质上是赚的，甚至赚得还不少，赚的不只是账面上的金钱。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "这笔公民信用贷将会深刻的改变公民社会的伦理关系，更深更全面的兑现全民所有制的制度优势。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P025", "quote": "如果眼光辽阔一些，它甚至可以以此为契机和先导测试，成为一种长期制度。本质上讲，这其实是一种扩大了的学贷。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P026", "quote": "因为有更好的选择存在，所以我反对“全民发现金”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["经济政策", "财政与货币", "社会保障"],
   "issue_candidates": ["全民发现金与信贷放水之争", "专项贷款与社会信用体系挂钩", "公共服务全民所有的制度优势", "信用数据与货币扩张"],
   "text_function_candidates": ["答疑（转为政策建议）", "政策建议", "论证"],
   "object_candidates": ["中国", "资本主义国家", "公民", "全民所有制", "国企"],
   "working_keywords": ["专项贷款", "公民信用贷", "社会信用体系", "全民发现金", "信贷放水", "全民所有", "空卡路里", "供求信号", "学贷", "舆论正当性"]
  },
  "notes": "正文无图片节点。提问问的是网络舆论现象，正文未分析舆论，而是给出替代政策方案并说明其理由；已按正文实际论述记录，未据提问补写。brief 为正文语句摘录，仅作导航。"
 },
 "33c3a852": {
  "analysis": {
   "question_context": "提问者（Q001）自述“被网络暴力的有点严重，现在心里有点想不开，不敢找别人求助”，请人开导。作者未回应其心理危机，而是给出战术性建议：善用合法武力，在有准备的阵地上按对你有利的规则作战（P001、P002）；以知乎为例，主张冲突意见要写自己的答案而非去别人评论区发评论，自己的评论区就是预设阵地（P003、P004）；随后给出屏蔽、不回复、让对方写独立答案、避开无删评与拉黑权的平台等具体做法（P006-P012），并预言人人明白该规则后网暴会渐渐消失（P013）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出总原则：善用合法武力，在有准备的阵地上按照对自己有利的规则作战，这是永恒的战术。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "以知乎为例：有冲突的意见不去看起来品格不好的人的评论区发评论，而要自己写答案；自己的评论区是预设阵地，没人能在这里占优势；P005 为两条其他问题标题（未覆盖片段）。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "具体做法之一：隔空对骂可屏蔽对方，等于让其静音，对方声嘶力竭却知道你听不见，这本身就是反击；看三无小号在评论区未能得逞、“实名反对”点赞不过十，算一种“邪恶的福利”。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "做法之二：让对方发在自己评论区并积极回复是最帮对方忙的行为；要公平竞争就欢迎对方写独立答案、让观点对等列出，让其自己体会没有预设立场下有多少人赞成；并称“你从来没占下风，你当然不会再跑来哭诉求援”，让不懂规则的人去哭诉求援。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "做法之三：不要去不给作者删评论权和拉黑权的平台，因为那里没有这种有利阵地；并引“千金之子，坐不垂堂；君子不立危墙之下”。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P013"], "summary": "结论性预测：如果人人都明白这个规则，网暴者自己才是弱势群体，网暴自然就渐渐消失了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出总原则：善用合法武力，在有准备的阵地上按照对你有利的规则作战，这是永恒的战术。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以知乎为例建议：有冲突的意见不要去看起来品格不好的人的评论区发评论，而要自己写答案；自己的评论区就是预设阵地，没人能在这里对你占优势。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对隔空对骂者可以屏蔽，等于让其静音；对方声嘶力竭却心知肚明你根本听不见，这本身就是反击。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称看着三无小号在评论区没能得逞、自己写“实名反对”却点赞数不超过十个，也算是一种“邪恶的福利”。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出让对方发在自己评论区并积极回复是最帮对方忙的行为；要公平竞争就欢迎对方自己写独立答案，让观点对等列出，让对方自己体会在没有预设立场下有多少人赞成以及“那份孤独和寂寞”。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言“你从来没占下风，你当然不会再跑来哭诉求援”，并让不懂这些规则的人去哭诉求援。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议不要去那种不给作者删评论权和拉黑权的平台，因为那里没有这种有利阵地；并引“千金之子，坐不垂堂；君子不立危墙之下”。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预言：如果人人都明白了这个规则，网暴者自己才是弱势群体，网暴自然就渐渐消失了。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "给出总原则：善用合法武力、在有准备的阵地上按有利规则作战（P001、P002）。",
    "以知乎为例说明何为预设阵地：自己写答案而非去他人评论区（P003、P004）。",
    "具体做法一：屏蔽隔空对骂者，让对方“静音”，这本身就是反击（P006）。",
    "补充心理收益：看小号未能得逞是一种“邪恶的福利”（P007）。",
    "具体做法二：不要让对方在自己评论区获得曝光与回复；欢迎其写独立答案并对等比较（P008）。",
    "断言与劝告：不占下风者不会哭诉求援；让不懂规则的人去哭诉求援（P009、P010）。",
    "具体做法三：避开不提供删评与拉黑权的平台，并引古语（P011、P012）。",
    "结论性预测：人人明白规则后网暴者成为弱势群体，网暴渐渐消失（P013）。"
   ],
   "concept_usage": [
    {"term": "合法武力", "meaning": "本文中指平台规则允许的操作（自己写答案、屏蔽、删评论、拉黑），“合法”即不违反平台规则与法律。", "evidence": "P001", "ambiguity": "作者未系统界定“合法武力”的边界（是否包括举报、公开挂人等）。"},
    {"term": "预设阵地／有利阵地", "meaning": "指自己的答案与评论区：作者认为在这里自己占规则优势。", "evidence": "P004", "ambiguity": "为军事比喻，未说明不同平台规则差异的具体影响。"},
    {"term": "三无小号", "meaning": "作者对无头像、无简介、无内容一类账号的称呼。", "evidence": "P007", "ambiguity": "未给出严格定义。"},
    {"term": "“实名反对”", "meaning": "作者加引号引用的平台行为／说法，指写长文公开反对。", "evidence": "P007", "ambiguity": "作者未说明具体所指。"},
    {"term": "邪恶的福利", "meaning": "作者自造的说法，指看到攻击者受挫时获得的快感。", "evidence": "P007", "ambiguity": "为调侃用语。"}
   ],
   "examples_and_targets": [
    "知乎：作者举例的平台（P003）。",
    "三无小号与“实名反对”：作者举出的现象（P007）。",
    "“千金之子，坐不垂堂；君子不立危墙之下”：作者引用的古语（P012）。",
    "P005 的两条其他知乎问题标题（“面对喷子，你的心理感受是怎样的？有哪些妥善的应对方式？”“怎么控制自己不被傻逼气到?”）：lexical未覆盖片段，功能未说明。",
    "提问者自述的“被网络暴力”“心里有点想不开”“不敢找别人求助”：提问者语境（Q001），正文未回应其心理危机。"
   ],
   "conditions": [
    "P003 以“拿知乎举个例子”标明举例。",
    "P006 以“如果对方和你隔空对骂”为条件给出屏蔽做法。",
    "P008 以“要公平竞争的话”为条件给出让对方写独立答案的做法。",
    "P011 以“不要去那种不给作者删评论权和拉黑权的平台”为条件提出平台选择建议。",
    "P013 以“如果人人都明白了这个规则”为条件作出预测。",
    "P004 以“没人能在这里对你占优势”作断言式限定。"
   ],
   "rhetoric_and_tone": "战术/军事比喻贯穿全篇（阵地、作战、占下风、弱势群体），对求助者以第二人称直接指导，语气笃定并带攻击性调侃（“邪恶的福利”“让那些不懂这些规则的人去哭诉求援去”）；引古语作依据；全篇未涉及心理疏导或求助建议。",
   "unresolved_questions": [
    "提问者自述“心里有点想不开”，正文未回应心理危机、未建议求助专业人士或他人，只给出平台战术建议，此点需研究者注意。",
    "P005 为“⚠lexical未覆盖片段”，正文含两条其他知乎问题标题（其中含粗口“傻逼”），其功能（链接或推荐位）及是否属正文未说明。",
    "“合法武力”的边界（是否包括举报、公开他人信息等）本文未说明。",
    "作者建议依赖平台的删评与拉黑功能，但未讨论平台不提供该功能或规则变化时的替代方案。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "善用合法武力，在有准备的阵地上按照对你有利的规则作战。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这个是永恒的战术。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "有冲突的意见不要去那些看起来品格不好的人的评论区里发评论，而要自己写答案。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你的评论区就是你的预设阵地，没人能在这里对你占优势。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "如果对方和你隔空对骂，你可以屏蔽ta，于是就自然收不到ta的推送了，等于ta静音了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "ta声嘶力竭却心知肚明你根本听不见，这本身就是反击。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "当然，看着三无小号在你的评论区没能得逞，自己写了个洋洋洒洒的“实名反对”却点赞数不超过十个，也算是一种邪恶的福利。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "你让ta发在你的评论区，然后还积极回复他，这是最帮ta忙的行为。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "让ta自己去体会在没有预设立场的前提下，有多少人赞成，让ta自己去品味那份孤独和寂寞。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "你从来没占下风，你当然不会再跑来哭诉求援。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "让那些不懂这些规则的人去哭诉求援去。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "不要去那种不给作者删评论权和拉黑权的平台，因为那里没有这种有利阵地。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "千金之子，坐不垂堂；君子不立危墙之下。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "如果人人都明白了这个规则，网暴者自己才是弱势群体。这样网暴自然就渐渐消失了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P005", "quote": "面对喷子，你的心理感受是怎样的？有哪些妥善的应对方式？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["网络社区行为", "冲突应对", "平台规则"],
   "issue_candidates": ["网络暴力的应对方式", "评论区与阵地选择", "屏蔽与拉黑的功能", "求助者的心理困境（正文未回应）"],
   "text_function_candidates": ["答疑（给战术建议）", "指导", "评论"],
   "object_candidates": ["提问者（被网暴者）", "网暴者/喷子", "知乎", "三无小号", "平台"],
   "working_keywords": ["网暴", "喷子", "合法武力", "预设阵地", "屏蔽", "删评论权", "拉黑权", "三无小号", "实名反对", "邪恶的福利"]
  },
  "notes": "正文无图片节点。P005 在阅读包中标注“⚠lexical未覆盖片段”，含两条其他知乎问题标题（其中一句含粗口）。提问者自述“心里有点想不开”，正文只给平台战术建议，未回应心理危机，已记入 unresolved_questions。brief 为正文语句摘录，仅作导航。"
 },
 "721372df": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待瑞幸公布调查显示伪造交易价值达 22 亿，盘前下跌超 80%？”，即请作者评论瑞幸财务造假事件。作者主张不必大惊小怪、不必担心中概股名声受损，也不要小看美国股民（P001、P002）；称比这更大的“雷”多了去了，瑞幸排 Top20 都排不进（P003）；以安然与雷曼兄弟为例反问“吓住投资人了么”（P004、P005）；并断言资本游戏规则不改则作弊玩家永不止息，最后给出对“金融”本质的尖锐界定（P006、P007）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者主张不必大惊小怪、不必担心“坏了中概股的名声”，也不要太小看美国股民。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "作者称比这更大的“雷”多了去了，瑞幸排 Top20 只怕都排不进。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "以安然（1100亿）与雷曼兄弟（负债六千亿）为例反问：是否吓住了“投资人”？", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "断言资本游戏的规则不改，作弊玩家就永不会止息；并把所谓“金融”的本质界定为无良父母强制透支尚未出世、毫无还手之力的子孙。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为不必大惊小怪，也不用担心“坏了中概股的名声”，并且不要太小看美国股民。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为比这更大的“雷”多了去了，瑞幸排 Top20 只怕都排不进（“只怕”为估计语气）。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以安然（1100亿）与雷曼兄弟（负债六千亿）为例反问：这些更大的事件是否吓住了“投资人”？", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言资本游戏的规则不改，作弊玩家就永不会止息。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把所谓的“金融”界定为：绝大部分内容的本质只不过是无良的父母们在强制透支尚未出世、毫无还手之力的子孙们。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "劝止担忧：不必大惊小怪、不必担心中概股名声、不要小看美国股民（P001、P002）。",
    "规模比较：更大的“雷”很多，瑞幸排不进 Top20（P003）。",
    "举例反问：安然 1100 亿、雷曼负债六千亿，是否吓住“投资人”（P004、P005）。",
    "结论一：资本游戏规则不改，作弊玩家永不止息（P006）。",
    "结论二：对“金融”本质的贬义界定（P007）。"
   ],
   "concept_usage": [
    {"term": "雷", "meaning": "本文中指重大的财务暴雷或丑闻事件。", "evidence": "P003", "ambiguity": "口语用法，未界定规模标准。"},
    {"term": "中概股的名声", "meaning": "提问语境中可能被担心受损的对象；作者认为不必担心。", "evidence": "P001", "ambiguity": "作者未说明该“名声”由谁在意、如何衡量。"},
    {"term": "资本游戏的规则", "meaning": "作者认为需要改变的对象，并称规则不改则作弊玩家永不止息。", "evidence": "P006", "ambiguity": "“规则”具体指什么、应如何改，本文未说明。"},
    {"term": "“投资人”", "meaning": "作者加引号使用，语带讥讽，指在类似事件中并未被吓住的投资者。", "evidence": "P004", "ambiguity": "引号的具体用意（讽刺其判断力还是其身份）本文未说明。"},
    {"term": "金融", "meaning": "作者加引号给出贬义界定：绝大部分内容是无良父母对未出世子孙的强制透支。", "evidence": "P007", "ambiguity": "为高度概括的批评，未给出适用范围与例外。"}
   ],
   "examples_and_targets": [
    "瑞幸伪造交易 22 亿、盘前下跌超 80%：提问者提供的事件（Q001），正文未复核其细节。",
    "安然与 1100 亿：作者举出的对比事件（P004），未注明数字口径。",
    "雷曼兄弟与负债六千亿：作者举出的对比事件（P005），未注明数字口径。",
    "美国股民：作者提醒不要小看的对象（P002）。",
    "“无良的父母们”与“尚未出世的子孙们”：作者用于界定“金融”的比喻（P007）。"
   ],
   "conditions": [
    "P001 用“不用……也不用……”作否定式劝止。",
    "P003 用“只怕都排不进”表示估计而非确定。",
    "P004、P005 以反问句式表达“投资人”未被吓住。",
    "P006 以“规则不改……就永不会止息”为条件句。",
    "P007 用“绝大部分内容的本质只不过”作限定式断言。"
   ],
   "rhetoric_and_tone": "短评体，连续反问（“吓住‘投资人’了吗？”）、口语词（“雷”“大惊小怪”）、给“投资人”“金融”加引号以示讥讽；结尾由事件评论升华为对金融的尖锐道德批评。",
   "unresolved_questions": [
    "瑞幸事件的具体事实（伪造 22 亿、盘前跌 80%）来自提问，正文未复核，需外部核查。",
    "安然 1100 亿、雷曼负债六千亿的数字与口径为作者举例，未注明出处，需外部核查。",
    "“Top20”的排名依据与范围本文未说明。",
    "正文未评价瑞幸公司、管理层或相关责任人的行为，也未讨论中概股监管问题。",
    "“资本游戏的规则”具体所指与改法本文未说明。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不要大惊小怪，也不用担心什么“坏了中概股的名声”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不要太小看美国股民。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "比这更大的雷多了去了，瑞幸排Top20只怕都排不进。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "安然不比瑞幸大个十倍？1100亿，吓住“投资人”了吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "雷曼兄弟轰然倒地，负债六千亿，吓住“投资人”了吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "资本游戏的规则不改，作弊玩家就永不会止息。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "所谓的“金融”，绝大部分内容的本质只不过是无良的父母们在强制透支尚未出世、于是毫无还手之力的子孙们而已。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["金融与资本市场", "公司丑闻", "时事评论"],
   "issue_candidates": ["瑞幸财务造假事件", "中概股名声与投资者信心", "资本市场的规则与作弊"],
   "text_function_candidates": ["答疑", "评论", "批评"],
   "object_candidates": ["瑞幸", "美国股民／投资人", "安然", "雷曼兄弟", "中概股"],
   "working_keywords": ["瑞幸", "造假", "中概股", "雷", "安然", "雷曼兄弟", "资本游戏", "金融", "投资人"]
  },
  "notes": "正文无图片节点。brief 为正文语句摘录，仅作导航。事件事实来自提问，正文未复核，已记入 unresolved_questions。"
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
