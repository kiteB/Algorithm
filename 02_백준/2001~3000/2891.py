# 카약과 강품
import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
reserve = list(map(int, input().split()))

damaged_set = set(damaged) - set(reserve)
reserve_set = set(reserve) - set(damaged)

answer = 0
for i in reserve_set:
    if i - 1 in damaged_set:
        damaged_set.remove(i - 1)
    elif i + 1 in damaged_set:
        damaged_set.remove(i + 1)

print(len(damaged_set))
