# Lv.1 | 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    stack = []

    for num in arr:
        # stack에 없는 숫자이거나 연속된 숫자가 아니면 stack에 삽입
        if not stack or num != stack[-1]:
            stack.append(num)

    return stack
