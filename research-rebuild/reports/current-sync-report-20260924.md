# 岐伯论分类推进同步报告

更新时间：2026-09-24

## 当前语料与覆盖

- 当前 v2 语料共4,305篇；分类候选和打印索引均为4,305个唯一ID。
- 官方目录快照的最近同步日期为2026-09-21。
- 人工主专题决定4,305篇，其中 `manual_confirmed` 4,079篇、`manual_provisional` 226篇；决定表覆盖率100%，当前仍有226篇处于暂定/待补证队列。
- 图片库存共765张，已完成人工视觉复核436张，涉及129篇文章；仍有329张、125篇文章待复核。图片复核只记录可见内容与图文关系，不替代OCR或外部事实核验。
- 当前原始JSONL的SHA-256仍为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`，原文未被改写。

## Round 101

- 完成50篇无图文章全文分类，正文86,182字，最长6,142字；44篇主题确认，6篇因正文未完或疑似断尾保留临时状态。
- 批次决定表经16篇主线程抽核，另有独立审读者抽查15篇。复核发现《反驳》更应以通用论证方法为主，因此由A05/A03修订为A03/A05；《认错》因标注未完保留临时状态，待续文后复核。
- 抽核记录：[round101-independent-spotcheck.md](round101-independent-spotcheck.md)；决定表：[round101-decisions.tsv](round101-decisions.tsv)；正式表：[print-topic-manual-decisions-v2.csv](../data/print-topic-manual-decisions-v2.csv)。
- 追加后已重建候选、全量分类、打印索引、人工抽样和实时待分类队列。人工决定审计通过；专题结构审计 pass=true，错误0、警告0。

## Round 102 已完成

- 从301篇队列中按无图、最多50篇及90,000字预算选出42篇；合计89,936字，最长9,223字。前后半分别全文审读，最终38篇 manual_confirmed、4篇因正文未完保留 manual_provisional。
- 抽核修订移除4篇中仅由修辞/例证支撑的副码，并将《受伤害》由A01主码调整为A06主码；抽核同时将安全/法律/心理主张与主题判断分开。详见[Round 102抽核报告](round102-independent-spotcheck.md)和[合并决定表](round102-decisions.tsv)。原始分段决定表保留供追溯。
- 已正式追加并重建候选、分类索引、打印索引、抽样和实时待分类队列。人工决定审计通过：4,046条、唯一ID 4,046、错误0；专题结构审计 `pass=true`、错误0、警告0。分类索引及打印索引均覆盖4,305个唯一ID。
- 批次：[live-manual-budget-batch-v2-round102-90k.csv](live-manual-budget-batch-v2-round102-90k.csv)；全文：[round102-fulltext.json](round102-fulltext.json)。

## Round 103 已完成

- 从无图且正文可读队列选出36篇，正文89,424字，最长6,058字。分段审读、主线程抽核和独立高风险盲审完成；经边界裁定后29篇 manual_confirmed、7篇 manual_provisional。详见[Round 103抽核报告](round103-independent-spotcheck.md)及[合并决定表](round103-decisions.tsv)。
- 追加后决定审计通过：4,082条且唯一ID 4,082、错误0；专题结构审计 `pass=true`、错误0、警告0。分类与打印索引仍覆盖4,305个唯一ID。
- 批次：[live-manual-budget-batch-v2-round103-90k.csv](live-manual-budget-batch-v2-round103-90k.csv)；全文：[round103-fulltext.json](round103-fulltext.json)。

## Round 104 已完成

- 从刷新后的无图、正文可读队列中，按最多50篇及90,000字预算选出41篇；正文89,458字，最长5,888字。两位审读者分段全文分类，独立审读者盲审9篇高风险样本，主线程对高风险及跨专题边界回读并裁定。
- 最终36篇 `manual_confirmed`、5篇 `manual_provisional`。暂定项均为正文断尾或明确未完；《子女的隐私》副码从盲审建议A03裁定为A04；《黄色玩笑》定为A02主/A07副且保留暂定。第16篇风险备注补明“忍耐即爱”不证明关系安全或适合结婚。
- 详见[Round 104独立抽核报告](round104-independent-spotcheck.md)及[合并决定表](round104-decisions.tsv)；分段原表保留：[前20篇](round104-firsthalf-decisions.tsv)、[后21篇](round104-secondhalf-decisions.tsv)。
- 追加后正式表4,123条、唯一ID 4,123；人工决定审计 `pass=true`、错误0。分类和打印索引覆盖4,305个唯一ID；专题结构审计 `pass=true`、错误0、警告0。
- 当前覆盖4,123/4,305（95.77%），待分类182篇。原始JSONL哈希未变；官方目录快照仍更新至2026-09-21。作者的事实、法律、医学、政策与安全主张未外部核验，不因主题确认而视为已证实。
- 批次：[live-manual-budget-batch-v2-round104-90k.csv](live-manual-budget-batch-v2-round104-90k.csv)；全文：[round104-fulltext.json](round104-fulltext.json)。

## Round 105 已完成

- 从182篇刷新队列筛出104篇无图、正文可读文章；在不超过50篇、90,000字的约束下选择38篇，合计89,239字，最长12,953字。其余66篇仍留在原待分类池中。
- 按正文长度而非篇数均分为前15篇44,050字、后23篇45,189字，分段全文审读；另对10篇跨段高风险样本作独立盲审。盲审特别提示《打骨折》的未成年人伤害处置、《死亡》的未完及史实论断、《道法自然》的活体动物伤害计划。
- 主线程按主题中心复核边界：将《电车难题》定为A11/A10，《长生不死的脑残》定为A19/A03，《老有所依2》定为A19/A09，《拿住不抛》副码由A13改为A01；《权利的总和》《道法自然》保留A11主码，将动物议题列为A18副码。《紧追不放》维持A06/A02，因亲密关系筛选是中心、拒绝边界为关键次轴。
- 补强《打骨折》《道法自然》的即时伤害风险备注，并为《长生不死的脑残》《老有所依2》《拿住不抛》《权利的总和》区分作者主张与已验证事实、法律、医疗或金融结论。7篇暂定项均因原文明确未完或断尾，不是因事实主张尚未核验。
- 最终31篇 `manual_confirmed`、7篇 `manual_provisional`。决定表4,161条且ID唯一；人工决定审计 `pass=true`、错误0。全量候选和打印索引覆盖4,305个唯一ID；专题结构审计 `pass=true`、错误0、警告0。待分类队列144篇，覆盖率96.66%。
- 原始JSONL哈希仍为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`，未改写。官方目录快照最近同步日期仍为2026-09-21。
- 详情：[Round 105抽核报告](round105-independent-spotcheck.md)、[合并决定表](round105-decisions.tsv)；分段原表：[前15篇](round105-firsthalf-decisions.tsv)、[后23篇](round105-secondhalf-decisions.tsv)；批次：[live-manual-budget-batch-v2-round105-90k.csv](live-manual-budget-batch-v2-round105-90k.csv)；全文：[round105-fulltext.json](round105-fulltext.json)。
- 为支持按字数平衡拆分，合并脚本现校验两段拼接后与批次ID顺序完全一致，不再要求两段篇数对半：[merge_live_manual_decisions_v2.py](../scripts/merge_live_manual_decisions_v2.py)。

