# F7
import sys

n = int(sys.stdin.readline())
scores = [int(sys.stdin.readline()) for _ in range(n)]
scores.sort(reverse=True)

cnt = 0
best = scores[0] + 1
for i in range(n):
    if scores[i] + n >= best:
        cnt += 1
    best = max(best, scores[i] + i + 1)

print(cnt)
