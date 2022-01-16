# 카드
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
numbers = defaultdict(int)

for _ in range(n):
    num = int(sys.stdin.readline())
    numbers[num] += 1

numbers = sorted(numbers.items(), key=lambda x: (-x[1], x[0]))
print(numbers[0][0])
