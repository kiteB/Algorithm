# 촌수 계산
import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()

        for n in graph[node]:
            if result[n] == 0:
                result[n] = result[node] + 1
                queue.append(n)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
print(result[b] if result[b] > 0 else - 1)
