# Lv.1 | K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for each in commands:
        i, j, k = each
        numbers = sorted(array[i - 1:j])
        answer.append(numbers[k - 1])

    return answer
