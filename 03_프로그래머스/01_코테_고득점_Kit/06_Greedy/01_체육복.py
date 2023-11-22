# Lv.1 | 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 여분의 체육복을 가진 학생들이 도난당한 학생들에게 체육복을 빌려줌
    for num in reserve_set:
        if num - 1 in lost_set:
            lost_set.remove(num - 1)
        elif num + 1 in lost_set:
            lost_set.remove(num + 1)

    return n - len(lost_set)
