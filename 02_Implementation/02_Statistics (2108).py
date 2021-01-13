# N개의 수가 주어졌을 때, 네 가지 기본 통계값 출력하기
# 산술평균, 중앙값, 최빈값, 범위
# 산술평균은 소수점 이하 첫째 자리에서 반올림한 값 출력
# 최빈값이 여러 개일 경우에는 최빈값 중 두 번째로 작은 값 출력
import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = []

# 1개의 수가 입력되었을 때,
if N == 1:
    num = int(sys.stdin.readline())
    # 산술평균
    print(num)
    # 중앙값
    print(num)
    # 최빈값
    print(num)
    # 범위
    print(0)

else:
    # numbers에 입력 저장
    for i in range(N):
        numbers.append(int(sys.stdin.readline()))

    # numbers 정렬
    numbers.sort()

    # 산술평균
    print(round(sum(numbers)/N))

    # 중앙값
    print(numbers[N//2])

    # 최빈값
    mode = Counter(numbers).most_common()
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])

    # 범위
    print(max(numbers) - min(numbers))
