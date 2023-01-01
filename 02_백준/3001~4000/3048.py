# 개미
import sys

input = sys.stdin.readline

n1, n2 = map(int, input().split())
ant1 = list(input().strip())
ant2 = list(input().strip())
T = int(input())

ant1.reverse()
direction = {}

for i in ant1:  # → 방향으로 이동
    direction[i] = True
for i in ant2:  # ← 방향으로 이동
    direction[i] = False

ants = ant1
ants.extend(ant2)

for _ in range(T):
    idx = 0

    while idx < len(ants) - 1:
        if direction[ants[idx]] and not direction[ants[idx + 1]]:
            ants[idx], ants[idx + 1] = ants[idx + 1], ants[idx]
            idx += 1
        idx += 1

print(''.join(ants))