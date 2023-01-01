# 위에서 아래로
import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(numbers, reverse=True):
    print(i, end=' ')