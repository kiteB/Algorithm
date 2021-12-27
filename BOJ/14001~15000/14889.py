# 스타트와 링크
import sys
from itertools import combinations

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
combi = list(combinations(list(range(1, n + 1)), n // 2))   # 팀 조합 개수

answer = int(1e9)
for i in range(len(combi) // 2):
    start_team = list(combinations(combi[i], 2))
    link_team = list(combinations(combi[len(combi) - 1 - i], 2))

    start, link = 0, 0      # 스타트팀과 링크팀의 능력치
    for j in start_team:
        a, b = j
        start += board[a - 1][b - 1]
        start += board[b - 1][a - 1]

    for j in link_team:
        a, b = j
        link += board[a - 1][b - 1]
        link += board[b - 1][a - 1]

    answer = min(answer, abs(start - link))

print(answer)