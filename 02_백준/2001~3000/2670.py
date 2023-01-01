# 연속부분최대곱
import sys

n = int(sys.stdin.readline())
numbers = [float(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i] * numbers[i - 1])

print(f'{max(numbers):.3f}')