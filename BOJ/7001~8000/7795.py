# 먹을 것인가 먹힐 것인가
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    i, j = 0, 0
    cnt = 0
    while i < n and j < m:
        if a[i] > b[j]:
            cnt += m - j
            i += 1
        else:
            j += 1

    print(cnt)
