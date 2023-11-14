# 흙길 보수하기
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()

dist, result = 0, 0
for start, end in pool:
    if dist < start:
        dist = start

    cnt = (end - dist) // l
    if (end - dist) % l != 0:
        cnt += 1
    result += cnt
    dist += cnt * l

print(result)