## Round 106 已完成

- Round105后待分类144篇，其中66篇满足无图、正文可读条件。按50篇上限及90,000字预算选择35篇，正文共89,513字、最长5,985字；另31篇无图候选因当前预算未装入本批，仍保留在队列。
- 本批全文核对后按字数平衡拆分为前18篇45,057字、后17篇44,456字；两段完成独立全文分类，另有10篇独立抽样盲审。图像依赖文章未混入本批。
- 独立盲审关注《组织生鲜供应》的医疗/食品安全及交易规则、《反欺凌》的儿童安全与法律断言、《尊师》的服从边界；主线程已把这些风险写入正式决定备注，不以未核验事实改变专题状态。
- 主线程维持或裁定的重点边界包括：《狮子》A06/A02（亲密关系为主、身体/同意为副）、《不破例》A02/A06（性经历与身体/同意是题面中心）、《越界》A07/A03（组织治理为主、论证方法为副）；《组织生鲜供应》《反欺凌》《尊师》《捧杀》因原文明确未完/待完善保留暂定。
- 最终追加31篇 `manual_confirmed`、4篇 `manual_provisional`。人工决定表4,196条、ID唯一；人工决定审计 `pass=true`、错误0。全量候选和打印索引仍覆盖4,305个唯一ID；专题结构审计 `pass=true`、错误0、警告0。待分类队列109篇，人工覆盖率97.47%。
- 原始JSONL哈希仍为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`，未改写；官方目录快照最近同步日期仍为2026-09-21。
- 详情：[Round 106抽核报告](round106-independent-spotcheck.md)、[合并决定表](round106-decisions.tsv)；分段原表：[前18篇](round106-firsthalf-decisions.tsv)、[后17篇](round106-secondhalf-decisions.tsv)；盲审表：[round106-blind-review.tsv](round106-blind-review.tsv)；批次：[live-manual-budget-batch-v2-round106-90k.csv](live-manual-budget-batch-v2-round106-90k.csv)；全文：[round106-fulltext.json](round106-fulltext.json)。

## Round 107 已完成

- Round106后待分类109篇，其中31篇为无图且正文可读文章；本轮已全部选出，正文共75,091字，最长10,454字，未超过50篇和90,000字预算。剩余78篇为图像审读或材料依赖文章，继续留队。
- 本轮按正文长度拆分为前18篇36,831字、后13篇38,260字，分别进行独立全文分类；另抽取10篇高风险/边界样本盲审。图像证据未读时不提升为确认。
- 批次：[live-manual-budget-batch-v2-round107-90k.csv](live-manual-budget-batch-v2-round107-90k.csv)；全文：[round107-fulltext.json](round107-fulltext.json)。
- 最终追加26篇 `manual_confirmed`、5篇 `manual_provisional`；人工决定表4,227条且ID唯一，打印索引、分类索引和抽样投影已同步重建。专题结构审计 `pass=true`、错误0、警告0；打印索引覆盖4,305篇、22个A专题和7个官方根节点。
- 当前待分类队列已刷新为78篇，全部涉及图像审读或首轮复读；不把图像未读文章误报为已完成。人工覆盖率98.19%。
- 独立抽查：[round107-independent-spotcheck.md](round107-independent-spotcheck.md)；10篇中8篇确认、2篇暂定。盲审与主线程仅有《慈善》主码的一项可追溯分歧，保留主线程决定，不覆盖正式表。
- 决定核验：Round107 31/31篇的主码、副码和状态与最新打印索引完全一致；原始JSONL哈希未变；官方目录快照仍更新至2026-09-21。

## Round 108 已完成

- 从Round107后的78篇图像依赖队列中按动态预算选出6篇；正文共29,108字，最长19,154字，未超过50篇和本批30,000字预算。批次：[live-manual-budget-batch-v2-round108-90k.csv](live-manual-budget-batch-v2-round108-90k.csv)；全文：[round108-fulltext.json](round108-fulltext.json)；图片清单：[round108-image-manifest.csv](round108-image-manifest.csv)。
- 前后半各3篇完成独立全文审读，正文主题均可判定，但43张图片全部 `unreviewed/not_started`，因此6篇全部标记 `manual_provisional`，没有因正文可判而伪装成完成。合并决定：[round108-decisions.tsv](round108-decisions.tsv)。
- 主码为：5G A13、斑点狗 A11、弓箭的杀伤力 A12、天网地廊 A13、眼神灵动 A18、你来我来 A13；副码均保留在决定表中，按主题中心而非图片内容扩张。
- 独立盲审：[round108-blind-review.tsv](round108-blind-review.tsv)，6/6主码一致；5G存在A14与A07/A08的副码取向差异，未覆盖主线程决定。军用武器、基础设施、动物生态、通信产业和工业质量等风险均已写入备注。
- 追加后人工决定表4,233条、ID唯一；打印索引、分类索引、抽样投影及实时队列均已重建。专题结构审计 `pass=true`、错误0、警告0；当前队列72篇，全部仍需图像审读/首轮复读。新增通用脚本：[extract_live_manual_batch_v2.py](../scripts/extract_live_manual_batch_v2.py)；含图追加需显式使用 `--allow-images`，并强制暂定状态。

## Round 109 已完成

- 从Round108后的72篇图像依赖队列中按动态预算选出17篇；正文共29,999字，最长3,748字，未超过50篇和本批30,000字预算。批次：[live-manual-budget-batch-v2-round109-90k.csv](live-manual-budget-batch-v2-round109-90k.csv)；全文：[round109-fulltext.json](round109-fulltext.json)；图片清单：[round109-image-manifest.csv](round109-image-manifest.csv)。
- 前9篇和后8篇完成独立全文审读；36张图片全部 `unreviewed/not_started`，因此17篇均标记 `manual_provisional`。合并决定：[round109-decisions.tsv](round109-decisions.tsv)。
- 重点边界包括：《人所不能者》A09主/A04、A01副（生理缺陷与照料/学校应对为轴，不因校园治理字样改成A10）；《镜面不锈钢》A16主/A10、A08副（公关与公共认知为轴）；《演员的自我修养》A03主/A11、A18副；《移星换斗》A12主/A13、A18副；《落草为王》A14主/A07、A13、A15副。
- 独立盲审：[round109-blind-review.tsv](round109-blind-review.tsv)，抽查8篇，主码7/8一致；唯一差异为《镜面不锈钢》（盲审A10、决定A16），已保留为边界风险，不覆盖主线程决定。所有含图文章均遵守“图像未审读不得确认”规则。追加后人工决定表4,250条、ID唯一；打印索引、分类索引、抽样投影及实时队列均已重建。专题结构审计 `pass=true`、错误0、警告0；当前队列55篇，人工覆盖率98.72%。Round109 17/17篇主码、副码和状态与最新打印索引一致。

## Round 110 已完成

- 从Round109后的55篇图像依赖队列中按动态预算选出14篇；正文共29,553字，最长3,909字，未超过50篇和本批30,000字预算。批次：[live-manual-budget-batch-v2-round110-90k.csv](live-manual-budget-batch-v2-round110-90k.csv)；全文：[round110-fulltext.json](round110-fulltext.json)；图片清单：[round110-image-manifest.csv](round110-image-manifest.csv)。
- 前7篇和后7篇完成独立全文审读；42张图片全部 `unreviewed/not_started`，因此14篇均标记 `manual_provisional`。合并决定：[round110-decisions.tsv](round110-decisions.tsv)。
- 重点边界包括：《科目二》A01主/A04副（冷启动信心与焦虑恢复是中心，不改作体育）；《南存北亡》A20主/A12、A17、A11副；《甲醛》A13主/A09、A18副；《下三路》A16主/A03、A12副；《大洪水》A20主/A18、A11副；其余技术、AI、艺术和竞技文章按正文中心分配。
- 追加后人工决定表4,264条、ID唯一；打印索引、分类索引、抽样投影及实时队列均已重建。专题结构审计 `pass=true`、错误0、警告0；Round110 14/14篇主码、副码和状态与最新打印索引一致；当前队列41篇，人工覆盖率99.05%。
- 独立盲审：[round110-blind-review.tsv](round110-blind-review.tsv)，抽查8篇，主码与决定表7/8一致；《南存北亡》盲审偏A12而决定取A20，已作为历史文明/军事秩序边界风险保留。甲醛、俄乌舆论、史前洪水、星舰工程、AI就业和亲子创伤等风险均未被当作已核验事实。

## Round 111 已完成

- 从Round110后的41篇图像依赖队列中按30,000字预算选出15篇，正文共29,637字，最长3,774字；54张图片均尚未完成视觉审读，因此本轮全部保留 `manual_provisional`。
- 前8篇和后7篇完成独立全文审读；盲审抽查8篇，主码与正式决定6/8一致。两项差异为《统战价值》（盲审A12、正式A06）和《兑换银钱的人》（盲审A08、正式A20），作为关系/战争与历史/金融边界风险保留，未覆盖正式决定。
- 重点边界包括：《逼你幸福》A15/A14、《痒了三块钱》A08/A03、《圣蓝》A15/A20/A11、《两罪并罚》A15/A03/A14、《评价表现》A10/A16/A03、《农村的未来》A18/A13/A20/A08；作者的艺术、金融、宗教史、疫情治理、货币战争和农业预测断言均未外部核验。
- 追加后人工决定表4,279条且ID唯一；人工决定审计 `pass=true`、错误0；分类索引、打印索引和抽样投影已重建，专题结构审计 `pass=true`、错误0、警告0。当前待分类队列26篇，人工覆盖率99.40%。
- 盲审表：[round111-blind-review.tsv](round111-blind-review.tsv)；决定表：[round111-decisions.tsv](round111-decisions.tsv)；分段表：[前8篇](round111-firsthalf-decisions.tsv)、[后7篇](round111-secondhalf-decisions.tsv)；批次：[live-manual-budget-batch-v2-round111-90k.csv](live-manual-budget-batch-v2-round111-90k.csv)；全文：[round111-fulltext.json](round111-fulltext.json)；图片清单：[round111-image-manifest.csv](round111-image-manifest.csv)。

## Round 112 已完成

- 从26篇图像依赖队列中按30,000字预算选出11篇，正文共29,890字；41张图片尚未完成视觉审读，因此11篇全部保持 `manual_provisional`。其余15篇留在刷新后的实时队列。
- 按正文长度平衡拆为前6篇14,419字、后5篇15,471字，完成独立全文分类。合并前发现后半文件误重复前6篇，已要求重写为连续第7至11篇；合并脚本随后验证11/11篇ID与批次顺序一致。
- 主码包括：《性侵危机》A11、《大男子主义》A02、《香料》A18、《烦躁》A01、《疯王》A20、《气泡膜》A01、《缺乏创新》A13、《厨房清洁策略》A13、《评头论足》A06、《疗愈艺术》A09、《节省时间》A13。医学、性侵、食品安全、心理健康和历史断言均与专题分类分开记录，未作事实核验结论。
- 追加后人工决定表4,290条且ID唯一；人工决定审计 `pass=true`、错误0；Round112 11/11篇主码、副码、状态与最新打印索引一致。分类索引、打印索引和抽样投影已重建；专题结构审计 `pass=true`、错误0、警告0。当前待分类15篇，人工覆盖率99.65%。
- 决定表：[round112-decisions.tsv](round112-decisions.tsv)；分段表：[前6篇](round112-firsthalf-decisions.tsv)、[后5篇](round112-secondhalf-decisions.tsv)；批次：[live-manual-budget-batch-v2-round112-90k.csv](live-manual-budget-batch-v2-round112-90k.csv)；全文：[round112-fulltext.json](round112-fulltext.json)；图片清单：[round112-image-manifest.csv](round112-image-manifest.csv)。独立盲审：[round112-blind-review.tsv](round112-blind-review.tsv)，抽查6篇，主码3/6一致；差异为《性侵危机》（A10/A11）、《香料》（A09/A18）和《疗愈艺术》（A15/A09），均保留为司法/医疗/艺术边界风险，不覆盖正式决定。

## 后续动作

1. 首轮分类已完成；下一阶段集中处理226篇 `manual_provisional` 的图片视觉审读、正文复读和边界裁定，按证据充分程度提升为 `manual_confirmed`；全库仍有125篇文章含未复核图片，其中72篇同时是 provisional，另有断尾、材料不足和历史理由缺口等非图片原因的 provisional 项。
2. 对当前226篇 provisional 做二次理由清理：其中72篇有图片门槛、88篇材料不完整、49篇进入边界复核；历史理由缺口仍需逐篇补写证据与不确定性说明。Round126至Round130已验证，不能把独立复核意见直接当成事实核验或自动改码。
   可刷新审计：[provisional-reasons-audit-v2.csv](provisional-reasons-audit-v2.csv)；当前重叠标记为图片门槛72篇、需重读98篇、边界复核59篇、历史理由缺口243篇；这些是分诊信号，不自动改变状态。
3. 图片库存的 `width/height` 字段仍是历史元数据缺口；已复核本地图片均可解码，但尺寸不作为当前主题判断依据，后续单独做可追溯的元数据补全。
4. 对Round112-114盲审分歧和高风险条目建立复核清单，优先复核司法/性侵、医疗食品、心理健康、金融、历史宗教、核聚变与战争治理断言；专题分类与事实核验继续分开。
5. 官方目录快照当前截至2026-09-21；若出现新增文章，先同步语料、重算覆盖和队列，再进入图片复核或新增首轮批次。
6. 实时人工复核队列已修正为只排除 `manual_confirmed`，因此当前保留226篇 `manual_provisional` 供图片、正文复读和边界审计继续处理；队列文件：[live-manual-classification-queue-v2.csv](live-manual-classification-queue-v2.csv)。

### Round 113 已完成

- 已从15篇队列按30,000字预算选出12篇，正文共29,942字，含52张待审图片；剩余3篇进入下一轮。前5篇14,772字、后7篇15,170字，完成独立全文分类，12篇全部保持 `manual_provisional`。
- 主码包括：《汉字基准字体》A15、《道德》A03、《不在乎》A01、《SOP》A13、《年号》A20、《辜鸿铭的辫子》A03、《不怯场》A16、《奢侈品》A08、《前途》A04、《执行力》A07、《能力》A04、《直升珠峰》A13。字体文化、道德定义、教育就业、工程安全和历史断言均与专题分类分开记录，未作事实核验结论。
- 追加后人工决定表4,302条且ID唯一；人工决定审计 `pass=true`、错误0；Round113 12/12篇主码、副码、状态与最新打印索引一致。分类索引、打印索引和抽样投影已重建；专题结构审计 `pass=true`、错误0、警告0。当前待分类3篇，人工覆盖率99.93%。
- 决定表：[round113-decisions.tsv](round113-decisions.tsv)；分段表：[前5篇](round113-firsthalf-decisions.tsv)、[后7篇](round113-secondhalf-decisions.tsv)；批次：[live-manual-budget-batch-v2-round113-90k.csv](live-manual-budget-batch-v2-round113-90k.csv)；全文：[round113-fulltext.json](round113-fulltext.json)；图片清单：[round113-image-manifest.csv](round113-image-manifest.csv)。

### Round 114 已完成

- 本轮原队列3篇、正文共17,440字；15张图片已全部下载并逐张视觉复核（15/15，图文一致，0张改变专题判断）。复核记录：[round114-image-review.tsv](round114-image-review.tsv)。
- 主码为：《讽刺》A16、《文物》A13、《可控核聚变》A18；独立盲审分别为A03、A13、A13。图片复核后仅《文物》因正式/盲审主码一致而提升为 `manual_confirmed`；《讽刺》《可控核聚变》保留 `manual_provisional`，等待表达伦理/生态能源与技术主码分歧的后续裁定。图片仅支持可见对象/语境，不替代OCR或外部事实核验。
- 图片库存和批次清单的15条记录已同步为 `reviewed`；OCR仍为 `not_started`。追加后人工决定表4,305条且ID唯一：`manual_confirmed` 3,889、`manual_provisional` 416；人工决定审计 `pass=true`、错误0；Round114 3/3篇主码、副码、状态与最新打印索引一致。分类索引、打印索引和抽样投影已重建；专题结构审计 `pass=true`、错误0、警告0。人工分类队列0篇，覆盖率100%；仍有251篇含图文章需后续视觉复核。
- 决定表：[round114-decisions.tsv](round114-decisions.tsv)；盲审表：[round114-blind-review.tsv](round114-blind-review.tsv)；图片复核：[round114-image-review.tsv](round114-image-review.tsv)；批次：[live-manual-budget-batch-v2-round114-90k.csv](live-manual-budget-batch-v2-round114-90k.csv)；全文：[round114-fulltext.json](round114-fulltext.json)；图片清单：[round114-image-manifest.csv](round114-image-manifest.csv)。

### Round 115 已完成

- 从含图 provisional 队列按图片数量和正文长度动态选出20篇，56张图片全部下载成功并逐张完成视觉复核；复核记录：[round115-image-review.tsv](round115-image-review.tsv)。
- 56/56张图片均无缺失、无重复，未改变任何文章的主专题判断。图片库存和批次清单已同步为 `reviewed`，OCR仍保持 `not_started`，不把图片当作事实核验证据。
- 4篇文章因图片复核补足证据由 `manual_provisional` 提升为 `manual_confirmed`；2篇因司法/技术与边界分歧继续 provisional。追加后人工决定表4,305条且ID唯一：`manual_confirmed` 3,893、`manual_provisional` 412。
- 分类索引、打印索引、人工抽样和实时队列均已重建。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 决定表：[round115-decisions.tsv](round115-decisions.tsv)；图片清单：[round115-image-manifest.csv](round115-image-manifest.csv)；批次：[live-image-review-batch-v2-round115.csv](live-image-review-batch-v2-round115.csv)。

### Round 116 已完成

- 从未复核图片队列按动态图片预算选出18篇，50张源图全部下载成功并逐张完成视觉复核；复核记录：[round116-image-review.tsv](round116-image-review.tsv)。此前生成的14篇/56图草稿未纳入正式结果，正式批次以 `live-image-review-batch-v2-round116.csv`、`round116-image-manifest.csv` 和 `image-review/round116b` 为准。
- 50/50张图片无缺失、无重复，均未改变专题判断；一致性为41张 `consistent`、9张 `limited`，OCR保持 `not_started`，图片不替代事实核验。
- 《地塔》《世交》原先仅因图片未审读而 provisional，本轮视觉证据完成后提升为 `manual_confirmed`；本轮18篇现全部 confirmed。追加后人工决定表4,305条且ID唯一：`manual_confirmed` 3,895、`manual_provisional` 410。
- 分类索引、打印索引、人工抽样和实时队列均已重建。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 决定表：[round116-decisions.tsv](round116-decisions.tsv)；图片清单：[round116-image-manifest.csv](round116-image-manifest.csv)；批次：[live-image-review-batch-v2-round116.csv](live-image-review-batch-v2-round116.csv)。

### Round 117 已完成

- 从当前未复核图片队列按动态预算选出18篇，47张源图全部下载成功并逐张完成视觉复核；复核记录：[round117-image-review.tsv](round117-image-review.tsv)。
- 47/47个图位完成复核，无缺失、无历史批次重叠，均未改变专题判断；其中同文第7/12图为重复源图，不新增独立图像证据。一致性为26张 `consistent`、21张 `limited`，OCR保持 `not_started`，图片不替代事实核验。
- 本轮18篇在图片复核前已是 `manual_confirmed`，因此不以图片证据重复提升状态；本轮仅补齐图像证据链，未改变主码、副码或人工状态。
- 分类索引、打印索引、人工抽样和实时队列均已重建。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 当前人工状态仍为 `manual_confirmed` 3,895、`manual_provisional` 410；图片库存累计168/765张已复核，195篇文章仍有未复核图片。决定表：[round117-decisions.tsv](round117-decisions.tsv)；图片清单：[round117-image-manifest.csv](round117-image-manifest.csv)；批次：[live-image-review-batch-v2-round117.csv](live-image-review-batch-v2-round117.csv)。

### Round 118 已完成

- 从 provisional 且有未复核图片的队列中选出21篇，46张源图全部下载成功并逐张视觉复核；复核记录：[round118-image-review.tsv](round118-image-review.tsv)。
- 46/46张图片无缺失、无重复、无历史批次重叠，均未改变专题判断；一致性为8张 `consistent`、34张 `limited`、4张 `inconclusive`。长图已分段核查；OCR保持 `not_started`，图片不替代事实核验。
- Round118完成时，21篇暂保持 `manual_provisional`，阻塞原因是正文重读、材料不足或专题边界，而不是图片未复核；其中6篇列入后续文本/来源审计候选，随后经独立正文复读确认正文完整、主副专题边界清楚并提升为 `manual_confirmed`，其余15篇仍保持 `manual_provisional`。旧的“图片待复核”措辞已改为“图片已复核、专题未改变、仍需文本/来源/边界复核”。
- 分类索引、打印索引、人工抽样和实时队列均已重建。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 当前人工状态仍为 `manual_confirmed` 3,895、`manual_provisional` 410；图片库存累计214/765张已复核，174篇文章仍有未复核图片。决定表：[round118-decisions.tsv](round118-decisions.tsv)；图片清单：[round118-image-manifest.csv](round118-image-manifest.csv)；批次：[live-image-review-batch-v2-round118.csv](live-image-review-batch-v2-round118.csv)。

### Round 119 已完成

- 因剩余 provisional 图片均来自历史批次，无法重复入选；本轮从全新、未复核图片组中选出6篇 confirmed 文章，48张源图全部下载成功并逐张视觉复核，长图另行分段检查。
- 48/48张图片无缺失、无重复、无历史批次重叠，均未改变专题判断；一致性为17张 `consistent`、30张 `limited`、1张 `inconclusive`（《日式》中的幸运饼干附图与正文主体对应不清）。
- 6篇原已 `manual_confirmed`，本轮只补齐图片证据链，不改变主码、副码或人工状态。图片库存累计262/765张已复核，168篇文章仍有未复核图片。
- 分类索引、打印索引、人工抽样和实时队列均已重建。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 决定表：[round119-decisions.tsv](round119-decisions.tsv)；图片清单：[round119-image-manifest.csv](round119-image-manifest.csv)；批次：[live-image-review-batch-v2-round119.csv](live-image-review-batch-v2-round119.csv)。

### Round 118 正文复读与 Round 120 已完成

- 对 Round 118 中图片已复核但仍因文本/边界理由保留 provisional 的6篇完成独立正文复读：《陵园》《高尔顿钉板》《侵略者》《濯我衣者》《掐丝镂空》《无威》。六篇正文均完整，现有主码与副码均可保留，均建议并已提升为 `manual_confirmed`；文本复读不等同于相关历史、教育、法律或安全主张已外部核验。
- Round 120 从全新、未出现在历史 manifest 的图片组中选出《军服》《井田》2篇，共44张源图；44/44张图片下载成功并逐张视觉复核，长图分段检查，未改变两篇既有专题判断。复核一致性为23张 `consistent`、19张 `limited`、2张 `inconclusive`；《井田》第1与第14图为同一源图，已在批次记录中注明。
- Round 120完成后人工决定表仍为4,305条且ID唯一：`manual_confirmed` 3,901、`manual_provisional` 404；图片库存累计306/765张已复核，166篇文章仍有未复核图片。人工决定审计 `pass=true`；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失，严格首轮覆盖4,296篇、有效主题覆盖4,305篇。
- 正式记录：[round118-image-review.tsv](round118-image-review.tsv)、[round118-decisions.tsv](round118-decisions.tsv)、[round120-image-review.tsv](round120-image-review.tsv)、[round120-decisions.tsv](round120-decisions.tsv)；图片清单：[round120-image-manifest.csv](round120-image-manifest.csv)；批次：[live-image-review-batch-v2-round120.csv](live-image-review-batch-v2-round120.csv)。正文复读提升脚本：[promote_round118_candidates.py](../scripts/promote_round118_candidates.py)。

### Round 121 正文复读已完成

- 对10篇无图片 provisional 文章完成独立正文复读，正文均完整、主题线索明确，10/10主码与既有决定一致，全部提升为 `manual_confirmed`。其中6篇按正文边界收敛副码：《一意孤行》A06/A03、《反战》A03、《不杀妇孺》A02/A20、《长平》A10/A03、《忒厚呀嘿》A16、《优势在我》A03；其余4篇副码维持。
- 本轮副码修正只反映正文中心与边界，不将政治、历史、军事、心理或其他事实性主张视为外部核验结论。审计表：[round121-text-audit.tsv](round121-text-audit.tsv)；落库脚本：[apply_round121_text_audit.py](../scripts/apply_round121_text_audit.py)。

### Round 121 图片复核已完成

- 从全新、未出现在历史 manifest 的图片组中选出21篇 confirmed 文章，共46张图位；46/46下载成功并逐图视觉复核，历史文章/图片键重叠0，未改变任何专题判断。视觉一致性为25张 `consistent`、17张 `limited`、4张 `inconclusive`；OCR仍为 `not_started`，图片不替代事实核验。
- 图片库存现累计352/765张已复核，145篇文章仍有未复核图片；人工决定表仍为4,305条，`manual_confirmed=3,911`、`manual_provisional=394`。正式记录：[round121-image-review.tsv](round121-image-review.tsv)、[round121-decisions.tsv](round121-decisions.tsv)、[round121-image-manifest.csv](round121-image-manifest.csv)、[live-image-review-batch-v2-round121.csv](live-image-review-batch-v2-round121.csv)；落库脚本：[finalize_round121_image_review.py](../scripts/finalize_round121_image_review.py)。

### Round 122 已完成

- 正文复读批次共10篇、正文约10,001字，15张图片均已在库存中完成视觉复核。9篇正文完整、主题中心与边界清楚，提升为 `manual_confirmed`；《活成这样》只有视频链接和题面，缺少可复核作者论述，保留 `A00/manual_provisional`，没有因篇幅短而强行归类。
- 9篇正文确认中的边界修正包括：《绳降逃生》移除无正文依据的A10、《到底在争夺什么》改为A12/A16、《均值模糊》将A05置于A20之前；其余主码稳定。审计表：[round122-text-audit.tsv](round122-text-audit.tsv)；落库脚本：[apply_round122_text_audit.py](../scripts/apply_round122_text_audit.py)。
- 图片补证批次从全新、未出现在历史 manifest 的组中选出8篇 confirmed 文章，共43张图；43/43下载并视觉复核，27张 `consistent`、16张 `limited`、0张 `inconclusive`，无专题改变。正式记录：[round122-image-review.tsv](round122-image-review.tsv)、[round122-decisions.tsv](round122-decisions.tsv)、[round122-image-manifest.csv](round122-image-manifest.csv)、[live-image-review-batch-v2-round122.csv](live-image-review-batch-v2-round122.csv)；落库脚本：[finalize_round122_image_review.py](../scripts/finalize_round122_image_review.py)。
- Round122完成后人工决定表仍为4,305条且ID唯一：`manual_confirmed=3,920`、`manual_provisional=385`；图片库存累计395/765张已复核，137篇文章仍有未复核图片。另有15篇 provisional 完成理由审计，其中8篇进入下一轮正式正文复读候选、7篇继续暂定，审计表：[round122-reason-audit.tsv](round122-reason-audit.tsv)。

### Round 123 已完成

- 对10篇正文候选完成全文复读，共22,407字。7篇因正文中心与专题边界清楚而确认，3篇因仅有外链、单句或正文截断而保持 `manual_provisional`；其中《没伦理》改列A00，不从题面推断正文主题。
- 对12篇、41张已下载图片完成逐张视觉复核：21张 `consistent`、20张 `limited`、0张 `inconclusive`，没有图片证据足以改变专题判断；OCR仍未开始，作者事实主张仍未外部核验。图片库存同步至436/765张、129篇文章已完成库存内图片复核，125篇仍有未复核图片。
- 正文决定已正式写入人工表；人工分类由 `manual_confirmed=3,920`、`manual_provisional=385` 更新为 `3,927/378`。重建后的候选表、分类索引、打印索引和实时队列均覆盖4,305个唯一ID；实时暂定队列378篇。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；全语料初读验证609/609批通过、4,296篇初读记录。当前原始JSONL SHA-256为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`，与9月22—24日记录一致，未被本轮修改；官方目录快照仍截至2026-09-21。
- 正文记录：[round123-text-audit.tsv](round123-text-audit.tsv)、[round123-text-decisions.tsv](round123-text-decisions.tsv)；图像记录：[round123-image-review.tsv](round123-image-review.tsv)、[round123-image-decisions.tsv](round123-image-decisions.tsv)；落库脚本：[apply_round123_text_audit.py](../scripts/apply_round123_text_audit.py)、[finalize_round123_image_review.py](../scripts/finalize_round123_image_review.py)。

