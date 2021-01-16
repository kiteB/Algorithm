# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자릿수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라고 한다.
# Ex) 245의 분해합은 245+2+4+5=256이 되며, 245는 256의 생성자가 된다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
N = int(input())
result = 0

# 1부터 N까지 for문을 돌려서 찾아내보자.
for i in range(1, N+1):
    A = list(map(int, str(i)))  # 숫자 자릿수 분리하기
    result = i + sum(A)         # 숫자 전체 + 각 자릿수의 합

    if result == N:
        print(i)
        break
if i == N:
    print(0)

