# 두 자연수 A, B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
# 두 자연수 A, B가 주어졌을 때, A와 B의 최소공배수를 구하시오.
import sys


# 최대공약수 구하기 (gcd)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 최소공배수 구하기 (lcm)
def lcm(a, b):
    return a * b // gcd(a, b)


T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A, B))
