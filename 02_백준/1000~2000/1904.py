# 01타일
import sys

n = int(sys.stdin.readline())
dp = [0, 1, 2] + [1] * (n - 2)

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[n] % 15746)
