# Lv.2 | 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def bfs(graph, start, exclude_edge):
    """
    시작 송전탐에서 출발하여 연결된 송전탑을 BFS로 탐색한 뒤, 방문한 송전탑의 개수를 반환한다.
    - graph: 송전탑 연결 정보
    - start: BFS 탐색의 시작 송전탑
    - exclude_edge: 현재 고려 중인 전선을 제외하고 BFS를 수행
    """
    n = len(graph) - 1  # 송전탑 개수
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    cnt = 1  # 방문한 송전탑 개수

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            # 해당 송전탑을 방문하지 않았고, 현재 고려 중인 전선을 제외하고 탐색 중인 송전탑과 연결되어 있지 않다면 아래를 수행함
            if not visited[node] and (now, node) != exclude_edge:
                visited[node] = True
                queue.append(node)
                cnt += 1

    return cnt


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n

    for a, b in wires:
        count_a = bfs(graph, a, (a, b))  # 현재 고려 중인 전선을 끊지 않았을 때의 송전탑 개수
        count_b = n - count_a  # 끊었을 때의 송전탑 개수
        answer = min(answer, abs(count_a - count_b))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
