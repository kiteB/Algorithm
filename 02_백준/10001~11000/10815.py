# 숫자 카드
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

card_dict = defaultdict(int)
# 상근이가 가지고 있는 카드 개수 저장
for card in cards:
    card_dict[card] += 1

for num in test:
    print(card_dict[num], end=' ')
