# N과 M (2)
import sys
input = sys.stdin.readline


def comb(depth, start):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for num in range(start, n + 1):
        if num not in result:
            result.append(num)
            comb(depth + 1, num + 1)
            result.pop()


n, m = map(int, input().split())
result = []
comb(0, 1)
