# 가장 긴 증가하는 부분 수열 2
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [0]

for num in numbers:
    if dp[-1] < num:
        dp.append(num)
    else:
        dp[bisect_left(dp, num)] = num

print(len(dp) - 1)
