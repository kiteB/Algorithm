# 주사위 세개
import sys
from collections import defaultdict

a, b, c = map(int, sys.stdin.readline().split())
num_dict = defaultdict(int)

num_dict[a] += 1
num_dict[b] += 1
num_dict[c] += 1
num_dict = sorted(num_dict.items(), key=lambda x: -x[1])

if len(num_dict) == 1:
    print(10000 + num_dict[0][0] * 1000)
elif len(num_dict) == 2:
    print(1000 + num_dict[0][0] * 100)
else:
    print(max(a, b, c) * 100)