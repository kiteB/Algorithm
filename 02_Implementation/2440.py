# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
import sys

N = int(sys.stdin.readline())

for i in range(N):
    print('*' * (N-i))
