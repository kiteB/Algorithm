# 괄호의 값
# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열은 다음과 같다.
# 1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
# 2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
# 3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
#
# 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
# 1. ‘()’ 인 괄호열의 값은 2이다.
# 2. ‘[]’ 인 괄호열의 값은 3이다.
# 3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# 4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# 여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.
# 입력: 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
# 출력: 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
import sys

case = list(sys.stdin.readline().strip())
stack = []

for i in case:

    # 오른쪽 소괄호인 경우
    if i == ')':
        numbers = 0

        while stack:
            top = stack.pop()
            if top == '(':
                if numbers == 0:
                    stack.append(2)
                else:
                    stack.append(2 * numbers)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                numbers += int(top)

    # 오른쪽 대괄호인 경우
    elif i == ']':
        numbers = 0

        while stack:
            top = stack.pop()
            if top == '[':
                if numbers == 0:
                    stack.append(3)
                else:
                    stack.append(3 * numbers)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                numbers += int(top)
    else:
        stack.append(i)

answer = 0
for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        answer += i
print(answer)


