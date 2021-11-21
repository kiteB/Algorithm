# 제곱수의 합
import sys
from math import sqrt

n = int(sys.stdin.readline())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i   # 1이 i개인 경우

    # 제곱수인 경우 dp[0] + 1 형태로 변환 -> 1개
    # dp[4] = dp[4 - 2 * 2] + 1 = dp[0] + 1
    for j in range(1, int(sqrt(i)) + 1):
        if dp[i - j * j] + 1 < dp[i]:   # 최솟값 갱신
            dp[i] = dp[i - j * j] + 1

print(dp[n])