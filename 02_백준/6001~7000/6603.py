# 로또
import sys
from itertools import combinations

while True:
    case = list(map(int, sys.stdin.readline().split()))
    k = case[0]

    if k == 0:
        break

    for combi in combinations(case[1:], 6):
        print(*combi)
    print()