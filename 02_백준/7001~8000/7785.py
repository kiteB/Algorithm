# 회사에 있는 사람
import sys
input = sys.stdin.readline

n = int(input())
access_dict = dict()

for _ in range(n):
    name, state = input().split()

    if state == "enter":
        access_dict[name] = state
    elif state == "leave":
        del access_dict[name]

print(*sorted(access_dict.keys(), reverse=True), sep='\n')
