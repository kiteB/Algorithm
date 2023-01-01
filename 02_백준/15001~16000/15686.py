# 치킨 배달
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 도시에 있는 치킨집 중 최대 M개를 선택했을 때, 도시의 치킨 거리의 최솟값 출력하기
# 입력: 첫째 줄에 N과 M이 주어지며, 둘째 줄부터 N개의 줄에는 도시의 정보가 주어짐.
# 도시의 정보는 0, 1, 2로 이루어져 있음 - 0은 빈 집, 1은 집, 2는 치킨집을 의미함.
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
houses = []             # 집의 위치를 저장할 리스트
chicken = []            # 치킨집의 위치를 저장할 리스트

for r in range(n):
    for c in range(n):
        # 집 찾기
        if maps[r][c] == 1:
            houses.append((r, c))
        # 치킨집 찾기
        elif maps[r][c] == 2:
            chicken.append((r, c))

answer = 1000000                # 도시의 치킨 거리의 최솟값
for c in combinations(chicken, m):
    result = 0                  # 집과 치킨집 거리의 최솟값

    for house in houses:
        min_val = 1000000

        for i in c:
            distance = abs(house[0] - i[0]) + abs(house[1] - i[1])            # 집과 치킨집의 거리 계산
            min_val = min(distance, min_val)

        result += min_val
    answer = min(answer, result)

print(answer)