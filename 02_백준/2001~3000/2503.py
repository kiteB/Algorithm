# 숫자 야구
import sys
from itertools import permutations

n = int(sys.stdin.readline())
numbers = list(permutations(list(range(1, 10)), 3))     # 가능한 모든 경우의 수 저장

tmp = []    # 제거할 리스트
for _ in range(n):
    test, strike, ball = map(int, sys.stdin.readline().split())     # 민혁이가 질문한 세 자리 수, 스트라이크 개수, 볼 개수
    test = str(test)

    for num in numbers:     # 가능한 모든 경우의 수와 하나씩 비교하기
        s, b = 0, 0

        for i in range(3):
            for j in range(3):
                if num[i] == int(test[j]):  # 숫자가 일치하고
                    if i == j:  # 인덱스가 일치하면 스트라이크
                        s += 1
                    elif i != j:    # 인덱스가 다르면 볼
                        b += 1

        if strike != s or ball != b:    # 스트라이크 수와 볼 수가 다르면 tmp 리스트에 추가
            tmp.append(num)

    while tmp:
        numbers.remove(tmp.pop())   # 조건에 맞지 않는 수 모두 제거

print(len(numbers))