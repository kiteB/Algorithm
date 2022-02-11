# RGB거리
import sys

n = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):   # i번째 집을 각각 R(0), G(1), B(2)로 칠했을 때의 최솟값 구하기
    costs[i][0] = costs[i][0] + min(costs[i - 1][1], costs[i - 1][2])
    costs[i][1] = costs[i][1] + min(costs[i - 1][0], costs[i - 1][2])
    costs[i][2] = costs[i][2] + min(costs[i - 1][0], costs[i - 1][1])

print(min(costs[n - 1]))