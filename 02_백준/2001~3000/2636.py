# 치즈
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    queue.append((0, 0))

    visited[0][0] = True
    cnt = 0
    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                visited[nr][nc] = True

                if board[nr][nc] == 1:
                    board[nr][nc] = 0
                    cnt += 1
                elif board[nr][nc] == 0:
                    queue.append((nr, nc))

    cheese.append(cnt)
    return cnt


h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
cheese = []

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

time = 0
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(cheese[-2])
