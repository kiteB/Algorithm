# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N과 K가 주어진다. 둘째 줄부터 N개의 줄에 동전이 가치 Ai가 오름차순으로 주어진다.
# 출력: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []   # 동전 종류 저장하기 위한 리스트
count = 0   # 동전 개수를 카운트하기 위한 변수

for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))

for i in reversed(coin):    # 큰 단위의 동전부터 접근하기 위해서 reversed를 이용
    if K >= i:              # 만약 입력 받은 금액이 i보다 크거나 같다면
        count += K // i     # K를 i로 나눈 몫을 count에 더해주기
        K = K % i           # K를 i로 나누었을 때의 나머지로 K를 바꿔주기

print(count)

