# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
numbers = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    numbers[num] = numbers[num] + 1     # 숫자 등장 횟수 저장

for i in range(10001):
    if numbers[i]:
        for _ in range(numbers[i]):
            print(i)