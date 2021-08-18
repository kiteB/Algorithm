# 만들 수 없는 금액
import sys

N = int(sys.stdin.readline())
coins = sorted(list(map(int, sys.stdin.readline().split())))
answer = 1

for coin in coins:
    if answer < coin:
        break
    answer += coin

print(answer)

