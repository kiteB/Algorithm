# 부분수열의 합
import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
s.sort()        # 오름차순 정렬

num = 1
for i in s:
    if num < i:     # 수열의 합으로 만들 수 없는 수가 발견되면 종료
        break
    num += i
print(num)