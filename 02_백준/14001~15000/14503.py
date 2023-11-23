# 로봇 청소기
import sys
from collections import deque
input = sys.stdin.readline


def cleaning(rx, cy, d):
    queue = deque([[rx, cy]])
    maps[rx][cy] = 2  # 현재 위치 청소
    cnt = 1  # 청소한 칸의 개수 저장할 변수

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            # 왼쪽으로 회전
            d = (d - 1) % 4

            nr = x + dr[d]
            nc = y + dc[d]

            # 범위 벗어나는 경우 체크
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            # a. 왼쪽 방향에 아직 청소하지 않은 공간 존재
            if maps[nr][nc] == 0:
                cnt += 1
                maps[nr][nc] = 2
                queue.append([nr, nc])
                break

            # c. 네 방향 모두 청소가 되어있거나 벽인 경우
            if i == 3:
                # 방향 유지한 채 한 칸 후진 후 2번으로
                nr = x + dr[(d + 2) % 4]
                nc = y + dc[(d + 2) % 4]
                queue.append([nr, nc])

                # d. 네 방향 모두 청소가 이미 되었거나 벽이면서, 뒤쪽 방향도 벽인 경우
                if maps[nr][nc] == 1:
                    return cnt


n, m = map(int, input().split())
r, c, direction = map(int, input().split())  # 로봇 청소기 좌표 (r, c), 바라보는 방향 d
maps = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

print(cleaning(r, c, direction))
