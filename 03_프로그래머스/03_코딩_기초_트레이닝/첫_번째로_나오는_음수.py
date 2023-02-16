# 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896
def solution(num_list):
    for idx, num in enumerate(num_list):
        if num < 0:
            return idx
    return -1