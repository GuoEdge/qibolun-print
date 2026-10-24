# 岐伯论分类重建同步报告

生成时间：2026-09-24（Round 100完成、Round 101审读中，Asia/Shanghai）

## 当前基线

- 权威语料：`sooon-q9adg-articles-v2.jsonl`
- 记录数：4,305；唯一 ID：4,305；重复 ID：0
- 最新发布时间：2026-09-21 19:00（北京时间）
- 当前 SHA-256：`CDC9C271309E1D71D9708889A3A31F4777E0C339EA54C3753521894AFDB8357D`
- 原始 JSONL 保持只读

## 分类进度

人工决定表 `data/print-topic-manual-decisions-v2.csv` 当前 3,954 篇：

- `manual_confirmed`：3,653
- `manual_provisional`：301
- 人工决定覆盖率：91.85%
- 正式打印索引：4,305 行，全部有唯一主专题入口
- 实时未人工分类队列：351 篇

正式索引的分类状态：

- `manual_confirmed`：3,653
- `manual_provisional`：301
- `audited`：34
- `review_required`：161
- `needs_human_classification`：156

结构审计结果：`pass=true`，错误 0，警告 0（Round 100追加后重建验证）；人工决定审计同为 `pass=true`、错误 0。抽样审计集1,105篇；结构PASS只证明ID、字段、专题代码、副专题上限和派生一致性，不代表全量语义细读已经完成。

## 批次推进

- Round 92：完成50篇无图全文细读，正文80,458字、最长2,809字；50篇均 `manual_confirmed`。两段独立全文审读后抽读边界项；主题中心确定性与产品隐私、法律、医疗及宏观事实主张的核验风险分开记录。《素问》《包容与纵容》《爱的弱肉强食》虽有事实或规范论证风险，主题中心仍可确定。决定见 `round92-decisions.tsv`，追加脚本为 `append_round92_decisions_v2.py`。
- Round 92：完成50篇无图全文细读，正文80,458字、最长2,809字；50篇均 `manual_confirmed`。两段独立全文审读后抽读边界项；主题中心确定性与产品隐私、法律、医疗及宏观事实主张的核验风险分开记录。《素问》《包容与纵容》《爱的弱肉强食》虽有事实或规范论证风险，主题中心仍可确定。决定见 `round92-decisions.tsv`，追加脚本为 `append_round92_decisions_v2.py`。
- Round 92 同步完成 Round 91 的9项边界修订：《稳定收入》A08/A06、《madness》A07/A21；其余为副专题收敛或补充。独立复核认为《突围》的教育内容只是例证，未加 A04。Round 92完成时人工决定3,562篇（确认3,262、临时300），覆盖82.74%。
- Round 93：完成50篇无图全文细读，正文85,238字、最长3,630字；两段独立复读并抽审12篇边界案例。复核后更新现存50条决定（不重复追加）：《大数定理》A13/A04、《王霸相继》A05/A07;A08、《罡》A11/A01、《好事多磨》A10/A20、《面子》A08/A06；《钢铁是怎样炼成的》由临时改确认为主题明确的A05/A04，儿童安全/法律论证风险另列；《拈花》因日常生活节律缺少准确入口保留A00临时。49篇 `manual_confirmed`、1篇 `manual_provisional`。逐篇依据见 `round93-decisions.tsv`；可复现校验/追加脚本为 `append_round93_decisions_v2.py`。
- Round 93后人工决定3,612篇（确认3,311、临时301），覆盖83.90%，实时未人工分类队列693篇。全库分类/打印索引4,305篇，人工决定ID唯一；结构审计与人工决定审计均 `pass=true`，错误0、警告0。结构PASS仅验证ID、字段、专题代码和派生一致，不代表4,305篇均已全文细读或图片核验。
- Round 94已完成50篇无图文章的全文复核与入表，正文85,464字、最长3,811字；50篇均为 `manual_confirmed`，高风险安全/医疗/法律主张另记风险备注，不把主题确认当作事实核验。批次、全文和权威决定投影分别为 `live-manual-budget-batch-v2-round94-90k.csv`、`round94-fulltext.json`、`round94-decisions.tsv`。
- Round 95已完成47篇无图文章全文细读与交叉复核，正文89,794字、最长4,152字；47篇均为 `manual_confirmed`。对《家传马奇诺》按正文主轴改为A04，重复抽读的《不欣赏权》统一为A06/A02；《保持饥饿》《缪斯性》《欺负》《好生不仁》的医学、词源/神话、受害者归责和古典/演化论断留在风险备注，不因事实待核而降低主题分类状态。批次、全文、合并决定与追加器分别为 `live-manual-budget-batch-v2-round95-90k.csv`、`round95-fulltext.json`、`round95-decisions.tsv`、`append_round95_decisions_v2.py`；后半段独立表 `round95-secondhalf-decisions.tsv`保留作审读依据。
- Round 95 后人工决定3,709篇（确认3,408、临时301），覆盖86.16%；实时队列596篇。人工决定审计与专题结构审计均 `pass=true`，错误0、警告0；候选与打印索引各4,305篇，抽样集1,109篇。结构PASS仅证明字段及派生一致，不代表全库语义细读或图片核验完成。
- Round 96完成50篇无图文章全文细读与两段独立阅读，正文72,300字、最长2,817字；50篇主题均可确定。独立抽核后修订8篇：将《知识的上限》改为A03主码、《迹不代心》改为A20主码；收敛《贫民窟》《密码安全》副码，并补准《肉身菩萨》依据和三篇高风险文章的安全/健康提示。风险判断与主题确定性分开记录。正式追加后人工决定3,759篇（确认3,458、临时301），覆盖87.32%，未分类队列546篇。决定、审读依据及可复现合并/追加/修订脚本见 `round96-decisions.tsv`、`round96-firsthalf-decisions.tsv`、`round96-secondhalf-decisions.tsv`、`merge_round96_decisions_v2.py`、`append_round96_decisions_v2.py`、`correct_round96_reviewed_topics_v2.py` 和 `round96-independent-spotcheck.md`。
- Round 97完成50篇无图文章全文审读，正文78,048字、最长3,030字；两段独立阅读各25篇，主线程另抽读8篇边界/高风险文章，未发现需改变主码的偏差。50篇均 `manual_confirmed`，风险另记；包括AI产业就业预测、星际工程可行性、俄罗斯宗教/民族史、中国军事化治理、网络围攻、艺术教育和家族财务建议等未核验主张。追加后人工决定3,809篇（确认3,508、临时301），覆盖88.48%，队列496篇。批次、全文、决定和抽核依据见 `live-manual-budget-batch-v2-round97-90k.csv`、`round97-fulltext.json`、`round97-decisions.tsv`、`round97-firsthalf-decisions.tsv`、`round97-secondhalf-decisions.tsv`、`round97-independent-spotcheck.md`；可复现器为 `merge_live_manual_decisions_v2.py --round 97`、`append_live_manual_decisions_v2.py --round 97`。
- Round 98完成50篇无图全文细读，正文79,238字、最长3,735字；两段独立审读各25篇，主线程抽读10篇边界/高风险文章，未发现需改变主码的偏差。50篇均 `manual_confirmed`、事实和专业风险另记；抽核涉及残障适应、平民诉讼成本、员工隐私与休假、政府民众秩序、家庭继承观及跨文化风险认知。正式决定、分段审读及抽核依据见 `round98-decisions.tsv`、`round98-firsthalf-decisions.tsv`、`round98-secondhalf-decisions.tsv`、`round98-independent-spotcheck.md`。本批用通用器 `merge_live_manual_decisions_v2.py --round 98` 合并、`append_live_manual_decisions_v2.py --round 98` 追加；追加后人工决定3,859篇（确认3,558、临时301），覆盖89.64%，队列446篇。
- Round 99完成49篇无图中长文全文细读，正文89,077字、最长7,554字；49篇选择是90,000字预算约束下的结果。两段独立审读，主线程抽读13篇跨专题/高风险条目；为《抗骚扰》《应急储备》补强了危险操作不得照做的安全提示。49篇均 `manual_confirmed`。决定与抽核记录见 `round99-decisions.tsv`、`round99-firsthalf-decisions.tsv`、`round99-secondhalf-decisions.tsv`、`round99-independent-spotcheck.md`、`correct_round99_risk_notes_v2.py`。追加后人工决定3,908篇（确认3,607、临时301），覆盖90.77%，队列397篇。
- Round 100完成46篇无图文章全文细读，正文89,798字、最长4,847字；两个独立审读组各23篇。主线程另抽核12篇跨专题/高风险文章及3篇固定种子随机文章，将《探险精神》从A01修订为A03/A01;A04，移除只作示例的A13；并补强《探险精神》《抢孩子》《侠》《女性恐惧》的风险备注。46篇均 `manual_confirmed`；主题可判定不等于相关事实、法律、医学、历史或政策主张已外部核验。追加后人工决定3,954篇（确认3,653、临时301），覆盖91.85%，实时队列351篇。决定、分段表及抽核依据见 `round100-decisions.tsv`、`round100-firsthalf-decisions.tsv`、`round100-secondhalf-decisions.tsv`、`round100-independent-spotcheck.md`；通用器为 `merge_live_manual_decisions_v2.py --round 100`、`append_live_manual_decisions_v2.py --round 100`。
- Round 101从刷新后的实时队列选出50篇无图文章，正文86,182字、最长6,142字，未超90,000字预算；批次与全文50/50对应，ID唯一，与正式人工表零重合。已分成前后各25篇独立审读，尚未追加。批次与全文为 `live-manual-budget-batch-v2-round101-90k.csv`、`round101-fulltext.json`；分段决定表待完成。

