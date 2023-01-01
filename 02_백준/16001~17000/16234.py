# 인구 이동 - 시간 초과
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 땅 정보 저장

# 방향 그래프 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 연합 국가 탐색
def bfs(x, y, visited):
    visited[x][y] = True        # 방문 여부 표시
    deq = deque([[x, y]])

    total = maps[x][y]   # 연합의 인구수
    unions = [[x, y]]    # 현재 국가와 연합인 국가 좌표가 담길 리스트

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능하고 아직 방문 전이면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(maps[nx][ny] - maps[x][y]) <= R:    # 국경선이 열릴 수 있는 조건을 만족한다면
                    visited[nx][ny] = True      # 방문 처리
                    total += maps[nx][ny]       # 연합의 인구수 증가
                    deq.append([nx, ny])
                    unions.append([nx, ny])     # 연합 리스트 추가

    people = total // len(unions)   # (연합을 이루는 각 칸의 인구 수) = (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
    for x, y in unions:
        maps[x][y] = people

    if len(unions) >= 2:         # unions의 길이가 2 이상이라면 인구 이동이 발생한 것이므로 True 리턴
        return True
    return False


day = 0     # 인구 이동 발생 횟수
while True:
    visited = [[False] * N for _ in range(N)]   # 방문 여부 체크용 리스트
    flag = False        # 인구 이동이 발생했는지 체크

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:   # 방문하지 않은 것이면
                tmp = bfs(i, j, visited)

                if tmp:         # 인구 이동 발생했으면, flag를 True로 바꾼다.
                    flag = True

    if not flag:    # 인구 이동이 발생하지 않았으면 break
        break
    day += 1

print(day)