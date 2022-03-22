# 진짜 메시지
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    case = input().strip()
    keys = list(set(case))
    count_dict = {}
    temp = ''

    for key in keys:
        count_dict[key] = 0

    idx = 0
    while idx < len(case):
        count_dict[case[idx]] += 1
        temp += case[idx]

        if count_dict[case[idx]] >= 3:
            temp += case[idx]
            count_dict[case[idx]] = 0
            idx += 1
        idx += 1

    if temp == case:
        print('OK')
    else:
        print('FAKE')