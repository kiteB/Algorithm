# 색종이 만들기
import sys
input = sys.stdin.readline


def check(n, x, y):
    global white, blue

    now = boards[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if now != boards[i][j]:
                size = n // 2
                check(size, x, y)
                check(size, x, y + size)
                check(size, x + size, y)
                check(size, x + size, y + size)
                return

    if now == 0:
        white += 1
    else:
        blue += 1


n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

check(n, 0, 0)

print(white)
print(blue)
