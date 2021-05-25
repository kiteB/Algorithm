# 두 개 뽑아서 더하기
from itertools import permutations


def solution(numbers):
    answer = []
    permute = permutations(numbers, 2)
    for i in permute:
        answer.append(sum(i))
    answer = set(answer)
    return sorted(answer)