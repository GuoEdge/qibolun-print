# -*- coding: utf-8 -*-
"""批次 r001-b0058 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0058.sessions.py            # 写 out/r001-b0058.out.jsonl
  python3 records/r001-b0058.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0058"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0058.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "a37fd4ea": {
  "analysis": {
   "question_context": "提问者问「聪明人更要下笨功夫」是什么意思（Q001，属提问者）。作者不反驳该说法，而以悖论式反问开场（P001-P002），随后给出自己的解释：这些功夫只是看起来很笨，去做它们才是最聪明的做法。正文为无标题的连续短段，无列表、引用块，图片节点 0。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以两个反问提出表面矛盾：聪明人怎么会做笨功夫、做笨功夫还算聪明人。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "反转前提：那些功夫只是看起来笨；聪明在于发现了没有第二捷径、绕不过去的苦路。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "机制理由：该功夫无法投机取巧、无法绕道，早起步且不松懈者形成他人（纵有无限资本）无法超越的壁垒。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "对比式理由：同等聪明、经验、资源、看见机会的人都有，肯做这件苦事的人罕有；差距只在肯不肯做。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017"], "summary": "结论：因此你有比较大的希望会赢。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "限定：这种笨功夫需绝顶聪明与绝佳运气才可能触及，且需绝顶聪明加极端努力才能确知无捷径。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "评价与比喻：上天安排“不做笨事就别想赢”的禁制令是仁慈；石墙要靠极聪明的笨人凿穿，墙后有阳光。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026"], "summary": "意义归结：真正的聪明人梦想命定于自己的笨事，那是心安之处、最平安的归宿与最恰如其分的死所。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029"], "summary": "收束：未曾体会者难以理解这种幸福；以格言与英文短句作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那些所谓笨功夫只是看起来很笨，去做它们其实是最聪明的做法。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "聪明之处在于发现了一些绝对没有第二捷径、绝对绕不过去的苦路。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在此类功夫上，只要早起步一个月且不松懈，别人即使有无限资本作后盾也绝对无法超越。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同样聪明、有同样经验与资源、且同样看见这件事的人都有，但同样肯做这件吃力不讨好苦事的人罕有。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "正因肯做者罕有，你才比较大的希望会赢（非必然）。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "满足全部条件的“绝妙笨功夫”需要绝顶聪明与绝佳运气才有机会触摸得到。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问表达：不是绝顶聪明外加极端努力，就无从知道这件事确确实实没有其他捷径可走。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上天安排“不做笨事就别想赢”的天然禁制令，是对人类极大的仁慈（评价性判断）。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的聪明人心心念念梦想那件命定属于自己的笨事，这种笨事是聪明人的心安之处。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "那些石墙注定要靠这种极聪明的笨人才有可能凿穿。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "开场以两个反问提出表面矛盾：聪明人怎么会做笨功夫／做笨功夫还怎么会是聪明人（P001-P002）",
    "反转前提：那些功夫只是看起来很笨，去做才是最聪明的做法（P003）；聪明在于发现绝对没有第二捷径、绕不过去的苦路（P004-P005）",
    "给出机制：该功夫无法投机取巧、无法绕道；唯一最快办法是靠条件相当、抱定决心并抗拒机会成本诱惑的人正面凿穿（P007），故早起步且不松懈者形成他人（纵有无限资本）无法超越的壁垒（P006）",
    "以“水滴石穿，直线前进”作过渡（P008）",
    "逐层对比：同样聪明者、同样经验者、同样有资源者、同样看见机会者都有，唯独同样肯做者罕有（P009-P015）",
    "点出唯一差距在于对方没你这么“笨”、不肯拿好条件“干这个”，由此推出你才比较大希望会赢（P016-P017）",
    "限定：该笨功夫需绝顶聪明与绝佳运气才可能触及（P018）；须绝顶聪明加极端努力才能确知无捷径（P019）",
    "价值升华：上天以“不做笨事就别想赢”的禁制令施予仁慈（P020-P021）；石墙要靠极聪明的笨人凿穿，墙后阳光普照（P022-P023）",
    "结论：真正的聪明人梦想命定于自己的笨事，那是心安之处、最平安的归宿与最恰如其分的死所（P024-P026）",
    "收束：未体会者难解其中幸福；以“笨人比聪明，聪明人比笨”与英文短句作结（P027-P029）"
   ],
   "concept_usage": [
    {"term": "笨功夫／笨事", "meaning": "看起来笨、无法投机取巧也绕不过去的苦功夫；被聪明人主动选中的必然吃力之路。", "evidence": "P003/P007/P018", "ambiguity": "“笨”既指方法上无巧可取，也指选择者被他人视为笨，两义在文中并置。"},
    {"term": "聪明", "meaning": "不是避免吃苦，而是能发现没有第二捷径的苦路并肯下注；与“绝顶聪明”“笨小孩”并置使用。", "evidence": "P005/P019/P020", "ambiguity": "未给出判定聪明的标准，主要靠对比与修辞界定。"},
    {"term": "石墙／玄武岩层", "meaning": "比喻需长期正面凿穿的障碍。", "evidence": "P007/P022", "ambiguity": "纯比喻，文中未指任何具体行业或问题。"},
    {"term": "天然禁制令", "meaning": "比喻“不做笨事就别想赢”的天然约束。", "evidence": "P021", "ambiguity": "非法律术语的字面用法，带拟人化修辞。"},
    {"term": "心安之处／死所", "meaning": "把绝妙笨事说成聪明人的归宿与最恰如其分的死去之所。", "evidence": "P025/P026", "ambiguity": "带宗教与诗意色彩，是否指向具体实践承诺不明确。"}
   ],
   "examples_and_targets": [
    "无具体人物、机构、事件或数据；全文以泛指人称展开。",
    "“石墙”“玄武岩层”“水滴石穿”为作者的比喻材料（P007-P008）。",
    "“哪怕拿着无限的资本做后盾”为假设性对手条件（P006），非实指对象。",
    "“老天／上天”为拟人化修辞主体（P020-P021）。",
    "反驳对象未点名：针对“聪明人做笨功夫不合算”的直觉（即P001-P002所设的悖论）。"
   ],
   "conditions": [
    "以“你不松懈”为前提（P006）；“如果早起步一个月”为假设条件（P006）。",
    "“满足上面这全部条件”的限定（P018）：需绝顶聪明、罕见机缘、深厚经验、难得资源。",
    "用“比较大的希望”“才有可能凿穿”，不作必然断言（P017/P022）。",
    "对象限定为具备上述条件的聪明人；未说明具体领域、时间尺度与规模。",
    "“不是绝顶聪明外加极端努力，你怎么知道……”暗示确知无捷径需此二条件（P019）。"
   ],
   "rhetoric_and_tone": "第二人称“你”与“ta们”对举的独白式劝导；开场与行文中反复使用反问（P001-P002/P004/P019）；措辞绝对化、夸张（“绝对没有第二捷径可言”“实在实在是太‘笨’了”）；军事与宗教意象（“必死的觉悟”“天然禁制令”“老天”“死所”）；结尾以格言“笨人比聪明，聪明人比笨”和英文短句“What a poetic irony”收束。整体语气为激励、训诫与自我确认，而非论证性说明。",
   "unresolved_questions": [
    "“笨功夫／这件事”究竟指什么领域或具体事项，正文未给出实例，需读者自行代入。",
    "如何判定“确确实实没有其他捷径可走”，本文未说明标准或检验方式（P019 只提出必要条件）。",
    "“绝顶聪明”“绝佳运气”如何识别，本文未说明。",
    "P020-P021 的“老天／上天”是修辞性拟人还是作者的实质主张，语气上无法完全确定。",
    "P028“笨人比聪明，聪明人比笨”的主语与比较方式有歧义，作为格言可作多种读法。",
    "文中以“ta／ta们”代称，为作者原文用字，非笔误。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "别傻了，那些功夫只是看起来很笨，其实去做它们是最聪明的做法。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "聪明在ta们发现了一些绝对没有第二捷径可言，绝对绕不过去的苦路。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "哪怕拿着无限的资本做后盾，也绝对没有可能在你不松懈的前提下超到你前面去。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "没有任何办法能投机取巧，没有任何办法能绕道", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P014", "quote": "却和你同样笨、会选这件吃力不讨好、要抱定必死的觉悟、耗费巨大的心血去把墙磨穿的人，", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P016", "quote": "ta与你唯一的差距，就是ta们没你这么笨", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P017", "quote": "所以，你才比较大的希望会赢。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P018", "quote": "是需要绝顶聪明、绝佳运气才有机会才有机会触摸得到的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "不是绝顶聪明外加极端努力，你怎么知道这件事确确实实没有其他捷径可走？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P021", "quote": "上天给聪明人们安排了这样一种“不做笨事就别想赢”的天然禁制令，真的是对人类一种极大的仁慈。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P024", "quote": "这就是为什么真正的聪明人，心心念念都在梦想那件真正命定属于自己的笨事。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "这种绝妙的笨事，是聪明人可以心安之处。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "那些石墙，注定要靠这种极聪明的笨人才有可能凿穿。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["个人成长与自我管理", "职业发展与择业策略", "成功学／励志话语"],
   "issue_candidates": ["聪明与笨功夫的关系", "先发优势与竞争壁垒", "机会成本与专注投入", "如何判断某条路没有捷径"],
   "text_function_candidates": ["答疑", "励志训诫", "比喻性论说"],
   "object_candidates": ["聪明人（泛称群体）", "笨小孩（修辞性称呼）", "未点名"],
   "working_keywords": ["笨功夫", "笨事", "绝妙笨功夫", "捷径", "苦路", "玄武岩层", "水滴石穿", "天然禁制令", "机会成本", "心安之处", "死所"]
  },
  "notes": "正文为无小标题的连续短段（29段），lexical 仅报告 paragraph 节点，无列表/引用块/图片，divergence=false。正文中 P027 与 P028、P028 与 P029 之间各有一小段字符间隙（868-870、882-884），疑为原文空行，未作引用。全文无具体事实性外部断言需外部核查；无图片，无需图像核验。"
 },
 "911abc81": {
  "analysis": {
   "question_context": "提问者问“法律的本质是什么？”（Q001，属提问者）。作者先以石头、沙子、马三个类比指出成分／来源／分类都不等于本质（P002-P011），再以圆为例说明人造理式才有本质（P012-P014），提出“谁创造，谁定义；谁定义，谁断言本质”的权柄原则（P016-P018），最后把该原则用于法律：法律是人类造就但无人真正定义过的“大杂烩”，故该问题只有猜测、没有真正答案（P029-P055）。正文无小标题，含一处寓言式比喻段群，图片节点 0。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"], "summary": "以石头（碳酸钙）、沙子（崩解的石头残骸）、马（奇蹄目）连续类比反问：成分、来源、分类都不是本质。", "role": "example"},
    {"unit_id": "U002", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "承认可用特征组合给出唯一描述以有效区分对象，但追问这是否即本质，并以身份证式描述作归谬。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "对照例：圆的定义确实是圆的本质；由此提请读者注意问题所在。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017", "P018"], "summary": "提出原则：谈本质先要确认人类是否有谈论权柄；非人所造的自在之物无资格谈本质；谁创造谁定义、谁定义谁断言本质。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020"], "summary": "限定：这种权柄有边界，也有交叉。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023"], "summary": "应用：石头非人所造故人类位格不足；石垒房屋只有不完全立场；理式完全出自人类构造时构造者有完全权柄。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "例证：弗洛伊德断言力比多、马蒂斯断言野兽派、自定义公式即“张王氏曲线”；概括为创造性贡献多少即占多少“话事权”。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P029", "P030"], "summary": "转折到主题：法律这一事物人类到底“持股”多少？人类的法律真是人类决定的吗？", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036", "P037"], "summary": "先设最理想情形（思想家—思想体系—价值观—法律体系），再指出价值观须受“行得通”“有可持续性”的实践斧正而不断改动。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P038", "P039"], "summary": "结论：法律是无数动机、利益、环境、问题不同者沿历史路径依赖掺和成的“七嘴八舌大杂烩”，谁也没有真正拥有理论上的定义权。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P040", "P041"], "summary": "法律研究为大杂烩寻找共性，总有一成装不进框架又无法割舍；法学家期待其为将自动脱落的“赘物”，现实却常是“赘物／胎盘”长成本体。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050"], "summary": "抄写员与拿皮鞭大块头的寓言：随便写→挨打→再写→再挨打→无限循环→最终写成勉强挨得住的“轻伤版”。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P051", "P052", "P053"], "summary": "反问：这本东西到底是你的作品还是那大块头的作品？谁真的手握它的“本质”？", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P054", "P055"], "summary": "收束结论：非你所造即无资格谈其本质，谈亦只是幻觉；该问题只有猜测、不会有真正的答案。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "指出石头的成分、沙子的来源、马的分类，都不是它们的本质。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "以抓取特征组合给出独一无二的描述可以有效地把对象与非它之物区分开，但作者追问这是否就是本质。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若特征描述即可称本质，则人的本质将可被表述为“持有编号为xxxxx的身份证的x国公民”（作者以此归谬）。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "圆的本质是“平面上到同一点距离相等的点的集合”，这的确确是圆的本质。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要谈论一件事物的本质，首先要确认人类是否对它拥有谈论的权柄。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切非人所造的自在之物，人类都没有资格谈论它们的“本质”。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原则是“谁创造，谁定义。谁定义，谁断言本质”。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种谈论本质的权柄既是有边界的，也是有交叉的。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "石头非人创造，故人类没有足够位格谈论其本质；对垒成房屋中人类注入创造力的部分有谈论立场但不完全；理式完全来自人类构造时构造者有完全权柄断言其本质。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "概念构造者对其构造的概念拥有绝对权柄，他人无法否定其定义（力比多、野兽派、自定义公式）。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "概括原则：对一个事物的创造性贡献有多少，人类就占有多少“话事权”。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：法律这一事物人类到底“持股”多少、人类的法律是否真的由人类决定。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "理想状态下建立的价值观须随时随地接受“行得通”“有可持续性”的实践斧正，最终重要的只有“行不行得通”，于是不断改掉又改回。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "法律实际上是被现实驱赶着掺和成的“七嘴八舌大杂烩”，沿历史路径依赖形成。", "evidence": ["E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "谁也没有真正拥有过那个理论上的定义权。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "法律研究试图为这团大杂烩总结共性，但即使做到极致仍有一成无法纳入框架又无法割舍；法学家期待它是将自动脱落的“赘物”，现实却常是“赘物／胎盘”反而长成本体。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以抄写员寓言说明：法律文本是在反复被鞭打驱赶的循环中写成的、勉强挨得住的“轻伤版”。", "evidence": ["E30", "E31"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问该产物究竟属于抄写员还是大块头，谁才真正手握着它的“本质”。", "evidence": ["E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是你所造的，你就没有资格谈论它的本质，谈了也无意义，再美妙的理论也只是幻觉。", "evidence": ["E33"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "因此“法律的本质是什么”这个问题其实只有猜测，并不会有真正的答案。", "evidence": ["E34"]}
   ],
   "argument_steps": [
    "以石头／沙子／马三例连续反问，指出成分、来源、分类都答的是别的问题而非本质（P002-P007）",
    "承认我们能用特征组合给出独一无二的描述并有效区分对象，但追问这是否就是本质（P008-P009）",
    "归谬：若此即本质，人的本质就成了身份证式的描述（P010-P011）",
    "反面对照：圆的定义“平面上到同一点距离相等的点的集合”确实就是圆的本质（P012-P014），由此提请读者注意问题（P015）",
    "提出权柄原则：谈论本质须先确认人类是否有此权柄；一切非人所造的自在之物人类无资格谈论其本质（P016-P017）",
    "立原则并加限定：“谁创造，谁定义。谁定义，谁断言本质”，且权柄有边界也有交叉（P018-P020）",
    "分层应用：石头非人创造（P021）；石垒房屋仅对注入创造力部分有不完全立场（P022）；纯人造理式的构造者有完全权柄（P023）",
    "以弗洛伊德之力比多、马蒂斯之野兽派、自定义“张王氏曲线”为例证（P024-P027），概括为创造性贡献多少即占多少话事权（P028）",
    "转向主题：法律人类“持股”多少、是否真由人类决定（P029-P030）",
    "先给最理想情形：思想家—思想体系—价值观—法律体系（P031-P032）",
    "转折：人类接受不了“坚守价值观宁可迎接毁灭”，价值观须受“行得通”“有可持续性”的实践斧正，重要的只有行不行得通（P033-P037）",
    "结论：现实是历史路径依赖下的“七嘴八舌大杂烩”，谁也没有真正拥有理论上的定义权（P038-P039）",
    "进一步描述法律研究：为杂烩找共性却总有一成无法纳入又无法割舍，法学家期待赘物自动脱落（P040）",
    "现实反例：下一个世代反而“胎盘”长大、“赘物”才是本体（P041）",
    "以抄写员与拿皮鞭大块头的寓言呈现文本成形的实际过程（P042-P050）",
    "反问作品的归属与“本质”的持有者（P051-P053）",
    "终局结论：非你所造即无资格谈其本质，谈亦只是幻觉，该问题只有猜测而无真正答案（P054-P055）"
   ],
   "concept_usage": [
    {"term": "本质", "meaning": "与成分、来源、分类、识别性描述相区别的东西；只有对人所创造的理式才谈得上。", "evidence": "P003/P008/P014/P016", "ambiguity": "作者未给出本质的正向定义，主要靠排除法与“圆”的正面例证界定。"},
    {"term": "权柄／位格", "meaning": "谈论某物本质的资格；“位格”用于说明人类对自在之物的资格不足。", "evidence": "P016/P017/P021", "ambiguity": "“位格”带神学／哲学意味，文中未定义、未注明来源。"},
    {"term": "自在之物", "meaning": "非人所造之物。", "evidence": "P017", "ambiguity": "疑为哲学术语用法，作者未说明其思想来源。"},
    {"term": "创造／构造", "meaning": "决定权柄归属的依据：创造得越多，可断言本质的资格越完全。", "evidence": "P018/P022/P023/P028", "ambiguity": "未给出衡量“创造性贡献”的方法。"},
    {"term": "话事权／持股", "meaning": "以商业持股比喻人类对事物定义权的份额。", "evidence": "P028/P029", "ambiguity": "比喻性用词，未量化。"},
    {"term": "大杂烩", "meaning": "形容法律实际由无数不同动机与处境者掺和而成。", "evidence": "P038/P040", "ambiguity": "描述性比喻，未给出成分清单。"},
    {"term": "赘物／胎盘", "meaning": "理论框架装不进却又无法割舍的部分，及其日后反而长成本体。", "evidence": "P040/P041", "ambiguity": "二者在文中并置互换，指涉不完全固定。"},
    {"term": "轻伤版", "meaning": "在反复挨打后写成的、勉强可承受的法律文本。", "evidence": "P050", "ambiguity": "寓言内部用词，未与现实立法程序对应。"}
   ],
   "examples_and_targets": [
    "石头／大理石（碳酸钙＝成分）、沙子（崩解的石头残骸＝来源）、马（奇蹄目＝分类）：作者的类比例证（P002-P007）。",
    "命名特定品种山羊（角、皮毛、花色、骨骼、内脏解剖结构）：识别性描述的例子（P008）。",
    "持有编号xxxxx身份证的x国公民：归谬式例子（P010）。",
    "圆：人造理式拥有本质的正面例证（P012-P014）。",
    "石头垒成的房子：部分创造只带来不完全谈论立场的例子（P022）。",
    "弗洛伊德断言力比多（libido）、马蒂斯断言野兽派：概念构造者拥有绝对权柄的例子（P024-P026）。",
    "“张王氏曲线”：假设性自定义公式的例子（P027）。",
    "新朝伊始的伟大思想家与思想体系：理想模型的假设例（P032）。",
    "抄写员与拿皮鞭的大块头：解释法律文本如何成形的寓言式比喻（P043-P050）。",
    "被质疑对象（未点名）：把本质等同于特征描述或分类的通行看法（P008-P011）；认为法律由人类理性设计所决定的看法（P031-P039）。"
   ],
   "conditions": [
    "结论以前提“人类是否对所谈对象拥有谈论权柄”为条件（P016），权柄随创造性贡献的比例而定（P022/P028）。",
    "理想模型以“在某位伟大的思想家的指引之下”为假设（P032）。",
    "限定词：“甚至”“顶多”“即使做到极致”“常常”“基本上”等（P035/P040/P041）。",
    "区分对象两类：自在之物（如石头）与人类构造的理式（如圆、力比多）；法律被归入后者，但“持股”比例作者以提问保留（P029-P030）。",
    "最终断言限定为“这个问题”的答案不可得，条件是“不是你所造的”（P054-P055）。"
   ],
   "rhetoric_and_tone": "以连续的类比反问推进（P002/P004/P006/P009/P011/P015/P030）；使用经文式对偶句“谁创造，谁定义。谁定义，谁断言本质。”（P018）；第二人称“你”贯穿举例与寓言（P010/P027/P043-P053）；“话事权”“持股”“大杂烩”“赘物”“胎盘”等商业／生物比喻混用；末段以抄写员反复挨鞭子的黑色幽默寓言收束。整体语气冷峻、反讽，带宿命论色彩，并直接对读者发出“你们看出问题来了吗”式诘问。",
   "unresolved_questions": [
    "“位格”的确切含义与来源本文未说明，疑为特定神学／哲学术语，需外部核查。",
    "“自在之物”是否为某哲学传统的专门术语，本文未注明出处。",
    "作者称权柄“有边界”且“有交叉”，但未说明边界与交叉如何划定（P019-P020）。",
    "法律究竟在多大程度上属于“人类构造的理式”，作者以提问方式保留，未给出结论（P029-P030）。",
    "自定义概念的排他权边界（例如他人独立发现同一公式时如何）本文未讨论（P027）。",
    "“下一个世代里反而是这个‘胎盘’长大了，这些‘赘物’才是本体”（P041）为经验性概括，依据未给出，属待外部核查的事实性断言。",
    "抄写员与“大块头”在现实中分别对应谁，本文未明说。",
    "正文未提及任何具体国家、法典或法学家，讨论停留在一般层面。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "那么是碳酸钙吗？那是它的成分。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "一把崩解的石头残骸？那是它的来源。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "一种奇蹄目动物？那是它的分类。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "借以将它与非它之物有效的区分开来", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "但是，这是它的本质吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "那么你的本质大可以被表述为“一名持有编号为xxxxx的身份证的x国公民”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "平面上到同一点距离相等的点的集合。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "这却的的确确是圆的本质。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "要谈论一件事物的本质，首先要确认人类是否对它拥有谈论的权柄。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "一切非人所造的自在之物，人类都没有资格谈论它们的“本质”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "谁创造，谁定义。谁定义，谁断言本质。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "这种权柄是有边界的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "这种权柄也是有交叉的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "石头不是人创造的，于是人类没有足够的位格谈论它的本质。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "人类对房子的创造部分就存在谈论的立场——但这是不完全的。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P023", "quote": "但若某理式完全来自人类的构造，那么构造者就有完全的权柄去断言它的本质。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "他们就有绝对的权柄和立场去谈论libido、野兽派的本质，因为这概念真的就是他们构造的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "你就可以绝对的否定ta", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "换句话说，对一个事物的创造性贡献有多少，人类就占有多少“话事权”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "现在问题来了，法律这个事物，人类到底“持股”多少？", "relation": "context"},
    {"key": "E21", "paragraph_id": "P030", "quote": "人类的法律，真的是人类决定的吗？", "relation": "context"},
    {"key": "E22", "paragraph_id": "P035", "quote": "于是这个价值观随时随地都要接受“行得通”“有可持续性”的实践斧正", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "重要的只有“行不行得通”。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P037", "quote": "昨天行得通的，今天行不通了，改掉；明天它又行得通了，改回去。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "沿着历史路径依赖，掺和起来的七嘴八舌大杂烩。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P039", "quote": "谁也没有真正拥有过那个理论上的定义权。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P040", "quote": "也仍然会有一成装不进这个理论框架而又无法割舍的东西。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P040", "quote": "这是必然会随着未来的到来而自动脱落的赘物", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P041", "quote": "反而是这个“胎盘”长大了，这些“赘物”才是本体。", "relation": "contradicts"},
    {"key": "E30", "paragraph_id": "P049", "quote": "无限循环。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P050", "quote": "最后你终于写了一个自己好歹挨得住的“轻伤版”。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P053", "quote": "问题是它到底是你的作品，还是那大块头的作品？你们谁才真的手握着它的“本质”？", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P054", "quote": "不是你所造的，你就没有资格去谈论它的本质，谈了也无意义", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P055", "quote": "这就是为什么这个问题其实只有猜测、并不会有真正的答案的原因", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["哲学／本体论", "法理学与法律理论", "概念史与方法论"],
   "issue_candidates": ["本质与成分／来源／分类的区别", "谈论本质的资格（权柄）问题", "人为构造物与自在之物的区分", "法律的本质与定义权归属", "法律是理性设计还是历史演化产物"],
   "text_function_candidates": ["答疑", "思辨论说", "比喻与寓言式论证", "批评（对通行本质观的质疑）"],
   "object_candidates": ["弗洛伊德", "马蒂斯", "法学家（泛称群体）", "未点名的国家与法典"],
   "working_keywords": ["本质", "权柄", "位格", "自在之物", "理式", "话事权", "持股", "大杂烩", "赘物", "胎盘", "路径依赖", "力比多", "野兽派", "张王氏曲线"]
  },
  "notes": "正文 55 段，lexical 仅报告 paragraph 节点，无列表／引用块／图片，divergence=false。P042-P050 的抄写员挨鞭子段落为寓言式比喻，语气与前后不同但仍是作者行文，未见引用标记，未按外部引用处理。正文无具体国家、法典、人物事件或数据；P041 的经验性概括以及“位格”“自在之物”的术语来源属待外部核查项。全文无图片，无需图像核验。"
 },
 "2c4d7eec": {
  "analysis": {
   "question_context": "提问者问“怎样成为一个受欢迎的人？”（Q001，属提问者，本身不含立场）。作者给出单一答案“施恩不图报就可以了”（P001），以“人们怕亏本”为前提（P002），先反驳以“不超额索报”冒充施恩不图报的流行说法（P004-P008），再提出“人情债中性体／施恩不亏本也不占便宜者”的中间方案（P009-P019），最后界定真正的施恩不图报（P020-P026），并以“万人迷真的是好事么”反问收尾（P027）。正文含编号列表（P023-P025），图片节点 0。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出答案：施恩不图报就可以了，别的都是多余的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "人性前提：人们怕亏本，喜欢不让自己亏本的人，讨厌让自己亏本的人。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "反面理由：施恩为图报则人家不敢受，受100总有一天要还101。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "反驳“索报不超过100即施恩不图报”之说：该结构不对称（给与时自愿、索还时对方不可拒绝），故所谓“0收益救济”其实有收益。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "行动建议：把“不得拒绝”改为“可自由决定押后”，即可在无实际亏损下更受欢迎，因为对方所还给的才是对等物。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "限定与补足：此点交往完全中性，但对方推迟n次会损失n-1次询问成本；补上“至少支付本次询问成本”条款即可扯平。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "结论：你成为“人情债中性体／施恩不亏本也不占便宜者”，比遵从涌泉相报者与“以施恩不图报名义暗赚必然性者”更受欢迎，已赢过九成九的人。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019"], "summary": "反问读者能否做到量力而为并允许被推迟；指出严格契约意义上只要对方最后还了就没吃亏；做得到就会受欢迎。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "递进界定：骑在中性线上仍不算施恩不图报；真正的施恩不图报须满足三项条件之一（未记下对方名字／未让对方知道自己名字／忘记曾帮过什么）。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P026", "P027"], "summary": "结论与反问收尾：养成此习惯必受欢迎、胜过99.99%的人即“万人迷”；但万人迷真的是好事么？", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要成为受欢迎的人，施恩不图报就可以了，别的都是多余的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "归根到底人们怕亏本：喜欢不让自己亏本的人，讨厌让自己亏本的人。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "施恩为图报时人家不敢受，因为受了你100，总有一天要还101。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的说法（“有的人说”）：不需要你还101，只要记得欠我的情，不会让你还到100，并称此为施恩不图报。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者判定上述说法是假的，因为这个实际上不对称。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不对称在于：给与时乙有选择权、在自己方便且能接受的前提下才给；而乙索还时甲多出一项不可拒绝的强制性义务，不能要求延期或更换种类。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者转述文化惯例：很多文化主张“滴水之恩当涌泉相报”，淡定些的也认为至少要按银行活期存款利率算利息。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被算作“施恩不图报”的“0收益救济”事实上是有收益的：收获“不可拒绝的义务”，把闲置的100变成黄金时刻高可得性、带活期利息的100。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若把“索报不得拒绝”改为“对方可自由决定押后”，就能在毫无实际亏损的情况下成为更受欢迎的人。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这样对方给的才是你当初给对方的对等物——一次对方有请求而自己确实觉得方便才给的帮助。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "到这一步双方交往完全中性；若对方真实守约则理论上没有吃亏，但实际仍有损失：对方推迟n次履约会损失n-1次询问成本。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要在互助协议中补充“如果甲方决定推迟回报，则至少要支付本次询问成本”，就能完全扯平、回归中性。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样做仍比遵从“滴水之恩涌泉相报＋不提出超额要求”原则者受欢迎，因为不会让对方欠下更大的人情债；作者自称其为“人情债中性体”“施恩不亏本也不占便宜者”。", "evidence": ["E16", "E17"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "严格执行“中性原则”的人已经赢过九成九的人，且只需允许别人在被索报时自由推迟，问一声的时间成本十几秒钟基本可忽略。", "evidence": ["E18", "E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在严格的契约意义上，只要对方最后一次还了，你就真的没有吃亏。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若做得到，你就会受欢迎——超过九成九的人。", "evidence": ["E21"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "骑在中性线的围墙上，你仍然不是一个“施恩不图报的人”，还要再往前迈一步才算进入“施恩多少算是不图报”的领域。", "evidence": ["E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的“施恩不图报”满足下列任意条件之一：一开始就没记下对方的名字、没给自己留下追讨凭证；一开始就没让对方知道自己的名字、没留下有效义务；忘记了自己曾帮过别人什么。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "养成这个习惯你必受欢迎，胜过99.99%的人，此即所谓万人迷。", "evidence": ["E26"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "结尾以反问保留：万人迷真的是好事么？", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "直接给出答案：施恩不图报就可以了，别的都是多余的（P001）",
    "给出人性前提：人们怕亏本，喜欢不让自己亏本的人（P002）",
    "反面说明：施恩为图报则人家不敢受，受100要还101（P003）",
    "引出流行说法：“不超过100的索报”被称作施恩不图报（P004），作者判其为假（P004）",
    "论证不对称：给与时乙有选择权且在自己方便前提下才给；索还时甲多出不可拒绝的强制义务（P005），且文化规范要求涌泉相报或计息（P006）",
    "结论一：所谓“0收益救济”其实有收益，是把闲置100变成黄金时刻高可得性、带活期利息的100（P007-P008）",
    "给出替代方案：把“不得拒绝”改成“可自由押后”（P009），使对方所还给的成为对等物（P010）",
    "自我限定并补足：此点交往中性，但推迟n次仍损失n-1次询问成本（P011），补上“支付本次询问成本”条款即扯平（P012）",
    "结论二：你成为“人情债中性体／施恩不亏本也不占便宜者”，胜过涌泉相报者与“暗赚必然性者”（P013-P015）",
    "强化论证：严格执行中性原则者已赢过九成九的人，成本仅十几秒询问时间（P016）",
    "反问读者能否做到，并说明严格契约意义上只要最后还了就没吃亏（P017-P018）",
    "条件式结论：做得到就会受欢迎，超过九成九的人（P019）",
    "抬高标准：骑在中性线上仍不算施恩不图报，须再迈一步（P020）",
    "给出真正施恩不图报的三项择一条件（P021-P025）",
    "结论三：养成此习惯必受欢迎、胜过99.99%的人，即万人迷（P026）",
    "以反问收尾，对“万人迷”本身是否好事存疑（P027）"
   ],
   "concept_usage": [
    {"term": "施恩不图报", "meaning": "被作者严格化：不留任何追讨凭证与义务的给予；文中区分“名义上的施恩不图报（实为暗赚必然性）”与“真正的施恩不图报”。", "evidence": "P001/P004/P013/P021", "ambiguity": "同一词语在文中先后指称被反驳的流行说法与作者的标准用法，含义随段落变化。"},
    {"term": "亏本", "meaning": "人际互助中的收支判断基准，按人情债的得失衡量。", "evidence": "P002/P007/P013", "ambiguity": "“本”的具体内容（时间、金钱、人情）未统一界定。"},
    {"term": "中性／人情债中性体", "meaning": "互助不使任何一方净欠人情债的状态与处于该状态的人。", "evidence": "P011/P012/P013", "ambiguity": "作者自造的标签，未给出形式化定义。"},
    {"term": "不对称", "meaning": "给与时自愿可选择、索还时对方不可拒绝的结构差异。", "evidence": "P004/P005/P006", "ambiguity": "未讨论关系亲疏或金额大小对该不对称的影响。"},
    {"term": "不可拒绝的义务", "meaning": "被作者视为“0收益救济”实际获得的收益。", "evidence": "P005/P007", "ambiguity": "此义务在法律与社交层面各有多大强制力，文中未区分。"},
    {"term": "询问成本", "meaning": "索报时耗去的时间成本，作者估为十几秒钟。", "evidence": "P011/P012/P016", "ambiguity": "仅为估计值，未说明适用场景。"},
    {"term": "万人迷", "meaning": "受欢迎程度的极端（胜过99.99%的人）。", "evidence": "P026/P027", "ambiguity": "作者随即反问其是否为好事，立场未明示。"},
    {"term": "滴水之恩当涌泉相报", "meaning": "被引作文化规范并充当比较基准。", "evidence": "P006/P013", "ambiguity": "作者称“很多文化都主张”，未指明具体文化。"}
   ],
   "examples_and_targets": [
    "某甲向某乙请求100、某乙索还100：贯穿全文的假设性例子（P005-P007）。",
    "“滴水之恩当涌泉相报”与“按银行活期存款利率算利息”：被作者引用的文化规范／社会惯例（P006）。",
    "“闲置的100”变成“在黄金时刻有高可得性的、带活期利息的100”：作者的比喻式说明（P007）。",
    "反驳对象：“有的人”所称的施恩不图报（索报不超过100即为不图报），作者判其为假（P004）。",
    "比较对象：遵从“滴水之恩涌泉相报＋我不会提出超额要求”者（P013）、“以施恩不图报名义暗赚必然性者”（P015）。",
    "修辞性量化：“赢过了九成九的人”“胜过99.99%的人”，未给出数据来源（P016/P026）。"
   ],
   "conditions": [
    "以对方真实守约为条件（P011）；并以“在严格的契约意义上”作限定（P018）。",
    "补足条款的条件式表述：“如果甲方决定推迟回报，则至少要支付本次询问成本”（P012）。",
    "假设条件句：“如果你放弃掉……改成……你就能……”（P009）。",
    "只在“理论上”不吃亏，实际仍损失n-1次询问成本（P011）。",
    "以“做得到”为前提得出受欢迎结论（P019）；“骑在这根中性线的围墙上”仍不算施恩不图报（P020）。",
    "真正施恩不图报的三项择一条件（P022-P025），未要求同时满足。",
    "成本量级限定：“时间成本不过十几秒钟，其实基本可以忽略”（P016）。"
   ],
   "rhetoric_and_tone": "第二人称“你”的劝导与训诫口吻，兼用契约与交易分析语汇（“协议”“条款”“成本”“中性”）；连续反问与追问推进（P008“你其实赚了，看到没有？”、P014“看清楚没有？”、P017“摸摸你的心……你能不能做到”、P019、P027）；比喻混用（“魔咒”“人情债中性体”“中性线的围墙”）；以“九成九”“99.99%”作夸张量化；结构上先给答案、再反驳常见替代方案、随后层层加码抬高标准，末尾以反问留悬念。整体语气自信、断言性强。",
   "unresolved_questions": [
    "“九成九”“99.99%”的受欢迎比例依据何在，本文未说明，属待外部核查的量化断言。",
    "“时间成本不过十几秒钟”为作者估计，未说明适用场景与对象关系（P016）。",
    "三项“真正施恩不图报”条件虽称“满足任意条件之一”，但三者效果是否等价、可否组合，文中未展开（P022-P025）。",
    "结尾“万人迷真的是好事么？”未给出答案，作者对此的立场在本文中未明示（P027）。",
    "“很多文化都主张‘滴水之恩当涌泉相报’”未指明具体是哪些文化，属待外部核查（P006）。",
    "若对方始终不履约（而非仅仅推迟），中性方案如何处理，本文未说明。",
    "适用关系类型（亲友、同事、陌生人）与长期关系中的边界，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "施恩不图报就可以了，别的都是多余的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "追根到底，人们是怕亏本，喜欢不让自己亏本的人，讨厌让自己亏本的人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "施恩为图报，那么人家就不敢受，因为受了你100，总有一天要还101。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "有的人说“不需要你还101，只要你记得欠我的情，我肯定不会让你还到100，肯定在100以下”，称这个为施恩不图报", "relation": "context"},
    {"key": "E5", "paragraph_id": "P004", "quote": "但这是假的，因为这个实际上不对称。", "relation": "contradicts"},
    {"key": "E6", "paragraph_id": "P005", "quote": "甲就额外多出了一项强制性的义务——甲不能拒绝。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "甲不能要求延期，不能要求更换请求种类", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "很多文化都主张“滴水之恩当涌泉相报”", "relation": "context"},
    {"key": "E9", "paragraph_id": "P007", "quote": "被算为“施恩不图报”的“0收益救济”，事实上是有收益的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "你将一份“闲置的100”，变成了“在黄金时刻有高可得性的、带活期利息的100”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "在毫无实际亏损的情况下成为一个更受欢迎的人。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "因为这样对方给你的才在本质意义上是你当初给对方的对等物", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "假如对方真实的守约，理论上你事实上没有吃亏", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P011", "quote": "对方如果推迟n次才履约，那么你会损失n-1次询问成本。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P012", "quote": "则至少要支付本次询问成本”，那就完全扯平了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "你是一个“人情债中性体”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P013", "quote": "而是一个“施恩不亏本也不占便宜者”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "已经赢过了九成九的人了", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "问一声的时间成本不过十几秒钟，其实基本可以忽略", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P018", "quote": "在严格的契约意义上，只要对方最后一次还了，你就真的没有吃亏。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "做得到，你就会受欢迎——超过九成九的人。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "骑在这根中性线的围墙上，你仍然不是一个“施恩不图报的人”。", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P022", "quote": "满足下面任意条件之一：", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "一开始就没有记下对方的名字，没有给自己留下任何追讨的凭证和线索。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "一开始就没让对方知道自己的名字，没有给对方留下任何有效的义务。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P026", "quote": "养成这个习惯，你必受欢迎，胜过99.99%的人，此即所谓万人迷。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P027", "quote": "剩下的问题是——万人迷真的是好事么？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往与社会心理", "人情／互惠规范", "行为策略与博弈式分析"],
   "issue_candidates": ["施恩与图报的边界", "人情债与互惠不对称", "受欢迎的条件", "中性互惠原则的设计", "量化断言（九成九／99.99%）的依据"],
   "text_function_candidates": ["答疑", "行动建议", "批评（对伪施恩不图报的拆解）", "劝说"],
   "object_candidates": ["某甲／某乙（假想人物）", "“有的人”（未具名的说法持有者）", "万人迷（泛称）"],
   "working_keywords": ["施恩不图报", "人情债", "亏本", "不对称", "不可拒绝的义务", "询问成本", "人情债中性体", "中性原则", "滴水之恩当涌泉相报", "万人迷"]
  },
  "notes": "正文 27 段，含一处编号列表（P023-P025，lexical 仍按 paragraph 计入），无引用块／图片，divergence=false。P004 的“有的人说”为作者引述并随即反驳的说法，已按 opponent_view 归属，未算作作者主张；P006 的“很多文化都主张”为作者转述的文化惯例。文中的比例数字（九成九、99.99%）与“十几秒钟”为作者修辞性量化与估计，无来源，列入待外部核查。全文无图片，无需图像核验。"
 },
 "8806ec71": {
  "analysis": {
   "question_context": "提问者（Q001）问 2020 年 7 月 12 日贵州安顺大巴车坠湖事件通报——司机因对拆迁不满蓄意报复社会——还有哪些新的信息量；事件信息属提问者提供。作者未补充案情，而是以“上了膛的枪、只带保险”为比喻，把该事件解释为价值观崩溃的结果（P004-P007），随后反驳“加强管理”式应对（P008-P011），主张真正的要害是“把火药取出来”（P012-P014）。正文极短（407 字，14 段），无小标题，图片节点 0。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "自述已写过“活死人问题”，以此设定本文语境。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "两个独立问句：如何看待南昌红谷滩实习女律师当街遇害一案、如何评价电影《祈祷落幕时》。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "核心比喻与判断：以“追求自身福利最大化”为人生价值观者是天生的上了膛的枪、只是带着保险；保险何时失效即何时击发；最大的运气只是击发得够晚而火药受潮。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "应用于本案：该公交车驾驶员的保险被磕碰失效而火药未受潮，于是枪响，有人中了价值观崩溃的流弹。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "反驳“加强管理”：这等于对十几亿支枪加强检查维护，即使不谈成本，从数量级看也避免不了此起彼伏的走火；何况路况颠簸、无从预知下一次走火。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "结论主张：真正的要害是把火药取出来，这是唯一办法；别的办法只是做努力状换取“我已经尽力了，责任不在我”的心安理得。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“追求自身福利最大化”作为人生价值观的人，天生是一把上了膛的枪，只是带着保险而已。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "保险什么时候失效，就会什么时候击发。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "最大的运气只不过是击发得足够晚，火药可能已经受潮失效。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把该公交车驾驶员解释为：保险被磕碰失效而火药还没受潮，于是人们听到枪响，有人中了价值观崩溃的流弹。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的主张（“有人说”）：我们要加强管理。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "加强管理等于加强对这十几亿支枪的检查和维护；即使不谈成本，仅从数量级看也避免不了此起彼伏的走火。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "现在这段路颠簸崎岖，不知正有多少保险在车厢里翻滚，也无从知道下一次是哪一把的什么部位落在水泥地上。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的要害是要把火药取出来，这是唯一办法。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别的办法都只不过是做努力状，赚一个“我已经尽力了，责任不在我”的心安理得而已。", "evidence": ["E11"]}
   ],
   "argument_steps": [
    "自述已写过“活死人问题”，并以两处关联问句（南昌红谷滩案、《祈祷落幕时》）设定语境（P001-P003）",
    "提出核心比喻与判断：以“追求自身福利最大化”为人生价值观者是天生的上了膛的枪、只带保险（P004）",
    "说明机制：保险何时失效即何时击发（P005）；最大运气只是击发够晚而火药受潮（P006）",
    "应用于本次事件：驾驶员保险被磕碰失效而火药未受潮，于是枪响，有人中价值观崩溃的流弹（P007）",
    "引出被反驳的主张：“有人说我们要加强管理”（P008）",
    "反驳：这等于对十几亿支枪加强检查维护，即使不谈成本，从数量级看也避免不了此起彼伏的走火（P009）",
    "补充现实条件：路况颠簸、不知多少保险在车厢里翻滚，亦无法预知下一次走火（P010-P011）",
    "给出结论：真正的要害是把火药取出来，这是唯一办法（P012-P013）",
    "贬斥替代方案：别的办法只是做努力状以换取“我已经尽力了，责任不在我”的心安理得（P014）"
   ],
   "concept_usage": [
    {"term": "活死人问题", "meaning": "作者自称已写过的论题，本文未作界定，仅作为语境引用。", "evidence": "P001", "ambiguity": "内容需回查作者其他文章，本文不提供定义。"},
    {"term": "上了膛的枪／保险／火药", "meaning": "比喻把“追求自身福利最大化”当作人生价值观的人及其失控条件：保险指约束机制，火药指内在驱动。", "evidence": "P004/P005/P006/P009", "ambiguity": "比喻各要素未逐一定义，与制度、心理、教育的对应关系不明确。"},
    {"term": "走火／流弹", "meaning": "比喻约束失效后造成的伤害及其波及他人。", "evidence": "P007/P009", "ambiguity": "“流弹”所指受害者与加害关系在文中未展开。"},
    {"term": "把火药取出来", "meaning": "比喻消除价值观层面的内在驱动，作者称之为唯一办法。", "evidence": "P012", "ambiguity": "具体手段、主体与代价本文均未说明。"},
    {"term": "价值观崩溃", "meaning": "描述肇事者的心理状态。", "evidence": "P007", "ambiguity": "未给出判定标准或心理学依据。"},
    {"term": "做努力状", "meaning": "形容替代性应对只是表演努力。", "evidence": "P014", "ambiguity": "口语化贬义表述，未指明具体政策或行为。"}
   ],
   "examples_and_targets": [
    "贵州安顺大巴车坠湖事件及其通报：仅见于 question 字段（属提问者），正文只称“这位公交车驾驶员”，未复述案情（Q001/P007）。",
    "南昌红谷滩实习女律师当街遇害案、电影《祈祷落幕时》：正文中以问句形式出现的两条关联话题（P002-P003）。",
    "“有人说我们要加强管理”：作者引出并反驳的主张（P008）。",
    "“十几亿支枪”“车厢”“水泥地”：规模修辞与比喻材料（P009-P011）。",
    "反驳对象（未点名）：主张以加强管理、检查维护来预防此类事件的观点（P008-P009）。"
   ],
   "conditions": [
    "比喻的限定对象是“把‘追求自身福利最大化’作为人生价值观的人”（P004）。",
    "以“可能”限定火药受潮（P006）；以“不知正有多少”“你也不知道”表达不确定性（P010-P011）。",
    "反驳的前提是“即使先不谈成本问题，仅仅从这数量级来看”（P009）。",
    "排他性断言：“这是唯一办法”（P013）。",
    "“把火药取出来”的实施主体、手段、可行性与代价，本文未说明。",
    "适用人群规模、时间范围与制度条件，本文未说明。"
   ],
   "rhetoric_and_tone": "冷峻的比喻式论断，全篇以“枪—保险—火药—走火—流弹”一以贯之；用第二人称“你”直接指向读者（P011）；以“十几亿支枪”作规模夸张（P009）；末段“做努力状赚一个‘我已经尽力了，责任不在我’的心安理得”带明显讽刺与训诫意味。对事件本身几乎不作叙述，语气克制而决绝；结构为比喻立论→否定主流应对→给出唯一解法。",
   "unresolved_questions": [
    "“活死人问题”的具体内容本文未定义，需回查作者其他文章（P001）。",
    "正文未出现安顺、大巴、坠湖、拆迁等字样；事件信息仅来自 question 字段（属提问者），本文未复述亦未核实。",
    "“把火药取出来”具体指什么（教育、价值重建、制度改造或其他），本文未说明。",
    "“这是唯一办法”的排他性依据，本文未给出。",
    "P002-P003 两条问句是正文论述的一部分，还是指向作者其他回答／外部链接，lexical 未报告链接节点，无法确定。",
    "P010“现在这段路颠簸崎岖”是比喻还是对现实形势的描述，存在歧义。",
    "事件通报内容（司机因对拆迁不满蓄意报复社会）的事实准确性需外部核查，本文未提供依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "把“追求自身福利最大化”作为人生价值观的人，天生是一把上了膛的枪，只是带着保险而已。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "保险什么时候失效，就会什么时候击发。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "最大的运气只不过是击发得足够晚的话，火药可能已经受潮失效了罢了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "这位公交车驾驶员的保险被磕碰失效了，而他的火药还没受潮，于是人们听到了枪响，有人中了价值观崩溃的流弹。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "有人说我们要加强管理。", "relation": "context"},
    {"key": "E6", "paragraph_id": "P009", "quote": "也避免不了此起彼伏的走火声。", "relation": "contradicts"},
    {"key": "E7", "paragraph_id": "P010", "quote": "尤其是现在这段路颠簸崎岖，不知正有多少保险正在车厢里翻滚。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "你也不知道下一次是哪一把的什么部位落在水泥地上。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "真正的要害，是要把火药取出来。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "这是唯一办法。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "别的办法都只不过是做努力状赚一个“我已经尽力了，责任不在我”的心安理得而已。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会事件评论", "价值伦理与人生价值观", "公共安全与社会治理"],
   "issue_candidates": ["报复社会型暴力事件的成因解释", "以“福利最大化”为人生价值观的后果", "加强管理／安检能否预防此类事件", "价值观层面的干预是否可行"],
   "text_function_candidates": ["评论", "批评（针对主流应对主张）", "比喻式论说"],
   "object_candidates": ["公交车驾驶员（未具名）", "贵州安顺大巴车坠湖事件（仅见提问字段）", "南昌红谷滩实习女律师遇害案（正文提及）", "电影《祈祷落幕时》（正文提及）", "“有人说”的加强管理主张者（未具名）"],
   "working_keywords": ["活死人问题", "上了膛的枪", "保险", "火药", "走火", "流弹", "价值观崩溃", "追求自身福利最大化", "加强管理", "十几亿支枪", "把火药取出来", "做努力状"]
  },
  "notes": "正文仅 407 字 14 段，无标题、列表、引用块与图片，lexical 仅报告 paragraph 节点，divergence=false。P002-P003 为两条独立问句，疑为作者关联回答的链接／标题（lexical 未报告链接节点，无法确认），本文按正文段落处理，并已在 unresolved_questions 标注该不确定性。事件细节（安顺大巴车坠湖、司机因对拆迁不满蓄意报复社会）仅见于 question 字段、属提问者提供，正文未复述，其事实性需外部核查。“有人说我们要加强管理”为作者引述并反驳的主张，已按 opponent_view 归属。全文无图片，无需图像核验。"
 },
 "c95a0865": {
  "analysis": {
   "question_context": "提问者（Q001）说“感觉中国程序员前景一片灰暗，是这样吗？”，该判断属提问者。作者明确不认同（P002“还灰暗……”），以“中美脱钩让出巨大市场”为总判断（P001-P003），随后列出可做替代的软件细分市场（P005-P013）、逐条反驳五类质疑（P015-P029、P058-P061），并引述“2025中国制造”的十大领域基本目标清单作为需求侧依据（P030-P052），最后把问题从行业前景转向个人是否有本事（P053-P062）。正文含三处 lexical 未覆盖的疑似链接／标题片段（P008、P014、P063），divergence=true。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以反问反驳提问者前提：中美脱钩让出的市场极大，“抢钱冲锋号都吹响了”，只看有没有本事。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009", "P010"], "summary": "列举被让出的市场细分：科学计算、图形图像、CAD/CAE/CAPP/CAM、数字内容等，并称数不胜数。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013"], "summary": "机会判断与建议：非开源的行业霸主均可做替代品；威慑压价与服务器境内安全即可带来采购；有此打算者应优先动手。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "反驳质疑一（用户少不赚钱）：以达索为开发幻影战斗机自研CATIA，及其成本与产量数据为例。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021"], "summary": "反驳质疑二（见效慢没人投）：反问华为5G搞了多少年。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "反驳质疑三（不是只有程序员能干的活）：连续反问物理学家等、各国企与互联网公司为何不能开软件公司。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029"], "summary": "反驳质疑四（中国市场养不起）：以Autodesk 1982年创始时的市场容量与2019年财务数据作反例。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052"], "summary": "引述“2025中国制造的基本目标”十大领域清单（每段带[10]标注），作为需求侧依据。", "role": "context"},
    {"unit_id": "U009", "paragraph_refs": ["P053", "P054", "P055", "P056", "P057"], "summary": "由清单推出：所需上下游供应商基本排除国外企业；反问中国程序员是否有前途，并转折到“前途是否轮得到你”。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P058", "P059", "P060", "P061", "P062"], "summary": "反驳质疑五（大部分程序员只会前端与数据库）：以“嗯，也许吧”让步，反问“前途”是否意味着无需额外努力，并以训诫式要求收尾。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的说法：感觉中国程序员前景一片灰暗，并询问是否如此。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问回应：中美脱钩让出的市场规模很大（“还灰暗……”即否定提问者判断）。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抢钱冲锋号都已吹响，能否抓住只取决于有没有本事。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所有行业细分市场的霸主，只要不是开源的，现在均可动手做替代品。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "仅仅为了威慑和压低美国报价，甚至仅仅因为服务器在国内没有突然中风的危险，都有机会得到采购。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "满足条件、有此打算者应优先动手，“迟早这些才是世界之王”。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的质疑一（“很多人在说”）：这种软件做了才几个用户，怎么能赚钱？", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以达索为幻影战斗机自研CATIA为例回应质疑一；并按现汇率给出制造成本约1.5亿人民币、造600架的数据（强调这是成本而非销售额）。", "evidence": ["E8", "E9"]},
    {"claim_id": "C009", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的质疑二（“有人说”）：大家都爱赚快钱，需要那么久才见效，没人会投。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问回应质疑二：华为的5G又搞了多少年？", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的质疑三（“又有人说”）：这不是只有程序员就能干的活。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问回应质疑三：程序员不必只在只有程序员的企业工作；物理学家、化学家、数学家可以开软件公司；中石化、中车、中船、沈飞、成飞、北方兵器工业集团、中科院、一汽、二汽等可以开软件公司；阿里、腾讯甚至百度并非只对互联网有兴趣。", "evidence": ["E13", "E14", "E15", "E16"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的质疑四：有人说中国市场养不起这些企业。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以Autodesk为反例：1982年创始时美国／世界软件市场容量有限；2019年Autodesk总资产47.9亿美元、利润7.33亿美元、雇员10000人。", "evidence": ["E18", "E19"]},
    {"claim_id": "C015", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "被引述的“2025中国制造的基本目标”清单：新一代信息技术、高档数控机床和机器人、航空航天装备、海洋工程装备及高技术船舶、先进轨道交通装备、节能与新能源汽车、电力装备、农机装备、新材料、生物医药及高性能医疗器械等十大领域，每段末尾带[10]标注。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "该清单所需的上下游技术供应商基本上把国外企业排除掉了——至少会对等地给中国企业留一个对等的名额。", "evidence": ["E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问推论：把清单里的“Autodesk”数目乘以10000，中国程序员并非没有前途，并追问“你还想多有前途”。", "evidence": ["E24", "E25"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "转折限定并反问：问题是这个前途轮不轮得到你？", "evidence": ["E26"]},
    {"claim_id": "C019", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的质疑五（“又有人说”）：现在的大部分程序员都干不了，因为只会搞搞前端和数据库、弄点web开发。", "evidence": ["E27"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者对该质疑作让步式回应：“嗯，也许吧。”", "evidence": ["E28"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问界定“前途”：是否指不用包含任何额外努力、像路边有人投币只需抱着桶接着那样的前途？", "evidence": ["E29"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若按上述理解，那你确实没前途，死心吧。", "evidence": ["E30"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行动要求：别再跟人起哄，去看书。", "evidence": ["E31"]}
   ],
   "argument_steps": [
    "以反问回击提问者前提：中美脱钩让出多大市场（P001），并直接否定“还灰暗”（P002）",
    "断言机会已来，取决于本事（P003）",
    "罗列被让出的市场细分：科学计算、图形图像、CAD/CAE/CAPP/CAM、数字内容等，并称数不胜数（P004-P010）",
    "判断：除开源外，各行业细分市场霸主均可做替代品（P011）",
    "给出采购动因：威慑并压低美国报价、服务器在境内的安全考虑（P012）",
    "建议有此打算者优先动手（P013）",
    "反驳质疑一（用户少不赚钱）：达索为幻影战斗机自研CATIA，其成本与产量数据（P015-P019）",
    "反驳质疑二（见效慢没人投）：反问华为5G搞了多少年（P020-P021）",
    "反驳质疑三（不是只有程序员能干的活）：连续反问物理学家等、各国企与互联网公司（P022-P026）",
    "反驳质疑四（中国市场养不起）：以Autodesk 1982年创始时的市场容量与2019年财务数据作反例（P027-P029）",
    "引述“2025中国制造”十大领域基本目标清单（P030-P052）",
    "由清单推出：上下游技术供应商基本排除国外企业，至少留对等名额（P053）",
    "反问式推论：Autodesk 乘以10000，中国程序员并非没有前途（P054-P056）",
    "转折限定：问题在于这个前途是否轮得到你（P057）",
    "引出质疑五（大部分程序员只会前端与web开发），以“嗯，也许吧”让步（P058-P059）",
    "以反问界定“前途”是否意味着无需额外努力，并作条件式结论“那你确实没前途”（P060-P061）",
    "以训诫式行动要求收尾：别起哄，去看书（P062）；末尾另有一段疑似链接标题片段（P063）"
   ],
   "concept_usage": [
    {"term": "中美脱钩", "meaning": "被视为让出巨大市场、产生替代机会的条件。", "evidence": "P001", "ambiguity": "未说明脱钩的范围、时间与程度。"},
    {"term": "替代品", "meaning": "对非开源行业霸主软件的国产替代。", "evidence": "P011", "ambiguity": "是否包含开源软件的商业化支持，未说明。"},
    {"term": "开源", "meaning": "作为可否动手做替代品的分界。", "evidence": "P011", "ambiguity": "为何开源即可不替代，理由未说明。"},
    {"term": "威慑和压低美国的报价", "meaning": "即使自身产品竞争力不足，也可因压价功能而获得采购。", "evidence": "P012", "ambiguity": "未说明该机制的实际发生条件。"},
    {"term": "服务器在国内没有突然中风的危险", "meaning": "以“中风”比喻境外服务被切断的风险，指境内数据与服务安全。", "evidence": "P012", "ambiguity": "比喻性表述，未对应具体政策或事件。"},
    {"term": "世界之王", "meaning": "对替代品企业前景的夸张说法。", "evidence": "P013", "ambiguity": "无具体衡量标准。"},
    {"term": "前途", "meaning": "在结尾被重新界定为是否“不用包含任何额外努力”的收益。", "evidence": "P060", "ambiguity": "作者以反问方式界定的含义未必等同于提问者的用法。"},
    {"term": "2025中国制造", "meaning": "被引述的目标清单名称，含十大领域。", "evidence": "P030", "ambiguity": "文件来源与版本未说明。"},
    {"term": "[10]", "meaning": "清单各段末尾的标注，疑为引文出处标记。", "evidence": "P032/P052", "ambiguity": "所指文献正文未说明，需外部核查。"}
   ],
   "examples_and_targets": [
    "软件产品与厂商清单：Mathematica（科学计算）、Adobe全家福（图形图像）、Autodesk全家福／SolidWorks／Mastercam／UG／SPICE／Saber／Ansys／ASAP（CAD/CAE/CAPP/CAM）、Unreal／Unity3D／Vay／Arnold／finalrender／redshift／Final Cut（数字内容）——作者列举的可替代对象（P005-P009）。",
    "达索为开发幻影战斗机自研CATIA；幻影战斗机成本约1.5亿人民币、造600架——作者回应质疑一的例证与数据（P016-P019）。",
    "华为5G——作者回应质疑二的反例（P021）。",
    "物理学家、化学家、数学家；中石化、中车、中船、沈飞、成飞、北方兵器工业集团、中科院、一汽、二汽；阿里、腾讯、百度——作者反问中列举的主体（P024-P026）。",
    "Autodesk：1982年创始；2019年总资产47.9亿美元、利润7.33亿美元、雇员10000人——作者回应质疑四的反例与数据（P028-P029）。",
    "“2025中国制造的基本目标”十大领域清单（P030-P052）——被引述的文本，每段带[10]标注，属 cited_source。",
    "被反驳的主张（以“有人说／很多人在说／又有人说”引出，均未点名）：用户少赚不到钱、见效慢没人投、不是只有程序员能干的活、中国市场养不起、大部分程序员干不了（P015/P020/P022/P027/P058）。",
    "疑似嵌入的链接或新闻标题片段：“工业软件，这才是中国制造业最大的短板！_EDA工具与IC设计-面包板社区”（P008）、“中国芯片产业前景到底怎么样？”（P014）、“国产工业软件迎来发展春天 上海加快打造产业发展沃土-新华网”（P063）——lexical 未覆盖，性质需核验。"
   ],
   "conditions": [
    "替代的前提是“只要不是开源的”（P011）。",
    "采购机会的条件：“仅仅为了威慑和压低美国的报价”“仅仅因为你的服务器在国内没有突然中风的危险”（P012）。",
    "清单结论以“基本上”“至少”限定（P053）。",
    "结论以个人本事为条件：“看你有没有本事而已”（P003）、“这个前途轮不轮得到你”（P057）。",
    "对“大部分程序员干不了”的让步：“嗯，也许吧”（P059）。",
    "条件式结论“那你确实没前途”（P061）以前述“无需额外努力的前途”理解为前提。",
    "未说明时间尺度、投资规模、政策落地程度与个人转型路径。",
    "引述清单每段带[10]标注，出处本文未说明。"
   ],
   "rhetoric_and_tone": "高度口语化，挑衅、反问与训诫并用；密集反问贯穿全篇（P001/P017/P018/P021/P023-P026/P028/P055-P057/P060）；使用“抢钱冲锋号”“世界之王”“死心吧”“废什么话”等夸张与命令式措辞；以“你们”直呼读者（P054/P055）；大量罗列产品名、公司名与政策条目形成铺陈与规模感；末段由论证转为督促（“还有时间在这跟人起哄，还不去看书？！”）。对提问者的“灰暗”判断持明显否定态度，但不作系统论证而主要依靠反问与清单铺陈。",
   "unresolved_questions": [
    "P008、P014、P063 三段经 lexical 判定为“未覆盖片段”（divergence=true），文本形态疑似嵌入的链接标题或新闻标题，其来源与是否属于作者正文需核验。",
    "清单各段末尾“[10]”所指文献，正文未说明，需外部核查。",
    "“2025中国制造”清单的发布主体与版本未说明，是否逐字引自某文件需外部核查。",
    "达索CATIA、幻影战斗机成本（约1.5亿人民币）与产量（600架）、Autodesk财务数据（总资产47.9亿美元、利润7.33亿美元、雇员10000人）均属待外部核查的事实性数据。",
    "“再乘以10000”为修辞性推估，无计算依据（P054）。",
    "“开源”作为可替代与否的分界，其理由本文未说明（P011）。",
    "若“大部分程序员只会搞前端和数据库”成立，技能缺口如何弥补，本文未说明。",
    "结尾“还不去看书”未说明应学习的具体方向。",
    "提问者的“前景一片灰暗”判断未被逐条讨论，作者主要以需求侧机会回应，供需两侧的对接问题（如采购是否真落到国产软件与个人）本文未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中美脱钩，你知道有多大的市场被让出来了吗？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "还灰暗……", "relation": "contradicts"},
    {"key": "E3", "paragraph_id": "P003", "quote": "抢钱冲锋号都吹响了，看你有没有本事而已。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "所有的行业细分市场的霸主，只要不是开源的，现在均可动手做替代品。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P012", "quote": "甚至仅仅因为你的服务器在国内没有突然中风的危险，都有机会得到采购。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "满足这个条件、有这个打算的优先动手，迟早这些才是世界之王", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "很多人在说“这种软件做了才几个用户，怎么能赚钱”？", "relation": "context"},
    {"key": "E8", "paragraph_id": "P016", "quote": "达索为了开发幻影战斗机，自己开发了CATIA。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "造了600架。这只是成本，这不是销售额。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "有人说“大家都爱赚快钱，需要那么久才会见效，没人会投的”。", "relation": "context"},
    {"key": "E11", "paragraph_id": "P021", "quote": "华为的5G又搞了多少年？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "又有人说，这不是只有程序员就能干的活。", "relation": "context"},
    {"key": "E13", "paragraph_id": "P023", "quote": "为什么程序员只能在只有程序员的企业里工作？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "谁说物理学家、化学家、数学家就不能开软件公司啊？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "谁说中石化、中车、中船、沈飞、成飞、北方兵器工业集团、中科院、一汽、二汽……不能开软件公司啊？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "谁说阿里、腾讯甚至百度【只对】互联网有兴趣？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "说中国市场养不起这些企业的人——", "relation": "context"},
    {"key": "E18", "paragraph_id": "P028", "quote": "Autodesk，1982年创始，1982年的美国/世界软件市场有多大的市场容量？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "2019年，Autodesk总资产47.9亿美元，利润7.33亿美元，雇员10000人。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "来，看看2025中国制造的基本目标：", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P034", "quote": "开发自主可控的高端工业平台软件和重点领域应用软件", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P052", "quote": "发展针对重大疾病的化学药、中药、生物技术药物新产品", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P053", "quote": "基本上把国外企业排除掉了——至少会对等的给中国企业留一个对等的名额。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P054", "quote": "你们数数看这里面有多少家“Autodesk”，再乘以10000。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P056", "quote": "你还想多有前途？", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P057", "quote": "问题是，这个前途轮不轮得到你？", "relation": "qualifies"},
    {"key": "E27", "paragraph_id": "P058", "quote": "因为ta们只会搞搞前端和数据库，弄点web开发。", "relation": "context"},
    {"key": "E28", "paragraph_id": "P059", "quote": "嗯，也许吧。", "relation": "qualifies"},
    {"key": "E29", "paragraph_id": "P060", "quote": "是不用包含任何额外努力的那种？", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P061", "quote": "那你确实没前途，死心吧。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P062", "quote": "废什么话？还有时间在这跟人起哄，还不去看书？！", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P008", "quote": "这才是中国制造业最大的短板", "relation": "context"},
    {"key": "E33", "paragraph_id": "P014", "quote": "中国芯片产业前景到底怎么样？", "relation": "context"},
    {"key": "E34", "paragraph_id": "P063", "quote": "国产工业软件迎来发展春天 上海加快打造产业发展沃土-新华网", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["软件产业与信息技术", "职业发展／就业前景", "产业政策与国产替代", "中美经贸关系"],
   "issue_candidates": ["中国程序员的前景", "中美脱钩让出的市场空间", "工业软件等细分市场的国产替代", "长期投入与快钱偏好", "政策清单对产业链的排除与留位效应"],
   "text_function_candidates": ["答疑", "论辩／反驳", "经验总结与建议", "训诫式督促", "政策文本引述"],
   "object_candidates": ["中国程序员", "美国（作为脱钩与技术来源方）", "达索（Dassault）", "Autodesk", "华为", "Adobe", "Mathematica", "中石化、中车、中船、沈飞、成飞、北方兵器工业集团、中科院、一汽、二汽", "阿里、腾讯、百度"],
   "working_keywords": ["中美脱钩", "市场被让出来", "替代品", "开源", "工业软件", "CAD", "CAE", "CAPP", "CAM", "2025中国制造", "Autodesk", "CATIA", "幻影战斗机", "5G", "web开发", "世界之王"]
  },
  "notes": "本篇 divergence=true：P008、P014、P063 为 lexical 未覆盖片段，文本形态疑似嵌入的链接标题或新闻标题（末尾字串为“_EDA工具与IC设计-面包板社区”“中国芯片产业前景到底怎么样？”“……-新华网”），其来源与是否属于作者正文无法由现有材料确定，已在 unresolved_questions 标注，未据此推断作者主张；evidence E32-E34 仅作结构异常的上文定位（relation=context），不支撑任何作者主张。P030-P052 的十大领域清单每段末尾均带“[10]”标注、文体与前后口语化行文明显不同，按被引述文本处理（claim_type=quoted_or_cited，attribution=cited_source），未归给作者；作者自己对清单的评论仅在 P053 之后。P015/P020/P022/P027/P058 以“有人说／很多人在说／又有人说”引出，均按 opponent_view 归属。文中数据（达索／幻影战斗机、Autodesk 财务、5G 年份）与[10]出处均属待外部核查。全文无图片，无需图像核验。"
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
