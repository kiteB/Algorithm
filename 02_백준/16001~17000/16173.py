# 점프왕 쩰리 (Small)
import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        if maps[x][y] == -1:    # 승리 지점에 도착
            return "HaruHaru"

        jump = maps[x][y]

        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

    return "Hing"


print(bfs(0, 0))