- Round 31：25 篇短文，已写入并重建。
- Round 32：50 篇短文，正文总计 27,177 字、无图片依赖；48 篇 `manual_confirmed`，2 篇短文证据不足列 `manual_provisional`。
- Round 33：50 篇短文，正文总计 28,386 字、无图片依赖；已全部写入人工表，846 篇 `manual_confirmed`。
- Round 34：50 篇短文，正文总计 25,101 字、最长 979 字、无图片依赖；已全部逐篇细读并写入人工表，896 篇 `manual_confirmed`。
- Round 35：50 篇短文，正文总计 26,083 字、最长 994 字、无图片依赖；已全部逐篇细读并写入人工表，946 篇 `manual_confirmed`。
- Round 36：从刷新后的实时队列选择45篇短文，正文总计29,574字、最长998字、已完成细读并写入人工表。`剖白` ID 已修正，结构审计恢复通过。
- Round 37：完成50篇短文细读，正文总计33,261字、均≤1000字、无图片依赖；已写入人工表并重建全链路，结构审计通过。另保留长文预算批次单列。
- 选择器：`scripts/select_live_manual_batch_v2.py`。每次先刷新实时队列，再按正文长度、图片依赖和总字数预算选择，避免旧 offset 文件重复取文。

本轮人工修正继续遵循“正文中心优先”：国家或战争背景不自动升级为 A10/A12，技术、家庭、医疗和媒体词面不覆盖文章实际论证中心；副专题最多三个，且不能与主专题重复。

- Round 61：完成50篇短文全文细读，选择器长度合计28,721字（正文+问题），正文合计28,001字，均≤1000字、无图片依赖；48篇 `manual_confirmed`、2篇 `manual_provisional`。决定依据见 `round61-decisions.tsv`，追加脚本为 `append_round61_decisions_v2.py`；人工决定累计2,198篇（覆盖51.06%），待人工分类2,107篇。

