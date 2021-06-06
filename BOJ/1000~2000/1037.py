# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 둘째 줄에는 N의 진짜 약수가 주어진다.
# 출력: 첫째 줄에 N을 출력한다.
import sys

N = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))

if min(divisors) != 1:
    print(max(divisors) * min(divisors))