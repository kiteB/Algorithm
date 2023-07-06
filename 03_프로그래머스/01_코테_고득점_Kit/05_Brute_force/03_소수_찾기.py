# Lv.2 | 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    permute = []  # 숫자들의 조합

    for i in range(1, len(numbers) + 1):
        permute += list(permutations(nums, i))
    result = [int(''.join(p)) for p in permute]

    for n in result:
        if n < 2:
            continue
        is_prime = True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            answer.append(n)

    return len(set(answer))
