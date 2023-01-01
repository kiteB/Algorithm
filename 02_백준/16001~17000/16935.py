# 배열 돌리기 3
import sys


def rotate1():  # 배열 상하 반전
    global arr
    arr = arr[::-1]


def rotate2():  # 배열 좌우 반전
    global arr
    for i in range(n):
        arr[i] = arr[i][::-1]


def rotate3():  # 오른쪽으로 90도 회전
    tmp = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            tmp[i][j] = arr[n - 1 - j][i]
    return tmp


def rotate4():  # 왼쪽으로 90도 회전
    tmp = [[0] * m for _ in range(n)]


def rotate5():  # 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 1
    tmp = [[0] * m for _ in range(n)]


def rotate6():  # 1 -> 4, 4 -> 3, 3 -> 2, 2 -> 1
    tmp = [[0] * m for _ in range(n)]


n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
operator = list(map(int, sys.stdin.readline().split()))

for op in operator:

    if op == 1:
        rotate1()
    elif op == 2:
        rotate2()
    elif op == 3:
        arr = rotate3()
    elif op == 4:
        rotate4()
    elif op == 5:
        rotate5()
    else:
        rotate6()

for i in arr:
    print(*i)