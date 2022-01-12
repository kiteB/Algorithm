# 점수 계산
import sys

scores = [int(sys.stdin.readline()) for _ in range(8)]
indexes = []
sorted_scores = sorted(scores, reverse=True)
total = 0

for i in range(5):
    score = sorted_scores[i]
    indexes.append(scores.index(score) + 1)
    total += score

print(total)
print(*sorted(indexes))