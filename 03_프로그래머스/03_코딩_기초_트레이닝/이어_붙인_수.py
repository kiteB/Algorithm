# 이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
def solution(num_list):
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 == 1:
            odd += str(num)
        else:
            even += str(num)

    return int(odd) + int(even)
