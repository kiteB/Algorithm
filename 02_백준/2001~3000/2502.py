# 떡 먹는 호랑이
import sys

day, k = map(int, sys.stdin.readline().split())
dp = [[] for _ in range(day)]   # 각 날마다 호랑이에게 준 떡의 개수를 저장할 리스트
dp[0], dp[1] = 1, 1

while True:
    for i in range(2, day):
        dp[i] = dp[i - 1] + dp[i - 2]

    if dp[day - 1] == k:    # n째 날 호랑이에게 준 떡의 개수가 k개면 출력하고 종료
        print(dp[0], dp[1], sep='\n')
        break

    elif dp[day - 1] > k:   # A와 B의 차이가 작아져야 한다.
        dp[0] += 1
        dp[1] = dp[0]

    else:   # A와 B의 차이가 커져야 한다.
        dp[1] += 1