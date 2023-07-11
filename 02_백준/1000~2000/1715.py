# 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
answer = 0

while len(cards) != 1:
    # 제일 작은 값 두 개를 pop해서 더해준다.
    result = heapq.heappop(cards) + heapq.heappop(cards)
    answer += result
    heapq.heappush(cards, result)

print(answer)
