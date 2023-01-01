# 경쟁적 전염
import sys
from collections import deque

# 방향 그래프 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():

    while deq:
        v, time, x, y = deq.popleft()   # 바이러스 번호, 시간, x 좌표, y 좌표

        if time == s:   # s초 지났다면 종료
            break

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:  # 범위 안에 있고, 시험관이 비어 있다면
                graph[nx][ny] = v   # 바이러스 증식
                deq.append([v, time + 1, nx, ny])

    return graph[target_x - 1][target_y - 1]


n, k = map(int, sys.stdin.readline().split())
graph = []  # 시험관 정보
virus = []  # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j], 0, i, j])    # 바이러스 번호, 시간, 좌표

s, target_x, target_y = map(int, sys.stdin.readline().split())

virus.sort()    # 번호가 낮은 바이러스부터 증식하기 떄문에 오름차순으로 정렬
deq = deque(virus)

print(bfs())