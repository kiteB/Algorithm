# N과 M (5)
import sys
input = sys.stdin.readline


def dfs(depth):
    if depth == m:
        print(*result)
        return
    for num in numbers:
        if num not in result:
            result.append(num)
            dfs(depth + 1)
            result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
dfs(0)
