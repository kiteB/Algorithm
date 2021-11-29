# 돌다리
import sys
from collections import deque


def bfs(now):
    deq = deque()
    deq.append(now)

    while deq:
        node = deq.popleft()

        for i in range(8):
            if i < 6:
                nx = node + dx[i]
            else:
                nx = node * dx[i]

            if 0 <= nx <= 100000 and distance[nx] == -1:   # 이동할 수 있는 경우
                deq.append(nx)
                distance[nx] = distance[node] + 1


a, b, n, m = map(int, sys.stdin.readline().split())
dx = [1, -1, a, -a, b, -b, a, b]    # 이동할 수 있는 8가지 방법

distance = [-1] * 100001     # 이동 횟수
distance[n] = 0      # n 위치까지 이동 횟수는 0

bfs(n)

print(distance[m])

