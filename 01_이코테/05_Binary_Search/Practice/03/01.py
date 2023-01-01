# 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    tmp = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= tmp + mid:
            cnt += 1
            tmp = house[i]

    # C개 이상의 공유기를 설치할 수 있는 경우
    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)