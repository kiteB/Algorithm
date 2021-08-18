# 미로 탈출
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    deq = deque([[y, x]])
    visited[y][x] = 1

    while deq:
        y, x = deq.popleft()

        # 미로 끝에 도착하면 종료
        if x == m-1 and y == n-1:
            print(visited[y][x])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0 and maze[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    deq.append([ny, nx])


bfs(0, 0)