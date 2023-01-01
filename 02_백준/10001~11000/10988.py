# 팰린드롬인지 확인하기
import sys

case = list(sys.stdin.readline().strip())

if case[::] == case[::-1]:
    print(1)
else:
    print(0)