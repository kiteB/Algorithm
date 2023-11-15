# 한 줄로 서기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
answer = []

for i in range(n):
    answer.insert(data[n - 1 - i], n - i)

print(*answer)