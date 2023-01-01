# 개미
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    l, n = map(int, sys.stdin.readline().split())
    min_time, max_time = 0, 0

    for i in range(n):
        position = int(sys.stdin.readline())

        min_move = min(l - position, position)  # 개미 한 마리 당 떨어지는 가장 빠른 시간
        max_move = l - min_move                 # 개미 한 마리 당 떨어지는 가장 느린 시간

        min_time = max(min_time, min_move)      # 개미가 모두 떨어지는데 걸리는 가장 빠른 시간
        max_time = max(max_time, max_move)      # 개미가 모두 떨어지는데 걸리는 가장 늦은 시간

    print(min_time, max_time)