### Round 124 已完成

- 从实时暂定队列中排除所有既有 `round*-decisions.tsv` 文章后，按正文长度选择50篇全新无图文章；正文合计2,929字，长度4–117字，图片0。批次与正文包：[round124-candidate-batch.csv](round124-candidate-batch.csv)、[round124-fulltext.json](round124-fulltext.json)，逐篇风险概览：[round124-candidate-overview.tsv](round124-candidate-overview.tsv)。
- 完成50篇正文细读：43篇 `manual_confirmed`，7篇因只有格言、隐喻、宗教入口或未回答问题而保留 `manual_provisional`。短文按正文证据决定专题，未用标题或机器候选强行定码；事实、法律、宗教、心理和政策主张均单列为未核验风险。
- 当前人工表由 `3,927/378` 更新为 `manual_confirmed=3,970`、`manual_provisional=335`；重建后的候选、分类索引、打印索引和实时队列均覆盖4,305个唯一ID，待审队列335篇。
- 已将批次选择器增加 `--exclude-prior-decisions`，并通过回归检查；Round124落库脚本可幂等复核。验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；全语料初读仍为609/609批通过、4,296篇初读记录。
- 决定与审计：[round124-decisions.tsv](round124-decisions.tsv)、[round124-text-audit.tsv](round124-text-audit.tsv)；脚本：[apply_round124_text_audit.py](../scripts/apply_round124_text_audit.py)、[prepare_round124_candidate_batch.py](../scripts/prepare_round124_candidate_batch.py)；选择器改动：[select_live_manual_batch_v2.py](../scripts/select_live_manual_batch_v2.py)。

