# 괄호 문자열은 두 개의 괄호 기호인 '('와 ')'만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열 (VPS)라고 부른다.
# 입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로 나타내라.
import sys

T = int(sys.stdin.readline())

for i in range(T):
    case = sys.stdin.readline().strip()
    stack = []
    check = True

    for j in case:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                print('NO')
                check = False
                break
            else:
                stack.pop()

    if check and len(stack) == 0:
        print('YES')
    elif check and len(stack) != 0:
        print('NO')