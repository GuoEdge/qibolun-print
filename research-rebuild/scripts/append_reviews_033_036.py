import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "independent-reviews.jsonl"

records = [
    {
        "article_id": "3f4efcaa-c89d-554b-bcc8-5686ed8527e6",
        "batch_id": "r001-b0070",
        "packet": "packets/independent-review/033-3f4efcaa.md",
        "reviewer": "codex", "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P022全部正文节点、lexical结构和IMG001；文字节点无遗漏。P001-P005提出心理洁癖及按类弃绝，P006-P010展开类别累乘，P011-P020以切割地球的夸张换算收束，P021-P022为结尾节点。",
        "attribution": "提问者问如何理解‘心窄路不宽’。作者以第一人称泛化‘人都是有心理洁癖的’开篇，将断绝某人解释为连同其所属类别一并弃绝；P006-P008的问答是作者自设的类别举例，P009-P010是作者的累乘推演，P011-P020是夸张的面积/体积比喻，P022称其为‘刀神的一生’，均属作者论述，不是外部统计或事实报告。",
        "evidence": "E001-E011均能在对应P段找到连续原文，位置与主张基本匹配。E006的引文覆盖P009较长句但核心‘一路累乘’准确；E008-E010支持的是作者设定下的算术比喻，不足以证明真实人口比例或实际社会关系。‘人都是有心理洁癖’和‘弃绝十八个人即可装进小格子’应保留作者断言/修辞模态。",
        "images": "pending", "image_note": "IMG001未进行视觉核验；不依据asset URL、标题或正文推测其可见内容、文字或与论证的关系。",
        "independent_judgment": "初读正确抓住‘心理洁癖—按类弃绝—累乘—小格子’链条，但将数学换算与经验事实混读的风险需要标明。文章没有给出类别相互独立、比例可直接相乘的统计依据，‘大半个世界’及面积换算是作者的讽喻性演示。图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "c4bab8ec-36c8-546c-84b2-a9fa20cd813d",
        "batch_id": "r001-b0074",
        "packet": "packets/independent-review/034-c4bab8ec.md",
        "reviewer": "codex", "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P087全部正文节点、lexical结构和IMG001；文字节点无遗漏。全文依次覆盖从众流/从村流、先知流、稳健流、基础学科与名校选择、强基计划及中国科研体系预测，P087为收束反问。",
        "attribution": "提问者问强基计划最终如何收场；作者借题讨论人生前途并提出三种策略（P001-P005）。P007-P021是作者对从众流及‘从村流’的批评，P022-P029讨论先知流及自己下注，P030-P038提出稳健流和年龄/定位判断。P039-P045转述并反驳‘有钱人孩子不学基础学科’等说法；P046-P056是作者关于中国科研体系、强基计划和未来就业的判断/预测；P057-P066讨论名校、专业与尖酸刻薄意见；P068-P087转述‘基础学科没前途’等反方说法并继续作作者预测。",
        "evidence": "初读E001-E054均可定位到连续原文，段落归属总体正确。需把‘骗人入坑’（P049）、‘基础学科没前途’（P068）等明确标为被转述/被反驳观点；‘大批重点单位一抢而空’（P054）、‘待遇最好、职业最稳定’（P056）及科研体系必然改变是作者预测或判断，不是已验证事实。‘买研究报告才算真正从众’是作者设置的门槛，不是方法学定义。",
        "images": "pending", "image_note": "IMG001未进行视觉核验；不根据图片URL、标题或上下文推断图片是否为表格、人物或论据材料。",
        "independent_judgment": "初读对三种策略和主要证据位置的索引基本准确，但将作者的宏观预测、规范建议和经验性断言压成确定结论的风险较高。P047-P056涉及中国科研政策、国际竞争与就业，需保留作者预测模态并另行外部核查；‘基础学科’与‘应用学科’的价值排序是作者立场，不启动正式分类。图片核验前保持needs_reread。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "2867ed0d-0c0c-5bb4-a328-50f679d93142",
        "batch_id": "r001-b0077",
        "packet": "packets/independent-review/035-2867ed0d.md",
        "reviewer": "codex", "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P030全部正文节点、lexical结构和IMG001-IMG002；文字节点无遗漏。P001-P010论渡江补给和歼灭守军，P011-P025论会战之地，P026-P030为战略收束。",
        "attribution": "提问者问长江很长为何仍强调天险、其他地方能否渡河。作者主张难点不在找到渡口，而在隐蔽通过、建立滩头、跨江补给及渡江时歼灭守军（P001-P010）；随后把攻击方策略概括为寻找能迫使守军集中兵力的‘会战之地’（P011-P025），并以‘不是过江地方难得，而是毕其功于一役的地方难得’及‘渡江之战就是灭国之战’收束（P029-P030）。",
        "evidence": "E001-E025均能在对应P段找到连续原文，位置基本准确；E003、E009、E011等表达的是作者的假设或战略推演，不能直接当作所有战争的普遍事实。‘古代战争最大的奥妙’、‘常常渡江之战就是灭国之战’是作者概括，需与具体历史案例和军事史证据分开。P006关于水寨、船只和水军的比较也是论证性设想。",
        "images": "pending", "image_note": "IMG001-IMG002未进行视觉核验；不依据asset URL或正文推断地图、战场、示意图等可见内容。",
        "independent_judgment": "初读较完整地抽取了从渡河可行性到会战地点的论证链，但对‘古代战争’‘凡渡江之战’等全称表达需要保留其作者概括性质。本文未提供史例、数据或出处，历史与军事判断均应标为待外部核查命题；图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "9d092af8-9d49-5ddb-a70e-105515d496b0",
        "batch_id": "r001-b0077",
        "packet": "packets/independent-review/036-9d092af8.md",
        "reviewer": "codex", "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P005全部正文节点、lexical结构和IMG001-IMG003；文字节点无遗漏。作者按宫观、一般民居、大宅、架空地板民居与回廊分项回答。",
        "attribution": "提问者问中国古代建筑如何处理高差。作者P001主张宫观抬高地面并以夯土台找平，P002讨论一般民居在高处找平及品级限制，P003描述大宅的坡度与排水配合，P004描述柱框架架空地板，P005称回廊基本依地势而建；全部为作者说明，未引入独立来源或他人观点。",
        "evidence": "E001-E010均为对应P001-P005的连续原文，能够支持初读所列五类做法。引文支持的是文章中的概括，不足以证明‘都会’、品级制度、排水模式或架空结构在中国古代各时期各地普遍成立；这些范围与历史技术含义需外部核查。",
        "images": "pending", "image_note": "IMG001-IMG003均未进行视觉核验；不根据URL、文章类别或上下文补写建筑、地形、排水或结构图像内容。",
        "independent_judgment": "初读基本覆盖五段，但status为full_text_checked=False，复核后文字节点已完整回看。应将‘宫观类建筑都会’、‘品级制度不允许平民造台’等表述保留为作者概括，不能扩展成无条件历史规律；‘高差’的建筑史分类、夯土/须弥座/架空地板的具体实例待外部资料与图片核验。保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
]

existing = []
if OUT.exists():
    existing = [json.loads(line) for line in OUT.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
ids = {r["article_id"] for r in existing}
new = [r for r in records if r["article_id"] not in ids]
with OUT.open("a", encoding="utf-8", newline="\n") as f:
    for record in new:
        f.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
print(json.dumps({"existing": len(existing), "appended": len(new), "total": len(existing) + len(new)}, ensure_ascii=False))
