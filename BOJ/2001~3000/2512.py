# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
# 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자.
# 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.
# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.
# 입력: 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다.
# 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다.
# 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 
# 출력: 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 
import sys

number = int(sys.stdin.readline())                      # 지방의 수
budget = list(map(int, sys.stdin.readline().split()))   # 지방의 예산 요청
national_budget = int(sys.stdin.readline())             # 전체 국가 예산

start, end = 0, max(budget)             # 시작, 끝 지정
answer = 0

if national_budget >= sum(budget):      # 요청된 예산의 총합보다 국가예산의 총액이 크다면
    answer = end                        # 요청 중 가장 큰 값이 최댓값이 된다.
else:
    while start <= end:
        mid = (start + end) // 2        # 중간값 구하기
        total = 0                       # 배정된 예산의 총합

        for item in budget:
            total += min(mid, item)     # 중간값과 요청 예산 중 최솟값을 더해준다.
            
        if total <= national_budget:    # 예산보다 작으면 start 값 조정
            start = mid + 1
        else:                           # 초과할 경우 end 값 조정
            end = mid - 1

        answer = end

print(answer)