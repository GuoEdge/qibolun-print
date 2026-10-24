import json
from pathlib import Path

out = Path(__file__).resolve().parent.parent / "reports" / "independent-reviews.jsonl"
rows = [
    {
        "article_id": "4cbed42c-3df1-5042-bc95-625b46e3256e",
        "batch_id": "r001-b0055",
        "packet": "packets/independent-review/029-4cbed42c.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P010全部正文节点、lexical结构和IMG001；未发现文字遗漏。P010‘图侵删’只是图片删除提示，图片中的推荐书目清单尚未核验。",
        "attribution": "提问者问高中生适合读什么书。作者P001-P006建议从科学经典、自然史和自然史学出发，把客观世界及其规律称为不同意识形态可理解和协商的common ground，并提出先理解世界再探索哲学和价值观；P007-P009又明确说不要把这些内容视为真理，而是人类所能达到的‘有质量的错误’。上述均为作者建议、论断或限定，不是研究者结论。",
        "evidence": "初读E001-E009均可在对应P段找到连续原文，段落位置正确，足以支持作者建议及其‘不要视为真理’的限定；但‘自然史学经典’具体指哪些书，正文没有列出，不能从IMG001 URL或上下文补足。‘客观世界规律是common ground’和‘有质量的错误’是作者的哲学表述，不能仅凭引文当作外部共识或经验事实。",
        "images": "pending",
        "image_note": "IMG001未确认推荐书目、封面、文字或排版内容；不依据‘下面这个推荐的系列’、URL或正文猜测图片清单。",
        "independent_judgment": "初读对文章主旨和模态把握基本准确，但需把‘科学经典’与图片中可能存在的具体书目分开；P003-P006是规范性建议和作者认识论框架，P007-P009是对其确定性的限制。图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "c947b0a0-3a44-571d-bef7-8663f537fb19",
        "batch_id": "r001-b0056",
        "packet": "packets/independent-review/030-c947b0a0.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P090全部正文与list节点、lexical结构和IMG001-IMG010；未发现文字节点遗漏。P001-P002为专栏/投稿说明，P027以后为未完的训练科目清单；多处‘下图’‘如下’依赖图片，图片尚未核验。",
        "attribution": "提问者问年轻人最核心的能力。作者P003将其界定为无歧义、完备、简洁的表达能力，并在P005-P007定义无错、无漏、无费；P008-P026论证该能力与判断力、学习理解探索创造能力及作者所谓精英划分的关系。P027-P090列出表达、图形、编码、建模、素描、3D、信息分类等训练及练习。‘七十二绝技’‘小无相功’和‘精英与非精英’均是作者比喻或分类，不是外部标准。",
        "evidence": "初读E001-E027均可定位到连续原文，位置基本准确；E022的引文只截取P051中‘尽可能简短’，完整要求还包括同一集合中唯一且他人可复算一致，需结合P051全文理解。P028-P029、P048-P049、P057-P067、P075-P085等重复list节点是原始结构重复，不应去重为遗漏。‘直接关系到高度’、‘唯一真正需要关心指标’、训练后应观察到准确迅速提升等属于作者论断或预期，不能凭引文视为已验证因果。",
        "images": "pending",
        "image_note": "IMG001-IMG010未确认房型图、参考图、示例命名、透视/产品图、街景或分类示例的可见内容及文字；不根据‘下图’‘如下’或asset URL补足图像事实。",
        "independent_judgment": "初读抓住核心能力定义和训练清单，且full_text_checked为真；但应保留P090‘未完，待续’这一边界，不能把清单当成完整课程。P008、P013、P016-P017、P026及P035/P043是作者的因果、上限或预期观察表述；P001-P002是栏目语境，不是核心能力主张。图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "848b2ead-d70b-55d5-9858-690fc5a2a227",
        "batch_id": "r001-b0057",
        "packet": "packets/independent-review/031-848b2ead.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P012全部正文节点、lexical结构和IMG001；未发现文字遗漏。P007为独立引语，P008为紧接其后的作者反问/戏仿，需与P001-P006关于儒家礼乐的论证分开。",
        "attribution": "提问者问现在是否是礼崩乐坏的时代。作者P001-P006批评其所概括的儒家/孔子理想社会框架，认为其把稳定不变的礼乐当作最终理想，并以周公制礼作乐已经完成为其归纳对象；P006进一步提出这种理想会压制发展和变化。P007是被引的家庭式怀旧话语，P008是作者借此作的戏仿反问；P009-P012是作者的概括性断言和反事实结论。",
        "evidence": "初读E001-E011均可在相应P段找到连续片段，位置准确；但E002-E005描述的是作者对儒家立场的归纳，并非孔子原文或完整儒家思想的独立证据。‘任何时代都注定礼崩乐坏’和‘全员NPC’分别是作者的概括断言与反事实修辞，不应外推为历史规律或现实状态事实。",
        "images": "pending",
        "image_note": "IMG001未确认其是否为配图、引文图或其他内容；不依据正文或asset URL推测可见人物、文字及语境。",
        "independent_judgment": "初读正确识别文章没有直接给出当下时代的事实评估，而是围绕理想秩序的可变性展开批评；需进一步将P007的引语、P008的戏仿和P009-P012的作者断言分层。‘儒家’‘孔子’的归纳范围及历史准确性待外部核查；图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
    {
        "article_id": "12b7d5cf-a944-57e4-ba3e-02db106ed7c0",
        "batch_id": "r001-b0064",
        "packet": "packets/independent-review/032-12b7d5cf.md",
        "reviewer": "codex",
        "reviewed_at": "2026-09-21",
        "coverage": "已回看提问字段、P001-P031全部正文节点、lexical结构和IMG001；未发现文字遗漏。P011-P014处理估计误差与基线修正，P015-P023介绍当值法及其作者评价，P024-P031讨论无法估算进度时的适用边界。",
        "attribution": "提问者问什么是执行力。作者以‘推动进度条的神秘力量’作比喻性界定，主张多数人缺少进度条；P006-P014提出按关键路径估计工时的工时法，P015-P023提出以分摊工资确定步骤权重的当值法，并称后者更精确、分别对应技术专家与管理者训练。P024-P031给出专业/兴趣区分、退后一步或求助学习的建议。‘关键路径’技术含义被作者要求读者自行查询，文章未展开定义。",
        "evidence": "初读E001-E016均可定位到连续原文，位置正确；E002同时概括P003和P004，需分别保留‘大部分人没有进度条’与‘打游戏因有进度条’两条主张。E003-E004与E015共同说明工时法按估计工时计算、实际工时只记录且下次修正，不能遗漏P012的限定。E005只覆盖P016，完整当值法还需结合P018-P020的工资摊平、权重和技能成本。作者称当值法‘更精确’、三重进阶‘最终指向一番事业’及‘胜任’标准，均为作者评价或建议，不是验证后的管理学定律。",
        "images": "pending",
        "image_note": "IMG001未确认是否为进度条示意、表格或其他配图；不依据文章方法描述、URL或上下文臆测图片内容。",
        "independent_judgment": "初读对两种方法和适用边界的概括基本准确，但需要把P012的‘估计错误怎么办’回答、P020的技能成本例外和P029允许较大误差的限定纳入同一证据链。‘执行力’在本文中是作者的项目进度管理隐喻，不能直接等同于通用心理学定义；图片核验前保持needs_reread，不启动正式分类。",
        "conclusion": "reviewed_needs_revision",
    },
]
seen = {json.loads(x)["article_id"] for x in out.read_text(encoding="utf-8").splitlines() if x.strip()}
with out.open("a", encoding="utf-8", newline="\n") as f:
    for row in rows:
        if row["article_id"] not in seen:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
