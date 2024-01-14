# 숫자 야구
import sys
from itertools import permutations
input = sys.stdin.readline


def bulls_and_cows(numbers, test, strike, ball):
    remove_list = []

    for num in numbers:
        s, b = 0, 0

        for i in range(3):
            for j in range(3):
                if num[i] == int(test[j]):
                    if i == j:
                        s += 1
                    else:
                        b += 1

        if strike != s or ball != b:
            remove_list.append(num)

    for r in remove_list:
        numbers.remove(r)


n = int(input())
numbers = list(permutations(list(range(1, 10)), 3))     # 가능한 모든 경우의 수 저장

for _ in range(n):
    test, strike, ball = map(int, input().split())
    bulls_and_cows(numbers, str(test), strike, ball)

print(len(numbers))
