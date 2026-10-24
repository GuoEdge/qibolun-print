import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------------------------------------------------------------------------
# 尺寸与出血规划（300 DPI 印刷标准 / 16开大度全展开书衣）
# 总宽: 勒口80mm + 封底170mm + 书脊38mm + 封面170mm + 勒口80mm = 538 mm
# 总高: 240 mm
# 300 DPI:
#   总宽 538 mm ≈ 6355 px
#   总高 240 mm ≈ 2835 px
# ---------------------------------------------------------------------------

DPI = 300
MM_TO_PX = DPI / 25.4

W_FLAP_L = int(80 * MM_TO_PX)     # 左勒口 ~945 px
W_BACK   = int(170 * MM_TO_PX)    # 封底   ~2008 px
W_SPINE  = int(38 * MM_TO_PX)     # 书脊   ~449 px
W_FRONT  = int(170 * MM_TO_PX)    # 封面   ~2008 px
W_FLAP_R = int(80 * MM_TO_PX)     # 右勒口 ~945 px

H_TOTAL  = int(240 * MM_TO_PX)    # 高度   ~2835 px
W_TOTAL  = W_FLAP_L + W_BACK + W_SPINE + W_FRONT + W_FLAP_R # ~6355 px

# 各区域水平切分 X 坐标
X_FLAP_L_START = 0
X_FLAP_L_END   = W_FLAP_L                           # 945
X_BACK_START   = X_FLAP_L_END                       # 945
X_BACK_END     = X_BACK_START + W_BACK              # 2953
X_SPINE_START  = X_BACK_END                         # 2953
X_SPINE_END    = X_SPINE_START + W_SPINE            # 3402
X_FRONT_START  = X_SPINE_END                        # 3402
X_FRONT_END    = X_FRONT_START + W_FRONT            # 5410
X_FLAP_R_START = X_FRONT_END                        # 5410
X_FLAP_R_END   = W_TOTAL                            # 6355

print(f"Canvas size: {W_TOTAL} x {H_TOTAL} px (300 DPI)")

# 字体配置
FONTS = {
    "huidian":  "/storage/Users/currentUser/HO_DATA_EXT_MISC/Download/UURemote/LAPTOP-RG87B9KG/HYZiKuTangHuiDianKaiShuW.ttf",
    "changli":  "/storage/Users/currentUser/Download/HYChangLiSongKeBen(Original)W.ttf",
    "puyancai": "/storage/Users/currentUser/Download/HYHanLinPuYanCaiW.ttf",
    "xiachan":  "/storage/Users/currentUser/Download/HYYongZiXiaChan-95W.ttf",
    "fz_kait":  "/system/fonts/FZKaiT-SC.ttf",
    "fz_lis":   "/system/fonts/FZLiS-SC.ttf"
}

def get_font(key, size):
    path = FONTS.get(key, FONTS["changli"])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.truetype(FONTS["changli"], size)

# 调色盘（素白宣纸·雅致文人调）
COLOR_PAPER_BG      = (248, 245, 239)      # 仿古宣纸本白微温暖
COLOR_PAPER_WHITE   = (255, 253, 250)      # 题签纯宣白
COLOR_INK_MAIN      = (28, 25, 22)         # 极深松烟墨（对比清晰有力）
COLOR_INK_SUB       = (68, 62, 56)         # 宿墨深灰
COLOR_INK_MUTED     = (125, 116, 106)      # 淡墨灰褐
COLOR_CINNABAR      = (176, 44, 34)        # 经典朱砂红
COLOR_CINNABAR_MUTED= (198, 76, 66)        # 柔和朱砂
COLOR_GOLD_LINE     = (188, 158, 112)      # 雅致古金边框线
COLOR_LINE_BORDER   = (215, 208, 196)      # 折线与辅助边框淡色

# 1. 载入原始星图并做宣纸化融合
base_map_path = "/storage/Users/currentUser/Documents/岐伯论/research-rebuild/assets/star_map_base.jpg"
raw_map = Image.open(base_map_path).convert("L")

scaled_map = raw_map.resize((W_TOTAL, H_TOTAL), Image.Resampling.LANCZOS)
scaled_pixels = scaled_map.load()

