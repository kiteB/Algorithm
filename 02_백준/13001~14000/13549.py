# 숨바꼭질 3
import sys
from collections import deque


def bfs():
    deq = deque([n])
    time[n] = 0             # 수빈이의 현재 위치인 n까지 가는데 걸리는 시간은 0

    while deq:
        x = deq.popleft()

        if x == k:
            print(time[x])
            break

        # 2 * X로 이동
        if x*2 < MAX and time[x*2] == -1:
            deq.appendleft(x*2)
            time[x*2] = time[x]

        # X + 1로 이동
        if x+1 < MAX and time[x+1] == -1:
            deq.append(x+1)
            time[x+1] = time[x] + 1

        # X - 1로 이동
        if 0 <= x-1 and time[x-1] == -1:
            deq.append(x-1)
            time[x-1] = time[x] + 1


n, k = map(int, sys.stdin.readline().split())
MAX = 100001
time = [-1] * MAX
bfs()