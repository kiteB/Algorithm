# 외판원 순회 2
import sys
from itertools import permutations


n = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
permutation = list(permutations(list(range(1, n + 1))))
path = permutation[:len(permutation) // n]   # 1로 시작하는 경우만 저장

answer = 1e9
for p in path:  # 각 경로마다 비용 계산
    total = []

    for i in range(n - 1):
        total.append(costs[p[i] - 1][p[i + 1] - 1])

    total.append(costs[p[n - 1] - 1][p[0] - 1])

    if 0 not in total:
        answer = min(answer, sum(total))
print(answer)