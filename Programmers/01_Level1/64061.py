# 크레인 인형뽑기


def solution(board, moves):
    answer = 0
    n = len(board)
    stack_list = [[] * i for i in range(n+1)]
    basket = []

    for i in range(n):
        for j in range(n):
            if board[n-j-1][i] != 0:
                stack_list[i+1].append(board[n-j-1][i])

    for move in moves:
        if len(stack_list[move]):
            if len(basket) and basket[-1] == stack_list[move][-1]:
                answer += 2
                basket.pop()
                stack_list[move].pop()
            else:
                basket.append(stack_list[move].pop())

    return answer