# 카드 놓기
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

answer = set()
# 모든 순열을 구해서 중복 없이 저장되도록 answer에 추가하기
for p in list(permutations(cards, k)):
    answer.add(int(''.join(map(str, p))))

print(len(answer))
