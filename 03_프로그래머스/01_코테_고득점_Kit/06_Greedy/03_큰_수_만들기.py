# Lv.2 | 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    stack = []

    for num in number:
        # stack이 비어있지 않고, 현재 숫자가 스택의 top보다 크고, 아직 제거해야 할 숫자가 남아있다면
        while stack and stack[-1] < num and k > 0:
            stack.pop()     # 숫자 제거
            k -= 1

        stack.append(num)

    # 아직 제거해야 할 숫자가 남아있다면 뒤에서부터 남은 k개 제거
    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)
