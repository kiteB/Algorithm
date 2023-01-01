# 두 수의 합
import sys

n = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

start, end = 0, n - 1
cnt = 0
while start < end:
    total = numbers[start] + numbers[end]
    if total == x:
        cnt += 1
        start += 1
        end -= 1
    elif total < x:
        start += 1
    else:
        end -= 1

print(cnt)
