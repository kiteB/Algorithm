# N번째 큰 수
import sys
import heapq
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
heapq.heapify(table)

for i in range(1, n):
    numbers = list(map(int, input().split()))

    for num in numbers:
        if table[0] < num:
            heapq.heappush(table, num)
            heapq.heappop(table)

print(table[0])
