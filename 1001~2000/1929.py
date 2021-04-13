# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력: 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
import sys

M, N = map(int, sys.stdin.readline().split())
prime_numbers = [False, False] + [True] * (N-1)

for i in range(2, N+1):
    if prime_numbers[i]:
        for j in range(i+i, N+1, i):
            prime_numbers[j] = False

for i in range(M, N+1):
    if prime_numbers[i]:
        print(i)