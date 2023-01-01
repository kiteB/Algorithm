# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x 좌표가 증가하는 순으로, x 좌표가 같으면 y 좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 점의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 i번 점의 위치 xi와 yj가 주어진다.
# 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
# 출력: 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    case = list(map(int, sys.stdin.readline().split()))
    lst.append(case)

for i in sorted(lst, key=lambda x: (x[0], x[1])):
    for j in i:
        print(j, end=' ')
    print()