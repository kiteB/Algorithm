# 창고 다각형
import sys

n = int(sys.stdin.readline())
pillars = [0] * 1001

max_h = 0       # 최대 높이
max_x = 0       # 최대 높이의 기둥 위치
end_idx = 0     # 마지막 인덱스

answer = 0

for _ in range(n):
    l, h = map(int, sys.stdin.readline().split())
    pillars[l] = h

    if max_h < h:
        max_h = h       # 최대 높이 갱신
        max_x = l       # 최대 높이의 기둥 위치 갱신
    end_idx = max(end_idx, l)   # 마지막 인덱스 갱신

stack = []
# 0부터 max_x까지
for i in range(0, max_x + 1):
    if not stack:                   # top 값 없으면 값 넣기
        stack.append(pillars[i])
        answer += stack[-1]
    else:
        if stack[-1] < pillars[i]:  # top 값 보다 현재 기둥의 값이 크다면
            stack.pop()             # top 값 갱신
            stack.append(pillars[i])
        answer += stack[-1]         # top 값 보다 작은 경우 top 값 넣어줌.

stack = []
# 오른쪽 끝부터 max_x까지
for i in range(end_idx, max_x, -1):
    if not stack:
        stack.append(pillars[i])
        answer += stack[-1]
    else:
        if stack[-1] < pillars[i]:
            stack.pop()
            stack.append(pillars[i])
        answer += stack[-1]

print(answer)