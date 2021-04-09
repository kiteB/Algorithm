# 모험가 길드
import sys

N = int(sys.stdin.readline())
adventurer = sorted(list(map(int, sys.stdin.readline().split())))

group = 0   # 그룹에 속한 인원 수
cnt = 0     # 총 그룹 수

for i in adventurer:
    group += 1

    if i <= group:
        cnt += 1
        group = 0

print(cnt)



