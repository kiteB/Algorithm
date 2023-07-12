import sys
input = sys.stdin.readline

n = int(input())
feature = sorted(list(map(int, input().split())))

start = 0
end = n - 1

min_val = abs(feature[start] + feature[end])
answer = [feature[start], feature[end]]

while start < end:
    gap = feature[start] + feature[end]

    if min_val > abs(gap):
        min_val = abs(gap)
        answer = [feature[start], feature[end]]

    if answer == 0:
        break

    if gap < 0:
        start += 1
    else:
        end -= 1

print(*answer)
