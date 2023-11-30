# 기타줄
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_package = 1001
min_individual = 1001

for _ in range(m):
    a, b = map(int, input().split())
    min_package = min(min_package, a)
    min_individual = min(min_individual, b)

answer = 0
if min_package > min_individual * 6:
    answer += n * min_individual
else:
    answer += (n // 6) * min_package

    if (n % 6) * min_individual > min_package:
        answer += min_package
    else:
        answer += (n % 6) * min_individual

print(answer)
