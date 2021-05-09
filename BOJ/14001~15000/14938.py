# 서강그라운드
# 예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다.
# 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다.
# 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다.
# 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는
# 낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만 어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.
# 각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다.
# 예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.
# 주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. (원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다)
# 예은이가 2번 지역에 떨어지게 되면 1번, 2번(자기 지역), 3번, 5번 지역에 도달할 수 있다.
# (4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.)
# 이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.
# 입력: 첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.
# 둘째 줄에는 n개의 숫자가 차례대로  각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.
# 세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.
# 출력: 예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.
import sys
import heapq

# 최대값 할당
INF = 1e9

# 입력부
vertex, limit, edge = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

# 인접 리스트 생성
adj = [[] for _ in range(vertex)]
for i in range(edge):
    x, y, z = map(int, sys.stdin.readline().split())
    adj[x-1].append([y-1, z])
    adj[y-1].append([x-1, z])


def dijstra(v):
    d[v] = 0
    q = [(d[v], v)]
    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for i in range(len(adj[now])):
            next = adj[now][i][0]
            nextdistance = adj[now][i][1] + dist
            if nextdistance < d[next]:
                d[next] = nextdistance
                heapq.heappush(q, (nextdistance, next))


# 각 정점에 대해 다익스트라 실행
ans = 0
for i in range(vertex):
    d = [INF] * vertex
    dijstra(i)
    cnt = item[i]
    for j in range(vertex):
        # 만일 j가 i가 아니고 수색범위 이내라면
        # cnt에 정점 j에서 얻을 수 있는 아이템 수를 더해줌
        if d[j] != 0 and d[j] <= limit:
            cnt += item[j]
    # 최대값 갱신
    if ans < cnt:
        ans = cnt
print(ans)

