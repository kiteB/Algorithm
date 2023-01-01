# 약수들의 합
import sys

while True:
    n = int(sys.stdin.readline())
    divisor = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if sum(divisor) == n:
        answer = (str(n) + ' = ')
        answer += ' + '.join(map(str, divisor))
        print(answer)
    else:
        print(f'{n} is NOT perfect.')