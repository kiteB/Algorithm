# 키로거
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    left = []
    right = []
    password = sys.stdin.readline().strip()

    for p in password:
        if p == '<':
            if left:
                right.append(left.pop())
        elif p == '>':
            if right:
                left.append(right.pop())
        elif p == '-':
            if left:
                left.pop()
        else:
            left.append(p)
        print(left, right)

    left.extend(reversed(right))
    print(''.join(left))