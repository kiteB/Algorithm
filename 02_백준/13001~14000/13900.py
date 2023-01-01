# 순서쌍의 곱의 합
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
total = sum(numbers)
answer = 0

for i in numbers:
    total -= i
    answer += (total * i)
print(answer)