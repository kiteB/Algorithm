# 좋은 단어
import sys

n = int(sys.stdin.readline())
answer = 0

for _ in range(n):
    case = sys.stdin.readline().strip()
    stack = []

    for i in case:
        # stack이 비어있지 않고, stack의 top이 현재 단어와 동일하다면
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        answer += 1

print(answer)