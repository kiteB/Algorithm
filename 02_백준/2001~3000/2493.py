# 탑
import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
answer = [0] * n
stack = []  # 탑의 높이와 인덱스를 저장할 스택

for i in range(n - 1, -1, -1):  # 왼쪽 방향으로 탐색
    while stack and height[i] > stack[-1][0]:
        idx = stack.pop()[1]
        answer[idx] = i + 1
    stack.append((height[i], i))    # 현재 탑을 스택에 추가

print(*answer)
