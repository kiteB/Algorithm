# 케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
# 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.
# 케빈 베이컨은 미국 헐리우드 영화배우들끼리 케빈 베이컨 게임을 했을 때 나오는 단계의 총 합이 가장 적은 사람이라고 한다.
# Baekjoon Online Judge의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 찾으려고 한다.
# 케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이다.
# BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 구하시오.
# 입력: 첫째 줄에 유저의 수 N과 친구 관계의 수 M이 주어진다. 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다.
# 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
# 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 또, 모든 사람은 친구 관계로 연결되어져 있다.
# 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.
# 출력: 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다.
# 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.
import sys
from collections import deque


def bfs(start):
    visited = dict()
    queue = deque([[start, 0]])
    total_route = 0

    while queue:
        visited_ver, route = queue.popleft()
        visited[visited_ver] = 1
        total_route += route

        for connected_ver in friends[visited_ver]:
            if connected_ver not in visited:
                queue.append([connected_ver, route + 1])
                visited[connected_ver] = 1

    return total_route


N, M = map(int, sys.stdin.readline().split())
friends = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())

    # 친구 연결하기
    friends[A].append(B)
    friends[B].append(A)

answer = [0, 1000000]
for start in range(1, N+1):
    kevin = bfs(start)

    # 최소값으로 업데이트하기
    if kevin < answer[1]:
        answer = [start, kevin]

print(answer[0])