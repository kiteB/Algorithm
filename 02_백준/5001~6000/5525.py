import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

answer = 0
cnt = 0
i = 0

while i < m - 1:
    if s[i:i + 3] == "IOI":
        cnt += 1

        if cnt == n:
            cnt -= 1
            answer += 1
        i += 2
    else:
        i += 1
        cnt = 0

print(answer)
