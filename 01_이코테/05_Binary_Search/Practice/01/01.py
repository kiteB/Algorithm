# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

count = bisect_right(data, m) - bisect_left(data, m)

if count == 0:
    print(-1)
else:
    print(count)

