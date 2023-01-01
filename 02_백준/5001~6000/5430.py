# 선영이는 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)와 D(버리기)가 있따.
# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
# 함수는 조합해서 한 번에 사용할 수 있다.
# 예를 들어 "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다.
# 예를 들어 "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다.
# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다.
# 다음 줄에는 [x1, ..., xn]과 같은 형태로 배열에 들어있는 수가 주어진다.
# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
# 출력: 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
import sys
from collections import deque

# 테스트 케이스 개수
T = int(sys.stdin.readline())

# 테스트 케이스의 개수만큼 반복
for i in range(T):
    # 함수를 저장할 p
    p = sys.stdin.readline().strip()
    # 배열에 들어 있는 수의 개수 n
    n = int(sys.stdin.readline())
    # 배열에 들어 있는 수
    arr = sys.stdin.readline().strip()[1:-1].split(',')
    deq = deque()
    
    for each in arr:
        if each != '':
            deq.append(each)

    error_flag = 0
    reverse = 0

    for each in p:
        if each == 'R':
            reverse = not reverse
        else:
            if deq and deq[0] != '':
                if not reverse:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error_flag = 1
                break

    if error_flag:
        print('error')
    else:
        if reverse:
            deq.reverse()
        
        print('[', end='')
        
        # deq의 요소 출력
        for j in range(len(deq)):
            if j == len(deq)-1:
                print(str(deq[j]), end='')
            else:
                print(deq[j], end=',')
        print(']')