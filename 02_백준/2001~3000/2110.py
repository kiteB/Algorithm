# 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]   # 집 좌표 저장
house.sort()

start = 1                   # 거리는 최소 1 이상
end = house[-1] - house[0]  # (공유기의 최대 거리) = (집 좌표 최댓값) - (집 좌표 최솟값)
answer = 0      # 공유기 사이의 최대 거리

while start <= end:
    mid = (start + end) // 2    # mid는 가장 인접한 공유기 사이의 최대 거리
    tmp = house[0]
    cnt = 1     # 공유기 설치 개수

    for i in range(1, n):
        # 공유기 설치
        if house[i] >= tmp + mid:
            cnt += 1
            tmp = house[i]

    if cnt >= c:        # C개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid + 1
        answer = mid    # 최적의 결과를 저장해두기
    else:
        end = mid - 1

print(answer)