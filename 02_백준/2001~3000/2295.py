# 세 수의 합
import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

sum_set = set()
for i in numbers:
    for j in numbers:
        sum_set.add(i + j)

answer = 0
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if numbers[i] - numbers[j] in sum_set:
            answer = max(answer, numbers[i])

print(answer)