map_rgb = Image.new("RGB", (W_TOTAL, H_TOTAL))
map_pixels = map_rgb.load()

bg_r, bg_g, bg_b = COLOR_PAPER_BG
ink_r, ink_g, ink_b = (38, 34, 30)

print("Blending star map texture onto rice paper...")
for y in range(H_TOTAL):
    for x in range(W_TOTAL):
        v = scaled_pixels[x, y] / 255.0
        t = math.pow(v, 0.85) 
        r = int(ink_r + (bg_r - ink_r) * t)
        g = int(ink_g + (bg_g - ink_g) * t)
        b = int(ink_b + (bg_b - ink_b) * t)
        map_pixels[x, y] = (r, g, b)

canvas = map_rgb.copy()
draw = ImageDraw.Draw(canvas)

# ---------------------------------------------------------------------------
# 绘制折痕参考线（极细淡墨虚线）
# ---------------------------------------------------------------------------
def draw_dashed_vline(draw_obj, x, y0, y1, color, dash_len=14, space_len=18):
    cur_y = y0
    while cur_y < y1:
        draw_obj.line([(x, cur_y), (x, min(cur_y + dash_len, y1))], fill=color, width=1)
        cur_y += dash_len + space_len

for fold_x in [X_FLAP_L_END, X_SPINE_START, X_SPINE_END, X_FRONT_END]:
    draw_dashed_vline(draw, fold_x, 0, H_TOTAL, (200, 192, 180), dash_len=14, space_len=20)

# ---------------------------------------------------------------------------
# 印章绘制函数
# ---------------------------------------------------------------------------
def draw_seal_yang(canvas_obj, x, y, size, text, font_key="huidian"):
    """阳刻朱文印（白底红字红边）"""
    draw_local = ImageDraw.Draw(canvas_obj)
    border_w = max(2, int(size * 0.055))
    draw_local.rectangle([x, y, x + size, y + size], fill=(255, 253, 250), outline=COLOR_CINNABAR, width=border_w)
    if len(text) == 2:
        f_size = int(size * 0.42)
        font = get_font(font_key, f_size)
        draw_local.text((x + size*0.28, y + size*0.06), text[0], font=font, fill=COLOR_CINNABAR)
        draw_local.text((x + size*0.28, y + size*0.52), text[1], font=font, fill=COLOR_CINNABAR)
    elif len(text) == 4:
        f_size = int(size * 0.40)
        font = get_font(font_key, f_size)
        draw_local.text((x + size*0.52, y + size*0.07), text[0], font=font, fill=COLOR_CINNABAR)
        draw_local.text((x + size*0.52, y + size*0.52), text[1], font=font, fill=COLOR_CINNABAR)
        draw_local.text((x + size*0.08, y + size*0.07), text[2], font=font, fill=COLOR_CINNABAR)
        draw_local.text((x + size*0.08, y + size*0.52), text[3], font=font, fill=COLOR_CINNABAR)

def draw_seal_yin(canvas_obj, x, y, size, text, font_key="huidian"):
    """阴刻白文印（红底白字）"""
    draw_local = ImageDraw.Draw(canvas_obj)
    draw_local.rectangle([x, y, x + size, y + size], fill=COLOR_CINNABAR, outline=COLOR_CINNABAR)
    if len(text) == 2:
        f_size = int(size * 0.40)
        font = get_font(font_key, f_size)
        draw_local.text((x + size*0.28, y + size*0.06), text[0], font=font, fill=(255, 253, 250))
        draw_local.text((x + size*0.28, y + size*0.52), text[1], font=font, fill=(255, 253, 250))
    elif len(text) == 4:
        f_size = int(size * 0.38)
        font = get_font(font_key, f_size)
        draw_local.text((x + size*0.52, y + size*0.07), text[0], font=font, fill=(255, 253, 250))
        draw_local.text((x + size*0.52, y + size*0.52), text[1], font=font, fill=(255, 253, 250))
        draw_local.text((x + size*0.08, y + size*0.07), text[2], font=font, fill=(255, 253, 250))
        draw_local.text((x + size*0.08, y + size*0.52), text[3], font=font, fill=(255, 253, 250))

