# 3의 배수
import sys

X = list(map(int, sys.stdin.readline().strip()))
count = 0

while len(X) > 1:
    count += 1
    X = list(map(int, str(sum(X))))

y = int(''.join(map(str, X)))
if y in [3, 6, 9]:
    print(count)
    print('YES')
else:
    print(count)
    print('NO')