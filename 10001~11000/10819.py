# N개의 정수로 이루어진 배열 A가 주어진다.
# 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
import sys
from itertools import permutations

N = int(sys.stdin.readline())
numbers = permutations(list(map(int, sys.stdin.readline().split())))
max_num = 0

for i in numbers:
    result = 0

    for j in range(N-1):
        result += abs(i[j] - i[j+1])
    max_num = max(max_num, result)
print(max_num)