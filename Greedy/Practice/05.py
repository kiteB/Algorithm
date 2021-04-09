# 볼링공 고르기
import sys

N, M = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))
weights = [0 for i in range(11)]

for i in balls:
    weights[i] = balls.count(i)

result = 0
for i in range(1, M+1):
    N -= weights[i]
    result += weights[i] * N

print(result)

