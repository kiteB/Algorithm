# 피보나치
import sys

t = int(sys.stdin.readline())
fibonacci = [0, 1]

for i in range(2, 46):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

for _ in range(t):
    num = int(sys.stdin.readline())
    answer = []

    for i in range(45, 0, -1):
        if fibonacci[i] <= num:
            answer.append(fibonacci[i])
            num -= fibonacci[i]

        if num == 0:    # num이 0이 되면 answer의 모든 요소들을 출력한다.
            answer.sort()
            print(*answer)
            break