- Round 62：完成50篇短文全文细读，选择器长度合计26,050字（正文+问题），正文合计26,050字，均≤1000字、无图片依赖；47篇 `manual_confirmed`、3篇 `manual_provisional`。决定依据见 `round62-decisions.tsv`，追加脚本为 `append_round62_decisions_v2.py`；人工决定累计2,248篇（覆盖52.22%），待人工分类2,057篇。
- Round 63：完成50篇短文全文细读，选择器长度合计26,173字（正文+问题），正文合计26,173字，均≤1000字、无图片依赖；49篇 `manual_confirmed`、1篇 `manual_provisional`。决定依据见 `round63-decisions.tsv`，追加脚本为 `append_round63_decisions_v2.py`；人工决定累计2,298篇（覆盖53.34%），待人工分类2,007篇。
- Round 64：完成50篇短文全文细读，选择器长度合计26,827字（正文+问题），正文合计26,827字，均≤1000字、无图片依赖；49篇 `manual_confirmed`、1篇 `manual_provisional`。决定依据见 `round64-decisions.tsv`，追加脚本为 `append_round64_decisions_v2.py`；人工决定累计2,348篇（覆盖54.49%），待人工分类1,957篇。
- 本轮提速规则：短文批次目标50篇，正文总量预算30,000字；约1,000字以内且无图片依赖的文章优先整批处理，中长文按相同总字数预算缩小批次。每批核验全文ID与人工表零重合。
- Round 65：50篇短文全文细读，正文23,074字，最长942字；47篇 `manual_confirmed`、3篇 `manual_provisional`。复核中将“对不住”归到证据与言论边界、“没关系”归到概念/关系边界，极短的“废话”进A00待审。依据见 `round65-decisions.tsv`，追加脚本 `append_round65_decisions_v2.py`；累计2,398篇（55.70%），待人工分类1,907篇。
- Round 66：50篇短文全文细读，正文24,860字，最长981字；47篇 `manual_confirmed`、3篇 `manual_provisional`。短评、短句和跨域文本使用A00或临时状态，不因标题先行归类。依据见 `round66-decisions.tsv`，追加脚本 `append_round66_decisions_v2.py`；累计2,448篇（56.82%），待人工分类1,857篇。
- Round 67：按短文50篇节奏完成全文细读，正文25,903字，最长979字；48篇 `manual_confirmed`、2篇 `manual_provisional`。修正先前决定表混入其他批次标题的问题，并将“普通不普通”“陨石弹头”暂列A00待复核。依据见 `round67-decisions.tsv`，追加脚本 `append_round67_decisions_v2.py`；累计2,498篇（58.02%），待人工分类1,807篇。
- Round 69：复核2篇高风险含图文章《反犹》《和弓》，根据正文确定临时主副专题；因正文引用的图片尚未视觉核验，均保持 `manual_provisional`。修复风险选择器遇首个超预算条目即停止的问题，保证同一风险层内能继续扫描。
- Round 70：完成50篇无图短文全文细读，正文26,123字、最长989字；47篇 `manual_confirmed`、3篇 `manual_provisional`。逐篇依据见 `round70-decisions.tsv`；批次、全文与决定按ID和顺序匹配，人工ID零重合。累计2,615篇（60.74%），待人工分类1,690篇。
- Round 71：完成50篇无图短文全文细读，正文28,097字、最长1,000字；49篇 `manual_confirmed`、1篇未完稿临时分类。逐篇依据见 `round71-decisions.tsv`；批次、全文和决定ID/标题顺序完全匹配。累计2,665篇（61.90%），待人工分类1,640篇。
- Round 72：完成50篇无图短文全文细读，正文24,582字、最长1,000字；45篇 `manual_confirmed`、5篇 `manual_provisional`（含正文过短或论证材料薄弱项）。逐篇依据见 `round72-decisions.tsv`，追加脚本为 `append_round72_decisions_v2.py`；累计2,715篇（63.06%），待人工分类1,590篇。
- Round 73：完成50篇无图短文全文细读，正文24,811字、最长959字；43篇 `manual_confirmed`、7篇 `manual_provisional`（保留论据过短或推断范围较大的文本待核）。逐篇依据见 `round73-decisions.tsv`，追加脚本为 `append_round73_decisions_v2.py`；累计2,765篇（64.23%），待人工分类1,540篇。
- Round 74：完成50篇无图短文全文细读，正文23,557字、最长978字；41篇 `manual_confirmed`、9篇 `manual_provisional`（短文、假说性材料和截断文本暂留）。逐篇依据见 `round74-decisions.tsv`，追加脚本为 `append_round74_decisions_v2.py`；累计2,815篇（65.39%），待人工分类1,490篇。
- Round 75：完成50篇无图短文全文细读，正文24,975字、最长985字；38篇 `manual_confirmed`、12篇 `manual_provisional`（材料过短、论据不足或待上下文核验项）。抽样复核后修订多个主专题及过宽副专题。逐篇依据见 `round75-decisions.tsv`，追加脚本为 `append_round75_decisions_v2.py`；累计2,865篇（66.55%），待人工分类1,440篇。
- Round 75后候选索引、正式分类索引和打印索引均4,305行；人工ID唯一；结构审计通过，错误0、警告0。PASS只代表结构和派生一致性。
- Round 76：完成48篇无图短文全文细读，正文19,358字、最长988字；36篇 `manual_confirmed`、12篇 `manual_provisional`。该风险层符合条件的仅48篇，未跨层强凑。逐篇依据见 `round76-decisions.tsv`，追加脚本为 `append_round76_decisions_v2.py`；累计2,913篇（67.67%），待人工分类1,392篇。
- Round 76后候选索引、正式分类索引和打印索引均4,305行；人工ID唯一；结构审计通过，错误0、警告0。PASS仅代表结构和派生一致性。
- Round 77：完成14篇中长文全文细读，正文29,150字、最长3,512字；8篇 `manual_confirmed`、6篇 `manual_provisional`（包括宏观推断范围大、论据待核项）。逐篇依据见 `round77-decisions.tsv`，追加脚本为 `append_round77_decisions_v2.py`；累计2,927篇（67.99%），待人工分类1,378篇。
- Round 77后候选索引、正式分类索引和打印索引均4,305行；人工ID唯一；结构审计通过，错误0、警告0。PASS仅代表结构和派生一致性。
- Round 78：完成12篇中长文全文细读，正文29,554字、最长6,495字，无图片依赖；12篇均暂列 `manual_provisional`，因为分类中心虽可判断，但文中关键宏观、历史或医学论断仍需证据核验。逐篇依据见 `round78-decisions.tsv`，追加脚本为 `append_round78_decisions_v2.py`；修订原先已先行写入的12条而未重复追加。累计2,939篇（68.27%），待人工分类1,366篇。
- Round 78 抽样式交叉复读核查：独立复核重点比较《伟大》（A11而非题面民族A17）、《内务班底》（A05而非组织A07），均依正文论证中心采纳；未发现需要改变中心分类的重大分歧。副专题按正文支持收敛，宏观事实判断与专题分类状态分开处理。
- Round 78后按“候选派生→正式分类→打印索引→实时队列→结构审计”重建；人工决定表2,939行且ID唯一，全库候选/分类索引各4,305行；结构审计 `pass=true`，错误0、警告0。该PASS只证明结构/派生一致，不代表语义全量审读完成。
- Round 79：短文层已无合格无图文章，按同一预算规则切换到中长文；完成14篇全文细读，正文29,482字、最长4,780字，均无图片依赖；4篇 `manual_confirmed`、10篇 `manual_provisional`。逐篇依据见 `round79-decisions.tsv`，追加脚本为 `append_round79_decisions_v2.py`；累计2,953篇（68.59%），待人工分类1,352篇。
- Round 79的四篇确认项为《征信体系》《废死》《实际存在》《自信》；其余文章因军事技术、历史/地域因果、政策和宏观预测等证据尚需核验而保留临时状态。Round 79完成后已重建候选、正式分类、打印索引、实时队列并通过结构审计（错误0、警告0）。
- Round 80：完成17篇无图中长文细读，正文29,884字、最长4,866字；9篇 `manual_confirmed`、8篇 `manual_provisional`。累计2,970篇，随后重建队列供Round 81选批。
- Round 81：按灵活批次重新选取50篇无图文章，正文84,156字、最长5,378字；抽样复核后将《室内动物》由制度/法律词面偏置纠正为A03概念论证。最终5篇 `manual_confirmed`、45篇 `manual_provisional`；累计3,020篇（70.15%），待人工分类1,285篇。分类覆盖面仍以逐篇边界和事实可核验性决定确认状态，不因提速强行确认。
- 批量节奏更新：保留风险优先与排除含图文章；以50篇为上限、90,000正文字符为硬预算。当前1,000字以下无图文章池已耗尽，实际按字数预算灵活处理；短文可接近50篇，长文自然缩小篇数，不再机械套用30,000字预算。
- Round 81批次、全文、决定及追加脚本：[live-manual-budget-batch-v2-round81-90k.csv](live-manual-budget-batch-v2-round81-90k.csv)、[round81-fulltext.json](round81-fulltext.json)、[round81-decisions.tsv](round81-decisions.tsv)、[append_round81_decisions_v2.py](../scripts/append_round81_decisions_v2.py)。追加时与已人工表中17条重合记录逐字段核对，另追加33条，没有重复ID。
- Round 81后人工表审计3,020条且ID唯一；候选及正式打印索引各4,305条，实时队列1,285条；结构审计 `pass=true`，错误0、警告0。该PASS只证明结构和派生一致，不代表4,305篇语义细读全部完成。
- Round 82：按50篇上限、90,000字正文预算完成50篇无图全文细读，正文80,189字、最长3,635字；50篇均因心理、教育、历史、法律或技术普遍性判断尚待独立证据而列 `manual_provisional`。逐篇依据见 `round82-decisions.tsv`；抽样复核将《无受怨》主类定为A06家庭亲密关系，避免被作者对酗酒风险的规范性重释带偏。累计3,070篇（71.31%），待人工分类1,235篇。
- Round 82批次、全文与追加脚本：[live-manual-budget-batch-v2-round82-90k.csv](live-manual-budget-batch-v2-round82-90k.csv)、[round82-fulltext.json](round82-fulltext.json)、[round82-decisions.tsv](round82-decisions.tsv)、[append_round82_decisions_v2.py](../scripts/append_round82_decisions_v2.py)。批次、全文、决定均50条且顺序/正文长度一致；与原人工表无重复，追加50条。
- Round 82后人工决定表审计3,070条且ID唯一；候选与正式打印索引各4,305条，实时队列1,235条；结构审计 `pass=true`，错误0、警告0。该PASS只证明结构和派生一致，不代表全量语义细读已完成。

