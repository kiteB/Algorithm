import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    commands = list(map(int, input().split()))

    if commands[0] == 1:
        stack.append(commands[1])
    elif commands[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == 3:
        print(len(stack))
    elif commands[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif commands[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
