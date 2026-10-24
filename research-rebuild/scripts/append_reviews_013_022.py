import json
from pathlib import Path

out = Path(__file__).resolve().parent.parent / "reports" / "independent-reviews.jsonl"
rows = [
    {
        "article_id": "5a32a445-202b-593a-a880-21c3716cd9cc",
        "batch_id": "r001-b0024",
        "packet": "packets/independent-review/013-5a32a445.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P295全部正文节点、lexical结构和21个图片索引；未发现文字段落遗漏。P078/P080是视频链接，P294-P295是答集链接标题，均已按正文存在但不将链接目标内容当作已读。图片内容尚未核验。",
        "attribution": "提问‘我用5G网络可以干什么？’属于提问者。作者在P001-P019反驳‘4G就够’的对立观点，在P021-P076、P081-P293分别提出公司协作、交通、信息架构、医疗、制造和参数进步的解释或预测；P078/P080仅为视频链接，P294-P295仅为外部答集标题。作者引用的‘上头’判断（P116）、历史人物/企业数据和技术数字仍是作者转述或陈述，不应改写成研究者已证实事实。",
        "evidence": "初读E001-E063所指段落均可在P001-P293找到相应连续文字，主要位置顺序正确；但部分char范围覆盖整段而非最小引文，且E027、E063分别涉及作者转述的‘上头断言’和二难式假设，不能据此当作作者无条件事实主张。P078/P080及P294-P295没有可用于证明链接目标内容的文字证据。‘5G将改变公司形态’、无人驾驶样式、医疗与云工厂等应保留为作者判断/预测，带宽、基站、人口与历史数字应标记为待外部核查命题。",
        "images": "pending",
        "image_note": "IMG001-IMG021均未确认可见内容、图中文字、图表或其与相邻段落的对应关系；不根据asset URL、文件名、标题或正文上下文臆测。视频链接也未作为图片或视频内容完成核验。",
        "independent_judgment": "文字覆盖基本完整，初读抓住了文章从网络容量论证转向社会/产业预测的结构，但应进一步拆分作者断言、预测、转述和反方观点，尤其不能把P116的‘上头断言’或P124的对立观点归成作者事实立场。P089的四万八千倍是作者算式，尚未核算其前提；P286-P293的迦太基类比是作者论证，不等于历史因果已被独立证实。图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "b95e3891-a76b-5252-86ca-12733a306294",
        "batch_id": "r001-b0048",
        "packet": "packets/independent-review/022-b95e3891.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P268全部正文节点、lexical结构和1个图片索引；未发现文字段落遗漏。P204与P268是平台卡片/链接标题，正文不在本篇；图片IMG001尚未核验。",
        "attribution": "提问‘纳粹为什么那么仇恨犹太人？’属于提问者。P001-P003是作者提出问题背景及‘约’的解释框架；文中关于犹太教、基督教、律法、德国反犹、纳粹、中国与美国的判断均是作者陈述、作者转述或作者行动主张，须按段落和语气分开。P004-P019等经文/教义材料属于被引文本或作者转述，不应直接归为作者本人信念；P204和P268只是关联条目标题。",
        "evidence": "初读E001-E043均可在对应P段找到连续片段，段落顺序总体正确；但若干引文只截取短语，不能独立支撑其扩展后的历史、宗教或群体概括，尤其E003、E006-E010、E028-E032及E036-E042需要保留‘作者转述/作者判断’模态。‘十五万犹太裔士兵’、路德与纳粹因果、人口比例等数字和历史断言只能记录为作者提出的待核查命题。",
        "images": "pending",
        "image_note": "IMG001未确认其可见人物、文字、图表或与P段落的关系；不根据URL、文章标题或上下文推测图片内容。",
        "independent_judgment": "文字覆盖完整，初读正确识别了文章由‘约’和律法观念展开至反犹、文明竞争及中国行动策略的论证链，但需更严格区分经文原文、作者对宗教的转述、作者自己的概括与规范性主张。涉及‘犹太人/基督徒’群体的广泛归纳和德国历史因果均不能在独立复核阶段当作研究者结论，也不应加入研究者价值评判。图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
]

seen = {json.loads(line)["article_id"] for line in out.read_text(encoding="utf-8").splitlines() if line.strip()}
with out.open("a", encoding="utf-8", newline="\n") as handle:
    for row in rows:
        if row["article_id"] not in seen:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
