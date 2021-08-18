# 문자열 뒤집기
import sys

S = list(map(int, sys.stdin.readline().strip()))
zero_to_one = 0
one_to_zero = 0

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        if S[i-1] == 0:
            zero_to_one += 1
        else:
            one_to_zero += 1

if S[-1] != S[0]:
    if S[-1] == 0:
        zero_to_one += 1
    else:
        one_to_zero += 1

print(min(zero_to_one, one_to_zero))

