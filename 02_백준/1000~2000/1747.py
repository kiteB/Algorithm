# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라고 부른다.
# 어떤 수 N이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하시오.
# 입력: 첫째 줄에 N이 주어진다.
# 출력: 첫째 줄에 조건을 만족하는 수를 출력한다.
import sys

N = int(sys.stdin.readline())
max_num = 1000000           # N의 최댓값
M = int(max_num ** 0.5)     # N의 약수의 최댓값
prime_numbers = [False, False] + [True] * (max_num-2)   # 소수 판별 저장할 리스트
answer = 0

# 소수 판별
for i in range(2, M+1):
    if prime_numbers[i]:
        for j in range(i+i, max_num, i):
            prime_numbers[j] = False

# 팰린드롬 판별
for i in range(N, max_num+1):
    num = str(i)
    reverse = num[::-1]
    if num == reverse and prime_numbers[i]:
        answer = num
        break

# 범위 내에 답이 없으면
if answer == 0:
    answer = 1003001

print(answer)