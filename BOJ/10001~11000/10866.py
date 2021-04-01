# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# 1. push_front X: 정수 X를 덱의 앞에 넣는다.
# 2. push_back X: 정수 X를 덱의 뒤에 넣는다.
# 3. pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 4. pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 5. size: 덱에 들어있는 정수의 개수를 출력한다.
# 6. empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# 7. front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 8. back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력: 첫째 줄에 주어지는 명령의 수 N이 주어진다. 들째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 출력: 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    case = list(map(str, sys.stdin.readline().split()))

    if case[0] == 'push_front':
        deq.appendleft(case[1])

    elif case[0] == 'push_back':
        deq.append(case[1])

    elif case[0] == 'pop_front':
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)

    elif case[0] == 'pop_back':
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)

    elif case[0] == 'size':
        print(len(deq))

    elif case[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif case[0] == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)

    elif case[0] == 'back':
        if len(deq) != 0:
            print(deq[len(deq)-1])
        else:
            print(-1)