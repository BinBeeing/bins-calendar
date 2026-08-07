#!/usr/bin/env python3
"""
매일 실행: 달력 HTML에서 오늘 날짜 🔴 마커 업데이트
"""
from datetime import date
import re

HTML_FILE = "all_in_one.html"

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 기존 🔴 마커 모두 제거
c = re.sub(r'🔴 (\d)', r'\1', c)

# 2. 오늘 날짜 찾아서 🔴 추가
today = date.today()
date_str = f"{today.year}-{today.month:02d}-{today.day:02d}"

# data-date 속성으로 셀 찾기
target = f'data-date="{date_str}">'
idx = c.find(target)

if idx != -1:
    span_start = c.find('<span class="day-num', idx)
    if span_start != -1:
        # 숫자 앞에 🔴 삽입
        c = c[:span_start] + c[span_start:].replace(
            f'>{today.day}</span>', f'>🔴 {today.day}</span>', 1
        ).replace(
            f'>{today.day}<span', f'>🔴 {today.day}<span', 1
        )
    print(f"✓ 오늘 날짜 {date_str} 표시 완료")
else:
    print(f"⚠ {date_str} 셀을 찾지 못했습니다")

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(c)
