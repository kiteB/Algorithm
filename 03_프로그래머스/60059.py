# 자물쇠와 열쇠 - 실패! (3시간 + α)
def rotate(arr):  # 90도 회전
    n = len(arr)
    tmp = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            tmp[x][n-1-y] = arr[y][x]
    return tmp


def solution(key, lock):
    answer = True
    keys = [key]
    m, n = len(key), len(lock)
    empty = []

    # lock에서 0인 좌표 저장하기
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                empty.append([i, j])

    # 비어 있는 칸이 없다면 True 리턴
    if not len(empty):
        return answer

    # key 리스트 90도 회전한 결과 keys에 저장하기
    for i in range(3):
        keys.append(rotate(keys[-1]))

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))