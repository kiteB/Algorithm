# 특정 거리의 도시 찾기
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

# 도시 연결 정보 저장
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(root):
    deq = deque([root])
    distance[root] = 0

    while deq:
        now = deq.popleft()

        # 모든 노드 거리 체크
        for node in graph[now]:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                deq.append(node)

    flag = False
    # 최단거리가 k인 노드를 오름차순으로 출력
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            flag = True

    if not flag:
        print(-1)


bfs(x)