# ---------------------------------------------------------------------------
# 竖排文字绘制工具
# ---------------------------------------------------------------------------
def draw_vertical_text(draw_obj, text, font, center_x, y_start, fill_color, line_spacing=12):
    cur_y = y_start
    for ch in text:
        bbox = font.getbbox(ch)
        h = (bbox[3] - bbox[1]) if bbox else 30
        w = (bbox[2] - bbox[0]) if bbox else 30
        draw_obj.text((center_x - w / 2, cur_y), ch, font=font, fill=fill_color)
        cur_y += h + line_spacing
    return cur_y

# ===========================================================================
# 一、封面设计 (FRONT COVER: 3402 ~ 5410, 宽度 2008 px)
# ===========================================================================
print("Rendering Front Cover...")

# 1. 古典竖向题签（位于封面右上方，比例严谨）
label_w = 380
label_h = 1520
label_x = X_FRONT_END - 260 - label_w # 4770
label_y = 220

# 题签淡阴影
shadow = Image.new("RGBA", (label_w + 30, label_h + 30), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow)
s_draw.rectangle([6, 6, label_w + 24, label_h + 24], fill=(50, 40, 30, 22))
shadow = shadow.filter(ImageFilter.GaussianBlur(6))
canvas.paste(shadow, (label_x - 3, label_y - 3), shadow)

# 题签纯宣白主体
draw.rectangle([label_x, label_y, label_x + label_w, label_y + label_h], 
               fill=COLOR_PAPER_WHITE, outline=COLOR_CINNABAR, width=3)
# 内衬细金线
draw.rectangle([label_x + 9, label_y + 9, label_x + label_w - 9, label_y + label_h - 9], 
               outline=COLOR_GOLD_LINE, width=1)
# 题签顶部微型装饰签耳
draw.rectangle([label_x + label_w/2 - 20, label_y - 12, label_x + label_w/2 + 20, label_y], 
               fill=COLOR_CINNABAR)

# 题签文字
# 右列：主书名【岐伯論選】
col_title_x = label_x + int(label_w * 0.62)
font_title = get_font("huidian", 112)
draw_vertical_text(draw, "岐伯論選", font_title, col_title_x, label_y + 110, COLOR_INK_MAIN, line_spacing=46)

# 左列：版本属性【一百二十篇典藏本】
col_sub_x = label_x + int(label_w * 0.28)
font_subtitle = get_font("changli", 40)
draw_vertical_text(draw, "一百二十篇典藏本", font_subtitle, col_sub_x, label_y + 260, COLOR_CINNABAR, line_spacing=24)

# 题签左列下端压角印：「成杰之印」
draw_seal_yang(canvas, int(col_sub_x - 40), label_y + label_h - 170, 80, "成杰之印", "huidian")

# 2. 封面左下角：典雅题词（带微透明宣纸底衬，彻底解决星轨穿插导致的看不太清问题）
desc_x = X_FRONT_START + 200
desc_y = H_TOTAL - 390
desc_pad_w = 1150
desc_pad_h = 240

pad_overlay = Image.new("RGBA", (desc_pad_w, desc_pad_h), (255, 253, 249, 215))
pad_draw = ImageDraw.Draw(pad_overlay)
pad_draw.rectangle([0, 0, desc_pad_w - 1, desc_pad_h - 1], outline=(225, 218, 206), width=1)
canvas.paste(pad_overlay, (desc_x - 30, desc_y - 25), pad_overlay)

font_quote = get_font("xiachan", 46)
draw.text((desc_x, desc_y), "立骨於濁世    求道於近思", font=font_quote, fill=COLOR_INK_MAIN)

font_tagline = get_font("changli", 32)
draw.text((desc_x, desc_y + 75), "五十五冊宏帙精裁  ·  現代人的立身與心智哲學", font=font_tagline, fill=COLOR_INK_SUB)

# 封面右上天头引首印：「稽古」
draw_seal_yin(canvas, X_FRONT_START + 120, 180, 68, "稽古", "huidian")


# ===========================================================================
# 二、书脊设计 (SPINE: 2953 ~ 3402, 宽度 449 px)
# ===========================================================================
print("Rendering Spine...")
spine_center_x = int((X_SPINE_START + X_SPINE_END) / 2) # 3177

