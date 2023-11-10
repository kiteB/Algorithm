# 빈도 정렬
import sys
from collections import Counter
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))
counter = Counter(arr).most_common()

answer = []
for num, cnt in counter:
    answer.extend([num] * cnt)

print(*answer)
