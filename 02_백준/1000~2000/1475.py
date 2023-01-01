# 방 번호
import sys
import math

number = list(map(int, sys.stdin.readline().strip()))
numbers = [0] * 9

for i in number:
    if i == 6 or i == 9:
        numbers[6] += 0.5
    else:
        numbers[i] += 1

print(math.ceil(max(numbers)))