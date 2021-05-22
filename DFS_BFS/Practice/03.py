# 경쟁적 전염
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
examiner = []
virusList = []

for i in range(n):
    # 시험관 정보 입력
    examiner.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if examiner[i][j] != 0:
            virusList.append([examiner[i][j], 0, i, j])       # virus 리스트에 바이러스 정보, 시간, y 좌표, x 좌표 저장

s, X, Y = list(map(int, sys.stdin.readline().split()))

virusList.sort()
deq = deque(virusList)

# 방향 그래프 정의
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while deq:
    virus, time, y, x = deq.popleft()

    # 시간(time)이 s초 지났다면 종료
    if time == s:
        break

    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있다면
        if 0 <= nx < n and 0 <= ny < n:
            if examiner[ny][nx] == 0:
                examiner[ny][nx] = virus
                deq.append([virus, time+1, ny, nx])

print(examiner[X-1][Y-1])
