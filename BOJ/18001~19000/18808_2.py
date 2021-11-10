import sys


def is_attachable(y, x, sticker):   # 스티커를 붙일 수 있는지 판단
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
    tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

    if r-1 > n or c-1 > m:
        continue
    else:
        stickers.append(tmp)

for k in range(len(stickers)):
    height, width = len(stickers[k]), len(stickers[k][0])
    rotate_cnt = 0
    is_attached = False

    while rotate_cnt < 4:
        if height - 1 > n or width - 1 > m:
            height, width, stickers[k] = width, height, [tmp[::-1] for tmp in zip(*stickers[k])]
            continue

        for i in range(n - height + 1):
            for j in range(m - width + 1):
                if is_attachable(i, j, stickers[k]):
                    attach(i, j, stickers[k])
                    is_attached = True
                    break

            if is_attached:
                break

        if is_attached:
            break
        else:
            rotate_cnt += 1
            height, width, stickers[k] = width, height, [tmp[::-1] for tmp in zip(*stickers[k])]

answer = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j] == 1:
            answer += 1
print(answer)