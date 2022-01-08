# 전구와 스위치
import sys

n = int(sys.stdin.readline())
current = list(map(int, sys.stdin.readline().strip()))
want = list(map(int, sys.stdin.readline().strip()))


def switch(bulb, cnt):
    if cnt == 1:
        bulb[0] = 1 - bulb[0]
        bulb[1] = 1 - bulb[1]

    for i in range(1, n):
        if bulb[i - 1] != want[i - 1]:
            cnt += 1
            bulb[i - 1] = 1 - bulb[i - 1]
            bulb[i] = 1 - bulb[i]

            if i != n - 1:  # 스위치 이후에 전구가 있다면 이후 전구 상태를 바꾼다.
                bulb[i + 1] = 1 - bulb[i + 1]

    if bulb == want:
        return cnt
    else:
        return -1


res1 = switch(current.copy(), 0)  # 첫 번째 전구 스위치를 누르지 않고 시작한 경우
res2 = switch(current.copy(), 1)  # 첫 번째 전구 스위치를 누르고 시작한 경우

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)
