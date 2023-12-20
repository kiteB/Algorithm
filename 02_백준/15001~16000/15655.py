# N과 M (6)
import sys
input = sys.stdin.readline


def dfs(depth, start):
    if depth == m:
        print(*result)
        return
    for idx in range(start, n):
        if numbers[idx] not in result:
            result.append(numbers[idx])
            dfs(depth + 1, idx + 1)
            result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
dfs(0, 0)