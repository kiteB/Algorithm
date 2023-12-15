# N과 M (1)
import sys
input = sys.stdin.readline


def perm(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for num in range(1, n + 1):
        if num not in result:
            result.append(num)
            perm(depth + 1)
            result.pop()


n, m = map(int, input().split())
result = []
perm(0)
