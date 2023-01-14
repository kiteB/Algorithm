# 빗물
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0  # 빗물이 고인 양
for i in range(1, w - 1):   # 맨 왼쪽과 오른쪽은 고일 수 없다.
    left_max = max(heights[:i])
    right_max = max(heights[i + 1:])

    min_val = min(left_max, right_max)  # 그 중 가장 낮은 블록

    if heights[i] < min_val:
        answer += min_val - heights[i]

print(answer)