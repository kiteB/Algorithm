# 실패율


def solution(N, stages):
    rates = {}
    num = len(stages)

    for i in range(1, N + 1):
        if num != 0:
            cnt = stages.count(i)
            rates[i] = cnt / num
            num -= cnt
        else:
            rates[i] = 0
    return sorted(rates, key=lambda x: -rates[x])