# N과 M (3)
import sys
input = sys.stdin.readline


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for num in range(1, n + 1):
        result.append(num)
        dfs(depth + 1)
        result.pop()


n, m = map(int, input().split())
result = []
dfs(0)
