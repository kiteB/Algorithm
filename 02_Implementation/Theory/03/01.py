# 왕실의 나이트
import sys

position = sys.stdin.readline()
rows = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
row, col = rows[position[0]], int(position[1])

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

cnt = 0

for i in range(len(dx)):
    nx = row + dx[i]
    ny = col + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)