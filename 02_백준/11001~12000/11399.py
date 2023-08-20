# ATM
import sys
input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))
answer = 0

for idx, val in enumerate(times):
    answer += val * (n - idx)

print(answer)