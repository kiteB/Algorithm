import sys

n, k = map(int, sys.stdin.readline().split())
quests = sorted(list(map(int, sys.stdin.readline().split())))

total = 0       # 총 경험치

for idx, quest in enumerate(quests):
    total += (quest * min(k, idx))

print(total)