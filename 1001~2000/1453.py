# 세준이는 피씨방에서 아르바이트를 한다. 세준이의 피씨방에는 1~100번의 컴퓨터가 있다.
# 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고 싶어한다. 따라서 들어오면서 번호를 말한다.
# 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.
# 거절당하는 사람의 수를 출력하는 프로그램의 작성하시오.
# 입력: 첫째 줄에 손님의 수 N이 주어진다. 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다.
# 출력: 첫째 줄에 거절당하는 사람의 수를 출력한다.
import sys

N = int(sys.stdin.readline())
case = list(map(int, sys.stdin.readline().split()))
pc = []
cnt = 0

for i in case:
    if i in pc:
        cnt += 1
    else:
        pc.append(i)
print(cnt)