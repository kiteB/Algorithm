# 도전 숫자왕
import sys
from itertools import combinations

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

total = set()
for i in range(1, n + 1):
    for combi in combinations(numbers, i):
        total.add(sum(combi))

print(sum(numbers) - len(total))