# 퇴사
import sys

n = int(sys.stdin.readline())
time_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if time_table[i][0] + i > n:    # 상담 종료일이 퇴사일을 넘어간다면
        dp[i] = dp[i + 1]           # 그 전날까지의 금액을 그대로 가져온다.
    else:
        # i일에 상담했을 때의 금액과, 하지 않았을 때의 금액을 비교하여 더 큰 값으로 갱신한다.
        dp[i] = max(time_table[i][1] + dp[i + time_table[i][0]], dp[i + 1])

print(dp[0])