## DeepSeek 初读缺口

初读记录仍为 4,296 篇，缺口为新增尾部 9 篇：

`无赢的宇宙`、`吹倒屋`、`见机行事`、`猫咬人`、`勤行`、`授时郎`、`小骇客`、`无章办事`、`老宋`。

这些文章正文并非空缺；在补导出前，索引继续单独保留 `first_pass_missing` 证据状态，不将其误报为初读完成。

## 本轮可复现审计

- Round 61：批次50篇，决定表对应该批的记录50篇，标题集合完全相同；正文50条唯一ID与批次顺序一致。
- 人工决定表审计：2,198行、唯一ID 2,198、PASS；结构审计：候选和正式索引均4,305行、PASS。
- Round 64：批次50篇，决定表与批次标题完全匹配；全文50条ID与选文顺序一致。
- 人工决定表审计：2,348行、唯一ID 2,348、PASS；结构审计：候选和正式索引均4,305行、PASS。
- Round 65：批次、全文、决定各50条，ID和标题对应；正文23,074字、最长942字。
- Round 66：批次、全文、决定各50条，ID和标题对应；正文24,860字、最长981字，与现有人工ID零重合。
- Round 67：批次、全文、决定各50条，ID和标题对应；正文25,903字、最长979字，与现有人工ID零重合；人工决定审计及全库结构审计均通过。
- Round 69：批次、全文、决定各2条；图片数为1与2，均保持 `manual_provisional`；两条均与旧人工ID零重合。
- Round 70：批次、全文、决定各50条；ID和标题顺序完全匹配；正文26,123字、最长989字，均无图片依赖；47篇确认、3篇临时。
- Round 71：批次、全文、决定各50条；ID和标题顺序完全匹配；正文28,097字、最长1,000字，无图片依赖；49篇确认、1篇临时。
- Round 72：批次、全文、决定各50条；ID和标题顺序完全匹配；正文24,582字、最长1,000字，无图片依赖；45篇确认、5篇临时；与原人工表零重合。
- Round 73：批次、全文、决定各50条；ID和标题顺序完全匹配；正文24,811字、最长959字，无图片依赖；43篇确认、7篇临时；与原人工表零重合。
- Round 74：批次、全文、决定各50条；ID和标题顺序完全匹配；正文23,557字、最长978字，无图片依赖；41篇确认、9篇临时；与原人工表零重合。
- 历史快照（Round 77，已过时）：人工决定2,927行；实时队列1,378篇。当前统计见本文顶部和 Round 92 记录。
- 当前实时人工分类队列：596篇；Round 96已选批，继续按图像/材料风险、长度和专题边界分层处理。
- Round 60 字符口径：选择器的28,752字符是“正文+问题”长度，抽出的完整 `text` 正文合计28,225字符。

