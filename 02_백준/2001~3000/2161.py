# 카드 1
from collections import deque

n = int(input())
cards = deque(list(range(1, n + 1)))
answer = []

while len(cards) > 1:
    answer.append(cards.popleft())
    cards.append(cards.popleft())
answer.extend(cards)

print(*answer)
