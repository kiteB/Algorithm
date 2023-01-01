# 접두사 찾기
import sys

n, m = map(int, sys.stdin.readline().split())
s = [sys.stdin.readline().strip() for _ in range(n)]
s.sort()

answer = 0
for _ in range(m):
    case = sys.stdin.readline().strip()

    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        temp = s[mid][:len(case)]

        if case < temp:
            high = mid - 1
        elif case > temp:
            low = mid + 1
        else:
            answer += 1
            break

print(answer)