# Lv.2 | 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    total = brown + yellow

    # 가로 * 세로 = total이 되는 조합 찾기
    for i in range(1, int(total ** 0.5) + 1):
        if total % i == 0:
            j = total // i
            if (i - 2) * (j - 2) == yellow:
                return [j, i]
