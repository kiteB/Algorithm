# 화성 수학
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    expression = list(sys.stdin.readline().split())
    num = float(expression[0])
    operator = expression[1:]

    for op in operator:
        if op == '@':
            num *= 3
        elif op == '%':
            num += 5
        elif op == '#':
            num -= 7
    print(f'{num:.2f}')
