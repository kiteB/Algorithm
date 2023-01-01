# 1, 2, 3 더하기 5
import sys

MAX = 100001
dp = [[0] * 4 for _ in range(MAX)]

# dp[i][j]: i가 만들어질 때, j로 끝나는 경우
# Ex) dp[3]:
# - dp[3][1]: 1로 끝나는 경우    -> 3 = 2 + 1
# - dp[3][2]: 2로 끝나는 경우    -> 3 = 1 + 2
# - dp[3][3]: 3으로 끝나는 경우  -> 3 = 3
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, MAX):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % 1000000009)