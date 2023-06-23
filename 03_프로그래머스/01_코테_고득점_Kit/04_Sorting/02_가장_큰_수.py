# Lv.2 | 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    str_list = list(map(str, numbers))
    sorted_list = sorted(str_list, key=lambda x: x * 3, reverse=True)
    return str(int(''.join(sorted_list)))
