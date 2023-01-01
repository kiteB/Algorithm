# 회문
import sys


def is_pseudo(s, start, end):   # 유사회문 판단
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def palindrome(s, start, end):  # 팰린드롬 판단
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            check1 = is_pseudo(s, start + 1, end)
            check2 = is_pseudo(s, start, end - 1)

            if check1 or check2:
                return 1
            else:
                return 2
    return 0


T = int(sys.stdin.readline())

for _ in range(T):
    case = list(sys.stdin.readline().strip())
    answer = palindrome(case, 0, len(case) - 1)
    print(answer)