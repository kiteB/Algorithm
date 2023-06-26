# 용액
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

s = 0
e = n - 1

answer = abs(data[s] + data[e])
start = s
end = e
while s < e:
    gap = data[s] + data[e]

    if abs(gap) < answer:
        start = s
        end = e
        answer = abs(gap)

        if answer == 0:
            break

    if gap < 0:
        s += 1
    else:
        e -= 1

print(data[start], data[end])
