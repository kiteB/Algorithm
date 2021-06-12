# 암기왕
import sys

t = int(sys.stdin.readline())       # 테스트케이스 개수

for _ in range(t):
    n = int(sys.stdin.readline())       # 수첩 1에 적어 놓은 정수의 개수
    note1 = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())       # 수첩 2에 적어 놓은 정수의 개수
    note2 = list(map(int, sys.stdin.readline().split()))

    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)

