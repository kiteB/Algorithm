# 부분합 - 골드 4
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_val = n + 1

while True:
    # 만약 총 합이 S가 넘는다면, left를 하나씩 옮겨 보면서 어디까지 길이가 줄어드나 확인
    if sum >= s:
        min_val = min(min_val, right - left)
        sum -= numbers[left]
        left += 1
    elif right == n:
        break

    # 만약 총합이 S를 넘지 않는다면, right 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을 때까지 더함
    else:
        sum += numbers[right]
        right += 1

if min_val == n + 1:
    print(0)
else:
    print(min_val)
