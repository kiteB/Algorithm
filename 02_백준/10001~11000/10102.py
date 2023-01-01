# 개표
import sys

v = int(sys.stdin.readline())
vote = list(sys.stdin.readline().strip())

a = vote.count('A')
b = vote.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
