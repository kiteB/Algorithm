# 대칭 차집합
import sys
input = sys.stdin.readline

cnt_a, cnt_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a ^ b))   # ^: XOR 연산자
