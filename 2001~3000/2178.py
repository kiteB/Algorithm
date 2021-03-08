# N X M 크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
# 입력: 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.
# 출력: 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

deq = deque([[0, 0]])
visited[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while deq:
    y, x = deq.popleft()

    if x == M-1 and y == N-1:
        print(visited[y][x])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if visited[ny][nx] == 0 and maze[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                deq.append([ny, nx])
    print(deq)
