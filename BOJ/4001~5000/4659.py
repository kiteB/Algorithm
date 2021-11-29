# 비밀번호 발음하기
import sys

while True:
    password = sys.stdin.readline().strip()

    if password == 'end':  # 'end' 입력 시 종료
        break

    vowel_flag = False  # 모음이 한 번 이상 등장했는지 판별하는 변수
    flag = False        # 조건에 어긋나는 상황이 발생했는지를 판별하는 변수
    repeat = [0, 0]     # 모음, 자음 반복 횟수

    for idx, p in enumerate(password):
        if p in 'aeiou':    # 모음일 경우
            vowel_flag = True
            repeat[0] += 1
            repeat[1] = 0   # 자음 반복 횟수 초기화

            if repeat[0] >= 3:  # 모음이 3개 이상 연속되면
                flag = True
                break

            if repeat[0] >= 2 and password[idx - 1] == p:  # 같은 글자가 2개 이상 연속되면 안된다.
                if p not in 'eo':   # 특수 케이스인 'ee', 'oo' 가 아닌 경우
                    flag = True
                    break

        else:   # 자음일 경우
            repeat[1] += 1
            repeat[0] = 0   # 모음 반복 횟수 초기화

            if repeat[1] >= 3:  # 자음이 3개 이상 연속되면
                flag = True
                break

            if repeat[1] >= 2 and password[idx-1] == p: # 같은 글자가 2개 이상 연속되면 안된다.
                flag = True
                break

    if not flag and vowel_flag:     # 조건에 벗어나는 경우가 없고, 모음이 1번 이상 등장했으면 acceptable
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
