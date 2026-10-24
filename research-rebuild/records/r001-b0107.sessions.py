# -*- coding: utf-8 -*-
"""批次 r001-b0107 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0107.sessions.py            # 写 out/r001-b0107.out.jsonl
  python3 records/r001-b0107.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0107"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0107.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "ea9197ca": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）问如何评价知乎女权大V @战斗力旺盛的伯爵 被平台永久禁言。作者不把该处置当作自己的胜利，也不评判伯爵言行本身的是非，而是借此事作自我告诫：掌有影响力者如何对待附在荣耀上的“公器”，旁观者应如何自肃；同时声明自己无条件支持当事人走规范程序报案、起诉与申诉，并对其人寄予劝勉。提问者的评价诉求与作者的回答重心不同，作者明言自己不代表最终正义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "开篇定调：把对方失足当作自己的胜利是对胜利的误解；此事应引起“观者的自肃”；提出公器命题与“公事无私怨”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "逐句解释自提的公器命题；以伯爵为例，说明其长期积累的人望所形成的关注与影响力，是关注其主张的人借给他的公器。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "公器是借给事业而非借给个人的；动用时难以分辨为公为私，故不要轻信自己的判断，应尽可能保守、尽可能不用。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "人有火性与傲气，可能因报复冲动悄悄移动准绳并给自己授权；既然自己无法分辨，用得越多越不祥，如同仪表失灵的船。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "出头说话要承受压力乃至生命威胁，只有不出头才绝对安全；拿可能丢命的事图虚荣和权利逻辑不通，出头必须是为远超十个百个人的公事。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018"], "summary": "公事不结私怨；以银行柜员当班挨骂为例，应办业务而不是记住客户以求回击。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025"], "summary": "澄清“观者自肃”：观者指作者自己这名旁观者，不是自觉在实施正义的伯爵批判者；作者自承也常盗用公器，是五十步笑一百步。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031"], "summary": "作者只间接看到片段、无精力细查，无把握判断伯爵是否真的如此；但那不是自肃的要害；以邻家失火应重思自家火灾隐患为喻；作者自认无资格、无权柄、无条件当法官。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034"], "summary": "无条件支持任何人走规范程序报案起诉，该权利不以“报案人正确或正义”为前提；反对要求先自证正义才承认权利；对胜诉败诉本身无倾向。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P035", "P036", "P037"], "summary": "支持向知乎管理员寻求裁决，因加入知乎时已通过用户决议自愿授权；作者自认处置过重（前纵而后酷），但签字同意的程序结果不可因不合己意而出尔反尔；愿赌服输。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040"], "summary": "声明自己不代表最终正义，以上本质上是自警；以“错了我也不改，md”收束解释部分。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P041", "P042", "P043", "P044"], "summary": "若放不下 ego 就不要伸手接荣耀与绑在其上的权力；接了就要忍人所不能忍、不能再指望“普遍人权”；荣耀的负担沉重，获得荣耀应被视为不幸的损失。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "直接对伯爵进言：希望不因挫折放弃追求，追求的正义性没问题而问题在方法；真诚的错误是正确的错误；应甘做轮下的铺路石而非争当时代的驾驶员或车轮。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063"], "summary": "回应密集提醒其支持对象劣迹者：反对“分清敌我然后仇杀”的逻辑；惩罚不等于不原谅、反对不等于停止帮助；必须学会原谅，原谅是为不值得原谅的人准备的，也是救自己。", "role": "rebuttal"},
    {"unit_id": "U015", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068"], "summary": "不在乎伯爵是否真如描述，那不影响这些看法；问对方“想要人改，还是想要人死”；写作真正指向的是时过境迁后仍会看到这些话的读者，纠结作者“站哪边”是失焦。", "role": "conclusion"},
    {"unit_id": "U016", "paragraph_refs": ["P069"], "summary": "末尾孤句“女权到底是指什么权利？”，未与上文衔接（语料尾部片段，lexical 结构未覆盖）。", "role": "open_question"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把对方的失足摔倒当作自己的胜利或武勋，显然误解了胜利，也不会让人肃然起敬。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "荣耀附带权力，任何权力本质上都是公器；对待公器宜戒慎恐惧、非不得已而用之，不为公事而擅用则不祥。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正值得人拼命的只有天下公事；公事就是公事，不要结私怨。", "evidence": ["E004", "E011"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以伯爵为例：其扛旗日久所集中的人望带来关注与荣耀，这些关注形成的影响力实际上是关注其主张的人借给他的公器。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "公器是借给人为事业服务的，不是借给人为自己服务的，而动用时到底为公为私极多时候难以分辨。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要轻易信任自己的判断，要尽可能保守，实践起来就是尽可能不动用公器；既然自己无法分辨是否公器私用，用得越多自然越不祥。", "evidence": ["E007", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人都有火性与傲气，自觉足够公正的判断很可能因报复冲动而悄悄移动准绳，从而给自己授予了动用公器的理由。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出头说话会承受压力甚至威胁精神与实体生命，只有不出头才绝对安全；拿可能丢掉命的事图虚荣和权利逻辑不通，故出头必须是为远超十个百个人的公事。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所说的“观者自肃”之“观者”指作者自己这名旁观者，而非自觉在实施正义的伯爵批判者；作者自承也常盗用公器，不过是五十步笑一百步。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者只是间接看到一句半段、无兴趣层层翻找，坦白说自己对伯爵是否真的如此并无把握判断。", "evidence": ["E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些看法是否为“伯爵问题的正确概括”并非自肃的要害；看到邻家失火应把自己房子的火灾隐患重新思考一遍，这才是头等重要。", "evidence": ["E016", "E017"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者在此事上既无资格、无权柄、也无条件充当合格的法官。", "evidence": ["E018"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无条件支持任何人出于自认合理的原因走规范程序报案起诉：该权利不以“报案人一定正确或正义”为前提；反之要求先自证正义才承认权利，是荒谬的无知与真正的剥夺。", "evidence": ["E019", "E020"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "支持自觉受害之人向法庭及知乎管理员寻求裁决，但对当事人胜诉或败诉本身并无倾向。", "evidence": ["E021"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者个人认为知乎处置过重（前纵而后酷），但那是各人签字同意过的程序正义的执行结果，不可因结果不合己意而出尔反尔。", "evidence": ["E022", "E023"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大丈夫行事应愿赌服输、挨打立正；不满归不满、认账归认账，输打赢要不可取。", "evidence": ["E024"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者声明自己不代表任何最终正义，以上本质上是自己对此事的自警。", "evidence": ["E025"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若放不下 ego、割舍不了荣耀与权力，就不要伸手去接；接了就要做好忍人所不能忍的准备，不能再指望与普通人付一样的价钱。", "evidence": ["E026", "E027"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "荣耀的负担沉重到足以让明白人为获得它而哀叹；“获得荣耀”应被视为值得同情、应当追悔的不幸损失，而非值得庆贺的命运馈赠。", "evidence": ["E028"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对伯爵的劝勉：追求的正义性没有问题，问题在于做事的方法；希望他不至于因这次挫折放弃追求。", "evidence": ["E029"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正造成改变的总是甘做轮下铺路石、宁可让时代忘记的人，而不是争当时代的驾驶员或车轮的人。", "evidence": ["E030"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "惩罚不意味着不原谅，若不是为了原谅，惩罚只是另一种办了证的作恶；反对也不意味着停止帮助，若不是出于帮助，反对不过是化了妆的迫害。", "evidence": ["E031", "E032"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不从“分清敌我，然后仇杀”式的嗜血强迫中解脱，会毁灭自己的前途与一切健康亲密关系的可能。", "evidence": ["E033"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须学会原谅：原谅从来是为“不值得原谅的人”准备的，原谅别人其实是自己在救自己。", "evidence": ["E034", "E035"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者写作真正指向的不是所举事例里的甲方或乙方，而是时过境迁后仍会看到这些话的读者；满心只想作者“站哪边”是失焦离题。", "evidence": ["E036"]}
   ],
   "argument_steps": [
    "以“这就以为算胜利了”否定理所当然的胜利情绪，提出应引起观者的自肃（P001-P002）",
    "给出总命题：荣耀附带权力，权力本质是公器，宜戒慎恐惧、非不得已而用之；不为公事勿擅用（P003）",
    "给出配套命题：真正值得拼命的是天下公事，公事无私怨（P004）",
    "声明下面逐句解释该段话（P005）",
    "定义：关注与荣耀的关系——以伯爵集中的人望为例，指出影响力是关注者借出的公器（P006-P007）",
    "限定公器用途：借给事业而非借给个人，动用时难以分辨为公为私（P008-P009）",
    "行动建议：不要轻信自己的判断、尽可能保守、尽可能不用（P010）",
    "理由：人有火性傲气，可能因报复冲动移动准绳而自我授权（P011）",
    "推论：无法自辨则用得越多越不祥；以仪表失灵之船为类比（P012）",
    "重申前提：值得拼命者只有天下公事（P013）",
    "理由：出头会承受压力乃至生命威胁，只有不出头绝对安全，故出头须为远超十百人的公事（P014-P015）",
    "重申并解释：公事无私怨，以银行柜员挨骂为例（P016-P018）",
    "自问自答澄清“观者自肃”所指：是作者自己，自承亦常盗用公器、五十步笑一百步（P019-P025）",
    "让步与限定：只看到片段、无把握判断伯爵是否如此；但这不是自肃要害（P026-P027）",
    "类比：邻家失火应重思自家隐患，而非详查对方起火原因（P028-P029）",
    "自认无资格、无权柄、无条件当法官（P030-P031）",
    "转入权利主张：无条件支持走规范程序报案起诉，不以报案人正确为前提（P032）",
    "反驳：要求先自证正义才承认权利是荒谬的剥夺；把这种支持当作赞同其正义性是强加私意（P033）",
    "支持向法庭与知乎管理员寻求裁决，但对胜败无倾向（P034-P035）",
    "让步：自认知乎处置过重，但程序结果须认账（P035）",
    "引出态度准则：愿赌服输、挨打立正（P036-P037）",
    "免责声明：不代表最终正义，以上是自警（P038-P040）",
    "条件性劝告：放不下 ego 就不要接荣耀与权力；接了则须忍人所不能忍、放弃“普遍人权”的指望（P041-P043）",
    "结论性判断：荣耀是负担而非馈赠，获得荣耀应视为不幸的损失（P044）",
    "直接呼告当事人：不要放弃追求，方法有问题而非追求有问题（P045-P049）",
    "比喻劝勉：不要争当驾驶员或车轮，要甘做铺路石（P050-P053）",
    "回应反驳意见：反对“分清敌我然后仇杀”的逻辑，主张惩罚与原谅、反对与帮助可以并存（P054-P056）",
    "警告：嗜血强迫的恶习会毁灭前途与亲密关系（P057-P059）",
    "行动建议：必须学会原谅，原谅是为不值得原谅者准备的，是自救（P060-P063）",
    "消解事实争议：不在乎伯爵是否真如描述，那不影响这些看法（P064）",
    "反问与收束：想要人改还是想要人死；写作对象是未来的读者而非当事双方（P065-P068）",
    "末尾孤句留问：女权到底是指什么权利？（P069）"
   ],
   "concept_usage": [
    {"term": "公器", "meaning": "荣耀所附带的、由众人关注与信任借出的影响力；应服务于事业而非个人。", "evidence": "P003/P007/P009", "ambiguity": "公器的授予、范围与收回机制未作界定。"},
    {"term": "观者自肃", "meaning": "旁观者（首先是作者自己）借他人之失检讨自身，而非对当事人实施审判。", "evidence": "P002/P023/P029", "ambiguity": "作者以自问自答方式澄清，未给出可操作判准。"},
    {"term": "公事无私怨", "meaning": "为公事行事不应夹带私人恩怨与报复动机。", "evidence": "P004/P017", "ambiguity": "何者算“私怨”在具体情形中的界线未说明。"},
    {"term": "武勋", "meaning": "借指把他人的失足摔倒算作自己的战功。", "evidence": "P001", "ambiguity": "无。"},
    {"term": "前纵而后酷", "meaning": "作者对知乎处置的评价：先前纵容、后来严酷。", "evidence": "P035", "ambiguity": "所指先前纵容的具体情形未说明。"},
    {"term": "普遍人权", "meaning": "接掌荣耀与权力者不能再主张的、对任何人都不过分的一般要求。", "evidence": "P043", "ambiguity": "与作者无条件支持的“当然权利”之间界线未详述。"}
   ],
   "examples_and_targets": [
    "@战斗力旺盛的伯爵：事件当事人；作为“公器”命题的实例，并成为直接进言与劝勉的对象；作者明言不评判其是非",
    "知乎管理员与知乎的处置：被讨论的平台裁决机制；作者自认处置过重但主张程序结果须认账",
    "法庭、报案与起诉：作者主张应无条件支持的规范程序",
    "银行柜员当班挨骂：说明“公事不要结私怨”的类比",
    "仪表失灵的船：类比公器用得越多越危险",
    "隔壁房子起火、电热毯：类比自肃应以他人之失检讨自身隐患，而非详查对方起火原因",
    "“千年妖狐”：作者自称，用于自嘲其隐忍与自审未必可靠",
    "时代的驾驶员、时代的车轮、轮下的铺路石：劝勉性的比喻材料",
    "密集提醒其人劣迹者：被反驳的对手观点来源（转述，非具名）",
    "ego、“别人都可以，为什么我不可以”、“毋庸置疑、无可辩驳的正义”：批评与自嘲所用的概念材料",
    "“女权到底是指什么权利？”：文末孤句提问，指向未展开的话题"
   ],
   "conditions": [
    "若放不下 ego、割舍不了欲望，则不要接荣耀与绑在其上的权力（P041）",
    "若接了荣耀与权力，就必须忍人所不能忍，不能再要求“普遍人权”（P042-P043）",
    "只有不出头才有绝对安全；出头就是拼命（P015）",
    "支持报案起诉以“走规范程序”为限，且不以理由事后被判决支持为前提（P032）",
    "签字同意过的程序（如知乎的用户决议），结果不利也要认账（P035/P037）",
    "作者对伯爵是否真的如此的判断，受限于其只间接看到片段且无精力翻找（P026）",
    "作者自认无资格、无权柄、无条件充当法官（P030-P031）",
    "对伯爵的进言以“如果你能看见”为前提（P046）",
    "自肃的要害在于检讨自身隐患，与对方起火的真实原因无关（P027-P029）"
   ],
   "rhetoric_and_tone": "训诫体与自省体混合：先对提问语境中的“胜利”情绪泼冷水（P001），再以“公器”立论；通篇大量反问与自问自答（P019-P023、P031、P034、P049、P059、P062-P063、P065）；用银行柜员、隔壁失火、仪表失灵的船等通俗类比；自称“千年妖狐”、自比“五十步笑一百步”以自贬，用“错了我也不改，md”的口语粗话消解说教姿态；中段转为直接 @当事人 的劝勉与祝愿，末段把读者指向“将来的人”。整体冷峻、克己、带道德训诫与反讽，同时反复声明不代表正义、不评判事实。",
   "unresolved_questions": [
    "伯爵被永久禁言的具体事由、平台处置依据与经过，正文未提供；作者也声明只看到片段、无把握判断",
    "“公器”的授予、范围与收回机制未界定；“尽可能不用”与公器本应服务于公事之间的操作界线不明",
    "“观者自肃”缺乏可操作判准：如何区分自省与对当事人的审判，正文未说明",
    "作者一方面无条件支持报案起诉的当然权利，一方面主张接掌荣耀者不能再要求“普遍人权”，两者界线未详述",
    "文末“女权到底是指什么权利？”（P069）孤立成段、与上文关系不明；该段为语料尾部片段，未被 lexical 结构覆盖（divergence）",
    "“前纵而后酷”所指知乎此前纵容的具体情形未说明",
    "“错了我也不改，md”是否为拒绝修正的认真表态，语气含混",
    "伯爵是否真的如一些人描述的那样，属需外部核查的事实，正文明确不予裁断"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "把对方的失足摔倒引以为自己的武勋，并不会让人肃然起敬。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "荣耀附带着权力，任何权力在本质上都是公器。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "对待公器，宜戒慎恐惧，非不得已而用之。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "真正值得人拼命的，只有天下公事。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "这些关注形成的影响力实际上是关注ta的主张的人借给他的公器。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "这是借给人为这个事业服务的，不是借给人为自己服务的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P010", "quote": "不要轻易信任自己的判断，要尽可能保守的判断。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P011", "quote": "很可能是因为自己有报复的冲动而悄悄移动了准绳的结果。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "自己到底有没有做这种事既然自己无法分辨，那么用得越多，自然越不祥。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P015", "quote": "所以出头必须是为比自己的生死荣辱更重要的事。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P017", "quote": "公事不要结私怨。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P022", "quote": "是我好吗？", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P024", "quote": "我也同样时常盗用公器！", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P025", "quote": "但是这不过是五十步笑一百步。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P026", "quote": "所以坦白说伯爵是不是真的如此，我其实也并无把握判断。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P027", "quote": "根本就不是“自肃”的要害所在。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P029", "quote": "你要把自己房子的火灾隐患——尤其是你觉得可能是对方失火的诱因的那些方面重新思考一遍", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P030", "quote": "我在这事上其实既无资格、也无权柄、更无条件去当这个合格的法官。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P032", "quote": "都是所有人不可剥夺的当然权利。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P033", "quote": "这本身就是荒谬的无知和一种真正的剥夺。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P034", "quote": "但我对当事人胜诉或者败诉本身并无倾向。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P035", "quote": "坦白说我个人的确认为处置过重，前纵而后酷", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P035", "quote": "不可以因为结果不合己意就出尔反尔。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P036", "quote": "大丈夫行事，愿赌服输，挨打立正。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P038", "quote": "以上本质上是我自己对这事的自警。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P041", "quote": "对待意外落到自己面前的荣耀和绑在这荣耀上的权力，不要伸手去接。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P043", "quote": "你接了比普通人更重的东西，无法再指望和普通人付一样的价钱。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P044", "quote": "“获得荣耀”，是值得人同情、应当追悔和反省何以没能摆脱的厄运", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P047", "quote": "这个追求的正义性没有任何问题，问题在于做事的方法。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P051", "quote": "最后造成了真正的改变的，总是那些甘做轮下的铺路石", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P055", "quote": "若不是为了原谅，惩罚只是另一种办了证的作恶。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P056", "quote": "若不是出于帮助，反对不过是化了妆的迫害。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P057", "quote": "从这里养成的恶习会毫不留情的、超乎你想象的毁灭你的一切前途和一切健康亲密关系的可能。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P060", "quote": "你必须学会原谅——原谅从来都是为“不值得原谅的人”准备的。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P063", "quote": "是你自己在救你自己。", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P067", "quote": "真正指向的从来不是所举事例里的甲方或者乙方，而是将来早已时过境迁之后，仍会看到这些话的读者。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["平台治理与内容审核", "公共影响力与责任伦理", "程序正义与权利", "自我修养与道德训诫", "女权议题（提问语境）"],
   "issue_candidates": ["女权大V被平台永久禁言如何评价", "影响力（公器）的正当使用边界", "报案起诉权的无条件支持", "程序正义与结果认账", "原谅与惩罚的关系", "旁观者的自省与审判之别"],
   "text_function_candidates": ["回应提问", "道德训诫", "自我告诫", "公开进言", "概念解释", "论辩回应"],
   "object_candidates": ["@战斗力旺盛的伯爵", "知乎平台与管理员", "报案起诉与法庭", "公器", "观者自肃", "原谅"],
   "working_keywords": ["公器", "观者自肃", "公事无私怨", "荣耀", "愿赌服输", "前纵而后酷", "铺路石", "原谅"]
  },
  "status": "read",
  "full_text_checked": True,
  "image_checked": False,
  "notes": "无图片节点（skeleton images 为空），故 image_checked=false 不影响 read 判定。语料与 lexical 结构存在分歧：P069“女权到底是指什么权利？”为 text_tail_not_in_lexical 的尾部片段，已在 unresolved_questions 中标注。P006/P008/P013/P016 为 quote 字段节点，是作者复述自己前文语句，非引用他人。提问字段（Q001）属提问者。伯爵被禁言的事由与知乎处置规则、以及“前纵而后酷”所指的具体情形，均需外部核查。"
 },
 "655b3e80": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）问“现代神学研究什么？”，期待的是当代神学的研究议题或分期。作者没有给出议题清单，反而先判定这个问题目前没有太大意义，转而说明传统的神学分期与议题列表为何在现代失效：教会的定义权流散、教牧关切碎片化、神学与宗教研究等学科混淆、研究者身份传承模糊。文末作者把这一局面归为“上帝的意志”，并以后置条件“如果你相信上帝的存在的话”作限定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接否定提问的现实意义；说明过去神学之所以可代代划分，是因为存在“主进程”，当代神学研究的实质是“下一次大公会议的议程”的预备。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "过去神学的可分期性来自教会设定议程、大公会议充当节拍器以及明确的师徒传承；而今天信仰及信仰实践的定义权已很大程度从教会手里流散。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "现代神学以另一种形态进行，多回应小体量教牧团体的需要；南美、非洲、韩国、香港教会关切各异，甚至相距百公里的教会甲乙因面向城市高知或乡村居民而话语体系不通。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "神学研究本身大规模模糊化：首先与社会性宗教研究混淆，研究者自己也分不清是神学、宗教、社会学、人类学还是考古学（以“圣经考古”归属之问为例）。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "其次研究者身份传承模糊化：未必师从神学研究者，退休医生、在任物理学家亦可提出跨宗派甚至跨宗教的神学理论；“上帝不掷骰子”是否算神学结论亦成疑问。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "结论：为现代神学研究划代或确定主要议题列表在逻辑上已欠缺意义；并称这并非人为安排而是上帝的意志，随后以信仰前提作限定。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“现代神学研究什么”这个问题目前没有太大的意义。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以前的神学可以一代一代地分，是因为有一个“主进程”可言；所谓当代的神学研究基本上是“下一次大公会议的议程”的预备。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "今天信仰与信仰实践的定义权，客观来说已经很大程度上从教会手里流散。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "过去神学有集体主攻方向，以教会为先导、大公会议等决议机制为节拍器，并有传承明确的师徒关系，故有分明的“一代接一代”。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代神学研究多是为回应更小体量教牧团体的需要，不同教会关切的问题完全不同，差异大到话语体系不通、会都开不起来。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "神学研究本身大规模模糊化了，首先极大与社会性的宗教研究混淆，研究者自己也未必分得清学科归属。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "研究者的身份传承也模糊化了：现在研究神学的人完全不见得师从另一位神学研究者，未进过修道院的退休医生或在任物理学家提出的跨宗派神学理论是否算神学研究成为疑问。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因此，给现代神学研究划代或确定一个主要议题列表，逻辑上已经欠缺意义。", "evidence": ["E013"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这种局面不是什么人安排的，本身就是上帝的意志——该断言以“如果你相信上帝的存在的话”为条件。", "evidence": ["E014", "E015"]}
   ],
   "argument_steps": [
    "先否定提问：这个问题其实目前没有太大的意义（P001）",
    "前提一：过去神学可代代划分，靠的是“主进程”，即当代研究为下一次大公会议议程作预备（P002）",
    "前提二：这一主进程依托教会先导、大公会议节拍器与明确的师徒传承（P004）",
    "转折：今天信仰及实践的定义权已很大程度从教会手里流散（P003）",
    "由此现代神学转为另一种形态：回应小体量教牧团体的具体需要（P005-P006）",
    "例证：关切差异可小到相距百公里的教会甲乙，话语体系不通（P007）",
    "第二层理由：神学研究本身模糊化（P008）",
    "其一，与社会性宗教研究混淆，学科归属难辨，以“圣经考古”为问（P009-P010）",
    "其二，研究者的身份传承模糊化，以退休医生与在任物理学家为例（P011-P013）",
    "以“上帝不掷骰子”追问是否算神学结论（P014）",
    "结论：划代与确定主要议题列表在逻辑上已欠缺意义（P015）",
    "收束：这不是什么人安排的，本身就是上帝的意志（P016）",
    "限定：如果你相信上帝的存在的话（P017）"
   ],
   "concept_usage": [
    {"term": "主进程", "meaning": "过去神学分期所依托的、由教会主导的统一议程。", "evidence": "P002", "ambiguity": "其具体所指与终止时点未说明。"},
    {"term": "大公会议", "meaning": "提供决议机制、充当神学研究天然节拍器的机构性安排。", "evidence": "P002/P004", "ambiguity": "无。"},
    {"term": "集体主攻", "meaning": "过去神学研究的组织形态：有先导、有节拍器、有明确师承。", "evidence": "P004", "ambiguity": "无。"},
    {"term": "教牧团体", "meaning": "现代神学研究实际回应的、体量更小且关切各异的服务对象。", "evidence": "P006", "ambiguity": "“更小体量”的具体规模未说明。"},
    {"term": "模糊化", "meaning": "作者对现代神学的概括：学科归属与研究者身份传承两方面的界限消失。", "evidence": "P008-P012", "ambiguity": "未给出判断模糊与否的标准。"},
    {"term": "上帝的意志", "meaning": "作者对现代神学碎片化局面给出的神学解释。", "evidence": "P016-P017", "ambiguity": "以信仰前提限定，未进一步论证。"}
   ],
   "examples_and_targets": [
    "大公会议：作为对比基准的历史决议机制（证据性举例）",
    "南美教会、非洲教会、韩国教会、香港教会：关切各异的教牧团体（举例）",
    "相距一百公里的教会甲与教会乙：城市高知与乡村居民取向差异（举例）",
    "“圣经考古”：学科归属之问的例子",
    "退休医生、在任物理学家：研究者身份传承模糊的例子",
    "“上帝不掷骰子”：是否为神学结论的例子（正文未指认其出处，不作补充）",
    "提问者（Q001）：被回应的对象，作者否定其问题的现实意义"
   ],
   "conditions": [
    "结论以“如果你相信上帝的存在的话”为条件（P017）",
    "划代与议题清单“逻辑上已经欠缺意义”是就现代这一时点而言（P015）",
    "现代神学“很多”回应小团体需要、“可以小到”百公里差异——均为程度限定（P006/P007）",
    "“有时候研究者自己也未必真的分得清”——以“有时候”限定学科混淆的范围（P009）"
   ],
   "rhetoric_and_tone": "冷静的学科观察语调。开篇以“其实目前没有太大的意义”直接否定提问，随后用“主进程—节拍器—师承”的机制性说明展开对比；连用反问呈现分类边界失效（“到底是一种历史研究还是一种宗教学研究？还是一种神学研究？”“是否还算是神学研究？”“算不算一种神学结论？”）；结尾转为断言式神学表述，并以“如果你相信上帝的存在的话”这一口语化条件句收束，带戏谑的敬虔感。",
   "unresolved_questions": [
    "未给出“现代神学研究什么”的正面清单，作者明确认为该问题已欠缺意义",
    "“主进程”的具体所指与终止时点未说明",
    "“定义权从教会手里流散”的程度、流向与后果未展开",
    "“上帝的意志”是作者的信仰表述还是修辞，正文以条件句收束，未进一步论证",
    "“上帝不掷骰子”的出处与是否属于神学结论，正文只提问未回答",
    "学科混淆的具体案例与判准未给出；各教牧团体关切的具体议题亦未列举"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "这个问题其实目前没有太大的意义。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "以前的神学一代一代的可以分，是因为有一个“主进程”可言。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P002", "quote": "基本上所谓的“当代的神学研究”，就是“下一次大公会议的议程”的预备。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "定义权已经很大程度上从教会手里流散了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "有提供和设定议程的教会作为先导，有大公会议等等决议机制作为天然的节拍器", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "很多是为了回应更小体量的教牧团体的需要", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "两边说话的话语体系都完全不一样——连会都不见得开得起来。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "首先就极大的和社会性的宗教研究混淆了。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "“圣经考古”，到底是一种历史研究还是一种宗教学研究？还是一种神学研究？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "现在研究神学的人，完全不见得是师从另一位神学研究者。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "由一天修道院也没有进过的退休医生、甚至在任的物理学家提出的跨宗派甚至跨宗教的神学理论，是否还算是神学研究？", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "典型的，“上帝不掷骰子”，算不算一种神学结论？", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P015", "quote": "因此，给现代神学研究划代也罢，确定一个主要议题列表也罢，逻辑上已经欠缺意义了。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P016", "quote": "但你要记住——这不是什么人安排的，这本身就是上帝的意志。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P017", "quote": "如果你相信上帝的存在的话。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与神学", "学术史与学科分类", "教会制度"],
   "issue_candidates": ["现代神学研究什么", "神学分期是否还有意义", "神学与宗教研究、社会科学的学科边界", "信仰定义权的转移"],
   "text_function_candidates": ["回应提问", "学科观察", "否定式回答", "分类学讨论"],
   "object_candidates": ["大公会议", "教牧团体", "神学研究者", "圣经考古", "上帝"],
   "working_keywords": ["主进程", "大公会议", "定义权", "集体主攻", "身份传承", "模糊化", "上帝的意志"]
  },
  "status": "read",
  "full_text_checked": True,
  "image_checked": False,
  "notes": "无图片节点（skeleton images 为空），image_checked=false 不影响 read 判定。无 text/lexical 分歧（divergence=false）。提问字段（Q001）属提问者，作者的否定性回答不等于提问者的立场。文中“上帝不掷骰子”未指认出处，属需外部核查的事实，本记录未据外部知识补写。"
 },
 "28ea871e": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）问“如何根除赌瘾？”。作者借“包钢的事”（并注明其“投资失败”之说只是“据说”，未作确认）切入戒赌话题。作者先批评流行的两条劝诫（不要冒自己不能承受的风险、不要做与自己能力不匹配的事情）无效并为赌瘾埋下祸根，再提出“永不期待超出自己时薪的收益”及四条执行法则，进而将其论证为以历史事实为锚、可用严谨数学算法执行的原则（等同“不劳不获”），并说明自由安放之处。全篇以“（未完，待续）”收尾，属未完成文本。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "由包钢之事引出戒赌；家长暗抱投机暴富的不甘、不用“不劳不获”而以“不要冒不能承受的风险/不要做能力不匹配的事”教子女，反为赌瘾埋祸根，因这两条只诉诸当事人的良好判断。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "小A案例（风险承受分支）：自认能承受百万风险，奋力一搏失败、败露后社会关系崩溃；结局A自杀（不多谈）；结局B家人卖房卖车卖信用兜底，小A反而发现原判断“的确是对的”、承受力比想象强，新信心再发育并开始第二轮拼搏；该法更不能接受小A从此完全不自信这另一种结局。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "“能力不匹配”分支同样无效：没吃过惨烈教训者永远觉得“谁说我能力不匹配”，阻止不了第一次大错；故两种最流行的抑制投机策略其实无效。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "提出原则“永不期待超出自己时薪的收益”，并给出四条执行要点：无经验时不期待0以上报酬；收益反复稳定超出或低于原时薪期待时相应调高或调低；超出估计部分视为需“消毒”的意外刺激，匿名捐出至少十分之一；与劳动量无关的长期资本性收入视为不可用于个人消费的“社会信托资产”。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "要求在一切收益上坚决、机械地执行，立为个人信条并作家族原则传承；这会根除因投机毁灭的可能，因为它根除了“投机”本身，其实就是“不劳不获”。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "不劳不获之所以重要在于尺度客观：用历史数据而非自我估量；虽有取样修正与“意外收入”的弹性，参考仍客观；不可更改、易于确认的基本事实具有神性，应作确定性之锚与数学方法刚性绑定。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "“不可更改”源于历史的无可更改性，“易于确认”是唯物原则最保守最基要的实践，严谨数学算法即科学；信从这三位一体是一种主义，本质上即科学历史唯物主义，在另一语境即对神的话语的服从。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059"], "summary": "自问是否把一切交给公式、自由何处安放；答自由栖息两处：一是技术性的算法参数决定（相机类比：取景、感光度、焦距、光圈、快门由你决定），二是更高层面可选择和设计算法。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "设计算法的要点：数学严谨、输入数值提取机制显而易见且难被情绪左右；必须足够简单；警惕故意复杂化以拒绝他人检验（“聪明”的蠢人以此绑架结果）；简单算法便于他人给出第二观点，可用“我有一个朋友”法与“hypothetically”剥离隐私或请陌生人验算；越简单越不易自欺，无限调参重建即背弃原则。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P071", "P072", "P073", "P074", "P075", "P076", "P077"], "summary": "“收入预期”不只是数字，而有连带实践：不计划超预期部分收入的用途、不计较其落空、不为保证这笔收入承担风险，因为这笔钱本来不存在。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P078", "P079", "P080", "P081"], "summary": "人们承担过大风险的根本原因，是假设一次尝试能获得远超历史数据的预期收入，用未获得过的想象收入抵偿现实风险与保险成本；按“这笔钱不存在”规划决策管理情绪是定锚所在。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090"], "summary": "会有无数声音嘲笑你保守、不聪明、缺少远见并炫耀成就，不要为其所动；过度冒险者终会在最后一次输光本金与信用并陷入巨额债务，往往不悔改而为翻本铤而走险，最终连同所有信任他们的人一起被拖进地狱。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P091"], "summary": "正文以“（未完，待续）”结束，未完结。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "author", "modality": "qualified", "statement": "作者据“包钢的事”切入戒赌问题，并注明该事被称为“投资失败”只是据说，未作确认。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家长暗抱“不能放弃投机暴富的一切可能”的不甘，不用“不劳不获”教育子女，而用“不要冒不能承受的风险”“不要做能力不匹配的事”抑制赌博，恰恰为赌瘾埋下祸根。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那两条劝诫没有提供判断“不能承受”和“与能力不匹配”的方法论，而是诉诸当事人自己的良好判断。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以小A的风险承受分支为例：家人兜底反而使原判断“的确是对的”得到验证，小A会意识到承受力比想象强，新的信心再次发育并开始第二轮拼搏。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该戒赌法更深的失败在于它也不能接受另一种结局——小A从此对自身承受风险的能力完全不自信；而这样一个被“精神阉割”的小A也无法被父母、配偶与自己接受。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“能力不匹配”法同样无效：没吃过足够惨烈教训的人永远觉得“谁说我能力不匹配”，阻挡不了第一次大错，也拿不出办法遏止其再次错误地自认能力足够。", "evidence": ["E009", "E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这两种最流行的抑制投机的策略其实是无效的。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应记住的原则是“永不期待超出自己时薪的收益”，并按四条要点执行：无经验时不期待0以上报酬；收益反复稳定超出或低于原时薪期待时相应调高或调低；超出估计的部分视为需“消毒”的意外刺激，匿名捐出至少十分之一给完全无利害关系的人；与劳动量无关的长期资本性收入视为不可用于个人消费的“社会信托资产”。", "evidence": ["E012", "E013", "E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要坚决、机械地在一切收益上执行，立为个人信条并作为家族原则传承；这会从根本上根除因投机毁灭的可能，因为它根除了“投机”本身，其实就是“不劳不获”。", "evidence": ["E016", "E017", "E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不劳不获之所以重要，是因为其尺度客观性大得多：衡量合理期望用历史数据而非自我估量；虽有取样修正与“意外收入”的弹性，其参考仍来自不可更改、易于确认的基本事实。", "evidence": ["E019", "E020"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不可更改、易于确认的基本事实具有神性、是一种神的低语，应作为高于一切的确定性之锚，并用由不得自己篡改的完备数学方法把一切估计与之刚性绑定。", "evidence": ["E021", "E022"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不可更改”根源于历史的无可更改性，“易于确认”是唯物原则最保守也最基要的实践，严谨的数学算法即联结自我与唯物历史的理性工具，其另一名字就是科学。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信从这样的三位一体可得到安全与发展的最大平衡，这是一种主义，本质上即科学历史唯物主义；在另一语境中即人对神的话语的服从，实践方法一致、效果预期相等、精神本质一体两面。", "evidence": ["E026", "E027", "E028"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的自由并未被真正剥夺：它存在于算法参数的决定上（如相机取景、感光度、焦距、光圈、快门的选择），并在更高层面存在于对算法的选择和设计上。", "evidence": ["E029", "E030", "E031"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "设计算法的方法必须在数学上严谨、不受主观判断干扰，输入数值的提取机制显而易见且难以被情绪左右，并且必须足够简单。", "evidence": ["E032", "E033"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "故意设计无人能理解的复杂算法，实际上拒绝了任何他人有效检验的可能；“聪明”的蠢人以此把算法堆到无法检验、用自己的意志绑架结果，这还不如赤裸裸的狂妄和贪婪。", "evidence": ["E034", "E035", "E036"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "算法足够简单时，知情且关心你的人能轻松给出有效的第二观点；可用“我有一个朋友”法和“hypothetically”剥离隐私，或向陌生人请求代为验算以避开利害关系；这种无利害关系的第二、第三观点对抑制罪性本能有极大实践意义。", "evidence": ["E037", "E038"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越是简单越不易自欺；一旦无限允许自己调整参数和重新建模，事实上就已经背弃了用历史来主导自己预期这一基本原则。", "evidence": ["E039", "E040"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“收入预期”不只是一个数字，而有一系列连带实践：不计划超预期部分收入的用途、不计较其落空、不为保证这笔收入承担风险，因为这笔钱本来就不存在。", "evidence": ["E041", "E042"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们承担过大风险的根本原因，正是假设自己可以在一次尝试中获得远超历史数据的预期收入，用没获得过的想象收入抵偿现实风险与保险成本；始终按“这笔钱不存在”规划决策管理情绪，是避免被 wishful thinking 卷入地狱的定锚所在。", "evidence": ["E043", "E044"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "会有无数声音嘲笑你保守、不聪明、缺少远见并炫耀成就，不要为其所动；过度冒险者总会在最后一次输光本金与一切信用并陷入巨额债务，往往不悔改而为翻本越出世俗所不能容的界限，最终连同所有敢于信任他们的人一起被拖进地狱。", "evidence": ["E045", "E046", "E047"]}
   ],
   "argument_steps": [
    "以“包钢的事”（据说投资失败）引入戒赌话题（P001）",
    "指认家长的真实心态：暗抱投机暴富的不甘，用“风险承受”与“能力匹配”代替“不劳不获”（P002-P003）",
    "判断：这恰恰为赌瘾埋下祸根（P004）",
    "理由：两条劝诫无判断方法，只诉诸当事人的良好判断（P005）",
    "设问“不能承受的标准是什么”，引出小A案例（P006-P008）",
    "案例推进：奋力一搏失败→高估承受力→败露、家庭与社会关系崩溃（P009-P011）",
    "支线：结局A自杀，作者声明先不多谈（P012）",
    "主线：结局B家人兜底，小A反而验证了原判断、重获信心并开始第二轮拼搏（P013-P018）",
    "更深失败：该法也不接受小A从此完全不自信这另一种结局（P019-P020）",
    "平行检验“能力不匹配”法：阻止不了第一次大错，也无法遏止再次误判（P021-P023）",
    "结论：两种最流行的抑制投机策略无效（P024）",
    "给出原则：永不期待超出自己时薪的收益（P025-P027）",
    "展开四条执行要点（P028-P033）",
    "要求坚决机械执行、立为信条与家族原则；等于根除投机本身，即“不劳不获”（P034-P037）",
    "追问不劳不获为何重要：尺度客观，用历史数据而非自我估量（P038-P040）",
    "提升为形而上表述：基本事实具神性、是神的低语，应作确定性之锚并以数学绑定（P041-P042）",
    "解释三项：历史的无可更改性、唯物原则、即科学的数学算法（P043-P045）",
    "合为“三位一体”的主义：科学历史唯物主义，亦即对神的话语的服从（P046-P053）",
    "自我反驳：这是否把一切交给公式、自由何在（P054-P055）",
    "回应：自由在算法参数决定与算法选择设计两处，以相机为类比（P056-P059）",
    "给出设计算法的要求：数学严谨、输入可核、足够简单（P060-P062）",
    "警告故意复杂化：拒绝他人检验、以意志绑架结果（P063-P067）",
    "再申简单之益：不易自欺，防止背弃历史主导预期的原则（P068-P070）",
    "落到收入预期的连带实践：这笔钱不存在（P071-P077）",
    "诊断根源：用想象收入抵偿现实风险，从一开始埋下失控祸根（P078-P081）",
    "收束：不要为嘲笑与炫耀所动，过度冒险者的结局是债务、越界与共同沉没（P082-P090）",
    "标注未完待续（P091）"
   ],
   "concept_usage": [
    {"term": "不劳不获", "meaning": "作者主张的根本原则：以劳动为收益依据，等价于“永不期待超出自己时薪的收益”。", "evidence": "P037/P002", "ambiguity": "“时薪”如何界定（岗位、行业、时期）未详述。"},
    {"term": "时薪期待", "meaning": "以客观历史收益数据衡量、可随长期稳定表现调整的合理收入基准。", "evidence": "P027/P030", "ambiguity": "调整的量化门槛未给出。"},
    {"term": "消毒", "meaning": "对超出估计的意外收益所做的处理：匿名捐出至少十分之一给完全无利害关系的人。", "evidence": "P031", "ambiguity": "为何是十分之一、如何选择受捐者未说明。"},
    {"term": "社会信托资产", "meaning": "与付出劳动量无关的长期资本性收入，视为为公共事业临时保管、不可用于个人消费。", "evidence": "P032", "ambiguity": "“公共事业”的范围与执行方式未说明。"},
    {"term": "确定性之锚", "meaning": "不可更改、易于确认的基本事实，被用作高于一切的判断基准。", "evidence": "P041/P042", "ambiguity": "如何筛选此类事实未给判准。"},
    {"term": "科学 历史 唯物 主义", "meaning": "作者对其原则的自我命名，与“对神的话语的服从”被视为一体两面。", "evidence": "P046-P048", "ambiguity": "“三位一体”所指的三项与宗教语汇的对应关系未严格界定。"},
    {"term": "wishful thinking", "meaning": "以想象收入替代客观数据的心态，作者视为入地狱的诱因。", "evidence": "P081", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "包钢的事（“据说”是投资失败）：引出话题的时事由头，作者未确认其性质",
    "小A：贯穿全篇的虚构/匿名案例人物，用于演示两种劝诫的失效路径",
    "小A的父母与配偶：在结局B中卖房卖车卖信用兜底，作为案例支线",
    "“老黄牛”“一辈子赚死工资”“人无横财不富，马无夜草不肥”“撑死胆大的、饿死胆小的”：家长心态的引用性表述（作者转述其信念）",
    "相机与参数（感光度、焦距、光圈、快门）：说明自由与算法关系的类比",
    "工资单、考卷积分、仓库磅秤读数、流水线视觉传感器计数：合格输入数值的举例",
    "“我有一个朋友”法与“hypothetically”：剥离隐私的实操举例",
    "假药与甜药：对伪装成科学算法的做法的比喻",
    "“爱拼才会赢”“有赌未为输”“胜利属于坚持的人”：被作者判定为有害的流行说法（引用并反驳）",
    "尸体从上游漂来、怒马香车醇酒美人：对过度冒险者结局的修辞性描绘",
    "提问者（Q001）：被回应的对象，作者未直接复述其表述"
   ],
   "conditions": [
    "全部论断针对“收益”与“投机”情形，并以“劳动量”为衡量参照（P032/P061）",
    "调高时薪期待的条件是实际收益“反复稳定”超出原期待；反之则需调低（P030）",
    "原则要求“在一切收益上”坚决机械执行，并以家族传承为条件（P034）",
    "算法须满足数学严谨、提取机制显而易见、足够简单三项要求方可采信（P061-P062）",
    "简单算法带来的第二观点，以“知道你的基本事实而对你足够关心的人”为条件（P064）",
    "作者由包钢之事引入，仅称其“据说是‘投资失败’”，未对事件本身作事实认定（P001）"
   ],
   "rhetoric_and_tone": "训诫与布道混合的强断言语调，带黑色幽默与诅咒式警告：以“魔鬼在这里冷笑”“迟早有一天，你会看到ta们的尸体从上游漂来”“一起拖进地狱”等形象化威吓推进；大量反问（“不能承受的标准是什么？”“难道这样一个被精神阉割了的小A就真的能让父母、配偶，包括ta自己接受吗？”“治不了病，甜有什么意义？”）；用“小A”的推演式案例与相机、假药等类比说明抽象原则；夹杂文言式断语“君子疾夫舍曰欲之而必为之辞”与“科学 历史 唯物 主义”的分词排版；结尾以“（未完，待续）”明示未完成。",
   "unresolved_questions": [
    "P024 出现“难以戒除毒瘾”一词，按上下文应指赌瘾，疑为原文笔误或语料问题，需外部核查（本记录未改动原文）",
    "P077“这笔钱本里就不存在”疑为“本来”之误，属原文用字问题",
    "“时薪期待”的界定与调高/调低的量化门槛（“反复稳定”的标准）未给出",
    "“消毒”捐出十分之一的依据、受捐对象与验证方式未说明",
    "“社会信托资产”所指“某种公共事业”的范围与托管机制未说明",
    "如何筛选“不可更改、易于确认的基本事实”未给判准",
    "“科学 历史 唯物 主义”与“对神的话语的服从”如何在实践上等同，正文未展开论证",
    "包钢之事的具体经过与该“投资失败”说法的真实性，属需外部核查的事实",
    "正文以“（未完，待续）”结束，后续内容缺失"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "最近有包钢的事，据说是“投资失败”，借这个问题，来讲一下戒赌问题。", "relation": "context"},
    {"key": "E002", "paragraph_id": "P002", "quote": "ta们常常暗地里抱着“不能放弃投机暴富的一切可能”的不甘", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "但这恰恰是为赌瘾埋下了祸根。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "而是诉诸当事人自己的良好判断。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P015", "quote": "但是，小A会发现，原来ta最初那个“能承受一百万亏损”的判断，的确是对的。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P018", "quote": "或迟或早，新的“我承受得了这个风险”的信心会再次发育出来，开始第二轮“拼搏”。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P019", "quote": "在于它甚至不能接受这故事的另一种结局——小A从此对自己承受风险的能力完全的不自信", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P020", "quote": "难道这样一个被精神阉割了的小A就真的能让父母、配偶，包括ta自己接受吗？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P021", "quote": "ta没吃过足够惨烈的教训，永远会觉得“谁说我能力不匹配”。这根本阻止不了ta犯下第一次大错。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P022", "quote": "又拿什么去遏止ta不再次错误的认为自己“能力足够”呢？", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P024", "quote": "所以，这两种最流行的抑制投机的策略其实是无效的。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P027", "quote": "永不期待超出自己时薪的收益。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P029", "quote": "1）无工作经验时，不要期待0以上的报酬。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P031", "quote": "3）超出估计的部分视为需要“消毒”的意外刺激，执行“消毒”操作——匿名捐出至少十分之一给完全无利害关系的人。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P032", "quote": "4）任何与付出劳动量无关的长期资本性收入，都要视为不可用于个人消费的“社会信托资产”来处理。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P034", "quote": "要坚决的、机械的，在一切收益上执行。要把这立为个人信条，并且要作为家族原则传承下去。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P036", "quote": "因为它根除了“投机”本身。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P037", "quote": "它其实就是“不劳不获”四个字。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P039", "quote": "因为它的尺度有大得多的客观性——衡量“合理期望”的时侯，它不是使用“自我估量”，而是使用客观得多的历史数据。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P040", "quote": "但是它提供的参考仍然是客观的，来自不可更改的、易于确认的基本事实。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P041", "quote": "不可更改、易于确认的基本事实，是具有神性的事物，它事实上就是一种神的低语。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P042", "quote": "你必须将不可更改、易于确认的事实作为高于一切的确定性之锚来使用", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P043", "quote": "“不可更改”，则根源于历史的无可更改性。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P044", "quote": "“易于确认”，是“唯物原则”的最保守也是最基要的实践。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P045", "quote": "则是联结自我与唯物历史的理性工具，它的另一个名字，就是科学。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P046", "quote": "信从这样的三位一体可以给予自己安全与发展的最大平衡，这是一种主义。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P047", "quote": "这答案的本质上，其实就是科学 历史 唯物 主义。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P048", "quote": "而它在另一语境中，也就是人对对神的话语的服从。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P056", "quote": "你的自由并没有被真正的剥夺。它还栖息在最重要的两处——", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P057", "quote": "第一，技术性的，它存在于算法的参数决定上。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P059", "quote": "第二，在更高的层面，你可以选择和设计算法。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P061", "quote": "1）这方法必须在数学上是严谨的，结果本身不受人的主观判断干扰。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P062", "quote": "2）这方法必须是足够简单的。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P063", "quote": "通过故意引入复杂性，你实际上拒绝了任何其他人能给你有效检验的可能性。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P065", "quote": "一些“聪明”的蠢人才会巧妙的利用自己的“学术能力”去把自己的算法堆积到无法检验，以便用自己的意志绑架结果。", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P066", "quote": "这甚至还不如赤裸裸的狂妄和贪婪，这只是怯懦化而后猥琐化了的狂妄和贪婪。", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P064", "quote": "那么知道你的基本事实而对你足够关心的人就能轻松的给你足够有效的第二观点。", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P065", "quote": "这种无利害关系的、基于纯逻辑运算的第二、第三观点对你有极大的抑制罪性本能的实践意义。", "relation": "supports"},
    {"key": "E039", "paragraph_id": "P068", "quote": "第二，越是简单，越是不易自欺。", "relation": "supports"},
    {"key": "E040", "paragraph_id": "P068", "quote": "你在事实上就已经背弃了用历史来主导自己的预期这一基本的原则。", "relation": "supports"},
    {"key": "E041", "paragraph_id": "P071", "quote": "这个“收入预期”并不仅仅是一个数字，而是有一系列连带的实践。", "relation": "supports"},
    {"key": "E042", "paragraph_id": "P075", "quote": "这笔钱本来就不存在。", "relation": "supports"},
    {"key": "E043", "paragraph_id": "P078", "quote": "人们在用自己没有获得过的想象收入，抵偿自己承受的现实风险，支付由此而来的一切保险措施的成本。", "relation": "supports"},
    {"key": "E044", "paragraph_id": "P081", "quote": "是避免被这种wishful thinking卷入地狱的定锚所在。", "relation": "supports"},
    {"key": "E045", "paragraph_id": "P082", "quote": "会有无数的声音嘲笑你“过于保守”、“不聪明”、“缺少远见”，向你炫耀ta们所获得的辉煌成就", "relation": "supports"},
    {"key": "E046", "paragraph_id": "P085", "quote": "因为ta们总会在最后一次不但输光所有本金和一切信用，还会陷入巨额债务。", "relation": "supports"},
    {"key": "E047", "paragraph_id": "P090", "quote": "最后将ta们细嚼慢咽、吮吸干净——连同所有敢于信任ta们的人，一起拖进地狱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["赌博与投机", "家庭理财与风险", "行为规范与自我约束", "宗教信仰与世俗实践"],
   "issue_candidates": ["如何根除赌瘾", "风险承受与能力匹配两条劝诫为何无效", "不劳不获原则的执行方法", "算法化自我管理与自由的关系"],
   "text_function_candidates": ["回应提问", "方案提出", "案例推演", "训诫", "论证与自我反驳"],
   "object_candidates": ["赌瘾", "投机", "时薪期待", "社会信托资产", "数学算法", "历史数据"],
   "working_keywords": ["不劳不获", "时薪", "消毒", "社会信托资产", "确定性之锚", "wishful thinking", "科学历史唯物主义"]
  },
  "status": "read",
  "full_text_checked": True,
  "image_checked": False,
  "notes": "无图片节点（skeleton images 为空），image_checked=false 不影响 read 判定。无 text/lexical 分歧。正文以“（未完，待续）”（P091）结束，属未完成文本，已在 unresolved_questions 标注。原文用字存疑处：P024“毒瘾”（按上下文应为赌瘾）、P077“本里”（疑为“本来”），均按原文照录、未改动，需外部核查。P001“包钢的事”“据说是‘投资失败’”属作者转述、未确认，需外部核查。提问字段（Q001）属提问者。"
 },
 "3a143486": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）问“以暴制暴是合理的吗？”。作者没有直接答“合理/不合理”，而是先贬斥这个年头仍想用暴力解决问题的人，再以反问否定“与之竞赛、比谁症状更猛烈”的思路；随后区分“暴”与“武”：真正的武力是周密计划、冷静执行、毫无情绪、公事公办的，以武才可以制暴，武胜于暴的要害在“义”与民心而非体力或怒气；末以除草为喻反问其是否算“暴”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "以省略号开篇；断言这个年头还想用暴力把别人如何如何的人智商发育有缺陷、社会认知极端不足且人格不健全，正走在不知哪天突然完蛋的道路上；再以反问否定“与之竞赛、比谁症状更猛烈”的想法。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "定义真正的武力：周密计划、冷静执行、毫无情绪、公事公办，如实验员处死小白鼠、导弹旅按下发射钮、农机手驾驶收割机；而睚眦欲裂、板斧排头砍去的血勇形象，是愚昧文人对同为弱者的观众的迎合。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "中国文人既不承认武人的专业性也不承认武力的智慧性，把最大武力模型描绘成葬送理智的血勇暴力，致民众误解取胜之道；但越是青面獠牙、血盆大口越不足为虑，文质彬彬、礼贤下士的才是心腹之患。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "提出“以暴何以制暴？以武才可以制暴”，并以“武”即“止戈”的字义训释作依据。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "武的首要根基是仁者爱人而得道多助、资源远胜令人恐惧憎恶的暴徒，因此能心安理得、举重若轻，才有从容计算的冷静、出手的精确、遇挫的定力、屡败屡战的长性与九死其犹未悔的决心。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "武胜于暴的要害不在体力、不在“怒气值”，而在“义”字与民心所向；正常操作对方即灭，如同除草，并以“田里除草，算‘暴’吗？”反问收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个年头还想用暴力把别人如何如何的人，显然智商发育有缺陷、社会认知极端不足且人格不健全，正走在不知哪天突然完蛋的道路上。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "对“有人还想与之展开竞赛、想比其症状更猛烈点”的合理性提出反问，未予肯定（反问即否定性表态）。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的武力总是周密计划、冷静执行、毫无情绪、公事公办的，如实验员处死小白鼠、导弹旅按下发射钮、农机手驾驶收割机。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "睚眦欲裂、大呼酣战、手持板斧排头砍去的描绘，是愚昧文人向同为弱者的观众所做的基于无知甚至无耻的迎合。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的文人既不承认武人的专业性、也不承认武力的智慧性，更不希望启发民众对武力的正确理解，因此把最大武力模型描绘成将理智完全葬送才有的血勇暴力，使民众误以为青面獠牙、血盆大口才是取胜之道。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越是青面獠牙、血盆大口越是不足为虑；文质彬彬、礼贤下士的才是心腹之患。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以暴不能制暴，以武才可以制暴；“武”即“止戈”，中国人应天生明白这个道理。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "武的首要根基是仁者爱人而得道多助，使其资源远胜令人恐惧憎恶的暴徒，因而能心安理得、举重若轻。", "evidence": ["E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "武胜于暴的要害不在于体力、也不在于“怒气值”，而在于“义”字与民心站在哪边。", "evidence": ["E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问表示：以武制暴属“正常操作”、如同除草，不应被算作“暴”（未直陈，以反问呈现）。", "evidence": ["E015", "E016"]}
   ],
   "argument_steps": [
    "以“……”开篇（承接或删节痕迹，语料未提供上下文）（P001）",
    "先贬斥：想用暴力把别人如何如何的人智商、社会认知与人格皆有缺陷，正走向完蛋（P002）",
    "指出有人反而想与之竞赛、比症状更猛烈，并反问其合理性（P003-P004）",
    "给出定义：真正的武力是周密计划、冷静执行、毫无情绪、公事公办的（P005）",
    "对比：血勇狂暴的武力形象是愚昧文人对弱者的无知迎合（P006）",
    "归因：文人否认武人的专业性与武力的智慧性，故将最大武力模型描绘成葬送理智的暴力（P007）",
    "推论：越是青面獠牙越不足为虑，文质彬彬、礼贤下士的才是心腹之患（P008-P009）",
    "提出主张：以暴何以制暴？以武才可以制暴（P010）",
    "依据：字义上“武”即“止戈”（P011）",
    "根基：仁者爱人而得道多助，资源远胜暴徒，故能心安理得、举重若轻（P012）",
    "由此推出武力的诸种品质与“以武制暴，战无不胜”（P013）",
    "定位要害：不在体力与怒气值，而在“义”与民心（P014）",
    "类比收束：正常操作如同除草，并反问除草是否算“暴”（P015-P016）"
   ],
   "concept_usage": [
    {"term": "暴", "meaning": "被贬斥的情绪化、血勇式暴力，即“以暴制暴”中的“暴”。", "evidence": "P002/P006/P010", "ambiguity": "作者未给出“暴”的完整界定，主要靠与“武”的对比凸显。"},
    {"term": "武", "meaning": "周密计划、冷静执行、毫无情绪、公事公办的武力；“武”即“止戈”，其根基是仁者爱人、得道多助。", "evidence": "P005/P010/P011/P012", "ambiguity": "“止戈”的字义训释为传统说法，正文未作考辨。"},
    {"term": "义", "meaning": "武胜于暴的要害所在，与民心站在哪边同义。", "evidence": "P014", "ambiguity": "由谁判定“义”与民心所向，正文未说明。"},
    {"term": "怒气值", "meaning": "作者否定的、以情绪强度衡量武力的标准（借用游戏化用语）。", "evidence": "P014", "ambiguity": "无。"},
    {"term": "心腹之患", "meaning": "指文质彬彬、礼贤下士因而真正具有威胁者，与青面獠牙者相对。", "evidence": "P009", "ambiguity": "所指的具体对象或事例不明。"}
   ],
   "examples_and_targets": [
    "实验员处死小白鼠、导弹旅按下发射钮、农机手驾驶收割机：说明“真正的武力”的类比举例",
    "睚眦欲裂、大呼酣战、手持两把板斧排头砍将过去：被贬斥的文学化暴力形象（修辞材料，正文未点名具体人物）",
    "青面獠牙、血盆大口：被误导的“取胜之道”的修辞材料",
    "自发团练：说明青面獠牙者不足为虑的例证（“你多闹腾几天周围的自发团练都把你灭了”）",
    "田里除草：类比以武制暴的“正常操作”，并以反问追问是否算“暴”",
    "中国的文人：被批评的对象群体",
    "泥腿子（造反的民众）：被误导者的指称",
    "提问者（Q001）：被回应的对象，作者未复述其表述"
   ],
   "conditions": [
    "贬斥性论断以“这个年头”为时间限定（P002）",
    "“就是放着你不剿，你多闹腾几天周围的自发团练都把你灭了”——以放任不剿为条件（P008）",
    "“以武制暴，战无不胜”以仁者爱人、得道多助、资源远胜暴徒为前提（P012-P013）",
    "“正常操作，对方就灭了”以“义”在我方、民心在我方为前提（P014-P015）"
   ],
   "rhetoric_and_tone": "冷峻、轻蔑而带训诫色彩的短论。开篇以省略号起，随即连用“智商发育有缺陷”“社会认知极端不足”“人格不健全”等强贬语；以“这合理吗？”“以暴何以制暴？”“田里除草，算‘暴’吗？”三处反问推进；用实验员、导弹旅、农机手与“两把板斧”血勇形象作强烈对照；引“武”即“止戈”作字义训释，语气斩截，带兵法与教化口吻，并用“泥腿子”“青面獠牙”等俗语化措辞。",
   "unresolved_questions": [
    "未给出“以暴制暴”在具体情境下可否使用的判定标准，只以“武/暴”与“义”的区分作答",
    "“义”与“民心站在哪边”由谁、依何判定，正文未说明",
    "“文质彬彬、礼贤下士的才是心腹之患”所指的具体对象或事例不明",
    "“武”即“止戈”属传统字义训释，正文未作考辨，需外部核查",
    "开篇“……”是否为承接上文或被删节的片段，语料未提供上下文",
    "“以武才可以制暴”中的“武”由谁掌握、以何种组织形式实施，正文未涉及"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "这个年头还想用暴力把别人如何如何的人，显然智商发育有缺陷，社会认知极端不足且人格不健全", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "有人还想与之展开竞赛，想比ta症状更猛烈点。", "relation": "context"},
    {"key": "E003", "paragraph_id": "P004", "quote": "这合理吗？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "真正的武力，总是周密计划、冷静执行、毫无情绪，公事公办的", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "这都是愚昧文人向同为弱者的观众所做的基于无知甚至无耻的迎合。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "既不承认武人的专业性、也不承认武力的智慧性，更不希望启发民众对武力的正确理解", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "将最大武力模型描绘成了将理智完全葬送才有的血勇暴力", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "越是青面獠牙、血盆大口，越是不足为虑", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "文质彬彬、礼贤下士的才是心腹之患。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "以暴何以制暴？以武才可以制暴。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "因为“武”即“止戈”。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "是因为仁者爱人而得道多助，以至于其资源远胜令人恐惧憎恶的暴徒", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "所以才有以武制暴，战无不胜。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "而在于那个“义”字，在于民心站在哪边。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "正常操作，对方就灭了，就像除草一样。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P016", "quote": "田里除草，算“暴”吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["暴力与武力", "军事与政治伦理", "文化批评"],
   "issue_candidates": ["以暴制暴是否合理", "武力与暴力的区别", "义与民心在武力中的作用", "文人对武力的误写"],
   "text_function_candidates": ["回应提问", "概念区分", "文化批评", "训诫"],
   "object_candidates": ["武力", "暴力", "义", "民心", "文人", "自发团练"],
   "working_keywords": ["以武制暴", "止戈", "仁者爱人", "得道多助", "怒气值", "心腹之患", "除草"]
  },
  "status": "read",
  "full_text_checked": True,
  "image_checked": False,
  "notes": "无图片节点（skeleton images 为空），image_checked=false 不影响 read 判定。无 text/lexical 分歧。提问字段（Q001）属提问者。文首“……”（P001）疑为承接上文或删节痕迹，语料未提供上下文，未作补写。全篇未出现具体现实人物或事件；历史与字义说法（“武”即“止戈”）属作者论断，需外部核查。"
 },
 "c760d4b4": {
  "analysis": {
   "question_context": "知乎提问（Q001，属提问者）问“长期坚持对一个人好，他会感动吗？”。作者以极短篇幅给出否定性回答：若这种“好”未经允许、甚至在被拒绝之后仍然坚持，则不但不会让对方感动，反而会因如此惊人的自私与贪婪而令人害怕；并进一步主张“允许帮助”存在资格门槛——不是随便什么人都有资格于你有恩，甚至也不是随便什么人都有资格与你有仇。作者未举任何例子，也未展开论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "对提问的直接回答：未经允许、甚至被拒绝在先的“坚持对人好”，不但不会让人感动，反而会因如此惊人的自私与贪婪而让人感到害怕。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "进一步命题：允许帮助是有资格门槛的；不是随便什么人都有资格于你有恩，甚至也不是随便什么人都有资格与你有仇。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "未经允许、甚至拒绝在先的“长期坚持对一个人好”，不但不会让对方感动，反而会因为如此惊人的自私与贪婪而让对方感到害怕。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "允许帮助，是有资格门槛的。", "evidence": ["E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是随便什么人都有资格于你有恩，甚至也不是随便什么人都有资格与你有仇。", "evidence": ["E005", "E006"]}
   ],
   "argument_steps": [
    "设定条件：未经允许，甚至拒绝在先（P001）",
    "否定提问的预期：不但不会感动（P002）",
    "给出实际后果：会因对方的自私与贪婪而感到害怕（P003）",
    "提出上位命题：允许帮助是有资格门槛的（P004）",
    "门槛的一体两面：不是随便什么人都有资格于你有恩（P005-P006）",
    "也不是随便什么人都有资格与你有仇（P007）"
   ],
   "concept_usage": [
    {"term": "未经允许的帮助", "meaning": "未被请求、未被同意，甚至在被拒绝之后仍然坚持的“对人好”。", "evidence": "P001", "ambiguity": "“允许”的形式（明示/默许）未说明。"},
    {"term": "资格门槛", "meaning": "允许他人施与帮助、使施助者得以“有恩于你”所需的资格条件。", "evidence": "P004", "ambiguity": "资格由谁判定、由何构成，正文未说明。"},
    {"term": "有恩/有仇", "meaning": "作者并列的两种需要资格的相互关系，被视为同一种门槛的两面。", "evidence": "P005/P007", "ambiguity": "两者的门槛是否同一，正文未说明。"},
    {"term": "自私与贪婪", "meaning": "作者对被拒绝仍坚持“对人好”者动机的判断。", "evidence": "P003", "ambiguity": "判断依据未给出。"}
   ],
   "examples_and_targets": [
    "无具体人物、事件、机构或数据；全文为一般性命题，未举任何例子",
    "提问者（Q001）：被回应的对象；作者的否定回答针对提问所设想的“长期坚持对人好”情形"
   ],
   "conditions": [
    "全部论断以“未经允许，甚至拒绝在先”为前提条件（P001）",
    "“允许帮助”的门槛针对施助方是否获得允许（P004）",
    "“不是随便什么人”为程度限定，未给出明确的资格标准（P005/P007）"
   ],
   "rhetoric_and_tone": "极简的格言式断言体：短句分行、以逗号断句形成递进（“未经允许，甚至拒绝在先的话，/ 不但不会感动，/ 还会……而感到害怕。”）；无称呼语、无例证、无论证展开，纯命题式陈述，语气冷静断然；两处“甚至”强化递进（甚至拒绝在先、甚至……与你有仇），结尾以对偶句收束，近于箴言。",
   "unresolved_questions": [
    "“资格”的构成与判定标准未说明",
    "对方未拒绝而是默许时，“长期坚持对人好”是否会让人感动，正文未回答",
    "“有恩/有仇”与“允许帮助”的关系只以并列断言给出，未展开论证",
    "提问所设想的“感动”是否还有其他成立情形，正文未讨论",
    "全文仅 96 字，是否为完整回答抑或摘录片段，语料未提供上下文",
    "作者未区分“未经允许”与“被拒绝在先”两种情形的差异"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "未经允许，甚至拒绝在先的话，", "relation": "context"},
    {"key": "E002", "paragraph_id": "P002", "quote": "不但不会感动，", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "还会因为如此惊人的自私与贪婪而感到害怕。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "允许帮助，是有资格门槛的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "不是随便什么人都有资格于你有恩，", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "也不是随便什么人都有资格与你有仇。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际伦理", "情感与关系", "帮助与边界"],
   "issue_candidates": ["长期坚持对一个人好会不会感动对方", "未经允许的帮助是否成立", "帮助与恩仇的资格门槛"],
   "text_function_candidates": ["回应提问", "格言式断言", "边界主张"],
   "object_candidates": ["未经允许的帮助", "资格门槛", "恩", "仇"],
   "working_keywords": ["未经允许", "拒绝在先", "感动", "自私与贪婪", "资格门槛", "有恩", "有仇"]
  },
  "status": "read",
  "full_text_checked": True,
  "image_checked": False,
  "notes": "无图片节点（skeleton images 为空），image_checked=false 不影响 read 判定。无 text/lexical 分歧。提问字段（Q001）属提问者。全文仅 96 字、7 个短段落，无例子与展开论证，按原文如实记录，未作补写或外部引申。"
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


if __name__ == "__main__":
    main()
