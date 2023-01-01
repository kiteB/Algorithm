import sys
from collections import deque


def bfs(start):
    deq = deque([start])
    distance[start] = 1     # 자기 자신은 1로 설정

    while deq:
        node = deq.popleft()

        for i in friends[node]:
            if not distance[i]:
                distance[i] = distance[node] + 1    # 관계 수 업데이트
                deq.append(i)


n = int(sys.stdin.readline())   # 상근이의 동기의 수
m = int(sys.stdin.readline())   # 리스트의 길이

friends = [[] for _ in range(n + 1)]    # 친구 정보
distance = [0 for _ in range(n + 1)]    # 관계를 저장할 리스트

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

bfs(1)  # bfs 수행

answer = 0
for i in distance:
    if 2 <= i <= 3:     # 2 (상근이의 친구), 3 (상근이의 친구의 친구)
        answer += 1
print(answer)