# 2 + 1 세일
import sys

n = int(sys.stdin.readline())
price = [int(sys.stdin.readline()) for _ in range(n)]
price.sort(reverse=True)

answer = 0
buy = []
for i in price:
    buy.append(i)
    if len(buy) == 3:
        answer += buy[0] + buy[1]
        buy = []

if len(buy) > 0:
    answer += sum(buy)
print(answer)