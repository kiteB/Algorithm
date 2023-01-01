# 지구 온난화
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(r)]  # 지도 정보

# 방향 그래프 정의
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

deq = deque()       # 바다로 변할 섬 리스트
for y in range(r):
    for x in range(c):
        if maps[y][x] == '.':   # 현재 좌표가 바다인 경우
            continue

        cnt = 0     # 주변 바다 개수
        for i in range(4):      # 섬인 경우, 현재 좌표의 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or nx < 0 or ny >= r or nx >= c:  # 범위를 벗어나는 곳은 바다
                cnt += 1
            else:
                if maps[ny][nx] == '.':     # 상하좌우 중 바다가 있으면
                    cnt += 1                # cnt +1

        if cnt >= 3:    # 주변에 바다가 3개 이상 있으면 바다가 된다.
            deq.append([y, x])

# 50년 후 바다가 되는 땅을 바다로 바꿔주자
while deq:
    y, x = deq.popleft() 
    maps[y][x] = '.'

# 섬을 포함하는 가장 작은 직사각형 찾기
start_row, end_row, start_col, end_col = 0, 0, c - 1, 0

for i in range(r):
    if 'X' in maps[i]:  # 섬의 좌표 중 가장 위의 행 저장
        start_row = i
        break

for i in range(r-1, -1, -1):
    if 'X' in maps[i]:  # 섬의 좌표 중 가장 아래 행 저장
        end_row = i
        break

for row in range(start_row, end_row + 1):
    tmp = []        # 섬의 좌표를 저장할 리스트

    for i in range(len(maps[row])):
        if maps[row][i] == 'X':     # 섬의 좌표를 모두 저장
            tmp.append(i)

    if not tmp:     # 섬이 없으면 continue
        continue

    start_col = min(tmp[0], start_col)  # 섬의 좌표 중 가장 왼쪽 열 저장
    end_col = max(tmp[-1], end_col)     # 섬의 좌표 중 가장 오른쪽 열 저장

for y in range(start_row, end_row + 1):
    for x in range(start_col, end_col + 1):
        print(maps[y][x], end='')
    print()