# 풍선 터뜨리기
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))
answer = []     # 터진 풍선 정보 저장

while queue:
    idx, move = queue.popleft()
    answer.append(idx + 1)

    if move > 0:
        queue.rotate(-(move - 1))
    else:
        queue.rotate(-move)

print(*answer)