import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deque = deque()

for _ in range(n):
    commands = list(map(int, input().split()))

    if commands[0] == 1:
        deque.appendleft(commands[1])
    elif commands[0] == 2:
        deque.append(commands[1])
    elif commands[0] == 3:
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif commands[0] == 4:
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif commands[0] == 5:
        print(len(deque))
    elif commands[0] == 6:
        if not deque:
            print(1)
        else:
            print(0)
    elif commands[0] == 7:
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif commands[0] == 8:
        if deque:
            print(deque[-1])
        else:
            print(-1)
