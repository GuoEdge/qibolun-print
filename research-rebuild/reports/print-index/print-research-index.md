# 岐伯论打印研究索引

本索引是 2026-09-21 v2 语料的导航与打印分组层。原始语料、官方快照、DeepSeek 初读和既有 23 概念映射均保持只读；本文档不把初读标签升级为研究结论。

## 使用方式

- `print-research-index.csv`：每篇文章一行的主索引，可按 `primary_print_topic`、`secondary_print_topics`、`official_root_names`、日期、`classification_status`、`evidence_state` 和 `print_index_status` 筛选。
- `print-research-index.jsonl`：同一主索引的 UTF-8 结构化版本。
- `by-topic/`：按 A01–A21/A00 打印主专题输出；一篇文章只在一个主专题文件出现，也可在最多三个副专题文件出现。
- `by-official-root/`：按素问官方一级对象输出；没有官方节点的文章不强行归类。

## 总体统计

- 语料文章数：4305
- 主专题文章总数（每文恰好一个）：4305
- 专题交叉归属总数（主+副）：12312
- 有官方节点文章数：3689
- 官方未归类文章数：616
- DeepSeek 初读记录数：4296
- 初读缺失数：9
- 独立复核记录数：34

## 按打印主专题

|代码|主专题|主专题文章数|交叉归属数|文件|
|---|---|---:|---:|---|
|A00|跨域行动语法与待审|5|91|[by-topic/01-A00-跨域行动语法与待审.csv](by-topic/01-A00-跨域行动语法与待审.csv)|
|A01|心理主体与情绪劳动|379|1366|[by-topic/02-A01-心理主体与情绪劳动.csv](by-topic/02-A01-心理主体与情绪劳动.csv)|
|A02|性别身体与同意|146|434|[by-topic/03-A02-性别身体与同意.csv](by-topic/03-A02-性别身体与同意.csv)|
|A03|认识论事实与论证|405|1505|[by-topic/04-A03-认识论事实与论证.csv](by-topic/04-A03-认识论事实与论证.csv)|
|A04|教育学习与能力形成|266|735|[by-topic/05-A04-教育学习与能力形成.csv](by-topic/05-A04-教育学习与能力形成.csv)|
|A05|家庭亲属与代际秩序|311|644|[by-topic/06-A05-家庭亲属与代际秩序.csv](by-topic/06-A05-家庭亲属与代际秩序.csv)|
|A06|亲密关系友人与婚恋|552|1038|[by-topic/07-A06-亲密关系友人与婚恋.csv](by-topic/07-A06-亲密关系友人与婚恋.csv)|
|A07|职场组织与合作|362|980|[by-topic/08-A07-职场组织与合作.csv](by-topic/08-A07-职场组织与合作.csv)|
|A08|财富劳动与市场|314|973|[by-topic/09-A08-财富劳动与市场.csv](by-topic/09-A08-财富劳动与市场.csv)|
|A09|医疗疾病与照料|80|257|[by-topic/10-A09-医疗疾病与照料.csv](by-topic/10-A09-医疗疾病与照料.csv)|
|A10|国家法律犯罪与司法|275|899|[by-topic/11-A10-国家法律犯罪与司法.csv](by-topic/11-A10-国家法律犯罪与司法.csv)|
|A11|宗教自然法与世俗论证|169|512|[by-topic/12-A11-宗教自然法与世俗论证.csv](by-topic/12-A11-宗教自然法与世俗论证.csv)|
|A12|战争军事外交与大国秩序|220|480|[by-topic/13-A12-战争军事外交与大国秩序.csv](by-topic/13-A12-战争军事外交与大国秩序.csv)|
|A13|技术工程与产业路径|182|443|[by-topic/14-A13-技术工程与产业路径.csv](by-topic/14-A13-技术工程与产业路径.csv)|
|A14|人工智能机器与未来秩序|43|107|[by-topic/15-A14-人工智能机器与未来秩序.csv](by-topic/15-A14-人工智能机器与未来秩序.csv)|
|A15|艺术审美与文化生产|177|391|[by-topic/16-A15-艺术审美与文化生产.csv](by-topic/16-A15-艺术审美与文化生产.csv)|
|A16|媒体舆论与公共认知|130|397|[by-topic/17-A16-媒体舆论与公共认知.csv](by-topic/17-A16-媒体舆论与公共认知.csv)|
|A17|民族族群与身份秩序|47|197|[by-topic/18-A17-民族族群与身份秩序.csv](by-topic/18-A17-民族族群与身份秩序.csv)|
|A18|生态能源与自然科学|97|248|[by-topic/19-A18-生态能源与自然科学.csv](by-topic/19-A18-生态能源与自然科学.csv)|
|A19|死亡祭祀与纪念|39|67|[by-topic/20-A19-死亡祭祀与纪念.csv](by-topic/20-A19-死亡祭祀与纪念.csv)|
|A20|历史文明与历时演变|101|537|[by-topic/21-A20-历史文明与历时演变.csv](by-topic/21-A20-历史文明与历时演变.csv)|
|A21|体育、运动与竞技伦理|5|11|[by-topic/22-A21-体育、运动与竞技伦理.csv](by-topic/22-A21-体育、运动与竞技伦理.csv)|

## 按官方一级对象

|官方一级对象|文章数|文件|
|---|---:|---|
|与自己|1247|[by-official-root/01-与自己.csv](by-official-root/01-与自己.csv)|
|与其它|204|[by-official-root/02-与其它.csv](by-official-root/02-与其它.csv)|
|与亲族|488|[by-official-root/03-与亲族.csv](by-official-root/03-与亲族.csv)|
|与社会|987|[by-official-root/04-与社会.csv](by-official-root/04-与社会.csv)|
|与合作者|380|[by-official-root/05-与合作者.csv](by-official-root/05-与合作者.csv)|
|与自然|117|[by-official-root/06-与自然.csv](by-official-root/06-与自然.csv)|
|与友人|413|[by-official-root/07-与友人.csv](by-official-root/07-与友人.csv)|

## 证据与打印闸门

`print_index_status` 仅表示打印前需要做什么检查：`hold_theme_review` 表示 A 专题仍待人工复核；`hold_provisional_theme` 表示人工临时判断；`hold_first_pass_missing` 表示缺少初读；`review_before_annotation` 表示初读需重读或含图片；`index_ready_with_source_caveat` 只表示可进入打印批次导航，不代表外部事实已经核验。
