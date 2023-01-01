# 카드 놓기
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

numbers = []
for p in permutations(cards, k):
    num = ''.join(map(str, p))

    if num not in numbers:
        numbers.append(num)

print(len(numbers))
