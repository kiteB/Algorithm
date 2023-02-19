# 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
from math import pow


def solution(num_list):
    total = 0
    multiple = 1

    for num in num_list:
        total += num
        multiple *= num

    total = pow(total, 2)
    return int(total > multiple)
