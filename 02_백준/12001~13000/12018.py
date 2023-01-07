# Yonsei TOTO
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

for _ in range(n):
    p, l = map(int, input().split())
    mileage = list(map(int, input().split()))

    if p < l:
        result.append(1)
    else:
        mileage.sort(reverse=True)
        result.append(mileage[l - 1])

result.sort()
answer = 0
for i in result:
    if m >= i:
        m -= i
        answer += 1

print(answer)
