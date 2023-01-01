# 중복 빼고 정렬하기
import sys

n = int(sys.stdin.readline())
numbers = sorted(set(map(int, sys.stdin.readline().split())))
for i in numbers:
    print(i, end=' ')