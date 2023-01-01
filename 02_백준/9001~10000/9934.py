# 완전 이진 트리
import sys


def solve(tree, depth):
    if len(tree) == 1:
        answer[depth].extend(tree)
        return

    mid = len(tree) // 2
    answer[depth].append(tree[mid])     # 부모 노드 저장
    solve(tree[:mid], depth + 1)        # 왼쪽 트리 탐색
    solve(tree[mid + 1:], depth + 1)    # 오른쪽 트리 탐색


k = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))

n = len(nodes)
answer = [[] for _ in range(k)]

solve(nodes, 0)

for a in answer:
    print(*a)