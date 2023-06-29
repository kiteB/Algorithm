# 두 배열의 합
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        a_dict[sum(a[i:j + 1])] += 1

answer = 0
for i in range(m):
    for j in range(i, m):
        answer += a_dict[T - sum(b[i:j + 1])]

print(answer)
