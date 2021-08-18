# 연산자 끼워넣기
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_num = -1e9
min_num = 1e9


def solve(idx, number, add, sub, mul, div):
    global max_num, min_num

    # 종료를 위한 조건문
    if idx >= n:
        max_num = max(max_num, number)
        min_num = min(min_num, number)
        return

    # 연산자 개수가 0이 아니라면 다음의 조건문 실행
    if add:
        solve(idx + 1, number + a[idx], add - 1, sub, mul, div)
    if sub:
        solve(idx + 1, number - a[idx], add, sub - 1, mul, div)
    if mul:
        solve(idx + 1, number * a[idx], add, sub, mul - 1, div)
    if div:
        # number 가 양수일 때와 아닌 경우를 나눠줌.
        if number > 0:
            result = number // a[idx]
        else:
            result = -((-number) // a[idx])
        solve(idx+1, result, add, sub, mul, div-1)


solve(1, a[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)

