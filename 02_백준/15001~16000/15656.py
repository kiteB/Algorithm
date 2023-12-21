# N과 M (7)
import sys
input = sys.stdin.readline


def dfs(depth):
    if depth == m:
        print(*result)
        return
    for i in range(len(numbers)):
        result.append(numbers[i])
        dfs(depth + 1)
        result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
dfs(0)