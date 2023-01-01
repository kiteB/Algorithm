# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
# 입력: 첫재 줄부터 N번째 줄까지 문자열이 주어진다. 문자열의 길이는 100을 넘지 않는다.
# 출력: 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
import sys

while True:
    try:
        case = list(str(sys.stdin.readline().rstrip('\n')))
        super_cnt = 0
        lower_cnt = 0
        digit_cnt = 0
        white_space_cnt = 0

        if not case:
            break

        for i in case:
            if i.islower():
                lower_cnt += 1
            elif i.isupper():
                super_cnt += 1
            elif i.isdigit():
                digit_cnt += 1
            elif i == ' ':
                white_space_cnt += 1
        print(lower_cnt, super_cnt,  digit_cnt, white_space_cnt)
    except EOFError:
        break