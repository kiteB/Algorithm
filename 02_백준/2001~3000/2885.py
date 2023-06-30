# 초콜릿 식사
import sys
from math import ceil
input = sys.stdin.readline

k = int(input())
print(ceil(k ** 0.5))
size = 2 ** ceil(k ** 0.5)
print(size)

cnt = 0
while 2 * cnt < k:
    cnt += 1
    size //= 2

print(cnt)
