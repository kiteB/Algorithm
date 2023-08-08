# 접미사 배열
from sys import stdin

s = stdin.readline().rstrip()
answer = []
for i in range(len(s)):
    answer.append(s[i:])

print(*sorted(answer), sep='\n')
