# 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

T = int(input())
dp = [1, 2, 4, 7]

for _ in range(T):
    n = int(input())

    for i in range(len(dp), n):
        dp.append((dp[-3] + dp[-2] + dp[-1]) % 1000000009)
    print(dp[n - 1])
