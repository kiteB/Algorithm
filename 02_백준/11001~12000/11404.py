# 플로이드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e9
bus = [[INF] * n for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())

    if bus[a - 1][b - 1] > c:
        bus[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if bus[i][k] + bus[k][j] < bus[i][j]:
                    bus[i][j] = bus[i][k] + bus[k][j]

for i in range(n):
    for j in range(n):
        if bus[i][j] == INF:
            print(0, end=' ')
        else:
            print(bus[i][j], end=' ')
    print()