# 书脊顶端古典朱红装订纹线
draw.line([(X_SPINE_START + 35, 120), (X_SPINE_END - 35, 120)], fill=COLOR_CINNABAR, width=3)
draw.line([(X_SPINE_START + 35, 130), (X_SPINE_END - 35, 130)], fill=COLOR_GOLD_LINE, width=1)

# 书脊主书名 (竖排，大字会典楷书)
font_spine_title = get_font("huidian", 88)
draw_vertical_text(draw, "岐伯論選", font_spine_title, spine_center_x, 240, COLOR_INK_MAIN, line_spacing=46)

# 书脊分类标：“一百二十篇”
font_spine_sub = get_font("xiachan", 36)
draw_vertical_text(draw, "一百二十篇", font_spine_sub, spine_center_x, 960, COLOR_CINNABAR, line_spacing=20)

# 书脊学术定性：“實存哲學”
font_spine_desc = get_font("changli", 30)
draw_vertical_text(draw, "全息實存哲學", font_spine_desc, spine_center_x, 1450, COLOR_INK_SUB, line_spacing=25)

# 书脊底部出版款识与年代
font_spine_foot = get_font("changli", 28)
draw_vertical_text(draw, "深圳謹製", font_spine_foot, spine_center_x, H_TOTAL - 500, COLOR_INK_SUB, line_spacing=18)

# 书脊底端印章：「岐伯」
draw_seal_yin(canvas, int(spine_center_x - 36), H_TOTAL - 290, 72, "岐伯", "huidian")

# 底端双线
draw.line([(X_SPINE_START + 35, H_TOTAL - 130), (X_SPINE_END - 35, H_TOTAL - 130)], fill=COLOR_GOLD_LINE, width=1)
draw.line([(X_SPINE_START + 35, H_TOTAL - 120), (X_SPINE_END - 35, H_TOTAL - 120)], fill=COLOR_CINNABAR, width=3)


# ===========================================================================
# 三、封底设计 (BACK COVER: 945 ~ 2953, 宽度 2008 px)
# ===========================================================================
print("Rendering Back Cover...")
back_center_x = int((X_BACK_START + X_BACK_END) / 2) # 1949

# 封底正中央：八卷全息架构表与核心要旨提要框
back_box_w = 1420
back_box_h = 1860
back_box_x = int(back_center_x - back_box_w / 2) # 1239
back_box_y = 260

# 纯净宣纸底托（微透度由228提升到246，彻底消除背景杂色干扰，文字如刀刻般清朗）
box_overlay = Image.new("RGBA", (back_box_w, back_box_h), (255, 253, 248, 246))
box_draw = ImageDraw.Draw(box_overlay)
box_draw.rectangle([0, 0, back_box_w - 1, back_box_h - 1], outline=COLOR_LINE_BORDER, width=2)
box_draw.rectangle([10, 10, back_box_w - 11, back_box_h - 11], outline=COLOR_GOLD_LINE, width=1)

canvas.paste(box_overlay, (back_box_x, back_box_y), box_overlay)

# 封底框内文字排版
# 1. 顶部小标题：八卷全息架構考
font_back_h = get_font("huidian", 50)
draw.text((back_box_x + 90, back_box_y + 65), "八 卷 全 息 架 構 考", font=font_back_h, fill=COLOR_CINNABAR)

# 装饰红金双线
draw.line([(back_box_x + 90, back_box_y + 135), (back_box_x + back_box_w - 90, back_box_y + 135)], 
          fill=COLOR_CINNABAR, width=2)
draw.line([(back_box_x + 90, back_box_y + 141), (back_box_x + back_box_w - 90, back_box_y + 141)], 
          fill=COLOR_GOLD_LINE, width=1)

# 2. 八卷架构简纲列举（左右双栏）
vol_list_left = [
    ("卷一 · 本根敦倫", "家庭宗族與代際權界 (十八篇)"),
    ("卷二 · 陰陽合離", "兩性本質與婚戀契約 (十篇)"),
    ("卷三 · 酬酢進退", "人我邊界與應世防身 (十五篇)"),
    ("卷四 · 存神調息", "身心容止與生理節律 (十篇)"),
]
vol_list_right = [
    ("卷五 · 度勢居貨", "職場博弈與資財籌謀 (十二篇)"),
    ("卷六 · 觀風察變", "時代思潮與世相反思 (十六篇)"),
    ("卷七 · 滌除玄覽", "本體認知與玄覽極境 (三十四篇)"),
    ("卷八 · 格物鑄器", "百工技藝與造物實相 (五篇)"),
]

