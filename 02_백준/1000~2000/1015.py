# 수열 정렬
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
sorted_array = sorted(array)
answer = []

for i in range(n):
    idx = sorted_array.index(array[i])
    answer.append(idx)
    sorted_array[idx] = -1

print(*answer)
