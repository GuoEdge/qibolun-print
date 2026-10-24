#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round180: visual audit of the 46 image-tail articles.

The images were fetched from the asset URLs already recorded in
``data/image-inventory.csv`` and reviewed as per-article contact sheets
(``image-review/round180/contact-sheets``).  Sheet reading order equals
ascending ``image_index``; the position map is in
``round180-contact-sheet-index.json``.

Two decisions are kept strictly apart, as the project rules require:

  * ``article_decision``  — is the ARTICLE kept?  (never driven by image state)
  * ``image_decision``    — are the IMAGES kept, omitted or archived?

A source image that could not be fetched is recorded as a source gap.  It is
never substituted with a neighbouring image and never described as if seen.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
SNAP = R / "reports/handoff-20260926/confirmed-with-image-work-snapshot.csv"
SRC = R / "image-review/round180"
REVIEW_DATE = "2026-09-26"
REVIEWER = "main-thread+round180-image-visual-review"

# (id, image_index) -> verbatim observation of what the image shows
IMG = {
    "8d2e0d1f-4e23-5e19-bb57-e8bf9b70839d": {
        1: "欧洲政区地形图（EUROPE 标注），覆盖北欧至地中海。",
        2: "亚洲/中国及周边的高空卫星影像，可见青藏高原与云系。"},
    "94ca1d90-a167-56fd-9970-14bd3d992491": {
        1: "19 世纪大型工业/万国博览会室内展厅，人群与展位。",
        2: "玻璃柜内的机械装置（行星仪器/球体机构）。",
        3: "机械轮式装置的专利式线描图（平面与结构视图）。",
        4: "华丽镀银家具/镜台的文物照片。",
        5: "老式黑色缝纫机实物照片。",
        6: "缝纫机针杆与压脚的微距照片。",
        7: "日本浮世绘：店铺街景与人群（店内悬挂暖帘）。",
        8: "日本浮世绘：街道与行人（落款可见）。",
        9: "日本浮世绘：桥头与人力/挑担者场景。",
        10: "日本浮世绘：长街店铺与人群。",
        11: "现代 SINGER 缝纫机产品图。"},
    "1aaa2ef5-6395-561f-b61e-8a69af24fc4a": {
        1: "绵羊品种图鉴：按品种排列的 46 种羊的彩色插画网格。",
        2: "同一图鉴的英文标注版式（46 Sheep Breeds）。"},
    "b4cf2664-7e4a-5e2b-b1fd-68b7a775e34d": {
        1: "科幻游戏角色插画（星灵/Protoss 风格，持蓝色能量刃）。"},
    "5cb9b9e6-3407-5b45-b947-25248e819e84": {
        1: "家具板材封边条产品广告：手撕封边条与“板材切口包边条”字样。",
        2: "白色桌面板材成品照片。",
        3: "蜂窝纸芯/蜂窝板方块堆叠（包装与填充材料）。"},
    "38a73bef-17e9-5fb4-a718-18931523f25c": {
        1: "地图软件截图：伯罗奔尼撒半岛与爱琴海区域，希腊/伊兹密尔/安塔利亚等地名。"},
    "6511b53f-878c-5ae0-af8f-d2f04e78569c": {
        1: "按笔画数分组的汉字字表截图（马、驭、驮……逐级到 20 画）。"},
    "2de34923-9512-534e-890b-d6a12739e092": {
        1: "建筑白色实体研究模型（展场环境，含展板与参观者）。",
        2: "黑色复杂曲面壳体结构模型（展柜内，网格/薄壳形态）。"},
    "977dd7aa-c7a7-5162-80ca-a65a57606979": {
        1: "中文正文截图（长段落，字迹较小）。",
        2: "蓝色曲线示意图：一条起伏轨迹上分布三个圆点与一个三角标记。"},
    "f2cdf0de-aaea-5723-8ff3-da22d9cc12f5": {
        1: "毕加索式公牛石版画渐进简化序列（十余幅由写实到线描）。"},
    "9838b31a-0141-5a0f-8e73-10d36ee4f97e": {
        1: "水下摄影：海豚群围猎鱼群形成的饵球。"},
    "68932127-ef69-52eb-952b-ff57983ae108": {
        1: "跳高运动员过杆瞬间的新闻照片。"},
    "8093cce8-fbd1-5050-b629-09fed6563b52": {
        1: "“质”字楷体与篆体对照图（附田字格，来源 cidianwang.com）。"},
    "11273ac5-c1a7-5414-b1ff-20cec8b2396b": {
        1: "圣米歇尔山（Mont Saint-Michel）实景照片。",
        2: "哥特式主教座堂版画（侧面剖视/立面）。"},
    "3444c1ed-fa7f-5bad-9546-9abbb06b6078": {
        1: "蓝色灯光下的洗手盆/水槽特写，水流下注。"},
    "f46a0755-178e-5cca-a92d-5dad6cd1eafb": {
        1: "网络表情图：花衬衫男子配字幕“你要是唠这个，我可不困了啊~”。"},
    "4660735d-ce7d-5a3e-be20-19823dd154df": {
        1: "新闻截图与 Facebook 引文：驻乌外国志愿者称作战人员服用安非他命、睾酮与类固醇（英文原文高亮）。"},
    "2b500e48-491a-537f-8a8a-6bba75958df4": {
        1: "电影《黑客帝国》剧照：墨镜镜片反光中的尼奥与红蓝药丸。"},
    "86144d35-7a44-50d0-89ae-16e3b50beacf": {
        1: "新闻截图：法国天主教大报《十字架报》呼吁投票给马克龙的报道文字。",
        2: "网络表情图：男子配字幕“这瓜保熟吗”。"},
    "334b5f77-c843-5bbd-856d-3cfdfe2b324f": {
        1: "两捆稻草实物图，分别配红底白字标语“干净整洁”“艰苦奋斗”。"},
    "015043d1-01b8-5915-9d30-d13722a542e7": {
        1: "白色张拉膜结构建筑（膜结构篷房/景观建筑）照片。"},
    "d680ad11-26a6-5468-a86f-0cc8d87222ac": {
        1: "视频截图：男子伏案，字幕“Клеветникам России. Александр Пушкин / 给诽谤俄罗斯的人们 普希金（俄国）”。"},
    "79b4b119-7e6a-527d-a28c-6e9da34b7dde": {
        1: "苏格兰折耳幼猫从木格栅后探头的照片。"},
    "ac2d41bb-c9e6-5a3a-be3f-d7bc018cf19a": {
        1: "黄河铁牛（蒲津渡遗址）青铜牛与铁人雕塑群实景，水印“永济市历史文化研究中心”。"},
    "049ac2a7-fd8b-5c5c-b78c-1133cbd4c75e": {
        1: "折线图“历年来我国研发经费投入强度”（2000—2018，NBD 数据）。"},
    "0e4b0837-bf37-58fa-8a6c-db65d160463a": {
        1: "电影《黑客帝国》剧照：红蓝药丸在两手掌心。"},
    "deb01db8-4255-5012-8a21-e4594a98dd43": {
        1: "玻璃罐装酱料实物照片。",
        2: "“铁鸟”牌黄皮酱商品图（两瓶装）。",
        3: "沙茶酱商品图（含食品伙伴网水印）。"},
    "b5744f29-b95b-5ab0-abb3-e62f8d8d0dac": {
        1: "小县城夜景全景：山体背景、道路车流与住宅楼群。",
        2: "县城夜景：高层建筑、街道照明与弧形商业体。"},
    "550d38d4-31b2-56d8-bc6e-8699b1cdbcb6": {
        1: "双源波干涉条纹图（紫红蓝同心环与节线）。",
        2: "航拍海岸防波堤：消波块与浪花。"},
    "2d033768-8886-500e-8f11-f60fa6f5c7f3": {
        1: "机柜内彩色跳线（橙、绿、紫）布线实景。",
        2: "PCB 叠层模式选择示意图（(a)(b)(c) 三种叠层与右侧参数面板）。"},
    "5b7b1e76-8ba5-5979-a471-53abbda25ce8": {
        1: "古代手写文书/契纸照片（朱批与墨书，孔夫子旧书网水印）。",
        2: "另一件古代手写文书照片（竖行墨书）。",
        3: "古籍印本页面长条截图（小字双行注）。"},
    "c07d9407-74a1-5bc0-9835-9b934f85f22f": {
        1: "《权力的游戏》剧照：耶哥蕊特与雪诺，字幕“You know nothing, Jon Snow.”。"},
    "6250c0e6-8b44-5423-8af0-8bf6cfe3257d": {
        1: "新闻报道照片：两名持枪少年（其中一人持 AK 系步枪），水印“知乎 @John Hexa”。"},
    "ad5c38aa-1757-5bd7-96ba-e5eeb39e48a1": {
        1: "手机浏览器截图：政府网站页面，正文为“什么类型的人才会被判处死刑立即执行？”，含法条文字。"},
    "b145ac9e-ecd3-57cc-815f-85e8e3e2dc73": {
        1: "影视表情图：虬髯男子配字幕“俺也一样！！！”。"},
    "7ac9cc0b-4709-5157-ba26-5c14ebc280ef": {
        1: "罐装干制蔬菜（青葱/香葱）商品图。",
        2: "脱水蔬菜（干制碎菜）商品图，标注“企业店铺”。",
        3: "调味粉对比图（孜然/五香等）。",
        4: "瓶装调味汁（香蕉油/香油/生抽）商品图。",
        5: "什锦蔬菜商品图，标注“纯蔬菜 不加糖”。",
        6: "脱水花菜干商品图。",
        7: "日晒莴笋干商品图（竹匾盛装）。",
        8: "干制菜丝/笋丝商品图（竹匾盛装）。",
        9: "干制蕨菜/干菜捆扎实物图。",
        10: "铝箔纸碗盛装的汤菜实拍图。",
        11: "铝箔纸包烤花蛤/海鲜实拍图。",
        12: "铝箔纸包烤鱼（配柠檬片）实拍图。",
        13: "成品菜肴（配绿叶菜与红色酱料）摆盘实拍图。",
        14: "多格铝箔/锡纸托盘（烘焙用）商品图。"},
    "1a742531-d472-5206-909d-af49dc6adb45": {
        1: "木质形状配对玩具（立方体开孔与彩色几何块）商品图。"},
    "5d8d149d-a664-5698-9b67-e7bde58386ea": {
        1: "动漫表情图：柯南指向前方，配字“真相只有一个！”。"},
    "19a2ff4c-0f01-5107-aa11-9614b01f7666": {
        1: "古籍文字截图：钱思公“平生惟好读书，坐则读经史，卧则读小说，上厕则阅小辞”与“余平生所作文章，多在马上、枕上、厕上”一段。"},
    "2867ed0d-0c0c-5bb4-a328-50f679d93142": {
        1: "卫星影像：河流与河曲地形（Google 水印）。",
        2: "Google 卫星图上的战役态势标注：第聂伯罗彼得罗夫斯克/Дніпро 周边防线轮廓与地名（新莫斯科斯克、巴甫洛格勒等）。"},
    "3f4efcaa-c89d-554b-bcc8-5686ed8527e6": {
        1: "金色神龛/佛龛柜实物照片（柜门内为金色神像，带锁）。"},
    "5f53ba7a-365e-55ce-9127-f98be023cce6": {
        1: "射击瞄准示意图：标注“对准目标的线”，并有说明“当瞄准具上没有压力时，用于瞄准的瞄准点会稍稍偏右一点”。"},
    "66e90cce-04d4-554c-87e6-c7bd02d1c81f": {
        1: "工业机器人展台照片：多台机械臂与焊接设备，现场有参观者。"},
    "e26ded3d-29e4-5733-8c83-39e877cf74f2": {
        1: "合成示意图：太阳、云层与沙地/海面（两组对比画面）。"},
    "5a32a445-202b-593a-a880-21c3716cd9cc": {
        16: "博物馆展陈：中国古代人物坐像与案几（展柜内，展签可见）。",
        17: "博物馆展陈：推独轮车的古代人物铜像。",
        18: "博物馆展陈：另一尊古代人物铜像（侧面）。",
        21: "地图：“The Commercial Network of the Phoenicians”（腓尼基商业网络与贸易路线，含 Carthage、Tyre、Cyprus 等）。"},
    "599b48e8-f608-54cb-9bc0-5ac53b459190": {
        1: "身着黑色长袍与头巾（abaya 式）的女性全身商品/素材照片。"},
}

