# 곱하기 혹은 더하기
import sys

S = list(map(int, sys.stdin.readline().strip()))
answer = S[0]

for i in range(1, len(S)):
    if answer <= 0 or S[i] <= 0:
        answer += S[i]
    else:
        answer *= S[i]

print(answer)

