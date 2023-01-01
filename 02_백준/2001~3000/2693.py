# N번째 큰 수
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    array = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    print(array[2])