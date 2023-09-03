# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    case = input().rstrip()

    if case[0] == '.':
        break

    stack = []
    check = True

    for i in case:
        # 왼쪽 괄호일 경우
        if i in '([':
            stack.append(i)
        # 오른쪽 괄호일 경우
        elif i in ')]':
            if not stack or (i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '['):
                print("no")
                check = False
                break
            stack.pop()

    if check and not stack:
        print("yes")
    elif check and stack:
        print("no")
