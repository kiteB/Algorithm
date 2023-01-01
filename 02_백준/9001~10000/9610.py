# 사분면
import sys

n = int(sys.stdin.readline())
quadrants = [0] * 5
axis = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x > 0 and y > 0:
        quadrants[1] += 1
    elif x < 0 and y > 0:
        quadrants[2] += 1
    elif x < 0 and y < 0:
        quadrants[3] += 1
    elif x > 0 and y < 0:
        quadrants[4] += 1
    else:
        axis += 1

for i in range(1, 5):
    print(f'Q{i}: {quadrants[i]}')
print(f'AXIS: {axis}')
