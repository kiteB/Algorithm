# N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(N-1):
    ans += numbers[i]*(sum(numbers)-sum(numbers[0:(i+1)]))

print(ans)
