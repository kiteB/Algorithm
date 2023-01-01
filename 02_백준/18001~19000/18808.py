# 스티커 붙이기
import sys


def is_attachable(y, x, sticker):   # 스티커를 붙일 수 있는지 판별
    h, w = len(sticker), len(sticker[0])
    for i in range(h):
        for j in range(w):
            if sticker[i][j] == 1 and notebook[i+y][j+x] == 1:
                return False
    return True


def attach(y, x, sticker):  # 스티커 붙이기
    h, w = len(sticker), len(sticker[0])
    for i in range(h):
        for j in range(w):
            if sticker[i][j] == 1:
                notebook[y + i][x + j] = 1


n, m, k = map(int, sys.stdin.readline().split())
notebook = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    stickers.append([list(map(int, sys.stdin.readline().split())) for _ in range(r)])

for idx in range(k):
    height, width = len(stickers[idx]), len(stickers[idx][0])
    rotate_cnt = 0  # 회전 횟수
    is_attached = False     # 스티커를 붙였는지 여부

    while rotate_cnt < 4:   # 회전은 3번만
        if height > n or width > m:     # 범위를 벗어난 경우, 회전시키기
            rotate_cnt += 1
            height, width, stickers[idx] = width, height, [tmp[::-1] for tmp in zip(*stickers[idx])]
            continue

        for i in range(n - height + 1):
            for j in range(m - width + 1):
                if is_attachable(i, j, stickers[idx]):  # 스티커를 붙일 수 있다면
                    attach(i, j, stickers[idx])     # 붙이기
                    is_attached = True
                    break

            if is_attached:
                break

        if is_attached:
            break
        else:       # 스티커를 붙일 수 없다면 90도 회전시키기
            rotate_cnt += 1
            height, width, stickers[idx] = width, height, [tmp[::-1] for tmp in zip(*stickers[idx])]

answer = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j] == 1:
            answer += 1
print(answer)