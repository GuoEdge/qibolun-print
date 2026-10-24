#!/usr/bin/env python3
"""
全文通读分析整个卷五569篇文章。
逐篇输出分析结果，包括：
1. 属于哪一类主题？（商业竞争/资产投资、职场汇报/权责留痕、体制生存、纯私人/家庭/情感、纯哲学、纯社会热点）
2. 是否与所在册契合？
3. 不契合的原因与推荐归属。
"""

import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# 编写细致审查逻辑并打印各册可疑/不契合清单
