# 정수 X가 주어졌을 때, X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력한다.
# 수의 구성이 같다는 말은, 수를 이루고 있는 각 자릿수가 같다는 뜻이다.
# 입력: 첫째 줄에 X가 주어진다. X는 0으로 시작하지 않는다.
# 출력: 첫째 줄에 결과를 출력한다. 만약 그러한 숫자가 없는 경우에는 0을 출력한다.
import sys
from itertools import permutations

X = list(map(str, sys.stdin.readline().strip()))
permute = list(permutations(X))
numbers = []
for i in permute:
    numbers.append(''.join(i))
numbers.sort()

while True:
    num = 0
    for i in numbers:
        if int(i) > int(''.join(X)):
            num = i
            break
    break
print(num)