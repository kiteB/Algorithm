# N과 M (10)
import sys
input = sys.stdin.readline


def dfs(depth, start):
    if depth == m:
        print(*result)
        return
    prev = 0
    for i in range(start, n):
        if not visited[i] and prev != numbers[i]:
            visited[i] = True
            result.append(numbers[i])
            prev = numbers[i]
            dfs(depth + 1, i + 1)
            visited[i] = False
            result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n
result = []
dfs(0, 0)
