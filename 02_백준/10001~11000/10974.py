# 모든 순열
import sys
from itertools import permutations

n = int(sys.stdin.readline())
permutation = list(permutations(list(range(1, n + 1))))

for p in permutation:
    for idx in range(n):
        print(p[idx], end=' ')
    print()