# BABBA
import sys

k = int(sys.stdin.readline())
dp = [(0, 0)] * (k + 1)

dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, k + 1):
    a = dp[i - 1][0] + dp[i - 2][0]
    b = dp[i - 1][1] + dp[i - 2][1]
    dp[i] = (a, b)

print(*dp[k])
