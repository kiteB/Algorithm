# Lv.2 | 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    # 모든 순열을 고려함
    for p in permutations(dungeons, len(dungeons)):
        tmp = k     # 각 순열에 대해 시뮬레이션을 수행해야 하므로 임시 변수에 현재 피로도를 저장함
        cnt = 0     # 탐험한 던전 수 저장

        for min_required, cost in p:
            if tmp >= min_required:
                tmp -= cost
                cnt += 1

        answer = max(answer, cnt)

    return answer
