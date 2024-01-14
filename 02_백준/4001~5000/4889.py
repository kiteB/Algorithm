# 안정적인 문자열
import sys

idx = 1
while True:
    case = sys.stdin.readline().strip()

    if '-' in case:
        break

    stack = []
    cnt = 0

    for s in case:
        if s == '}':
            if not stack:
                cnt += 1
                stack.append(s)
            else:
                stack.pop()
        else:
            stack.append(s)

    cnt += len(stack) // 2

    print(f'{idx}. {cnt}')
    idx += 1
