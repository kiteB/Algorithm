# 스위치 켜고 끄기
import sys

cnt = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
on_off = {0: 1, 1: 0}
student = int(sys.stdin.readline())

for _ in range(student):
    gender, num = map(int, sys.stdin.readline().split())

    if gender == 1:  # 남자인 경우
        for i in range(num, cnt + 1, num):
            switch[i] = on_off[switch[i]]

    else:  # 여자인 경우
        left = switch[num - 1:0:-1]
        right = switch[num + 1:]

        same = 0
        for i in range(min(len(left), len(right))):
            if left[i] == right[i]:
                same += 1
            else:
                break

        for i in range(same):
            left[i] = on_off[left[i]]
            right[i] = on_off[right[i]]

        switch = [0] + left[::-1] + [on_off[switch[num]]] + right

for i in range(1, cnt + 1):
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')