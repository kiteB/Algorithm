# 톱니바퀴
import sys
from collections import deque


# 왼쪽이 회전 가능한지 검사
def check_left(num, d):
    if num < 1 or gears[num][2] == gears[num+1][6]:
        return

    if gears[num+1][6] != gears[num][2]:
        check_left(num-1, -d)
        gears[num].rotate(d)


# 오른쪽이 회전 가능한지 검사
def check_right(num, d):
    if num > 4 or gears[num-1][2] == gears[num][6]:
        return

    if gears[num-1][2] != gears[num][6]:
        check_right(num+1, -d)
        gears[num].rotate(d)


gears = {}
# 톱니바퀴의 상태 저장
for i in range(1, 5):
    gears[i] = deque(list(map(int, sys.stdin.readline().strip())))

k = int(sys.stdin.readline())       # 회전 횟수
for _ in range(k):
    gear_num, direction = map(int, sys.stdin.readline().split())
    check_left(gear_num-1, -direction)
    check_right(gear_num+1, -direction)
    gears[gear_num].rotate(direction)

result = 0
for i in range(1, 5):
    result += pow(2, i-1) * gears[i][0]
print(result)