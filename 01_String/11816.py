# 정수 X가 주어질 때, 정수 X는 항상 8진수, 10진수, 16진수 중 하나이다.
# 8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.
# X를 10진수로 바꿔서 출력하시오.
import sys

case = sys.stdin.readline()

# 8진수인 경우
if case[0] == '0':
    # 16진수인 경우
    if case[1] == 'x':
        print(int(case, 16))
    else:
        print(int(case, 8))

else:
    print(case)