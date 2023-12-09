# 비밀번호 발음하기
import sys


def is_acceptable(password):
    vowel_flag = False
    repeat = [0, 0]

    for idx, p in enumerate(password):
        if p in 'aeiou':
            vowel_flag = True
            repeat[0] += 1
            repeat[1] = 0

            if repeat[0] >= 3 or (repeat[0] >= 2 and password[idx-1] == p and p not in 'eo'):
                return False

        else:
            repeat[1] += 1
            repeat[0] = 0

            if repeat[1] >= 3 or (repeat[1] >= 2 and password[idx-1] == p):
                return False

    return vowel_flag


while True:
    password = sys.stdin.readline().strip()

    if password == "end":
        break

    if is_acceptable(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
