# 약수
import sys
input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))

if min(divisors) != 1:
    print(max(divisors) * min(divisors))
