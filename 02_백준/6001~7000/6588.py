# 골드바흐의 추측
import sys

MAX_NUM = 1000000 + 1
number = [True] * MAX_NUM
for i in range(2, int(MAX_NUM ** 0.5) + 1):
    if number[i]:
        for j in range(i * i, MAX_NUM, i):
            number[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if number[i] and number[n - i]:
            print(f"{n} = {n - i} + {i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")