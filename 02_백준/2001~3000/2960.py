# 에라토스테네스의 체
import sys

n, k = map(int, sys.stdin.readline().split())
numbers = [True] * (n + 1)
cnt = 0

for i in range(2, n + 2):
    for j in range(i, n + 1, i):
        if numbers[j]:
            numbers[j] = False
            cnt += 1

            if cnt == k:
                print(j)
                break