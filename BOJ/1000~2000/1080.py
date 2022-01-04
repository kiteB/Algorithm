# 행렬
import sys


def transform(matrix, x, y):  # 0 -> 1, 1 -> 0으로 뒤집는 동작을 수행한다.
    for r in range(x, x + 3):
        for c in range(y, y + 3):
            matrix[r][c] = 1 - matrix[r][c]

    return matrix


n, m = map(int, sys.stdin.readline().split())

matrix1 = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
matrix2 = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if matrix1[i][j] != matrix2[i][j]:
            matrix1 = transform(matrix1, i, j)
            cnt += 1

is_available = True # A를 B로 바꿀 수 있는지 체크하기 위한 변수
for i in range(n):
    for j in range(m):
        if matrix1[i][j] != matrix2[i][j]:
            is_available = False
            break

if is_available:
    print(cnt)
else:
    print(-1)