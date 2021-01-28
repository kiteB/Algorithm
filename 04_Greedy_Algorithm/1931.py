# 한 개의 회의실이 있는데 이를 사용하고나 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작 시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
# 단, 회의는 한 번 시작하면 중간에 중단될 수 없으며, 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작 시간과 끝나는 시간이 같을 수도 있다.
# 입력: 첫째 줄에 회의의 수 N이 주어진다. 둘째 줄부터 N+1줄까지 각 회의의 정보가 주어진다.
# 출력: 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
import sys

N = int(sys.stdin.readline())
count = 0       # 회의의 최대 개수를 저장할 변수
lst = []        # 모든 케이스를 저장할 리스트

for i in range(N):
    case = list(map(int, sys.stdin.readline().split()))
    lst.append(case)

lst = sorted(lst, key=lambda x: (x[1], x[0]))

start = 0
end = 0

for i in lst:
    if i[0] >= end:
        start = i[0]
        end = i[1]
        count += 1

print(count)