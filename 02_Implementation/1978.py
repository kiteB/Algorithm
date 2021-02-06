# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in numbers:
    # 1인 경우는 break
    if i == 1:
        continue

    elif i == 2:
        cnt += 1

    # 2보다 큰 수인 경우 체크해주기
    else:
        idx = 0
        # 2부터 i-1까지의 수로 나누었을 때 나머지가 0이면 소수가 아니다.
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                idx += 1

        if idx == i-2:
            cnt += 1

print(cnt)