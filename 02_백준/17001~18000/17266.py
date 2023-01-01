# 어두운 굴다리
import sys


def is_available(data, target):
    if data[0] > target:
        return False

    if (n - data[-1]) > target:
        return False

    for i in range(1, m):
        if ((data[i] - data[i - 1]) / 2) > target:
            return False
    return True


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lights = list(map(int, sys.stdin.readline().split()))

if m == 1:
    print(max(lights[0], n - lights[0]))
else:
    low = 1
    high = n
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if is_available(lights, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)