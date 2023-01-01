# 수가 주어지면, 그 수의 각 자릿수를 내림차순으로 정렬하기
import sys

num = list(map(str, sys.stdin.readline().rstrip()))
num.sort(reverse=True)
print(''.join(num))