# 카드 합체 놀이
import sys
from queue import PriorityQueue

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
q = PriorityQueue()     # 우선순위 큐

for i in cards:     # card를 우선순위 큐에 넣기
    q.put(i)

for i in range(m):  # 가장 작은 원소 두 개를 꺼낸 후, 두 원소의 합을 다시 넣기
    a = q.get()
    b = q.get()

    q.put(a + b)
    q.put(a + b)

total = 0
for i in range(n):  # 카드의 총합 구하기
    total += q.get()
print(total)