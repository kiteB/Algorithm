# AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

# 테스트 케이스의 개수만큼 반복
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(',')
    queue = deque()
    
    for each in arr:
        if each != '':
            queue.append(each)

    error_flag = 0
    reverse = 0

    for each in p:
        if each == 'R':
            reverse = not reverse
        else:
            if queue and queue[0] != '':
                if not reverse:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                error_flag = 1
                break

    if error_flag:
        print('error')
    else:
        if reverse:
            queue.reverse()
        
        print('[', end='')
        for j in range(len(queue)):
            if j == len(queue) - 1:
                print(str(queue[j]), end='')
            else:
                print(queue[j], end=',')
        print(']')
