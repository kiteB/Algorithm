# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(y, x):
    queue = deque([(y, x)])
    visited = deque([(y, x)])

    shark_size = 2           # 아기 상어 크기
    time = 0            # 물고기를 잡아먹을 수 있는 시간
    fish_cnt = 0            # 상어가 먹은 물고기 수
    eat_flag = False    # 현재 상태에서 물고기를 먹은 경우, for 문을 실행시키지 않기 위함.

    answer = 0

    while queue:
        # 위쪽, 왼쪽을 우선적으로 하기 위해서 오름차순으로 정렬
        queue = deque(sorted(queue))

        for _ in range(len(queue)):
            y, x = queue.popleft()

            # 물고기를 먹을 수 있는 경우
            if 1 <= maps[y][x] < shark_size:
                maps[y][x] = 0
                fish_cnt += 1

                # 상어 크기 만큼 먹었으면 fish 초기화 & 아기 상어 크기 +1
                if fish_cnt == shark_size:
                    shark_size += 1
                    fish_cnt = 0

                queue, visited = deque(), deque([(y, x)])
                eat_flag = True

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and (ny, nx) not in visited:
                    if maps[ny][nx] <= shark_size:
                        queue.append((ny, nx))
                        visited.append((ny, nx))

            # 현재 위치에서 물고기를 먹었다면, 더 이상 for문을 돌 필요가 없다.
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


def find_start():
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                maps[i][j] = 0
                return i, j


start_y, start_x = find_start()
print(bfs(start_y, start_x))
