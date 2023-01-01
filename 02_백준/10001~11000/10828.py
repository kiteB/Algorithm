# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.
# 1. push X: 정수 X를 스택에 넣는 연산이다.
# 2. pop: 스택에서 가장 위에 있는 정수를 뻬고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다,
# 3. size: 스택에 들어있는 정수의 개수를 출력한다.
# 4. empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5. top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력: 첫째 줄에 주어지는 명령의 수 N이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 출력: 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    case = list(map(str, sys.stdin.readline().strip().split()))

    if case[0] == 'push':
        stack.append(case[1])

    elif case[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print('-1')

    elif case[0] == 'size':
        print(len(stack))

    elif case[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')

    elif case[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print('-1')