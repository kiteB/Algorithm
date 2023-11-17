# 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
                graph[nx][ny] = True
                cnt += 1
                queue.append([nx, ny])

    return cnt


m, n, k = map(int, input().split())
space = [[False] * n for _ in range(m)]       # 영역 정보를 저장할 리스트 (False로 초기화)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    # 직사각형이 존재하는 영역 True
    for i in range(y1, y2):
        for j in range(x1, x2):
            space[i][j] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = []

# 각 영역의 크기 계산
for i in range(m):
    for j in range(n):
        if not space[i][j]:
            answer.append(bfs(space, i, j))

print(len(answer))
print(' '.join(map(str, sorted(answer))))
