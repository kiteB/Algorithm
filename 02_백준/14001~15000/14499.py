# 주사위 굴리기
import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]     # 지도 정보 저장
orders = list(map(int, sys.stdin.readline().split()))        # 명령 정보 저장
dice = [0] * 7          # 주사위 정보를 저장할 리스트

# 방향 그래프 정의 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for order in orders:
    nx = x + dx[order-1]
    ny = y + dy[order-1]

    # 이동할 수 없는 경우 명령 무시
    if not (0 <= nx <= n-1 and 0 <= ny <= m-1):
        continue

    # order에 따라 주사위 값 변경하기
    # order가 1일 때, dice[2]와 dice[5]의 값은 바뀌지 않는다.
    if order == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]

    # order가 2일 때, dice[2]와 dice[5]의 값은 바뀌지 않는다.
    elif order == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]

    # order가 3일 때, dice[3]과 dice[4]의 값은 바뀌지 않는다.
    elif order == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

    # order가 4일 때, dice[3]과 dice[4]의 값은 바뀌지 않는다.
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면 dice[6] 값으로 변경하기.
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[6]
    else:   # 0이 아니면 dice[6] 값이 변경된다.
        dice[6] = maps[nx][ny]
        maps[nx][ny] = 0

    # 주사위의 위치 변경
    x, y = nx, ny
    print(dice[1])
