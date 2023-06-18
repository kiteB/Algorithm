# n개 간격의 원소들
# https://school.programmers.co.kr/learn/courses/30/lessons/181888
def solution(num_list, n):
    return [num_list[idx] for idx in range(0, len(num_list), n)]
