# 괄호 끼워넣기
import sys

case = sys.stdin.readline().strip()
stack = []

for i in case:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

if len(stack) > 0:
    print(len(stack))