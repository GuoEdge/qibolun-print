# -*- coding: utf-8 -*-
"""批次 r001-b0012 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0012.sessions.py            # 写 out/r001-b0012.out.jsonl
  python3 records/r001-b0012.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0012"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0012.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "15ad7084": {
  "analysis": {
   "question_context": "提问者（Q001）问：现代驱逐舰上的主炮有什么用？作者给出的答案集中在两点：舰炮是驱逐舰自主任务之中最廉价的中远程打击武器，在性能可及的前提下是第一选择，且在射程之内无法有效防御；舰炮最主要的现实作用则是公海上的“耍流氓”（侮辱性抵近观察）。作者在文末（P035-P036）根据评论区提醒修正了开头的表述：把“完成所有任务的各种手段之中舰炮最便宜”改为追加前提的“驱逐舰自主任务之中，最具性价比的是舰炮”。提问属提问者；作者的回答限定了“自主任务”这一前提。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "修正后的总起判断：舰炮是驱逐舰自主任务中最廉价的中远程打击武器，性能可及前提下是第一选择；在其射程之内是决定性攻击力量、目前无法有效防御，因此事实上成为公海舰队隐性示威与骚扰战术的最有效工具（注明本段有修改，原因附文末）。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003"
     ],
     "summary": "说明导弹类武器的后勤负担：储弹量少、再装填要几小时甚至回港或专业补给舰，一旦使用在补充前严重影响制海权与战略能力；擅自动用会浪费军舰的战略价值；而对手明知你有防空反导系统，绝不会添油式试探，一定全力持续饱和攻击以求突防。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006",
      "P007",
      "P008"
     ],
     "summary": "描述两舰对决的基本策略：先以能全负荷工作的防空系统与干扰手段持续抵抗、力求尽可能久的完全防御以争取战或逃（盾）；再以巡航导弹、反舰导弹、舰炮等一切可用手段持续饱和攻击寻求突破（矛）；这是雷霆一击、胜负手；添油式发射等于浪费弹药和自杀。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P009",
      "P010",
      "P011",
      "P012",
      "P013",
      "P014",
      "P015"
     ],
     "summary": "说明导弹群协同战术：靠路线与航速规划编队集结、有前锋中锋游击，形成“狼群战术”，以超越近防炮扭矩极限与拦截导弹目标分配极限；导弹群协调战术是现代海战最大核心焦点；二十枚不应分两批放出，因为协同攻击可能第十六枚左右才找到机会，分批发射会辜负友舰付出血代价争取的发射阵位；由此可知除非决斗式任务，再装填困难的攻击手段都会被极力避免使用。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P016",
      "P017"
     ],
     "summary": "舰炮没有上述问题：炮弹几乎无限量、自动装弹机提高再装填速度，攻击力相当强大，除拉开距离降低命中率外对舰炮仍无可用防御手段、装甲基本无效；舰炮射程之内已无先进与落后之分，代差等于拉平。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020",
      "P021"
     ],
     "summary": "回答“为什么舰炮难以防御”：水冷系统使现代舰炮可一分钟四十发长时间射击且精准，密集阵与防空导弹系统都承受不了；若对方能放心大胆用舰炮攻击，说明你的防空力量已在前期导弹攻击中耗尽且对方确信自身安全。",
     "role": "reason"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P022",
      "P023",
      "P024",
      "P025",
      "P026",
      "P027"
     ],
     "summary": "说明舰炮射程对交战距离的约束：防空资源充沛时双方只敢隔一两百公里对峙，隐身舰可逼近到自己导弹射程内较近处，但绝不会接近到对方舰炮有效射程之内；舰炮射程内隐身可能性太小，还要考虑舰载预警机降低地球曲面遮蔽；新海战中双方在极限射程边等待增援，劣势方提前撤退；因此很难发生两舰舰炮互射，一旦发生被射击一方其实已经输了。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P028",
      "P029",
      "P030",
      "P031",
      "P032"
     ],
     "summary": "说明巨炮主义退出历史舞台的原因：靠惯性飞行增程不经济（阻力随速度平方乃至更高幂次增长、射程加倍需初速提高4-8倍、散布半径与射程平方成正比故火力密度要提高至少四倍以上），军舰只好变成巨舰而在现代海战中无异于找死；惯性飞行增程有极限，火炮极限射程在地球上只有一百公里上下（电磁炮也不例外），只有巨型履带平台有潜力超越；增程正道是火箭助推加末端制导，故导弹的合理性远高于巨炮；舰炮实际上是“豪猪刺”。",
     "role": "reason"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P033",
      "P034"
     ],
     "summary": "舰炮最主要的现实作用：用来“耍流氓”，即在公海上仗着对方不敢随便动手，用小破船公然接近到自己的舰炮射程之内，令对方吞不下又吐不出；这就是“侮辱性抵近观察”，其实也不见得会开炮，结果大家都吃不香睡不好。",
     "role": "claim"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P035",
      "P036"
     ],
     "summary": "文末修正：经评论区提醒（@囧囧 有贡献）补充说明——驱逐舰目前一般作战样式中主要担当巡航导弹发射平台（巡航导弹射程可达1800公里），发射导弹比开过去用舰炮攻击便宜；故“完成所有任务的各种手段之中舰炮最便宜”并不确切，需追加前提“驱逐舰自主任务之中，最具性价比的是舰炮”，并注明已修正。",
     "role": "qualification"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P037"
     ],
     "summary": "补充：巡航导弹虽好，但驱逐舰实际上是替司令部和旗舰扛枪，驱逐舰长自己几乎没有想用巡航导弹的场景（作者怀疑其是否有权独自决定动用），类似战略核潜艇艇长背核导弹却只会用鱼雷。",
     "role": "qualification"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者（修正后）主张舰炮是驱逐舰自主任务之中最廉价的中远程打击武器，在性能可及的前提下是第一选择；且在其射程之内舰炮是一种决定性的攻击力量、目前没有办法有效防御，因此事实上成了公海舰队进行隐性示威与骚扰战术的最有效工具。",
     "evidence": [
      "E001",
      "E002",
      "E003"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为巡航导弹、反舰导弹、防空导弹、密集阵都有很重的后勤负担：不到万不得已不动用，储弹量少、再装填要几个小时甚至需要回港或专业补给舰，擅自动用会极大浪费军舰的战略价值。",
     "evidence": [
      "E004",
      "E005"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为主动攻击你的对手明知你有防空反导系统，绝不会添油式试探，而一定会全力持续饱和攻击以求突防。",
     "evidence": [
      "E006"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为两舰对决中首先要以能全负荷工作的防空系统与干扰手段持续抵抗、力求尽可能久的完全防御以争取战或逃的机会；因为以现代反舰手段的威力，一旦有一次命中，全舰效能几乎不可能不受沉重打击（盾）。",
     "evidence": [
      "E007",
      "E008"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为举盾之后须以巡航导弹、反舰导弹、舰炮等一切可用手段持续饱和攻击寻求突破（矛），这是雷霆一击、胜负手、绝无留手余地；以间隔一分钟一发的频率添油式发射等于浪费弹药和自杀。",
     "evidence": [
      "E009",
      "E010",
      "E011"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出现在的默认策略是导弹在空中靠路线规划与航速规划巧妙编队集结、有前锋有中锋有游击地调动对方防空火力以创造突防条件，是一种“狼群战术”；这种导弹群的协调战术是现代海战最大的核心焦点。",
     "evidence": [
      "E012",
      "E013",
      "E042"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为若一共有二十枚导弹，不应分成两个批次各十枚放出：协同攻击可能第十六枚左右才会找到机会，而分批发射的主官只怕要上军事法庭，因为这种发射阵位往往是友舰付出血的代价才争取到的。",
     "evidence": [
      "E014",
      "E015"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为除非涉及决斗式任务，这类再装填困难的攻击手段都会被极力避免使用（对方的铠甲有一尺厚，你的刀却只有一尺一寸长）。",
     "evidence": [
      "E016",
      "E017"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为舰炮没有导弹的后勤问题：炮弹几乎无限量、再装填速度因自动装弹机大大提高，且攻击力相当强大，除拉开距离降低命中率外对舰炮仍没有可用防御手段、装甲基本无效；舰炮射程之内已无先进与落后的区别，代差等于拉平了。",
     "evidence": [
      "E018",
      "E019",
      "E020"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为因为有水冷系统，现代舰炮可以一分钟四十发的频率长时间射击，且因先进火控系统与测量矫正手段而相当精准，无论是密集阵还是防空导弹系统都承受不了这样持续而猛烈的火力压力。",
     "evidence": [
      "E021",
      "E022"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者提出条件性判断：如果对方已经可以放心大胆地用舰炮攻击，说明你的防空力量基本已在前期导弹攻击中耗尽、对方比较确信你的舰炮已完蛋或自身射程一定超过你；此时你的密集阵顶不住多久。",
     "evidence": [
      "E023"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为双方防空资源充沛、反舰手段齐装满员时只敢隔一两百公里对峙；隐蔽性能好的舰可以逼近到自己导弹射程以内较近的地方使导弹规划路线更复杂；但无论如何也不会接近到对方舰炮的有效射程之内，因为那会招致导弹与舰炮齐发，且舰炮射程内还能隐身的可能性太小，还要考虑对方舰载预警机降低地球曲面的遮蔽。",
     "evidence": [
      "E024",
      "E025"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为新海战中两舰对峙是互相疯狂侦查、都站在极限射程边上等待友舰与空中支援，谁先凑够压倒优势谁先发动进攻，劣势一方会提前撤退；因此很难发生两艘现代军舰舰炮互相射击的场景，一旦发生被射击的一方其实已经输了（类似装甲骑士已倒地，对方只掏匕首来割首级）。",
     "evidence": [
      "E026"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为巨炮主义退出历史舞台是因为靠惯性飞行提高射程不经济：阻力在低于2马赫时与速度平方成正比、高于两马赫幂次还要提高，射程加倍需初速提高4-8倍并同步提高装药与膛压、发射机构变大；散布半径与射程平方成正比，维持同等命中率火力密度要提高至少四倍以上；军舰作为发射平台只好变成巨舰，在现代海战条件下无异于找死；惯性飞行增程存在极限（电磁炮也不例外），火炮极限射程在地球上只能保持一百公里上下，只有巨型履带平台有潜力超越。",
     "evidence": [
      "E027",
      "E028",
      "E029",
      "E030"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为增大射程的正道是火箭助推加末端制导，因此导弹作为远程攻击手段的合理性远远高过巨炮；舰炮实际上是一种“豪猪刺”，用来警告对方不可以逼得过近，一旦进入舰炮射程攻击强度就会陡然倍增，而隔着舰炮射程就给被攻击一方的防空手段大大增加了反应调度时间。",
     "evidence": [
      "E031",
      "E032"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为舰炮现在最主要的现实作用是用来“耍流氓”：在公海上仗着对方不敢随便动手，开着“小破船”公然接近对方到自己的舰炮射程之内，搞得对方吞不下又吐不出；对方既不能因距离近又不肯避让就直接先动手，也不能主动后撤或绕开，这就是所谓的“侮辱性抵近观察”。",
     "evidence": [
      "E033",
      "E034"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者据评论区提醒修正自己的表述：驱逐舰在目前一般作战样式中主要担当巡航导弹发射平台，巡航导弹射程可达1800公里、足以深入内陆，发射导弹飞过去要比把驱逐舰开到附近用舰炮攻击便宜；因此“在完成所有任务的各种手段之中舰炮最便宜”并不确切，需追加前提——“驱逐舰自主任务之中，最具性价比的是舰炮”。",
     "evidence": [
      "E036",
      "E037",
      "E038"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为驱逐舰实际上是替司令部和旗舰扛枪，驱逐舰长自己几乎没有会想要使用巡航导弹的场景（作者甚至怀疑驱逐舰长有没有权力独自决定动用巡航导弹），类似战略核潜艇艇长背着几十枚核导弹自己却只会用鱼雷。",
     "evidence": [
      "E039",
      "E040"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "open_question",
     "attribution": "questioner",
     "modality": "questioned",
     "statement": "提问者问“现代驱逐舰上的主炮有什么用”；作者给出的回答集中在“自主任务中最具性价比的中远程打击武器”与“公海耍流氓（侮辱性抵近观察）”，未逐项列举主炮的其他用途。",
     "evidence": []
    }
   ],
   "argument_steps": [
    "先给出（修正后的）总判断：舰炮是自主任务中最廉价的中远程打击武器，射程内是决定性力量且无法有效防御（P001）。",
    "说明导弹的后勤负担与再装填困难，擅自动用会浪费战略价值（P002）。",
    "指出对手不会添油式试探，一定饱和攻击求突防（P003）。",
    "展开两舰对决的盾—矛模型：先完全防御争取战或逃，再以一切手段饱和攻击（P004-P008）。",
    "描述导弹群“狼群战术”与预编程的复杂度分级，说明不能分批发射（P009-P014）。",
    "得出导弹使用受严格限制的结论，并以铠甲一尺厚、刀一尺一寸长的比喻收束（P015）。",
    "对比舰炮：炮弹几乎无限、再装填快、攻击力强、无法防御，代差被拉平（P016-P017）。",
    "回答“为什么舰炮难以防御”：水冷高频射击加精准火控，密集阵与防空导弹承受不了（P018-P021）。",
    "说明舰炮射程如何约束交战距离与隐身逼近，并推出现代舰炮互射极难发生（P022-P027）。",
    "解释巨炮主义退出历史舞台的弹道与经济原因，指出增程正道是火箭助推加末端制导（P028-P032）。",
    "给出舰炮最主要的现实作用——“耍流氓”与侮辱性抵近观察（P033-P034）。",
    "文末根据评论区提醒追加前提与修正说明，并补充驱逐舰作为巡航导弹发射平台的角色（P035-P037）。"
   ],
   "concept_usage": [
    {
     "term": "自主任务",
     "meaning": "作者在文末追加的前提中所用的限定：指驱逐舰自身可决策、可执行的任务范围；作者据此把“最具性价比”的范围从“完成所有任务”缩小为“驱逐舰自主任务”。",
     "evidence": "P036",
     "ambiguity": "该词由作者在修正说明中引入，本文未给出正式界定。"
    },
    {
     "term": "盾/矛",
     "meaning": "作者用来比喻两舰对决中的两个环节：以防空系统与干扰手段持续抵抗（盾）与以一切可用手段持续饱和攻击（矛）。",
     "evidence": "P005、P006",
     "ambiguity": "属比喻用法，本文未说明其与具体战术条令的对应。"
    },
    {
     "term": "狼群战术",
     "meaning": "作者用来指导弹在空中靠路线规划与航速规划编队集结、以多方向多批次调动对方防空火力以创造突防条件的协同战术。",
     "evidence": "P009",
     "ambiguity": "与二战潜艇“狼群战术”的关系本文未说明，属借喻。"
    },
    {
     "term": "添油式（发射）",
     "meaning": "作者指以间隔较长时间、少量逐次投入攻击的方式；作者认为这在现代海战中等于浪费弹药和自杀。",
     "evidence": "P003、P008",
     "ambiguity": "无。"
    },
    {
     "term": "豪猪刺",
     "meaning": "作者对舰炮作用的比喻：用来警告对方不可以逼得过近，进入其射程后攻击强度陡然倍增。",
     "evidence": "P032",
     "ambiguity": "属比喻用法。"
    },
    {
     "term": "耍流氓/侮辱性抵近观察",
     "meaning": "作者指在公海上用小舰船公然接近对方到自身舰炮射程之内、使对方既不能开火又不能避让的骚扰与示威行为。",
     "evidence": "P033",
     "ambiguity": "“耍流氓”是口语化贬义说法，作者并未给出军语定义。"
    },
    {
     "term": "代差",
     "meaning": "作者认为在舰炮射程之内已不存在先进与落后的区别，代差等于被拉平。",
     "evidence": "P017",
     "ambiguity": "该断言的作用范围限于“舰炮射程之内”，本文未说明其外部条件。"
    }
   ],
   "examples_and_targets": [
    "巡航导弹、反舰导弹、防空导弹、密集阵（P002、P006）：作者举的导弹类武器，用来说明后勤负担与再装填困难。",
    "三组导弹两前一后、一组向船头一组向船尾、后一组指向中段（P010）：作者设想的导弹协同攻击阵位。",
    "十枚、十五枚、二十枚与放出18枚/20枚的差别（P012）：作者举的复杂度与战果对比。",
    "两小时前为打鱼雷艇用掉六枚导弹（P013、P014）：作者举的消耗导弹的陷阱例。",
    "铠甲一尺厚、刀一尺一寸长（P015）：作者的比喻材料。",
    "水冷系统、自动装弹机、火控系统与测量矫正手段（P016、P020）：作者举的技术条件。",
    "装甲骑士已倒地、人家只掏匕首来割首级（P027）：作者的比喻材料。",
    "惯性飞行、2马赫、4-8倍初速、射程平方与散布半径、战列巡洋舰（P029、P030）：作者的弹道学与舰种论证材料，含需外部核查的定量断言。",
    "电磁炮、巨型履带平台（P031）：作者对增程极限的举例与设想的例外平台。",
    "火箭助推加末端制导（P032）：作者认为的增程正道。",
    "“小破船”抵近公海舰队（P033）：作者设想的场景。",
    "评论区提醒与 @囧囧（P035）：作者据以修正开头表述的外部意见来源。",
    "巡航导弹射程1800公里、驱逐舰替司令部和旗舰扛枪、战略核潜艇艇长背核导弹却只用鱼雷（P036、P037）：作者的比较与类比材料。",
    "反驳/限定对象：作者自己开头“舰炮最便宜”的表述（P001、P036），作者在文末主动追加前提修正。"
   ],
   "conditions": [
    "“在性能可及的前提下，舰炮是第一选择”（P001）：第一选择的前提条件。",
    "“在完成所有任务的各种手段之中，舰炮最便宜，并不确切。需要追加一条前提——驱逐舰自主任务之中，最具性价比的是舰炮”（P036）：作者自己追加的核心限定。",
    "“不到万不得已都不会动用”（P002）：导弹使用的条件。",
    "“一旦有一次命中，全舰效能几乎是不可能不受沉重打击的”（P005）：后果性条件。",
    "“如果对方已经可以放心大胆的用舰炮攻击了”（P021）、“或者自己的射程一定超过你”（P021）：条件句。",
    "“如果发生新海战……一旦彼此都下了作战决心”（P026）：假设条件。",
    "“前提是对方给了你机会在射程内发射到了十六枚枚导弹，这一点首先就很困难，要看你的盾有多结实了”（P013）：协同攻击第十六枚左右才找到机会的前提条件（原文“枚枚”为重复用字）。",
    "“即使是电磁炮也不例外”（P031）：让步限定。",
    "“除非涉及到这类决斗式的任务”（P015）：例外条件。",
    "“目前”“直到目前”“现在”等时间限定（P016、P020、P033）。"
   ],
   "rhetoric_and_tone": "知乎长答的战术科普—论辩体，第一人称与第二人称“你”交替，用两舰对决的推演带动读者。以“此为盾”“此为矛”的对仗句分段；大量比喻：铠甲一尺厚与刀一尺一寸长、豪猪刺、装甲骑士倒地后掏匕首割首级、小破船“耍流氓”。口语与戏谑并存（“约等于剧终了”“是不是很无耻？”“搞得对方吞不下又吐不出”），并以括号插入自嘲式说明（“我甚至怀疑驱逐舰长有没有权力独自决定动用巡航导弹”）。P018 用一行破折号作分隔。文末设“经评论区提醒”的修正段，公开更正开头表述并注明 @囧囧 有贡献，属罕见的自我修订结构。",
   "unresolved_questions": [
    "P001 与 P036 之间存在版本性修订关系：P001 是修改后的开头并注明“这一段有修改，原因附文末”，P036 说明原表述“舰炮最便宜”不确切并追加前提。重建时需把两处合并理解为作者的最终立场（驱逐舰自主任务之中最具性价比），本文未给出修改前的原文。",
    "P002 “再装填要几个小时”与 P029“初速需要提高4-8倍”“火力密度要提高至少四倍以上”等定量说法本文未给出来源，待外部核查。",
    "P013 “这种发射阵位往往是友舰付出了血的代价才能争取到的”“主官只怕要上军事法庭”属作者的推想与修辞，本文未给出实例或条令依据。",
    "P031 “火炮的极限射程在地球上只能保持一百公里上下。只有巨型履带平台有这个潜力超越”是作者的断言，本文未给出来源。",
    "P033 描述的“侮辱性抵近观察”是否有公开实例，本文未说明；作者也未给出该说法的出处。",
    "P035 评论区提醒与 @囧囧 的具体内容本文只给出结论式转述，未附原文。",
    "P037 作者怀疑“驱逐舰长有没有权力独自决定动用巡航导弹”，属作者的疑问，本文未给出答案。",
    "提问者问“现代驱逐舰上的主炮有什么用”，作者的回答以“自主任务中的性价比”和“公海示威骚扰”为主，未系统列举主炮的全部用途（如对陆支援、防空辅助等）。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P001",
     "quote": "舰炮是驱逐舰自主任务之中最廉价的中远程打击武器",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P001",
     "quote": "且在其射程之内，舰炮是一种决定性的攻击力量，目前没有办法有效防御",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P001",
     "quote": "（这一段有修改，原因附文末）",
     "relation": "context"
    },
    {
     "key": "E004",
     "paragraph_id": "P002",
     "quote": "储弹量就那么点，再装填要几个小时，甚至需要回港或者专业补给舰才能办到。",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P002",
     "quote": "你如果擅自动用这个储备去完成本来不必这个手段去完成的任务，你将极大的浪费掉军舰的战略价值。",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P003",
     "quote": "绝不会添油式的试探，而是一定会全力持续饱和攻击以求突防。",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P005",
     "quote": "一旦有一次命中，全舰效能几乎是不可能不受沉重打击的",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P005",
     "quote": "此为盾。",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P006",
     "quote": "此为矛。",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P007",
     "quote": "这是雷霆一击，胜负手，绝无留手余地。",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P008",
     "quote": "那等于浪费弹药和自杀。",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P009",
     "quote": "是一种“狼群战术”。",
     "relation": "supports"
    },
    {
     "key": "E013",
     "paragraph_id": "P011",
     "quote": "这种导弹群的协调战术是现代海战最大的核心焦点。",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P013",
     "quote": "协同攻击，可能第十六枚左右才会找到机会",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P013",
     "quote": "分两个批次发射，主官只怕要上军事法庭",
     "relation": "supports"
    },
    {
     "key": "E016",
     "paragraph_id": "P015",
     "quote": "除非涉及到这类决斗式的任务，这类再装填困难的攻击手段都会被极力的避免使用。",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P015",
     "quote": "你可以理解为对方的铠甲有一尺厚，你的刀却只有一尺一寸长。",
     "relation": "context"
    },
    {
     "key": "E018",
     "paragraph_id": "P016",
     "quote": "而舰炮没有这个问题。炮弹几乎是无限量的",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P016",
     "quote": "对舰炮仍然没有可用的防御手段，装甲这类东西对现代舰炮基本无效",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P017",
     "quote": "舰炮射程之内已无先进与落后的区别，代差等于拉平了。",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P020",
     "quote": "现代舰炮可以做到以一分钟四十发的频率长时间射击",
     "relation": "supports"
    },
    {
     "key": "E022",
     "paragraph_id": "P020",
     "quote": "无论是密集阵还是防空导弹系统都承受不了这样持续而猛烈的火力压力。",
     "relation": "supports"
    },
    {
     "key": "E023",
     "paragraph_id": "P021",
     "quote": "你的防空力量肯定基本已在前期导弹攻击力耗尽了",
     "relation": "supports"
    },
    {
     "key": "E024",
     "paragraph_id": "P024",
     "quote": "但无论如何也不会接近到对方舰炮的有效射程之内。",
     "relation": "supports"
    },
    {
     "key": "E025",
     "paragraph_id": "P025",
     "quote": "更何况舰炮射程以内还能隐身的可能性太小了。",
     "relation": "supports"
    },
    {
     "key": "E026",
     "paragraph_id": "P027",
     "quote": "所以很难很难发生两艘现代军舰舰炮互相射击的场景。一旦发生，被射击的一方其实已经输了。",
     "relation": "supports"
    },
    {
     "key": "E027",
     "paragraph_id": "P029",
     "quote": "因为要提高射程，全靠惯性飞行是非常不经济的。",
     "relation": "supports"
    },
    {
     "key": "E028",
     "paragraph_id": "P029",
     "quote": "这意味着射程加大一倍，要维持同等命中率，火力密度要提高至少四倍以上。",
     "relation": "supports"
    },
    {
     "key": "E029",
     "paragraph_id": "P030",
     "quote": "这就是为什么现代海军已经不搞战列巡洋舰的原因。",
     "relation": "supports"
    },
    {
     "key": "E030",
     "paragraph_id": "P031",
     "quote": "火炮的极限射程在地球上只能保持一百公里上下。",
     "relation": "supports"
    },
    {
     "key": "E031",
     "paragraph_id": "P032",
     "quote": "所以导弹作为远程攻击手段的合理性要远远的高过巨炮。",
     "relation": "supports"
    },
    {
     "key": "E032",
     "paragraph_id": "P032",
     "quote": "舰炮实际上是一种豪猪刺，用来警告对方不可以逼得过近的。",
     "relation": "supports"
    },
    {
     "key": "E033",
     "paragraph_id": "P033",
     "quote": "实际上现在舰炮最主要的现实作用，是用来耍流氓。",
     "relation": "supports"
    },
    {
     "key": "E034",
     "paragraph_id": "P033",
     "quote": "这就是所谓的“侮辱性抵近观察”。",
     "relation": "supports"
    },
    {
     "key": "E035",
     "paragraph_id": "P034",
     "quote": "其实你也不见得就会开炮，结果搞得大家都吃不香睡不好，是不是很无耻？",
     "relation": "supports"
    },
    {
     "key": "E036",
     "paragraph_id": "P036",
     "quote": "所以说本文所说在完成所有任务的各种手段之中，舰炮最便宜，并不确切。",
     "relation": "qualifies"
    },
    {
     "key": "E037",
     "paragraph_id": "P036",
     "quote": "需要追加一条前提——驱逐舰自主任务之中，最具性价比的是舰炮。这条已经修正了。",
     "relation": "qualifies"
    },
    {
     "key": "E038",
     "paragraph_id": "P036",
     "quote": "巡航导弹射程可以达到1800公里，足以深入内陆。",
     "relation": "supports"
    },
    {
     "key": "E039",
     "paragraph_id": "P037",
     "quote": "驱逐舰实际上是替司令部和旗舰扛枪。",
     "relation": "supports"
    },
    {
     "key": "E040",
     "paragraph_id": "P037",
     "quote": "驱逐舰长自己几乎没有会想要使用巡航导弹的场景",
     "relation": "supports"
    },
    {
     "key": "E041",
     "paragraph_id": "P035",
     "quote": "经评论区提醒，做一些额外说明， @囧囧 对此有贡献：",
     "relation": "context"
    },
    {
     "key": "E042",
     "paragraph_id": "P012",
     "quote": "放出18枚和放出20枚，很可能是毫无战果与击沉的差别。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "海军战术",
    "舰炮与导弹武器",
    "军事技术",
    "海战推演"
   ],
   "issue_candidates": [
    "驱逐舰主炮的用途",
    "舰炮与导弹的成本和后勤比较",
    "导弹饱和攻击与防空",
    "舰炮射程与交战距离",
    "巨炮主义的衰落",
    "公海抵近示威"
   ],
   "text_function_candidates": [
    "答疑",
    "战术推演",
    "科普",
    "自我修正说明"
   ],
   "object_candidates": [
    "现代驱逐舰",
    "舰炮",
    "巡航导弹",
    "反舰导弹",
    "密集阵",
    "防空导弹",
    "战列巡洋舰",
    "电磁炮",
    "公海舰队",
    "评论区 @囧囧"
   ],
   "working_keywords": [
    "自主任务",
    "中远程打击武器",
    "盾",
    "矛",
    "狼群战术",
    "添油式",
    "代差",
    "巨炮主义",
    "豪猪刺",
    "侮辱性抵近观察",
    "耍流氓",
    "1800公里"
   ]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P037 共 37 段全部读完，status=read、full_text_checked=true。文本与 lexical 无 divergence。brief 字段为正文开头的截断（含“（这一段有修改，原因附文末）”），与正文 P001 重合，不作为独立证据。Q001 属提问者。本篇存在作者自己的版本性修订：P001 注明有修改、P036 说明修改原因并追加“驱逐舰自主任务之中”这一前提，已在 unresolved_questions 登记。P018 为一行为“—————”的分隔线（body 字段）。平台为知乎。"
 },
 "f9e70dc0": {
  "analysis": {
   "question_context": "提问者（Q001）问：《越人学远射》的寓言什么意思？作者先否定一种通行解读（把“适在五步之内”解为“箭射了还没五步远”，把越人当作不善射的反面教材），再给出自己的正解：越人对着天空反复发射而箭都落在方圆五步之内，是因为决不改变射箭的姿势（“不易仪”），寓言要人即使世道已变也要守住本道，越人在文中是以神射入文。作者并称该段被“一代代不尊师训的宅儒”全部解反。提问属提问者；正解与反驳均属作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "引《越人学远射》原文（quote 字段）：“越人学远射，参天而发，适在五步之内，不易仪也。世已变矣，而守其故，譬犹越人之射也。”", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "否定通行解读：把该句解为“越人朝天上射箭，箭射了还没五步远”是错的。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004", "P005"], "summary": "给出正解：越人学远射、对天空反复发射，远处落地的箭却都落在方圆五步以内，原因在于决不改变射箭的姿势；世道已改变时还是要守住原来的宗旨。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "指出原文作者把越人当正面教材，并以紧随其后的下文（月望日夺其光、末不可以强于本、一渊不两鲛、故惟不动则所以无不动也）为证，解为“有些东西是本道、坚守不动，守住本道才能维持平衡和基础、才能展开变化”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "论证“第一，越人以射见称”，列举《孟子》《韩非子》《越绝书》及《吴越春秋》（作者称其为古代论射经典篇章之一）为证。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P017"], "summary": "长引《吴越春秋》中范蠡进善射者陈音、陈音为越王论射道（弩生于弓、正射持弩之道、望敌仪表、道出于天事在于人）及越王使陈音教士习射、三月军士皆能用弓弩之巧的整段（quote 字段）。", "role": "context"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "引《史记·越王句践世家》越师射伤吴王阖庐事，并反问“飞鸟尽，良弓藏”是哪国人说的，断言越人不是射术的反面典型。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023"], "summary": "以越王勾践剑存世、吴越兵甲冠于天下、越国是战斗民族、楚国有百步穿杨的养由基等常识反驳“越人不善射”之说，认定该说法是匪夷所思的妄断；结论：越人是以神射入文。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "补充第二至第四点理由：“适”作“恰好击中”解更匹配原意；射术里“不易仪”永远没有贬义；若真是远射，这个集中度绝对算是神射，即使解为垂直向天落在身边五步之内也一样是神射。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029", "P030"], "summary": "总结：只可能把越人解为极为正面的含义；把这种神射解为笑话的是解读人全无射箭经验的妄解；并批评“一代代不尊师训的宅儒”把君子六艺丢到天边、把整个段落全部解反。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "被作者反驳的解读是：把《越人学远射》解为“越人朝天上射箭，箭射了还没五步远”，即把越人当作不善射的反面教材。", "evidence": ["E002", "E028"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的正解是：越人学习远射，对着天空反复发射，远处落地的箭却都落在方圆五步范围以内，原因在于他们决不改变射箭的姿势；世道已改变时，还是要守住原来的宗旨，犹如越人射箭那样。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为原文作者不是在把越人当白痴反面教材，而是拿他们当正面教材。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引该段的下文（月望日夺其光、日出星不见、末不可以强于本、指不可以大于臂、下轻上重其覆必易、一渊不两鲛、水定则清正动则失平、故惟不动则所以无不动也）作为判断文义的依据。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者解为：原文是在说有些东西是本道、坚守不动，次要的东西并不能影响它；守住这些本道才能维持平衡和基础、才能展开变化；即要求做到“（即使）世已变矣，（也要）而守其故，譬犹越人之射”。", "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的第一个理由是越人以射见称，并举《孟子》“越人关弓而射之”、《韩非子》“可必，则越人不疑羿”、《越绝书》“射浦者，句践教习兵处也”与《吴越春秋》为证。", "evidence": ["E010", "E011", "E012", "E013", "E031"]},
    {"claim_id": "C007", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者长引《吴越春秋》陈音论射（弩生于弓、正射持弩之道、望敌仪表、道出于天事在于人）及越王使陈音教士习射于北郊之外、三月军士皆能用弓弩之巧一节，用以证明越国重视射术。", "evidence": ["E014", "E015"]},
    {"claim_id": "C008", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引《史记·越王句践世家》所记越因袭击吴师、吴师败於槜李、射伤吴王阖庐一节，作为越人善射的史证。", "evidence": ["E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反问“飞鸟尽，良弓藏”是哪国人说的，并断言越人是不是射术的反面典型不言而喻。", "evidence": ["E017", "E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以越王勾践剑至今存世、吴越兵甲冠于天下（作者称这是古代常识）、越国是出了名的战斗民族、楚国出了百步穿杨的养由基等为据，认为说越人不善射到“对空发射都射不出五步远”的程度显然是匪夷所思的妄断。", "evidence": ["E019", "E020", "E021"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出结论：合理的答案只有一个——越人在这里不但不是不善射的反面教材，反而是以神射入文。", "evidence": ["E022"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的第二个理由：“适”作为“及远”解远不如作“恰好击中”解来得匹配原意，适逢、适中、适才、合适都是“刚刚好”“命中”之意。", "evidence": ["E023", "E024"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的第三个理由：射术里提到“不易仪”，永远没有贬义（作者称“这一点不解释”）。", "evidence": ["E025"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的第四个理由：“参天而射，适在五步之内”如果是真的远射，这个集中度绝对算是神射；甚至解为垂直向天发射落在身边五步之内，都一样是神射。", "evidence": ["E026", "E027"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结：只可能将越人解为极为正面的含义；把越人这种神射解为笑话的，其实是解读人全无射箭经验的妄解；并批评一代代不尊师训的宅儒把君子六艺丢到天边、把整个段落全部解反。", "evidence": ["E028", "E029", "E030"]},
    {"claim_id": "C016", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问《越人学远射》的寓言什么意思；作者以“守本道、越人以神射入文”作答，并否定了另一种解读。", "evidence": []}
   ],
   "argument_steps": [
    "先引原文（P001）。",
    "否定通行解读“箭射了还没五步远”（P002）。",
    "给出正解：因决不改变姿势而箭落五步之内，世变而守其故（P003-P005）。",
    "指出原文作者以越人为正面教材（P006）。",
    "引出原文下文为证，解为守住本道才能维持平衡与展开变化（P007-P010）。",
    "逐条举证：第一，越人以射见称（《孟子》《韩非子》《越绝书》《吴越春秋》）（P011-P017）。",
    "续引《史记》越师射伤吴王阖庐事，并反问“飞鸟尽，良弓藏”的出处（P018-P021）。",
    "以越王勾践剑、吴越兵甲、养由基等常识反驳越人不善射之说，结论为以神射入文（P022-P023）。",
    "补第二至第四点理由（“适”的训释、“不易仪”无贬义、集中度即神射）（P024-P027）。",
    "收束为对“宅儒”误读的整体批评（P028-P030）。"
   ],
   "concept_usage": [
    {"term": "适在五步之内", "meaning": "争论的核心短语。作者主张“适”应作“恰好击中”解，全句指箭恰好落在五步之内（集中度极高），而非“箭射了还没五步远”。", "evidence": "P002、P024", "ambiguity": "作者承认若解为垂直向天落在身边五步之内“都一样是神射”，故该短语的最终训释在文中仍有两种并存读法。"},
    {"term": "不易仪", "meaning": "作者解为“决不改变射箭的姿势”；并称射术里提到“不易仪”永远没有贬义。", "evidence": "P004、P025", "ambiguity": "作者明说“这一点不解释”，未给出训诂或出处依据。"},
    {"term": "本道", "meaning": "作者用来指原文中坚守不动、次要东西不能影响的东西；守住本道才能维持平衡和基础并展开变化。", "evidence": "P009", "ambiguity": "该词是作者的解释用语，原文并未出现“本道”二字。"},
    {"term": "宅儒", "meaning": "作者对被指误读该段者的贬称，称其不尊师训、丢掉君子六艺。", "evidence": "P029", "ambiguity": "具体所指（哪一注家或哪个时代的解读传统）本文未说明。"},
    {"term": "神射", "meaning": "作者用来指越人形象：射术极高、集中度极高（而非不善射）。", "evidence": "P023、P026", "ambiguity": "“神射”与“集中度”的量化标准本文未给出。"}
   ],
   "examples_and_targets": [
    "《越人学远射》原文及其下文（P001、P008）：作者引作论证对象的古籍文本，本文未说明其出处书名，待外部核查。",
    "《孟子》“有人于此，越人关弓而射之”（P013）：作者引证。",
    "《韩非子》“羿执鞅持扞……故曰：可必，则越人不疑羿；不可必，则慈母逃弱子”（P014）：作者引证。",
    "《越绝书》“射浦者，句践教习兵处也”“射卒陈音死，葬民西，故曰陈音山”（P015）：作者引证。",
    "《吴越春秋》陈音论射长段（P016、P017）：作者引证，并称该篇是古代论射的经典篇章之一。",
    "《史记·卷四十一·越王句践世家第十一》吴越槜李之战（P018、P019）：作者引证。",
    "“飞鸟尽，良弓藏”（P020）：作者引用的成语，并反问出自哪国人。",
    "越王勾践剑、吴越兵甲、养由基百步穿杨（P022）：作者举的常识性证据。",
    "反驳对象：把越人解为不善射反面教材的通行解读与持此说的“宅儒”（P002、P028、P029）。"
   ],
   "conditions": [
    "“如果是真的远射”（P026）：作者对第四点理由设定的条件。",
    "“甚至你就算解为垂直向天发射落在身边五步之内”（P027）：让步性假设。",
    "“（即使）世已变矣，（也要）而守其故”（P010）：作者括注出的让步—坚持结构。",
    "“这一点不解释”（P025）：作者对第三点理由主动不作展开。",
    "“就算是修辞，也修辞得有点太傻大胆了”（P022）：作者的让步式修辞评价。"
   ],
   "rhetoric_and_tone": "训诂—论辩体，语气笃定而带训斥。大量使用古籍引文与书名冒号式列举（《孟子》《韩非子》《越绝书》《吴越春秋》《史记》），并以反问推进（“更别忘了，‘飞鸟尽，良弓藏’，这话是哪国人说的？”“越人是不是射术的反面典型，不言而喻”）。以“第一/第二/第三/第四”分点。对异见者用贬称“宅儒”“妄解”“妄断”，并称“一代代不尊师训的宅儒们，君子六艺丢到天边去了”。篇幅过半为引文（P017 一段近千字）。",
   "unresolved_questions": [
    "本文通篇未说明《越人学远射》出自何书，也未标出通行解读的出处与注家；作者所反驳的“宅儒”具体指谁，本文未说明，待外部核查。",
    "P017 的《吴越春秋》引文长达约一千字，属整段照录；其文字与传世版本的差异需版本核对。",
    "P019《史记》引文中“射伤吴王阖庐”与《越绝书》等记载的异同，本文未作比对说明。",
    "P020 反问“飞鸟尽，良弓藏”是哪国人说的，作者未直接给出答句，读者需自行推断（作者暗示为越国）。",
    "作者称“射术里提到‘不易仪’，永远没有贬义”并明说“这一点不解释”，该断言的依据本文未给出。",
    "作者承认即使把“参天而射，适在五步之内”解为垂直向天落在身边五步之内“都一样是神射”，故该句究竟应取“击中远处目标”还是“垂直发射”读法，文中未最终确定。",
    "P029“一代代不尊师训的宅儒们”属群体性贬称，未点名，重建时不得据此外推到具体个人。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "越人学远射，参天而发，适在五步之内，不易仪也。", "relation": "context"},
    {"key": "E002", "paragraph_id": "P002", "quote": "这解为“越人朝天上射箭，箭射了还没五步远”是错的。", "relation": "contradicts"},
    {"key": "E003", "paragraph_id": "P004", "quote": "越人学习远射，对着天空反复发射，远处落地的箭却都落在方圆五步范围以内，原因在于他们决不改变射箭的姿势。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "世道已改变时，还是要守住原来的宗旨，犹如越人射箭那样。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "作者不是在把越人当白痴反面教材，而是在拿ta们当成正面教材。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "故末不可以强于本，指不可以大于臂。下轻上重，其覆必易。", "relation": "context"},
    {"key": "E007", "paragraph_id": "P008", "quote": "故惟不动，则所以无不动也。", "relation": "context"},
    {"key": "E008", "paragraph_id": "P009", "quote": "有些东西是本道，是坚守不动的，次要的东西并不能影响它", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "（即使）世已变矣，（也要）而守其故，譬犹越人之射", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "第一，越人以射见称。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "有人于此，越人关弓而射之。", "relation": "context"},
    {"key": "E012", "paragraph_id": "P014", "quote": "故曰：可必，则越人不疑羿；不可必，则慈母逃弱子。", "relation": "context"},
    {"key": "E013", "paragraph_id": "P015", "quote": "射浦者，句践教习兵处也。", "relation": "context"},
    {"key": "E014", "paragraph_id": "P017", "quote": "道出于天，事在于人，人之所习，无有不神。", "relation": "context"},
    {"key": "E015", "paragraph_id": "P017", "quote": "于是乃使陈音教士习射于北郊之外，三月，军士皆能用弓弩之巧。", "relation": "context"},
    {"key": "E016", "paragraph_id": "P019", "quote": "越因袭击吴师，吴师败於槜李，射伤吴王阖庐。", "relation": "context"},
    {"key": "E017", "paragraph_id": "P020", "quote": "更别忘了，“飞鸟尽，良弓藏”，这话是哪国人说的？", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P021", "quote": "越人是不是射术的反面典型，不言而喻。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P022", "quote": "吴越兵甲，冠于天下，这是古代常识。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P022", "quote": "楚国可是出了百步穿杨养由基的", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P022", "quote": "显然是匪夷所思的妄断。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P023", "quote": "越人在这里不但不是不善射的反面教材，反而是以神射入文。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P024", "quote": "“适”作为“及远”解远不如作“恰好击中”解来的匹配原意。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P024", "quote": "适逢、适中、适才，合适，都是“刚刚好”“命中”之意。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P025", "quote": "第三，射术里提到“不易仪”，永远没有贬义。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P026", "quote": "如果是真的远射，这个集中度绝对算是神射。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P027", "quote": "甚至你就算解为垂直向天发射落在身边五步之内，都一样是神射。", "relation": "qualifies"},
    {"key": "E028", "paragraph_id": "P028", "quote": "把越人这种神射解为笑话的，其实是解读人全无射箭经验的妄解。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P029", "quote": "一代代不尊师训的宅儒们，君子六艺丢到天边去了。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P030", "quote": "ta们把整个段落全部解反了。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P016", "quote": "(这一篇是古代论射的经典篇章之一)", "relation": "context"},
    {"key": "E032", "paragraph_id": "P018", "quote": "《史记·卷四十一·越王句践世家第十一》：", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["训诂与古籍解读", "先秦史", "射术史", "寓言解释"],
   "issue_candidates": ["《越人学远射》的文义", "“适在五步之内”的训释", "越人是否善射", "守故与应变的古今之辨"],
   "text_function_candidates": ["答疑", "训诂考辨", "驳论", "引证"],
   "object_candidates": ["越人", "陈音", "越王句践", "吴王阖庐", "养由基", "羿", "《孟子》", "《韩非子》", "《越绝书》", "《吴越春秋》", "《史记》", "勾践剑", "宅儒"],
   "working_keywords": ["越人学远射", "参天而发", "适在五步之内", "不易仪", "守其故", "本道", "神射", "妄解", "君子六艺"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P030 共 30 段全部读完，status=read、full_text_checked=true。文本与 lexical 无 divergence；字段中 P001、P017、P019 为 quote（引文），其余为 body。brief 字段是正文开头的截断（原文＋“这解为……是错的”），与正文重合，不作为独立证据。Q001 属提问者。作者未说明所引古籍的出处书名与所反驳注家的身份，已在 unresolved_questions 登记；P017 引文过长（约 1000 字），记录中的段落转录会按 MAX_PARA_SAMPLE 截断，短引仍可回查语料原文。平台为知乎。"
 },
 "145d3e3c": {
  "analysis": {
   "question_context": "提问者（Q001）问：学理工科真的会影响文笔表达吗？怎么样可以兼顾？作者承认“理工科的确从统计上讲文笔比较差”，但认为这不是理工科本身的错：主要原因是理工科被选择为“对爱幻灭的遗族们为自己的子女选择的避难所”，即父母安排子女学理工是在安排其出家避世，背后隐藏着对爱的恐惧与厌弃；因此文笔好的前提与安排你学理工的基本初衷相背离。对于“如何兼顾”，作者没有给出方法，只说“如果你真的想要‘文笔’好，你唯一需要的只是爱”。提问属提问者；作者的回答是一种社会—心理成因解释。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "承认前提并否认归因：理工科从统计上文笔比较差，但这不是理工科本身的错，逻辑链条要长得多。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "给出主因：理工科是“对爱幻灭的遗族们为自己的子女选择的避难所”；中国经历了可怕的社会变迁，原来信奉的乡土之谊、同志之情、亲族之爱、朋友之义在不同时期反而成了自己遇害的因由。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "说明这种避难所的功能：人们渴望置身于人际关系之外、回避一切个人态度的表达，最好是你问什么我只给全无责任的回答；学了理工科就有理由以数据不全能力有限推脱，或给出只跟自然常数、自然规律和国家标准有关的客观计算，从而“中立而且安全”，还有“不善交往”“不通世故”的保护色。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "点明动机：父母强力安排子女学理工科是在安排出家避世；这个默然不言的动机下隐藏着对爱的神秘的恐惧和厌弃——不想爱了，怕爱了，也怕被“爱”了。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "推出文笔结论：理工科里充斥着被默许、被褒扬、被暗自期待的对感情、对关切、对“感性”的隔离；没有爱连性也乏味到需要快进，何况“文笔”；这才是中国多年“抑文扬理”的根源，理工科难出文笔好的青年是因为文笔好的前提与安排你学理工的基本初衷相背离。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020"], "summary": "反转式收束：这可以算是为你好，文笔什么的，不重要；但如果你真的想要“文笔”好，你唯一需要的只是爱——有爱才有令人动容的力量、才有明白发生了什么的眼睛、才在人生故事中出场、才有所谓的经历。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "补充论证：即使没文化的人出于爱的粗口，文笔也能压倒骈四骊六的《洛神赋》；世界上最无价值的就是雕饰繁复而没有心的垃圾；内有真爱则语言形式的“粗粝”反而增色；无爱的人会盛赞“技巧”，因为他们以为那是可以“学”的能力，作者说这根本就想错了。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者承认理工科的确从统计上讲文笔比较差。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这不是理工科本身的错，逻辑链条要比这长得多。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的主要原因是：理工科是对爱幻灭的遗族们为自己的子女选择的避难所。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者叙述：中国经历了可怕的社会变迁和风雨飘摇，原来信奉的乡土之谊、同志之情、亲族之爱、朋友之义，都在不同的时期反而成了自己遇害的因由。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人们渴望能置身于人际关系之外、回避一切个人态度的表达，最好的安排是无论被问什么都只给出自己全无责任的回答（如以“这个没有科学研究”不答，或只代科学给出计算）。", "evidence": ["E005", "E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以第一人称说明学了理工科后的处境：有充分理由以数据不全能力有限推脱，或给出与个人态度全然无关、只跟自然常数、自然规律和国家标准有关的客观计算；无论哪个都是中立而且安全的，没有表露个人态度，别人怪不到头上。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者还说自己有“不善交往”“不通世故”的保护色。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言父母们为子女强力安排理工科，是在为他们安排出家避世。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为在这个默然不言的动机下隐藏了对爱的神秘的恐惧和厌弃：不想爱了，怕爱了，也怕被“爱”了，所以理工。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为理工科里充斥着被默许的、被褒扬的、被暗自期待的对感情、对关切、对“感性”的隔离。", "evidence": ["E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为没有了爱，连性也乏味到需要快进，何况“文笔”；这才是中国这么多年“抑文扬理”的根源；理工科难出文笔好的青年，是因为文笔好的前提与安排你学理工的基本初衷相背离。", "evidence": ["E016", "E017", "E018"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“这可以算是为你好。文笔什么的，不重要。”作反讽式小结。", "evidence": ["E019"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出正面条件：如果你真的想要“文笔”好，你唯一需要的只是爱；有爱才会有令人动容的力量、才有明白发生了什么的眼睛、才在人生故事中出场、才有所谓的经历；无爱的人不是没有经历过事情，而是意识不到自己在经历什么、已经经历了什么。", "evidence": ["E020", "E021"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为即使是没有文化的人在急切之下的口不择言的粗口，若是出于爱，文笔也能压倒骈四骊六的《洛神赋》；世界上最无价值的就是雕饰繁复而没有心的垃圾；内有真爱，语言形式的“粗粝”反而只会增色。", "evidence": ["E022", "E023"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人们只会因为深受打动而赠你文豪桂冠，再反过来赞叹你如何“质朴不文、直指人心”。", "evidence": ["E024"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为无爱的人会盛赞你的“技巧”，因为他们以为那是可以“学”的，以为那是“能力”、是你“厉害”，会相信“大家都是人，他能我也能”；作者说这根本就想错了。", "evidence": ["E025", "E026"]},
    {"claim_id": "C017", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“学理工科真的会影响文笔表达吗？怎么样可以兼顾”；作者回答了成因（避难所与对爱的隔离），但未给出“兼顾”的具体办法，只说唯一需要的是爱。", "evidence": []}
   ],
   "argument_steps": [
    "先承认“理工科统计上文笔比较差”，但否认这是理工科本身的错（P001-P002）。",
    "把原因归为“避难所”：社会变迁使传统的乡土、同志、亲族、朋友之义反成遇害因由（P003-P004）。",
    "说明避难所的功能是回避个人态度表达、只给全无责任的回答（P005-P008）。",
    "指出“不善交往”“不通世故”的保护色（P009）。",
    "点明父母安排理工科即安排出家避世，动机隐藏着对爱的恐惧与厌弃（P010-P014）。",
    "推出理工科对感情与感性的隔离，并据此解释“抑文扬理”与文笔的缺失（P015-P018）。",
    "以反讽小结“文笔什么的，不重要”（P019）。",
    "给出正面条件：想要文笔好，唯一需要的是爱（P020）。",
    "以粗口与《洛神赋》的对比、以“技巧”与“爱”的对立收束（P021-P024）。"
   ],
   "concept_usage": [
    {"term": "避难所", "meaning": "作者用来指理工科在本文中的社会功能：让“对爱幻灭的遗族”的子女得以置身于人际关系之外、回避个人态度的表达。", "evidence": "P003、P010", "ambiguity": "属作者的比喻性定性，本文未给出可检验的界定（如统计口径）。"},
    {"term": "出家避世", "meaning": "作者用来比喻父母为子女强力安排理工科的用意，与宗教出家作类比。", "evidence": "P010", "ambiguity": "属比喻用法，本文未说明其与真实宗教出家的异同。"},
    {"term": "中立而且安全", "meaning": "作者用来指以理工科式的客观计算回答一切问题，从而不表露个人态度、不承担责任的状态。", "evidence": "P007、P008", "ambiguity": "作者的讽刺性用语，本文未说明其在职业伦理上的含义。"},
    {"term": "文笔", "meaning": "本文中作者把它与“爱”绑定：有爱才有令人动容的力量与经历，文笔是被打动后追认的结果，而非可“学”的技巧。", "evidence": "P020、P021、P023", "ambiguity": "作者未给出“文笔”的定义或评价标准，也未讨论“兼顾”的具体路径。"},
    {"term": "抑文扬理", "meaning": "作者用来指中国多年偏重理工、压抑人文的现象，并称其根源在于上述对爱的隔离。", "evidence": "P018", "ambiguity": "该说法带引号，作者未给出处或时间范围。"},
    {"term": "爱幻灭的遗族", "meaning": "作者用来指因社会变迁而对传统人情之爱幻灭的一代人（即安排子女学理工的父母辈）。", "evidence": "P003", "ambiguity": "该群体的具体所指与代际范围本文未说明。"}
   ],
   "examples_and_targets": [
    "乡土之谊、同志之情、亲族之爱、朋友之义（P004）：作者对中国社会变迁的叙述材料。",
    "“你问我喜欢哪一派，我回答你这个没有科学研究”“你问我这反应是否能发生，我能给你一张计算纸”（P006）：作者举的回避表态的对话例。",
    "自然常数、自然规律、国家标准（P007）：作者举的“客观计算”所依据的东西。",
    "“不善交往”“不通世故”（P009）：作者自称的保护色。",
    "《洛神赋》与“骈四骊六”（P021）：作者用来对比的文学典故与文体。",
    "无爱的人盛赞“技巧”并相信“大家都是人，他能我也能”（P023）：作者描述并反驳的对象（未点名具体个人）。",
    "反驳/改述对象：提问者所问“学理工科是否影响文笔、如何兼顾”（Q001）——作者未按“兼顾”作答。",
   ],
   "conditions": [
    "“理工科的确从统计上讲文笔比较差”（P001）：作者把论断限定为统计层面。",
    "“如果你真的想要‘文笔’好，你唯一需要的只是爱”（P020）：条件句，也是作者给出的唯一正面路径。",
    "“即使是没有文化的人在急切之下的口不择言的粗口，若是出于爱”（P021）：让步＋条件句。",
    "“内有真爱，语言形式的‘粗粝’反而只会增色”（P021）：条件性判断。",
    "“在这个默然不言的动机下”（P012）：作者对该动机“未被明说”的限定。",
    "“这可以算是为你好”（P019）：反讽式让步。",
   ],
   "rhetoric_and_tone": "第二人称对话体，短句与反问交替（“明白了吗？”“问题是，”“所以理工。”“何况‘文笔’呢？”）。以“避难所”“出家避世”“保护色”构成一套隐喻链，把学科选择写成心理防御与自我隔离。语气由冷峻分析转向抒情—训诫（“有爱才会有那种令人动容的力量”“世界上最无价值的，就是雕饰繁复而没有心的垃圾”）。P019“这可以算是为你好。文笔什么的，不重要。”为反讽。结尾“这根本就想错了。”为短促断语。",
   "unresolved_questions": [
    "作者称“理工科的确从统计上讲文笔比较差”，但未给出任何统计来源或衡量方式，待外部核查。",
    "提问者所问的“怎么样可以兼顾”未被正面回答；作者只给出“唯一需要的只是爱”这一条件，未说明兼顾的具体办法。",
    "P004 关于中国社会变迁使“乡土之谊、同志之情、亲族之爱、朋友之义”成为遇害因由的叙述，时间、范围与所指事件本文均未说明，需外部核查（P020 另有“无爱的人不是没有经历过事情”的辨析）。",
    "“对爱幻灭的遗族”的具体代际与群体所指，本文未说明。",
    "“抑文扬理”这一说法的出处与所指时段，本文未说明。",
    "作者以第一人称“我”举例说明回避表态的处境，这些例子是自述经验还是设想的普遍情形，本文未说明。",
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "理工科的确从统计上讲文笔比较差。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "但这不是理工科本身的错，逻辑链条要比这长得多。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这更主要的是因为——理工科是对爱幻灭的遗族们为自己的子女选择的避难所。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "原来信奉的乡土之谊、同志之情、亲族之爱、朋友之义，都在不同的时期反而成了自己遇害的因由。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "人们渴望能置身于人际关系之外，回避一切个人态度的表达。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "无论你问我什么，我只告诉你我自己全无责任的回答。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "譬如你问我喜欢哪一派，我回答你这个没有科学研究，于是可以不答。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "我有充分的理由要么以数据不全能力有限推脱", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "我都是中立而且安全的。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P009", "quote": "我还有“不善交往”“不通世故”的保护色。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P010", "quote": "其实父母们为子女强力安排理工科，是在为他们安排出家避世。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "在这个默然不言的动机下，隐藏了对爱的神秘的恐惧和厌弃。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "不想爱了，怕爱了，也怕被“爱”了。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "所以理工。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "于是理工科里充斥着被默许的、被褒扬的、被暗自期待的对感情、对关切、对“感性”的隔离。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P017", "quote": "没有了爱，连性也乏味到需要快进，何况“文笔”呢？", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P018", "quote": "这才是中国这么多年“抑文扬理”的根源。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P018", "quote": "理工科难出文笔好的青年，是因为文笔好的前提是与安排你学理工的基本初衷相背离的。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P019", "quote": "这可以算是为你好。文笔什么的，不重要。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P020", "quote": "如果你真的想要“文笔”好，你唯一需要的只是爱。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P020", "quote": "无爱的人不是没有经历过事情，而是他们意识不到自己在经历什么、已经经历了什么。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P021", "quote": "即使是没有文化的人在急切之下的口不择言的粗口，若是出于爱，文笔也能压倒骈四骊六的《洛神赋》。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P021", "quote": "内有真爱，语言形式的“粗粝”反而只会增色，并不会被视为“不文”。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P022", "quote": "人们只会因为深受打动而赠你文豪桂冠", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P023", "quote": "无爱的人会盛赞你的“技巧”，因为他们以为那是可以“学”的。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P024", "quote": "这根本就想错了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育社会学", "文笔与写作", "心理与文化批评", "中国当代社会变迁"],
   "issue_candidates": ["理工科与文笔的关系", "学科选择作为心理防御", "回避个人态度表达", "抑文扬理", "爱与写作的关系"],
   "text_function_candidates": ["答疑", "社会—心理成因解释", "评论", "训诫", "抒情议论"],
   "object_candidates": ["理工科", "父母", "爱幻灭的遗族", "《洛神赋》", "自然常数", "国家标准"],
   "working_keywords": ["避难所", "出家避世", "保护色", "全无责任的回答", "中立而且安全", "抑文扬理", "文笔", "爱", "技巧"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P024 共 24 段全部读完，status=read、full_text_checked=true。文本与 lexical 无 divergence。brief 字段为正文开头的截断，与正文重合，不作为独立证据。Q001 属提问者；作者回答了成因，但未就“如何兼顾”给出方法，已在 unresolved_questions 登记。P004 涉及中国社会变迁的历史叙述，本文未给出时间、事件与出处，属待外部核查内容，未作补全。平台为知乎。"
 },
 "0a4606e9": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么有人说艺术和哲学搞多了容易成为废人？作者的答案是：根本原因在于艺术与哲学都是“瘸腿的”——在真、善、美之中，绝大多数知识都要接受“真”的检验，而艺术（作者认为哲学即是思想的艺术）不必接受现实的拷问，其中一大流派更以对一切规则的背叛和对一切现实的超脱为生命源泉；但叛逆现实在任何时候都是危险的选择，九死一生，只有一开始就知道代价并选择“普罗米修斯式的牺牲”的人才不把牺牲算作失败，若为成名而来则必废无疑。提问属提问者；作者未复述“有人说”的具体出处。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总起：根本原因，是因为艺术与哲学都是瘸腿的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "铺垫框架：世间学问无非真、善、美；绝大多数知识都不得不接受真的检验，自然科学、工程技术自不必说，历史学、伦理学、法学、政治学这类社会学科也要通过它们所指导下的族群的命运接受真的约束。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "指出例外：艺术不必接受现实的拷问（哲学被并入艺术，因为哲学即是思想的艺术）；艺术中有一个极大的流派以对一切规则的背叛和对一切现实的超脱为生命源泉，向人提供令人窒息的现实的另一种可能。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "解释现实为何令人窒息：现实在令人窒息之外还宣称自己是唯一的、已经是最美好的（“现实即是合理”），要它的合理与秩序就要接受它的拷打与逼迫；艺术则桀骜地回答存在截然对立却同样美丽者；作者并称艺术常常是狭隘最好的敌人，真总是被美启示出来的。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "转折（标题式两段）：叛逆现实在任何时候都是危险的选择；点亮新世界的荣耀太大，吸引来的贪婪者多基于傲慢、为虚荣而来，选择低级而无效，其尸骨只是为真正的使徒指出死路的路标；这条路九死一生、九成九失败。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "给出例外条件：除非你一开始就明明的知道这代价和风险，知道自己在选择普罗米修斯式的牺牲；那样牺牲就不成其为失败，而是成功了。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "连续追问收束：你真的这么选了吗？你是来牺牲的，还是来成名的？若为成名则必废无疑——哪怕真拿到了真的东西也承受不住那份荣耀；选择名利要么直接失败要么虽胜犹败，选择牺牲要么直接成功要么求仁得仁；末句再问“你怎么选的？”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为艺术和哲学搞多了容易成为废人的根本原因，是因为艺术与哲学都是瘸腿的。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为世间学问无非真、善、美；绝大多数知识都不得不接受真的检验：自然科学、工程技术自不必说，历史学、伦理学、法学、政治学这类社会学科也要通过它们所指导下的族群的命运接受真的约束。", "evidence": ["E002", "E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为艺术例外；之所以不提哲学，是因为哲学即是思想的艺术，哲学家只不过是思想的艺术家。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为与其他学科不同，除实用艺术以外，艺术不必接受现实的拷问；艺术之中有一个极大的流派以对一切规则的背叛和对一切现实的超脱为生命源泉，向人提供令人窒息的现实的另一种可能。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述现实之所以令人窒息：因为它在令人窒息之外，还宣称自己是唯一的、已经是最美好的（“现实即是合理”），要它的合理与秩序就要接受它的拷打与逼迫。", "evidence": ["E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者代艺术作答（拟人化）：艺术桀骜地回答——相信有与现实截然对立却同样美丽的，而在这截然对立同样美丽之外，还有截然对立而同样美丽的。", "evidence": ["E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为在很多时候艺术是狭隘最好的敌人；真总是被美启示出来的；对“现实”的万千“背叛”之中，常有被降下的真实启示。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以标题式短句断言：叛逆现实，在任何时候都是危险的选择。", "evidence": ["E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为点亮新世界的荣耀太大，吸引到的贪婪者太多；他们绝大多数基于傲慢、为虚荣而来，选择往往低级而无效，他们的尸骨只是为真正的使徒指出死路的路标。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这条路的失败几率太大，堪称九死一生——选择了这条路，也就九成九选择了失败。", "evidence": ["E015"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者提出例外条件：除非你一开始就明明的知道这代价和风险，知道你是在选择普罗米修斯式的牺牲。", "evidence": ["E016"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为你选择了牺牲，然后牺牲了，牺牲就不成其为失败，而是成功了。", "evidence": ["E017"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问读者：但你真的这么选了吗？你是来牺牲的，还是来成名的？", "evidence": ["E018", "E019"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者提出条件性判断：若是为成名而来，你必废无疑——哪怕你真的拿到了真的东西，那份荣耀你也是承受不住的；选择名利要么直接失败、要么虽胜犹败，选择牺牲要么直接成功、要么求仁得仁。", "evidence": ["E020", "E021"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以末句追问收束全文：“你怎么选的？”", "evidence": ["E022"]},
    {"claim_id": "C016", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“为什么有人说艺术和哲学搞多了容易成为废人”；作者未复述“有人说”的出处，而是给出自己的成因解释（瘸腿、叛逆现实危险、为成名则必废）。", "evidence": []}
   ],
   "argument_steps": [
    "先给总因：艺术与哲学都是瘸腿的（P001）。",
    "立框架：学问分真善美，绝大多数知识要接受真的检验，社会学科也要通过族群的命运受真的约束（P002-P004）。",
    "指出艺术例外，并把哲学并入艺术（P005-P006）。",
    "说明该例外流派的性质：背叛规则、超脱现实，提供另一种可能（P006）。",
    "解释现实为何令人窒息，并拟艺术之口作答；指出艺术常是狭隘之敌、真由美启示（P007-P009）。",
    "转折：叛逆现实任何时候都危险，荣耀吸引虚荣者，其尸骨成为路标，九死一生（P010-P013）。",
    "给出例外：预先知道代价并选择普罗米修斯式牺牲者，牺牲即是成功（P014-P015）。",
    "以连续追问收束：为牺牲还是为成名；为成名者必废无疑；两种选择的结局；末句再问（P016-P019）。"
   ],
   "concept_usage": [
    {"term": "瘸腿的", "meaning": "作者用来形容艺术与哲学：它们不必（或被认为不必）接受“真”的检验，因而在真善美三足中缺一足。", "evidence": "P001、P005", "ambiguity": "属比喻性论断，作者未给出“瘸腿”的判定标准，也未说明实用艺术为何除外。"},
    {"term": "现实即是合理", "meaning": "作者引作现实自我宣称的口径：现实以其唯一性自证为最美好，要求人接受它的秩序与拷打。", "evidence": "P007", "ambiguity": "作者加了引号但未注明出处（该语式与黑格尔—恩格斯语境相关，本文未说明）。"},
    {"term": "背叛/超脱", "meaning": "作者描述艺术中一大流派的生命源泉：对一切规则的背叛与对一切现实的超脱。", "evidence": "P006", "ambiguity": "“一切规则”“一切现实”的范围与例外，本文未说明。"},
    {"term": "普罗米修斯式的牺牲", "meaning": "作者用来指预先知道代价和风险仍然选择叛逆现实的那种牺牲。", "evidence": "P014", "ambiguity": "属典故性比喻，本文未展开普罗米修斯神话本身，也未说明牺牲的具体内容。"},
    {"term": "废人", "meaning": "本篇回应提问中的“废人”：作者把它解释为“为成名而来却承受不住”的必废结局，而非泛指从事艺术与哲学的人。", "evidence": "P012、P018", "ambiguity": "作者未给出“废”的具体标准（成就、生计还是人格），也未说明“搞多了”的限度。"},
    {"term": "真的东西", "meaning": "作者用来指艺术叛逆者可能真正获得的东西（与荣耀相对）；即使拿到它，为名利而来者也承受不住。", "evidence": "P018", "ambiguity": "“真的东西”的所指本文未说明。"}
   ],
   "examples_and_targets": [
    "真、善、美三分（P002）：作者自设的学问框架。",
    "自然科学、工程技术、历史学、伦理学、法学、政治学接受真的检验/约束（P003、P004）：作者举的学科例。",
    "“现实即是合理”这一现实的自称口径（P007）：作者拟现实之口，非引用具体著作。",
    "艺术流派桀骜的回答（P008）：作者拟艺术之口的修辞。",
    "贪婪者、虚荣者与“真正的使徒”，以及他们的尸骨成为路标（P012）：作者的比喻材料。",
    "普罗米修斯式的牺牲（P014）：作者引用的神话典故。",
    "名利与牺牲两条路的结局对照（P018）：作者构造的价值对照。",
    "被反驳/被解释对象：提问者所说的“有人说艺术和哲学搞多了容易成为废人”（Q001），作者把“废”重新解释为“为成名而来者必废”。"
   ],
   "conditions": [
    "“除实用艺术以外”（P006）：作者对“艺术不必接受现实的拷问”这一断言的例外限定。",
    "“若是后者”（P018）：指“来成名的”，为条件句。",
    "“除非，你一开始就明明的知道这代价和风险”（P014）：例外条件。",
    "“哪怕你真的拿到了真的东西”（P018）：让步条件。",
    "“在任何时候”（P011）：作者对“叛逆现实是危险选择”的时间范围强调。",
    "“这个几率太大，堪称九死一生”（P013）：概率性限定。"
   ],
   "rhetoric_and_tone": "短篇议论，警句化、格言化。以“但是，”与“叛逆现实，在任何时候都是危险的选择。”两个单行段落作标题式转折（P010、P011，lexical 标为 heading）。大量拟人：现实“狞笑着对人说”，艺术“桀骜的回答”。排比与递进（“在这截然对立同样美丽的之外，还有截然对立而同样美丽的”）。结尾由陈述转为对读者的连续追问（“但你真的这么选了吗？”“你是来牺牲的，还是来成名的？”“你怎么选的？”），带训诫与逼问色彩。全文未点任何具体艺术家或作品名。",
   "unresolved_questions": [
    "提问者所用的“有人说”未给出处，作者也未复述该说法的原貌，只给出自己的成因解释。",
    "P007“现实即是合理”未注明出处，其与常见哲学命题的关系本文未说明，待外部核查。",
    "P014“普罗米修斯式的牺牲”未展开所指，牺牲的具体内容与代价本文未说明。",
    "作者称“艺术之中有一个极大的流派”，但未点名该流派或代表人物、作品，读者无法核实其范围。",
    "作者未说明“搞多了”的限度，也未讨论从事艺术与哲学而未成名者的具体处境，仅给出“九死一生”的比例（无来源）。",
    "P018“哪怕你真的拿到了真的东西”中的“真的东西”所指不明，本文未说明。",
    "P005 把哲学等同于“思想的艺术”是作者的界定，本文未说明该界定与通常哲学学科的关系。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "根本原因，是因为艺术与哲学都是瘸腿的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "世间学问，无非真、善、美。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "绝大多数知识都不得不接受真的检验。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "也要通过它们所指导下的族群的命运接受真的约束", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "但是艺术例外。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "因为哲学即是思想的艺术。哲学家只不过是思想的艺术家。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "除实用艺术以外，艺术不必接受现实的拷问。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P006", "quote": "以对一切规则的背叛和对一切现实的超脱为生命源泉", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P007", "quote": "现实即是合理。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P008", "quote": "我相信有与你截然对立却同样美丽的。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P009", "quote": "在很多时候，艺术是狭隘最好的敌人。真总是被美启示出来的。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P011", "quote": "叛逆现实，在任何时候都是危险的选择。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P012", "quote": "他们之中绝大多数都是基于傲慢，为虚荣而来，他们的选择往往是低级而无效的。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P012", "quote": "他们的尸骨只是为真正的使徒指出死路的路标。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P013", "quote": "这个几率太大，堪称九死一生。选择了这条路，也就九成九选择了失败。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P014", "quote": "除非，你一开始就明明的知道这代价和风险，知道你是在选择普罗米修斯式的牺牲。", "relation": "qualifies"},
    {"key": "E017", "paragraph_id": "P015", "quote": "你选择了牺牲，然后牺牲了，牺牲就不成其为失败。而是成功了。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P016", "quote": "但你真的这么选了吗？", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P017", "quote": "你是来牺牲的，还是来成名的？", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P018", "quote": "若是后者，你必废无疑", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P018", "quote": "选择名利，要么你直接失败，要么你虽胜犹败。选择牺牲，要么你直接成功，要么你求仁得仁。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P019", "quote": "你怎么选的？", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P010", "quote": "但是，", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术哲学", "学问分类（真善美）", "价值论", "人生选择"],
   "issue_candidates": ["艺术与哲学是否为废人之因", "艺术是否接受真的检验", "叛逆现实的风险", "为牺牲与为成名的区别"],
   "text_function_candidates": ["答疑", "议论", "警句体", "训诫"],
   "object_candidates": ["艺术", "哲学", "实用艺术", "现实", "普罗米修斯", "真正的使徒"],
   "working_keywords": ["瘸腿的", "真善美", "现实即是合理", "背叛", "超脱", "叛逆现实", "九死一生", "普罗米修斯式的牺牲", "成名", "废"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P019 共 19 段全部读完（正文 794 字），status=read、full_text_checked=true。文本与 lexical 无 divergence；P010、P011 两段在 lexical 中标为 heading（“但是，”与“叛逆现实，在任何时候都是危险的选择。”），其余为 body。brief 字段为正文开头的截断，与正文重合，不作为独立证据。Q001 属提问者；“有人说”的出处本文未给出，作者的解释属其本人判断，已在 unresolved_questions 登记。平台为知乎。"
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
