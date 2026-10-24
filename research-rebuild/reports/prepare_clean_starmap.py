import os
from PIL import Image, ImageOps

ROOT = '/storage/Users/currentUser/Documents/岐伯论'
ASSETS_DIR = os.path.join(ROOT, 'research-rebuild/assets')
orig_path = os.path.join(ASSETS_DIR, 'star_map_base.jpg')

raw = Image.open(orig_path).convert('RGB')
w, h = raw.size # 1920, 856

# 保持原始黑白拓片的古拙纯粹性，微调色阶让纸底洁净平整，墨线清晰劲拔
gray = raw.convert('L')
# 自动提升微对比度（增强拓片版画感）
contrast_gray = ImageOps.autocontrast(gray, cutoff=0.5)

# A4 比例高宽比为 1.414 (高/宽)，而原图是横幅长卷 (宽1920, 高856，宽/高 = 2.24)
# 艺术画册典藏设计原则：绝不压扁或拉伸原图！
# 1. 封面完整原画：在封面页中横跨上部或中上部，居中放置完整的星图核心浑仪天河拓片
contrast_gray.save(os.path.join(ASSETS_DIR, 'star_map_authentic_full.png'), 'PNG')

# 2. 封面构图切幅：取原图右半部宏大的天河银汉与二十八宿核心（1000~1920, 0~856），比例更适合垂直页面构图
cover_slice = contrast_gray.crop((920, 0, 1920, 856))
cover_slice.save(os.path.join(ASSETS_DIR, 'star_map_cover_clean.png'), 'PNG')

# 3. 封底构图切幅：取原图左半部紫微垣与北斗天市垣核心（0~1000, 0~856）
back_slice = contrast_gray.crop((0, 0, 1000, 856))
back_slice.save(os.path.join(ASSETS_DIR, 'star_map_back_clean.png'), 'PNG')

print("Authentic star map slices generated successfully!")
