# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O가 교대로 나오는 문자열을 Pn이라고 한다.
# P1: IOI
# P2: IOIOI
# P3: IOIOIOI
# Pn: IOIOIO .... OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S 안에 Pn이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.
# 출력: S에 Pn이 몇 군데 포함되어 있는지 출력한다.
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = list(sys.stdin.readline().strip())

cnt = 0
pattern = 0

i = 0
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1

        if pattern == N:    # 우리가 찾고자 하는 패턴이 발견되면
            pattern -= 1
            cnt += 1
        i += 1
    else:
        pattern = 0
    i += 1

print(cnt)
