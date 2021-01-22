# ATM 앞에 N명의 사람들이 있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
# 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
# 줄을 서 있는 사람의 수가 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())
times = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0

for i in range(N):
    sum += times[i] * (N-i)
print(sum)