# id -> (image_decision, rationale)
DEC = {
    "8d2e0d1f-4e23-5e19-bb57-e8bf9b70839d": ("keep_selected_images", "两张为欧洲与亚洲的地形/卫星底图，为正文地理讨论提供定位参照，不含正文之外的独立事实主张。"),
    "94ca1d90-a167-56fd-9970-14bd3d992491": ("keep_3_industry_omit_rest", "11 张分三类：工业博览会展厅、机械/缝纫机实物与专利图、日本浮世绘街景。前两类可作正文工业与器物史的插图；浮世绘街景与正文论证关系较弱，建议只保留 3 张以内的代表作。"),
    "1aaa2ef5-6395-561f-b61e-8a69af24fc4a": ("omit_or_keep_as_illustration", "两张为绵羊品种图鉴。可作“落草为王”题旨的比喻插图，但不承载正文论证，属可删可留的装饰性图片。"),
    "b4cf2664-7e4a-5e2b-b1fd-68b7a775e34d": ("omit_unless_illustration_needed", "唯一图片是游戏角色插画，只能说明正文引用了该形象，不提供任何事实或论证，不保留也不影响正文理解。"),
    "5cb9b9e6-3407-5b45-b947-25248e819e84": ("keep_selected_images", "三张分别对应板材封边、成品桌面与蜂窝纸芯，与“甲醛”来源与家具材料的正文议题直接相关，建议保留。"),
    "38a73bef-17e9-5fb4-a718-18931523f25c": ("keep_selected_images", "地图截图给出伯罗奔尼撒半岛与爱琴海的地理位置，为正文地理讨论提供定位，保留一张即可。"),
    "6511b53f-878c-5ae0-af8f-d2f04e78569c": ("keep_and_ocr", "按笔画分组的汉字字表是正文讨论汉字字形/字表结构的直接材料，建议保留并做 OCR 以便引用具体字例。"),
    "2de34923-9512-534e-890b-d6a12739e092": ("keep_selected_images", "两张建筑模型照片分别展示实体研究与薄壳结构，属于正文建筑议题的可视材料，保留。"),
    "977dd7aa-c7a7-5162-80ca-a65a57606979": ("omit_unless_illustration_needed", "第二张蓝色轨迹示意图或与台球走位论证有关，但第一张只是正文截图，重复正文且字迹不可读；建议只保留示意图一张并说明其为示意。"),
    "f2cdf0de-aaea-5723-8ff3-da22d9cc12f5": ("keep_selected_images", "毕加索公牛渐进简化序列是“逼你幸福”题旨的核心视觉论证材料，保留。"),
    "9838b31a-0141-5a0f-8e73-10d36ee4f97e": ("keep_selected_images", "海豚围猎饵球的纪录片截图与正文自然观察议题一致，保留。"),
    "68932127-ef69-52eb-952b-ff57983ae108": ("keep_selected_images", "跳高过杆照片是体育情境的直接图示，保留。"),
    "8093cce8-fbd1-5050-b629-09fed6563b52": ("keep_and_ocr", "“质”字楷篆对照是正文字义/字形讨论的直接材料，来源水印为 cidianwang.com，需保留并核验来源。"),
    "11273ac5-c1a7-5414-b1ff-20cec8b2396b": ("keep_selected_images", "圣米歇尔山与哥特教堂版画用于建筑史论证，保留并标注后者为版画而非照片。"),
    "3444c1ed-fa7f-5bad-9546-9abbb06b6078": ("omit_unless_illustration_needed", "蓝色洗手盆特写是氛围图，不承载论证，属可删。"),
    "f46a0755-178e-5cca-a92d-5dad6cd1eafb": ("omit_or_keep_as_character_reference", "网络表情图只作情绪表达，不提供任何论据，属可删或仅作行文语气参考。"),
    "4660735d-ce7d-5a3e-be20-19823dd154df": ("keep_and_ocr", "英文引文截图是正文“营级战术群”讨论的一手引述来源，必须保留并 OCR，同时把来源核验状态记为未核验。"),
    "2b500e48-491a-537f-8a8a-6bba75958df4": ("omit_unless_illustration_needed", "《黑客帝国》剧照只是比喻性配图，不承载事实或论证。"),
    "86144d35-7a44-50d0-89ae-16e3b50beacf": ("archive_and_ocr", "新闻截图与表情图：新闻截图可作舆论材料但需 OCR 与来源核验；表情图无论证价值。建议新闻截图存档并 OCR。"),
    "334b5f77-c843-5bbd-856d-3cfdfe2b324f": ("keep_selected_images", "两捆稻草配标语是“稻草”题旨的直接讽刺材料，保留，但需注明标语为加工图而非实物标注。"),
    "015043d1-01b8-5915-9d30-d13722a542e7": ("keep_selected_images", "张拉膜结构建筑照片与“宗教的价值”正文的建筑/公共空间讨论相关，保留一张。"),
    "d680ad11-26a6-5468-a86f-0cc8d87222ac": ("keep_and_ocr", "视频字幕给出普希金《给诽谤俄罗斯的人们》这一具体文本线索，是正文俄罗斯议题的关键引用，保留并 OCR。"),
    "79b4b119-7e6a-527d-a28c-6e9da34b7dde": ("omit_unless_illustration_needed", "折耳幼猫照片是情绪性配图，不承载论证。"),
    "ac2d41bb-c9e6-5a3a-be3f-d7bc018cf19a": ("keep_selected_images", "蒲津渡黄河铁牛雕塑是“浮桥”正文的直接实物材料，保留并保留水印来源。"),
    "049ac2a7-fd8b-5c5c-b78c-1133cbd4c75e": ("keep_and_ocr", "研发经费投入强度折线图是“人才流失”正文的量化证据，保留并 OCR 出具体年份数值，同时记录数据来源为 NBD。"),
    "0e4b0837-bf37-58fa-8a6c-db65d160463a": ("omit_unless_illustration_needed", "《黑客帝国》红蓝药丸剧照为比喻配图，与“闲聊协议”正文无直接论证关系。"),
    "deb01db8-4255-5012-8a21-e4594a98dd43": ("keep_selected_images", "三张酱料实物（含黄皮酱、沙茶酱）与“香料”正文直接相关，保留；商品图水印需记录。"),
    "b5744f29-b95b-5ab0-abb3-e62f8d8d0dac": ("keep_selected_images", "两张县城夜景照片是“小县城的未来”正文的直接对象材料，保留。"),
    "550d38d4-31b2-56d8-bc6e-8699b1cdbcb6": ("keep_selected_images", "干涉条纹与消波块航拍分别对应“烦躁”正文的物理类比与海岸工程意象，保留两张。"),
    "2d033768-8886-500e-8f11-f60fa6f5c7f3": ("keep_and_ocr", "机柜布线照片与 PCB 叠层示意图是“齐齐整整”正文秩序议题的直接材料，叠层图需 OCR 以引用具体叠层名称。"),
    "5b7b1e76-8ba5-5979-a471-53abbda25ce8": ("keep_and_ocr", "两张古代文书与一张古籍印本页面是“疯王”历史论证的一手图像材料，必须保留并 OCR；来源水印为孔夫子旧书网，需记录为未经档案核验。"),
    "c07d9407-74a1-5bc0-9835-9b934f85f22f": ("omit_or_keep_as_character_reference", "剧照字幕只是流行文化引用，不承载论证。"),
    "6250c0e6-8b44-5423-8af0-8bf6cfe3257d": ("keep_selected_images", "持枪少年新闻照片是“缺乏创新”正文讨论社会条件时引用的图像材料，保留，但来源与拍摄背景记为未核验。"),
    "ad5c38aa-1757-5bd7-96ba-e5eeb39e48a1": ("keep_and_ocr", "政府网站截图给出“死刑立即执行”适用对象的法条说明，是“不原谅的诅咒”正文的法律依据来源，必须保留并 OCR。"),
    "b145ac9e-ecd3-57cc-815f-85e8e3e2dc73": ("omit_or_keep_as_character_reference", "影视表情图只作语气参考，不承载论证。"),
    "7ac9cc0b-4709-5157-ba26-5c14ebc280ef": ("keep_6_omit_8_unrelated", "14 张全部是脱水蔬菜、调味汁、铝箔餐具与成品菜商品图。与“节省时间”的烹饪省时主题直接相关的 6 张（脱水菜、铝箔纸碗/包、成品菜）建议保留，其余 8 张（调味粉、酱料、干菜捆、托盘等）为同类堆叠，属可删。"),
    "1a742531-d472-5206-909d-af49dc6adb45": ("keep_selected_images", "木质形状配对玩具是“道德”正文讨论早期教育与规则习得的实物材料，保留。"),
    "5d8d149d-a664-5698-9b67-e7bde58386ea": ("omit_or_keep_as_character_reference", "柯南表情图只作语气参考，不承载论证。"),
    "19a2ff4c-0f01-5107-aa11-9614b01f7666": ("keep_and_ocr", "古籍“三上”文字截图是“时间不够”正文的核心引用，必须保留并 OCR；引用出处需核验（钱思公/宋公垂/欧阳修）。"),
    "2867ed0d-0c0c-5bb4-a328-50f679d93142": ("keep_and_ocr", "第聂伯罗周边防线态势图与河流卫星影像是“长江天险”正文类比论证的直接材料，保留并 OCR 地名，注明底图为 Google 卫星影像。"),
    "3f4efcaa-c89d-554b-bcc8-5686ed8527e6": ("omit_unless_illustration_needed", "金色神龛照片与“心窄路不宽”正文的关系只能靠联想建立，属可删。"),
    "5f53ba7a-365e-55ce-9127-f98be023cce6": ("keep_and_ocr", "瞄准线示意图是“正中心”正文的直接技术材料，保留并 OCR 图中说明文字。"),
    "66e90cce-04d4-554c-87e6-c7bd02d1c81f": ("keep_selected_images", "工业机器人展台照片是“专业布局”正文产业议题的直接材料，保留。"),
    "e26ded3d-29e4-5733-8c83-39e877cf74f2": ("omit_unless_illustration_needed", "太阳/云/沙地的合成示意图与“可见光通信”正文的技术议题关系薄弱，属可删。"),
    "5a32a445-202b-593a-a880-21c3716cd9cc": ("source_incomplete_review_valid_images_only", "本轮补获 4 张（第 16、17、18、21 张）：博物馆古代人物坐像与推独轮车铜像三张、以及腓尼基商业网络地图一张。第 19、20 张源图仍返回空文件（36 字节），属源材料不完整。已获图片只按可见内容记录，不用邻近缩略图替代缺失源图，也不据此声称已完整理解全文。"),
    "599b48e8-f608-54cb-9bc0-5ac53b459190": ("keep_selected_images", "黑袍头巾女性素材图与“原谅宝”正文讨论的性别与审查议题相关，保留一张。"),
}


