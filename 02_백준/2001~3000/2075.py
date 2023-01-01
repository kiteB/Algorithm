# N번째 큰 수
# N X N의 표에 수 N^2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다.
# N번째 큰 수를 찾는 프로그램을 작성하라. 표에 채워진 수는 모두 다르다.
# 입력: 첫째 줄에 N (1 <= N <= 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다.
# 출력: 첫째 줄에 N번째 큰 수를 출력하라.
import sys
import heapq

N = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
heapq.heapify(table)

for i in range(1, N):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in temp:
        if table[0] < j:
            heapq.heappush(table, j)
            heapq.heappop(table)

print(table[0])

