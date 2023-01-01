# 체스판 다시 칠하기
import sys

n, m = map(int, sys.stdin.readline().split())
chess = [list(sys.stdin.readline().strip()) for _ in range(n)]

answer = 65
for i in range(n - 7):
    for j in range(m - 7):
        white, black = 0, 0     # 각각 첫 번째 칸이 W, B일 때 다시 칠해야 하는 개수

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:        # 첫 번째 칸에 칠한 색과 색이 같아야 하는 칸들의 경우,
                    if chess[a][b] != 'W':  # W가 아니라면, W로 칠해야 한다.
                        white += 1
                    else:       # B가 아니라면, B로 칠해야 한다.
                        black += 1
                else:                       # 첫 번째 칸에 칠한 색과 달라야 하는 칸들의 경우,
                    if chess[a][b] != 'B':  # B가 아니라면, W로 칠해야 한다.
                        white += 1
                    else:       # W가 아니라면, B로 칠해야 한다.
                        black += 1

        cnt = min(black, white)
        answer = min(answer, cnt)

print(answer)