# OX 퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하기.
n = int(input())    # 테스트 케이스의 개수


for i in range(n):  # 테스트 케이스만큼 반복
    score = 0
    count = 0       # 연속된 O의 개수
    a = input()

    for j in a:
        if j == 'O':            # 'O'인 경우
            count += 1          # 'O'가 나왔으니 count + 1
            score += count      # count 만큼 더해주기
        elif j == 'X':          # 'X'인 경우
            count = 0           # count 0로 초기화

    print(score)

