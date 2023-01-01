# 과자
import sys

k, n, m = map(int, sys.stdin.readline().split())
needed_money = k * n - m

if needed_money > 0:
    print(needed_money)
else:
    print(0)
