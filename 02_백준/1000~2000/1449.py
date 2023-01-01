# 수리공 항승
import sys

n, l = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))
location.sort()

start = location[0]
end = start + l     # 시작 지점부터 테이프를 붙였을 때 테이프의 끝 위치

tape = 1
for i in location:
    if start <= i < end:    # 테이프 범위 내에 있으면 아무런 동작 X
        continue
    else:               # 새로 테이프를 붙여야 한다.
        tape += 1
        start = i
        end = start + l

print(tape)
