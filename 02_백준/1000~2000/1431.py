# 시리얼 번호
import sys


def sum_num(numbers):   # number에 있는 총 숫자의 합을 구해주는 함수
    result = 0
    for i in numbers:
        if i.isdigit():
            result += int(i)
    return result


n = int(sys.stdin.readline())
guitars = [sys.stdin.readline().strip() for _ in range(n)]
guitars.sort(key=lambda x: (len(x), sum_num(x), x))     # 길이, sum_num의 값 (총 숫자의 합), x 기준으로 정렬

for guitar in guitars:
    print(guitar)
