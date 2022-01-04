# 주식
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))

    max_val = price[-1]
    answer = 0

    for i in range(n - 2, -1, -1):  # 뒤에서부터 접근해야 시간 초과가 발생하지 않는다.
        if price[i] < max_val:  # max_val 보다 작으면 (max_val - 현재값)
            answer += (max_val - price[i])
        else:   # 그렇지 않으면 max_val 값 갱신
            max_val = price[i]

    print(answer)