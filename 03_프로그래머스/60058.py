# 올바른 문자열인지 판단해주는 함수
def is_correct(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not len(stack):
                return False
            else:
                stack.pop()
    return True


# 균형잡힌 문자열인지 판단해주는 함수
def is_balanced(s):
    tmp = 0
    for i in s:
        if i == '(':
            tmp += 1
        else:
            tmp -= 1

    if tmp == 0:
        return True
    else:
        return False


def solution(p):
    u = ''
    v = ''

    # 1. 입력이 빈 문자열인 경우
    if p == '':
        return p

    # 2. 문자열 w를 u, v로 분리
    for i in range(2, len(p)+1, 2):
        if is_balanced(p[:i]):
            u, v = p[:i], p[i:]
            break

    # 3. u가 올바른 괄호 문자열이라면
    if is_correct(u):
        return u + solution(v)

    else:       # 4. 아니라면
        tmp = '(' + solution(v) + ')'

        # 4-4. u의 첫 번째, 마지막 문자를 제거하고, 나머지 괄호를 뒤집어서 붙이기
        for i in u[1:-1]:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp