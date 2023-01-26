# 패션왕 신해빈
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    costume = defaultdict(int)

    for i in range(n):
        name, kind = input().split()
        costume[kind] += 1

    answer = 1
    # 모든 의상 종류에 대해서, (옷의 개수 + 1)을 곱한다.
    # 각 의상 종류에서 아무것도 선택하지 않는 경우도 고려해야 하기 때문
    for val in costume.values():
        answer *= val + 1

    # 모든 종류의 의상을 선택하지 않은 경우를 제외하기 위해 1을 빼준다.
    print(answer - 1)
