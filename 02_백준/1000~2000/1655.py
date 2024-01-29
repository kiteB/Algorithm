# 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
answer = []

for _ in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and -left_heap[0] > right_heap[0]:
        min_val = heapq.heappop(right_heap)
        max_val = -heapq.heappop(left_heap)
        heapq.heappush(left_heap, -min_val)
        heapq.heappush(right_heap, max_val)
    answer.append(-left_heap[0])

print(*answer, sep='\n')
