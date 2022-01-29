# 서버실
import sys


def check(data, height, n):  # 정상 작동하는 컴퓨터 검사
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += (height if height <= data[i][j] else data[i][j])

    return cnt


n = int(sys.stdin.readline())
computers = []
total = max_val = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    computers.append(line)
    max_val = max(max_val, max(line))
    total += sum(line)

low, high = 0, max_val
answer = 0
while low <= high:
    mid = (low + high) // 2

    if check(computers, mid, n) >= total / 2:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)
