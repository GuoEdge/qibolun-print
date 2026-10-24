# -*- coding: utf-8 -*-
"""批次 r001-b0094 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0094.sessions.py            # 写 out/r001-b0094.out.jsonl
  python3 records/r001-b0094.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0094"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0094.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "cceb5b68": {
  "analysis": {
   "question_context": "本文回应知乎提问「导演的水平会影响演员的演技吗？」（Q001，提问者只提问、未表态）。作者以“何止‘有影响’”作答，把问题从“水平高低影响演技”转为导演与演员的权责结构与行业趋势；全文以第一人称“我”对“你”（年轻演员）发言。brief 只截取开头数段，仅作导航。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回应提问：何止“有影响”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "导演与演员的正常关系是木偶师与提线木偶；最优秀的演员接受这一本质。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "进组前可尽情挑剧本、挑导演、表达疑虑；认准导演后应彻底交托。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "做不到交托，演什么都是演自己、干什么都是在干导演，成事不足败事有余。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "导演最忌演员“谈自己的想法”，年轻演员误认特权是致命错误；老戏骨能谈戏源于演员本分与分寸，而非咖位。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "“演员是表达工具、以导演判断为绝对标准”的共识不变；ng百次不焦躁才是好演员，易出好东西。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "演员最关键的不是“演技”或“明星范”，而是彻底交托；做到则戏路、作品、人脉自会有，做不到恐怕根本没下次。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028"], "summary": "追加论述：电影到底是谁的创作，它注定越来越成为导演的创作。", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "以吊威亚魔幻镜头为例：角度、秒数、表情、构图开拍前数月已定，上百人现场就绪，演员临场提异议被写成荒诞场景。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049"], "summary": "想参与创作可以在最开始以共同投资人、联合导演等身份开会；到了片场作为演员去主张什么，分寸要自己掂量。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P050", "P051"], "summary": "没人说演员不能有自己的理解与表达，但空间由导演给；越界、抢空间、索要解释都不被接受。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P052", "P053", "P054", "P055"], "summary": "投资方不会站演员一边（每秒都在烧钱）；这是演员与导演创作地位的对比，难听的话应是入行前的决策前提。", "role": "reason"},
    {"unit_id": "U013", "paragraph_refs": ["P056", "P057", "P058", "P059", "P060", "P061", "P062"], "summary": "历史趋势：分工越细，决策权创作权越向上移动，团队领袖成绝对核心（交响乐团类比）。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "原因在院线发行体制：能上映的片子有限、同一时间只有一部旗舰、赢家通吃，保护政策只是自留地。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079"], "summary": "小制作难获发行认可，不如随大资本下注；制作是刚性成本，投入后限制表演与剧情，归结为时代大势。", "role": "reason"},
    {"unit_id": "U016", "paragraph_refs": ["P080", "P081", "P082", "P083", "P084"], "summary": "例证：漫威演员不能一次获得全部剧本，绿幕难以意会效果，后期可微调表情语气；现场拍摄只近于“胚子”。", "role": "example"},
    {"unit_id": "U017", "paragraph_refs": ["P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093"], "summary": "更残酷的是演员的必要性正受挑战；作者给出动画软件教程、MetaHuman、YouTube 与 NVIDIA 工具链接让读者亲身体会。", "role": "example"},
    {"unit_id": "U018", "paragraph_refs": ["P094", "P095", "P096", "P097", "P098"], "summary": "电影制作正在迅速虚拟化，已无任何表演必须依赖真人；演员表演在下个世代只是“数据发生器”；新海诚一人成片不是奇迹而是即将出现的新常态。", "role": "claim"},
    {"unit_id": "U019", "paragraph_refs": ["P099", "P100", "P101", "P102", "P103", "P104"], "summary": "人工智能已接近听懂镜头与表情的自然语言指示，已能生成群演动作与照片级远景中景；演员已需严肃思考为什么拍电影还有必要用人的表演。", "role": "claim"},
    {"unit_id": "U020", "paragraph_refs": ["P105", "P106", "P107", "P108", "P109"], "summary": "结论：电影越来越成为导演或创作团队的作品，演员的艺术影响趋近可忽略；“电影演员”职业走向衰落，甚至可能被人工智能取消。", "role": "conclusion"},
    {"unit_id": "U021", "paragraph_refs": ["P110", "P111"], "summary": "对年轻演员的警告：当下明星不是在从事演员职业，而是偶像与品牌营销的道成肉身，因资本关系被选中。", "role": "claim"},
    {"unit_id": "U022", "paragraph_refs": ["P112", "P113", "P114", "P115", "P116", "P117"], "summary": "但演员职业并非无意义：剧组不是唯一需要好演员之处，好演员本质是好的细分专业导演，理解角色灵魂的大脑无可替代。", "role": "qualification"},
    {"unit_id": "U023", "paragraph_refs": ["P118", "P119", "P120"], "summary": "二十岁者四十岁前可见此事成真；须想清做演员的本钱，若只是美貌自信与“做一切必要事情”的心理准备，劝重新考虑。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对“导演的水平是否影响演员演技”，作者的回应是“何止有影响”，即影响远超该问法所能涵盖。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "导演与演员正常且最“出货”的关系是木偶师与提线木偶的关系；最优秀的演员是最清楚、理解并接受这一关系本质且没有怨言的人。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "演员进组前可尽情挑剧本、挑导演并表达疑虑，认准导演能力和意愿后应心甘情愿、彻底地把自己交出来。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做不到彻底交托的演员，演什么都是演自己、干什么都是在干导演，成事不足败事有余。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "导演最不喜欢听、也最容易出大事的是演员“谈自己的想法”；年轻演员把前辈谈戏误认为“主角的特权”是致命错误。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的看法：老戏骨能找导演谈戏、提建议，是因为他们“有足够的咖位”或是“主角”、导演“惹不起”。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的反驳：老戏骨能与导演聊戏，是因为其行为在刻在骨子里的“演员本分”自觉之下，导演确信他们懂分寸、明分际，因此反而可聊。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论怎么聊，演员是表达工具、一切以导演判断为绝对标准的共识不变；ng 一百次不焦躁、不逆反、不对抗、只努力调整重来，才是真正的好演员。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "演员最关键的不是“演技”或“明星范”之类的宣传文案，而是彻底交托。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做到彻底交托，戏路、作品、人脉乃至“演技惊人”的评价自然会有；没有这些，恐怕根本没有下次。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "电影注定会越来越成为导演的创作。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以反问指出：在全员等待导演喊 action 的片场，演员提出对镜头的不同意见是说不出口的（作者视为荒谬）。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想参加创作，应在最开始以共同投资人、联合导演等身份与技术、美术、武术、作者团队充分开会，而那时已不是“演员”。", "evidence": ["E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到了片场作为演员主张什么要自己掂量分寸；导演给多大空间就拿多大空间，抢空间即不被接受。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "投资方不会站在演员一边：演员多扯淡的每一秒都在烧投资方的钱（原文以反问强化）。", "evidence": ["E26", "E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "组织业务越依赖细致专业的分工，决策权与创作权就越不可避免向上移动；电影越成为团队合作，团队领袖就越必然成为绝对核心（以交响乐团类比）。", "evidence": ["E28", "E29", "E30"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "电影走向细分分工取决于院线发行体制：能上映的片子有限、同一时间只有一部旗舰、赢家通吃。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "制作是硬功夫、刚性成本，一旦投入就会自然对表演甚至剧情产生深刻的限制性；这是时代大势所趋，非人力所能对抗。", "evidence": ["E34", "E35"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现场拍摄越来越只接近于是个“胚子”，演员表演的任务越来越接近于创造二次编辑空间最大、成本最低、效率最高的毛胚素材，而非直接表演。", "evidence": ["E36"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "更为残酷的是，演员本身的必要性正在受到挑战。", "evidence": ["E37"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "电影制作正在迅速虚拟化，已没有任何表演必须依赖真人实现；演员的表演在下一个世代只是一个“数据发生器”。", "evidence": ["E38", "E39"]},
    {"claim_id": "C022", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述：很多人认为新海诚一个人做出一整部电影是“奇迹”。", "evidence": ["E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张新海诚一人成片并不是奇迹，而只是人们尚未意识到即将出现的新常态。", "evidence": ["E41"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "人工智能即将能听懂更抽象的自然语言镜头建议，离听懂表情微调指示已近在咫尺；它已能生成群演动作与照片级远景中景。", "evidence": ["E42", "E43"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "演员已经需要严肃思考：为什么拍一部电影还有必要用到人的表演？", "evidence": ["E44"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "电影将越来越成为导演或创作团队的作品，演员在艺术层面的影响趋于可忽略；“电影演员”这一职业已在衰落，甚至可能被人工智能取消而非取代。", "evidence": ["E45", "E46", "E47", "E48"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当下举足轻重的明星并不是在做演员这个职业，而是偶像、是品牌营销的道成肉身；他们被选中不是因为演技出众，而是因为与资本的关系或构建良好关系的潜力。", "evidence": ["E49", "E50"]},
    {"claim_id": "C028", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "但这不意味着演员职业不再有意义：好演员本质上是好的细分专业导演，在CG世代能理解和呈现角色灵魂的大脑仍无可替代。", "evidence": ["E51", "E52", "E53"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "以后的“演员”将不再穿戏服面对摄像机，而是与导演、技术工程师坐在监视器前工作，被安排出演某个角色将越来越是因为其理解与表达能力、因为其心灵。", "evidence": ["E54"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果做演员的本钱只是对美貌的自信以及对“做一切必要事情”的“心理准备”，作者劝其重新考虑。", "evidence": ["E55"]}
   ],
   "argument_steps": [
    "以“何止有影响”顶回提问，把问题抬到导演与演员的权责关系",
    "定义：导演与演员的正常关系是木偶师与提线木偶，最优秀的演员接受这一本质",
    "前提：进组前可尽情挑剧本、挑导演、表达疑虑；认准后须彻底交托",
    "反面推论：做不到交托则演什么都是演自己，成事不足败事有余",
    "禁区：片场“谈自己的想法”是导演最忌；年轻演员误认主角特权是致命错误",
    "反驳“咖位说”：老戏骨能谈戏源于演员本分与懂分寸明分际",
    "共识前提：演员是表达工具，一切以导演判断为绝对标准",
    "结论一：彻底交托才是演员最关键的，做到则有戏路作品人脉，做不到则没下次",
    "转入第二层：电影注定越来越成为导演的创作",
    "例证：吊威亚镜头方案在数月前已定，现场上百人准备就绪",
    "区分位置：想参与创作应在前期以投资人、联合导演等身份开会；片场须自掂分寸",
    "让步与限定：允许有限发挥，但空间由导演给，抢空间越界",
    "理由：投资方不会站演员一边，每拖延一秒都在烧钱",
    "趋势论证：分工细化使决策权创作权上移，团队领袖成绝对核心（交响乐团类比）",
    "归因：院线发行体制——银幕档期稀缺、单一旗舰片、赢家通吃、保护政策只是自留地",
    "后果：小制作难获发行认可→制作刚性投入→反过来限制表演与剧情（时代大势）",
    "例证：漫威剧本分发、绿幕、后期微调，现场表演只近于“胚子”",
    "提出演员必要性受挑战，并列出动画与数字人工具链接",
    "推进：表演成为“数据发生器”，新海诚案例不是奇迹而是新常态",
    "列出人工智能已能做到或近在咫尺的能力",
    "结论二：电影成为导演/团队作品，演员影响趋近可忽略，职业走向衰落甚至被取消",
    "区分明星与演员：明星是偶像与品牌营销的道成肉身，因资本关系被选中",
    "让步转向：演员职业并非无意义，好演员本质是好的细分专业导演",
    "收束：提醒想清做演员的本钱，若只是美貌自信则劝重新考虑"
   ],
   "concept_usage": [
    {"term": "提线木偶", "meaning": "作者用来定义导演与演员关系的核心比喻，指演员在创作执行上由导演支配。", "evidence": "P002", "ambiguity": "作者同时承认演员有有限发挥空间（P050），比喻与“可发挥几次”的边界未明确划定。"},
    {"term": "出货", "meaning": "带引号的行业口语，指能产出好作品、出成果。", "evidence": "P002", "ambiguity": "未界定“出货”的评判标准。"},
    {"term": "演员本分", "meaning": "作者指老戏骨刻在骨子里的职业自觉，是他们能与导演谈戏的前提。", "evidence": "P014", "ambiguity": "未给出识别“本分”的具体标准，也未说明与“听话”的差别。"},
    {"term": "分际关系", "meaning": "作者指演员对自身在剧组中位置与权限界限的清楚认识。", "evidence": "P014", "ambiguity": "分际的具体界线正文未列举。"},
    {"term": "彻底交托", "meaning": "作者所指演员最关键的品质，即把表达完全交给导演、接受重拍与否定。", "evidence": "P021", "ambiguity": "与“你可以发挥个几次”（P050）之间的界限未给出操作标准。"},
    {"term": "胚子／毛胚素材", "meaning": "作者形容现场拍摄的产物，指供后期二次编辑的原始素材。", "evidence": "P084", "ambiguity": "未说明该判断适用于哪些类型的影片。"},
    {"term": "数据发生器", "meaning": "作者预测下个世代演员表演的功能定位，即提供图像数据源。", "evidence": "P096", "ambiguity": "属预测性用语，无时间表与实现路径说明。"},
    {"term": "取消（而非取代）", "meaning": "作者区分人工智能对演员职业的两种影响：不是替换现有演员，而是使该职业不再必要。", "evidence": "P108", "ambiguity": "“取消”的具体含义与时间尺度未说明。"},
    {"term": "旗舰电影", "meaning": "作者指同一时间窗口内发行与影院集中投放的唯一大作。", "evidence": "P066", "ambiguity": "未说明该格局是否适用于所有国家与流媒体时代。"},
    {"term": "赢家通吃", "meaning": "作者对院线发行竞争结果的概括。", "evidence": "P068", "ambiguity": "未给出数据支持。"},
    {"term": "道成肉身", "meaning": "作者借宗教用语指明星是品牌营销的肉身化身。", "evidence": "P111", "ambiguity": "为修辞性用法，非严格定义。"}
   ],
   "examples_and_targets": [
    "吊威亚痛哭着从悬崖边飞扑拉住中箭坠落的魔法伙伴（P031）——假设表演情景，论证材料",
    "全身传感器的动捕演员／特型演员，最终呈现为半机械半魔法的龙形精灵（P032）——假设例子",
    "特效导演、美术导演、故事板画师、原著作者、编剧、制片人开制作会议（P033）——论证材料",
    "CG组、道具组、美术组、化妆组、摄影轨道、测光跟焦、威亚师傅（P035—P037）——制作准备之庞大的论证材料",
    "片酬两千多万、从香港飞来的天皇巨星（P038）——讽刺性修辞，未指明人物",
    "现场一百多人的摄影师、武师、灯光师、群演、电工、木工、茶水、司机等（P039）——论证材料",
    "演员在片场提“我对这个镜头的不同意见”的假想对话（P041—P044）——假设情景与反问修辞",
    "七百二十度大转体、断肠崖顶 power landing、大特写（P043）——假想的荒谬要求，修辞材料",
    "对投资方站哪边的反问（P052—P053）——修辞性反问，非实名对象",
    "四重奏首席小提琴引领全场 vs 一百多人的交响乐团（P060—P061）——类比论证",
    "《钢铁侠》上映时影院几乎全放《钢铁侠》，对比《爱在黎明时》《雷锋日记》（P065）——举例与对比（片名照原文）",
    "中国市场、越南市场、新加坡各有一个名额（P067）——假设与反驳对象",
    "漫威新片演员不能一次获得全部剧本（P080）——转述的行业事实，无出处，需外部核查",
    "Adobe Character Animator 系列教程（bilibili，P086—P087）——外部链接，正文未说明内容",
    "MetaHuman Creator 新特性（P088—P089，称“四天前刚发布”）——外部链接材料",
    "youtube.com/watch?v=tdxMo11KJGk（P090—P091）——外部链接，正文未说明内容",
    "nvidia-research-mingyuliu.com/gaugan（P092—P093）——外部链接，正文称可直接试一试",
    "新海诚一个人做出一整部电影（P097）——例证（未指明片名）",
    "在远景里加上一群1930年中国上海风格的平民随机走动（P101）——人工智能能力举例",
    "游戏工业中照片级远景中景的现实应用（P102）——举例",
    "提问者与其问题“导演的水平会影响演员的演技吗”（Q001）——本文回应对象"
   ],
   "conditions": [
    "“进组之前”“接本、进组之前”是作者给出挑剧本、挑导演、表达疑虑的时间条件（P004、P005）",
    "“只要导演觉得还不够，重拍一千遍也是份内应当”为让步式条件句（P016）",
    "“如果你有这个本事的话”限定演员可在前期以导演、制片人、编剧、动作指导身份参与（P048）",
    "“到了片场，对着镜头，你作为一个演员”限定分寸要求适用的场景（P049）",
    "P051 以连续条件句给出可接受与不可接受的分界（四秒就收、坐起来、慢走两步、索要解释、要求说第二遍）",
    "“你如果真的有志于把前途押在一个职业上”限定劝告的适用对象（P055）",
    "“只是有电影工业野心的国家通过保护政策”为限定条件（P069）",
    "“一部电影也许可以新人导演、素人演员，但是势必要用非常扎实硬核的制作团队”为让步—条件结构（P077）",
    "“如果你还是一名年轻的演员”限定收尾警告的受众（P110）",
    "“如果这本钱是你对自己美貌的自信”为末段劝告的触发条件（P120）"
   ],
   "rhetoric_and_tone": "第二人称训诫与断言体。开篇以“何止‘有影响’”顶回提问；大量反问（“电影到底是谁的创作？”“这话正常人说得出口吗？”）；粗直贬斥语（“狗屁”“王八蛋”）；铺陈式列举与排比（现场上百工种、连续“你就是王八蛋”条件句）；第一人称权威叙事（“我再加一段”“但我要告诉你们”）；类比推进（木偶师与提线木偶、四重奏与交响乐团）；插入外部链接；结尾转箴言式警告与自我盘问。",
   "unresolved_questions": [
    "P086—P093 四处外部链接（bilibili 动画软件教程、MetaHuman Creator、YouTube 视频、NVIDIA Gaugan）内容均未在正文说明，链接有效性与具体内容需外部核查。",
    "P080 漫威新片“演员不能一次获得全部剧本”是作者转述的行业说法，正文未给出处，需外部核查。",
    "P038 “片酬两千多万”“踩着点从香港飞来的天皇巨星”是否为实指、指向何人，正文未说明。",
    "P097 “新海诚已经做到过一个人做出一整部电影”未指明是哪一部作品。",
    "P042 “哦？”独立成段，语义完全依附上下文，单独不可解。",
    "P086 与 P087、P088 与 P089、P090 与 P091、P092 与 P093 存在链接文字与正文混排重复；P087/P089/P091/P093 被标注“lexical未覆盖片段”，疑为抓取残留，原文形态需核验。",
    "“演员可以发挥个几次”与“抢空间就是王八蛋”之间没有可操作的界分标准，全文未给统一判据。",
    "提问问的是“导演的水平”对“演技”的影响机制，作者转而论证权责结构与行业趋势，“演技”如何被影响未正面展开。",
    "本文 published_at 为 2021-02-14、updated_at 为 2025-10-17，是否含发表后修改不明。",
    "P033 称原著作者依合同可否决不合适的改编，该合同惯例的普遍性需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "何止“有影响”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "就是木偶师和提线木偶的关系。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "就是最清楚、最理解、最接受这一关系本质，没有怨言", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "进组之前可以挑剧本、挑导演、往死里挑，任何不服气，都可以尽情挑。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "就能全心全意的、心甘情愿的、彻彻底底的把自己交出来", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "做不到，演什么都是演自己。干什么都是在干导演。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "自然而然的成事不足，败事有余。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "当导演，最不喜欢听的、也最容易出大事的，就是演员“谈自己的想法”。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "尤其是年轻的演员，常常看着一些前辈这样做就以为这是“主角的特权”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "这是一个致命的错误。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "根本不是因为ta们“有足够的咖位”，或者是“主角”，导演“惹不起”。", "relation": "contradicts"},
    {"key": "E12", "paragraph_id": "P014", "quote": "而是因为ta们做这些是在刻在骨子里的“演员本分”的自觉前提之下做的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "演员是一种表达的工具，一切以导演的判断为绝对标准的共识不变。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "ng一百次，不焦躁、不逆反、不对抗，只会努力调整重来", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "既不是所谓的“演技”，更不是所谓的什么狗屁“明星范”这类宣传用的鬼话文案，", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "而是那种勇敢得让人肃然起敬的彻底交托，是一个演员最关键的东西。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "做得到这一条，“戏路”“作品”“人脉”自然会有。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "没这些，直白点讲恐怕根本就没下次了，还谈什么“演技”？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "它注定会越来越成为导演的创作。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P041", "quote": "我能跟你说说我对这个镜头的不同意见吗？", "relation": "context"},
    {"key": "E21", "paragraph_id": "P044", "quote": "这话正常人说得出口吗？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P045", "quote": "你想参加创作，你可以在最开始就以共同投资人的身份、联合导演的身份来开会。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P049", "quote": "你作为一个演员，你想想在表演的时候，去主张点什么，你该是什么分寸", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P050", "quote": "这五秒你要怎么管理表情，你可以发挥个几次我来选", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P051", "quote": "我给你多大空间，你拿多大空间，你来抢空间，你就是王八蛋。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P052", "quote": "你以为投资方站你这边？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P053", "quote": "你多扯淡的每一秒钟ta们的钱都在燃烧", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P058", "quote": "这项业务的决策权、创作权就会不可避免的越向上移动。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P059", "quote": "电影越发展成为团队合作，团队的领袖就必然越成为绝对核心。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P060", "quote": "一百多人的团队就算想要跟着首席乐手走，在技术上也根本不可能", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P064", "quote": "每年能登上荧幕的片子数量是相当有限的", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P066", "quote": "同一时间，只能有一部旗舰电影。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P068", "quote": "事实是残酷的赢家通吃。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P077", "quote": "而这部分一旦投下去，就会自然而然的对表演、甚至对剧情产生深刻的限制性。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P078", "quote": "这是时代大势所趋，非人力所能对抗。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P084", "quote": "演员表演的任务越来越更接近于“创造一个二次编辑空间最大、成本最低、效率最高的毛胚素材”", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P085", "quote": "更为残酷的是——演员本身的必要性正在受到挑战。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P095", "quote": "已经没有任何表演还必须要依赖真人实现", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P096", "quote": "演员的表演在下一个世代里只是一个“数据发生器”", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P097", "quote": "很多人认为这是“奇迹”", "relation": "context"},
    {"key": "E41", "paragraph_id": "P098", "quote": "这并不是奇迹，而只是你们没有意识到即将出现的新常态罢了。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P101", "quote": "它已经可以做到“在远景里加上一群1930年中国上海风格的平民随机走动”", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P102", "quote": "它已经可以根据风格性的指示生成足够可信的、照片级的远景甚至中景", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P104", "quote": "演员已经需要严肃的思考这样一个问题——为什么拍一部电影，还有必要用到人的表演？", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P105", "quote": "电影将越来越成为导演——或者说创作团队的作品。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P106", "quote": "这一点之所以还没有被观众觉察、是因为电影艺术本身之外的市场营销的原因。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P107", "quote": "事实上已经在逐渐走向衰落", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P108", "quote": "甚至可能被人工智能取消。不是取代，而是取消。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P111", "quote": "ta们的职业不是演员，而是偶像、是品牌营销的道成肉身。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P111", "quote": "ta们不是因为“演技出众”而被选中的，而是因为与资本的关系", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P112", "quote": "但这不是打算告诉你们演员这个职业不再有意义。", "relation": "qualifies"},
    {"key": "E52", "paragraph_id": "P115", "quote": "一个好的演员，本质上也是一名好的细分专业的导演。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P116", "quote": "但是一个能理解和呈现一个角色的灵魂的大脑，仍然是无可替代的。", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P117", "quote": "安排ta来出演某个角色，将越来越多的是因为ta的理解和表达能力", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P120", "quote": "如果这本钱是你对自己美貌的自信，以及对“做一切必要事情”的“心理准备”，劝你重新考虑。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["电影工业", "表演艺术", "影视制作", "职业发展", "技术与劳动分工"],
   "issue_candidates": ["导演与演员的权责关系", "演员的创作空间与片场分寸", "院线发行体制与赢家通吃", "人工智能对演员职业的冲击", "演员职业前景"],
   "text_function_candidates": ["知乎问答回答", "行业经验陈述", "训诫与劝告", "趋势预测", "反驳与澄清"],
   "object_candidates": ["导演", "演员", "现代电影工业", "院线发行体制", "人工智能与数字人", "明星与资本"],
   "working_keywords": ["提线木偶", "演员本分", "彻底交托", "胚子", "数据发生器", "旗舰电影", "赢家通吃", "道成肉身"]
  },
  "notes": "无图片，image_checked=false；4处外链及P086-P093抓取残留仅列为未决，不据链接推断。判断均取正文；作者身份未说明，Q001仅为提问。"
 },
 "30c953b6": {
  "analysis": {
   "question_context": "回应Q001“实现按需分配需要什么样的社会条件？”作者只讨论终身基本生活保障的物质条件，并声明不是政策主张。",
   "content_units": [{"unit_id":"U001","paragraph_refs":["P001","P002"],"summary":"作者称，若享受者自愿放弃生育，并排除福利需求随生育增长，基本衣食住疗的按需保障在数学上可实现。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P003"],"summary":"作者把上述内容限定为事实陈述而非政策倡议。","role":"qualification"}],
   "main_claims": [{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"终身基本生活保障的绝对必要条件被作者归结为享受者自愿放弃生育。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"在排除‘坐吃福利指数增长’后，基本生存条件的按需分配并非不可想象。","evidence":["E2"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"negated","statement":"作者明确不把文本当作政策主张。","evidence":["E3"]}],
   "argument_steps": ["以生育是否导致保障需求增长作为数学条件。","将基本保障范围限定为衣食住疗。","用免责声明区分事实判断与政策立场。"],
   "concept_usage": [{"term":"按需分配","meaning":"本文中指基本生存条件按个人需要获得保障，不等同于作者完整制度方案。","evidence":"P002","ambiguity":"未定义需求标准、资源来源或分配机制。"},{"term":"坐吃福利指数增长","meaning":"作者假定的福利需求随生育扩大的情形。","evidence":"P002","ambiguity":"未说明指数增长的具体模型。"}],
   "examples_and_targets": ["基本衣食住疗（P001）——保障范围","享受者生育与福利需求增长（P001-P002）——条件关系","Q001提问——回应对象"],
   "conditions": ["‘绝对必要条件只有一条’是作者的强断言（P001）","‘去掉坐吃福利指数增长’限定P002的可行性判断","‘不代表主张这种政策’限定文本功能（P003）"],
   "rhetoric_and_tone": "极简、断言式，使用数学可行性和免责声明压缩论证；未展开社会制度、伦理或政策层面的讨论。",
   "unresolved_questions": ["‘自愿放弃生育’为何是绝对必要条件，正文未给推导。","基本保障的资源约束、劳动参与和人口结构未讨论。","按需分配的需求判定与制度执行方式未说明。"],
   "evidence": [{"key":"E1","paragraph_id":"P001","quote":"实现终身基本生活保障（基本衣食住疗）的绝对必要条件只有一条——享受者自愿放弃生育。","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"实现基本生存条件相关的按需分配并不是什么天方夜谭。","relation":"supports"},{"key":"E3","paragraph_id":"P003","quote":"这并不代表主张这种政策，只是陈述一个基本事实。","relation":"qualifies"}]
  },
  "provisional_tags": {
  "domain_candidates": ["社会保障","人口与资源","分配制度"],
  "issue_candidates": ["基本生活保障的条件","生育与福利需求","按需分配"],
  "text_function_candidates": ["知乎问答回答","条件判断","立场限定"],
  "object_candidates": ["基本生活保障","生育","福利分配"],
  "working_keywords": ["按需分配","基本衣食住疗","放弃生育","福利增长"]
  },
  "notes": "无图片；短文，判断严格限于3个正文段落。"
 },
 "8cad2f25": {
  "analysis": {
   "question_context": "回应Q001“只会埋头苦干、不会吹嘘拍马屁的人最后都过得好吗？”作者先质疑‘埋头苦干’的含义，再讨论有前途的工作、领导者的心理支持和下属的去留。",
   "content_units": [{"unit_id":"U001","paragraph_refs":["P001","P002"],"summary":"把埋头苦干具体化为重复、少交流、少发言的执行劳动。","role":"definition"},{"unit_id":"U002","paragraph_refs":["P003","P004","P005"],"summary":"作者认为这类任务缺乏前途，易被自动化或成为低收入劳动；管理岗不适用此工作方式。","role":"claim"},{"unit_id":"U003","paragraph_refs":["P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016"],"summary":"有前途的工作需要提供信息、方案、决策并公开沟通，执行也是实验和数据采集；创新要求团队探险与维持士气。","role":"argument"},{"unit_id":"U004","paragraph_refs":["P017","P018","P019","P020","P021","P022","P023","P024","P025"],"summary":"所谓拍马屁可能承担领导者的心理支持职能，问题在于支持是否交给有职业道德的人，而非需求本身。","role":"qualification"},{"unit_id":"U005","paragraph_refs":["P026","P027","P028","P029","P030","P031"],"summary":"下属不应轻率评价该辅助者；若领导偏爱虚假肯定且看不出问题，应准备跳槽。","role":"advice"}],
   "main_claims": [{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"纯重复、少交流的‘埋头苦干’型工作通常没有前途，可能被自动化或压低为青春饭。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"有前途的工作要求发言、提供信息方案决策，并把执行当作测试和数据采集。","evidence":["E2","E3"]},{"claim_id":"C003","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"领导者需要外部肯定并不必然是问题，关键是支持者是否诚实、有职业道德。","evidence":["E4"]},{"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"若领导无法识别虚假逢迎，下属留在这条船上争位置没有意义，应考虑跳槽。","evidence":["E5"]}],
   "argument_steps": ["先通过插秧、车零件等例子界定‘埋头苦干’。","把重复执行与自动化、低收入劳动的趋势相连。","以创新的不确定性说明沟通、表达和士气维护是工作本身。","重估‘拍马屁’为可能的心理支持劳动，再区分诚实支持与虚假肯定。","以领导识别能力作为下属是否离开的判断点。"],
   "concept_usage": [{"term":"埋头苦干","meaning":"作者特指不发言、只重复执行的工作方式，而非一般意义上的勤奋。","evidence":"P001-P003","ambiguity":"未讨论需要长期专注但仍有前途的职业。"},{"term":"吹嘘拍马屁","meaning":"作者将其拆分为可能提供心理肯定的辅助职能与无职业道德的虚假肯定。","evidence":"P017-P024","ambiguity":"两者的识别标准未完全列出。"},{"term":"结队探险","meaning":"作者对创新团队面对未知的比喻。","evidence":"P013","ambiguity":"是修辞类比而非组织模型。"}],
   "examples_and_targets": ["插两亩地秧、车一千个零件（P002）——重复劳动例子","自动化、年轻人或低收入国家的青春饭（P003）——趋势判断","提供信息、方案、决策（P007）——工作价值类型","领导者心理治疗师/辅助者（P018、P024）——支持职能","领导偏爱虚假肯定的组织（P027-P031）——离职情境","Q001提问——回应对象"],
   "conditions": ["‘如果工作确实’限定重复劳动的评价（P003）","‘有前途的工作’限定沟通与决策要求（P006-P011）","‘如果你交错了人’限定虚假肯定的风险（P021）","‘如果你确信’且领导看不出逢迎，触发跳槽建议（P027）"],
   "rhetoric_and_tone": "反问开篇，随后用分类、因果推断和直接训诫推进；语言口语化、评价强烈，末段以‘没前途的船’作比喻收束。",
   "unresolved_questions": ["自动化将消除哪些重复岗位，正文无数据。","心理支持职能与逢迎、操纵之间的边界未操作化。","作者把沟通热情视为普遍职业要求，未区分行业和岗位。"],
   "evidence": [{"key":"E1","paragraph_id":"P003","quote":"这种只要闷头执行，无限重复就可以交付的任务，要么就已经自动化或者即将自动化了","relation":"supports"},{"key":"E2","paragraph_id":"P006","quote":"有前途的工作，都是要参与意见和决策的。","relation":"supports"},{"key":"E3","paragraph_id":"P014","quote":"出声是你的工作不可分割的一部分。","relation":"supports"},{"key":"E4","paragraph_id":"P022","quote":"这是一个完全合理合法的需求，一个需要正视的需求。","relation":"supports"},{"key":"E5","paragraph_id":"P027","quote":"你要做的是立刻着手准备跳槽","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates": ["职场与组织","管理","劳动与自动化"],
  "issue_candidates": ["重复劳动的前途","沟通与决策","领导心理支持","逢迎与跳槽"],
  "text_function_candidates": ["知乎问答回答","概念澄清","职场劝告"],
  "object_candidates": ["执行劳动","创新团队","领导者","下属"],
  "working_keywords": ["埋头苦干","出声","结队探险","肯定贩卖者","跳槽"]
  },
  "notes": "无图片；将‘埋头苦干’与‘拍马屁’按正文区分为工作方式和支持职能，不替作者补充行业数据。"
 },
 "178eaaf6": {
  "analysis": {
   "question_context": "回应Q001“农村大量男光棍问题怎么解决？”作者不提供政策方案，而是把婚育从前现代生存法则转为现代人口、生产率和伦理变化问题。",
   "content_units": [{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006"],"summary":"前现代社会依赖人力、寿命短、土地生产率低，人口不繁盛会造成存续危机；婚育因此被视为生存法则。","role":"historical_reconstruction"},{"unit_id":"U002","paragraph_refs":["P007","P008","P009","P010","P011"],"summary":"现代生产能力可养活更多人口但只需较少人口，工业化后人口先升后降，不婚不育增加却不必然危及社会存续。","role":"claim"},{"unit_id":"U003","paragraph_refs":["P012","P013","P014","P015","P016","P017","P018","P019","P020","P021"],"summary":"作者把生育崇拜视为历史惯性，认为个体不应把时代变迁理解为被谁迫害，应接受并寻找其他价值。","role":"advice"},{"unit_id":"U004","paragraph_refs":["P022","P023","P024","P025","P026","P027","P028","P029","P030"],"summary":"作者预测婚育伦理继续变化，非婚性行为和无后代状态趋于无罪化，并把对无婚无育者的逼迫视为社会问题根源。","role":"forecast"}],
   "main_claims": [{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"婚配和生育在前现代是由人力、寿命、生产率和人口存续条件塑造的生存法则。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"现代生产率与人口需求错位，使不婚不育增加但不必然危及社会延续。","evidence":["E2","E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"将时代转型视为‘被害’会增加精神消耗，作者建议接受变化并寻找其他价值。","evidence":["E4"]},{"claim_id":"C004","claim_type":"author_qualified","attribution":"author","modality":"predicted","statement":"作者预言非婚性行为与无后代状态将逐步去罪化，反婚育逼迫本身会成为更主要的社会问题。","evidence":["E5"]}],
   "argument_steps": ["回溯前现代婚育的物质条件。","指出工业化、城市化和商品经济带来人口先增后降。","以‘无人要害你’区分结构性变迁与人为迫害。","由人口判断推及婚育伦理的未来变化。"],
   "concept_usage": [{"term":"前现代条件下的生存法则","meaning":"婚育因人力生产、短寿命和低生产率而具有社会存续功能。","evidence":"P002-P006","ambiguity":"未区分不同历史社会。"},{"term":"生育崇拜","meaning":"作者所称几千年文明史形成的生育观念惯性。","evidence":"P012","ambiguity":"未给出具体制度或群体范围。"},{"term":"无罪化","meaning":"作者对非婚性行为和无后代状态社会评价下降的预测性概括。","evidence":"P025-P026","ambiguity":"不是法律条文的明确分析。"}],
   "examples_and_targets": ["保家、卫国、生产依靠人力（P003）——历史条件","工业化后人口先升后降（P008-P010）——人口趋势模型","君主和族长为兵源、税基宣扬婚育价值（P022）——作者的历史解释","经济不平等待遇、舆论攻击、关系贱民化（P028）——逼迫后果","Q001提问——回应对象"],
   "conditions": ["‘前现代条件下’限定婚育生存法则（P002）","‘甫一进入工业化时代’限定人口先升后降过程（P009）","‘首先不会没有人生育’与生产率足够构成不婚育不危及存续的条件（P011）","‘如果是有人要害你’与‘没有任何人要害你’构成反事实对照（P017-P019）"],
   "rhetoric_and_tone": "先历史解释，后趋势断言，再以命令式劝告收束；语气冷峻、去情绪化自我标注明显，同时含‘早点领悟，早点解脱’等安慰与训诫。",
   "unresolved_questions": ["人口趋势和‘足够的社会继承人’无统计依据。","婚育价值由君主族长宣扬的说法未给史料。","‘无罪化’究竟指法律、舆论还是伦理，层次未区分。","对农村男性具体处境没有个案或政策层面的解决路径。"],
   "evidence": [{"key":"E1","paragraph_id":"P006","quote":"社会要全方面的出问题，要亡国灭种。","relation":"supports"},{"key":"E2","paragraph_id":"P007","quote":"它可以养活极大的人口，但它事实上只需要极少的人口。","relation":"supports"},{"key":"E3","paragraph_id":"P011","quote":"这并不会真的影响到这个社会的存续性","relation":"supports"},{"key":"E4","paragraph_id":"P019","quote":"没有任何人要害你，你是自然而然要面对某种结局","relation":"supports"},{"key":"E5","paragraph_id":"P027","quote":"对婚育的无理性执着、以及由此执着而蒸腾出来的对无婚无育的逼迫和伤害才是造成社会问题的根源。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates": ["人口社会学","婚姻家庭","社会伦理","现代化"],
  "issue_candidates": ["农村男性不婚","人口转型","婚育观念","非婚无育伦理"],
  "text_function_candidates": ["知乎问答回答","历史解释","趋势预测","劝告"],
  "object_candidates": ["农村光棍","现代社会","婚育制度","生育崇拜"],
  "working_keywords": ["前现代生存法则","人口转型","生育崇拜","无罪化","接受命运"]
  },
  "notes": "无图片；正文未提出针对农村男性的具体治理方案，记录保留这一范围限制。"
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