## 当前可交付文件

- 人工决定：[data/print-topic-manual-decisions-v2.csv](../data/print-topic-manual-decisions-v2.csv)
- 全量打印索引：[print-index/print-research-index.csv](print-index/print-research-index.csv)
- 全量分类索引：[article-classification-v2.csv](article-classification-v2.csv)
- 实时人工队列：[live-manual-classification-queue-v2.csv](live-manual-classification-queue-v2.csv)
- Round 60 选择文件：[live-manual-short-batch-v2-round60-short50.csv](live-manual-short-batch-v2-round60-short50.csv)
- Round 60 全文：[round60-fulltext.json](round60-fulltext.json)
- Round 61 选择文件：[live-manual-short-batch-v2-round61-short50.csv](live-manual-short-batch-v2-round61-short50.csv)
- Round 61 全文：[round61-fulltext.json](round61-fulltext.json)
- Round 61 分类依据：[round61-decisions.tsv](round61-decisions.tsv)
- Round 62 选择文件：[live-manual-short-batch-v2-round62-short50.csv](live-manual-short-batch-v2-round62-short50.csv)
- Round 62 全文：[round62-fulltext.json](round62-fulltext.json)
- Round 62 分类依据：[round62-decisions.tsv](round62-decisions.tsv)
- Round 63 选择文件：[live-manual-short-batch-v2-round63-short50.csv](live-manual-short-batch-v2-round63-short50.csv)
- Round 63 全文：[round63-fulltext.json](round63-fulltext.json)
- Round 63 分类依据：[round63-decisions.tsv](round63-decisions.tsv)
- Round 64 选择文件：[live-manual-short-batch-v2-round64-short50.csv](live-manual-short-batch-v2-round64-short50.csv)
- Round 64 全文：[round64-fulltext.json](round64-fulltext.json)
- Round 64 分类依据：[round64-decisions.tsv](round64-decisions.tsv)
- Round 65 选择表：[live-manual-short-batch-v2-round65-short50.csv](live-manual-short-batch-v2-round65-short50.csv)
- Round 65 全文：[round65-fulltext.json](round65-fulltext.json)
- Round 65 分类依据：[round65-decisions.tsv](round65-decisions.tsv)
- Round 66 选择表：[live-manual-short-batch-v2-round66-short50.csv](live-manual-short-batch-v2-round66-short50.csv)
- Round 66 全文：[round66-fulltext.json](round66-fulltext.json)
- Round 66 分类依据：[round66-decisions.tsv](round66-decisions.tsv)
- Round 67 选择表：[live-manual-short-batch-v2-round67-short50.csv](live-manual-short-batch-v2-round67-short50.csv)
- Round 67 全文：[round67-fulltext.json](round67-fulltext.json)
- Round 67 分类依据：[round67-decisions.tsv](round67-decisions.tsv)
- Round 65/66 追加脚本：[append_round65_decisions_v2.py](../scripts/append_round65_decisions_v2.py)、[append_round66_decisions_v2.py](../scripts/append_round66_decisions_v2.py)
- Round 67 追加脚本：[append_round67_decisions_v2.py](../scripts/append_round67_decisions_v2.py)
- Round 68 选择表：[live-manual-budget-batch-v2-round68-30k.csv](live-manual-budget-batch-v2-round68-30k.csv)
- Round 68 全文：[round68-fulltext.json](round68-fulltext.json)
- Round 68 分类依据：[round68-decisions.tsv](round68-decisions.tsv)
- Round 68 选择器与追加脚本：[select_round68_budgeted_batch_v2.py](../scripts/select_round68_budgeted_batch_v2.py)、[append_round68_decisions_v2.py](../scripts/append_round68_decisions_v2.py)
- Round 68 图像依赖记录暂缓复核；选择器跳过 `deepseek_image_count > 0` 的文章，图像文章转入独立视觉核验批次。
- Round 69 风险批次：[live-manual-risk-batch-v2-round69-30k.csv](live-manual-risk-batch-v2-round69-30k.csv)、[round69-fulltext.json](round69-fulltext.json)、[round69-decisions.tsv](round69-decisions.tsv)；追加脚本：[append_round69_decisions_v2.py](../scripts/append_round69_decisions_v2.py)
- Round 70 短文批次：[live-manual-short-batch-v2-round70-short50.csv](live-manual-short-batch-v2-round70-short50.csv)、[round70-fulltext.json](round70-fulltext.json)、[round70-decisions.tsv](round70-decisions.tsv)；全文导出与追加脚本：[export_round70_fulltext_v2.py](../scripts/export_round70_fulltext_v2.py)、[append_round70_decisions_v2.py](../scripts/append_round70_decisions_v2.py)
- Round 71 短文批次：[live-manual-short-batch-v2-round71-short50.csv](live-manual-short-batch-v2-round71-short50.csv)、[round71-fulltext.json](round71-fulltext.json)、[round71-decisions.tsv](round71-decisions.tsv)；追加脚本：[append_round71_decisions_v2.py](../scripts/append_round71_decisions_v2.py)
- Round 72 已完成批次：[live-manual-short-batch-v2-round72-short50.csv](live-manual-short-batch-v2-round72-short50.csv)、[round72-fulltext.json](round72-fulltext.json)、[round72-decisions.tsv](round72-decisions.tsv)；追加脚本：[append_round72_decisions_v2.py](../scripts/append_round72_decisions_v2.py)。
- Round 73 已完成批次：[live-manual-short-batch-v2-round73-short50.csv](live-manual-short-batch-v2-round73-short50.csv)、[round73-fulltext.json](round73-fulltext.json)、[round73-decisions.tsv](round73-decisions.tsv)；追加脚本：[append_round73_decisions_v2.py](../scripts/append_round73_decisions_v2.py)。
- Round 74 已完成批次：[live-manual-short-batch-v2-round74-short50.csv](live-manual-short-batch-v2-round74-short50.csv)、[round74-fulltext.json](round74-fulltext.json)、[round74-decisions.tsv](round74-decisions.tsv)；追加脚本：[append_round74_decisions_v2.py](../scripts/append_round74_decisions_v2.py)。
- Round 75 已完成批次：[live-manual-short-batch-v2-round75-short50.csv](live-manual-short-batch-v2-round75-short50.csv)、[round75-fulltext.json](round75-fulltext.json)、[round75-decisions.tsv](round75-decisions.tsv)；追加脚本：[append_round75_decisions_v2.py](../scripts/append_round75_decisions_v2.py)。
- Round 76 已完成批次：[live-manual-short-batch-v2-round76-short50.csv](live-manual-short-batch-v2-round76-short50.csv)、[round76-fulltext.json](round76-fulltext.json)、[round76-decisions.tsv](round76-decisions.tsv)；追加脚本：[append_round76_decisions_v2.py](../scripts/append_round76_decisions_v2.py)。
- Round 77 已完成批次：[live-manual-budget-batch-v2-round77-30k.csv](live-manual-budget-batch-v2-round77-30k.csv)、[round77-fulltext.json](round77-fulltext.json)、[round77-decisions.tsv](round77-decisions.tsv)；追加脚本：[append_round77_decisions_v2.py](../scripts/append_round77_decisions_v2.py)。
- Round 78 完成批次：[live-manual-budget-batch-v2-round78-30k.csv](live-manual-budget-batch-v2-round78-30k.csv)、[round78-fulltext.json](round78-fulltext.json)、[round78-decisions.tsv](round78-decisions.tsv)；追加脚本：[append_round78_decisions_v2.py](../scripts/append_round78_decisions_v2.py)。
- Round 79 完成批次：[live-manual-budget-batch-v2-round79-30k.csv](live-manual-budget-batch-v2-round79-30k.csv)、[round79-fulltext.json](round79-fulltext.json)、[round79-decisions.tsv](round79-decisions.tsv)；追加脚本：[append_round79_decisions_v2.py](../scripts/append_round79_decisions_v2.py)。
- 弹性选择器：[select_live_manual_batch_v2.py](../scripts/select_live_manual_batch_v2.py)现会跳过超出剩余字数预算的文章并继续扫描，输出超额跳过清单；短文批次仍按风险优先级、无图、单篇≤1,000字筛选，不使用批次offset推进。
- Round 60 分类依据：[round60-review-notes.md](round60-review-notes.md)
- Round 33 选择文件：[live-manual-short-batch-v2-round33.csv](live-manual-short-batch-v2-round33.csv)
- Round 34 选择文件：[live-manual-short-batch-v2-round34.csv](live-manual-short-batch-v2-round34.csv)
- Round 35 选择文件：[live-manual-short-batch-v2-round35.csv](live-manual-short-batch-v2-round35.csv)
- Round 36 选择文件：[live-manual-short-batch-v2-round36.csv](live-manual-short-batch-v2-round36.csv)
- 分类框架：[final-classification-framework-v2.md](final-classification-framework-v2.md)
- 结构审计：[print-topic-structure-audit-v2.md](print-topic-structure-audit-v2.md)

