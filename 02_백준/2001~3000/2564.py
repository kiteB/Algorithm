# 경비원
import sys


def clockwise(direction, x):   # 시계방향 거리 계산
    if direction == 1:      # 북쪽
        return x
    elif direction == 2:    # 남쪽
        return w + h + (w - x)
    elif direction == 3:    # 서쪽
        return w + h + w + (h - x)
    else:                   # 동쪽
        return w + x


w, h = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())     # 상점 개수
store = []

for _ in range(cnt):
    store.append(list(map(int, sys.stdin.readline().split())))  # 상점 위치 정보 저장

a, b = map(int, sys.stdin.readline().split())
guard = clockwise(a, b)     # 경비원의 위치

answer = 0
total = (w + h) * 2     # 둘레 길이

distance = []
for d, x in store:
    tmp = clockwise(d, x)   # 0부터 시계 방향으로 따졌을 때의 거리 계산
    dist = abs(guard - tmp)     # 경비원과의 차이 계산
    distance.append(min(dist, total - dist))    # dist(시계 방향)와 total-dist (반시계 방향) 중 더 작은 값 저장

print(sum(distance))