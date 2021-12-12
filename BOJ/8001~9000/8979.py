# 올림픽
import sys

n, k = map(int, sys.stdin.readline().split())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    if scores[i][0] == k:    # 인덱스 찾기
        idx = i
        break

gold, silver, bronze = scores[idx][1], scores[idx][2], scores[idx][3]
rank = 1
for i in range(n):
    if scores[i][1] > gold:
        rank += 1
    elif scores[i][1] == gold:
        if scores[i][2] > silver:
            rank += 1
        elif scores[i][2] == silver:
            if scores[i][3] > bronze:
                rank += 1
print(rank)