## 后续动作

1. Round 96待推进：对当前预算批次全文分段复读、对边界样本独立抽审，再决定和复核入表。
2. 继续抽查 A21 候选的边界召回；候选用于定位，正文中心决定主类。暂以五篇人工确认的 A21 样本作为种子，不能把全部机器候选直接转为专题决定。
3. 每轮完成后重建候选、全量分类索引、打印索引、抽样集、实时队列和结构审计；主题可确认但事实待核的文章照常确认专题并另注风险。
4. 分开补齐 9 篇 DeepSeek 初读缺口，并优先处理图片依赖及 A02/A09/A12/A19/A00 边界样本。

- Round 83 已完成：[live-manual-budget-batch-v2-round83-90k.csv](live-manual-budget-batch-v2-round83-90k.csv)、[round83-fulltext.json](round83-fulltext.json)、[round83-decisions.tsv](round83-decisions.tsv)；49篇、89,635字、最长4,446字、无图，全部写入人工表。追加脚本：[append_round83_decisions_v2.py](../scripts/append_round83_decisions_v2.py)。
- Round 84 已完成：[live-manual-budget-batch-v2-round84-90k.csv](live-manual-budget-batch-v2-round84-90k.csv)、[round84-fulltext.json](round84-fulltext.json)、[round84-decisions.tsv](round84-decisions.tsv)；50篇、73,214字、最长3,016字、无图，均逐篇细读并确认为 `manual_confirmed`。追加脚本：[append_round84_decisions_v2.py](../scripts/append_round84_decisions_v2.py)。完成后累计人工决定3,169篇（确认2,875、临时294），覆盖率73.59%，待人工分类1,136篇。
- Round 85 已完成：[live-manual-budget-batch-v2-round85-90k.csv](live-manual-budget-batch-v2-round85-90k.csv)、[round85-fulltext.json](round85-fulltext.json)、[round85-decisions.tsv](round85-decisions.tsv)；50篇、正文78,367字、最长3,688字、无图；49篇 `manual_confirmed`、1篇 `manual_provisional`。《防人》的一般人际安全主题在现有目录中缺少准确入口，暂列临时待边界复核。逐篇结论分别由两位复读者对第26–50篇独立抽样复核；分类确定性与医疗、法律、历史、政治及宏观主张的事实核验分开。追加脚本：[append_round85_decisions_v2.py](../scripts/append_round85_decisions_v2.py)。
- Round 85 后累计人工决定3,219篇（确认2,924、临时295），覆盖率74.77%，实时待分类1,086篇。候选层与打印索引各4,305行、唯一ID 4,305、重复0；人工决定表唯一ID 3,219；决定表/正式索引一致。决定表审计及专题结构审计均 `pass=true`，错误0、警告0；抽样集刷新为1,107篇（确认838、需图像复核26、uncertain 62、待读181）。结构 PASS 不代表全量语义细读或图片核验已完成。
- Round 86 已完成：[live-manual-budget-batch-v2-round86-90k.csv](live-manual-budget-batch-v2-round86-90k.csv)、[round86-fulltext.json](round86-fulltext.json)、[round86-decisions.tsv](round86-decisions.tsv)；50篇、正文89,501字、最长4,675字、无图，48篇 `manual_confirmed`、2篇 `manual_provisional`。第14、17篇经二次复核后按正文中心确认；事实、法律、医疗及安全主张另记为待核验，不等同于主题确认。追加脚本：[append_round86_decisions_v2.py](../scripts/append_round86_decisions_v2.py)。
- Round 86 后累计人工决定3,269篇（确认2,972、临时297），覆盖率75.94%，实时待人工分类1,036篇。候选层与正式打印索引各4,305行、唯一ID 4,305、重复0；人工决定表唯一ID 3,269，决定表与正式索引一致。决定表审计及专题结构审计均 `pass=true`，错误0、警告0；抽样集1,108篇（确认839、需图像复核26、uncertain 62、待读181）。结构 PASS 不代表全量语义细读或图片核验已完成。
- Round 87 已完成：[live-manual-budget-batch-v2-round87-90k.csv](live-manual-budget-batch-v2-round87-90k.csv)、[round87-fulltext.json](round87-fulltext.json)、[round87-decisions.tsv](round87-decisions.tsv)；50篇、正文89,831字、最长3,506字、无图。首次独立复核为45篇 `manual_confirmed`、5篇 `manual_provisional`；抽样再审发现其中《抱怨游戏》《寒症》《火星劝退者》主题清楚，仅事实/因果待核不应降为临时，故修正为48篇 `manual_confirmed`、2篇 `manual_provisional`。《抱怨游戏》改 A08/A11，《寒症》改 A10/A03，《火星劝退者》改 A08/A04;A20。二次抽样审计建议与复核意见已并入决定依据及风险备注；追加脚本：[append_round87_decisions_v2.py](../scripts/append_round87_decisions_v2.py)。
- Round 87 后累计人工决定3,319篇（确认3,020、临时299），覆盖率77.10%，实时待人工分类986篇。候选层与正式打印索引各4,305行、唯一ID 4,305、重复0；决定表审计及专题结构审计均 `pass=true`，错误0、警告0；抽样集1,109篇（确认840、需图像复核26、uncertain 62、待读181）。结构 PASS 不代表全量语义细读或图片核验已完成。
- Round 88 已完成：[live-manual-budget-batch-v2-round88-90k.csv](live-manual-budget-batch-v2-round88-90k.csv)、[round88-fulltext.json](round88-fulltext.json)、[round88-decisions.tsv](round88-decisions.tsv)；47篇、正文89,727字、最长4,819字、无图，46篇 `manual_confirmed`、1篇 `manual_provisional`。两名复核者分段独立阅读，另抽核6篇高边界/高风险文章；风险注记与主题判断分列，1篇《远小人》因现有目录缺少一般人际威慑入口暂列A00。逐篇依据见决定表，追加脚本：[append_round88_decisions_v2.py](../scripts/append_round88_decisions_v2.py)。
- Round 88 后累计人工决定3,366篇（确认3,066、临时300），覆盖率78.19%，实时待人工分类939篇。候选层与正式打印索引各4,305行、唯一ID 4,305、重复0；人工决定表唯一ID 3,366，决定表审计与专题结构审计均 `pass=true`，错误0、警告0；抽样集1,110篇（确认841、需图像复核26、uncertain 62、待读181）。结构 PASS 不代表全量语义细读或图片核验已完成。
- Round 89 已完成：[live-manual-budget-batch-v2-round89-90k.csv](live-manual-budget-batch-v2-round89-90k.csv)、[round89-fulltext.json](round89-fulltext.json)、[round89-decisions.tsv](round89-decisions.tsv)；48篇、正文89,639字、最长4,432字、无图，双人分段复核均认为主题中心清楚，48篇 `manual_confirmed`。对《我不同意》《维特观鲨》《预期不良》《谢罪》《小儿无礼》等高风险文另行抽读，风险提示与分类依据分列。追加脚本：[append_round89_decisions_v2.py](../scripts/append_round89_decisions_v2.py)。
- Round 89 后累计人工决定3,414篇（确认3,114、临时300），覆盖率79.30%，实时待人工分类891篇。候选与正式打印索引各4,305行，决定表ID唯一；决定表审计和专题结构审计均 `pass=true`，错误0、警告0；抽样集1,112篇（确认843、需图像复核26、uncertain 62、待读181）。结构 PASS 不代表全库语义细读或图片核验已完成。
- Round 90 已完成：[live-manual-budget-batch-v2-round90-90k.csv](live-manual-budget-batch-v2-round90-90k.csv)、[round90-fulltext.json](round90-fulltext.json)、[round90-decisions.tsv](round90-decisions.tsv)；50篇、正文86,354字、最长6,343字、无图，49篇 `manual_confirmed`、1篇 `manual_provisional`。前后半批分别独立阅读，另作整批专题边界审计。《体育问题》中心为群众体育生态，现有目录缺少体育入口，按规则列A00临时待审；《政策观察》经抽审由A10/A08调整为A08/A10；《所谓国富民穷》删去缺少独立论证支撑的A13副专题。主题决定和事实、伦理风险分别记录。写入与边界修订脚本：[append_round90_decisions_v2.py](../scripts/append_round90_decisions_v2.py)、[correct_round90_policy_observation.py](../scripts/correct_round90_policy_observation.py)。
- Round 90 后累计人工决定3,464篇（确认3,163、临时301），覆盖率80.46%，实时待人工分类841篇。候选与正式打印索引各4,305行、决定表唯一ID 3,464；决定表审计和专题结构审计均 `pass=true`，错误0、警告0；抽样集刷新为1,111篇。结构 PASS 不代表全库语义细读或图片核验已完成。
- Round 91 已完成：[live-manual-budget-batch-v2-round91-90k.csv](live-manual-budget-batch-v2-round91-90k.csv)、[round91-fulltext.json](round91-fulltext.json)、[round91-decisions.tsv](round91-decisions.tsv)；48篇、正文89,775字、最长4,949字、无图；两位复核者分段阅读全文并对边界/风险样本另作抽审。47篇 `manual_confirmed`，1篇《0-1-2-3》因私人数字资料管理缺少准确入口列 `manual_provisional`。
- Round 91 完成时（历史快照，Round 92 复核前）：人工决定 3,512 篇（确认 3,212、临时 300），实时队列 793 篇。A21 候选与强体育线索用于检索，不是最终分类。Round 91/92 复核后 A21 人工主类4篇：《体育问题》《体育大国》《罗马彩票》《MMA》；《madness》调整为 A07 主、A21 副；《清白体育》为 A17 主、A21 副，《奥运会的非体育意义》留 A15。
- Round 92 决定：[live-manual-budget-batch-v2-round92-90k.csv](live-manual-budget-batch-v2-round92-90k.csv)、[round92-fulltext.json](round92-fulltext.json)、[round92-decisions.tsv](round92-decisions.tsv)、[append_round92_decisions_v2.py](../scripts/append_round92_decisions_v2.py)。人工决定 ID 与选中文章零重合；正式分类逐行继承50条决定。




