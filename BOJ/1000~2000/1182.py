# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하시오.
# 입력: 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다.
# 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
# 출력: 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
import itertools    # 조합을 구해주는 모듈

N, S = map(int, input().split())
num = list(map(int, input().split()))
count = 0   # 부분 수열의 개수를 저장할 변수
list1 = []  # 부분 수열을 저장할 리스트

for i in range(1, N+1):
    # num의 조합을 list1에 저장
    list1 = list(itertools.combinations(num, i))

    for i in list1:
        # 부분수열의 합이 S와 같다면 count 1 증가시켜주기
        if sum(i) == S:
            count += 1
print(count)