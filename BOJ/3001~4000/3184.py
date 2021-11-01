# 양
import sys
from collections import deque

# 방향 그래프 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    visited[a][b] = True
    deq = deque()
    deq.append([a, b])
    sheep, wolf = 0, 0  # 양, 늑대 개수

    while deq:
        x, y = deq.popleft()

        if maps[x][y] == 'o':       # 양인 경우
            sheep += 1
        elif maps[x][y] == 'v':     # 늑대인 경우
            wolf += 1

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:  # 범위를 벗어난 경우
                continue
            else:
                if maps[nx][ny] != '#' and not visited[nx][ny]:     # 울타리가 아니고 방문하지 않았다면
                    visited[nx][ny] = True  # 방문 체크
                    deq.append([nx, ny])

    if sheep > wolf:    # 양이 늑대보다 많으면 늑대를 쫓아낸다.
        wolf = 0
    else:               # 그렇지 않다면 늑대가 모든 양을 먹는다.
        sheep = 0

    return sheep, wolf


r, c = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

sheep_cnt, wolf_cnt = 0, 0  # 양, 늑대 개수
for i in range(r):
    for j in range(c):
        if maps[i][j] != '#' and not visited[i][j]:     # 울타리가 아니고 방문하지 않았다면 BFS 수행
            tmp = bfs(i, j)
            sheep_cnt += tmp[0]
            wolf_cnt += tmp[1]

print(sheep_cnt, wolf_cnt)