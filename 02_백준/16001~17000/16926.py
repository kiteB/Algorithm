# 배열 돌리기 1
import sys

n, m, r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i     # 돌려지는 배열 중 첫 번째 인덱스
        tmp = data[x][y]

        for j in range(i + 1, n - i):  # 왼쪽 배열 회전
            x = j
            current = data[x][y]    # 현재 값 저장
            data[x][y] = tmp        # 이전 칸의 값 저장
            tmp = current           # 다음 칸에서 사용할 값

        for j in range(i + 1, m - i):  # 아래쪽 배열 회전
            y = j
            current = data[x][y]
            data[x][y] = tmp
            tmp = current

        for j in range(i + 1, n - i):  # 오른쪽 배열 회전
            x = n - j - 1
            current = data[x][y]
            data[x][y] = tmp
            tmp = current

        for j in range(i + 1, m - i):  # 위쪽 배열 회전
            y = m - j - 1
            current = data[x][y]
            data[x][y] = tmp
            tmp = current

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()