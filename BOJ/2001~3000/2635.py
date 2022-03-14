# 수 이어가기
import sys

num = int(sys.stdin.readline())
answer = []

for i in range((num // 2), num + 1):
    temp = [num, i]
    idx = 1

    while True:
        gap = temp[idx - 1] - temp[idx]
        if gap < 0:
            break
        temp.append(gap)
        idx += 1

        if len(temp) > len(answer):
            answer = temp

print(len(answer))
print(*answer)

