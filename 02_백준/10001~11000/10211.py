# Maximum Subarray
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = numbers[0]

    for i in range(1, n):
        dp[i] = max(numbers[i], dp[i - 1] + numbers[i])

    print(max(dp))