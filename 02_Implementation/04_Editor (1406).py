# 한 줄로 된 간단한 에디터를 구현해보자
# 첫째 줄에 초기에 편집기에 입력되어 있는 문자열이 주어짐.
# 둘째 줄에는 명령어의 개수를 나타내는 정수 M이 주어짐.
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력하라.
from collections import deque
import sys

deq_1 = deque(sys.stdin.readline().strip())
deq_2 = deque()
N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()

    # L 입력 -> 커서를 왼쪽으로 한 칸 옮김
    if command[0] == 'L':
        if len(deq_1) != 0:
            deq_2.appendleft(deq_1.pop())

    # D 입력 -> 커서를 오른쪽으로 한 칸 옮김
    elif command[0] == 'D':
        if len(deq_2) != 0:
            deq_1.append(deq_2.popleft())

    # B 입력 -> 커서 왼쪽에 있는 문자를 삭제
    elif command[0] == 'B':
        if len(deq_1) != 0:
            deq_1.pop()

    # P $ 입력 -> $라는 문자를 커서 왼쪽에 추가하기
    elif command[0] == 'P':
        deq_1.append(command[1])

for i in deq_2:
    deq_1.append(i)
print(''.join(deq_1))