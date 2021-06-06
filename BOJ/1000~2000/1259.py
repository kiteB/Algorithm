# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
import sys

while True:
    case = sys.stdin.readline().strip()

    if case == '0':
        break

    if case[::-1] == case:
        print('yes')
    else:
        print('no')
