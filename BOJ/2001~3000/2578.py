# 빙고
import sys

input = sys.stdin.readline


def bingo(graph):
    erase = 0

    for row in graph:  # 가로줄 빙고 확인
        if row.count(0) == 5:
            erase += 1

    for r in range(5):  # 세로줄 빙고 확인
        temp = 0
        for c in range(5):
            if graph[c][r] == 0:
                temp += 1

        if temp == 5:
            erase += 1

    temp = 0
    for k in range(5):  # 왼쪽 위 대각선 빙고 확인
        if graph[k][k] == 0:
            temp += 1
    if temp == 5:
        erase += 1

    temp = 0
    for k in range(5):  # 오른쪽 위 대각선 빙고 확인
        if graph[k][4 - k] == 0:
            temp += 1
    if temp == 5:
        erase += 1

    return erase


board = []
position = {}
for i in range(5):  # 빙고판 만들기, 숫자 위치 저장
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(5):
        position[line[j]] = (i, j)

count = 0
idx = 0
for i in range(5):  # 부르는 수 저장, 숫자 위치 찾기
    line = list(map(int, input().split()))

    for j in range(5):
        y, x = position[line[j]]
        board[y][x] = 0
        idx += 1

        count = bingo(board)
        if count >= 3:
            print(idx)
            exit(0)
