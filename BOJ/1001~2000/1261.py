# 알고스팟
# 알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다.
# 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
# 알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다.
# 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
# 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
# 단, 미로의 밖으로 이동 할 수는 없다.
# 벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다.
# 벽을 부수면, 빈 방과 동일한 방으로 변한다.
# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다.
# 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다.
# 0은 빈 방을 의미하고, 1은 벽을 의미한다. (1, 1)과 (N, M)은 항상 뚫려있다.
# 출력: 첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.
import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(N)]      # 미로 정보를 저장할 리스트
distance = [[-1] * M for _ in range(N)]                 # 가중치

deq = deque([[0, 0]])
distance[0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while deq:
    y, x = deq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if distance[ny][nx] == -1:
                if maze[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x]
                    deq.appendleft([ny, nx])
                else:   # maze가 1인 경우 부셔야하므로 +1
                    distance[ny][nx] = distance[y][x] + 1
                    deq.append([ny, nx])

print(distance[N-1][M-1])