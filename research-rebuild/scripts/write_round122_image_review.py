#!/usr/bin/env python3
"""Write conservative per-image Round122 visual review and decisions."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]; REPORTS = ROOT / "research-rebuild/reports"
MANIFEST = REPORTS / "round122-image-manifest.csv"; REVIEW = REPORTS / "round122-image-review.tsv"; DECISIONS = REPORTS / "round122-decisions.tsv"
COMMON = "图片来源、时间、人物/地点身份及外部事实未独立核验；图像不能单独证明正文之外的历史、因果、性能或制度结论。"

def read(path: Path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as f: return list(csv.DictReader(f, delimiter=delimiter))
def d(visible, relation, consistency="limited"): return visible, relation, consistency

DATA = {
"2bf92107-11dc-543e-b730-097ed3035394": [
 d("影视/武侠画面中人物持刀或兵器站在昏暗室内，画面有中文字幕。", "对应正文把摧毁首都比作给强敌脸上打一拳的暴力隐喻，但不能证明俄乌军事事实。"),
 d("影视画面中多人围在树木和木架旁，中央人物带伤或被控制，底部有字幕。", "只能作为冲突、围观和受伤的戏剧化视觉材料，支持正文的反围观起哄比喻。"),
 d("同一影视场景的近景截图，多人和中央人物清晰可见，带中文字幕。", "与正文关于旁观者为攻击强敌呐喊助威的比喻相近，不能外推现实政治结论。"),
 d("影视画面中人物被多人围住或推搡，底部有中文字幕。", "表现集体围攻/冲突的象征性场景，可辅助正文关于鼓动冒险与承担后果的论述。"),
 d("持刀人物的近景影视截图，人物表情激烈，底部有中文字幕。", "直接提供‘出拳/攻击’的戏剧化情绪语境，但与正文地缘政治论证仅为类比关系。"),
 d("另一名影视人物的面部近景，画面有中文字幕。", "只能确认影视对话与紧张情绪，不能证明正文涉及的军事能力、责任或生存判断。"),
],
"b3332d8f-753e-517f-a8cf-ddbf5b520b9c": [
 d("工厂车间中安装隔音/框架结构，图片带红色中文广告文字。", "直接对应正文建议用工程化框架搭建家庭隔音舱。", "consistent"),
 d("隔音板产品广告，展示多层板材及隔音、厚度等参数。", "直接对应正文关于隔音板、尺寸和成本的技术方案。", "consistent"),
 d("多块透明或半透明板材叠放的商品图，带价格与电商信息。", "支持正文以标准板材和模块化材料解决邻里噪声问题，但价格和性能未核验。"),
 d("多种隔音/吸音材料和设备的商品拼图，带中文商品说明。", "对应正文罗列技术材料、资源选择和隔音舱配置。", "consistent"),
 d("白色壁挂式新风/通风设备广告，标有进风方向和过滤信息。", "直接对应正文提出隔音舱换气方案；设备性能与宣传文字未核验。", "consistent"),
 d("现代室内的吸顶灯、吊顶和窗帘示例，整体为明亮居住空间。", "对应正文关于隔音舱照明、换气和居住舒适度的配套设计。"),
],
"0c2ac588-068e-5031-9108-d72783cbb739": [
 d("女子综合格斗比赛中两名运动员在擂台上对抗。", "直接对应正文把竞技、劳动和身体投入都视为用身体交换未来的论证。", "consistent"),
 d("女子武术/格斗训练或比赛画面，两名运动员正面对峙。", "支持正文关于女性身体能力并非只能被理解为性交易的反驳。", "consistent"),
 d("女性运动员手持弓箭进行射击训练或比赛。", "对应正文列举身体训练、技能和职业路径等身体劳动。", "consistent"),
 d("黑白历史体育照片，运动员在球场上进行比赛。", "把身体投入与竞技、劳动联系起来，支持正文的身体劳动类比。"),
 d("女性军人持枪训练或执行队列任务的照片。", "直接呼应正文所说身体可以服务于职业、国家与公共目标，而不只指性交易。", "consistent"),
 d("两张一元人民币纸币的图片，突出货币面额与交换意象。", "对应正文标题中的‘交换未来’和身体/劳动换取资源的交换隐喻，但不能证明经济价值。"),
],
"f8287ec8-2410-57d6-a7a1-849ae813da76": [
 d("长篇网页或新闻截图，包含多段中文文字。", "作为正文进行事实核查时引用的报道/材料截图，支持其提出待核实案情；来源与全文未独立核验。", "consistent"),
 d("另一张纵向中文网页截图，显示密集段落和页面内容。", "对应正文对老人死亡事件、社区处置和责任链条的材料核查。", "consistent"),
 d("表格/网页截图，列出药品或配送相关条目并有标记。", "直接对应正文验证封控区买药和医疗救助可行性的证据链。", "consistent"),
 d("地图或配送应用截图，显示路线、地点标记和服务界面。", "直接对应正文下单并验证封控区可以送药的操作性证据。", "consistent"),
 d("手机消息/订单提示截图，显示配送完成或服务反馈文字。", "支持正文关于药品送达及不能仅凭情绪判断案情的说明；消息真实性未核验。", "consistent"),
],
"eb0078aa-8b15-5fce-87e0-19ee9ddc54c4": [
 d("古装影视画面中两名人物端碗进食，带中文字幕。", "以历史影视中的儿童/家庭行为作情绪化旁证，与正文关于‘懂事’和代际秩序的抽象论述对应有限。"),
 d("古装影视画面中儿童与另一名儿童交谈，带中文字幕。", "只能表现影视化的儿童互动，不能证明现实儿童心理或代际规律。"),
 d("古装儿童人物做出防御或武术动作，画面带字幕。", "可作为‘听话/反叛’两种行为张力的戏剧化材料，但与正文心理结论对应有限。"),
 d("同一儿童影视人物的低角度动作镜头，带中文字幕。", "对应正文对儿童服从、成长和反抗的文化叙事，但不是心理学证据。"),
 d("影视画面中儿童人物与成人或环境互动，带平台水印和字幕。", "只能确认影视语境；正文关于现代化、父母认知优势和叛逆风险的判断不能由画面证明。"),
],
"edf11fe5-9c57-5fbc-af6c-6f56b20dd1de": [
 d("世界地图上标注航线、方向箭头和海域范围。", "直接对应正文关于海权、陆权和全球航道空间的地理分析。", "consistent"),
 d("带经纬线和红色航线的地球/亚洲示意图。", "支持正文对大陆地理、海上拒止范围和全球战略空间的讨论。", "consistent"),
 d("港口和航母/大型舰船的卫星图或地图截图。", "直接对应正文对航母停泊、港口和沿岸军事空间的分析，但地点与时间未核验。", "consistent"),
 d("另一处港口及舰船的卫星图，显示岸线、道路和船只。", "支持正文比较海上平台与陆基拒止区域的论证。", "consistent"),
 d("港口或舰船进港过程的影像/地图截图，带中文说明。", "对应正文关于舰队活动、沿岸安全区域与海权局限的讨论。", "consistent"),
],
"0abb35df-d669-5b45-ac03-2fbc11fada80": [
 d("复活节岛石像群及草地景观照片。", "直接对应正文将巨大拟物建筑与宗教造像相比较的建筑审美论证。", "consistent"),
 d("埃及金字塔群照片，前景有沙漠和行人。", "作为大型象征性/纪念性建筑的实例，支持正文对建筑具象化和信仰功能的讨论。", "consistent"),
 d("巨石阵遗址照片，带新闻台标识。", "直接提供宗教、仪式或纪念性巨型建筑的实例，但图片来源未核验。"),
 d("吴哥窟或类似大型宗教建筑的全景照片。", "对应正文把建筑造像、信仰和实用居住功能区分开的论述。", "consistent"),
 d("中美洲阶梯金字塔照片，游客在建筑前活动。", "支持正文关于大型具象/宗教建筑不应简单按普通居住建筑评价的例证。", "consistent"),
],
"95ae40bd-6bce-5354-856f-6dbd939c45a4": [
 d("木柄小型戒刀/僧人用刀的商品图，带绳环。", "直接对应正文解释戒刀是僧人割衣等用途的短刀，而非杀气武器。", "consistent"),
 d("两把带绳环和木柄的短刀商品图。", "直接对应正文对戒刀形制、尺寸和日常工具属性的说明。", "consistent"),
 d("两把红柄厨房刀或餐刀并排放置的照片。", "支持正文把戒刀类比为小型餐刀、强调实用器物属性的论述。", "consistent"),
 d("白色顶骨/骨珠念珠盘绕在深色底座上的商品图。", "直接对应正文澄清人顶骨念珠并非一百零八个骷髅头的说明。", "consistent"),
 d("古代壁画中僧道人物的服饰场景。", "直接对应正文关于直裰、僧人服饰和‘神装/杀气’误读的解释。", "consistent"),
],
}

def main():
    manifest = read(MANIFEST); assert len(manifest) == 43
    expected = {(a, str(i)) for a, vals in DATA.items() for i in range(1, len(vals)+1)}
    actual = {(r["id"], r["image_index"]) for r in manifest}; assert actual == expected
    assert all(r["download_status"] == "success" for r in manifest)
    fields = ["ordinal","id","title","image_index","local_file","download_status","visible_content","relation_to_text","changes_topic_judgment","image_text_consistency","limitations","review_status","review_date"]
    out=[]
    for row in manifest:
        visible, relation, consistency = DATA[row["id"]][int(row["image_index"])-1]
        out.append({**{k: row.get(k, "") for k in fields}, "visible_content": visible, "relation_to_text": relation, "changes_topic_judgment": "no", "image_text_consistency": consistency, "limitations": COMMON, "review_status": "reviewed", "review_date": "2026-09-24"})
    with REVIEW.open("w", encoding="utf-8-sig", newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t"); w.writeheader(); w.writerows(out)
    manual={r["id"]:r for r in read(ROOT/"research-rebuild/data/print-topic-manual-decisions-v2.csv")}; decisions=[]
    for aid in DATA:
        rows=[r for r in out if r["id"]==aid]; m=manual[aid]
        decisions.append({"id":aid,"title":m["title"],"primary":m["primary_print_topic_code"],"secondary":m["secondary_print_topic_codes"],"status":m["classification_status"],"recommendation":"retain_confirmed; image review completed; no topic change","basis":m["decision_basis"],"risk_note":f"Round122 visual review {len(rows)}/{len(rows)}; changes_topic_judgment=no; image_text_consistency={';'.join(r['image_text_consistency'] for r in rows)}; 图片仅记录可见内容，不替代OCR或外部事实核验。"})
    decisions.sort(key=lambda r:r["id"])
    with DECISIONS.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["id","title","primary","secondary","status","recommendation","basis","risk_note"],delimiter="\t"); w.writeheader(); w.writerows(decisions)
    print({"articles":len(DATA),"images":len(out),"consistent":sum(r["image_text_consistency"]=="consistent" for r in out),"limited":sum(r["image_text_consistency"]=="limited" for r in out),"inconclusive":sum(r["image_text_consistency"]=="inconclusive" for r in out)})
if __name__ == "__main__": main()
