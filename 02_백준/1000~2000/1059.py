# 좋은 구간
import sys

l = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
n = int(sys.stdin.readline())
a, b = 1, max(numbers)

if n in numbers:
    print(0)
else:
    for num in numbers:
        if n > num:     # a 값 찾기
            a = num + 1
        else:   # b 값 찾기
            b = num - 1
            break

    print((b - a) + (b - n) * (n - a))