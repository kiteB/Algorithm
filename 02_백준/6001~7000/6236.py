# 용돈 관리
import sys

n, m = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(n)]

start = max(money)      # 인출할 금액의 최댓값보다는 크거나 같아야 한다
end = sum(money)        # 인출할 금액의 합보다는 작거나 같아야 한다

while start <= end:
    mid = (start + end) // 2    # 인출할 금액
    total = 0   # 사용 금액
    cnt = 1     # 인출 횟수

    for i in money:
        # 인출 금액이 모자라다면 새로 인출
        if total + i > mid:
            cnt += 1        # 인출 횟수 증가
            total = 0       # 사용 금액 초기화

        total += i          # 사용 금액 증가

    if cnt <= m:        # 인출이 가능한 경우, 더 작은 값 있는지 확인하기
        end = mid - 1
    else:               # 인출이 불가능한 경우, 더 큰 값으로 조정
        start = mid + 1

print(start)            # 최솟값을 구하는 것이므로 start 출력