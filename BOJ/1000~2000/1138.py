# 한 줄로 서기
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n):
    answer.insert(data[n - 1 - i], n - i)

for i in answer:
    print(i, end=' ')