# 물병
import sys

n, k = map(int, sys.stdin.readline().split())
purchase = 0     # 상점에서 구입한 물병의 개수

while bin(n).count('1') > k:    # n을 이진수로 바꿨을 때 1의 개수가 k개 이하가 될 때까지 동작 수행
    idx = bin(n)[::-1].index('1')   # n을 이진수로 바꿨을 때 1이 처음 등장하는 위치 저장
    purchase += pow(2, idx)
    n += pow(2, idx)

print(purchase)