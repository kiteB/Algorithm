# GCD 합
import sys
from itertools import combinations
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


T = int(input())
for _ in range(T):
    case = list(map(int, input().split()))[1:]
    answer = 0

    for a, b in combinations(case, 2):
        answer += gcd(a, b)

    print(answer)
