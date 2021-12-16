# 괄호의 값
import sys

case = list(sys.stdin.readline().strip())
stack = []

for i in case:

    # 오른쪽 소괄호인 경우
    if i == ')':
        numbers = 0

        while stack:
            top = stack.pop()
            if top == '(':
                if numbers == 0:
                    stack.append(2)
                else:
                    stack.append(2 * numbers)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                numbers += int(top)

    # 오른쪽 대괄호인 경우
    elif i == ']':
        numbers = 0

        while stack:
            top = stack.pop()
            if top == '[':
                if numbers == 0:
                    stack.append(3)
                else:
                    stack.append(3 * numbers)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                numbers += int(top)
    else:
        stack.append(i)

answer = 0
for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        answer += i
print(answer)