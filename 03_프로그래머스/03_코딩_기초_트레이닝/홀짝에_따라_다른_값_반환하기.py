# 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
def solution(n):
    if n % 2 == 0:
        answer = 0
        for i in range(2, n + 1, 2):
            answer += i * i
        return answer
    else:
        return sum(list(range(1, n + 1, 2)))
    