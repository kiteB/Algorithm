# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
import sys


def fibonacci(num):
    fibo = [0, 1]

    for i in range(2, num+1):
        fibo.append(fibo[i-2] + fibo[i-1])

    return fibo[num]


n = int(sys.stdin.readline())
print(fibonacci(n))