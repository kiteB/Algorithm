# N과 M (8)
import sys
input = sys.stdin.readline


def dfs(depth, start):
    if depth == m:
        print(*result)
        return
    for i in range(start, n):
        result.append(numbers[i])
        dfs(depth + 1, i)
        result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
dfs(0, 0)
