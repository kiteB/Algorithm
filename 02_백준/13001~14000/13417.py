# 카드 문자열
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    cards = list(sys.stdin.readline().split())
    queue = deque()

    for i in cards:
        if not queue:
            queue.append(i)
        else:
            if i <= queue[0]:
                queue.appendleft(i)
            else:
                queue.append(i)
    print(''.join(queue))
