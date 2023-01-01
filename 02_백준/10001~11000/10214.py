# Baseball
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    yonsei = 0
    korea = 0

    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        yonsei += y
        korea += k

    if yonsei > korea:
        print('Yonsei')
    elif yonsei < korea:
        print('Korea')
    else:
        print('Draw')
