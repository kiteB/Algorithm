# Sort 마스터 배지훈의 후계자
import sys

n, m = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
b = sorted(a)

for _ in range(m):
    d = int(sys.stdin.readline())

    answer = -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2

        if b[mid] == d:
            answer = mid
            high = mid - 1
        elif b[mid] < d:
            low = mid + 1
        else:
            high = mid - 1

    print(answer)