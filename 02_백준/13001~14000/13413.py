# 오셀로 재배치
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    init = input().strip()
    target = input().strip()

    cnt_b = 0
    cnt_w = 0

    for i in range(n):
        if init[i] != target[i]:
            if init[i] == 'B':
                cnt_b += 1
            else:
                cnt_w += 1

    print(max(cnt_b, cnt_w))
