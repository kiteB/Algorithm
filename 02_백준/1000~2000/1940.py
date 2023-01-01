# 주몽
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
materials = sorted(list(map(int, sys.stdin.readline().split())))

start, end = 0, n - 1
cnt = 0
while start < end:
    total = materials[start] + materials[end]
    if total == m:
        cnt += 1
        start += 1
        end -= 1
    elif total < m:
        start += 1
    else:
        end -= 1

print(cnt)