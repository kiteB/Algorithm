# 이동하기
import sys

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 아래, 오른쪽, 오른쪽 아래 대각선으로 이동할 수 있으므로
        # 위, 왼쪽, 왼쪽 위 대각선의 dp 중 큰 값과 왼쪽 위 대각선의 maze 값을 더해준다.
        dp[i][j] = maze[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n][m])