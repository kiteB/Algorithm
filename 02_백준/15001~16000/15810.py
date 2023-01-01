# 풍선 공장
import sys

n, m = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(times) * m
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = 0

    for i in times:
        total += (mid // i)

    if total < m:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1

print(answer)
