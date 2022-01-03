# 햄버거 분배
import sys

n, k = map(int, sys.stdin.readline().split())
data = list(sys.stdin.readline().strip())

answer = 0
for i in range(n):
    if data[i] == 'P':  #사람일 때
        for j in range(i - k, i + k + 1):   # (i - k) ~ (i + k) 범위 내에
            if 0 <= j <= n - 1:
                if data[j] == 'H':  # 햄버거를 발견하면
                    answer += 1     # 개수 증가
                    data[j] = '.'   # `.`으로 변경
                    break
print(answer)
