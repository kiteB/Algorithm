# 이상한 술집
import sys

n, k = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(n)]

low = 1
high = max(data)
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = 0

    for i in data:
        total += i // mid

    if total < k:
        high = mid - 1
    else:
        answer = mid
        low = mid + 1

print(answer)
