# 집합
import sys

m = int(sys.stdin.readline())
s = []

for _ in range(m):
    case = list(sys.stdin.readline().split())

    if len(case) > 1:
        op, x = case[0], int(case[1])

        if op == 'add':
            if x not in s:
                s.append(x)
        elif op == 'remove':
            if x in s:
                s.remove(x)
        elif op == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.append(x)
    else:
        op = case[0]

        if op == 'all':
            s = list(range(1, 21))
        elif op == 'empty':
            s = []