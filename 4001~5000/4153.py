# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인 것을 알아냈다.
# 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
import sys

while True:
    case = list(map(int, sys.stdin.readline().split()))

    if case[0] == 0 and case[1] == 0 and case[2] == 0:
        break
    else:
        case.sort(reverse=True)
        if case[0] ** 2 == case[1] ** 2 + case[2] ** 2:
            print('right')
        else:
            print('wrong')