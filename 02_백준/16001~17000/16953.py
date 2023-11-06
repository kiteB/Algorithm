# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# - 2를 곱한다.
# - 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
# 입력: 첫째 줄에 A, B (1 <= A < B <= 10^9)가 주어진다.
# 출력: A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
import sys

A, B = map(int, sys.stdin.readline().split())
cnt = 1     # A를 B로 바꾸는데 필요한 연산 횟수

while True:
    # A == B인 경우 break
    if A == B:
        break

    # A > B인 경우
    elif A > B:
        cnt = -1
        break

    # 연산 1) 2를 곱한다.
    elif B % 2 == 0:
        B //= 2
        cnt += 1

    # 연산 2) 1을 수의 가장 오른쪽에 추가한다.
    elif B % 10 == 1:
        B //= 10
        cnt += 1

    else:
        cnt = -1
        break

print(cnt)