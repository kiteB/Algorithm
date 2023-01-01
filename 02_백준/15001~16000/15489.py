# 파스칼 삼각형
import sys

r, c, w = map(int, sys.stdin.readline().split())
dp = [[1 for j in range(i)] for i in range(1, r + w)]

for i in range(2, r + w - 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0
for i in range(w):
    for j in range(i + 1):
        answer += dp[r + i - 1][c + j - 1]

print(answer)
