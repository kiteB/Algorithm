# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾아라.
# 일곱 난쟁이의 키의 합은 100이다. 이 조건을 이용해서 일곱 난쟁이의 키를 오름차순으로 출력하라.
import sys
from itertools import combinations

case = []
for i in range(9):
    case.append(int(sys.stdin.readline()))

case.sort()

lst = list(combinations(case, 7))
for i in lst:
    if sum(i) == 100:
        for j in i:
            print(j)
        break