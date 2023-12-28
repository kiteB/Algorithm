# 적록색약
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(r, c):
    visited[r][c] = True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if not visited[nr][nc] and maps[nr][nc] == maps[r][c]:
            dfs(nr, nc)


n = int(input())
maps = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
blindness_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1


visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'G':
            maps[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            blindness_cnt += 1

print(cnt, blindness_cnt)
