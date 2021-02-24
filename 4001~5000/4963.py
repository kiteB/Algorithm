import sys


def bfs(graph, y, x):
    cnt = 1

    queue = [[y, x]]
    graph[y][x] = 0

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    while queue:
        y, x = queue.pop()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] == 1:
                    cnt += 1
                    graph[ny][nx] = 0
                    queue.append([ny, nx])

    return cnt


while True:
    # 지도의 너비 w, 높이 h 저장
    w, h = map(int, sys.stdin.readline().split())
    # 지도 정보 저장
    mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

    cntList = []  # 섬의 개수를 저장할 리스트

    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if mat[i][j]:
                cntList.append(bfs(mat, i, j))

    print(len(cntList))
