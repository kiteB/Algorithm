# Lv.2 | 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque((i, j) for i, j in enumerate(priorities))     # (순서, 우선순위)

    while queue:
        front = queue.popleft()

        # queue 내의 가장 앞에 있는 프로세스보다 우선순위가 높은 프로세스가 있다면 뒤로 보내기
        if any(front[1] < process[1] for process in queue):
            queue.append(front)
        else:
            # 없다면 프로세스 실행
            answer += 1

            # 현재 프로세스가 location 위치에 있는 프로세스였다면 실행 순서 리턴
            if front[0] == location:
                return answer
