# 사탕 게임
import sys

n = int(sys.stdin.readline())
boards = [list(sys.stdin.readline().strip()) for _ in range(n)]


def count(candy):
    max_cnt = 0
    
    for i in range(n):
        row_cnt = 1     # 행 선택 시 사탕 최대 개수
        col_cnt = 1     # 열 선택 시 사탕 최대 개수

        for j in range(n-1):
            
            # 행 기준으로 탐색
            if candy[i][j] == candy[i][j+1]:    # 색이 동일하면 +1
                row_cnt += 1
            else:   # 색이 다르면 max_cnt 값 갱신하고 row_cnt 1로 초기화
                max_cnt = max(row_cnt, max_cnt)
                row_cnt = 1
            
            # 열 기준으로 탐색
            if candy[j][i] == candy[j+1][i]:    # 색이 동일하면 +1
                col_cnt += 1
            else:   # 색이 다르면 max_cnt 값 갱신하고 col_cnt 1로 초기화
                max_cnt = max(col_cnt, max_cnt)
                col_cnt = 1

        max_cnt = max(row_cnt, col_cnt, max_cnt)

    return max_cnt


answer = 0  # 상근이가 먹을 수 있는 사탕의 최대 개수
for i in range(n):
    for j in range(n - 1):

        # 자신의 오른쪽 사탕과 비교
        if boards[i][j] != boards[i][j + 1]:    # 색이 다른 경우만 체크해보기
            boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]
            answer = max(count(boards), answer)
            boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]     # 원상복귀
        
        # 자신의 아래쪽 사탕과 비교
        if boards[j][i] != boards[j + 1][i]:
            boards[j][i], boards[j + 1][i] = boards[j + 1][i], boards[j][i]
            answer = max(count(boards), answer)
            boards[j][i], boards[j + 1][i] = boards[j + 1][i], boards[j][i]     # 원상복귀

print(answer)
