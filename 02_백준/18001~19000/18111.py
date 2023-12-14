# 마인크래프트
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
grounds = []
for _ in range(n):
    grounds.extend(map(int, input().split()))

time = [0 for i in range(257)]
height = 0
for g in range(257):
    block = b

    for ground in grounds:
        if ground <= g:
            time[g] += g - ground
            block -= g - ground
        else:
            time[g] += 2 * (ground - g)
            block += ground - g

    if block >= 0 and time[g] <= time[height]:
        height = g

print(time[height], height)