font_vol_t = get_font("xiachan", 34)
font_vol_d = get_font("changli", 28)

y_cursor = back_box_y + 175
for title, desc in vol_list_left:
    draw.text((back_box_x + 90, y_cursor), title, font=font_vol_t, fill=COLOR_INK_MAIN)
    draw.text((back_box_x + 90, y_cursor + 50), desc, font=font_vol_d, fill=COLOR_INK_SUB)
    y_cursor += 125

y_cursor_r = back_box_y + 175
col2_x = back_box_x + int(back_box_w / 2) + 20
for title, desc in vol_list_right:
    draw.text((col2_x, y_cursor_r), title, font=font_vol_t, fill=COLOR_INK_MAIN)
    draw.text((col2_x, y_cursor_r + 50), desc, font=font_vol_d, fill=COLOR_INK_SUB)
    y_cursor_r += 125

# 中间分割淡金线
draw.line([(back_box_x + 90, back_box_y + 710), (back_box_x + back_box_w - 90, back_box_y + 710)], 
          fill=COLOR_LINE_BORDER, width=1)

# 3. 核心精要引语
quote_lines = [
    "「世間無抽象孤立之是非，唯有誰在此事中擁有權責邊界之實存。」",
    "「倫理其實是一件武器，為人的行為設立強硬之軌道。」",
    "「收回對自身之評價權，心性如金剛，不毀不損。」",
    "「非特節略字句以省翻檢之勞，蓋在剝落蕪雜、萃取精微，",
    "  欲使後之學者掩卷沉思之際，知其人道物理不可逾越之經緯所在。」"
]
font_b_quote = get_font("puyancai", 34)
y_quote = back_box_y + 760
for ql in quote_lines:
    draw.text((back_box_x + 90, y_quote), ql, font=font_b_quote, fill=COLOR_INK_MAIN)
    y_quote += 70

# 封底下方版本款识与 ISBN 条块
isbn_y = H_TOTAL - 450
font_isbn = get_font("changli", 30)
draw.text((back_box_x + 90, isbn_y), "《岐伯論選》· 一百二十篇典藏精編本", font=font_isbn, fill=COLOR_INK_MAIN)
draw.text((back_box_x + 90, isbn_y + 48), "內部學術典藏 · 非賣品 · 二〇二六年深圳", font=font_isbn, fill=COLOR_INK_SUB)
draw.text((back_box_x + 90, isbn_y + 96), "ISBN 978-7-98026-120-8", font=get_font("xiachan", 32), fill=COLOR_INK_MAIN)

# 右下角压印：「立骨」
draw_seal_yin(canvas, back_box_x + back_box_w - 180, isbn_y + 5, 90, "立骨", "huidian")


# ===========================================================================
# 四、前勒口设计 (FRONT FLAP: 5410 ~ 6355, 宽度 945 px)
# ===========================================================================
print("Rendering Front Flap (Right)...")
font_flap_title = get_font("huidian", 46)
font_flap_body  = get_font("changli", 30)

# 加宣纸衬托块
flap_r_pad_w = 740
flap_r_pad_h = 1600
flap_r_pad_x = X_FLAP_R_START + 100
flap_r_pad_y = 260

pad_r = Image.new("RGBA", (flap_r_pad_w, flap_r_pad_h), (255, 253, 248, 242))
pad_r_draw = ImageDraw.Draw(pad_r)
pad_r_draw.rectangle([0, 0, flap_r_pad_w - 1, flap_r_pad_h - 1], outline=COLOR_LINE_BORDER, width=1)
canvas.paste(pad_r, (flap_r_pad_x, flap_r_pad_y), pad_r)

