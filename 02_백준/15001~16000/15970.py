# 화살표 그리기
import sys
input = sys.stdin.readline

n = int(input())
dots = [[] for _ in range(n + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    dots[y].append(x)

distance = 0
for dot in dots:
    dot.sort()

    for idx, x in enumerate(dot):
        if idx == 0:
            distance += dot[1] - x
        elif idx == len(dot) - 1:
            distance += x - dot[len(dot) - 2]
        else:
            distance += min(x - dot[idx - 1], dot[idx + 1] - x)

print(distance)