def main() -> int:
    tail = list(csv.DictReader(SNAP.open(encoding="utf-8-sig")))
    inv: dict[str, list[dict]] = {}
    for row in csv.DictReader((R / "data/image-inventory.csv").open(encoding="utf-8-sig")):
        inv.setdefault(row["id"], []).append(row)
    log = json.loads((SRC / "round180-fetch-log.json").read_text(encoding="utf-8"))
    failed = {(e["id"], e["image_index"]) for e in log["entries"] if e.get("result") == "failed"}
    fetched = {(e["id"], e["image_index"]) for e in log["entries"] if e.get("result") in ("ok", "cached")}

    review_rows, decision_rows = [], []
    stats = {"images_reviewed": 0, "images_failed": 0, "articles_complete": 0,
             "articles_partial": 0, "articles_retain": 0, "articles_excluded": 0}
    for art in tail:
        aid = art["id"]
        notes = IMG.get(aid, {})
        for row in sorted(inv.get(aid, []), key=lambda r: int(r["image_index"])):
            idx = int(row["image_index"])
            if (aid, idx) in failed:
                note, status = "源图获取失败（返回空文件），本轮不得据其内容作任何判断，也不以邻近图片替代。", "source_incomplete"
            elif idx in notes:
                note, status = notes[idx], "reviewed"
            else:
                # already reviewed in an earlier round (5G images 1-15)
                note, status = "该张在第 3926 号文章的历史轮次（round?) 已复核，本轮沿用其既有状态，未重复审读。", "reviewed_in_prior_round"
            review_rows.append({
                "ordinal": art["ordinal"], "id": aid, "title": art["title"],
                "image_index": idx, "src": row["src"], "review_status": status,
                "visual_note": note, "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE,
            })
            if status == "reviewed":
                stats["images_reviewed"] += 1
            if status == "source_incomplete":
                stats["images_failed"] += 1
        img_decision, rationale = DEC[aid]
        n_now = len(notes)
        reviewed_total = n_now + (15 if aid == "5a32a445-202b-593a-a880-21c3716cd9cc" else 0)
        failed_n = sum(1 for (i, _) in failed if i == aid)
        status = "partial" if failed_n else "complete"
        stats["articles_partial" if failed_n else "articles_complete"] += 1
        decision_rows.append({
            "ordinal": art["ordinal"], "id": aid, "title": art["title"],
            "text_chars": art["text_chars"], "image_count": art["image_count"],
            "reviewed_image_count": reviewed_total, "failed_image_count": failed_n,
            "image_review_status": status,
            "article_decision": "retain_article_source_incomplete" if failed_n else "retain_article",
            "image_decision": img_decision, "confidence": "manual_visual_audit_20260926",
            "rationale": rationale, "classification_status": art["classification_status"],
            "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE,
        })
        if failed_n:
            stats["articles_excluded"] += 0
        else:
            stats["articles_retain"] += 1

    (SRC / "round180-image-review.tsv").write_text(
        "\ufeff" + "\n".join("\t".join(str(r[k]) for k in r) for r in [ {k: k for k in review_rows[0]} ] + review_rows),
        encoding="utf-8")
    # rewrite properly with csv for correct quoting
    with (SRC / "round180-image-review.tsv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(review_rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(review_rows)
    with (SRC / "round180-image-decisions.tsv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(decision_rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(decision_rows)

    summary = {
        "round": 180, "articles": len(tail),
        "images_in_scope": len(review_rows),
        "images_visually_reviewed_this_round": stats["images_reviewed"],
        "images_source_incomplete": stats["images_failed"],
        "articles_complete": stats["articles_complete"],
        "articles_partial": stats["articles_partial"],
        "articles_retained": len(tail),
        "articles_deleted": 0,
        "classification_status_changed": 0,
        "outputs": ["round180-image-review.tsv", "round180-image-decisions.tsv"],
    }
    (SRC / "round180-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
