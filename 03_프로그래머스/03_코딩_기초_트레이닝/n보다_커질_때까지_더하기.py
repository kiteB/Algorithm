# n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884
def solution(numbers, n):
    answer = 0
    idx = 0

    while answer <= n:
        answer += numbers[idx]
        idx += 1

    return answer
