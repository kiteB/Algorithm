# 2Xn 크기의 정사각형을 1X2, 2X1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2X5 크기의 직사각형을 채운 한 가지 방법의 예이다.
# 입력: 첫째 줄에 n이 주어진다.
# 출력: 첫째 줄에 2Xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tile = [1, 2, ]

for i in range(2, n+1):
    tile.append(tile[i-2]+tile[i-1])
print(tile[n-1] % 10007)
