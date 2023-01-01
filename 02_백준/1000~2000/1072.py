# 게임
import sys

x, y = map(int, sys.stdin.readline().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    low = 1
    high = int(1e9)

    while low <= high:
        mid = (low + high) // 2
        new_x, new_y = x + mid, y + mid

        if int((new_y * 100) / new_x) > z:
            high = mid - 1
        else:
            low = mid + 1
    print(high + 1)
