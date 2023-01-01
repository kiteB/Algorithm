# 숨바꼭질
import sys
from collections import deque


def bfs(start):
    deq = deque([start])
    distance[start] = 0

    while deq:
        node = deq.popleft()

        for i in graph[node]:
            if distance[i] == -1:   # 아직 방문하지 않았다면 distance 갱신
                distance[i] = distance[node] + 1
                deq.append(i)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)

for _ in range(m):  # 헛간 정보 저장
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)  # 1부터 bfs 수행
answer = max(distance)
print(distance.index(answer), answer, distance.count(answer))   # 헛간 번호, 헛간까지의 거리, 동일한 거리를 갖는 헛간 개수