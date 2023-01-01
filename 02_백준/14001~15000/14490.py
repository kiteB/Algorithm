# 백대열
import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n, m = map(int, sys.stdin.readline().split(':'))
print(f'{n // gcd(n, m)}:{m // gcd(n, m)}')