# 용액 합성하기
import sys
input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))

start = 0
end = n - 1
answer = features[start] + features[end]
while start < end:
    gap = features[start] + features[end]

    if abs(gap) < abs(answer):
        answer = gap

    if gap == 0:
        break
    elif gap < 0:
        start += 1
    else:
        end -= 1

print(answer)
