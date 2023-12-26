# N과 M (12)
import sys
input = sys.stdin.readline


def dfs(depth, start):
    if depth == m:
        print(*result)
        return
    prev = 0
    for i in range(start, n):
        if prev != numbers[i]:
            result.append(numbers[i])
            prev = numbers[i]
            dfs(depth + 1, i)
            result.pop()


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
dfs(0, 0)