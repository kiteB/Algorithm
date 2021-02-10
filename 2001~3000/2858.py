# 상근이는 기숙사 생활을 한다. 상근이의 방의 크기는 L * W이다.
# 수업시간에 타일 채우기 경우의 수를 계산하던 상근이는 자신의 방을 1*1크기 타일로 채우려고 한다. 이때 가장자리는 빨간색으로 나머지는 갈색으로 채우려고 한다.
# 어느 날 상근이네 방에 하근이가 놀러왔다. 하근이는 상근이의 타일 배치에 감동을 받았다.
# 다시 방으로 돌아온 하근이는 빨간색과 갈색 타일의 개수는 기억했지만, 방의 크기는 기억해내지 못했다.
# 빨간색과 갈색 타일의 개수가 주어졌을 때, 상근이 방의 크기를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 빨간색 타일의 수 R과 갈색 타일의 수 B가 주어진다.
# 출력: 첫째 줄에 상근이네 방의 크기 L과 W을 공백으로 구분하여 출력한다. 만약, 두 수가 다르면 큰 수가 L이 되고, 작은 수가 W이 된다.
import sys

R, B = map(int, sys.stdin.readline().split())
sum_LW = (R + 4) // 2   # L + W의 값
multiple_LW = R + B     # L * W의 값

for i in range(1, multiple_LW):
    if (sum_LW - i) * i == multiple_LW:
        print(max(sum_LW - i, i), min(sum_LW - i, i))
        break