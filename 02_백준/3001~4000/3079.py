# 입국심사
import sys

n, m = map(int, sys.stdin.readline().split())
time = list(int(sys.stdin.readline()) for _ in range(n))

start = min(time)           # 최소 시간
end = max(time) * m         # 최대 시간
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in time:
        total += (mid // i)

    if total < m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)