# 두 개의 자연수를 입력받아 최대공약수와 최소공배수를 출력하시오.
# 입력: 첫째 줄에는 두 개의 자연수가 주어진다.
# 출력: 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최대공배수를 출력하라.
import sys

A, B = map(int, sys.stdin.readline().split())


# 최대공약수 구하기 (gcd)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 최소공배수 구하기 (lcm)
def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(A, B))
print(lcm(A, B))