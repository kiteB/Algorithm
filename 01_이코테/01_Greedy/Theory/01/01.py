# 큰 수의 법칙
import sys

N, M, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort(reverse=True)
idx = K
answer = 0

for i in range(M):
    if i == idx:
        answer += numbers[1]
        idx += K + 1
    else:
        answer += numbers[0]
print(answer)