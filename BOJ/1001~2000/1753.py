# 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.
# 입력: 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
# u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
# 출력: 첫째 줄부터 V개의 줄에 걸쳐, i번재 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())   # 정점의 개수, 간선의 개수
K = int(sys.stdin.readline())       # 시작 정점의 번호
graph = [[] for i in range(V+1)]    # 노드 정보를 저장할 리스트
INF = V * 10 + 1
distances = [INF for _ in range(V + 1)]  # start로부터의 거리 값을 저장하기 위함


def dijkstra(g, start):
    distances[start] = 0  # 시작 노드는 0
    queue = []
    heapq.heappush(queue, [0, start])  # 가중치와 시작 노드를 push

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색할 노드와 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 거리가 기존의 거리보다 크다면 그냥 넘어감.
            continue

        for new_destination, new_distance in g[current_destination]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            
            if distance < distances[new_destination]:  # 알고 있는 거리보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 queue에 삽입


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

dijkstra(graph, K)

for i in range(1, V+1):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])