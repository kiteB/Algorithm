# N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 입력: 첫째 줄에 자연수 N이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], ..., A[N]이 주어진다.
# 다음 줄에는 M이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A 안에 존재하는지 알아내면 된다.
# 출력: M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
import sys


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(sys.stdin.readline())
N_array = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_array = list(map(int, sys.stdin.readline().split()))
N_array.sort()

for i in M_array:
    print(binary_search(i, N_array))
