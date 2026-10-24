# 书衣满版底图（含 3mm 出血）：封底 | 书脊 | 封面 一体展开
# 星图按高度等比放大、居中裁切，不变形；书脊段反相为墨底白星，形成书脊色带。
from PIL import Image, ImageOps, ImageFilter

ROOT = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/assets/'
SRC, OUT = ROOT + 'star_map_base.jpg', ROOT + 'jacket_bg_full.jpg'
DPI = 300
BLEED, PAGE_W, PAGE_H, SPINE = 3, 210, 297, 38
W_MM, H_MM = BLEED * 2 + PAGE_W * 2 + SPINE, BLEED * 2 + PAGE_H
mm = lambda v: round(v / 25.4 * DPI)
W, H = mm(W_MM), mm(H_MM)

im = Image.open(SRC).convert('L')
im = ImageOps.autocontrast(im, cutoff=0.5)
scale = H / im.height
im = im.resize((round(im.width * scale), H), Image.LANCZOS)
x0 = (im.width - W) // 2
im = im.crop((x0, 0, x0 + W, H)).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))

# 拓片墨色：纯白纸底微压一点暖灰，线条保持原黑
paper = Image.new('L', im.size, 246)
im = Image.composite(im, paper, im.point(lambda p: 255 if p < 246 else 0))

# 书脊：反相为墨底星图
sx0, sx1 = mm(BLEED + PAGE_W), mm(BLEED + PAGE_W + SPINE)
spine = ImageOps.invert(im.crop((sx0, 0, sx1, H))).point(lambda p: int(18 + p * 0.55))
im = im.convert('RGB')
im.paste(Image.merge('RGB', [spine] * 3), (sx0, 0))
im.save(OUT, quality=92, dpi=(DPI, DPI))
print(OUT, im.size, (W_MM, H_MM))
