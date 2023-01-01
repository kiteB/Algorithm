# 숫자 정사각형
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if i + k < n and j + k < m:
                if board[i][j] == board[i + k][j] == board[i][j + k] == board[i + k][j + k]:
                    answer = max(answer, (k + 1) * (k + 1))

print(answer)