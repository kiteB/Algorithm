# 파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

# dp[y][x][z] -> (y, x) 좌표에 z 방향으로 오는 파이프
# 0: →, 1: ↓, 2: ↘
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# (0, 1) 에 오른쪽 방향의 파이프로 도달하는 방법이 1가지
dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if maps[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]

        if i == 0:
            continue
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]

        if maps[i - 1][j] == 1 or maps[i][j - 1] == 1:
            continue
        dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

print(dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2])
