# Lv.1 | 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import defaultdict


def solution(participant, completion):
    participant_counts = defaultdict(int)

    # 참가자 이름을 key 값으로 하여 등장 횟수 저장
    for p in participant:
        participant_counts[p] += 1

    # 완주하였다면 value 값 하나씩 감소
    for c in completion:
        participant_counts[c] -= 1
        if participant_counts[c] == 0:  # 참가자가 모두 완주하였다면 dict에서 삭제
            del participant_counts[c]

    # 딕셔너리의 키 중에서 첫 번재 키 값 반환하기
    return next(iter(participant_counts.keys()))
