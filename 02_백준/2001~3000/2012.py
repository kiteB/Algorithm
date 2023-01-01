# 등수 매기기
import sys

n = int(sys.stdin.readline())
expected_rank = [int(sys.stdin.readline()) for _ in range(n)]
expected_rank.sort()

answer = 0
for i in range(n):
    answer += abs(expected_rank[i] - (i + 1))   # 불만도 계산

print(answer)