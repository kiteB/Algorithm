# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys

n, m = map(int, sys.stdin.readline().split())
combination = [[True] * (n + 1) for _ in range(n + 1)]  # 함께 먹을 수 있는지 여부 저장할 리스트

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    combination[a][b] = False
    combination[b][a] = False

answer = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if not combination[i][j]:  # 맞지 않은 조합이면
            continue
        for k in range(j + 1, n + 1):
            if combination[i][k] and combination[j][k]:
                answer += 1

print(answer)
