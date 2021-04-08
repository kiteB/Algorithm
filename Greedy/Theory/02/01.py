# 숫자 카드 게임
import sys

N, M = map(int, sys.stdin.readline().split())
answer = 0

for i in range(N):
    card = list(map(int, sys.stdin.readline().split()))
    answer = max(answer, min(card))

print(answer)