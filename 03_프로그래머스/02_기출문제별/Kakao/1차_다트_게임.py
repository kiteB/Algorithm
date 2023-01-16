# [1차] 다트게임
def solution(dartResult):
    n = ''
    score = {'S': 1, 'D': 2, 'T': 3}
    answer = []

    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i in ['S', 'D', 'T']:
            n = pow(int(n), score[i])
            answer.append(n)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1

    return sum(answer)