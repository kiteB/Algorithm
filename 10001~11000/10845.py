# 정수를 저장한느 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯 가지이다.
# 1. push X: 정수 X를 큐에 넣는 연산이다.
# 2. pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 3. size: 큐에 들어있는 정수의 개수를 출력한다.
# 4. empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# 5. front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 6. back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력: 첫째 줄에 주어지는 명령의 수 N이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 출력: 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
import sys

T = int(sys.stdin.readline())
queue = []

for i in range(T):
    case = list(map(str, sys.stdin.readline().split()))

    if case[0] == 'push':
        queue.append(case[1])

    elif case[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print('-1')

    elif case[0] == 'size':
        print(len(queue))

    elif case[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')

    elif case[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print('-1')

    elif case[0] == 'back':
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print('-1')