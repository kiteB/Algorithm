# 눈금의 간격이 1인 M X N 크기의 모눈 종이가 있다.
# 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때,
# K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y 좌표값과 오른쪽 위 꼭짓점의 x, y 좌표값이 빈칸을 사이에 두고 차례로 주어진다.
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0, 0)이고, 오른쪽 위 꼭짓점의 좌표는 (N, M)이다.
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
# 출력: 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다.
# 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
import sys


def bfs(graph, x, y):
    queue = [[x, y]]
    graph[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not graph[nx][ny]:
                    graph[nx][ny] = True
                    cnt += 1
                    queue.append([nx, ny])

    return cnt


M, N, K = map(int, sys.stdin.readline().split())
space = [[False]*N for i in range(M)]       # 영역 정보를 저장할 리스트 (False로 초기화)

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # 직사각형이 존재하는 영역 True로 바꿔주기
    for i in range(y1, y2):
        for j in range(x1, x2):
            space[i][j] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cntList = []

for i in range(M):
    for j in range(N):
        if not space[i][j]:
            cntList.append(bfs(space, i, j))

print(len(cntList))
print(' '.join(map(str, sorted(cntList))))


