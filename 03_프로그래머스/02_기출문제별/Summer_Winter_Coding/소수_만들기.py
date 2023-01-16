# 소수 만들기
from itertools import combinations


def is_prime_number(i):
    total = sum(i)
    for i in range(2, total):
        if total % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    numbers = list(combinations(nums, 3))

    for i in numbers:
        if is_prime_number(i):
            answer += 1

    return answer