# 색종이
import sys
input = sys.stdin.readline

n = int(input())
maps = [[False] * 100 for _ in range(100)]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if not maps[i][j]:
                maps[i][j] = True
                answer += 1

print(answer)