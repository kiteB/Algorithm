# Lv.2 | H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True)  # 내림차순으로 정렬
    answer = 0  # H-Index 초기값

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer += 1
        else:
            break

    return answer
