# 도영이가 만든 맛있는 음식
import sys
from itertools import combinations

n = int(sys.stdin.readline())
ingredient = []

for _ in range(n):
    sour, bitter = map(int, sys.stdin.readline().split())   # 신맛과 쓴맛
    ingredient.append([sour, bitter])

answer = 1e9
for i in range(1, n + 1):
    for combi in list(combinations(list(range(n)), i)):
        a = list(combi)     # tuple은 조작이 불편해서 리스트로 변환

        s, b = 1, 0     # 각 조합마다 신맛, 쓴맛 계산값을 저장할 변수
        while a:
            idx = a.pop(0)
            s *= ingredient[idx][0]
            b += ingredient[idx][1]
        answer = min(answer, abs(s - b))

print(answer)