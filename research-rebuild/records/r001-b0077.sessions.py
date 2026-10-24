# -*- coding: utf-8 -*-
"""批次 r001-b0077 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0077.sessions.py            # 写 out/r001-b0077.out.jsonl
  python3 records/r001-b0077.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0077"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0077.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f56baf4c": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：如何证明你不是你所讨厌的那种人。提问预设人可能不是自己讨厌的那种人并要求给出证明；作者未接受该预设，开篇直接断定“你当然是你所讨厌的那种人，这个不用问”，转而论证人身上同时具备全部人类特质。（平台 zhihu，发表 2020-10-13）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开篇直接回答：你就是你所讨厌的那种人，不必问。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "以“全元素杂合体”与抓一把土的类比说明人不是高纯物质，人类全部精神要素在任何人身上都存在。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "列举成对的正反特质，断言一切特质你都有。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "不能用哪种特质占“比重”占优来给人定性；理由是没法给特质分比重。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "你既是公平的人也是双标的人，并非“公平时更多所以总体公平”的安排，而是碰巧未遇上触发双标的事，客观结果不改变这一点。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "坦克类比：极少开炮、多数时候只是行驶，不能据此把它定性为陈列装饰或拖拉机。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "引出图片（IMG001，未核验）与分层蛋比喻：每层颜色都有，外表花纹取决于在具体事件中被磨到多深；未打磨的蛋看似纯白只是表象。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018"], "summary": "结论：你是每一种人，所以一定也是你讨厌的那种人；并且也是你所喜欢的那种人。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不接受提问预设，直接断定：你当然是你所讨厌的那种人，此事不需要问。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人不是高纯物质而是“全元素杂合体”，如同抓一把土几乎含元素周期表全部元素、只是比例不同；人类所有精神要素在任何一个人身上都存在。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论你讨厌的是哪一种人类特质，你身上都有；且不能用某特质在“比重”上占优来定性一个人是什么样的人。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无法给这些特质分比重，所以按比重给人定性不成立。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "你既是公平的人也是双标的人；这不是“公平时候更多、所以总体上是一个公平的人”的安排，而是碰巧总遇上不会刺激出双标属性的事情（大部分人如此），客观结果不表示你不是双标的人。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "坦克类比：不能因坦克停着不动的时间占比最大而认定它只是陈列装饰，也不能因它绝大多数时候只是行驶而认为它基本上只是拖拉机。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人如分层彩蛋：每一层颜色你都有，外表呈现什么花纹取决于在具体事件里被磨到多深；磨成不同形状花纹会变，另一个蛋磨成同样形状花纹也不同。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "即便作为一颗新的还没打磨的蛋、表面看似只有最外层雪白纯色，那也只是表象。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你是每一种人，所以你一定也是你讨厌的那种人。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提醒读者：你也是你所喜欢的那种人。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "不接受提问预设，直接给出“你就是你讨厌的那种人，不用问”（P001）。",
    "以“全元素杂合体”和抓土类比建立前提：全部人类精神要素都在一个人身上，只有比例差异（P002-P003）。",
    "列举成对特质并断言一切特质你都有（P004-P005）。",
    "否定按特质“比重”定性，理由是比重无法分配（P006-P007）。",
    "澄清“公平/双标”不是时段分配问题，而是刺激条件未出现（P008-P009）。",
    "以坦克类比支撑“占比大不等于本质”（P010）。",
    "引出图片与分层蛋比喻：花纹由被磨深度决定，表面纯白只是表象（P011-P016）。",
    "结论：你是每一种人，故必是你讨厌的、也是你喜欢的那种人（P017-P018）。"
   ],
   "concept_usage": [
    {"term": "全元素杂合体", "meaning": "借抓一把土说明人同时含有全部人类精神要素、只有比例差异，不是高纯物质。", "evidence": "P002", "ambiguity": "“比例”如何度量未说明，且与后文否认可分比重存在表述张力。"},
    {"term": "比重", "meaning": "指各特质在一个人身上所占份额，作者否认可据此给人定性。", "evidence": "P006", "ambiguity": "带引号使用，未给出可操作定义。"},
    {"term": "双标", "meaning": "与“公平”并列存在的一种特质，是否显现取决于有没有遇到刺激它的事情。", "evidence": "P008", "ambiguity": "未界定双标的判定标准。"},
    {"term": "花纹/层", "meaning": "蛋的层次与花纹比喻人被具体事件“打磨”后外在呈现的样子，而每一层颜色本来都有。", "evidence": "P012", "ambiguity": "该比喻紧接未核验图片之后，图与“层”的对应关系不明。"}
   ],
   "examples_and_targets": [
    "抓一把土、元素周期表几乎就全了：作者类比，用于说明人含全部精神要素（P002）。",
    "坦克极少开炮、多数时候只是行驶：作者类比，用于否定按占比定性（P010）。",
    "分层蛋、花纹、未打磨的蛋表面纯白：作者比喻；P011“人类其实是这样的（侵删）”后接IMG001，图片未核验。",
    "括号注“（侵删）”说明该图为转载素材，来源与权利人未说明（P011）。",
    "提问字段的“如何证明你不是你所讨厌的那种人”是被回应的提问，非作者主张（Q001）。"
   ],
   "conditions": [
    "“大部分人都是这样”（P009括号内）——把“未被刺激出双标”限定为多数人的常见情形。",
    "“取决于在具体的事件里面你被磨到多深”（P012）——外观呈现取决于具体事件这一条件。",
    "“哪怕你作为一颗新的还没打磨的蛋”（P016）——以假设情形说明表象。"
   ],
   "rhetoric_and_tone": "开篇以“这个不用问”否定提问前提，语气斩截；通篇以比喻链推进（元素杂合体—坦克—分层蛋），带调侃意味；括号夹注“（侵删）”属平台转载习惯；结尾“别忘了”转为提醒式柔和收束。",
   "unresolved_questions": [
    "IMG001 未核验：P011“人类其实是这样的（侵删）：”直接引出该图，P012“每一层颜色你都有”承接图意，图片内容不明使该比喻的指涉无法确认，需图像核验。",
    "“全元素杂合体”中的“比例差异”与后文“没法给这些特质去分比重”之间的表述张力，正文未调和。",
    "“双标”“公平”的判定标准以及“刺激出双标属性的事情”的范围，正文未说明。",
    "记录含 updated_at（2021-05-16）晚于 published_at（2020-10-13），正文是否经修改无法从本记录判断。",
    "brief 与正文首段重合且被截断（“仁爱也有”后中断），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你当然是你所讨厌的那种人，这个不用问。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "人不是什么高纯物质，而是一种“全元素杂合体”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "人类所有的精神要素在任何一个人身上都是存在的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "正直也有、卑鄙也有；公平也有、偏袒也有；诚实也有、伪诈也有；仁爱也有，贪婪也有", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "无论你讨厌的是人类的哪一种特质，你身上都有。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "是不能用“比重”上哪个特质占优来定性“是什么样的人”的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "因为你没法给这些特质去分比重。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "所以呈现出这么一个客观的结果。但这根本不表示你就不是一个双标的人了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你并不能因为它停着不动的时间占比最大而认定它只是一种陈列装饰", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "每一层颜色你都有，最后你的外表呈现为什么样的花纹被他人和自己明确的看到，取决于在具体的事件里面你被磨到多深。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "看起来似乎只有最外一层的雪白的纯色，那只是表象。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "你是每一种人，所以你一定也是你讨厌的那种人。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "别忘了，你也是你所喜欢的那种人。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人性论/道德心理", "自我认识"],
   "issue_candidates": ["人是否可能不是自己所讨厌的那种人", "特质与人格定性", "公平与双标并存"],
   "text_function_candidates": ["答疑", "比喻说理"],
   "object_candidates": ["提问者（未具名）", "泛指的“你”"],
   "working_keywords": ["全元素杂合体", "比重", "双标", "花纹", "打磨", "侵删"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含1个图片节点（IMG001），图片内容未经核验，需图像核验；正文文本已通读（P001-P018），故按简报要求标 status=needs_reread、image_checked=false、full_text_checked=false。P011“（侵删）”后的图片与P012-P016的“层/花纹”比喻直接相关。"
 },
 "2867ed0d": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：为何古代战争都强调长江天险？长江那么长，别的地方不能渡河吗？提问预设“长江长、总可以另选渡口”，暗含对天险意义的疑问。作者的回答把问题从“能否找到渡口”转为“能否在渡江会战中消灭守军主力”，并提出“会战之地”概念。（平台 zhihu，发表 2020-10-21）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出核心判断：难处不是找不到别处渡河，而是无法让足够规模部队不被察觉地过江、无法在对方反应前建立稳固滩头阵地。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "理由：勉强渡江即背水一战，敌方陆地补给而我方跨江补给，补充不及会被消灭；即使过去十几万人，只要敌主力未被消灭，长江造成的补给困难仍会把人消耗干净。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "由此推出：渡江不光要过江，还要在渡江战役中扎实消灭守军有效兵力，做不到就是找死。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "限定：随便找处过河并不难，时间够久即可，攻方可借陆地火力建坚固水寨；先造大量船只提高成功率有用但非决定性。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "渡江没有花巧可玩，必须堂堂正正打赢会战、当天正面击穿击溃对方之阵；如此过江后敌方元气大伤，才可能从容攻略、占自给自足的地盘做前进基地。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "反面情形：勉强过去容易，但在陌生领土上与士气未挫、因长江天险而有必胜信心的敌军纠缠久了会日久生变。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "攻方真正寻找的不是方便渡江的滩头而是“会战之地”；古代战争最怕战事绵延、速战速决的办法是诱使对方集中全部力量总会战，即“攻你所最必守、也最愿守”之处；守方必须觉得“没准我能行”才愿在此拼命。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P019"], "summary": "推论：参谋按两个“最”筛选，总会得出同样的几个地方，多半是历代先辈用过之处。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "以图片（IMG001-IMG002，未核验）引出“会战之地”的地形特征：对攻方是突出部、约等于三面围攻；对守方背后一马平川、失败损失大；又有双城夹江补给优势和消耗攻方的诱惑，故成双方默契共识，都自信能把它变成绞肉机。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P029", "P030"], "summary": "结论：难得的不是过江之处，而是可以毕其功于一役之处；所以渡江之战常常是灭国之战。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "长江的主要问题不是找不到别的地方渡河，而是不可能让有足够规模的部队越过长江而不被对方察觉，也不可能在对方有所反应之前建立足够稳固的滩头阵地。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "勉强渡江的部队立足未稳就要背水一战，且敌方陆地补给、渡河部队跨江补给，物资人员补充不及只会被消灭。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "即便让十几万人、整个兵团过江，只要对手主力没有被有效消灭，长江造成的补给困难一样会导致这十几万人最终被消耗干净。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "渡江问题不光是要过江，还要在渡江战役里扎实消灭守军的有效兵力；做不到这一点，勉强渡过去就是找死。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "随便找一处过河不难，只要时间够久也谈不上多少船只问题，因为攻方可以在陆地火力掩护下构建坚固水寨。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在长江上寻找支流先造好大量船只以提高渡河成功率是有用的，但并不是决定性的。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "渡江真正的问题在于没有花巧可玩，必须堂堂正正同时打赢渡江这场会战；渡江当天必须正面击穿击溃对方的堂堂之阵。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有击溃守军主力，过江后对方才长期无法形成有效威胁，才可能从容攻略、占住足够自给自足的地盘做前进基地。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "否则勉强过去容易，但在陌生领土上与士气未受严重挫折、甚至因长江天险而有必胜信心的敌军纠缠久了会日久生变。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "渡江之战中攻击方真正采取的策略不是寻找方便渡江的滩头，而是寻找最有利于一次击溃所有守军的“会战之地”。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代战争最大的奥妙是找到“会战之地”，因为最可怕的不是作战而是战事绵延、出现不可控变数。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "速战速决的最好办法是找一个对方觉得优势也足够大、战略意义又足够重要的地方，引诱或迫使对方集中全部力量做一次总会战，即攻其最必守也最愿守之处。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须让对方“最愿守”：若明知守不住，对方宁可让掉该地、等我立足未稳时另选威胁更大的攻击点；所以仅让我方感到有威胁不够，还要让对方有“没准我能行”的感受才会真正集中兵力拼命。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "渡江战役时参谋把可过江地点按两个“最”筛选，总是会得出同样的几个地方，而那几个地方多半是历代先辈过江时已用过的。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类地方的特征：对攻方是突出部、约等于三面围攻，可派小部队强渡形成暂时四面围攻；对守方背后一马平川、失败损失很大；另一方面又有双城夹江的补给优势与依赖地利消耗攻方有生力量的诱惑（自己没把握野战取胜时诱惑更大）。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这里旷日持久的战斗可算攻守双方在自然规则媒合下的默契共识，双方都自信能把这里变成最有效消耗对手的绞肉机。", "evidence": ["E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是过江的地方难得，而是可以毕其功于一役的地方难得；也正因如此，渡江之战常常是灭国之战。", "evidence": ["E24", "E25"]}
   ],
   "argument_steps": [
    "先把提问的焦点从“找渡口”移开，指出真正的障碍是兵力规模、隐蔽性与滩头阵地的建立（P001）。",
    "以补给不对称（敌陆地补给/我跨江补给）论证勉强渡江必被消耗，并推到十几万人亦然（P002-P003）。",
    "给出结论：渡江战役本身必须消灭守军有效兵力（P004-P005）。",
    "让步与限定：过河并不难、船只不是决定性因素（P006-P007）。",
    "正面提出标准：必须堂堂正正打赢会战，之后才谈得上攻略与前进基地（P008-P009）。",
    "反面设想：若不如此，与士气未挫之敌纠缠会日久生变（P010）。",
    "把问题抽象为“寻找会战之地”，给出两个“最”的条件及其心理机制（P011-P018）。",
    "推论出历代渡江地点重复出现（P019）。",
    "以图片所示地形归纳“会战之地”的攻守特征，说明双方为何在此默契决战（P020-P028）。",
    "收束：难得的是毕其功于一役之地，故渡江常为灭国之战（P029-P030）。"
   ],
   "concept_usage": [
    {"term": "长江天险", "meaning": "提问中的说法，作者将其实际作用落在渡江部队的补给困难与敌军士气信心上，而非江面本身难渡。", "evidence": "P001", "ambiguity": "作者未给“天险”下定义，且明确说长江并不那么湍急宽阔（P011）。"},
    {"term": "会战之地", "meaning": "最有利于一次击溃所有守军的地点，需同时满足“攻方最必守、守方最愿守”两个带“最”的条件。", "evidence": "P012", "ambiguity": "两个“最”如何判断与量化，正文未说明。"},
    {"term": "绞肉机", "meaning": "双方都自信能在此最有效消耗对手的地点，旷日持久战斗的结果。", "evidence": "P026", "ambiguity": "带比喻色彩，非军事术语定义。"},
    {"term": "毕其功于一役", "meaning": "在一次会战中解决渡江与灭敌两件事，作者用它概括“会战之地”的价值。", "evidence": "P029", "ambiguity": "无。"},
    {"term": "滩头阵地", "meaning": "渡江后在对方反应前建立稳固的登陆立足点。", "evidence": "P001", "ambiguity": "未给出“足够稳固”的标准。"}
   ],
   "examples_and_targets": [
    "长江中下游尽是平原、两岸远谈不上陡峭：作者作为反驳“找方便滩头”说法的地理依据（P011）。",
    "攻方在陆地火力掩护下构建坚固水寨、对方集中水军来攻的假想对决：作者设想的对抗情景与反问（P006）。",
    "“妈的，没准我能行”：作者设想的守方心理台词（引号内为设想的口语），非引用他人文献（P018）。",
    "IMG001、IMG002（未核验）：位于P021“譬如这个：”之后，用作“会战之地”的图例，图片内容不明。",
    "“历代先辈过江时已经用过的”地点：作者的历史性概括，未给出任何具体战役或地名（P019）。",
    "提问者的“为何古代战争都强调长江天险”是被回应的提问，不是作者主张（Q001）。"
   ],
   "conditions": [
    "“只要时间够久”（P006）——过河不难这一判断的时间条件。",
    "“只要对手的主力部队没有被有效消灭”（P003）——补给困难足以消耗大军的条件。",
    "“如果做不到这一条，勉强渡过去就是找死”（P005）——明示的必要条件。",
    "“这里有两个条件，而且都带着‘最’字”（P017）——会战之地的双重限定。",
    "“尤其是自己没把握在野战和陆战中取胜，这诱惑就更大”（P024）——守方选择在此消耗的附加条件。",
    "“在对方的血流到足够干之前”（P027）——攻方不愿偷渡小部队的时间条件。"
   ],
   "rhetoric_and_tone": "以军事推演口吻逐层推进，大量“所以/因为”连接；设问自答（“这会是一种什么样的地方呢？”“为什么一定要你也最愿守？”）；对假想对手用第二人称直接叫阵（“你可以试试集中水军来攻击我的坚固工事”）；引号内插入粗口语“妈的，没准我能行”形成落差；以“绞肉机”“岂不快哉”等词带出战事残酷与从容盘算的对照；结尾用“毕其功于一役”“灭国之战”收束。",
   "unresolved_questions": [
    "IMG001、IMG002 未核验：两图位于P021“譬如这个：”之后、P022之前，应是“会战之地”的图例，图中所绘地点或战例不明，P022-P024 的地形描述很可能依附于该图，需图像核验。",
    "“历代先辈过江时已经用过的”未给出任何具体战例、地名或年代，属概括性历史叙述，需外部核查。",
    "“双城夹江”具体指何种城邑格局，正文未说明，仅能从图片（未核验）推测。",
    "两个“最”的判定标准，以及“优势足够大”的程度，正文未给出可操作判据。",
    "记录含 updated_at（2022-03-26）晚于 published_at（2020-10-21），正文是否经修改无法从本记录判断。",
    "brief 与正文首段重合且被截断（“物资人员”后中断），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "长江的主要问题，不是找不到别的地方渡河，而是你不可能让有足够规模的部队越过长江而不被对方察觉", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "问题是交战的敌人是陆地补给，而渡河部队却要跨江补给。物资人员补充不及，只会被眼睁睁的消灭。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "只要对手的主力部队没有被有效消灭，背后的长江所造成的补给困难就一样会导致这十几万人最终被消耗干净。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "渡江的问题不光是要过掉这条江，而且是要在渡江这一战役里扎扎实实的消灭掉守军的有效兵力。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "如果做不到这一条，勉强渡过去就是找死。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "随便找一处过河是不难的，只要时间够久，这也谈不上多少船只问题。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "在长江上寻找一支流先造好大量船只来提高渡河的成功率是有用的，但却并不是决定性的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "渡江真正的问题在于它没有花巧可玩。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "也就是渡江当天，必须是正面击穿击溃对方的堂堂之阵。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "对方已经元气大伤，在很长一段时间内都无法再对过江部队形成有效威胁", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "但在陌生的地方领土上和士气并没有严重挫折，甚至因着长江天险而有着必胜的信心的敌军纠缠久了一样日久生变。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "攻击方真正会采取的策略不是在寻找“方便渡江的滩头”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "他们在寻找的是最有利于自己一次击溃所有守军的“会战之地”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "古代战争最大的奥妙，就是找到这块“会战之地”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "因为古代战争最可怕的不是作战，而是战事绵延，出现不可控的变数。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "就是找一个对方觉得优势也足够大，而战略意义又足够重要的地方，引诱或者迫使对方把全部的力量都集中到这里来做一次总会战。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "也就是攻你所最必守，而且也最愿守的地方。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "必须让你有足够的“妈的，没准我能行”的感受，你才会有这个意愿在这里真正的集中兵力跟我拼命。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "参谋们把可以过江的所有地点列出来拿着这两个“最”一撸，总是会撸出同样的几个地方来", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "对于攻方，你这是一个突出部，我约等于三面围攻", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "对于守方，背后是一马平川，失败的损失很大。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "存在依赖地利最有效的消耗攻方有生力量的诱惑", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "在这里旷日持久的战斗，可以算是一种攻守双方在自然规则媒合下的默契共识。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P029", "quote": "不是过江的地方难得，而是可以毕其功于一役的地方难得。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P030", "quote": "也正因为如此，常常渡江之战就是灭国之战。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["古代军事史", "军事地理", "战略战术理论"],
   "issue_candidates": ["渡江为何集中于特定地点", "渡江战役的补给与滩头问题", "会战/速战速决逻辑"],
   "text_function_candidates": ["答疑", "军事推演式说理"],
   "object_candidates": ["长江", "攻方与守方（泛称）", "历代渡江战役（未点名）"],
   "working_keywords": ["长江天险", "滩头阵地", "背水一战", "会战之地", "绞肉机", "毕其功于一役", "双城夹江"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含2个图片节点（IMG001、IMG002），均位于P021“譬如这个：”与P022之间，图片内容未经核验，需图像核验；正文文本已通读（P001-P030），故按简报要求标 status=needs_reread、image_checked=false、full_text_checked=false。P022-P024对“会战之地”地形特征的描述很可能依附于这两张图。"
 },
 "0cc1ee55": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：一个人的教养如何体现？提问只问“如何体现”，未给教养下定义。作者先给出自己关于教养的定义与机制（言谈举止→观感→关系建立），再以“小电视台”比喻展开管理问题，中段谈家教背景与礼仪信号的实际作用，末段转折到作者认为更关键的方面：如何对待未知。（平台 zhihu，发表 2020-10-21）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "定义教养为言谈举止中体现的特性，其受关注是因为直接关系到他人观感；教养好即过建立积极关系第一关，不好则遇第一个门槛。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "“小电视台”比喻：人人不断向可见者广播言谈举止，互联网使广播可瞬时传遍全球甚至跨越时间；危机是不知如何管理电视台，任由杏仁核当台长、额叶当摄像师音响师。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "“有教养”第一条是意识到电视台及其要害性、让额叶当台长；此后才有好/坏教养之分，当台长后用什么指导思想编排节目是教养问题的本质。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "观众解读逻辑之一：风俗礼节是潜在知识，家教渊源深者受教更多，言行“若合符节”“世家风范”暗示背景深厚；此类信号年轻人不易看懂，老江湖敏感，经验不足的小孩因此成为“可用资源”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "应对得体、揖让有规矩本身可以“辟邪”；浑身尖刺、阴阳怪气地放“不好惹”信号没用，且是没底气的证明（三墙齐倒，五鬼临门）。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "限定与批评：人人都有不能保持教养的点，点越低越易成猎物；作者为为小事放下教养者感到揪心，强调“要不要丢掉教养”是另一个更严重、更致命的问题，写下的话会留存并被“鲨鱼”物色。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P036", "P037", "P038"], "summary": "世家正因意识到这种知识的要害性才重视揖让进退，从而享受“被动辟邪”的福利；系统教育性价比胜过请保镖、买保险，是世家长期繁荣的支柱。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "转折：没有家学渊源并非没救；不懂中国礼仪的外国人不能说没有教养，因为人们以其“没学会礼节”为新的基线衡量，基线之上往上偏还是往下偏才给人定调。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060"], "summary": "三项检验（不懂时是否假定礼貌、无能力判定时是否当成撒谎、没把握时是否当作“没什么大不了”）推出：教养不在于什么都知道，而在于如何对待未知，即把好的那一头留给别人。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P061", "P062", "P063", "P064", "P065", "P066", "P067"], "summary": "结论：尽可能把好的一头留给别人、赠予benefit of the doubt者必多朋友与贵人；这种可能性就是“深厚背景”，胜过只有世家渊源而无真正教养者——后者是死水无源，前者才是真正的活教养。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教养是人的言谈举止里体现出来的一种特性，它广受关注是因为直接关系到他人对人的直接观感；教养好就过了建立积极关系的第一关，不好就先遇到第一个门槛。", "evidence": ["E01", "E02", "E03"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每个人都是一个小电视台，不断对一切能看到自己的人广播自己的言谈举止；这种广播在互联网时代可以沿着网线、靠搜索引擎和推荐算法瞬间传遍全球。", "evidence": ["E04", "E05"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们面临“不知道如何管理自己这个小电视台”的危机，常让智商还没超过恐龙的杏仁核担任台长，而让满腹学识的额叶只当摄像师和音响师。", "evidence": ["E06", "E07"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“有教养”的第一条，是意识到这个电视台的存在与要害性，让额叶而不是杏仁核来当“台长”。", "evidence": ["E08"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做到第一条之后才有“好教养”“坏教养”之分（不管正负分，好歹有分而不是null）；以什么指导思想编排自己的“节目”，就是教养问题的本质。", "evidence": ["E09", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人际交往中有风俗礼节这类潜在知识，父母辈见多识广、家族传承有渊源的人受此类教育更多，其称呼、语气、动作附和规范即“若合符节”“世家风范”，暗示人脉背景深，令人不敢轻视。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "经验不足的小孩子天然是老江湖、老油条们的“可用资源”；若让人感觉“这孩子背后恐怕有某种根深叶茂的不明背景”，老狐狸们会三思而后行，因此应对得体、揖让进退有规矩本身就可以辟邪。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反而浑身尖刺、见谁怼谁、阴阳怪气、含沙射影地放“不好惹”信号是没用的，且是一种特别没有底气的证明。", "evidence": ["E16", "E17"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "人不是上帝、没有无限忍耐力，最终每个人都有不能保持教养的点；但这个点越低，人就越容易成为猎物，这个问题无比冰冷而现实。", "evidence": ["E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对为微不足道的理由放下教养这个“最大的护身符”、大搞含沙射影阴阳怪气的人感到揪心，认为这样做是不知死活；无论争执的具体事情多重要，“要不要丢掉教养”都是另一个单独的、更严重、更致命的问题。", "evidence": ["E19", "E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "写下的话会一直留在那里供一切路过的人观看，其中有鲨鱼专门物色下一个对象；为争一根棒棒糖而对黑暗森林里的猎人们广播自己的位置并不值得。", "evidence": ["E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世家正因意识到这种知识的要害性才重视揖让进退的礼仪，从而享受“被动辟邪”的福利；这种系统教育的性价比远胜过请保镖、买保险，是世家长期繁荣稳定的一大支柱。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尽管上面这些的确是真的、对人的命运非常重要，但它并不是教养最关键的方面；没有家学渊源的人只是获得了一根新的基线，之后从这根基线往上偏还是往下偏才是真正给人定调的东西。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C014", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "作者以设问形式提出并否定的一种立场（未指名持论者）：不懂中国的揖让进退、不会正确区分席次与身份就等于没有教养；作者举不懂中国礼仪的外国人为例，判定“并不能”，理由是人们会用“没学会礼节的人”的新基线来衡量。", "evidence": ["E28", "E29"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的教养不是“什么都知道”，而是如何对待未知：在两种可能性里把好的那一头留给别人、把坏的那一头留给自己；在可以爱也可以恨时选择爱而不是放纵恨。", "evidence": ["E30", "E31", "E32", "E33"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把好的那一头尽可能留给别人、对ta人尽可能赠予benefit of the doubt的人必多朋友，不会少了人喜欢、看好与贵人相助；这种可能性就是你的“深厚背景”，胜过只有“世家渊源”却没有真正教养的人。", "evidence": ["E34", "E35"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "空有家传礼仪知识而在根本关头上没有教养，就像有一潭死水却没有水源，人脉将来也会磨损耗尽；没有家传积累而在根本关头上站得住，人脉与社会网络会像泉水一样滚滚而来——后面这个才是真正的活教养。", "evidence": ["E36", "E37", "E38"]}
   ],
   "argument_steps": [
    "先给教养下操作性定义并说明其后果（积极关系的第一关/第一个门槛）（P001-P003）。",
    "用“小电视台”比喻把事情放大到信息传播与自我管理问题，指出杏仁核当台长、额叶当技术工的错位（P004-P008）。",
    "提出“有教养”的第一条标准：意识到电视台并让额叶当台长；再声明这才进入好坏教养之分（P009-P012）。",
    "转入“观众的解读逻辑”：家教渊源→礼仪信号→背景暗示→老江湖的读取（P013-P019）。",
    "由信号推出正面做法（应对得体可辟邪）与反面做法（尖刺放话没用且暴露没底气）（P020-P026）。",
    "加限定：人人都有失守的点，点越低越危险；并对放下教养者作批评（P027-P031）。",
    "强调丢掉教养是独立且更致命的问题，写下的话会留存（P032-P035）。",
    "以世家为例说明这种知识的收益与性价比（P036-P038）。",
    "转折设问：没有家教传承是否没救，用不懂礼仪的外国人为例提出“新基线”（P039-P048）。",
    "以三组设问检验把结论落到“如何对待未知、把好的那一头留给别人”（P049-P060）。",
    "收尾：赠予benefit of the doubt者必多朋友，死水与水源之喻，落在“真正的活教养”（P061-P067）。"
   ],
   "concept_usage": [
    {"term": "教养", "meaning": "言谈举止中体现、直接作用于他人观感的特性；本文最终定义为如何对待未知、在两种可能性中把好的那一头留给别人。", "evidence": "P001", "ambiguity": "文中先在“礼仪/家教信号”意义上使用，后又声明那不是最关键的方面，前后用法存在层次差别。"},
    {"term": "小电视台", "meaning": "比喻每个人持续向外广播自己的言谈举止，且其内容可被检索、存储与跨时间观看。", "evidence": "P004", "ambiguity": "“管理电视台”的具体标准未给出。"},
    {"term": "杏仁核/额叶", "meaning": "以杏仁核代指未经反思的情绪冲动、额叶代指理性审思，用“谁当台长”比喻自我管理的主导权。", "evidence": "P006", "ambiguity": "通俗化神经科学用法，未给文献依据，属比喻性表述。"},
    {"term": "辟邪", "meaning": "得体的言谈举止使潜在的加害者心生疑虑而转移目标，形同护身符。", "evidence": "P020", "ambiguity": "引号内的比喻用法，非字面意义。"},
    {"term": "新基线", "meaning": "没有受过家训礼仪教育者的起始水平，人们以此为基准衡量其言行；基线之上的偏向才给人定调。", "evidence": "P046", "ambiguity": "基线如何被他人识别与判定，正文未说明。"},
    {"term": "benefit of the doubt", "meaning": "在不确定时把好的那一头留给对方，即对他人尽可能作善意假定。", "evidence": "P061", "ambiguity": "直接夹用英文短语，未给中文定译。"},
    {"term": "黑暗森林", "meaning": "借用来比喻公开言论场中存在专门物色猎物的加害者。", "evidence": "P034", "ambiguity": "出自刘慈欣《三体》的术语，正文未标明出处。"}
   ],
   "examples_and_targets": [
    "小电视台、台长、摄像师音响师、恐龙：作者贯穿全篇的比喻装置（P004-P010）。",
    "“若合符节”“世家风范”“文质彬彬”“如沐春风”：作者引用的成语式雅语，用于描述礼仪信号（P016、P020）。",
    "老江湖、老油条、老鲨鱼、老狐狸、鲨鱼、猎人：作者对加害型社交者的比喻性称呼（P018、P019、P022、P033、P034）。",
    "不懂中国基本礼仪、不会汉语的外国人：作者举的假设性例子，用于说明“不懂礼节不等于没有教养”（P043）。",
    "“黑暗森林”、棒棒糖、死水与水源、泉水：作者用作修辞材料（P034、P064、P065）。",
    "被批评对象：为了微不足道的理由放下教养、大搞含沙射影与阴阳怪气的人（作者称“我看到这里有些人”），以及认为尖刺式放话有威慑力者（P021、P030）。",
    "提问字段的“一个人的教养如何体现”是被回应的提问，非作者主张（Q001）。"
   ],
   "conditions": [
    "“这种广播的范围在信息时代之前仅限于…；而在互联网时代，则可以沿着网线…”（P004）——以时代为条件的传播范围变化。",
    "“越是父母辈见多识广、家族传承有渊源的人，受到的这类教育就越多”（P016）——程度条件。",
    "“小孩子再优秀，毕竟仍然幼稚、天真而且经验不足”（P018）——把“可用资源”限定于经验不足者。",
    "“只要让ta们有一点疑虑，瞄准线都自然先移到别人身上去了”（P019）——辟邪生效的条件。",
    "“当然，人不是上帝，没有无限的忍耐力，最终每个人都有不能保持教养的点”（P027）——普遍限定。",
    "“尽管上面这些的确是真的，也的确对人的命运非常重要，但它却并不是教养最关键的方面”（P042）——让步式限定，改变全篇重心。",
    "“在你不懂的前提下”（P049-P050）、“你自己没有能力判定对方是不是撒谎”（P051）、“你并没有把握”（P053）——三项检验各自的前提。",
    "“你可以爱，也可以恨的时候”（P059）——选择爱恨的条件。",
    "“就算有人脉，将来也会磨损耗尽”（P064）——让步条件下的后果。"
   ],
   "rhetoric_and_tone": "全篇以比喻系统推进（小电视台/台长/恐龙、辟邪与护身符、鲨鱼与猎人、黑暗森林、棒棒糖、死水与水源、泉水）；反复用设问自答（“什么叫有教养？”“看懂这个规律没有？”“什么叫教养？”“值得吗？”）带动读者；第二人称“你”为主，间用“你们要记住”的训诫口吻；夹杂英文短语benefit of the doubt与编程词null；用“三墙齐倒，当然五鬼临门”“不可以道里计”等雅俗混用语；P030“我看到这里有些人”把批评落到平台现场语境；结尾以“自己多想想吧”收束，带训诫意味。",
   "unresolved_questions": [
    "“杏仁核”“额叶”的通俗神经科学用法未给出依据，“智商还没超过恐龙”亦为修辞，均需外部核查，本文不作裁决。",
    "“黑暗森林”（P034）未标明出处（与刘慈欣《三体》中同名概念的关系未说明）。",
    "P030“我看到这里有些人”中的“这里”指平台评论区，正文未交代具体场景与对象。",
    "“世家”未限定具体历史时期、地域或家族，属概括性叙述（P036-P038）。",
    "三项检验（P049-P054）以设问—判定形式给出，但“没有教养”的判定是否唯一、是否存在例外，正文未讨论。",
    "记录含 updated_at（2025-10-15）远晚于 published_at（2020-10-21），正文是否经修改无法从本记录判断。",
    "brief 与正文首段重合且被截断（结尾停在“这”），仅作导航。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "教养是人的言谈举止里体现出来的一种特性", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P001", "quote": "它直接与ta人对人的直接观感相连", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P002", "quote": "觉得教养好，就过了建立积极关系的第一关。", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P004", "quote": "每个人都是一个小电视台，在不断的对一切能看到自己的人广播自己的言谈举止。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P004", "quote": "则可以沿着网线、靠着搜索引擎和推荐算法瞬间传遍全球", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P005", "quote": "不知道如何管理自己这个小电视台", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P006", "quote": "任由智商还没超过恐龙的杏仁核来担任电视台的台长", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P009", "quote": "让额叶而不是杏仁核来当“台长”", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P011", "quote": "从这里往前，才有分所谓“好教养”和“坏教养”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "你要以什么样的指导思想去编排你的“节目”，这就是“教养”问题的本质。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "越是父母辈见多识广、家族传承有渊源的人，受到的这类教育就越多。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "也就是所谓的“若合符节”“世家风范”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "天然的就是老江湖、老油条们的“可用资源”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "通过言谈举止让人感觉“这孩子背后恐怕有某种根深叶茂的不明背景”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "这本身就可以辟邪。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "反而浑身尖刺、见谁怼谁、阴阳怪气、含沙射影，时时处处向外放信号让别人知道你“不好惹”反而是没用的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "不但没用，这还是一种特别没有底气的证明。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "这个点越低，人就越容易成为猎物。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P030", "quote": "为了微不足道的理由就放下教养这个最大的护身符", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "“要不要丢掉教养”都是另一个单独的、更严重、更致命的问题。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "你写下的话可是一直会留在那里，供一切路过的人观看的", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P034", "quote": "值不值得对黑暗森林里的猎人们广播你的位置？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "这种系统教育的性价比之高，远远胜过请保镖、买保险。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "这本身就是世家得以长期繁荣稳定的一大支柱。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P042", "quote": "但它却并不是教养最关键的方面。", "relation": "qualifies"},
    {"key": "E26", "paragraph_id": "P046", "quote": "因为人们会用“没学会礼节的人”的新基线为基准来衡量ta的言谈举止。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P048", "quote": "接下去你从这根新基线是往上偏还是往下偏，才是真正给你定调的东西。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P043", "quote": "不懂中国的揖让进退，就断言ta没有教养吗？", "relation": "contradicts"},
    {"key": "E29", "paragraph_id": "P044", "quote": "并不能。", "relation": "contradicts"},
    {"key": "E30", "paragraph_id": "P050", "quote": "在自己不懂的前提下假定自己所做的肯定没有什么不礼貌，这就是没有教养。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P057", "quote": "真正的问题是你如何对待未知。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P058", "quote": "但你在两种可能性里把哪一头留给了别人，把哪一头分给了自己？", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P059", "quote": "你是选择了爱，还是放纵了恨？", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P061", "quote": "对ta人尽可能赠予benefit of the doubt", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P063", "quote": "这种可能性就是你的“深厚背景”", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P064", "quote": "就好像你有一潭死水，却没有水源。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P065", "quote": "好的人脉关系、社会网络自然会像泉水一样滚滚而来。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P066", "quote": "后面这个，才是真正的活教养。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社交行为与礼仪", "人格修养/伦理劝诫", "信息时代的自我呈现"],
   "issue_candidates": ["教养如何体现", "礼仪信号的社交功能", "家教背景与个人品质的关系", "如何对待未知"],
   "text_function_candidates": ["答疑", "训诫式说理", "经验总结"],
   "object_candidates": ["提问者（未具名）", "世家", "老江湖/老油条（泛称群体）", "不懂中国礼仪的外国人（假设）"],
   "working_keywords": ["教养", "小电视台", "杏仁核", "额叶", "世家风范", "辟邪", "新基线", "benefit of the doubt", "黑暗森林"]
  },
  "notes": "本篇无图片节点（lexical 仅 paragraph 67），正文 P001-P067 全部通读，status=read、full_text_checked=true。P006/P009 的“杏仁核/额叶”、P034 的“黑暗森林”等用语出处未标注，已记入未决问题；updated_at 远晚于 published_at，是否改稿无法判断。"
 },
 "a58a755a": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：被恶意诋毁是种怎样的体验？提问要的是体验描述。作者先承认“不舒服”，随即把话题转为应对方式与代价—收益：不追究诋毁者是为了身边的人，最好的反击是生活本身自然呈现的事实。（平台 zhihu，发表 2020-10-22）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "承认被诋毁不舒服，同时视为考验自己的机会；原谅、不计较是重要品质；不追究是为了身边的人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "反面论证：睚眦必报会让身边人怵然而惧，因为身边人相处更久、受你伤害的能力也更大；这造成两层寒心。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "克制暴力的收益：在诋毁者那里吃了亏，却在爱你的人那里收获千百倍；诋毁者如同过客坏天气，身边人才是世界的基石，处理得好诋毁会转化为更强的爱与信任。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "最好的反击不是赌气报复，而是你本来就不是对方描述的那种人，生活自然出现对方难以自圆其说的事实（小气/慷慨、不懂科学/上好论文）。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020", "P021"], "summary": "诋毁者的长期处境：言论一天比一天尴尬，几年后自己无地自容；若曾当众发表，会成为亲友认定其缺少判断力的依据，潜在损失难以想象。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024"], "summary": "收尾：删评论不是最好做法，真正明白的人会回来道歉、承认错误才能解脱；删痕拉黑其实是在保护对方，ta们不懂罢了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被恶意诋毁当然是不舒服的，但这也是考验自己的一个好机会。", "evidence": ["E01"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“人不知而不愠”、可以原谅、可以不计较，是非常重要的品质。", "evidence": ["E02"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不追究这些人，不是为了这些人，而是为了你身边的人。", "evidence": ["E03"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "人如果受不得委屈、吃不得亏，必要以眼还眼、以牙还牙甚至“君子报仇十年不晚”“十倍奉还”，最大的问题是会让身边人怵然而惧。", "evidence": ["E04"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "身边人朝夕相处，让你受委屈的机会远超偶然遇到的无礼路人，而你对他们的伤害能力也远超对素不相识的路人。", "evidence": ["E05"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对路人睚眦必报、出手狠辣、不死不休意味着两件事：没有意识到身边人作为永恒旁观者的存在（一层寒心）；身边人会害怕你（第二层寒心）。", "evidence": ["E06"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被素不相识的人诋毁却没使用暴力手段去“处理”对方，虽然吃了点亏，但在爱你的人这里收获了千百倍。", "evidence": ["E07"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "诋毁者怎么想其实没有关系，ta们不过是过客、如同坏天气；关键是你身边的人、爱你的人怎么想，ta们才是你世界的基石。", "evidence": ["E08", "E09"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果你处理得好，人对你的诋毁反而会转化为身边人对你更强烈的爱和信任，那是无价之宝。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最好的反击是你并不是诋毁里所描述的那种人，后面的生活里自然出现诋毁者很难解释、很难自圆其说的事实（如被说小气而后有人感谢你慷慨相助；被说不懂科学而几个月后上了好论文）。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不需要是你为“报复”赌气去干的事，而是你本来就不是ta们想象的那种人；你只需接着生活下去，对方就自然要挨反击。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "越来越多的事实会让诋毁你的言论一天比一天尴尬；过几年对方成熟懂事后回头看自己当初的蠢话会无地自容。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "ta们若还在亲朋好友面前大声发表过这些诋毁，诋毁会成为亲友认定其“缺少判断力”的依据，其潜在损失难以想象——本来能借到的钱就不好借了。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最后ta们会静悄悄来删评论，但那不是最好的做法；真正最明白的人会回来道歉、承认错误，只有正面承认错误才能从自己造成的厄运里解脱出来。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "删掉、抹去痕迹、拉黑ta们，其实是在保护ta们；ta们不懂罢了。", "evidence": ["E21"]}
   ],
   "argument_steps": [
    "承接提问先承认不适，再定性为考验（P001）。",
    "给出品质命题：原谅与不计较重要（P002）。",
    "点明动机：不追究是为身边的人，而非为诋毁者（P003）。",
    "反面推演睚眦必报的后果：身边人怵然而惧，并给出两层寒心的理由（P004-P006）。",
    "转入收益侧：克制换来爱与信任，诋毁者不值得作为关注中心（P007-P011）。",
    "反驳“必须反击”的取向：真正的反击是生活事实的自然呈现（P012-P018）。",
    "预测诋毁者的长期处境与潜在损失（P019-P021）。",
    "收尾判定：道歉才是解脱，删痕拉黑反而是保护对方（P022-P024）。"
   ],
   "concept_usage": [
    {"term": "反击", "meaning": "本文指的不是即时回击，而是你并非对方所描述的那种人、由后续生活自然呈现的事实。", "evidence": "P013", "ambiguity": "作者未说明这种“反击”是否被诋毁者感知或承认。"},
    {"term": "寒心", "meaning": "身边人因你对待路人的方式而产生的两层失望与恐惧。", "evidence": "P006", "ambiguity": "“一层/第二层”为作者自定的层次划分。"},
    {"term": "暴力手段", "meaning": "作者用引号指对诋毁者进行“处理”的手段。", "evidence": "P007", "ambiguity": "具体所指（现实暴力、网络报复或其他）未说明。"},
    {"term": "过客/坏天气", "meaning": "比喻诋毁者与你的关系是短暂且不可控的，不构成你世界的支点。", "evidence": "P008", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "“君子报仇十年不晚”“十倍奉还”“以眼还眼、以牙还牙”：作者引号引用并加以批评的流行说法（P004）。",
    "“对方说你小气，过两个月有人出来感谢你慷慨相助”：作者以“比如”举的假设性例子（P014）。",
    "“对方说你不懂科学，结果过几个月你上了好论文”：同上，假设性例子（P015）。",
    "无礼路人、诋毁者、身边人、爱你的人：作者使用的泛称角色，未涉及具体人物或事件（全篇）。",
    "过客、坏天气、基石、无价之宝：作者的比喻材料（P008-P011）。",
    "提问字段的“被恶意诋毁是种怎样的体验”是被回应的提问，非作者主张（Q001）。"
   ],
   "conditions": [
    "“人如果受不得委屈、吃不得亏，必要以眼还眼、以牙还牙”（P004）——假设条件，引出反面后果。",
    "“你虽然委屈，却没有使用暴力手段去‘处理’对方”（P007）——克制是获得收益的前提。",
    "“如果你处理得好”（P010）——诋毁转化为爱与信任的条件。",
    "“这不需要是你为了‘报复’这些人而赌气干的事”（P017）——排除动机条件。",
    "“过个几年ta自己成熟点、懂点事了”（P020）——诋毁者醒悟的时间条件。",
    "“ta们如果还大声在自己的亲朋好友面前发表过这些诋毁”（P021）——损失扩大的条件。",
    "“只有这样正面承认错误，ta们才会真的从自己造成的厄运里解脱出来”（P023）——明示的必要条件。"
   ],
   "rhetoric_and_tone": "第二人称劝导口吻，先共情（“当然是不舒服的”）后说理；大量对比（路人/身边人、吃亏/收获千百倍）；引号引用俗语再作否定（“十倍奉还”“处理”）；以“过客”“坏天气”“基石”“无价之宝”作比喻；结尾“其实是在保护ta们。ta们不懂罢了”在宽容与轻微讥讽之间收束。",
   "unresolved_questions": [
    "“暴力手段”（P007）具体所指不明：现实暴力、网络报复或法律手段均可能，正文未说明。",
    "P015“上了好论文”以什么标准衡量，正文未说明，属需外部核查的事实性表述。",
    "全篇未给出任何具体诋毁事件、人物或平台，P014-P015 的例子均为“比如”引出的假设。",
    "“ta们”的群体边界（诋毁者、路人、旁观亲友）在部分段落中可作多重理解。",
    "记录含 updated_at（2025-11-13）晚于 published_at（2020-10-22），正文是否经修改无法从本记录判断。",
    "brief 与正文重合且被截断（“最大的问题是会让身边人”后中断），仅作导航。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "当然是不舒服的，但这也是考验自己的一个好机会。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P002", "quote": "人不知而不愠，而可以原谅，可以不计较，是非常重要的品质。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P003", "quote": "你不追究这些人，不是为了这些人，而是为了你身边的人。", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P004", "quote": "最大的问题是会让身边人怵然而惧。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P005", "quote": "让你受委屈的机会远远超过这些路人无数倍", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P006", "quote": "这就已经是一层寒心；第二，ta们会害怕你，这是第二层寒心。", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P007", "quote": "你是在那些人那里吃了点亏，但在爱你的人这里，你收获了千百倍。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P008", "quote": "因为ta们不过是过客，如同坏天气。", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P009", "quote": "关键是你身边的人怎么想，爱你的人怎么想。ta们才是你的世界的基石。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "人对你的诋毁，反而会转化为身边人对你更强烈的爱和信任。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "在后面的生活里自然而然的出现诋毁者很难解释、很难自圆其说的事实。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "比如对方说你小气，过两个月有人出来感谢你慷慨相助。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "对方说你不懂科学，结果过几个月你上了好论文。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "这不需要是你为了“报复”这些人而赌气干的事", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "你只需要接着生活下去，对方就自然要挨反击。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "自然会让诋毁你的言论一天比一天尴尬。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "这些诋毁自然而然会成为亲朋好友认识到“ta缺少判断力”的一个依据。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "本来能借到的钱，可就不好借了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "真正最明白的人，会回来道歉、承认错误。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "ta们才会真的从自己造成的厄运里解脱出来。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "其实是在保护ta们。ta们不懂罢了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际冲突与应对", "道德修养/情绪管理"],
   "issue_candidates": ["被诋毁时的应对方式", "报复的代价", "身边人的旁观视角"],
   "text_function_candidates": ["答疑", "劝诫式说理"],
   "object_candidates": ["提问者（未具名）", "诋毁者（泛称）", "身边人与亲友（泛称）"],
   "working_keywords": ["诋毁", "反击", "睚眦必报", "寒心", "身边人", "无价之宝", "十年不晚"]
  },
  "notes": "本篇无图片节点（lexical 仅 paragraph 24），正文 P001-P024 全部通读，status=read、full_text_checked=true。全文无具体事件与人物，例子均为假设；“暴力手段”“上了好论文”等表述含义或标准待核，已记入未决问题。"
 },
 "ee56045a": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：表弟声称「伟大和自私，本质上是同一码事」，如何看待这句话？被评论的论断出自提问者转述的表弟，不是作者的话。作者没有逐字评断“本质上是同一码事”，而是提出自己的替代表述：人没有伟大的，只有一种自私和另一种自私，并主张追求善良者应自觉认识到这一点。（平台 zhihu，发表 2020-10-22）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者的主张：人没有伟大的，只有一种自私和另一种自私；追求善良的人不应自认为在追求伟大，而应认识到自己也在追求另一种自私。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "理由与收益：这种认识是好事，可避免做了点事就要求赞美、有几个人受益就觉得世界欠自己飞黄腾达；是真正有点正面成就的必修课。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "进一步主张：非要认定某些自私是伟大，这个执念本身就妨碍人“伟大”；要“伟大”的认证就“伟大”不了，丢掉这念头反而最可能被旁人看作“伟大”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "以英文短句点出上述反差的诗性反讽。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人没有伟大的，只有一种自私和另一种自私，这没有什么好讳言的。", "evidence": ["E01"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "追求善良的人不应该自认为是在追求伟大，而最好老老实实、清清楚楚地认识到自己也不过是在追求另一种自私。", "evidence": ["E02", "E03"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种认识是好事，可以避免自己做了点事情就觉得人人都应该赞美自己、有几个人受益就觉得世界欠自己飞黄腾达；这是一个人真正有点正面成就的必修课。", "evidence": ["E04", "E05", "E06"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "非要认定某些自私是伟大，这个执念本身就妨碍了人“伟大”。", "evidence": ["E07"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "你要“伟大”的认证，你就“伟大”不了；你丢掉“伟大”这个念头，反而会有最大的概率被旁人在最后看为“伟大”。", "evidence": ["E08"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以上述反差为“又一出诗性的反讽”（Yet another poetic irony）。", "evidence": ["E09"]},
    {"claim_id": "C007", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "提问者转述其表弟的论断：“伟大和自私，本质上是同一码事”——见于提问字段（Q001），属被转述的第三方说法，本文未把它作为作者主张。", "evidence": []}
   ],
   "argument_steps": [
    "先给出自己的替代表述：人没有伟大的，只有一种自私和另一种自私（P001）。",
    "由此给追求善良者一条自我认识上的要求（P002）。",
    "说明这样认识的好处：抑制自我神圣化与索取回报的心态（P003-P004）。",
    "把它定为取得正面成就的必修课（P005）。",
    "指出反向代价：执意认定某些自私伟大，反而不利于“伟大”（P006）。",
    "用对举句给出机制：求认证则不得，弃念头反而最可能被旁人看作“伟大”（P007）。",
    "以英文短句收束为反讽（P008）。"
   ],
   "concept_usage": [
    {"term": "伟大", "meaning": "本文均加引号使用，指人自我认定或向他人索取的道德高度认证，作者认为没有人当得起，且追求它会自我妨碍。", "evidence": "P001", "ambiguity": "未给定义或判定标准；“被旁人看为伟大”与“自认伟大”是两种不同用法。"},
    {"term": "自私", "meaning": "作者用它统称人的一切追求动机，故有“一种自私和另一种自私”之分，未作褒贬。", "evidence": "P001", "ambiguity": "“另一种自私”的具体内涵未界定。"},
    {"term": "认证", "meaning": "指对外部承认的索取（要求被认定伟大）。", "evidence": "P007", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "提问者转述的表弟论断「伟大和自私，本质上是同一码事」：被评论的第三方说法，非作者主张（Q001，无对应正文段落）。",
    "“做了点事情就觉得人人都应该赞美自己”“有几个人受益就觉得世界欠自己飞黄腾达”：作者描述的泛化心态，非具体人事（P004）。",
    "无任何具体人物、事件或数据作为例证；正文仅264字。"
   ],
   "conditions": [
    "“你要‘伟大’的认证”／“你丢掉‘伟大’这个念头”（P007）——条件对举，分别对应两种结果。",
    "“被旁人在最后看为‘伟大’”（P007）——结果取决于他人的最终评价。",
    "“最大的概率”（P007）——作者用概率限定，未作必然判断。",
    "“有几个人受益”（P004）——描述索取心态时的最小规模情形。"
   ],
   "rhetoric_and_tone": "短促断言开篇，“这没有什么好讳言的”显坦率、不回避的语气；叠词“老老实实的、清清楚楚的”加强自我要求；以“必修课”作教育隐喻；“伟大”一词全程加引号表示保留态度；以未翻译的英文短句“Yet another poetic irony.”作反讽收束，带冷峻的调侃意味。",
   "unresolved_questions": [
    "作者未界定“伟大”“自私”的含义，也未直接评断表弟那句“本质上是同一码事”中“本质”的所指。",
    "“另一种自私”的具体内涵正文未说明。",
    "提问者转述的表弟原话无法核验：该句仅见于提问字段，作者也未引用其完整表述。",
    "正文极短（264字），无例证与论证展开，“最大的概率”亦无依据说明。",
    "记录含 updated_at（2021-05-16）晚于 published_at（2020-10-22），正文是否经修改无法从本记录判断。",
    "brief 与正文重合且被截断（结尾停在“这是”），仅作导航。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "人没有伟大的，只有一种自私和另一种自私，这没有什么好讳言的。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P002", "quote": "追求善良的人不应该自认为是在追求伟大", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P002", "quote": "认识到自己也不过就是在追求另一种自私", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P003", "quote": "这是好事。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P004", "quote": "可以避免自己做了点事情就觉得人人都应该赞美自己，有几个人受益就觉得世界欠自己飞黄腾达。", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P005", "quote": "这是一个人真正有点什么正面成就的必修课。", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P006", "quote": "非要认定某些自私是伟大，这个执念本身就妨碍了人“伟大”。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P007", "quote": "你丢掉“伟大”这个念头，你反而会有最大的概率被旁人在最后看为“伟大”。", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P008", "quote": "Yet another poetic irony.", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德心理", "动机与自我评价"],
   "issue_candidates": ["伟大与自私是否同一回事", "行善的动机", "道德自我认证"],
   "text_function_candidates": ["答疑", "评论（对一句论断表态）"],
   "object_candidates": ["提问者的表弟（仅见提问字段）", "追求善良的人（泛称）"],
   "working_keywords": ["伟大", "自私", "认证", "执念", "poetic irony"]
  },
  "notes": "本篇无图片节点（lexical 仅 paragraph 8），正文 P001-P008 全部通读，status=read、full_text_checked=true。被评论的论断出自提问者转述的“表弟”（Q001），已单列为 cited_source，未归给作者。"
 },
 "9d092af8": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：中国古代建筑是如何处理高差的？作者按建筑类型给出做法清单：宫观类做地台与夯土台找平、一般民居先在地势高处找平（并指出品级制度限制）、讲究的大宅用细微坡度配合排水系统、另一类民居用柱框架空楼板、回廊依地势而建。（平台 zhihu，发表 2020-10-23）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "宫观类建筑抬高地面做地台，下为夯土基层，夯土层用须弥座或砖石保护；高差在做完夯土台后即找平。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "一般民居在地势相对高处先找平；作者在括号内纠正理解：不见得是没财力，而是品级制度不允许平民造台。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "细微高差安排更微妙：讲究的大宅整体地面有北高南低、中间高两侧低、堂高院低的轻微坡度，与明暗排水沟渠管道配合形成排水系统。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "另一类民居的找平与地面基本无关：一楼地板与真正地面悬空，靠柱子和框架在起伏地面上举起可铺地板的平面。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "回廊这类基本依地势而建。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "宫观类建筑都会抬高地面、额外做出地台，下面是夯土基层；夯土层还要用须弥座或者砖石保护起来；高差在做夯土台之后就找平了。", "evidence": ["E01", "E02", "E03"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一般民居也会在地势相对高的地方先把地找平；作者并纠正一种可能误解：这不见得是没财力，而是品级制度不允许平民造台。", "evidence": ["E04", "E05"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "细微的高差安排更为微妙：一些比较讲究的大宅，整体地面有北高南低、中间高两侧低、堂高院低的轻微坡度，与明暗排水沟渠管道配合形成排水系统。", "evidence": ["E06", "E07"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "还有一类民居的找平与地面基本无关：一楼地板与真正的地面之间悬空，用柱子和框架从起伏不平的地面上举起一个可供铺地板的平面。", "evidence": ["E08", "E09"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "至于回廊这类，就基本是依地势而建了。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "先给出最常见做法：宫观类做地台、夯土基层、须弥座或砖石护面，做完夯土台即完成找平（P001）。",
    "补充民居的做法，并预先纠正“没财力”的误读，指出是品级制度限制（P002）。",
    "进一步说明讲究做法中的细微坡度与排水系统的配合（P003）。",
    "补充另一类以柱框架空楼板来实现找平的民居（P004）。",
    "最后以“基本依地势而建”收束回廊这一类（P005）。"
   ],
   "concept_usage": [
    {"term": "高差", "meaning": "指建筑基址与地面、以及院内各部分之间的高低差别，本文的“处理”方式包括做台找平、做坡排水、架空楼板、依势而建。", "evidence": "P001", "ambiguity": "未区分山地与平地等不同地形条件下的差别。"},
    {"term": "找平", "meaning": "通过夯土台、选高地势、柱框架空等方式获得可供使用的水平面。", "evidence": "P002", "ambiguity": "除夯土台外的具体工艺未说明。"},
    {"term": "品级制度", "meaning": "作者用它解释平民不做台的原因：不是财力不足，而是制度不允许。", "evidence": "P002", "ambiguity": "未指明具体朝代与制度条文，属需外部核查的表述。"},
    {"term": "须弥座", "meaning": "文中指用于保护夯土层的台座式做法（或砖石护面）。", "evidence": "P001", "ambiguity": "此处用法偏“台座/护面”之意，与一般建筑术语中的须弥座关系未展开。"}
   ],
   "examples_and_targets": [
    "宫观类建筑、一般民居、讲究的大宅、一楼架空的民居、回廊：作者按类型举的建筑类别，非具体实例（全篇）。",
    "夯土台、地台、须弥座、砖石护面、明暗排水沟渠管道、柱子与框架：文中出现的构件与做法（P001-P004）。",
    "IMG001、IMG002（未核验）：位于P001之后，疑为宫观类地台做法的图例；IMG003（未核验）：位于P004之后，疑为架空楼板民居的图例。",
    "提问字段的“中国古代建筑是如何处理高差的”是被回应的提问，非作者主张（Q001）。"
   ],
   "conditions": [
    "“一般民居也会在地势相对高的地方先把地找平”（P002）——民居做法依赖选址条件。",
    "“实际上不见得是没财力，而是品级制度不允许平民造台”（P002）——把“不做台”限定为制度原因。",
    "“一些比较讲究的大宅”（P003）——把细微坡度限定于特定等级与讲究程度的建筑。",
    "“还有一类民居”（P004）——明示这只是若干类型中的一类。",
    "“至于回廊这类就基本是依地势而建了”（P005）——以“基本”作程度限定。"
   ],
   "rhetoric_and_tone": "说明文体，按建筑类型分类罗列，句子短、术语直接，无修辞铺陈与价值判断；唯一带议论色彩处是括号内的纠偏（“实际上不见得是没财力，而是品级制度不允许平民造台”），语气平实。",
   "unresolved_questions": [
    "IMG001-IMG003 未核验：两图在P001之后（疑为宫观类地台与夯土台做法）、一图在P004之后（疑为架空楼板民居），图与文字的对应关系只能推测，需图像核验。",
    "“品级制度不允许平民造台”未给出朝代、制度名称或出处，属需外部核查的事实性表述。",
    "全篇未给出任何具体建筑实例、年代与地域。",
    "“须弥座”“砖石保护”的具体构造，以及夯土台以外如何找平，正文未展开。",
    "结构记录显示 lexical 有 9 个 paragraph 节点而正文非空段落为 5 个（另有 3 个图片节点与 1 个空段落），空段落位置未在阅读包中给出；divergence=false。",
    "记录含 updated_at（2025-12-10）晚于 published_at（2020-10-23），正文是否经修改无法从本记录判断。",
    "brief 与正文首段部分重复且被截断（“一些比较讲究”后中断），仅作导航。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "宫观类建筑都会抬高地面，额外做出地台来。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P001", "quote": "这个夯土层还要用须弥座或者砖石保护起来。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P001", "quote": "高差在做夯土台之后就找平了。", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P002", "quote": "一般民居也会在地势相对高的地方先把地找平", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P002", "quote": "实际上不见得是没财力，而是品级制度不允许平民造台", "relation": "qualifies"},
    {"key": "E06", "paragraph_id": "P003", "quote": "整体地面有一个北高南低、中间高两侧低、堂高院低的轻微坡度", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P003", "quote": "与明暗排水沟渠管道配合形成一个排水系统。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P004", "quote": "它的一楼地板和真正的地面之间是悬空的", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P004", "quote": "靠一系列的柱子和框架从起伏不平的地面上举起一个可供铺地板的平面就可以了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P005", "quote": "至于回廊这类就基本是依地势而建了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国古代建筑", "建筑技术史"],
   "issue_candidates": ["建筑基址高差处理", "夯土台与地台做法", "民居找平与架空楼板", "建筑排水坡度"],
   "text_function_candidates": ["答疑", "建筑做法说明"],
   "object_candidates": ["宫观类建筑", "一般民居", "讲究的大宅", "回廊"],
   "working_keywords": ["高差", "地台", "夯土台", "须弥座", "找平", "明暗排水沟渠", "架空楼板", "品级制度"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含3个图片节点（IMG001、IMG002 在P001之后，IMG003 在P004之后），图片内容未经核验，需图像核验；正文文本已通读（P001-P005），故按简报要求标 status=needs_reread、image_checked=false、full_text_checked=false。"
 },
 "4eac69b1": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：如何评价电影《金刚川》？作者的评价分三层：先从电影技术角度给“中规中矩、及格过线”，再把它当作中国文艺界“镜头说书”系统问题的样本，最后转为对该片体现的电影工业能力的肯定，并引申到电影创作者与“美”的讨论。（平台 zhihu，发表 2020-10-24）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "总体技术评价：中规中矩、及格过线；故事情节简短，靠叙事手法撑到两小时有些勉强；战斗经过有勉强安排冲突之感。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "诊断：影片像文艺工作者基于有限资料对朝鲜战场的想象与重构，缺少背景知识，犯下过于“镜头说书”的老问题；作者认为这在中国文艺界几乎是系统问题。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "归因：文化软实力不足与电影学院制度有关——培养“职业导演/职业艺术家”，但职业说书人缺少真实生活与对接专业顾问的能力，精力过多放在把既定故事讲得漂亮。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "代际观察：第五代靠时代给的“戏”，第六代靠打开眼界带来的海外的戏；但时间久了内里是空的，只剩身段、唱腔与各种“筋斗”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017"], "summary": "转折：中国电影的希望在这片子里——2600人团队、三位导演、三个月完成，成品不算优秀但算“行货”，技术上无明显瑕疵，是电影工业极限考验下的漂亮答卷。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "由“器”论推进：工欲善其事必先利其器，器越利则对“工”的门槛越低，成熟工业体系能帮有戏但不工的创作者做出中等水准以上的作品。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "对创作者的要求：要有戏、有看得见戏的“心眼”、有能用人的心胸气度，才能摆脱把别人的故事当调料、把外来元素撒在炸酱面上的“万国炸酱面”困局。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032"], "summary": "立论：顾问、老战士、战场文物、史家才是“戏肉”；他们是故事、你才是佐料；明白则食神，否则只是伙夫，百年之后无人记得，因为你做的只是讲故事的技术。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P033", "P034", "P035"], "summary": "提升到文明层面：武力不足以让文明立住，唯有美能刻下名字；人类看不到“真”，美就是正与邪的分野。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P036", "P037"], "summary": "作者自陈忧虑所在：不忧虑武力威胁，而忧虑民族把美视为虚无软弱的业余之事与点缀。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040"], "summary": "以三段短句作结：黄金铺台、钢铁铸座，唯桂枝做得成王冠。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只从纯电影技术的角度说，该片中规中矩、及格过线。", "evidence": ["E01"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "故事本身情节简短，如果保证信息密度估计只够拍半个小时，靠叙事手法做到两个小时实在有些勉力为之。", "evidence": ["E02"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "具体的战斗经过，有一定的勉强安排剧情冲突的感觉。", "evidence": ["E03"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "给人的感觉是这片子拍的是文艺工作者基于短时间有限的资料采集对朝鲜战场的想象和重构；因缺少足够背景知识，犯了过于“镜头说书”的老问题。", "evidence": ["E04", "E05"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这在中国的文艺界几乎是一个系统的问题。", "evidence": ["E06"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的文化软实力不足与电影学院制度有非常深的关系：学院培养“职业导演”“职业艺术家”，致命问题是这些职业说书人自己缺少真实的生活，又缺少与专业顾问资源必要的对接能力。", "evidence": ["E07", "E08"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他们的能力培养过多注重于把既定故事讲得漂亮美观（不是好，只是漂亮），占用了职业生涯的过多精力。", "evidence": ["E09", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第五代导演的成功在于因时代原因碰巧人生有戏，有戏加叙事技巧就会出佳作；但老天爷赏的戏不是无限的，时间久了不免出现匮乏、重复。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第六代导演主要靠打开眼界，技术、市场尤其是国际交流带来的海外的戏给了他们养分；但时间久了内里是空的，故事敷衍，全是身段、唱腔和筋斗。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "西洋筋斗、东洋筋斗、视觉合成筋斗，毕竟仍然只是筋斗。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国电影的希望在这片子里：它是2600人的团队配合三位导演只用三个月做出来的；成品不算优秀，但完全可以算“行货”，镜头、表演、特效、场景管理、调色、配音、配乐全都中规中矩、老练劲道。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是一次电影工业的极限考验，答卷交得令人意外的漂亮：2600人分属不同企业、不同职能，放在一般组织三个月连沟通会都开不完，而该片在技术上没有肉眼可见的瑕疵。", "evidence": ["E19", "E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "工欲善其事，必先利其器；事虽仍未善，这器的确可以开始露出一点利的意思了。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "器越利，对“工”的门槛就越低，越容易给有戏但不工的创作者机会：不熟练、不懂规矩，也有成熟电影工业体系帮助做出中等水准以上的东西。", "evidence": ["E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "创作者要做的是有戏、有看得见戏的“心眼”，以及能用得了人的心胸气度；有心胸气度才能最大限度利用专业人的技术能力，有看得见戏的心眼才能在上天赏赐了故事的人面前谦卑。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "而不是只会把他们的故事切成葱花、拍成蒜末，拿来做自己那碗炸酱面的调料。", "evidence": ["E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有进到这层境界，电影艺术工作者才能变成脚踏大地的泰坦，不再受限于个人经历，也不再受限于别人的作品（尤其所谓“商业片”）。", "evidence": ["E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有这样才能摆脱买咖喱撒在炸酱面上做出“印度菜”、抹芥末端出“日本料理”的终极困局。", "evidence": ["E29"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "军事技术顾问、受访的志愿军老战士、战场文物与战争痕迹、历史学家与战史专家那里才是“戏肉”：不是编个故事再撒点他们的东西当佐料，而是他们是故事、你才是佐料；你是厨师，但农夫和牧人才是餐桌的主角。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "什么时候你明白，什么时候你就是食神；否则任你如何努力，也只是伙夫而已。", "evidence": ["E33", "E34"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不论多少人捧你，百年之后将无人记得你——因为没有人会用更新的技术把你的故事再讲一次，而看过你的人都已死去；追根到底，你做的不是故事，而是讲故事的技术。", "evidence": ["E35", "E36"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有千军万马、横行天下并不足以让一个文明真正立住；真正让一个文明在人类历史上刻下永不磨灭名字的，只有它所创造的美。", "evidence": ["E37"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类的眼睛是看不到“真”的；对人类而言，美就是正与邪的分野。", "evidence": ["E38", "E39"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者一点也不忧虑还有任何人能在武力上真正威胁到中国的根本安全——此非人力所能及，也显然不是天心所愿。", "evidence": ["E40"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者所忧虑的是这个民族将美普遍视作一种虚无软弱的业余之事、一种点缀、一种余兴节目；这是真正阻碍这个中央之国回到它该有的位置的最大问题。", "evidence": ["E41"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以诗句收束：黄金能铺就高台、钢铁能铸成王座，但唯有桂枝才做得成王冠。", "evidence": ["E42"]}
   ],
   "argument_steps": [
    "先给出技术层面的低限评价（中规中矩）与剧作层面保留（情节短、冲突安排勉强）（P001-P003）。",
    "把影片归因为资料有限条件下的想象与重构，命名为“镜头说书”问题（P004）。",
    "把问题推到行业制度层面：电影学院培养方式与职业说书人的短板（P005-P007）。",
    "以第五代、第六代导演的得失作历史佐证（P008-P011）。",
    "转折设问“中国电影还有希望吗”，从该片的工业协作能力给出肯定（P012-P017）。",
    "由“器”与“工”的关系推出工业成熟对创作者的助益（P018-P019）。",
    "转向对创作者的要求与“万国炸酱面”困局（P020-P025）。",
    "以顾问、老战士、史家为“戏肉”，重排故事与创作者的位置，落到食神/伙夫之别（P026-P032）。",
    "再提升为文明与美的一般判断（P033-P035）。",
    "以自陈忧虑点明现实关切（P036-P037），以诗体三句收束（P038-P040）。"
   ],
   "concept_usage": [
    {"term": "镜头说书", "meaning": "作者用引号标示的批评用语：以镜头技巧讲述一个既定故事，而缺少真实生活与背景知识支撑。", "evidence": "P004", "ambiguity": "未给出判定标准，仅以该片为例。"},
    {"term": "有戏/工", "meaning": "“有戏”指拥有值得讲述的真实故事与人生经验，“工”指电影技术与工艺；作者认为工业成熟可补“工”之不足，但“戏”不可替代。", "evidence": "P019", "ambiguity": "“有戏”的判定标准未说明。"},
    {"term": "戏肉", "meaning": "指顾问、老战士、战场文物、史家等一手经验与资料中所含的真正内容。", "evidence": "P026", "ambiguity": "口语化用词，未界定范围。"},
    {"term": "美", "meaning": "作者在结尾把它抬到文明立身与正邪分野的层次，认为武力不足以让文明立住，唯美能刻下名字。", "evidence": "P033", "ambiguity": "未给“美”的定义；P035“美，就是正与邪的分野”为其强表述。"},
    {"term": "中央之国", "meaning": "作者用来指称中国，并称其有“该有的位置”。", "evidence": "P037", "ambiguity": "“该有的位置”具体所指未说明。"}
   ],
   "examples_and_targets": [
    "电影《金刚川》：全文的评价对象；作者称其为2600人团队、三位导演、三个月完成（制作数据属作者陈述，待外部核查）（P013、P016）。",
    "第五代导演、第六代导演：作者的历史性概括，未点名任何具体人物与作品（P008-P010）。",
    "朝鲜战场、志愿军老战士、军事技术顾问、历史学家、战史专家、战场文物与战争痕迹：作者举出的行业与资料对象（P004、P026）。",
    "筋斗、身段、唱腔：作者借戏曲语汇比喻第六代导演作品中的技术表演性（P010-P011）。",
    "炸酱面、葱花、蒜末、咖喱、芥末、淘宝包邮、菜场、“印度菜”“日本料理”“万国炸酱面”：作者的修辞材料，用于批评拼贴式创作（P023-P027）。",
    "食神与伙夫、厨师与农夫牧人、脚踏大地的泰坦：作者的比喻（P024、P029、P030）。",
    "黄金、钢铁、桂枝、王座、王冠：结尾诗句中的比喻材料（P038-P040）。",
    "提问字段的“如何评价电影《金刚川》”是被回应的提问，非作者主张（Q001）。"
   ],
   "conditions": [
    "“从纯电影技术的角度说”（P001）——限定该评价只就技术而言。",
    "“其实如果保证信息密度的话，估计只够拍半个小时”（P002）——假设与估计语气。",
    "“有一定的勉强安排剧情冲突的感觉”（P003）——程度限定。",
    "“这在中国的文艺界几乎是一个系统的问题”（P005）——以“几乎”限定普遍性。",
    "“第五代导演之所以成功，在于他们因为时代原因碰巧人生有戏”（P008）——把成功归因于时代与偶然。",
    "“但这些老天爷赏的戏毕竟不是无限的，时间久了不免出现匮乏、重复”（P008）——资源有限的时间条件。",
    "“只用了三个月做出来的”（P013）、“放在一般的组织，三个月时间怕是连沟通会都没开完”（P016）——制作时间及其对比条件。",
    "“只有进到这层境界”（P024）、“只有这样才能摆脱”（P025）——必要条件表述。",
    "“不论多少人捧你，百年之后将无人记得你”（P031）——时间尺度的限定。",
    "“我一点也不忧虑……我所忧虑的，是……”（P036-P037）——作者明确区分不忧虑与忧虑的对象。"
   ],
   "rhetoric_and_tone": "影评、行业批评与文明论三段递进；用设问“那么中国电影还有希望吗？”转折；比喻密集且带厨房与戏曲两套词汇（筋斗、身段、唱腔、炸酱面、万国炸酱面、食神、伙夫、厨师与农夫牧人）；引用古语“工欲善其事，必先利其器”；口语词（行货、戏肉、心眼）与庄重表述并用；结尾三段短句排比，带诗体与宣言式语气；全篇以第二人称“你”对创作者说话。",
   "unresolved_questions": [
    "“三位导演”未点名；第五代、第六代导演未给出具体人物与作品，属概括性代际叙述。",
    "2600人、三位导演、三个月等制作数据无法在本记录内核验，标为待外部核查，不作判断。",
    "“中国的文化软实力不足”（P006）未给出衡量依据或数据。",
    "P036“也显然不是天心所愿”的“天心”所指不明（带天命/宗教意味的表述），正文未解释。",
    "“中央之国”“它该有的位置”（P037）未给出具体含义与标准。",
    "记录含 updated_at（2022-01-27）晚于 published_at（2020-10-24），正文是否经修改无法从本记录判断。",
    "brief 与正文首段重合且被截断（“文艺工作者基于短时间有限的资料采集”后中断），仅作导航。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "这个片子从纯电影技术的角度说，只能说中规中矩，及格过线。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P002", "quote": "其实如果保证信息密度的话，估计只够拍半个小时，靠叙事手法做到两个小时，实在有些勉力为之。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P003", "quote": "具体的战斗经过，有一定的勉强安排剧情冲突的感觉。", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P004", "quote": "给人的感觉是这片子拍的是文艺工作者基于短时间有限的资料采集，对朝鲜战场的一种想象和重构。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P004", "quote": "犯下了一个老问题——过于“镜头说书”。", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P005", "quote": "这在中国的文艺界几乎是一个系统的问题。", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P006", "quote": "中国的文化软实力不足，和我们的电影学院制度有非常深的关系。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P006", "quote": "这些职业说书人，自己缺少真实的生活，又缺少与专业顾问资源必要的对接能力。", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P007", "quote": "过多的注重在如何将一个既定的故事讲得漂亮美观（注意，不是好，而只是漂亮", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "这占用了他们职业生涯的过多精力。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "第五代导演之所以成功，在于他们因为时代原因碰巧人生有戏。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "但这些老天爷赏的戏毕竟不是无限的，时间久了不免出现匮乏、重复", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P009", "quote": "而第六代导演则主要是靠打开了眼界，技术、市场、尤其是国际交流所带来的海外的戏，给了他们扬名立身的充分养分。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P010", "quote": "但是时间久了，你会看到内里是空的。故事是敷衍的，全是身段、唱腔和筋斗。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P011", "quote": "西洋筋斗、东洋筋斗、视觉合成筋斗，毕竟仍然只是筋斗。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "它是2600人的团队，配合三位导演，只用了三个月做出来的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "成品的确不算优秀，但完全可以算“行货”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P014", "quote": "全都中规中矩，老练劲道。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P015", "quote": "这是一次电影工业的极限考验，而这答卷交得令人意外的漂亮。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P016", "quote": "而且居然在技术上没有什么肉眼可见的瑕疵。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P018", "quote": "工欲善其事，必先利其器。事虽仍未善，这器的确可以开始露出一点利的意思了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P019", "quote": "器越利，对工的门槛就越低。就越容易会给有戏但不工的创作者机会", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P019", "quote": "自有成熟的电影工业体系给你足够的帮助，帮你做出中等水准以上的东西来。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P020", "quote": "你要做的，是要有戏，是有看得见戏的“心眼”。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P021", "quote": "有心胸气度，就能最大限度的利用专业人的技术能力去做好表达。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P022", "quote": "有看得见戏的心眼，才能真的在上天赏赐了故事的人面前谦卑。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P023", "quote": "而不是只会把他们的故事切成葱花，拍成蒜末", "relation": "contradicts"},
    {"key": "E28", "paragraph_id": "P024", "quote": "只有进到这层境界，一个电影艺术工作者才能变成脚踏大地的泰坦", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P025", "quote": "只有这样才能摆脱现在这种去菜场买点咖喱，往炸酱面上一撒，就做出一道“印度菜”", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P026", "quote": "你咨询的那些历史学家、战史专家……戏肉在他们那里。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P028", "quote": "而是他们是故事、你才是佐料。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P029", "quote": "你是个厨师，但农夫和牧人才是餐桌的主角。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P030", "quote": "什么时候你明白，什么时候你就是食神。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P030", "quote": "否则任你如何努力，也只是伙夫而已。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P031", "quote": "不论多少人捧你，百年之后将无人记得你", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P032", "quote": "因为追根到底，你做的不是故事，而是讲故事的技术罢了。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P033", "quote": "真正让一个文明在人类的历史上刻下永不磨灭的名字的，只有它所创造的美。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P034", "quote": "人类的眼睛是看不到“真”的。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P035", "quote": "对人类而言，美，就是正与邪的分野。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P036", "quote": "我一点也不忧虑这个世界上还有任何人能在武力上真正的威胁到中国的根本安全", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P037", "quote": "我所忧虑的，是这个民族将美普遍视作一种虚无软弱的业余之事，一种点缀，一种余兴节目。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P040", "quote": "但唯有桂枝，才做得成王冠。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["电影批评", "文艺创作与industry制度", "文化评论/文明论"],
   "issue_candidates": ["《金刚川》影片评价", "电影学院培养制度", "创作者与真实生活/顾问资源的关系", "美与文明"],
   "text_function_candidates": ["影评", "行业批评", "评论", "宣言式议论"],
   "object_candidates": ["电影《金刚川》", "第五代/第六代导演（泛称群体）", "志愿军老战士", "军事技术顾问", "历史学家/战史专家", "中国电影界"],
   "working_keywords": ["镜头说书", "职业说书人", "行货", "有戏", "戏肉", "万国炸酱面", "食神", "伙夫", "美", "桂枝"]
  },
  "notes": "本篇无图片节点（lexical 仅 paragraph 40），正文 P001-P040 全部通读，status=read、full_text_checked=true。2600人/三位导演/三个月等制作数据与“文化软实力不足”等判断已记入未决问题，标为待外部核查，未作裁决。"
 },
 "60fd68e8": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）：当全世界都爆发丧尸，哪里最安全？提问要求给出地理上的安全地点。作者没有回答“哪里最安全”，而是否定提问的威胁预设，提出一套诱捕—销毁的处置方案。（平台 zhihu，发表 2020-10-25）",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "核心判断：行为逻辑过于简单的丧尸不该对人类构成危机。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "理由式断言：非常简单的陷阱就能批量消灭丧尸。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004", "P005"], "summary": "方案设想：太阳能绞肉机后装大喇叭，前方大喇叭一站一站播放形成“采集网络”，层层接力把附近丧尸引到预定“销毁中心”，多个销毁中心定期轮流检修即可。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "丧尸这种行为逻辑过于简单的“猛兽”对人类根本不该构成危机。", "evidence": ["E01"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "非常简单的陷阱就能批量消灭丧尸。", "evidence": ["E02"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "设想方案：在太阳能绞肉机后面装一个大喇叭，前面再用大喇叭一站一站地播放，形成“采集网络”。", "evidence": ["E03"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "依靠依次播放、层层接力，把附近丧尸吸引到预定的“销毁中心”就可以。", "evidence": ["E04"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多个销毁中心定期轮流检修就行了。", "evidence": ["E05"]}
   ],
   "argument_steps": [
    "先否定提问的威胁预设：丧尸行为逻辑过于简单，不构成危机（P001）。",
    "给出可行性断言：简单陷阱即可批量消灭（P002）。",
    "以“比如”给出具体设想：太阳能绞肉机与大喇叭组成的“采集网络”（P003）。",
    "说明运作方式：依次播放、层层接力吸引丧尸至“销毁中心”（P004）。",
    "补充维护安排：多个销毁中心定期轮流检修（P005）。"
   ],
   "concept_usage": [
    {"term": "行为逻辑过于简单", "meaning": "作者用来判定丧尸不构成危机的理由，即其行动模式易被预测与诱导。", "evidence": "P001", "ambiguity": "该前提未展开论证，也未说明依据何种丧尸设定。"},
    {"term": "采集网络", "meaning": "带引号的方案术语：以大喇叭一站一站播放、层层接力把丧尸引导至销毁点的装置链。", "evidence": "P003", "ambiguity": "装置规模、间距与能源供给未说明。"},
    {"term": "销毁中心", "meaning": "带引号的方案术语：集中消灭被引来丧尸的场所（前接“太阳能绞肉机”）。", "evidence": "P004", "ambiguity": "构造、容量与安全性未说明。"}
   ],
   "examples_and_targets": [
    "太阳能绞肉机、大喇叭、“采集网络”、“销毁中心”：作者设想的装置与流程，非现实例证（P003-P005）。",
    "丧尸：虚构设定对象，来自提问者的假设情境（Q001），作者以“猛兽”加引号指称（P001）。",
    "无任何现实人物、机构、数据或历史事例。"
   ],
   "conditions": [
    "提问者设定“当全世界都爆发丧尸”（Q001）——本文讨论的整体前提，属提问者设定。",
    "“太阳能”（P003）——绞肉机供能方式的条件。",
    "“依靠依次播放，层层接力”（P004）——方案运作依赖连续性播放与接力引导。",
    "“定期轮流检修”（P005）——方案可持续性的维护条件。"
   ],
   "rhetoric_and_tone": "极简短（136字）的口语化工程设想，句式直陈、无铺垫；“猛兽”加引号带贬抑意味；“绞肉机”“销毁中心”“采集网络”构成工业化处置意象，把末世危机处理为设备运维问题；全篇未回答提问的“哪里最安全”，形成答非所问式的反驳姿态。",
   "unresolved_questions": [
    "正文未回答提问的地理安全问题“哪里最安全”，而是否定丧尸构成危机的预设，提问与回答不完全对应。",
    "“行为逻辑过于简单”这一前提未论证，也未说明依据（现实设定、影视设定或其他）。",
    "“太阳能绞肉机”的构造、能耗、容量与可行性未说明；“大喇叭”的有效范围亦未说明。",
    "正文仅136字，无数据、无出处、无实施细节与风险评估。",
    "brief 与正文基本重复（仅少量文字差异），仅作导航，不能单独支持主张。",
    "记录含 updated_at（2021-11-12）晚于 published_at（2020-10-25），正文是否经修改无法从本记录判断。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "丧尸这种行为逻辑过于简单的“猛兽”对人类根本不该构成危机。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P002", "quote": "非常简单的陷阱就能批量消灭。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P003", "quote": "比如在太阳能绞肉机后面装一个大喇叭，前面再用大喇叭一站一站的播放形成“采集网络”。", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P004", "quote": "依靠依次播放，层层接力吸引附近丧尸", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P005", "quote": "多个销毁中心定期轮流检修就行了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["虚构情境推演", "应急/工程设想"],
   "issue_candidates": ["丧尸危机的应对方案", "诱捕与销毁网络的设计"],
   "text_function_candidates": ["答疑", "方案设想", "反驳提问预设"],
   "object_candidates": ["丧尸（虚构设定）", "提问者（未具名）"],
   "working_keywords": ["丧尸", "太阳能绞肉机", "大喇叭", "采集网络", "销毁中心", "行为逻辑"]
  },
  "notes": "本篇无图片节点（lexical 仅 paragraph 5），正文 P001-P005 全部通读，status=read、full_text_checked=true。正文未回答提问的“哪里最安全”，已记入未决问题；brief 与正文基本重复，仅作导航。"
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
