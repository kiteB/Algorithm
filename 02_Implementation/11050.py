# 자연수 N과 정수 K가 주어졌을 때, 이항 계수를 구하는 프로그램을 작성하시오.
import sys
from math import factorial

N, K = map(int, sys.stdin.readline().split())
print(factorial(N) // (factorial(K) * factorial(N-K)))