#!/bin/sh
# 单个分册重建脚本 - 用法: ./rebuild_single.sh B01 build_volume_v1.js

BOOKLET="$1"
SCRIPT="$2"

if [ -z "$BOOKLET" ] || [ -z "$SCRIPT" ]; then
    echo "用法: $0 <分册代码> <生成脚本>"
    exit 1
fi

BASE="/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"

# 在正确目录执行，避免 getcwd 问题
cd "$BASE" || exit 1
/data/service/hnp/bin/node "$SCRIPT" "$BOOKLET"
