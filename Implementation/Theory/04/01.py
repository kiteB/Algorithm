# 게임 개발
import sys
from collections import deque


def solution(y, x, d):
    # 현재 위치 방문 여부 표시
    deq = deque([[y, x]])
    maps[y][x] = 2      # 방문 표시 : 2
    cnt = 1

    while deq:
        x, y = deq.popleft()

        # 왼쪽 방향부터 탐색
        for i in range(4):
            # 북(0) -> 서(3), 동(1) -> 북(0), 남(2) -> 동(1), 서(3) -> 남(2)
            # 북쪽은 경우에만 d = 3으로 설정, 아닌 경우에는 -1 해주면 됨.
            if d == 0:
                d = 3
            else:
                d -= 1

            # 이동하기
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 2
                    cnt += 1
                    deq.append([nx, ny])
                    break

            if i == 3:
                # 방향 유지한 채 한 칸 후진 후 2번으로
                nx = x + dx[(d+2) % 4]
                ny = y + dy[(d+2) % 4]
                deq.append([nx, ny])

                if maps[nx][ny] == 1:
                    return cnt


N, M = map(int, sys.stdin.readline().split())
A, B, direct = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 북(0), 동(1), 남(2), 서(3) (시계 방향)
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

print(solution(A, B, direct))