### Round 125 已完成

- 按“长文少做、总字数预算”从排除历史决定后的实时队列选出34篇无图文章，正文合计29,979字，长度194–1,427字；未超过单批30,000字预算。批次：[round125-selection.csv](round125-selection.csv)；正文包：[round125-fulltext.json](round125-fulltext.json)。
- 完成34篇正文细读并全部确认主专题；涉及舆论战、环境工程、公共政策、医学/生物、战争战略和亲密关系等边界，均按正文中心确定主码，最多保留3个副码，并在审计表中区分作者推断与未核验事实。
- 当前人工表在本轮正文复读后达到 `4,004/301`；随后Round124盲审边界修正将最终状态校正为 `manual_confirmed=4,003`、`manual_provisional=302`（见下节）。打印索引和实时队列覆盖4,305个唯一ID，暂定队列最终为302篇。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；全语料初读仍为609/609批通过、4,296篇初读记录。原始JSONL SHA-256仍为 `CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`，未被修改。
- 决定与审计：[round125-decisions.tsv](round125-decisions.tsv)、[round125-text-audit.tsv](round125-text-audit.tsv)；落库脚本：[apply_round125_text_audit.py](../scripts/apply_round125_text_audit.py)。

### Round124 盲审修正（最终状态）

- 对Round124的10篇边界样本完成独立盲审对照，发现3项需要落库修正：`《同性恋》`主/副专题由A02/A11改为A11/A02；`《酒神与天神》`副专题由A01改为A03并保持暂定；`《行为艺术》`补列A10副专题并由 `manual_confirmed` 改为 `manual_provisional`。
- 修正已写入人工决定表、Round124决定/审计表，并重建候选、分类索引、打印索引、抽样投影和实时队列；正式统计由 `4,004/301` 校正为 `4,003/302`。
- 修正后的验收：人工决定审计 `pass=true`、错误0；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失；`validate_all.py --quiet` 通过，609/609批通过、4,296篇有首轮记录。
- 记录：[round124-blind-review.tsv](round124-blind-review.tsv)；修正脚本：[correct_round124_blind_review.py](../scripts/correct_round124_blind_review.py)。三篇的专题决定仍仅表示正文中心判断，不等于其宗教、药物、司法、安全或事实性主张已核验。

