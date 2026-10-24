import os
from PIL import Image, ImageDraw, ImageFont

ROOT = "/storage/Users/currentUser/Documents/岐伯论"
ASSET = ROOT + "/research-rebuild/assets"
OUT = ROOT + "/岐伯论选·完整书封展开预览.jpg"
SPINE_MM = 42.3
WIDTH_MM = 80 + 170 + SPINE_MM + 170 + 80
W, H = 3200, round(3200 * 240 / WIDTH_MM)
MM = W / WIDTH_MM

bg = Image.open(ASSET + "/qibo_jacket_background.png").convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
d = ImageDraw.Draw(bg)

FONT_H = "/storage/Users/currentUser/HO_DATA_EXT_MISC/Download/UURemote/LAPTOP-RG87B9KG/HYZiKuTangHuiDianKaiShuW.ttf"
FONT_C = "/storage/Users/currentUser/Download/HYChangLiSongKeBen(Original)W.ttf"
FONT_X = "/storage/Users/currentUser/Download/HYYongZiXiaChan-95W.ttf"

def f(path, mm):
    return ImageFont.truetype(path, round(mm * MM))

def txt_center(text, center, y, font, fill):
    box = d.textbbox((0, 0), text, font=font)
    d.text((center - (box[2]-box[0])/2, y), text, font=font, fill=fill)

def wrap_chars(text, font, max_width):
    lines=[]; current=""
    for ch in text:
        candidate=current+ch
        if d.textbbox((0,0), candidate, font=font)[2] <= max_width:
            current=candidate
        else:
            if current: lines.append(current)
            current=ch
    if current: lines.append(current)
    return lines

# Fold marks, deliberately subtle and only for proofing.
for x_mm in (80,250,250+SPINE_MM,250+SPINE_MM+170):
    x=round(x_mm*MM)
    for y in range(0,H,round(2.8*MM)):
        d.line((x,y,x,min(H,y+round(1.2*MM))), fill=(118,113,106), width=max(1,round(.12*MM)))

ink=(32,29,26); red=(145,47,39); muted=(82,77,70)

# Back cover copy: compact, aligned to page grid.
back_left=round((80+16)*MM); back_top=round(18*MM); back_width=round(138*MM)
d.text((back_left,back_top),"岐 伯 論 選  /  全 書 綱 領",font=f(FONT_X,2.8),fill=muted)
d.text((back_left,back_top+round(8*MM)),"八卷通覽",font=f(FONT_H,7),fill=red)
d.line((back_left,back_top+round(18*MM),back_left+back_width,back_top+round(18*MM)),fill=red,width=max(1,round(.2*MM)))
intro="由近及遠，由下學而至上達。八卷相貫，自家庭倫常、人我進退、身心安頓與世事觀察，推至本體之思與格物之用。"
intro_font=f(FONT_C,3.1)
for i,line in enumerate(wrap_chars(intro,intro_font,back_width)):
    d.text((back_left,back_top+round((23+i*5.8)*MM)),line,font=intro_font,fill=ink)
vols=[
("卷一　本根敦倫","家庭、宗族與代際契約"),("卷五　度勢居貨","職場博弈與資財籌謀"),
("卷二　陰陽合離","兩性名理與婚戀契約"),("卷六　觀風察變","時代思潮與世相反思"),
("卷三　酬酢進退","人我邊界與應世防身"),("卷七　滌除玄覽","本體哲學與心智模型"),
("卷四　存神調息","身心安頓與生命節律"),("卷八　格物鑄器","百工技藝與造物實相")]
col_gap=round(5*MM); colw=(back_width-col_gap)//2; start_y=back_top+round(48*MM); rowh=round(18*MM)
for i,(title,desc) in enumerate(vols):
    col=i%2; row=i//2
    x=back_left+col*(colw+col_gap); y=start_y+row*rowh
    d.text((x,y),title,font=f(FONT_X,3.0),fill=red)
    d.text((x,y+round(5*MM)),desc,font=f(FONT_C,2.55),fill=muted)

# Front cover: quiet center typography, broad negative space.
front_left=round((250+SPINE_MM)*MM); front_width=round(170*MM); center=front_left+front_width//2
small=f(FONT_X,2.8)
txt_center("全 息 實 存 哲 學  ·  一 百 二 十 篇",center,round(20*MM),small,muted)
txt_center("岐伯論選",center,round(78*MM),f(FONT_H,22),ink)
txt_center("典 藏 精 編 本",center,round(104*MM),f(FONT_C,4.2),red)
txt_center("立骨於濁世　求道於近思",center,round(169*MM),f(FONT_X,5.6),muted)
txt_center("歲在丙午金秋　成杰囑命編纂　·　鵬城謹製",center,round(212*MM),f(FONT_C,2.7),muted)

# Spine, based on user's confirmed preliminary 12 mm thickness.
spine_center=round((250+SPINE_MM/2)*MM)
spine_font=f(FONT_H,2.7)
for i,ch in enumerate("岐伯論選"):
    txt_center(ch,spine_center,round((61+i*10)*MM),spine_font,(255,255,255))
txt_center("120篇",spine_center,round(127*MM),f(FONT_X,1.8),(248,244,238))

# Flaps: restrained short copy, prevent overflow by wrapping.
flap_font=f(FONT_C,2.55)
for x0,title,body in [
    (0,"編選識","《岐伯論》五十五冊，通收四千三百九十一篇。本選以文本精研為準繩，精裁一百二十篇，使讀者由篇章見全貌，由問題入義理。"),
    (458,"讀法指要","切己體察，莫作看客。順藤摸瓜，統攬脈絡。得意忘言，貴在踐履。先通讀全編以見其體，再就專題涵泳以得其用。")]:
    left=round((x0+12)*MM); width=round(56*MM); c=left+width//2
    txt_center(title,c,round(20*MM),f(FONT_H,4.1),red)
    d.line((left,round(29*MM),left+width,round(29*MM)),fill=(154,145,132),width=max(1,round(.16*MM)))
    y=round(36*MM)
    for line in wrap_chars(body,flap_font,width):
        d.text((left,y),line,font=flap_font,fill=ink); y+=round(4.6*MM)

bg.save(OUT,"JPEG",quality=94,dpi=(300,300),optimize=True)
print(OUT, bg.size)
