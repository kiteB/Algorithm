# 이장님 초대
import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)
answer = []

for i in range(1, n + 1):
    answer.append(i + trees[i - 1])

print(max(answer) + 1)