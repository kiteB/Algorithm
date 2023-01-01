# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 t가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다.
# 각 테스트 케이스는 수의 개수 n이 주어지고, 다음에는 n개의 수가 주어진다.
# 출력: 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
import sys
from itertools import combinations

t = int(sys.stdin.readline())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(t):
    case = list(map(int, sys.stdin.readline().split()))
    case = case[1:]
    ans = 0

    for a, b in combinations(case, 2):
        ans += gcd(a, b)
    print(ans)