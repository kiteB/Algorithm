# 큐 2
import sys
from collections import deque


def is_empty(q):
    if len(q) == 0:
        return True
    return False


input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    command = list(input().split())

    if len(command) > 1:
        operator, x = command

        if operator == 'push':
            queue.append(x)
    else:
        operator = command.pop()
        if operator == 'pop':
            if is_empty(queue):
                print(-1)
            else:
                print(queue.popleft())

        elif operator == 'size':
            print(len(queue))

        elif operator == 'empty':
            if is_empty(queue):
                print(1)
            else:
                print(0)

        elif operator == 'front':
            if is_empty(queue):
                print(-1)
            else:
                print(queue[0])

        elif operator == 'back':
            if is_empty(queue):
                print(-1)
            else:
                print(queue[-1])
