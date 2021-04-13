from sys import stdin
from collections import deque


def cleaning(rx, cy, d):
    deq = deque([[rx, cy]])
    maps[rx][cy] = 2    # 현재 위치 청소
    cnt = 1

    while deq:
        x, y = deq.popleft()

        # 회전
        for i in range(4):
            if d != 0:
                d -= 1
            else:
                d = 3

            nx = x + dx[d]
            ny = y + dy[d]

            # 왼쪽 방향에 아직 청소하지 않은 공간이 있을 경우
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    deq.append([nx, ny])
                    cnt += 1
                    maps[nx][ny] = 2
                    break

            # 사방에 갈 곳이 없는 경우
            if i == 3:
                # 방향 유지한 채 한칸 후진 후 2번으로
                nx = x + dx[(d+2) % 4]
                ny = y + dy[(d+2) % 4]
                deq.append([nx, ny])

                # 뒷 칸도 벽인 경우
                if maps[nx][ny] == 1:
                    return cnt


N, M = map(int, stdin.readline().split())
r, c, direction = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for i in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(cleaning(r, c, direction))