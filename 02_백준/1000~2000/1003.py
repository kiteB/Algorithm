# N이 주어졌을 때, fibonacci(N)을 호출했을 때 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다.
# 출력: 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cnt_zero = [1, 0]
    cnt_one = [0, 1]

    for i in range(2, 41):
        cnt_zero.append(cnt_zero[i-2] + cnt_zero[i-1])
        cnt_one.append(cnt_one[i-2] + cnt_one[i-1])

    print(cnt_zero[N], cnt_one[N])