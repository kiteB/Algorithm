# 보물
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
answer = 0

for i in range(n):
    answer += a[i] * b.pop(b.index(max(b)))

print(answer)