### Round126 已完成

- 从实时队列排除全部历史决定后，按总字数约30,000字选择12篇无图文章，正文合计29,954字，最长9,097字；批次：[round126-selection.csv](round126-selection.csv)，正文包：[round126-fulltext.json](round126-fulltext.json)。
- 完成12篇正文细读：9篇 `manual_confirmed`、3篇 `manual_provisional`。暂定项为《财富观》（正文明确未完）、《忠与叛》（题干/正文错位及族群本质化风险）、《对待讨厌的人》（仅135字且无具体情境）。
- 复核裁定将《财富观》定为A11/A08;A18;A05，将《忠与叛》定为A17/A20，将《对待讨厌的人》定为A01/A06；《内务班底》经正文回看维持A05/A07。所有作者的宗教、经济、外交、法律、医学、军事和族群事实性主张均保留为未核验风险。
- 已正式写入人工表并重建候选、分类索引、打印索引、抽样投影和实时队列。最终人工状态为 `manual_confirmed=4,012`、`manual_provisional=293`；实时队列293篇，分类和打印索引仍覆盖4,305个唯一ID。
- 验收：人工决定审计 `pass=true`、错误0；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失；`validate_all.py --quiet`通过，609/609批通过、4,296篇有首轮记录。
- 记录：[round126-decisions.tsv](round126-decisions.tsv)、[round126-text-audit.tsv](round126-text-audit.tsv)、[round126-independent-audit.tsv](round126-independent-audit.tsv)；落库脚本：[apply_round126_text_audit.py](../scripts/apply_round126_text_audit.py)。独立复核审阅前看过前半决定表，因此明确标注为独立复核而非严格盲审。

