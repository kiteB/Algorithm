# 입국심사
import sys

n, m = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(n)]   # 각 심사대마다 걸리는 시간

start = min(times)      # m(인원수)이 1인 경우, 가장 빠르게 처리하는 심사대 시간
end = times[0] * m      # n(심사대 개수)이 1인 경우, 심사대 하나에서 모든 인원을 처리해야 하므로 (심사대 시간) * (총 인원 수)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for time in times:
        total += (mid // time)  # mid 값을 time 으로 나누면 각 심사대마다 처리할 수 있는 인원수가 나온다

    if total < m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)