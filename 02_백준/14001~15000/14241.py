# 슬라임 합치기
import sys
from collections import deque

n = int(sys.stdin.readline())
slime = deque(sorted(list(map(int, sys.stdin.readline().split()))))
score = 0

while len(slime) >= 2:
    x, y = slime.popleft(), slime.popleft()
    slime.append(x + y)
    score += x * y

print(score)