### Round127 已完成

- 从实时队列排除全部历史决定后，按总字数约30,000字选择10篇无图文章，正文合计29,974字，最长6,495字；批次：[round127-selection.csv](round127-selection.csv)，正文包：[round127-fulltext.json](round127-fulltext.json)。
- 完成10篇正文细读，10篇均 `manual_confirmed`。主专题包括全球化A08、反同化A17、民主专制A10、完美传染病A09、资本家A08、幼稚权A10、历史必然A12、芯片前景A13、生吃A20、一万零一全A01。
- 独立复核先读正文和专题注册表、未读前后半决定表，覆盖7篇高风险文章；主码全部一致。复核裁定为《民主专制》补列A11副码、《完美传染病》补列A14副码；其余主副码保持不变。
- 已正式写入人工表并重建候选、分类索引、打印索引、抽样投影和实时队列。最终人工状态为 `manual_confirmed=4,022`、`manual_provisional=283`；实时队列283篇，分类和打印索引仍覆盖4,305个唯一ID。
- 验收：人工决定审计 `pass=true`、错误0；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无结构性缺失；`validate_all.py --quiet`通过，609/609批通过、4,296篇有首轮记录。
- 记录：[round127-decisions.tsv](round127-decisions.tsv)、[round127-text-audit.tsv](round127-text-audit.tsv)、[round127-independent-audit.tsv](round127-independent-audit.tsv)；落库脚本：[apply_round127_text_audit.py](../scripts/apply_round127_text_audit.py)。

