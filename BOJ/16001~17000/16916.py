# 부분 문자열
import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

if p in s:
    print(1)
else:
    print(0)