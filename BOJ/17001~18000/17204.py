# 죽음의 게임
import sys
from collections import deque


def bfs(v):
    queue = deque([v])
    cnt = 0  # 지목한 횟수

    while queue:
        node = queue.popleft()
        next_node = graph[node]

        if not visited[next_node]:  # 방문하지 않은 노드라면
            visited[next_node] = True  # 방문 여부 체크
            cnt += 1

            if next_node == k:  # 지목된 사람이 보성이라면
                return cnt

            queue.append(next_node)  # 지목된 사람 정보 추가

    return -1


n, k = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(n)]
visited = [False for _ in range(n)]

print(bfs(0))
