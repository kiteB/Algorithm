# < 아기 상어 >
# N X N 크기의 공간에 물고기 M 마리와 아기 상어 1마리가 있다. 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
# - 아기 상어 > 물고기 : 먹을 수 있음.
# - 아기 상어 == 물고기 : 먹을 수 없음. 지나갈 수 있음.
# - 아기 상어 < 물고기 : 먹을 수 없음. 지나갈 수 없음.
# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
# - 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
#   * 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
#   * 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
# 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈칸이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.
# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
# < 입력 >
# 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
# 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
# - 0: 빈 칸
# - 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# - 9: 아기 상어의 위치
# 아기 상어는 공간에 한 마리 있다.
# < 출력 >
# 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
import sys
from collections import deque

N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# 방향 정보를 저장할 리스트
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def solution(y, x):
    deq, visited = deque([(y, x)]), deque([(y, x)])
    shark = 2           # 아기 상어 크기
    time = 0            # 걸린 시간
    fish = 0            # 상어가 먹은 물고기 수
    eat_flag = False

    answer = 0

    while deq:
        deq = deque(sorted(deq))

        for _ in range(len(deq)):
            y, x = deq.popleft()

            # 물고기를 먹을 수 있는 경우
            if 1 <= maps[y][x] < shark:
                maps[y][x] = 0              # 먹었다!
                fish += 1

                # 상어 크기 만큼 먹었으면 fish 초기화 & 아기 상어 크기 +1
                if fish == shark:
                    shark += 1
                    fish = 0

                # 물고기를 먹었으면 다시 탐색을 해야하니까 초기화를 해준다.
                deq, visited = deque(), deque([(y, x)])
                eat_flag = True

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and (ny, nx) not in visited:
                    if maps[ny][nx] <= shark:
                        deq.append((ny, nx))
                        visited.append((ny, nx))

            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            maps[i][j] = 0              # 현재 위치를 0으로 바꾸기
            print(solution(i, j))       # y 좌표, x 좌표


