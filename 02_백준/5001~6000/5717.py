# 상근이의 친구들
import sys

while True:
    male, female = map(int, sys.stdin.readline().split())

    if male * female == 0:
        break

    print(male + female)