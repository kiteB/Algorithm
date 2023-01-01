# 바닥 장식
import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
boards = [list(sys.stdin.readline().strip()) for _ in range(n)]


def dfs(x, y, shape):
    if 0 <= x < n and 0 <= y < m and boards[x][y] == shape:
        boards[x][y] = '.'  # 방문 여부 체크

        if shape == '-':
            dfs(x, y - 1, shape)
            dfs(x, y + 1, shape)
        else:
            dfs(x - 1, y, shape)
            dfs(x + 1, y, shape)

        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if boards[i][j] != '.': # 아직 방문하지 않았다면 dfs 수행
            dfs(i, j, boards[i][j])
            cnt += 1

print(cnt)
