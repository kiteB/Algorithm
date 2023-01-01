# 후위 표기식2
import sys

input = sys.stdin.readline
n = int(input())
expression = input().strip()
numbers = [int(input()) for _ in range(n)]
stack = []

for i in expression:
    if i.isalpha():
        stack.append(numbers[ord(i) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        else:
            stack.append(num1 / num2)

print(f'{stack[0]:.2f}')