### Round128 已完成

- 按总字数预算选择14篇无图文章，正文合计29,992字；前7篇19,390字、后7篇10,602字，未超过本批约30,000字预算。批次：[round128-selection.csv](round128-selection.csv)；正文包：[round128-fulltext.json](round128-fulltext.json)。
- 14篇完成正文细读：13篇 `manual_confirmed`、1篇 `manual_provisional`。《自由意志》明确标注“待续”，保留暂定，不因盲审建议确认而提前提升；其余文章均按正文中心确定主专题，未使用标题或机器候选强行归类。
- 本轮关键边界裁定：`《为中华之崛起而读书》`定A04/A08;A20，未把国家战略背景误归战争外交；`《0-1-2-3》`由A00提升为A03/A13；`《远小人》`定A06/A01，移除A00；`《清静无为》`定A20/A10;A11；`《最强耐力》`定A18，不归体育A21。作者的心理、医学、产业、历史、政治与安全主张仍与专题分类分开，未作事实核验结论。
- 独立盲审覆盖8篇，均记录 `prior_decision=not_consulted`、`blind_status=strict_blind`；盲审意见作为边界证据，不自动覆盖主线程决定。决定表：[round128-decisions.tsv](round128-decisions.tsv)；前半：[round128-firsthalf-decisions.tsv](round128-firsthalf-decisions.tsv)；后半：[round128-secondhalf-decisions.tsv](round128-secondhalf-decisions.tsv)；独立审计：[round128-independent-audit.tsv](round128-independent-audit.tsv)。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,035`、`manual_provisional=270`；分类索引、打印索引、抽样投影和实时队列均重建。当前待审队列270篇，人工确认率93.73%。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；`validate_all.py --quiet`通过。图片库存仍为436/765张已复核，125篇文章仍有未复核图片；原始JSONL哈希未变，官方目录快照仍截至2026-09-21。
- 落库脚本：[apply_round128_text_audit.py](../scripts/apply_round128_text_audit.py)；暂定理由审计：[provisional-reasons-audit-v2.csv](provisional-reasons-audit-v2.csv)。

### Round129 已完成

- 按“长文少选、总字数约30,000”选择20篇无图、正文可读文章，正文合计29,993字；与既有批次和批内均无重复。批次：[round129-selection.csv](round129-selection.csv)；正文包：[round129-fulltext.json](round129-fulltext.json)。
- 完成20篇正文细读：18篇 `manual_confirmed`、2篇 `manual_provisional`。暂定项为《信仰自由》（复杂家庭冲突被高度归结为履约，具体情境不足）和《拼命解决》（正文仅147字，原回答已搬迁，缺少案件与法律事实）。
- 关键边界修正包括：`《烂不透》`定A01/A08;A11，删除正文无依据的A14；`《拼命解决》`定A10/A05，不因联想添加A14；`《铁尺》`定A08/A07；`《反谣言》`定A10/A05;A01；`《保持善良》`定A10/A11;A08；`《翼护》`维持A05并移除无正文中心依据的A10。A00仅保留在确实缺少可拆解正文的既有文章中。
- 独立盲审覆盖8篇，包含《信仰自由》《拼命解决》及6篇跨主题/高风险文章；8篇均记录 `prior_decision=not_consulted`、`blind_status=strict_blind`，盲审意见作为边界证据，不自动替换正文主线程决定。盲审：[round129-independent-audit.tsv](round129-independent-audit.tsv)；风险抽样：[round129-risk-stratified-blind-sample.csv](round129-risk-stratified-blind-sample.csv)。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,053`、`manual_provisional=252`；分类索引、打印索引、抽样投影和实时队列均重建，当前待审队列252篇，人工确认率94.14%。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；`validate_all.py --quiet`通过，609/609首轮批次通过。图片库存仍为436/765张已复核，125篇文章仍有未复核图片；原始JSONL哈希未变，官方目录快照仍截至2026-09-21。
- 落库脚本：[apply_round129_text_audit.py](../scripts/apply_round129_text_audit.py)；决定表：[round129-decisions.tsv](round129-decisions.tsv)；正文审计：[round129-text-audit.tsv](round129-text-audit.tsv)。

### Round130 已完成

