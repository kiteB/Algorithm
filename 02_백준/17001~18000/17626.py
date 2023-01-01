# Four Squares
import sys
from math import sqrt

n = int(sys.stdin.readline())
dp = [0, 1] + [0] * (n - 1)

for i in range(2, n + 1):  # 2부터 n까지
    if i == int(sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n + 1):
    for j in range(1, int(sqrt(i)) + 1):
        if i == int(sqrt(i)) ** 2:  # 제곱근일 경우
            dp[i] = 1
        else:   # 제곱근이 아닐 경우
            dp[i] = min(i, dp[j * j] + dp[i - j * j])

print(dp[n])