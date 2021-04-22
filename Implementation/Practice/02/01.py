# 문자열 재정렬
import sys

S = sys.stdin.readline().strip()
lst = []
sum_num = 0

for i in S:
    # 만약 숫자라면
    if i.isdigit():
        # sum_num에 더해주기
        sum_num += int(i)
    else:
        # 문자열인 경우 lst에 바로 추가해주기
        lst.append(i)

lst.sort()                  # 오름차순 정렬
lst.append(str(sum_num))    # 마지막에 숫자들의 합 추가해주기

print(''.join(lst))         # 문자열로 만들어주기