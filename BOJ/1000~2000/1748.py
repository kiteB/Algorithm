# 수 이어 쓰기 1
import sys

n = sys.stdin.readline().strip()
length = len(n)

answer = 0
for i in range(1, length):  # length 전 자릿수까지의 총 자릿수를 구하는 for문
    answer += i * (pow(10, i) - pow(10, i - 1))

answer += (int(n) - pow(10, length - 1) + 1) * length
print(answer)