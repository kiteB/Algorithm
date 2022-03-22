# 반지
import sys

input = sys.stdin.readline

target = input().strip()
n = int(input())
count = 0

for _ in range(n):
    ring = input().strip()

    for i in range(len(ring)):
        temp = ring[i:] + ring[0:i]
        if target in temp:
            count += 1
            break

print(count)