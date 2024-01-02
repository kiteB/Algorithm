# 가로수
import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
trees = [int(input()) for _ in range(n)]

distances = [abs(trees[i + 1] - trees[i]) for i in range(n - 1)]
tmp = distances[0]

for dist in distances:
    tmp = gcd(tmp, dist)

len_arr = (max(trees) - min(trees)) // tmp + 1
print(len_arr - n)
