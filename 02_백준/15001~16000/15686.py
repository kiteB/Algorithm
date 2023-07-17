# 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
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
