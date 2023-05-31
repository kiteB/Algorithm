# 배열의 길이에 따라 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
def solution(arr, n):
    start = int(len(arr) % 2 == 0)

    for idx in range(start, len(arr), 2):
        arr[idx] += n

    return arr
