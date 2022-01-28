# CD
import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    data1 = [int(sys.stdin.readline()) for _ in range(n)]
    data2 = [int(sys.stdin.readline()) for _ in range(n)]

    i, j = 0, 0
    answer = 0
    while True:
        if data1[i] == data2[j]:
            answer += 1
            i += 1
            j += 1
        elif data1[i] < data2[j]:
            i += 1
        else:
            j += 1

        if i > n - 1 or j > m - 1:
            break
    print(answer)