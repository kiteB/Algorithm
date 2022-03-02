# Base Conversion
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()

decimal = 0     # 10진법으로 변환한 값
for i in range(m):
    decimal += numbers[i] * (a ** i)

result = []
while decimal:
    result.append(str(decimal % b))
    decimal //= b

print(*result[::-1])