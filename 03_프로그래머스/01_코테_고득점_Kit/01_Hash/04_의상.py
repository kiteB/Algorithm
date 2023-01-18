# Lv.2 | 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict


def solution(clothes):
    clothes_dict = defaultdict(int)
    for name, kind in clothes:
        clothes_dict[kind] += 1

    answer = 1
    for key, val in clothes_dict.items():
        answer *= (val + 1)
    return answer - 1