draw.text((flap_r_pad_x + 60, flap_r_pad_y + 60), "【 岐 伯 其 人 】", font=font_flap_title, fill=COLOR_CINNABAR)
draw.line([(flap_r_pad_x + 60, flap_r_pad_y + 130), (flap_r_pad_x + flap_r_pad_w - 60, flap_r_pad_y + 130)], 
          fill=COLOR_CINNABAR, width=2)

author_intro = [
    "岐伯先生，隱於市井之智者。",
    "其論發端於日常困頓疑難，",
    "因題立骨，借象明理。",
    "",
    "不尚虛言空論，",
    "專研物理、演化、博弈與心法。",
    "其辭凌厲痛快，剖骨露髓，",
    "使人破除虛妄執念，",
    "明辨人己權柄，自建立身之本。",
    "",
    "全帙五十五冊，",
    "本選精輯其核心骨架一百二十篇，",
    "為通達其學之首選定本。"
]
y_f = flap_r_pad_y + 180
for line in author_intro:
    draw.text((flap_r_pad_x + 60, y_f), line, font=font_flap_body, fill=COLOR_INK_MAIN)
    y_f += 62

draw_seal_yang(canvas, int(flap_r_pad_x + flap_r_pad_w/2 - 45), flap_r_pad_y + flap_r_pad_h - 140, 90, "明道", "huidian")


# ===========================================================================
# 五、后勒口设计 (BACK FLAP: 0 ~ 945, 宽度 945 px)
# ===========================================================================
print("Rendering Back Flap (Left)...")
flap_l_pad_x = 105
flap_l_pad_y = 260
flap_l_pad_w = 740
flap_l_pad_h = 1600

pad_l = Image.new("RGBA", (flap_l_pad_w, flap_l_pad_h), (255, 253, 248, 242))
pad_l_draw = ImageDraw.Draw(pad_l)
pad_l_draw.rectangle([0, 0, flap_l_pad_w - 1, flap_l_pad_h - 1], outline=COLOR_LINE_BORDER, width=1)
canvas.paste(pad_l, (flap_l_pad_x, flap_l_pad_y), pad_l)

draw.text((flap_l_pad_x + 60, flap_l_pad_y + 60), "【 編 纂 旨 要 】", font=font_flap_title, fill=COLOR_CINNABAR)
draw.line([(flap_l_pad_x + 60, flap_l_pad_y + 130), (flap_l_pad_x + flap_l_pad_w - 60, flap_l_pad_y + 130)], 
          fill=COLOR_CINNABAR, width=2)

editor_intro = [
    "若夫《岐伯論》如山嶽之渾淪，",
    "則《文選》乃其主脈岩脊。",
    "",
    "丙午秋，成杰囑命梳理，",
    "以第一性原理為綱，",
    "考其概念發軔，",
    "析其論辯自洽，",
    "終成此一百二十篇典藏帙。",
    "",
    "讀者切己體察，",
    "順藤摸瓜，得意忘言，",
    "方不負著述傳世之苦心。"
]
y_fl = flap_l_pad_y + 180
for line in editor_intro:
    draw.text((flap_l_pad_x + 60, y_fl), line, font=font_flap_body, fill=COLOR_INK_MAIN)
    y_fl += 62

draw_seal_yang(canvas, int(flap_l_pad_x + flap_l_pad_w/2 - 45), flap_l_pad_y + flap_l_pad_h - 140, 90, "成杰", "huidian")

# ---------------------------------------------------------------------------
# 保存高分辨率印刷大图与预览图
# ---------------------------------------------------------------------------
out_full_path = "/storage/Users/currentUser/Documents/岐伯论/岐伯论选·典藏书皮展开全图(300DPI).jpg"
out_preview_path = "/storage/Users/currentUser/Documents/岐伯论/岐伯论选·书皮展开效果图.jpg"

print(f"Saving high-res cover jacket to: {out_full_path} ...")
canvas.save(out_full_path, "JPEG", quality=95, dpi=(300, 300))

preview_w = 2400
preview_h = int(H_TOTAL * (preview_w / W_TOTAL))
canvas_preview = canvas.resize((preview_w, preview_h), Image.Resampling.LANCZOS)
canvas_preview.save(out_preview_path, "JPEG", quality=92)

print(f"Saving web preview to: {out_preview_path} ...")
print("All Book Cover Design Tasks Completed Successfully!")
