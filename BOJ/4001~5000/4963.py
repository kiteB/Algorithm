import sys


def bfs(graph, y, x):
    cnt = 1     # 섬의 개수를 카운트하기 위한 변수

    queue = [[y, x]]
    graph[y][x] = 0

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    while queue:
        # 현재 위치를 pop
        y, x = queue.pop()
        
        # 상하좌우, 대각선 4방향의 총 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 지도 밖으로 나가지 않고
            if 0 <= nx < w and 0 <= ny < h:
                # 육지인 경우
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
    cnt_list = []  # 섬의 개수를 저장할 리스트

    # 0 두 개 입력받았을 경우 종료
    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if mat[i][j]:
                cnt_list.append(bfs(mat, i, j))

    print(len(cnt_list))