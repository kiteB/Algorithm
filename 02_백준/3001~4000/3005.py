import sys

r, c = map(int, sys.stdin.readline().split())
puzzle = [list(sys.stdin.readline().strip()) for _ in range(r)]

words = []
for i in range(r):    # 가로를 기준으로 단어 탐색
    tmp = ''

    for j in range(c):
        if puzzle[i][j] == '#':
            if len(tmp) >= 2:
                words.append(tmp)
            tmp = ''
        else:
            tmp += puzzle[i][j]

    if len(tmp) >= 2:
        words.append(tmp)

for j in range(c):    # 세로를 기준으로 단어 탐색
    tmp = ''

    for i in range(r):
        if puzzle[i][j] == '#':
            if len(tmp) >= 2:
                words.append(tmp)
            tmp = ''
        else:
            tmp += puzzle[i][j]

    if len(tmp) >= 2:
        words.append(tmp)

words.sort()
print(words[0])