- Round 38：完成50篇短文细读，正文总计31,380字，均≤1000字，无图片依赖；结构审计通过。

- Round 39：完成50篇短文细读，正文总计29,445字，最长994字，无图片依赖；结构审计通过。

- Round 40：完成50篇短文细读，正文总计30,567字，最长1000字，无图片依赖；结构审计通过。

- Round 41：完成50篇短文细读，正文总计31,949字，最长999字，无图片依赖；修正一条批次ID后结构审计通过。
- Round 42：完成50篇短文细读，正文总计31,972字，最长981字，无图片依赖；按正文中心完成主专题与副专题裁决，修复正式索引人工决定继承问题，结构审计通过。
- Round 43：完成17篇长文/中长文细读，正文总计29,341字；按总字数预算控制批量，覆盖心理韧性、技术安全、亲密关系、货币制度、政治秩序与市场治理等主题，结构审计通过。
- Round 44：完成19篇中长文细读，正文总计29,733字；覆盖伦理边界、亲密关系、家庭治理、政治秩序、战争谈判与技术文化等主题，结构审计通过。
- Round 45：完成17篇中长文细读，正文总计29,586字；覆盖家庭继承、情绪沟通、反腐治理、国际政治、市场风险与文明制度等主题，结构审计通过。

- Round 53：完成50篇短文全文细读，正文总计30,770字，最长990字；采用弹性批量规则，主副专题按lexical正文中心裁决；结构审计通过。人工决定累计1,798篇（覆盖41.77%），待人工分类2,507篇。

