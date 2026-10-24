import os
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
mem_dir = '/storage/Users/currentUser/Documents/岐伯论/.workbuddy/memory'
os.makedirs(mem_dir, exist_ok=True)
log_file = os.path.join(mem_dir, f"{today}.md")

entry = f"""
## {today} 卷二（阴阳合离）全量内容契合度深度审查
- **审查范围**：卷二全量 179 篇文章（B11 58篇、B12 50篇、B13 71篇），基于全文实质通读（非关键词法）。
- **主要发现**：
  1. 卷二总体契合度约为 84%（151/179 篇真正属于两性亲密与婚恋主题）。
  2. 发现 15 篇严重越界错位文章（如《勉强》谈房屋改造、《车道问题》谈儿童教育与社会边界、《雷峰夕照》谈哲思名相、《经纪人》谈演艺圈危机公关等），应迁往 V1、V3、V5、V6、V7 等相应卷册。
  3. 发现 13 篇卷二内部册间错位文章（如《余庆》结婚十年相处困境误入B11甲册、《one last chance》婚外怀孕出轨误入B12乙册、《天河》《大前门》择偶筛选与吸引误入B13丙册等），需在 B11/B12/B13 之间对调。
"""

with open(log_file, 'a', encoding='utf-8') as f:
    f.write(entry)
print("Updated memory log.")
