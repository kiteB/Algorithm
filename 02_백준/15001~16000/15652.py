# N과 M (4)
import sys
input = sys.stdin.readline


def dfs(depth, start):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        result.append(i)
        dfs(depth + 1, i)
        result.pop()


n, m = map(int, input().split())
result = []
dfs(0, 1)
