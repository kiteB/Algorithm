# 내 선물을 받아줘 2
import sys

n = int(sys.stdin.readline())
maps = list(sys.stdin.readline().strip())

gift = 0
for i in range(n - 1):
    if maps[i] == 'E' and maps[i + 1] == 'W':
        gift += 1

print(gift)