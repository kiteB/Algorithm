# 한나는 고랭지에서 유기농 배추를 재배하기로 하였다. 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
# 이 지렁이는 배추 근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으며 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로, 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 입력: 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해, 첫째 줄에는 배추를 심은 배추밭의 가로 길이 M과 세로 길이 N, 그리고 배추가 심어져 있는 위치의 개수 K가 주어진다.
# 그 다음 K 줄에는 배추의 위치가 주어진다.
# 출력: 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
import sys

sys.setrecursionlimit(10**6)
cnt = 0


def counting(x, y):
    # 전역변수 cnt 설정
    global cnt

    # 방문했던 적이 없는 노드라면 visited[x][y]를 1로 바꿔주기
    if visited[x][y] == 0:
        visited[x][y] = 1

        # 집이 존재한다면 house 1로 바꾸기
        if field[x][y] == 1:
            cnt += 1

            # 오른쪽으로 이동할 수 있으면
            if x < M-1:
                if visited[x+1][y] == 0:
                    counting(x+1, y)

            # 아래로 이동할 수 있으면
            if y < N-1:
                if visited[x][y+1] == 0:
                    counting(x, y+1)

            # 왼쪽으로 이동할 수 있으면
            if x > 0:
                if visited[x-1][y] == 0:
                    counting(x-1, y)

            # 위로 이동할 수 있으면
            if y > 0:
                if visited[x][y-1] == 0:
                    counting(x, y-1)

            return True
        return False


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0]*N for _ in range(M)]   # 배추 정보 저장
    visited = [[0]*N for _ in range(M)]
    earthworm = []  # 지렁이 개수
    
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        field[a][b] = 1

    for i in range(M):
        for j in range(N):
            if counting(i, j):
                earthworm.append(cnt)
                cnt = 0

    print(len(earthworm))