# 먹을 것인가 먹힐 것인가
import sys
from bisect import bisect
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    answer = 0
    for num in a:
        answer += bisect(b, num - 1)
    print(answer)
