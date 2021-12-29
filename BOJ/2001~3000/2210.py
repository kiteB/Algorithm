# 숫자판 점프
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, num):
    if len(num) == 6:   # 숫자 길이가 6일 경우
        if num not in numbers:  # numbers 리스트에 없으면 추가
            numbers.append(num)
        return  # 길이가 6이므로 종료

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5:     # 이동 가능한 범위 내에 있으면
            dfs(nx, ny, num + boards[nx][ny])


boards = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

numbers = []
for i in range(5):
    for j in range(5):
        dfs(i, j, boards[i][j])

print(len(numbers))