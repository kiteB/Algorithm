# 0의 개수
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    count = 0

    for i in range(n, m + 1):
        temp = str(i)
        count += temp.count('0')

    print(count)
