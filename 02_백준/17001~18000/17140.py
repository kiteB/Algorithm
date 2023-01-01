# 이차원 배열과 연산
import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
time = 0        # 시간
flag = False    # k인지 체크
answer = 0


def r_operation(arr):       # R 연산
    max_len = 0  # 최대 행 크기
    sorted_arr = []

    for row in arr:
        count_arr = list(sorted(Counter(row).items(), key=lambda x: [x[1], x[0]]))      # 1) 등장 횟수, 2) 같다면 숫자 순으로 오름차순 정렬

        tmp = []
        for line in count_arr:
            if line[0] != 0:   # 0이 아닌 경우만 합치기
                tmp += line

        max_len = max(max_len, len(count_arr)*2)  # 최대 행 크기 계산
        sorted_arr.append(tmp)

    for idx, val in enumerate(sorted_arr):
        if len(val) < max_len:      # 모든 행의 크기가 max_len이 되도록 0 채우기
            sorted_arr[idx] += [0] * (max_len - len(val))

    arr = sorted_arr
    return arr


while time <= 100:  # 100초 동안만 수행
    if r <= len(A) and c <= len(A[0]) and A[r-1][c-1] == k:    # A[r][c] = k인 경우인지 체크
        flag = True
        answer = time
        break

    time += 1           # 시간 +1

    # R 연산
    if len(A) >= len(A[0]):     # (행 길이) >= (열 길이)
        A = r_operation(A)
    else:   # C 연산
        reversed_A = list(map(list, zip(*A)))   # 행렬 뒤집기
        tmp = r_operation(reversed_A)
        A = list(map(list, zip(*tmp)))          # 다시 행렬 뒤집기

if flag:
    print(answer)
else:
    print(-1)