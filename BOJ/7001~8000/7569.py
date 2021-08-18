# 토마토
# m: 상자의 가로 칸의 수, n: 상자의 세로 칸의 수, h: 쌓아올려지는 상자의 수
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
boxes = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

# 방향 그래프 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while deq:
        z, y, x = deq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[z][y][x] + 1
                deq.append([nz, ny, nx])


deq = deque()
# 3차원 배열은 [z][y][x] ([깊이][행][열])
for z in range(h):
    for y in range(n):
        for x in range(m):
            # 익은 토마토 발견하면
            if boxes[z][y][x] == 1:
                deq.append([z, y, x])

bfs()

time = 0            # 토마토가 모두 익기까지 걸리는 시간을 카운트할 변수
ripe = True         # 토마토가 모두 익었는지 체크할 변수
for z in range(h):
    for y in boxes[z]:
        # 아직 익지 않은 토마토가 있다면
        if 0 in y:
            ripe = False
            break
        time = max(time, max(y))

if ripe:
    print(time-1)
else:
    print(-1)
