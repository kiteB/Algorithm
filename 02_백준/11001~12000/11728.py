# 배열 합치기
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
numbers = a + b
numbers.sort()
print(*numbers)