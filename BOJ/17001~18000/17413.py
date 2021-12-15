# 단어 뒤집기 2
import sys

s = list(sys.stdin.readline().rstrip())
answer = ''
reverse = True
tmp = ''

for i in s:
    if i == '<':    # 열린 괄호를 만나면
        if reverse:
            answer += tmp[::-1]
            tmp = ''
        reverse = False
        answer += i
    elif i == '>':  # 닫힌 괄호를 만나면
        reverse = True
        answer += i
    elif i == ' ':  # 공백을 만나면
        if reverse:
            answer += tmp[::-1]
            tmp = ''
        answer += i
    else:
        if reverse:
            tmp += i
        else:
            answer += i

if len(tmp) > 1:
    if reverse:
        answer += tmp[::-1]
    else:
        answer += tmp
print(answer)