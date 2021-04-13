# 자연수 M과 N이 주어질 때 M 이상 N 이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 입력: 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다. M은 N보다 작거나 같다.
# 출력: M 이상 N 이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 단, M 이상 N 이하의 자연수 중 소수가 없을 경우에는 첫째 줄에 -1을 출력한다.
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
isPrime = [False, False] + [True] * (N-1)
prime_numbers = []

for i in range(2, N+1):
    if isPrime[i]:
        for j in range(i+i, N+1, i):
            isPrime[j] = False

for i in range(M, N+1):
    if isPrime[i]:
        prime_numbers.append(i)

if sum(prime_numbers) != 0:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)