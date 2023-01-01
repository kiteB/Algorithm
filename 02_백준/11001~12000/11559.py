# Puyo Puyo
# 뿌요뿌요 룰
# 1. 필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.
# 2. 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
# 3. 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 4. 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.
# 5. 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
# 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!
# 입력:
# - . : 빈 공간
# - R : 빨강, G : 초록, B : 파랑, P : 보라, Y : 노랑
# 출력: 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
import sys
from collections import deque

field = []
for _ in range(12):
    field.append(list(sys.stdin.readline().strip()))

# 방향 그래프 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 탐색하는 함수
def bfs(y, x, color):
    # 탐색 코드
    deq = deque([[y, x]])
    visited[y][x] = True    # 방문 여부 체크

    puyo = deque([[y, x]])  # 터진 뿌요를 저장할 deque
    cnt = 1                 # color 뿌요가 터진 개수
    
    flag = 0                # 1 연쇄가 시작되었는지 체크할 변수

    while deq:
        y, x = deq.popleft()

        # 네 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있는지 & 방문 여부 확인
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[ny][nx] and field[ny][nx] == color:
                visited[ny][nx] = True      # 방문 여부 체크
                cnt += 1                    # 같은 색깔의 뿌요 터짐 개수 +1
                puyo.append([ny, nx])       # 터진 뿌요를 puyo에 저장
                deq.append([ny, nx])        # 다음 좌표 deq에 추가

    # 2. 같은 색 뿌요가 4개 이상 연결되어 있으면 (cnt가 4 이상이면) 터진다. -> 이때 1 연쇄 시작
    if cnt >= 4:
        # 연결되어 있는 뿌요를 '.'로 바꿔주기
        for y, x in puyo:
            field[y][x] = '.'
        flag = 1

    return flag


# 뿌요를 떨어뜨리는 함수
def down():
    for j in range(6):
        puyos = deque()             # 뿌요를 저장할 deque
        
        # 11부터 돌면서 뿌요가 있는지 탐색
        for i in range(11, -1, -1):
            # '.'이 아닌 뿌요가 있으면
            if field[i][j] != '.':
                puyos.append(field[i][j])

        # 11부터 돌면서 뿌요를 내릴 수 있으면 내리기
        for i in range(11, -1, -1):
            # 뿌요가 있으면
            if puyos:
                field[i][j] = puyos.popleft()
            else:
                field[i][j] = '.'


answer = 0              # 전체 연쇄가 몇 번 되었는지

# 필드를 돌면서 '.'이 아니고 아직 방문한 적이 없는 뿌요가 발견되면 함수 실행
while True:
    visited = [[False] * 6 for _ in range(12)]  # 방문 여부 체크할 리스트
    tmp = 0             # 탐색 동안 발생하는 연쇄 발생 횟수
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                tmp += bfs(i, j, field[i][j])

    # tmp가 0이라면 (연쇄가 한 번도 일어나지 않았다면)
    if not tmp:
        break
    else:
        # 연쇄가 일어났다면 answer (총 연쇄 횟수)를 1 증가
        answer += 1
        down()                  # 뿌요를 떨어뜨리기

print(answer)