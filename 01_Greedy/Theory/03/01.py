# 1이 될 때까지
import sys

N, K = map(int, sys.stdin.readline().split())
answer = 0

while N >= K:
    if N % K != 0:
        N -= 1
        answer += 1
    else:
        N //= K
        answer += 1

while N > 1:
    N -= 1
    answer += 1
print(answer)