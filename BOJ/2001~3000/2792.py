# 보석 상자
import sys
import math

n, m = map(int, sys.stdin.readline().split())
jewelry = [int(sys.stdin.readline()) for _ in range(m)]     # 보석 색깔 종류 개수 저장

start = 1           # 최소 1명은 보석을 가져야 하므로
end = max(jewelry)  # 보석 색깔 중 가장 많은 보석 개수 (1명에게 다 나눠주는 경우) 

while start <= end:
    mid = (start + end) // 2    # 한 명이 가져가는 보석 수
    total = 0   # 보석을 가지고 있는 아이들 수

    for j in jewelry:
        total += math.ceil(j / mid)     # 올림을 이용해서 보석을 갖게 되는 인원 수 계산하기

    if total > n:       # n보다 더 많은 사람이 보석을 가져간 것이므로 mid 값을 늘려야 한다
        start = mid + 1
    else:
        end = mid - 1

print(start)