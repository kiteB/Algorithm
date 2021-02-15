# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴푸터의 수를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고, 각 컴퓨터에는 1번부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에는 직접 연결되어 있는 컴퓨터의 쌍의 수가 주어진다.
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
# 출력: 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
import sys


def bfs(g, v, root):
    queue = [root]   # 시작 노드를 큐에 추가

    # 큐가 빌 때까지 반복
    while queue:
        node = queue.pop()

        if node not in v:
            v.append(node)

            for i in g[node]:
                if i not in v:
                    queue.append(i)

    cnt = len(v)

    if root in v:
        cnt -= 1

    return cnt


computer = int(sys.stdin.readline())    # 컴퓨터 수
linked_com = int(sys.stdin.readline())  # 연결되어 있는 컴퓨터 쌍의 수
network = [[] for i in range(computer+1)]    # 연결을 나타내는 리스트
visited = []    # 방문했는지를 나타내는 리스트

# 연결되어 있는 노드 나타내기
for i in range(linked_com):
    n1, n2 = map(int, sys.stdin.readline().split())
    network[n1].append(n2)
    network[n2].append(n1)

print(bfs(network, visited, 1))