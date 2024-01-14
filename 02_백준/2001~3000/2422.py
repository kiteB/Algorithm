# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
combination = [[True] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    combination[a][b] = False
    combination[b][a] = False

answer = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if not combination[i][j]:
            continue
        for k in range(j + 1, n + 1):
            if combination[i][k] and combination[j][k]:
                answer += 1

print(answer)
