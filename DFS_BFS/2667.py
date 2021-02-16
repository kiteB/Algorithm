# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
# 입력: 첫 번째 줄에는 지도의 크기 N이 입력되고, 그 다음 N 줄에는 각각 N개의 자료(0 혹은 1)가 입력됨.
# 출력: 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
import sys

N = int(sys.stdin.readline())   # 지도의 크기
maps = []   # 지도
visited = [[0]*N for i in range(N)]     # 방문했는지 체크하는 리스트
house = []  # 각 단지마다 집 수를 저장할 리스트
cnt = 0     # 단지 내 집 수를 카운트하기 위한 변수

# 지도 데이터 저장하기
for i in range(N):
    line = list(map(int, sys.stdin.readline().strip()))
    maps.append(line)


def numbering(x, y):
    # 전역변수 cnt 설정
    global cnt

    # 방문했던 적이 없는 노드라면 visited[x][y]를 1로 바꿔주기
    if visited[x][y] == 0:
        visited[x][y] = 1

        # 집이 존재한다면 house 1로 바꾸기
        if maps[x][y] == 1:
            cnt += 1

            # 오른쪽으로 이동할 수 있으면
            if x < N-1:
                if visited[x+1][y] == 0:
                    numbering(x+1, y)

            # 아래로 이동할 수 있으면
            if y < N - 1:
                if visited[x][y + 1] == 0:
                    numbering(x, y + 1)

            # 왼쪽으로 이동할 수 있으면
            if x > 0:
                if visited[x-1][y] == 0:
                    numbering(x-1, y)

            # 위로 이동할 수 있으면
            if y > 0:
                if visited[x][y-1] == 0:
                    numbering(x, y-1)

            return True
        return False


for i in range(N):
    for j in range(N):
        # 만약 numbering(i, j)가 True인 경우
        if numbering(i, j):
            # house에 cnt를 추가하고
            house.append(cnt)
            # cnt를 다시 0으로 초기화하기
            cnt = 0

# 총 단지 수
print(len(house))
# 단지내 집의 수 오름차순으로 정렬
for i in sorted(house):
    print(i)