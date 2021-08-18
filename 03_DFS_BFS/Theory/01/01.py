# 음료수 얼려 먹기
import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]


def dfs(x, y):
    # 이동 가능할 경우 좌표를 바꿔서 이동
    if 0 <= x < n and 0 <= y < m and maps[x][y] == 0:
        maps[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)