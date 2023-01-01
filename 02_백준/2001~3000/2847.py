# 게임을 만든 동준이
import sys

n = int(sys.stdin.readline())
points = [int(sys.stdin.readline()) for _ in range(n)]

answer = 0
for i in range(n - 1, 0, -1):
    while points[i - 1] >= points[i]:
        points[i - 1] -= 1
        answer += 1
print(answer)