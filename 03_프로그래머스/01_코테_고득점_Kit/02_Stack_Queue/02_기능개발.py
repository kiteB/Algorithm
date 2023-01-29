# Lv.2 | 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []

    while progresses:
        feature = 0     # 작업이 완료된 기능 개수

        # 작업이 완료된 기능들 progresses, speeds 에서 제거
        # 맨 앞에 있는 기능이 배포될 때 함께 배포되므로, progresses[0]이 100 이상일 때만 수행
        while progresses and progresses[0] >= 100:
            feature += 1
            progresses.pop(0)
            speeds.pop(0)

        # 진도율 증가
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 작업이 완료된 기능이 있을 경우
        if feature:
            answer.append(feature)

    return answer