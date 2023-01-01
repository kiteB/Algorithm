# 킹
import sys

direction = {
    'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
}
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, cnt = sys.stdin.readline().split()

# 킹과 돌의 위치를 좌표로 변환
kx, ky = col.index(king[0]), int(king[1]) - 1
sx, sy = col.index(stone[0]), int(stone[1]) - 1

for i in range(int(cnt)):
    cmd = sys.stdin.readline().strip()

    dx, dy = direction[cmd]

    # 명령대로 이동한 킹의 위치
    nx = kx + dx
    ny = ky + dy

    if nx < 0 or nx > 7 or ny < 0 or ny > 7:    # 이동 가능한 범위를 벗어나면 이동 무시
        continue

    if nx == sx and ny == sy:    # 이동 후 좌표가 돌의 좌표와 동일한 경우

        # 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시키기
        stone_nx = sx + dx
        stone_ny = sy + dy

        if stone_nx < 0 or stone_nx > 7 or stone_ny < 0 or stone_ny > 7:    # 이동 가능한 범위를 벗어나면 이동 무시
            continue

        sx, sy = stone_nx, stone_ny     # 돌의 좌표 갱신

    kx, ky = nx, ny     # 킹의 좌표 갱신

king_pos = col[kx] + str(ky + 1)
stone_pos = col[sx] + str(sy + 1)

print(king_pos)
print(stone_pos)