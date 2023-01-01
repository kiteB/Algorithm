# 그림
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
paint = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# 방향 그래프 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y, x):
    visited[y][x] = True  # 방문 체크
    deq = deque([[y, x]])
    cnt = 1

    while deq:
        y, x = deq.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= ny < n and 0 <= nx < m:
                if paint[ny][nx] == 1 and not visited[ny][nx]:  # 그림이 있고, 아직 방문하지 않았다면
                    cnt += 1
                    deq.append([ny, nx])
                    visited[ny][nx] = True

    return cnt


answer = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and not visited[i][j]:  # 그림이 있고, 아직 방문하지 않았다면 bfs 수행
            answer.append(bfs(i, j))

print(len(answer))
print(max(answer) if len(answer) > 0 else 0)