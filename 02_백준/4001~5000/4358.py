# 생태학
import sys
from collections import defaultdict

trees = defaultdict(int)
total = 0  # 전체 나무 개수

while True:
    name = sys.stdin.readline().strip()
    if not name:
        break
    trees[name] += 1
    total += 1

trees = sorted(trees.items(), key=lambda x: x[0])
for key, val in trees:
    print('%s %.4f' % (key, val / total * 100))
