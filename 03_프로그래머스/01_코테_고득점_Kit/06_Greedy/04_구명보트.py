# Lv.2 | 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = len(people)    # 필요한 구명보트의 개수
    people.sort()
    i = 0
    j = len(people) - 1

    while i < j:
        # 동일한 보트에 태울 수 있는지 확인
        if people[i] + people[j] <= limit:
            i += 1
            answer -= 1
        j -= 1

    return answer


print(solution([70, 50, 80, 50], 100))