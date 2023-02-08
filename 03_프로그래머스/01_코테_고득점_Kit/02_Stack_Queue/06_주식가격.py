# Lv.2 | 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i, price in enumerate(prices):
        target = stack[-1]

        # 주식 가격이 떨어졌다면 주식이 떨어진 기간 계산
        while stack and price < prices[target]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i) # 가격이 떨어진 시점은 stack에서 제거

    # 스택에 남아 있는 인덱스: 끝까지 가격이 떨어지지 않음
    while stack:
        j = stack.pop()
        answer[j] = (len(prices) - 1) - j

    return answer
