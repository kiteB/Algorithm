# 이진수 - 브론즈 3
T = int(input())

for _ in range(T):
    n = bin(int(input()))

    for idx, val in enumerate(n[-1:1:-1]):
        if val == '1':
            print(idx, end=' ')
