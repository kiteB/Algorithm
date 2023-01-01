# 연결 요소의 개수
import sys
sys.setrecursionlimit(10 ** 7)


def dfs(now):
    visited[now] = True
    for node in graph[now]:
        if not visited[node]:
            dfs(node)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
