# 걷기
from sys import stdin

x, y, w, s = map(int, stdin.readline().split())

# 1. 평행 이동
cost1 = (x + y) * w

# 2. \, /으로 이동
# x와 y의 합이 짝수일 경우, \와 /만으로 이동할 수 있다.
cost2 = 0
if (x + y) % 2 == 0:
    cost2 = max(x, y) * s
else:
    cost2 = (max(x, y) - 1) * s + w

cost3 = min(x, y) * s + abs(x - y) * w
print(min(cost1, min(cost2, cost3)))
