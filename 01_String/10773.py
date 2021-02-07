# 잘못된 수를 입력할 때마다 0을 추가로 입력하여, 가장 최근 값을 지운 다음 모든 수의 합을 구하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())
numbers = []

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))
