# 차집합
import sys
input = sys.stdin.readline

cnt_a, cnt_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = sorted(list(set(a) - set(b)))

if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)
    