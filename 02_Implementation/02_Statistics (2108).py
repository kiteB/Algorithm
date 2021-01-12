# N개의 수가 주어졌을 때, 네 가지 기본 통계값 출력하기
# 산술평균, 중앙값, 최빈값, 범위
# 산술평균은 소수점 이하 첫째 자리에서 반올림한 값 출력
# 최빈값이 여러 개일 경우에는 최빈값 중 두 번째로 작은 값 출력
N = int(input())
numbers = []
cnt = []

for i in range(N):
    numbers.append(int(input()))

# 산술평균
avg = sum(numbers)/N
print(round(avg))

# 중앙값
median = numbers[round(N/2 + 1)]
print(median)

# 최빈값
# 아직 구현 못함

# 범위
difference = max(numbers) - min(numbers)
print(difference)
