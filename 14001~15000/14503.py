import sys
from collections import deque


def cleaning(rx, cy, d):
    deq = deque([[rx, cy]])
    maps[rx][cy] = 2    # 현재 위치 청소
    cnt = 1

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            # 왼쪽 방향 탐색
            # 북(0) -> 서(3), 동(1) -> 북(0), 남(2) -> 동(1), 서(3) -> 남(2)
            if d != 0:
                d -= 1
            else:
                d = 3

            nx = x + dx[d]
            ny = y + dy[d]

            # a. 왼쪽 방향에 아직 청소하지 않은 공간 존재
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    cnt += 1
                    maps[nx][ny] = 2
                    deq.append([nx, ny])
                    break

            # c. 네 방향 모두 청소가 되어있거나 벽인 경우
            if i == 3:
                # 방향 유지한 채 한 칸 후진 후 2번으로
                nx = x + dx[(d+2) % 4]
                ny = y + dy[(d+2) % 4]
                deq.append([nx, ny])

                # d.네 방향 모두 청소가 이미 되었거나 벽이면서, 뒤쪽 방향도 벽인 경우
                if maps[nx][ny] == 1:
                    return cnt


N, M = map(int, sys.stdin.readline().split())
r, c, direction = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(cleaning(r, c, direction))