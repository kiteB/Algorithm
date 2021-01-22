# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N과 K가 주어진다. 둘째 줄부터 N개의 줄에 동전이 가치 Ai가 오름차순으로 주어진다.
# 출력: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
count = 0

for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))

for i in reversed(coin):
    if K >= i:
        count += K // i
        K = K % i

print(count)

