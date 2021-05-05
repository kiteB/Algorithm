# N개의 정수로 이루어진 배열 A가 주어진다.
# 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
import sys
from itertools import permutations

N = int(sys.stdin.readline())   # 배열에 들어있는 수의 개수
numbers = permutations(list(map(int, sys.stdin.readline().split())))    # 배열 A의 순열
max_num = 0     # 식의 최댓값

for i in numbers:   # 생성된 순열을 하나씩 꺼내오기
    result = 0      # 각 케이스마다 식의 계산값 저장할 변수

    for j in range(N-1):
        result += abs(i[j] - i[j+1])    # 식 계산

    max_num = max(max_num, result)  # max_num과 result 중 더 큰 값으로 설정

print(max_num)