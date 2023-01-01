# 대표 자연수
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

# 자연수 개수가 홀수일 경우
if n % 2 != 0:
    print(numbers[n // 2])
else:
    print(numbers[(n // 2) - 1])