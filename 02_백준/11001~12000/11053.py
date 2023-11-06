# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
# 입력: 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
# 출력: 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
# Longest Increasing Subsequences (LIS) 문제
import sys

size = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * size                             # 1로 초기화해주는 이유는 0번째 인덱스가 무조건 1이기 때문

for i in range(size):
    for j in range(i):
        if a[i] > a[j]:                     # 증가하는 수열을 찾기 위한 조건
            dp[i] = max(dp[i], dp[j]+1)     # +1을 해주는 이유는 마지막 i값을 추가한 값과 비교해야하기 때문
print(max(dp))