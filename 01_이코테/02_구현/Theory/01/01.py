# 상하좌우
# 시작 좌표는 항상 (1, 1)
import sys

N = int(sys.stdin.readline())
commands = list(map(str, sys.stdin.readline().split()))
x, y = 1, 1     # 시작 위치는 항상 (1, 1)

# 북, 동, 남, 서 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = ['U', 'R', 'D', 'L']

nx, ny = 0, 0

for i in commands:
    for j in range(4):
        if i == direction[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    
    # 범위를 벗어나지 않는 경우에만 현재 위치 변경
    if 1 <= nx <= N and 1 <= ny <= N:
        x, y = nx, ny

print(x, y)
