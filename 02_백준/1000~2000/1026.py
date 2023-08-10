# 보물
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
answer = 0
for i in range(n):
    answer += a[i] * b.pop(b.index(max(b)))

print(answer)
