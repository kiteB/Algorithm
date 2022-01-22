# 주사위 게임
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
prize = 0

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    num_dict = defaultdict(int)

    num_dict[a] += 1
    num_dict[b] += 1
    num_dict[c] += 1
    num_dict = sorted(num_dict.items(), key=lambda x: -x[1])

    temp = 0
    if len(num_dict) == 1:
        temp = 10000 + num_dict[0][0] * 1000
    elif len(num_dict) == 2:
        temp = 1000 + num_dict[0][0] * 100
    else:
        temp = max(a, b, c) * 100
    prize = max(prize, temp)

print(prize)