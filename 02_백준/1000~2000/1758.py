# 알바생 강호
import sys

n = int(sys.stdin.readline())
tips = [int(sys.stdin.readline()) for _ in range(n)]
tips.sort(reverse=True)
answer = 0

for i in range(n):
    tip = tips[i] - i
    if tip > 0:
        answer += tip
print(answer)