# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 연산자가 주어진다.
# 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
# 연산자의 개수는 N-1보다 많을 수도 있다. 모든 수의 사이에는 연산자를 한 개 끼워넣어야 하며, 주어진 연산자를 모두 사용하지 않고 모든 수의 사이에 연산자를 끼워넣을 수도 있다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
# N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
# 셋째 줄에는 합이 N-1보다 크거나 같고, 4N보다 작거나 같은 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
# 출력: 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다.
# 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
# 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_num = -1e9
min_num = 1e9


def solve(idx, number, add, sub, mul, div):
    global max_num, min_num
    
    # 종료를 위한 조건문
    if idx >= N:
        max_num = max(max_num, number)
        min_num = min(min_num, number)
        return

    # 연산자 개수가 0이 아니라면 다음의 조건문 실행
    if add:
        solve(idx+1, number + A[idx], add-1, sub, mul, div)
    if sub:
        solve(idx+1, number - A[idx], add, sub-1, mul, div)
    if mul:
        solve(idx+1, number * A[idx], add, sub, mul-1, div)
    if div:
        # number 가 양수일 때와 아닌 경우를 나눠줌.
        if number > 0:
            result = number // A[idx]
        else:
            result = -((-number) // A[idx])
        solve(idx+1, result, add, sub, mul, div-1)


solve(1, A[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)