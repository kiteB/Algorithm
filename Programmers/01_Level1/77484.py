# 로또의 최고 순위와 최저 순위


def solution(lottos, win_nums):
    # key : 맞은 문제 개수, value : 순위
    ranking = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    max_cnt = 0
    min_cnt = 0
    answer = []

    for num in lottos:
        if num in win_nums:
            min_cnt += 1
        if num == 0:
            max_cnt += 1
    max_cnt += min_cnt

    answer.append(ranking[max_cnt])
    answer.append(ranking[min_cnt])
    return answer