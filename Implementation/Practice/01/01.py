# 럭키 스트레이트
import sys

N = list(map(int, sys.stdin.readline().strip()))
mid = len(N) // 2       # 중앙 인덱스 구하기

# 중앙을 기준으로 나눈 각각의 합이 같으면
if sum(N[:mid]) == sum(N[mid:]):
    print("LUCKY")
else:   # 같지 않다면
    print("READY")