- Round 54：完成50篇短文全文细读，正文合计30,302字，最长983字；按正文中心裁决主专题与副专题，结构审计通过。人工决定累计1,848篇（覆盖42.93%），待人工分类2,457篇。

- Round 55：完成50篇短文全文细读，正文合计30,598字，最长983字；按正文中心裁决主专题与副专题，结构审计通过。人工决定累计1,898篇（覆盖44.08%），待人工分类2,407篇。

- Round 56：全文复核并完成50篇短文分类，正文合计29,673字；按现行专题注册表逐项确定主副专题，结构审计通过。人工决定累计1,948篇（覆盖45.25%），待人工分类2,357篇。

- Round 57：细读并分类50篇短文，正文合计26,731字；按正文中心裁决主副专题，结构审计通过。人工决定累计1,998篇（覆盖46.36%），待人工分类2,307篇。

- Round 58：全文细读并分类50篇短文，正文合计31,568字；按正文中心裁决主副专题，结构审计通过。复核并更正 Round 57 两篇专题边界（汽车产业中心归财富/市场；暗算预防中心归主体安全）；人工决定累计2,048篇（覆盖47.57%），待人工分类2,257篇。

- Round 59：按原文全文完成50篇短文分类，正文合计28,462字；逐篇判定依据见 round59-review-notes.md；结构审计通过。人工决定累计2,098篇（覆盖48.72%），待人工分类2,207篇。

- Round 60：完成50篇短文全文细读，选择器批次长度合计28,752字（含问题），正文字段合计28,225字；按正文中心确认主副专题，抽查后将副专题收紧为有明确论证支撑者。判定表与逐篇依据见 `round60-decisions.tsv`、`round60-review-notes.md`；结构审计通过。累计人工决定2,148篇（覆盖49.90%），其中 `manual_confirmed` 2,057篇、`manual_provisional` 91篇，待人工分类2,157篇。

- Round 61：完成50篇短文全文细读，正文合计28,001字，均≤1000字；48篇 `manual_confirmed`、2篇 `manual_provisional`。决定依据见 `round61-decisions.tsv`；结构审计通过。累计人工决定2,198篇（覆盖51.06%），其中 `manual_confirmed` 2,105篇、`manual_provisional` 93篇，待人工分类2,107篇。

- Round 62：完成50篇短文全文细读，正文合计26,050字，均≤1000字；47篇 `manual_confirmed`、3篇 `manual_provisional`。决定依据见 `round62-decisions.tsv`；结构审计通过。累计人工决定2,248篇（覆盖52.22%），其中 `manual_confirmed` 2,152篇、`manual_provisional` 96篇，待人工分类2,057篇。
- Round 63：完成50篇短文全文细读，正文合计26,173字，均≤1000字；49篇 `manual_confirmed`、1篇 `manual_provisional`。决定依据见 `round63-decisions.tsv`；结构审计通过。累计人工决定2,298篇（覆盖53.34%），其中 `manual_confirmed` 2,201篇、`manual_provisional` 97篇，待人工分类2,007篇。
- Round 64：完成50篇短文全文细读，正文合计26,827字，均≤1000字；49篇 `manual_confirmed`、1篇 `manual_provisional`。决定依据见 `round64-decisions.tsv`；结构审计通过。累计人工决定2,348篇（覆盖54.49%），其中 `manual_confirmed` 2,250篇、`manual_provisional` 98篇，待人工分类1,957篇。
- Round 65：完成50篇短文全文细读，正文23,074字，最长942字；47篇确认、3篇临时确认。决定见 `round65-decisions.tsv`；人工决定累计2,398篇（55.70%），待人工分类1,907篇。
- Round 66：完成50篇短文全文细读，正文24,860字，最长981字；47篇确认、3篇临时确认。决定见 `round66-decisions.tsv`；人工决定累计2,448篇（56.82%），待人工分类1,857篇。
- Round 67：50篇短文全文细读，正文25,903字、最长979字；48篇确认、2篇临时确认。人工决定累计2,498篇（58.02%），待人工分类1,807篇；审计通过。
- Round 68：完成20篇中长文/短答细读，正文29,987字、最长4,932字；18篇确认、2篇临时确认。累计2,563篇（59.54%），待人工分类1,742篇；审计通过。
