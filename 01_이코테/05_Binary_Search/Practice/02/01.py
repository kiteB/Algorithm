# 고정점 찾기
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
flag = False

for i in data:
    if i == bisect_left(data, i):
        answer = i
        flag = True

if not flag:
    print(-1)
else:
    print(answer)
