# 화살표 그리기
import sys

n = int(sys.stdin.readline())
dots = [[] for _ in range(n + 1)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots[y].append(x)   # 색깔별로 점의 좌표 추가하기

distance = 0    # 총 거리
for dot in dots:
    if len(dot) > 1:    # 점이 존재하는 경우
        dot.sort()      # 오름차순 정렬

        for i in range(len(dot)):
            if i == 0:  # 맨 첫번째 점일 경우, 자신의 오른쪽 점까지의 거리 더하기
                distance += dot[1] - dot[0]
            elif i == len(dot) - 1:     # 맨 마지막 점일 경우, 자신의 왼쪽 점까지의 거리 더하기
                distance += dot[len(dot) - 1] - dot[len(dot) - 2]
            else:   # 그 외에 경우, 자신의 왼쪽에 있는 점까지의 거리와 자신의 오른쪽에 있는 점까지의 거리 중 더 작은 값 더하기
                distance += min(dot[i] - dot[i - 1], dot[i + 1] - dot[i])
print(dots)
