# 기타 레슨
import sys

n, m = map(int, sys.stdin.readline().split())
lessons = list(map(int, sys.stdin.readline().split()))

# 한 블루레이의 크기의 범위를 정함.
start = max(lessons)        # 레슨 영상 길이 중 가장 긴 것보다는 크거나 같아야 한다.
end = sum(lessons)          # 총 레슨 영상 길이보다는 작거나 같아야 한다.

while start <= end:
    mid = (start + end) // 2
    total = 0       # 한 블루레이의 들어가 있는 레슨 영상의 총 길이
    cnt = 1         # 블루레이 개수

    for i in lessons:
        # 만약 total이 mid보다 크다면 새로운 블루레이 필요
        if total + i > mid:
            cnt += 1
            total = 0   # 새로운 블루레이 크기 측정을 위해 초기화

        total += i      # 레슨 길이만큼 블루레이 크기 증가

    if cnt <= m:        # 블루레이에 담을 수 있는 경우, 더 작은 값 있는지 확인하기
        end = mid - 1
    else:               # 더 큰 값으로 조정
        start = mid + 1

print(start)    # 최소 금액이므로 start 출력

