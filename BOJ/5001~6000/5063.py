# TGN
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().split())
    profit = e - c

    if profit > r:
        print('advertise')
    elif profit == r:
        print('does not matter')
    else:
        print('do not advertise')