- 按正文长度预算选择27篇无图文章，正文合计29,932字；前14篇、后13篇分别完成独立正文细读。批次：[round130-selection.csv](round130-selection.csv)；正文包：[round130-fulltext.json](round130-fulltext.json)。
- 27篇中26篇 `manual_confirmed`、1篇 `manual_provisional`。`《穿越幽谷》`只有基督教经文摘引、没有上下文或作者自有论证，且图片未审，因此保留暂定，不因标题或引文强行确认。
- 关键边界修正包括：`《人所不知者》`定A05/A03（兄弟亲属沟通，不扩为A06）；`《拿刀的规矩》`定A09/A07;A01（医患服务合作，不扩为A06）；`《涉密》`定A10/A07（法律/审批责任为中心）；`《幸福的窗口》`定A06/A05；`《交换比》`定A08/A05；`《晚景凄凉》`定A06/A19;A01。所有事实、医疗、教育、法律和安全主张仍未外部核验。
- 独立盲审覆盖8篇，全部记录 `prior_decision=not_consulted`、`blind_status=strict_blind`，并将《穿越幽谷》列为正文可识别但证据不足的边界项；盲审意见用于校正副码和风险边界，不自动覆盖正文证据门槛。盲审：[round130-independent-audit.tsv](round130-independent-audit.tsv)。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,079`、`manual_provisional=226`；分类索引、打印索引、抽样投影和实时队列均重建，当前待审队列226篇，人工确认率94.75%。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；`validate_all.py --quiet`通过，609/609首轮批次通过。Round130落库时发现并修复脚本漏写CSV表头问题，修复后正式表与索引已重新生成并复验通过。
- 落库脚本：[apply_round130_text_audit.py](../scripts/apply_round130_text_audit.py)；决定表：[round130-decisions.tsv](round130-decisions.tsv)；正文审计：[round130-text-audit.tsv](round130-text-audit.tsv)。

### Round131 已完成

- 按“短文多做、长文控制总字数”的批量规则选择15篇无图、正文可读文章，正文合计29,976字；前8篇19,994字、后7篇9,982字。批次：[round131-selection.csv](round131-selection.csv)；正文包：[round131-fulltext.json](round131-fulltext.json)。
- 15篇完成前后半独立正文细读：13篇 `manual_confirmed`、2篇 `manual_provisional`。暂定项为《胆小鬼大军》（篇幅较短且社会心理推断泛化）和《不吭声》（儿童心理后果推断超出正文证据）；没有用标题或机器候选强行确认。
- 关键边界修正包括：`《怯擦边》`以亲密关系A06为主、性化内容仅A02副码；`《不听老人言》`、`《肉闹钟》`、`《不吭声》`、`《小可靠》`均以亲子教育A05为主；`《不骄的兵》`以概率/论证A03为主；`《新解》`以教育与AI时代适应A04为主；`《爱有所止》`保留自然法A11次码；`《十万八千想》`删除无诊疗依据的A09；潜艇、拳击和游泳等仅作比喻或介入例子，不升为A12/A21。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,092`、`manual_provisional=213`；分类索引、打印索引、抽样投影和实时队列均按依赖顺序重建，当前待审队列213篇，人工确认率95.05%。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；`validate_all.py --quiet`通过。全量首轮证据仍为609/609批、4,296篇；图片库存仍为436/765张已复核，125篇文章仍有未复核图片；原始JSONL与官方目录快照未改动（官方快照截至2026-09-21）。
- 记录与脚本：[round131-decisions.tsv](round131-decisions.tsv)、[round131-firsthalf-decisions.tsv](round131-firsthalf-decisions.tsv)、[round131-secondhalf-decisions.tsv](round131-secondhalf-decisions.tsv)、[round131-text-audit.tsv](round131-text-audit.tsv)、[apply_round131_text_audit.py](../scripts/apply_round131_text_audit.py)。

### Round132 已完成

- 按总字数预算选择19篇无图、正文可读文章，正文合计29,875字；正文包：[round132-fulltext.json](round132-fulltext.json)，批次：[round132-selection.csv](round132-selection.csv)。
- 19篇完成全文细读：18篇 `manual_confirmed`、1篇 `manual_provisional`。`《创新问题》`正文明确“未完，待续”，仅确认当前可见的创新定义/论证中心，保留暂定；其余文章均按正文中心决定，不以标题、官方路径或机器候选替代正文证据。
- 关键边界修正包括：`《孤单的锁》`归A07合作组织而非泛亲密关系；`《好不自在》`以社会协作与秩序成本为A07主轴；`《捉影》`以文学叙事批评A15为主；`《慢反击》`以制度/防卫准备A10为主；`《野人》`以性别身体与同意A02为主、运动仅作手段；`《童言》`以公共传播A16为主；`《拿蛇的人》`以教育学习A04为主。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,110`、`manual_provisional=195`；人工确认率95.47%，实时待审队列195篇。分类索引、打印索引、抽样投影和实时队列均已重建。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；`validate_all.py --quiet`通过。Round132落库脚本已修复为可幂等运行，并显式保留CSV表头；原始JSONL未修改，官方目录快照仍截至2026-09-21。
- 记录与脚本：[round132-decisions.tsv](round132-decisions.tsv)、[round132-text-audit.tsv](round132-text-audit.tsv)、[apply_round132_text_audit.py](../scripts/apply_round132_text_audit.py)。

### Round133 准备中

- 从剩余待审队列按同一正文预算选出19篇，正文合计29,938字；已生成批次、正文包、图片清单及前后半选择表，尚未写入正式分类表。
- 批次：[round133-selection.csv](round133-selection.csv)；正文包：[round133-fulltext.json](round133-fulltext.json)。

### Round133 已完成

- 按总字数预算完成19篇正文细读，共29,938字；18篇 `manual_confirmed`、1篇 `manual_provisional`。`《学生官僚》`仅130字，缺少后续论证，保留暂定。
- 关键边界修正包括：`《语不及私2》`以亲密关系边界为主；`《大补》`以意见处理和论证边界为主；`《敏感问题》`以职场组织反馈为主；`《无受怨》`以家庭亲属关系为主；`《叛军》`、`《坚持的前提》`、`《死之花》`分别按历史政治秩序、工业化历史和文明观念归入A20；`《救道》`以制度/法律责任A10为主。
- 追加后人工决定表4,305条且ID唯一：`manual_confirmed=4,128`、`manual_provisional=177`；人工确认率95.89%，实时待审队列177篇。分类索引、打印索引、抽样投影和实时队列已重建。
- 验收：人工决定审计通过；专题结构审计 `pass=true`、错误0、警告0；主题质量审计无ID缺失和非法概念；`validate_all.py --quiet`通过。原始JSONL未修改，官方目录快照仍截至2026-09-21。
- 记录与脚本：[round133-decisions.tsv](round133-decisions.tsv)、[round133-text-audit.tsv](round133-text-audit.tsv)、[apply_round133_text_audit.py](../scripts/apply_round133_text_audit.py)。
