# 줄어드는 수
import sys
from itertools import combinations

n = int(sys.stdin.readline())

result = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = sorted(comb, reverse=True)
        result.append(int(''.join(map(str, comb))))

result.sort()
if n > len(result):
    print(-1)
else:
    print(result[n - 1])