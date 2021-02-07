# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하시오.
import sys

A, B, C = map(int, sys.stdin.readline().split())
num = 0

if A >= B and A >= C:
    if B >= C:
        num = B
    else:
        num = C
elif B >= C and B >= A:
    if C >= A:
        num = C
    else:
        num = A
elif C >= A and C >= B:
    if A >= B:
        num = A
    else:
        num = B

print(num)