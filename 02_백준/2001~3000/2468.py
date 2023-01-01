# 안전 영역
import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, height):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 이동 가능한 범위 내에 있고, 아직 방문하지 않았으며 잠기지 않으면
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] > height:
            visited[nx][ny] = True
            dfs(nx, ny, height)


n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_height = max(map(max, maps))

answer = 1
for h in range(1, max_height + 1):  # 1부터 max_height까지
    visited = [[False] * n for _ in range(n)]   # 방문 여부를 체크하기 위한 리스트
    safe = 0    # 물에 잠기지 않는 영역의 개수

    for i in range(n):
        for j in range(n):
            if maps[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                safe += 1
                dfs(i, j, h)

    answer = max(answer, safe)

print(answer)
