# N과 M (11)
import sys
input = sys.stdin.readline


def dfs(depth):
    if depth == m:
        print(*result)
        return
    prev = 0
    for i in range(n):
        if prev != numbers[i]:
            result.append(numbers[i])
            prev = numbers[i]
            dfs(depth + 1)
            result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n
result = []
dfs(0)
