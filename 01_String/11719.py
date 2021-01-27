# 입력 받은 대로 출력하는 프로그램 작성하기
while True:
    try:
        print(input())
    except EOFError:
        break