# 점화식
import sys

n = int(sys.stdin.readline())
dp = [1, 1] + [0] * (n - 1)

for i in range(2, n + 1):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i - 1 - j]

print(dp[n])
