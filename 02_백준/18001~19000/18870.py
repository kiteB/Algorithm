# 좌표 압축
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
set_data = sorted(set(data))
idx = {}

for i in range(len(set_data)):
    idx[set_data[i]] = i

for i in range(n):
    print(idx[data[i]], end=' ')
