# -*- coding: utf-8 -*-
"""批次 r001-b0131 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0131.sessions.py            # 写 out/r001-b0131.out.jsonl
  python3 records/r001-b0131.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0131"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0131.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "8859afe4": {
  "analysis": {
   "question_context": "知乎回答，回应提问“家长可以强迫孩子去睡觉吗？”。作者未按操作层面作答，而把问题提升为亲子间“管理与服从管理”关系的一般讨论：先复述“家长有权甚至有义务让子女适应强迫”的流行论证，再区分“服从”与“屈从”，最后给出父母如何培养真服从的建议。提问者与作者立场不同；追问的具体情境（年龄、强迫形式）正文未展开，到末段才回到“下令让孩子去睡觉”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "设定亲子间存在管理与服从关系，子女‘不听话’被父母视为顽疾。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "复述流行辩护：家长有权甚至有义务让子女适应强迫，以学会在暴力前委曲求全。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "让步：协作必涉及顺从，父母必须构造子女的顺从机制。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "提出服从／屈从之分，并给出屈从定义。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "屈从的机理与后果：理性与暴力的双重失败、崇拜暴力、只养出失败者。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025"], "summary": "屈从机制使教育低效甚至不可能，训练的是反射式信号反应。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031"], "summary": "服从的定义：出于爱之信任或超越性诉求，自己决定违逆安逸本能。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037"], "summary": "第一理由：凭理性确认指令与自身追求一致，本质是服从自己的理性。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "第二理由：凭对爱的敏感性相信对方的爱而服从，这是学习的意志基础。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P046", "P047", "P048", "P049"], "summary": "前两种服从都含终止服从的自由与退出程序；服从是自由的实现。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055"], "summary": "第三种情况：管辖根源超越自身选择；该原则延伸至一切无可选择场合。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064"], "summary": "是否服从须各人自选、不得强令共识；同时须接受自然限制，否则陷永动机悲剧。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "把顺从锁定在服从定义内者获最大优势；主动服从的团体有组织优势。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078"], "summary": "转向父母的具体问题：如何使子女走向服从；要害是对动机的再定义。", "role": "transition"},
    {"unit_id": "U015", "paragraph_refs": ["P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092"], "summary": "驳‘服从是理所当然的起点’；用暴力即向子女宣告‘服从就是屈从’。", "role": "rebuttal"},
    {"unit_id": "U016", "paragraph_refs": ["P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115", "P116", "P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138", "P139", "P140", "P141", "P142", "P143", "P144", "P145", "P146", "P147", "P148", "P149", "P150", "P151", "P152"], "summary": "转变一：默认把不顺从读作健康的不屈从，视之为对自己的考验；方向是自省与忏悔。", "role": "action_advice"},
    {"unit_id": "U017", "paragraph_refs": ["P153", "P154", "P155", "P156"], "summary": "转变二：停止惩罚不顺从，赞许不屈从、赞美服从。", "role": "action_advice"},
    {"unit_id": "U018", "paragraph_refs": ["P157", "P158", "P159", "P160", "P161", "P162", "P163", "P164", "P165", "P166", "P167", "P168", "P169", "P170", "P171", "P172", "P173", "P174", "P175"], "summary": "自愿服从五要件：自愿声明、风险自担、判断权交托、自愿接受裁决、自愿接受执行。", "role": "definition"},
    {"unit_id": "U019", "paragraph_refs": ["P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184", "P185", "P186", "P187", "P188", "P189", "P190", "P191", "P192", "P193", "P194", "P195"], "summary": "交托之重：领受者须自知不配；明白后自然获得耐心与忏悔的下意识。", "role": "reason"},
    {"unit_id": "U020", "paragraph_refs": ["P196", "P197", "P198", "P199", "P200", "P201", "P202"], "summary": "结论：服从能力即爱的能力本质；看懂者才可以下令让孩子去睡觉。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "亲子间存在管理与服从管理的关系，且是父母挫折感最强的科目。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "流行辩护：家长有权甚至有义务让子女适应强迫，以学会在暴力优势前委曲求全。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "让步：协作必涉及顺从，父母必须构造子女的某种顺从机制。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "关键分歧是父母构造的顺从他属于服从还是屈从。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "屈从是以对实力（实为暴力）的判断取代是非判断，每次奏效都是暴力与理性的双重失败。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "屈从只能养出崇拜暴力、轻视理性的失败者，并使教育低效甚至不可能。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "服从是基于对他人爱的信任或对自身超越性诉求的坚持，自己选择违逆安逸本能。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人决定服从只有三个理由；第一种是凭理性确认指令与自身追求一致，本质是服从自己的理性。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二种是凭对爱的敏感性相信对方的爱而服从，这是学习的意志基础。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把一切服从混同于屈从而无差别抗拒者将失去多数经验增长机会，最终反陷‘被迫屈从’。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育的首要前提是：要学习就必须服从教导。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "前两种服从都含‘决定终止服从的自由’，理性的服从约定必须包含退出程序。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这两种情况人其实服从的是自己，故服从不是自由的失败而是自由的实现。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "管辖根源超越自身选择时应作有意义有原则的服从，该原则延伸至一切没有留下不顺从选择的场合。", "evidence": ["E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人仍可以生命为赌注反抗，故有终极自由；人类缺少的只是廉价、足够‘经济’的自由。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是否服从须各人自己选择，不应被强令成‘共识’，指责拒绝共同反抗者侵犯他人自由。", "evidence": ["E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实力的绝对差异本身是一种答案，意味着对方从自然手里获得管理你的特殊许可。", "evidence": ["E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对自然给你的限制必须寻找某种形式去服从；这是服从的形式与艺术问题。", "evidence": ["E27"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主动服从的团体在合作成本与产出效益上显著优于被动屈从者，‘降将’居高位即其组织机理之例。", "evidence": ["E28", "E29"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母问题的要害是‘对动机的再定义’：子女靠观察父母的随后反应形成对自己动机的解读。", "evidence": ["E30"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "必须放弃‘服从是理所当然的起点’之妄念：服从是教育的永恒终点；用暴力即宣告‘服从就是屈从’。", "evidence": ["E31", "E32"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "语言上对理智说的话无法抵消用事实的语言对灵魂的宣告，因为‘事实是神的语言’。", "evidence": ["E33"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应默认把不顺从读作不屈从：它是未能确认爱之前的健康本能，也是筛选服从对象的天然机制。", "evidence": ["E34", "E35"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母未因正当的不屈服而沮丧暴躁才获得试探性服从的资格；这其实是对父母的考验。", "evidence": ["E36", "E37"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "唯一正确的方向是自问‘我在哪里流露出了我不自知的威胁性’，并相信自己的理解仍有无法察觉的缺陷。", "evidence": ["E38", "E39"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所领受的服从是凡人领受不起的权柄，唯有自知不配才可被视为配得；身为领袖，道歉比责罚强大。", "evidence": ["E40", "E41"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二个转变是停止惩罚不顺从，赞许不屈从的勇气并赞美服从。", "evidence": ["E42"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自愿服从由五项要件构成，其中自愿接受裁决的唯一例外是死刑。", "evidence": ["E43", "E44"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "服从延续到哪一刻是发愿者不可剥夺的权利，可在惩罚落下前叫停，并应为叫停致歉。", "evidence": ["E45"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "明白后不必忧虑是在刻意扭曲、‘设计’子女人生，只是遵循本来就存在的规律。", "evidence": ["E46"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "反复申明‘并非只有完美服从才算及格’可把命令变成得到父母爱戴的机会。", "evidence": ["E47"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "服从的能力是激发一切爱的那把钥匙，因为它就是爱的能力的本质。", "evidence": ["E48"]},
    {"claim_id": "C033", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若读者看懂，就可以下令让孩子去睡觉；命令是谦卑者、忏悔者、爱人者的特权，僭越者即为敌人；若没看懂或不认同，最好不要随便下令。", "evidence": ["E49", "E50", "E51"]}
   ],
   "argument_steps": [
    "复述流行论证：为让子女看懂暴力优势、学会委曲求全，家长有权甚至有义务让子女适应强迫（P003-P008）。",
    "反问后让步：协作必涉及顺从，父母必须构造顺从机制（P009-P010）。",
    "提出关键分歧：构造的顺从是服从还是屈从（P011）。",
    "定义屈从：以实力（暴力）判断替代是非判断；它是理性的失败与投降（P012-P014）。",
    "推屈从后果：崇拜暴力、只养出失败者，并使教育低效甚至不可能（P015-P025）。",
    "定义服从：出于爱之信任或超越性诉求、自己决定违逆安逸本能（P027-P030）。",
    "第一理由：凭理性确认指令与自身追求一致（志愿兵、组织、契约），本质是服从自己的理性（P033-P037）。",
    "第二理由：凭对爱的敏感性相信对方的爱而服从，这使教育成为可能（P038-P040）。",
    "反证：一概抗拒一切服从者反陷被迫屈从，故要学习就必须服从教导（P041-P044）。",
    "前两种服从都含终止自由与退出程序；人其实服从自己，服从是自由的实现（P046-P049）。",
    "第三种情况：管辖根源超越自身选择，并延伸至一切无可选择的自然限制（P050-P053）。",
    "保留终极自由：人可赌上生命反抗，缺少的只是廉价自由（P054-P055）。",
    "限定：是否服从由各人自选，不得强令成共识；但须接受自然限制，否则陷永动机悲剧（P056-P064）。",
    "结论性推论：把顺从锁定在服从定义内者获最大优势，主动服从的团体有组织优势（P065-P071）。",
    "转向操作问题：如何让子女走向服从而非屈从，要害是对动机的再定义（P072-P078）。",
    "反驳‘服从是理所当然的起点’：服从是教育终点；用暴力即宣告‘服从就是屈从’（P080-P092）。",
    "转变一：默认不顺从为不屈从（健康本能与筛选机制），视为对自己的考验，方向是自省忏悔（P094-P152）。",
    "转变二：停止惩罚不顺从，赞许不屈从、赞美服从（P153-P156）。",
    "定义自愿服从五要件，并保留随时叫停的权利与致歉义务（P157-P175）。",
    "以交托之重反问领受者资格：明白后自然获得耐心与忏悔下意识（P176-P195）。",
    "结论：服从能力即爱之能力本质；看懂者才可以下令让孩子去睡觉（P196-P202）。"
   ],
   "concept_usage": [
    {"term": "屈从", "meaning": "搁置并废弃自己的判断，以对实力（实为暴力）的判断替代对是非正误的判断作为遵从前提。", "evidence": "P012", "ambiguity": "与‘顺从’‘服从’在同一段落并用，需靠上下文区分。"},
    {"term": "服从", "meaning": "基于对他人爱的信任或对自身超越性诉求的坚持，自己决定在具体问题上违逆安逸本能的选择。", "evidence": "P027", "ambiguity": "既指形式上服从他人，又说本质上是服从自己的理性／自己（P037、P049）。"},
    {"term": "顺从", "meaning": "上位概念，涵盖服从与屈从两种机制（P011）。", "evidence": "P011", "ambiguity": "有时与‘服从’近义互换，如P065‘一切顺从牢牢的锁定在服从的定义之内’。"},
    {"term": "爱", "meaning": "能被子女本能洞察动机的、可靠的爱；是第二种服从的依据。", "evidence": "P038", "ambiguity": "未下定义；又被说成世界得以被造的原则（P198），二者关系未说明。"},
    {"term": "本能（天赐本能／恐惧本能）", "meaning": "自然赋予、先于理智运作的防御机制，能洞察他人极力掩饰的敌意。", "evidence": "P120", "ambiguity": "文中称其判断‘不是你的子女作出的’，主体归于本能而非人（P125）。"},
    {"term": "自然", "meaning": "被人格化的主宰者：给出客观反馈、检验父母资格，甚至‘下令’启动自毁机制。", "evidence": "P062", "ambiguity": "与生物学意义的自然关系未说明，属形而上断言。"},
    {"term": "事实的语言／事实是神的语言", "meaning": "父母的实际行为向子女灵魂传达的讯息，压过口头说理。", "evidence": "P092", "ambiguity": "‘神’的所指未定义，属宗教语汇借用。"},
    {"term": "权柄", "meaning": "父母／上位者所领受的、被自愿服从的资格，被称为凡人领受不起的权柄。", "evidence": "P140", "ambiguity": "授予者被归于‘自然’或‘ta’，未明确。"}
   ],
   "examples_and_targets": [
    "P003-P008：对‘很多人’暴力教育观的复述，含‘能屈能伸’‘趋吉避凶’‘君子报仇，十年不晚’等俗语——作者反驳对象，非作者主张。",
    "P020、P042：‘媳妇熬成婆’与‘魔王／小鬼’——作者用语，描摹屈从者的补偿心理。",
    "P024：‘高级的膝盖’‘膝跳反应级别’——作者比喻。",
    "P034-P036：志愿兵参军服从指挥链、加入认同宗旨的组织、与企业或个人签约——作者例证（第一种服从）。",
    "P044：‘1+1=2’与‘人口尺手’——作者比较；后者疑为笔误或特定典故，待核。",
    "P051：子女服从父母、俘虏服从俘获者、被捕罪犯服从狱卒——作者例证（第三种情况）。",
    "P053：受重力束缚、墙与悬崖的阻隔——作者类比，说明无选择余地。",
    "P062：‘永动机’不可行——作者比喻，指拒绝接受自然限制者虚度人生。",
    "P067-P069：屈从组织的‘隐形权力栅栏’与‘降将’在战胜集团居高位——作者例证，说明组织规律。",
    "P102-P104、P148-P151：‘城墙／城门’隐喻与‘厉鬼’‘同归于尽’——作者比喻。",
    "P110、P122：抽十张彩票都没中；兔子、老鼠、苍蝇的恐惧本能——作者类比。",
    "P162-P164、P167：军人不服从由国家（经军事法庭）判断、封建领主掌判断权；死刑为唯一例外——作者例证与边界设定。"
   ],
   "conditions": [
    "让步的适用范围：‘人如果要成为社会的人’才必须学会协作与顺从（P010）。",
    "屈从定义依赖‘作为遵从指示的前提条件’这一限定（P012）。",
    "前两种服从以‘决定终止服从的自由’与约定好的退出程序为前提（P046、P048）。",
    "第三种服从的条件：‘受到管辖的原因是超越自己的选择的’，并延伸至一切没有留下不顺从选择的场合（P050、P052）。",
    "是否服从被限定为各人自己的选择，且明确反对将其变成强令他人的‘共识’（P056-P057）。",
    "暴力教育的因果为条件式：‘因为只要你这么做’，即向子女宣告‘服从就是屈从’（P089）。",
    "父母的资格为条件式：‘你被证明没有因这完全正当的不屈服而沮丧、暴躁和愤怒’（P107）。",
    "五要件的时间限定：‘在服从承诺有效期间’，以‘按照程序声明停止服从之前’为界（P159、P161）。",
    "唯一例外：自愿接受裁决不包括死刑（P166）。",
    "结尾双重条件：若看懂则可以下令；若没看懂或因任何原因不认同，最好不要随便下令（P199、P202）。"
   ],
   "rhetoric_and_tone": "全篇第二人称‘你’直接训诫父母／上位者，设问与反问密集（‘无懈可击，对吗？’P009、‘你看懂了吗？’P114、‘凭什么要“公平”？’P137）。大量宗教—道德语汇（神、灵魂、忏悔、圣杯、罪、权柄、僭越者即为敌人），比喻成体系（高级的膝盖、城墙与城门、永动机、彩票、降将）。以‘服从／屈从’概念对举驱动全篇论证，对暴力教育观持明显讽刺与批判，对父母则训诫中含劝慰；结尾由论述转为近乎宣战式断言。全篇用‘ta’作无性别第三人称，含口语化与夸张成分。",
   "unresolved_questions": [
    "题面‘家长可以强迫孩子去睡觉吗’直到P199才被回应，未区分‘强迫’的具体形式（命令、体罚、经济手段）与子女年龄段。",
    "P038-P039称‘对爱的敏感性和替代抗拒的策略，后面会专门阐述’，但本文未见该专门阐述。",
    "P062由‘实力的绝对差异’推出‘对方从自然手里获得了管理你的特殊许可’，该推理前提未加论证。",
    "P129称自然‘会下令让你的子女……启动自毁机制’，主体与机制不明，属需外部核查的形而上断言。",
    "P044‘人口尺手’疑为笔误或特定典故，无法确定所指；P080‘有意识有意识’重复字照原文保留。",
    "P020、P042以‘媳妇熬成婆’‘魔王／小鬼’描摹屈从者心理，属修辞性断言，无经验材料支持。",
    "自然人化表述（自然‘下令’‘惩罚’）与生物学意义的自然之关系未说明，可能影响解释。",
    "published_at为2021-06-05、updated_at为2022-04-08，正文是否有改动、改动何处，语料未提供版本差异信息。",
    "全文以亲子关系开篇，中段大量转向军队、契约、国家等一般支配关系，两类关系如何统一论述未明确说明。",
    "五要件中‘自愿接受裁决（死刑除外）’（P166-P167）与‘以生命为赌注反抗’的终极自由（P054）之间的关系未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "父母和子女之间存在着一个管理和服从管理的关系", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "很多人已经将这视为了一种必不可少的暴力的教育", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P008", "quote": "家长当然有权利——甚至是有义务——让子女适应强迫", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "父母是必须要尝试构造子女的某种顺从机制的", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P011", "quote": "你正在构造的顺从，到底是一种服从，还是一种屈从？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "转而以对实力——实则是暴力——的判断代替对是非、正误的判断", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "它的每一次奏效，都是当事人暴力和理性的双重失败", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P019", "quote": "ta怎么能不学会崇拜暴力、轻视理性、甚至仇视独立人格呢？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P021", "quote": "建立屈从机制本身将会使得教育本身变得低效、甚至变成不可能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P023", "quote": "而是在锻炼捕获信号、反射性反应的能力", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "服从是基于对他人的爱的信任或对自己超越性诉求的坚持", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P037", "quote": "在形式上虽然是在服从其他人，但在本质上是在服从自己的理性", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P038", "quote": "相信对方对自己的爱足够可靠", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P040", "quote": "这就是学习的意志基础", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P041", "quote": "这个人将失去绝大多数的经验增长机会", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P042", "quote": "最终的结果，反而恰恰是要无穷尽的“被迫屈从”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P044", "quote": "但你不能不明白要学习就必须要服从教导", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P046", "quote": "都包含了一项至关重要的要素——那就是决定终止服从的自由", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P048", "quote": "没有约定这一程序的契约是不完备的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P049", "quote": "不但不是人自由的失败，反而是人自由的实现", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P050", "quote": "理性的选择有意义、有原则的服从，而不是无意义、无原则的反抗", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P053", "quote": "在本质上与受到重力的束缚、受到墙和悬崖的阻隔没有区别", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P055", "quote": "人类缺少的并不是自由本身，而只是廉价的、足够“经济”的自由", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P058", "quote": "但你没有任何权利和立场去指责拒绝与你做同样选择", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P060", "quote": "本身就是一种被企图的奴役", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P062", "quote": "对方从自然手里获得了管理你的特殊许可", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P064", "quote": "这是一个服从的形式和艺术问题，而不是一个服从或者不服从的问题", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P066", "quote": "无论在合作成本上还是在产出效益上都有数学上极为显著的优势", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P069", "quote": "这其实就是何以某些“降将”反而可能同样在战胜集团内身居高位的内在原因", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P073", "quote": "也是人类教育的最大奥秘——对动机的再定义", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P085", "quote": "服从精神、服从自觉和服从必要的技能都是你教育的永恒的终点", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P089", "quote": "向可以凭本能倾听这现实的语言的子女说“服从就是屈从”", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P092", "quote": "因为事实是神的语言。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P095", "quote": "不屈从却是正确的、健康的、甚至至关重要的本能", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P100", "quote": "它是一种客观的筛选“有资格得到我的服从”的天然机制", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P107", "quote": "你才有获得试探性的服从的资格", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P116", "quote": "这其实不是对子女的考验，而是对你的考验。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P131", "quote": "我在哪里流露出了我不自知的威胁性？", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P142", "quote": "而绝不会是你真的绝对正义，毫无过错", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P146", "quote": "唯有你自知不配，你才可以被视为配得", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P147", "quote": "身为领袖，道歉比责罚强大", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P154", "quote": "而不屈从是应该赞许的勇气，不是需要惩戒的叛逆", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P175", "quote": "这五条，合起来构成自愿服从的全部要件。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P166", "quote": "无论那裁决是什么，只有一个例外——就是死刑。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P170", "quote": "ta有权在惩罚真的落下之前宣布服从不再有效", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P184", "quote": "你只是在遵循本来就存在的规律", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P189", "quote": "都是值得全部赞美的胜利", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P196", "quote": "因为它就是爱的能力的本质", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P199", "quote": "那么你就可以下令让你的孩子去睡觉", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P200", "quote": "命令，是专一给予谦卑者、忏悔者、爱人者的特权", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P202", "quote": "那么你最好不要随便下令，以免自取其辱，两败俱伤。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育学／家庭教育", "伦理学（服从与自由）", "社会心理学（权威与顺从）", "组织理论", "政治哲学（支配与反抗）"],
   "issue_candidates": ["家长能否强迫孩子", "服从与屈从之别", "体罚与暴力教育", "权威的正当性与资格", "自由与自愿服从", "对不服从的定性"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "经验总结与劝诫", "批判"],
   "object_candidates": ["父母／家长", "子女", "志愿兵与军队指挥链", "国家与军事法庭", "封建领主", "俘虏与罪犯", "组织与契约关系"],
   "working_keywords": ["服从", "屈从", "顺从", "不屈从", "自愿", "权柄", "本能", "爱", "暴力", "动机的再定义", "人格圣杯", "永动机", "隐形权力栅栏", "降将", "自然"]
  },
  "notes": "无图片节点（IMG 0），正文202段与lexical结构无text-lexical divergence（node_counts: paragraph 205 / quote 1 / heading 4）。brief为正文P001-P002摘录，未用于支持主张。P003-P008是对‘很多人’暴力教育观的复述，已标注为opponent_view，未归给作者。P048在lexical中为quote节点但无外部引文署名（以‘顺便’起句），按作者行文处理。P080‘有意识有意识’重复字、P044‘人口尺手’照原文保留，已在unresolved_questions登记。published_at 2021-06-05与updated_at 2022-04-08不同，语料无版本差异信息。"
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
