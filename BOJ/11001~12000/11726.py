# 2Xn 크기의 정사각형을 1X2, 2X1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2X5 크기의 직사각형을 채운 한 가지 방법의 예이다.
# 입력: 첫째 줄에 n이 주어진다.
# 출력: 첫째 줄에 2Xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
import sys
from math import factorial

n = int(sys.stdin.readline())
repeat = n // 2 + 1
cnt = 0

for i in range(repeat):
    horizon_cnt = i
    vertical_cnt = n - (horizon_cnt * 2)

    result = factorial(horizon_cnt+vertical_cnt) // (factorial(horizon_cnt) * factorial(vertical_cnt))
    cnt += result

print(cnt % 10007)