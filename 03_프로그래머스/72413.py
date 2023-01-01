# 합승 택시 요금 - 47분
def solution(n, s, a, b, fares):
    INF = int(1e9)          # 최댓값 설정
    graph = [[INF] * n for _ in range(n)]       # 노드 간 금액을 저장할 리스트
    
    # 자기 자신은 0
    for i in range(n):
        graph[i][i] = 0
    
    # 이동 경로 정보 저장
    for fare in fares:
        x, y, z = fare
        graph[x-1][y-1] = z
        graph[y-1][x-1] = z

    # i에서 j로 가는데 필요한 최소 비용 구하는 코드 작성
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    # i -> j의 비용보다 i -> k -> j의 비용이 적게 든다면 업데이트 해주기
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

    answer = INF
    # 중간 노드마다 경우 따져주기
    for k in range(n):
        # 시작 노드부터 k 까지 + k 노드부터 a + k 노드부터 b까지
        tmp = graph[s-1][k] + graph[k][a-1] + graph[k][b-1]
        answer = min(answer, tmp)
    return answer