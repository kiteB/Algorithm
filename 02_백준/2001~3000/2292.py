# 벌집
import sys
input = sys.stdin.readline

n = int(input())
answer = 1  # 필요한 방 개수
max_num = 1  # 방에서 가장 큰 값을 저장

if n == 1:
    print(answer)
else:
    while True:
        if n <= max_num:  # n이 max_num 보다 작거나 같으면
            print(answer)  # answer 그대로 출력
            break
        else:  # n이 max_num 보다 큰 경우
            max_num += 6 * answer
            answer += 1
